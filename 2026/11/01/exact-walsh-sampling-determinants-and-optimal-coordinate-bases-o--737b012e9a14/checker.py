"""Exact checks for edge-Walsh Gram determinants on uniform perfect matchings.

Usage: python checker.py
No nonstandard packages, no external data.
"""
from fractions import Fraction
from itertools import combinations
from math import comb
from random import Random


def matchings(vs):
    if not vs:
        yield ()
        return
    x=vs[0]
    for j in range(1,len(vs)):
        y=vs[j]
        for rest in matchings(vs[1:j]+vs[j+1:]):
            yield ((x,y),)+rest


def determinant(a):
    """Exact integer Bareiss, including singular pivots."""
    a=[list(row) for row in a]; n=len(a)
    if n==0: return 1
    sign=1; prev=1
    for k in range(n-1):
        if a[k][k]==0:
            r=next((r for r in range(k+1,n) if a[r][k]),None)
            if r is None: return 0
            a[k],a[r]=a[r],a[k]; sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%prev==0
                a[i][j]=num//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]


def expected(n, edges, selected):
    omitted=set(edges)-set(selected)
    b=[[int(i in e) for e in omitted] for i in range(n)]
    q=[[sum(a*b for a,b in zip(b[i],b[j])) for j in range(n)] for i in range(n)]
    c=Fraction(n-2,(n-1)*(n-3))
    return c*4, determinant(q), (n-2)**(n-1)*(2*n-2)


def gram(n, selected, all_m):
    samples=[]
    for matching in all_m:
        s=set(matching)
        samples.append([1]+[1-2*int(e in s) for e in selected])
    d=len(samples[0]); g=[[sum(row[i]*row[j] for row in samples) for j in range(d)] for i in range(d)]
    return Fraction(determinant(g), len(all_m)**d)


def components_odd_unicyclic(n, omitted):
    adj=[[] for _ in range(n)]
    for u,v in omitted:
        adj[u].append(v);adj[v].append(u)
    seen=set(); b=0
    for root in range(n):
        if root in seen: continue
        stack=[root];seen.add(root);vs=[]
        while stack:
            v=stack.pop();vs.append(v)
            for w in adj[v]:
                if w not in seen:seen.add(w);stack.append(w)
        edges=sum(len(adj[v]) for v in vs)//2
        if edges!=len(vs): return None
        # A unicyclic graph is nonbipartite exactly when its cycle is odd.
        parity={vs[0]:0};stack=[vs[0]];odd=False
        while stack:
            v=stack.pop()
            for w in adj[v]:
                if w not in parity:
                    parity[w]=1-parity[v];stack.append(w)
                elif parity[w]==parity[v]:odd=True
        if not odd:return None
        b+=1
    return b


def main():
    rng=Random(827193)
    count=0; size_tests=0; max_counts={}
    for n in (6,8):
        edges=list(combinations(range(n),2))
        all_m=list(matchings(tuple(range(n))))
        if n==6:
            tests=[tuple(edges[i] for i in indices) for k in range(0,10) for indices in
                   [tuple(rng.sample(range(len(edges)),k)) for _ in range(12)]]
            # Include all critical bases under the combinatorial independent criterion.
            levels={}
            for om_idx in combinations(range(len(edges)),n):
                om=set(edges[i] for i in om_idx)
                b=components_odd_unicyclic(n,om)
                levels[b]=levels.get(b,0)+1
            assert levels[2]==10, levels
            assert sum(levels.values())==comb(15,6)
            max_counts[n]=levels
        else:
            tests=[tuple(edges[i] for i in rng.sample(range(len(edges)),k))
                   for k in (0,1,3,6,10,15,20) for _ in range(5)]
            # Add disconnected-two-component maximal designs and singular maximal designs.
            for omit in [((0,1),(1,2),(0,2),(3,4),(4,5),(5,6),(3,6),(6,7)),
                         ((0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,6),(6,7)),
                         ((0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4))]:
                tests.append(tuple(e for e in edges if e not in set(tuple(sorted(x)) for x in omit)))
        for selected in tests:
            scalar, qdet, den=expected(n,edges,selected)
            lhs=gram(n,selected,all_m)
            rhs=scalar**len(selected)*Fraction(qdet,den)
            assert lhs==rhs, (n,len(selected),lhs,rhs)
            count+=1
            if len(selected)==len(edges)-n:
                b=components_odd_unicyclic(n,set(edges)-set(selected))
                assert (qdet==(0 if b is None else 4**b)), (n,b,qdet)
                size_tests+=1
    # Independent finite counts of small odd-unicyclic components, used in
    # the all-order labelled optimizer enumeration.
    g={}
    for v in (3,4,5):
        ee=list(combinations(range(v),2))
        g[v]=sum(components_odd_unicyclic(v,set(f))==1 for f in combinations(ee,v))
    assert g=={3:1,4:12,5:162}, g
    assert comb(8,5)*g[5]+comb(8,4)//2*g[4]**2==14112
    print('PASS exact small-component optimizer census:',g,'eight-vertex count 14112')
    print('PASS exact direct Gram determinant identities:',count)
    print('PASS maximal-cardinality graph-classification tests:',size_tests)
    print('PASS exhaustive six-vertex omitted-graph census:', max_counts[6])

if __name__=='__main__': main()
