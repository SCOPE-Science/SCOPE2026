#!/usr/bin/env python3
"""Literal edge-orientation checker for convex-indegree minimizers of bicliques.

Uses adjacency-list cycle detection, not the proposed side-word characterization.
"""
from collections import defaultdict, deque
from fractions import Fraction
from math import factorial


def predicted(a,b):
    m=min(a,b); t=abs(a-b)
    return int(Fraction(factorial(m)*factorial(m+t)) * Fraction(3,2)**(m-1) * (Fraction(1,factorial(t))+Fraction(1,factorial(t+1))))


def enumerate_dag_indegrees(a,b):
    n=a+b
    edges=[(i,a+j) for i in range(a) for j in range(b)]
    for mask in range(1 << len(edges)):
        indeg=[0]*n
        out=[[] for _ in range(n)]
        for k,(u,v) in enumerate(edges):
            if (mask >> k) & 1:
                u,v=v,u
            out[u].append(v)
            indeg[v]+=1
        counts=indeg.copy()
        q=deque(v for v in range(n) if counts[v]==0)
        seen=0
        while q:
            u=q.popleft()
            seen+=1
            for v in out[u]:
                counts[v]-=1
                if counts[v]==0:
                    q.append(v)
        if seen==n:
            yield tuple(indeg)


def main():
    cases=0; orientations=0; dags=0
    fs={"square": lambda z:z*z, "cube": lambda z:z*z*z, "exp": lambda z:2**z, "shifted_square":lambda z:z*z-7*z}
    for a,b in [(a,b) for a in range(1,5) for b in range(a,5)] + [(1,5),(2,5),(3,5)]:
        all_degrees=list(enumerate_dag_indegrees(a,b))
        dags+=len(all_degrees)
        orientations+=1 << (a*b)
        m=min(a,b);t=abs(a-b)
        indegree_pattern=tuple(sorted([0]+[i for i in range(1,m) for _ in range(2)]+[m]*(t+1)))
        expected_count=predicted(a,b)
        for name,f in fs.items():
            val=min(sum(map(f,ds)) for ds in all_degrees)
            expected_val=f(0)+2*sum(f(i) for i in range(1,m))+(t+1)*f(m)
            optimizers=[ds for ds in all_degrees if sum(map(f,ds))==val]
            assert val==expected_val,(a,b,name,'value',val,expected_val)
            assert len(optimizers)==expected_count,(a,b,name,'number',len(optimizers),expected_count)
            assert all(tuple(sorted(ds))==indegree_pattern for ds in optimizers), (a,b,name,'pattern')
            cases+=1
        print(f'OK a={a},b={b}: DAGs={len(all_degrees)}, optimizers={expected_count}')
    print(f'PASS: {cases} strictly-convex cost tests, {orientations} edge assignments, {dags} acyclic orientations.')
if __name__=='__main__': main()
