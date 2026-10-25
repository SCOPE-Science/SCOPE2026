"""Reproducible exact checks for the Gauss--Padé complete multipartite theorem.

Run: python verify_pade.py (requires SymPy).
All finite graph matrices use integer/rational arithmetic; the proof for arbitrary
part sizes is in RESULT.md and does not rely on the finite tests.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
import sympy as s

def solve_inverse(A):
    n = len(A)
    B = [[F(A[i][j]) for j in range(n)] + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        t = next(k for k in range(i, n) if B[k][i])
        B[i], B[t] = B[t], B[i]
        z = B[i][i]
        B[i] = [v/z for v in B[i]]
        for k in range(n):
            if k != i:
                z = B[k][i]
                if z: B[k] = [u-z*v for u,v in zip(B[k], B[i])]
    return [row[n:] for row in B]

def mul(A,B):
    n=len(A); return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def graph_laplacian(parts):
    n=sum(parts); owners=[i for i,m in enumerate(parts) for _ in range(m)]
    return [[F(n-parts[owners[i]]) if i==j else F(-int(owners[i]!=owners[j]))
             for j in range(n)] for i in range(n)],owners

def pade(L,h):
    n=len(L); L2=mul(L,L)
    plus=[[12*int(i==j)+6*h*L[i][j]+h*h*L2[i][j] for j in range(n)] for i in range(n)]
    minus=[[12*int(i==j)-6*h*L[i][j]+h*h*L2[i][j] for j in range(n)] for i in range(n)]
    return mul(minus,solve_inverse(plus))

def main():
    h,N,m=s.symbols('h N m',positive=True)
    d=lambda z:z*z+6*z+12
    R=lambda z:(z*z-6*z+12)/d(z)
    a=N-m
    assert s.factor(1-R(N*h)-12*N*h/d(N*h)) == 0
    b=s.factor((1-R(N*h))/N+(R(N*h)-R(a*h))/m)
    goal=12*a*h*h*((2*N-m)*h+6)/(d(a*h)*d(N*h))
    assert s.factor(b-goal)==0
    p4=s.Matrix([[1,-1,0,0],[-1,2,-1,0],[0,-1,2,-1],[0,0,-1,1]])
    r4=(12*s.eye(4)-6*h*p4+h*h*p4**2)*(12*s.eye(4)+6*h*p4+h*h*p4**2).inv()
    denom=2*(h*h+3*h+3)*(h**4+12*h**3+54*h*h+72*h+36)
    targets={(0,1):-3*h*(h**4-6*h**3-60*h*h-108*h-72)/denom,
             (0,2):9*h*h*(h**3+6*h*h+16*h+12)/denom,
             (0,3):3*h**3*(5*h*h+18*h+12)/denom,
             (1,2):3*h*(h**4+6*h**3+24*h*h+72*h+72)/denom}
    for (i,j),formula in targets.items():assert s.cancel(r4[i,j]-formula)==0
    graph_count=0;entry_count=0
    for parts_len in range(2,5):
        for parts in combinations_with_replacement(range(1,5),parts_len):
            if sum(parts)>11:continue
            L,owners=graph_laplacian(parts)
            n=len(L)
            for v in (F(1,17),F(1,1),F(13,2),F(101,1)):
                T=pade(L,v)
                dn=d
                for i in range(n):
                    assert sum(T[i])==1
                    for j in range(n):
                        assert T[i][j]>0
                        if i!=j:
                            if owners[i]!=owners[j]:
                                formula=F(12)*v/F((n*v)**2+6*n*v+12)
                            else:
                                aa=n-parts[owners[i]]
                                formula=F(12)*aa*v*v*((2*n-parts[owners[i]])*v+6)/(
                                    ((aa*v)**2+6*aa*v+12)*((n*v)**2+6*n*v+12))
                            assert T[i][j]==formula
                        entry_count+=1
            graph_count+=1
    P4=[[F(p4[i,j]) for j in range(4)] for i in range(4)]
    assert pade(P4,F(11))[0][1]>0
    assert pade(P4,F(12))[0][1]<0
    assert pade(P4,F(100))[0][1]<0
    print('VERIFY_OK: scalar and multipartite symbolic identities, 4 symbolic path entries,',graph_count,
          'multipartite graphs,',entry_count,'exact rational matrix entries, path sign transition')
if __name__=='__main__':main()
