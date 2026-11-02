"""Exact finite-tree verification of the fringe/degree factorization.
No external packages. The proof of asymptotic assertions is analytic, not finite enumeration.
"""
from itertools import product
from fractions import Fraction
from collections import Counter
from math import factorial


def stirling_cycles(m):
    old = [1]
    for r in range(1, m+1):
        new = [0]*(r+1)
        for k,x in enumerate(old):
            new[k] += (r-1)*x
            new[k+1] += x
        old = new
    return old


def tail(n, j, s):
    if s < 1:
        return Fraction(1)
    if s > n-j+1:
        return Fraction(0)
    z = Fraction(1)
    for r in range(s-1):
        z *= Fraction(n-j-r, n-1-r)
    return z


def check():
    checked = 0
    for n in range(2,9):
        obs = {j:Counter() for j in range(2,n+1)}
        total = 0
        for parents in product(*(range(1,v) for v in range(2,n+1))):
            par=[0,0,*parents]
            deg=[0]*(n+1)
            sz=[1]*(n+1)
            for v in range(2,n+1):
                deg[par[v]]+=1
            for v in range(n,1,-1):
                sz[par[v]]+=sz[v]
            for j in range(2,n+1):
                obs[j][(sz[j],deg[j])]+=1
            total+=1
        assert total==factorial(n-1)
        for j in range(2,n+1):
            for s in range(1,n-j+2):
                mass = tail(n,j,s) - tail(n,j,s+1)
                cycles=stirling_cycles(s-1)
                for d in range(s):
                    actual=Fraction(obs[j][(s,d)],total)
                    expected=mass*Fraction(cycles[d],factorial(s-1))
                    assert actual==expected,(n,j,s,d,actual,expected)
                    checked+=1
                assert sum(obs[j][(s,d)] for d in range(s))==mass*total
        print('n',n,'recursive trees',total,'joint probabilities verified')
    print('PASS',checked,'exact joint probabilities; matching conditional law and beta-binomial tail')

if __name__=='__main__':
    check()
