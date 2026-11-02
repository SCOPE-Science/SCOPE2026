#!/usr/bin/env python3
"""Independent exact graph-distance verification of the wheel shattering theorem."""
from collections import Counter
from itertools import combinations
from math import comb


def wheel_adjacency(m):
    # Rim 0,...,m-1; universal vertex m.
    adj=[set() for _ in range(m+1)]
    for i in range(m):
        for j in ((i+1)%m, (i-1)%m, m):
            adj[i].add(j);adj[j].add(i)
    return adj


def distances(adj):
    n=len(adj); ans=[]
    for a in range(n):
        d=[n+1]*n;d[a]=0;front=[a]
        for x in front:
            for y in adj[x]:
                if d[y]>d[x]+1:
                    d[y]=d[x]+1;front.append(y)
        ans.append(d)
    return ans


def independent_graph_convexity(m):
    adj=wheel_adjacency(m);dist=distances(adj); n=m+1
    concept=[]
    for mask in range(1<<n):
        vertices=[v for v in range(n) if mask>>v&1]
        ok=True
        for i,j in combinations(vertices,2):
            if any(dist[i][p]+dist[p][j]==dist[i][j] and not(mask>>p&1) for p in range(n)):
                ok=False;break
        if ok: concept.append(mask)
    return concept


def predicted_concepts(m):
    allmask=(1<<m)-1;h=1<<m
    result={0}|{1<<i for i in range(m)}|{(1<<i)|(1<<((i+1)%m)) for i in range(m)}
    for x in range(1<<m):
        if all(not((x>>i&1) and (x>>((i+2)%m)&1) and not(x>>((i+1)%m)&1)) for i in range(m)):
            result.add(x|h)
    return result


def predicted_shattered_supports(m):
    hub=1<<m;ret=set()
    for x in range(1<<m):
        if all(not((x>>i&1) and (x>>((i+1)%m)&1) and (x>>((i+2)%m)&1)) for i in range(m)):
            ret.add(x)
    ret.add(hub)
    for i in range(m):
        ret.add(hub | (1<<i))
        ret.add(hub | (1<<i) | (1<<((i+1)%m)))
    return ret


def independently_shattered(concepts,m):
    n=m+1
    result=set()
    for support in range(1<<n):
        if len({h&support for h in concepts})==(1<<support.bit_count()):
            result.add(support)
    return result


def coefficient_formula(m,k):
    j=m-k
    if j==0:return 0
    coeff=0
    for b in range(j+1):
        a=k-2*b
        if 0<=a<=j-b:
            coeff+=comb(j,b)*comb(j-b,a)
    assert m*coeff%j==0
    return m*coeff//j


def run():
    for m in range(5,12):
        concepts=set(independent_graph_convexity(m))
        assert concepts==predicted_concepts(m),('convexity mismatch',m)
        brute=independently_shattered(concepts,m)
        predicted=predicted_shattered_supports(m)
        assert brute==predicted,('shattering mismatch',m,brute^predicted)
        spectrum=Counter(x.bit_count() for x in brute)
        for k in range(m+2):
            expected=coefficient_formula(m,k) if k<=m else 0
            if k==1:expected+=1
            if k==2 or k==3: expected+=m
            assert spectrum[k]==expected,('coefficient mismatch',m,k,spectrum[k],expected)
        assert max(spectrum)==2*m//3,('VC mismatch',m)
        print(f'WHEEL_EXHAUSTIVE_GRAPH_DISTANCE_PASS rim={m} convex_sets={len(concepts)} shattered={len(brute)} VC={max(spectrum)} spectrum={dict(sorted(spectrum.items()))}')
    for m in range(12,21):
        theoretical=predicted_shattered_supports(m)
        spectrum=Counter(x.bit_count() for x in theoretical)
        assert max(spectrum)==2*m//3
        for k in range(m+2):
            expected=coefficient_formula(m,k) if k<=m else 0
            if k==1: expected+=1
            if k in (2,3): expected+=m
            assert spectrum[k]==expected
        print(f'WHEEL_COEFFICIENT_FORMULA_PASS rim={m} VC={max(spectrum)}')
    print('ALL_WHEEL_SHATTERING_CHECKS_PASS')

if __name__=='__main__':run()
