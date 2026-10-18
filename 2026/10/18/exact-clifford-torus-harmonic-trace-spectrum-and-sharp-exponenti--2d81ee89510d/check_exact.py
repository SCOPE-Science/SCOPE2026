"""Exact rational test of Clifford-torus restriction eigenvalues by independent methods.
Methods: normalized Hopf/Jacobi basis and Gegenbauer/SU(2) addition kernel on the torus.
"""
from collections import defaultdict
from fractions import Fraction as F
from math import comb, factorial

def hopf_value(a,b,L):
    if a+b>=L: return F(0)
    val=F(0)
    for j in range((L-1-a-b)//2+1):
        norm=F((2*j+a+b+1)*factorial(j)*factorial(j+a+b), factorial(j+a)*factorial(j+b))
        # Jacobi at x=0 = 2^-j sum_{r=0}^j binom(j+b,j-r) binom(j+a,r)*(-1)^r
        P=F(sum(((-1)**r)*comb(j+b,j-r)*comb(j+a,r) for r in range(j+1)),2**j)
        val += norm*P*P/F(2**(a+b))
    return val

def add(A,B):
    C=defaultdict(F)
    for z,v in A.items():C[z]+=v
    for z,v in B.items():C[z]+=v
    return dict(C)
def mul_u(A):
    C=defaultdict(F)
    for (m,n),v in A.items():
        for dm,dn in [(1,0),(-1,0),(0,1),(0,-1)]:C[(m+dm,n+dn)]+=v/F(4)
    return dict(C)
def scalar(A,s):return {z:v*s for z,v in A.items()}
def torus_kernel(L):
    u0={(0,0):F(1)}
    u1=scalar(mul_u(u0),2)
    K={}
    for r in range(L):
        if r==0: U=u0
        elif r==1: U=u1
        else:
            u0,u1=u1,add(scalar(mul_u(u1),2),scalar(u0,-1));U=u1
        K=add(K,scalar(U,r+1))
    return K

def main():
    for L in range(1,10):
        K=torus_kernel(L)
        assert sum(K.values())==sum((r+1)**2 for r in range(L)),(L,'trace identity')
        diamond={(m,n) for m in range(-L+1,L) for n in range(-L+1,L) if abs(m)+abs(n)<L}
        assert set(K)==diamond,(L,len(K),len(diamond))
        for (m,n),v in K.items():
            w=hopf_value(abs(m),abs(n),L)
            assert v==w,(L,m,n,v,w)
        mn=min(K.values());assert mn==F(L,2**(L-1))
        min_eq=[q for q,v in K.items() if v==mn]
        if L==2: assert set(min_eq)==diamond
        if L>=3: assert set(min_eq)=={(L-1,0),(-L+1,0),(0,L-1),(0,-L+1)}
        print('L=',L,'rank=',len(K),'domain=',sum((r+1)**2 for r in range(L)),
              'min=',mn,'min multiplicity=',len(min_eq),'max=',max(K.values()))
if __name__=='__main__':main()
