#!/usr/bin/env python3
"""Exact checks for a two-stage factorized randomized row-action iteration."""
from fractions import Fraction as Q
from itertools import product
from math import exp, log, log1p


def transport_maximal(p, q):
    assert sum(p) == sum(q) == 1
    m = len(p)
    c = [min(p[i], q[i]) for i in range(m)]
    leftover = 1 - sum(c)
    tab = [[Q(0) for _ in range(m)] for _ in range(m)]
    for i in range(m):
        tab[i][i] = c[i]
    if leftover:
        for i in range(m):
            for j in range(m):
                tab[i][j] += (p[i]-c[i]) * (q[j]-c[j])/leftover
    return tab


def exact_unfinished(p, q, joint, t):
    m = len(p)
    return [(1-p[i])**t + (p[i]-joint[i][i]) * sum(
        (1-p[i])**(s-1) * (1-q[i])**(t-s)
        for s in range(1,t+1)) for i in range(m)]


def brute_source_updates(a,b,rhs,joint,t):
    m=len(a)
    left=[Q(0)]*m
    options=[(i,j) for i in range(m) for j in range(m) if joint[i][j]>0]
    target=[rhs[i]/a[i]/b[i] for i in range(m)]
    for choices in product(options,repeat=t):
        x=[Q(0)]*m; z=[Q(0)]*m; wt=Q(1)
        for i,j in choices:
            wt*=joint[i][j]
            # Source RK-RK: first project a_i*x_i=rhs_i,
            # then project b_j*z_j=x_j, using UPDATED x_j.
            x[i]+=(rhs[i]-a[i]*x[i])/a[i]
            z[j]+=(x[j]-b[j]*z[j])/b[j]
        for h in range(m):
            left[h]+=wt*(z[h]-target[h])**2
    return left


def test():
    tests=0
    for a,b,max_t in [([1,2],[3,1],6),([1,2,3],[3,2,1],4),([1,1,2,2],[2,1,2,1],3)]:
        a,b=list(map(Q,a)),list(map(Q,b));m=len(a)
        p=[u*u/sum(v*v for v in a) for u in a]
        q=[u*u/sum(v*v for v in b) for u in b]
        indip=[[u*v for v in q] for u in p]
        optimal=transport_maximal(p,q)
        laws=[indip,optimal, [[(x+y)/2 for x,y in zip(r,s)] for r,s in zip(indip,optimal)]]
        rhs=[a[i]*b[i]*Q(i+1) for i in range(m)]
        goal=[Q(i+1) for i in range(m)]
        for law in laws:
            assert [sum(row) for row in law]==p
            assert [sum(law[i][j] for i in range(m)) for j in range(m)]==q
            for t in range(max_t+1):
                expected=exact_unfinished(p,q,law,t)
                brute=brute_source_updates(a,b,rhs,law,t)
                assert brute==[goal[i]**2*expected[i] for i in range(m)],(a,b,t,law,brute,expected)
                tests+=m
        # Maximal diagonal coupling dominates independent and any midpoint coupling.
        for t in range(1,max_t+1):
            e1=exact_unfinished(p,q,indip,t)
            e2=exact_unfinished(p,q,optimal,t)
            assert all(u>v for u,v in zip(e1,e2))
            tests+=m
    for m in range(2,19):
        r=Q(m-1,m);p=Q(1,m)
        for t in range(0,45):
            for theta in [Q(0),Q(1,10),Q(1,2),Q(9,10),Q(1)]:
                d=theta*p+(1-theta)*p*p
                lhs=r**t+(p-d)*sum(r**(t-1) for _ in range(t))
                rhs=r**t*(1+(1-theta)*Q(t,m))
                assert lhs==rhs
                tests+=1
    for m in [2000,20000,200000]:
        L=log(m)
        for theta in [0,0.5,1,1-1/L,1-1/L**0.5]:
            s=0.7
            eps = 1-theta
            center = L
            for _ in range(30):
                center = L + log1p(eps*center)
            assert abs(center-L-log1p(eps*center)) < 1e-10
            t=int(m*(center+s))
            expected=m*(1-1/m)**t*(1+eps*t/m)
            corrected = exp(-s) * (1 + eps*s/(1+eps*center))
            assert abs(expected-corrected) < 0.005, (m,theta,expected,corrected)
            tests+=1
    print(f"PASS: {tests} exact component comparisons or finite asymptotic checks")

if __name__=='__main__':test()
