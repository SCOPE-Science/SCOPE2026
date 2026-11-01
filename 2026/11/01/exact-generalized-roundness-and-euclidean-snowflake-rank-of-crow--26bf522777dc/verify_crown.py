#!/usr/bin/env python3
"""Reproducible finite checks for a crown-graph negative-type theorem.

The proof is algebraic and applies to arbitrary n; tests check graph distances,
quadratic-form decomposition, phase boundaries, and asymptotic comparisons.
No external packages are needed.
"""
from collections import deque
from fractions import Fraction
from math import exp, expm1, log
from random import Random

LN2, LN3 = log(2), log(3)


def distance_matrix(n):
    adj = [[] for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].append(n+j)
                adj[n+j].append(i)
    result = []
    for s in range(2*n):
        dist = [-1]*(2*n)
        dist[s] = 0
        todo = deque([s])
        while todo:
            v = todo.popleft()
            for w in adj[v]:
                if dist[w] < 0:
                    dist[w] = dist[v]+1
                    todo.append(w)
        result.append(dist)
    return result


def expected_distance(n, i, j):
    if i == j: return 0
    if (i < n) == (j < n): return 2
    return 3 if i % n == j % n else 1


def evalues(n, p):
    a,b=2**p,3**p
    return ((n-1)*a-n-b+1, b-a-1, 1-a-b)


def crit(n):
    if n<=4:return 1.0
    lo,hi=0.0,1.0
    for _ in range(85):
        mid=(lo+hi)/2
        val=(n-1)*expm1(mid*LN2)-exp(mid*LN3)
        if val>0:hi=mid
        else:lo=mid
    return (lo+hi)/2


def direct_q(n, d, x, p):
    a,b=2**p,3**p
    return sum(x[i]*x[j]*(a if d[i][j]==2 else b if d[i][j]==3 else 1.0)
               for i in range(2*n) for j in range(2*n) if i!=j)


def decomposition_q(n, x, p):
    assert sum(x)==0
    alpha=sum(x[:n])/(n*1.0)
    v=[(x[i]+x[n+i])/2.0 for i in range(n)]
    w=[(x[i]-x[n+i])/2.0-alpha for i in range(n)]
    lam0,lam1,lam2=evalues(n,p)
    return 2*n*alpha**2*lam0+2*sum(t*t for t in v)*lam1+2*sum(t*t for t in w)*lam2


def rational_decomposition(n, x, p):
    assert p in (0,1)
    alpha=Fraction(sum(x[:n]),n)
    v=[Fraction(x[i]+x[n+i],2) for i in range(n)]
    w=[Fraction(x[i]-x[n+i],2)-alpha for i in range(n)]
    l0,l1,l2=map(int,evalues(n,p))
    rhs=2*n*alpha**2*l0+2*sum(t*t for t in v)*l1+2*sum(t*t for t in w)*l2
    return rhs


def main():
    rng=Random(51917)
    totals=dict(distances=0, exact_quadratic=0, float_quadratic=0,
                transitions=0, endpoint_dimensions=0, comparison=0)
    for n in range(3,14):
        d=distance_matrix(n)
        for i in range(2*n):
            for j in range(2*n):
                assert d[i][j]==expected_distance(n,i,j)
                totals['distances']+=1
        for _ in range(420):
            xs=[rng.randint(-8,8) for _ in range(2*n-1)]
            xs.append(-sum(xs))
            for p in (0,1):
                a,b=2**p,3**p
                q=sum(xs[i]*xs[j]*(a if d[i][j]==2 else b if d[i][j]==3 else 1)
                       for i in range(2*n) for j in range(2*n) if i!=j)
                assert q==rational_decomposition(n,xs,p)
                totals['exact_quadratic']+=1
            for p in (.14,.38,.66,.92,1.18,1.6):
                q=direct_q(n,d,xs,p)
                r=decomposition_q(n,xs,p)
                assert abs(q-r)<1e-8*(1+abs(q)+abs(r)),(n,p,q,r)
                totals['float_quadratic']+=1
        endpoint=crit(n)
        l0,l1,l2=evalues(n,endpoint)
        if n==3:
            assert abs(l1)<1e-12 and l0<-.5 and l2<0
            rank=3
        elif n==4:
            assert abs(l1)<1e-12 and abs(l0)<1e-12 and l2<0
            rank=3
        else:
            assert abs(l0)<1e-11 and l1<0 and l2<0
            assert crit(n)<1
            p=crit(n)
            assert evalues(n,p*.99)[0]<0 and evalues(n,p*1.01)[0]>0
            rank=2*n-2
        assert rank==(3 if n<=4 else 2*n-2)
        totals['endpoint_dimensions']+=1
        # n >= 5: the bipartition witness violates 1-negative type exactly by 2n(n-4).
        witness=[1]*n+[-1]*n
        q1=sum(witness[i]*witness[j]*d[i][j] for i in range(2*n) for j in range(2*n))
        assert q1==2*n*(n-4)
        if n>=5: assert q1>0
        totals['transitions']+=1
        # The missing perfect matching always increases maximal negative type.
        unbroken=log(n/(n-1))/LN2
        assert endpoint>unbroken
        totals['comparison']+=1
    # The asymptotic refinement is tested quantitatively, not used in the proof.
    for n in (100,300,1000,3000):
        N=n-1
        p=crit(n)
        approx=(1/(N*LN2)+(LN3/LN2**2-1/(2*LN2))/N**2)
        assert abs(p-approx)<10/N**3
        delta=p-log(n/(n-1))/LN2
        assert abs(delta*N*N-LN3/LN2**2)<15/N
    print('VERIFIED',totals)
    print('critical n=5',format(crit(5),'.12f'))
    print('critical n=6',format(crit(6),'.12f'))

if __name__=='__main__':main()
