#!/usr/bin/env python3
"""Independent small-instance checks for paired-coalition graphs of bicliques.

Only a finite check: the mathematical proof of the infinite theorem is separate.
Does not use network matching libraries or analytic assumptions about imbalances
when computing the paired domination predicate.
"""
from collections import defaultdict, Counter
from fractions import Fraction
from functools import lru_cache
from math import factorial, isqrt


def partitions(n):
    # Enumerate each unlabeled set partition exactly once.
    if n < 1:
        yield ()
        return
    blocks = [[0]]
    def rec(k):
        if k == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for b in blocks:
            b.append(k)
            yield from rec(k + 1)
            b.pop()
        blocks.append([k])
        yield from rec(k + 1)
        blocks.pop()
    yield from rec(1)


def independent_paired_domination(m, n):
    # Construct an actual graph and implement dominating+perfect matching checks.
    N = m+n
    adj = tuple((sum(1 << j for j in range(m,N)) if i < m else
                 sum(1 << j for j in range(m))) for i in range(N))
    full = (1 << N)-1
    @lru_cache(maxsize=None)
    def has_matching(mask):
        if mask == 0:
            return True
        if mask.bit_count() % 2:
            return False
        i = (mask & -mask).bit_length()-1
        friends = adj[i] & mask
        while friends:
            bit = friends & -friends
            if has_matching(mask ^ (1<<i) ^ bit):
                return True
            friends -= bit
        return False
    @lru_cache(maxsize=None)
    def pds(mask):
        if not mask:
            return False
        if any(not (mask & ((1<<i)|adj[i])) for i in range(N)):
            return False
        return has_matching(mask)
    return pds


def examine(m, n):
    N=m+n
    pds=independent_paired_domination(m,n)
    counts=Counter()
    total=0
    for partition in partitions(N):
        masks=[sum(1<<i for i in b) for b in partition]
        if any(pds(mask) for mask in masks):
            continue
        k=len(masks)
        edges=[]
        degrees=[0]*k
        for i in range(k):
            for j in range(i+1,k):
                if pds(masks[i]|masks[j]):
                    edges.append((i,j)); degrees[i]+=1; degrees[j]+=1
        if any(d==0 for d in degrees):
            continue
        # Count components in independently constructed coalition graph.
        comps=[]; seen=set()
        for root in range(k):
            if root in seen:
                continue
            pending=[root];seen.add(root);vertices=[]
            while pending:
                v=pending.pop();vertices.append(v)
                for u,w in edges:
                    a=w if u==v else u if w==v else -1
                    if a>=0 and a not in seen:
                        seen.add(a);pending.append(a)
            comps.append(vertices)
        # Directly test that every component is a complete bipartite graph.
        edge_set={frozenset(e) for e in edges}
        for comp in comps:
            signs={};signs[comp[0]]=0;todo=[comp[0]]
            while todo:
                v=todo.pop()
                for w in comp:
                    if frozenset((v,w)) in edge_set:
                        if w in signs:
                            assert signs[w]!=signs[v]
                        else:
                            signs[w]=1-signs[v];todo.append(w)
            assert len(signs)==len(comp)
            assert all((frozenset((u,v)) in edge_set) == (signs[u]!=signs[v])
                       for x,u in enumerate(comp) for v in comp[x+1:])
        c=len(comps)
        assert c*(c+1)//2 <= min(m,n)
        counts[(c,k)] += 1
        total += 1
    return counts


def expected_components(m,n):
    return (isqrt(8*min(m,n)+1)-1)//2


def analytic_polynomial(m,n):
    # Independent coefficient extraction from the formal exponential generating
    # function. Rational weights absorb unlabeled blocks; multiply by m! n!.
    D=min(m,n)
    E={(0,0,0,0):Fraction(1)}
    def multiply(a,b):
        v=defaultdict(Fraction)
        for (i,j,c,k),x in a.items():
            for (I,J,C,K),y in b.items():
                if i+I<=m and j+J<=n:
                    v[(i+I,j+J,c+C,k+K)] += x*y
        return dict(v)
    def nonempty(d,positive):
        atom={}
        for t in range(min(m,n)+1):
            a,b=(d+t,t) if positive else (t,d+t)
            if a<=m and b<=n:
                atom[(a,b,0,1)]=Fraction(1,factorial(a)*factorial(b))
        z={};power={(0,0,0,0):Fraction(1)}
        for k in range(1,m+n+1):
            power=multiply(power,atom)
            if not power: break
            fac=factorial(k)
            for key,val in power.items(): z[key]=z.get(key,Fraction(0))+val/fac
        return z
    for d in range(1,D+1):
        pos=nonempty(d,True)
        neg=nonempty(d,False)
        component=multiply(pos,neg)
        shifted={(i,j,1,k):v for (i,j,c,k),v in component.items()}
        shifted[(0,0,0,0)]=Fraction(1)
        E=multiply(E,shifted)
    out={}
    for (i,j,c,k),v in E.items():
        if i==m and j==n:
            count=v*factorial(m)*factorial(n)
            assert count.denominator==1
            out[(c,k)]=int(count)
    return Counter(out)


def main():
    for m in range(1,6):
        for n in range(1,6):
            if m+n>10:
                continue
            direct=examine(m,n)
            formula=analytic_polynomial(m,n)
            assert direct==formula, (m,n,direct,formula)
            maxc=max(c for c,k in direct)
            assert maxc==expected_components(m,n),(m,n,maxc)
            print(f'OK K_{{{m},{n}}}: {sum(direct.values())} partitions; max components {maxc}')
    for c in range(1,5):
        n=c*(c+1)//2
        if n<=5:
            a=analytic_polynomial(n,n)
            actual=sum(v for (C,k),v in a.items() if C==c)
            expected=(factorial(n)//__import__('math').prod(factorial(j) for j in range(1,c+1)))**2
            assert actual==expected,(c,actual,expected)
            print(f'OK triangular n={n}: {actual} maximum-fragmentation partitions')
    # Larger triangular case: formal-series check only, not exhaustive partitions.
    formal=analytic_polynomial(6,6)
    assert sum(v for (C,k),v in formal.items() if C==3)==3600
    print('OK triangular n=6: 3600 maximum-fragmentation partitions (formal-series check)')
    print('ALL_FINITE_CHECKS_PASSED')

if __name__=='__main__':
    main()
