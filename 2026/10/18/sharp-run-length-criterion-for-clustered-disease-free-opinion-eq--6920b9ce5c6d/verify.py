"""Finite exact checks for community-opinion epidemic thresholds.
The unrestricted statements are established analytically in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import cos, pi, sqrt


def graph(m):
    n=4*m
    A=[[0]*n for _ in range(n)]
    for j in range(m):
        for u in range(4*j,4*j+4):
            for v in range(u+1,4*j+4):
                A[u][v]=A[v][u]=1
    for j in range(m-1):
        u,v=4*j,4*(j+1)
        A[u][v]=A[v][u]=1
    return A


def rho_power(A, steps=3000):
    n=len(A)
    if n==0:
        return 0.
    x=[1.0]*n
    for _ in range(steps):
        y=[sum(a*b for a,b in zip(row,x)) for row in A]
        t=max(y)
        if not t:
            return 0.
        x=[a/t for a in y]
    y=[sum(a*b for a,b in zip(row,x)) for row in A]
    return sum(xi*yi for xi,yi in zip(x,y))/sum(xi*xi for xi in x)


def radius_formula(ell):
    if ell==0:
        return 0.
    t=2*cos(pi/(ell+1))
    return (2+t+sqrt((2-t)**2+12))/2


def longest_negative(bits):
    k=best=0
    for s in bits:
        k=k+1 if s==-1 else 0
        best=max(k,best)
    return best


def at_corner(A,bits,eps=F(1,2),omega=F(1,2),alpha=F(1,2),phi=F(1,2),lam=F(4,25)):
    n=len(A)
    opinions=[F(bits[i//4]) for i in range(n)]
    infected=[F(0) for _ in range(n)]
    vacc=[F(1,1)/(1+phi) if opinions[i]==1 else F(0) for i in range(n)]
    O2=[]; I2=[]; V2=[]
    for i,row in enumerate(A):
        degree=sum(row)
        outside=opinions[i]+eps*sum(F(row[j])*opinions[j] for j in range(n))/degree+omega*sum(F(row[j])*infected[j] for j in range(n))/degree
        O2.append(max(F(-1),min(F(1),outside)))
        gamma=(1+opinions[i])/2
        q=F(1)
        for j,edge in enumerate(row):
            q*=1-lam*edge*infected[j]
        q=1-q
        S=1-infected[i]-vacc[i]
        I2.append((1-alpha)*infected[i]+S*(1-gamma)*q)
        V2.append((1-phi)*vacc[i]+S*gamma)
        assert opinions[i]*sum(row[j]*opinions[j] for j in range(n))>=1
    assert O2==opinions and I2==infected and V2==vacc


def main():
    total=0
    for m in range(1,8):
        A=graph(m)
        for bits in product((-1,1),repeat=m):
            total+=1
            if m<=5:
                at_corner(A,bits)
            neg=[4*j+k for j in range(m) if bits[j]==-1 for k in range(4)]
            H=[[A[i][j] for j in neg] for i in neg]
            ell=longest_negative(bits)
            computed=rho_power(H)
            predicted=radius_formula(ell)
            assert abs(computed-predicted)<1e-10,(m,bits,computed,predicted)
            stable=F(4,25)*computed < F(1,2)
            assert stable == (ell<=1)
        for q in range(0,m+1):
            expected=sum(longest_negative(x)<=q for x in product((-1,1),repeat=m))
            seq=[1]
            for n in range(1,m+1):
                seq.append(2**n if n<=q else sum(seq[n-j] for j in range(1,q+2)))
            assert seq[m]==expected,(m,q,seq[m],expected)
    # Rigorous exact, arithmetic-only witness inequalities.
    #  (4/25)*3 < 1/2 < (4/25)*(3+sqrt(13))/2.
    assert F(12,25)<F(1,2)
    assert F(13,4)**2 < 13  # implies sqrt(13)>13/4
    assert F(2,25)*(3+sqrt(13))>F(1,2)
    one=(-1,1,-1,1)
    two=(-1,-1,1,1)
    assert sum(x==1 for x in one)==sum(x==1 for x in two)==2
    assert longest_negative(one)==1 and longest_negative(two)==2
    assert (F(2,4)*F(1,1)/(1+F(1,2)))==F(1,3)
    assert sum(longest_negative(x)<=1 for x in product((-1,1),repeat=4))==8
    print(f'VERIFY_OK: {total} labeled spectral checks, 62 exact pinned equilibrium checks, run recurrence and equal-coverage stability reversal')

if __name__=='__main__':
    main()
