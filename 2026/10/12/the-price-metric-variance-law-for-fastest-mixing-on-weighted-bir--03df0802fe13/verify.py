#!/usr/bin/env python3
"""Exact-arithmetic spot checks for an optimal spectral-gap formula on priced paths."""
from fractions import Fraction as F
from random import Random

def check(m,g):
    n=len(m)
    p=[F(v,sum(m)) for v in m]
    P=[sum(p[:i+1]) for i in range(n-1)]
    G=[[P[min(i,j)]*(1-P[max(i,j)]) for j in range(n-1)] for i in range(n-1)]
    Fv=[sum(G[i][j]*g[j] for j in range(n-1)) for i in range(n-1)]
    D=sum(g[i]*Fv[i] for i in range(n-1))
    assert D>0 and all(v>0 for v in Fv)
    w=[Fv[i]/(D*g[i]) for i in range(n-1)]
    assert sum(w[i]*g[i]*g[i] for i in range(n-1))==1
    s=[F(0)]
    for a in g:s.append(s[-1]+a)
    mu=sum(p[i]*s[i] for i in range(n))
    x=[s[i]-mu for i in range(n)]
    assert sum(p[i]*x[i] for i in range(n))==0
    assert sum(p[i]*x[i]*x[i] for i in range(n))==D
    for i in range(n):
        lhs=(w[i-1]*g[i-1] if i else 0)-(w[i]*g[i] if i<n-1 else 0)
        assert lhs==p[i]*x[i]/D
    # Test exact Gram-factorization identity with 8 distinct, sign-changing edge signals.
    for k in range(8):
        d=[F(((-1)**(i+k))*(i+1)**((k%3)+1)+k-3) for i in range(n-1)]
        energy=sum(w[i]*d[i]**2 for i in range(n-1))-sum(d[i]*G[i][j]*d[j] for i in range(n-1) for j in range(n-1))/D
        rhs=sum(G[i][j]*g[i]*g[j]*(d[i]/g[i]-d[j]/g[j])**2 for i in range(n-1) for j in range(n-1))/(2*D)
        assert energy==rhs and rhs>=0
    return D,w

def main():
    rng=Random(901122)
    cases=0
    for n in range(2,12):
        for _ in range(80):
            m=[rng.randrange(1,15) for _ in range(n)]
            g=[rng.randrange(1,13) for _ in range(n-1)]
            check(m,g); cases+=1
    D,w=check([1,2,3,4],[1,2,3]);assert D==F(101,20) and w==[F(7,101),F(17,202),F(20,303)]
    print(f'VERIFY_OK {cases+1} exact positive-mass/price instances; {8*(cases+1)} exact ground-state quadratic-identity checks; budgets/eigenrelations')

if __name__=='__main__': main()
