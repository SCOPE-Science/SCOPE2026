#!/usr/bin/env python3
"""Reproduce the exact finite Paley secure-total domination computation.
Run: python3 check_python.py > verified_python.json
"""
import itertools,json
from collections import Counter,deque

def analysis(p):
    Q=sorted({(a*a)%p for a in range(1,p)})
    A=[sum(1<<j for j in range(p) if ((j-i)%p) in Q) for i in range(p)]
    allmask=(1<<p)-1
    def total(s):
        return all((s & A[u])!=0 for u in range(p))
    def secure(s):
        if not total(s):return False
        for u in range(p):
            if s & (1<<u):continue
            candidates=[v for v in range(p) if (s&(1<<v)) and (A[u]&(1<<v))]
            if not any(total(s ^ (1<<u) ^ (1<<v)) for v in candidates):return False
        return True
    double_hist=Counter();secure_hist=Counter(); counterexamples=[]
    for s in range(1<<p):
        double=all(((s & (A[u] | (1<<u))).bit_count() >= 2) for u in range(p))
        st=secure(s)
        if double:double_hist[s.bit_count()]+=1
        if st:secure_hist[s.bit_count()]+=1
        if double != st:counterexamples.append(s)
    assert not counterexamples, (p,counterexamples[:4])
    small={k:secure_hist[k] for k in range(5)}
    X=sorted(sum(1<<v for v in C) for C in itertools.combinations(range(p),5) if secure(sum(1<<v for v in C)))
    ix={s:i for i,s in enumerate(X)}
    def graph(sliding):
        E=[]; adj=[[] for _ in X]
        for i,s in enumerate(X):
            for u in range(p):
                if not(s>>u&1):continue
                for v in range(p):
                    if s>>v&1 or (sliding and not(A[u]>>v&1)):continue
                    j=ix.get(s^(1<<u)^(1<<v))
                    if j is not None and i<j:
                        E.append([i,j]);adj[i].append(j);adj[j].append(i)
        E.sort()
        for z in adj:z.sort()
        seen=set(); comps=[]
        for i in range(len(X)):
            if i in seen:continue
            queue=[i];seen.add(i)
            for u in queue:
                for v in adj[u]:
                    if v not in seen:seen.add(v);queue.append(v)
            comps.append(sorted(queue))
        comps.sort(key=lambda c:(-len(c),c[0]))
        ecc=[];distcounts=[]
        for src in range(len(X)):
            d=[-1]*len(X);d[src]=0; queue=[src]
            for u in queue:
                for v in adj[u]:
                    if d[v]<0:d[v]=d[u]+1;queue.append(v)
            ecc.append(max(d));distcounts.append(dict(sorted(Counter(x for x in d if x>=0).items())))
        return dict(edges=E,degree_hist=dict(sorted(Counter(len(z) for z in adj).items())),
                    components=comps,eccentricity_hist=dict(sorted(Counter(ecc).items())),
                    dist_histograms=distcounts,radius=min(ecc),diameter=max(ecc))
    orbits=[];unchecked=set(X)
    def orbit(s):
        return {sum(1<<((a+b*x)%p) for x in range(p) if s>>x&1) for a in range(p) for b in Q}
    while unchecked:
        rep=min(unchecked);orb=orbit(rep);assert orb<=set(X)
        orbits.append(dict(representative=rep,sets=sorted(orb)))
        unchecked-=orb
    orbits.sort(key=lambda z:(-len(z['sets']),z['representative']))
    return dict(prime=p,quadratic_residues=Q,open_neighborhood_masks=A,
                cardinality_below_five=small,
                double_domination_hist=dict(sorted(double_hist.items())),
                secure_total_hist=dict(sorted(secure_hist.items())),
                verified_equivalence_all_subsets=True,
                minimum_sets=X,affine_orbits=orbits,
                token_sliding=graph(True),token_jumping=graph(False))

if __name__=='__main__':
    result={str(p):analysis(p) for p in (13,17)}
    print(json.dumps(result,sort_keys=True,separators=(',',':')))
