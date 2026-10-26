"""Standalone test for edge-open-packing enumerators on matching-deficient bicliques.

Only uses the graph definition and pairwise third-edge conflict rule.
"""
from collections import Counter
from math import comb


def compute(p, q, t):
    assert 3 <= p and 3 <= q and 0 <= t <= min(p, q)
    edges = [(i,j) for i in range(p) for j in range(q) if not (i == j and i < t)]
    eset = set(edges)
    m = len(edges)
    compatible = [0] * m
    for x, (i,j) in enumerate(edges):
        for y,(k,l) in enumerate(edges):
            if x == y: continue
            endpoints_x = [('A',i),('B',j)]
            endpoints_y = [('A',k),('B',l)]
            connector = False
            for a in endpoints_x:
                for b in endpoints_y:
                    if a[0] == b[0]: continue
                    e = (a[1], b[1]) if a[0]=='A' else (b[1],a[1])
                    if e in eset and e != (i,j) and e != (k,l):
                        connector = True
            if not connector: compatible[x] |= 1 << y
    all_sets, maximal = Counter(), Counter()
    count = 0
    def visit(chosen, candidates):
        nonlocal count
        size = len(chosen)
        all_sets[size] += 1
        count += 1
        if size:
            S = set(chosen)
            if all(not all((compatible[e] >> f) & 1 for e in chosen)
                   for f in range(m) if f not in S):
                maximal[size] += 1
        while candidates:
            bit = candidates & -candidates
            e = bit.bit_length() - 1
            candidates &= candidates - 1
            visit(chosen + (e,), candidates & compatible[e])
    visit((), (1 << m) - 1)
    predicted_all = Counter({0:1, 1:m})
    predicted_maximal = Counter()
    centers = [q] * (p-t) + [q-1] * t + [p] * (q-t) + [p-1] * t
    for degree in centers:
        predicted_maximal[degree] += 1
        for k in range(2, degree+1):
            predicted_all[k] += comb(degree,k)
    predicted_all[2] += comb(t,2)
    predicted_maximal[2] += comb(t,2)
    assert all_sets == predicted_all, (p,q,t,all_sets,predicted_all)
    assert maximal == predicted_maximal, (p,q,t,maximal,predicted_maximal)
    return count, dict(sorted(all_sets.items())),dict(sorted(maximal.items()))

if __name__ == '__main__':
    import sys
    samples = 0
    visited = 0
    cases = []
    for p in range(3,7):
        for q in range(3,7):
            for t in range(min(p,q)+1):
                n,a,b = compute(p,q,t)
                samples += 1
                visited += n
                cases.append((p,q,t,n))
    print(f'PASS {samples} parameter triples; {visited} independently enumerated eligible subsets, including empty sets')
    for key in [(3,3,0),(3,3,2),(4,4,0),(4,4,1),(4,4,2),(4,4,4),(5,6,3)]:
        n,a,b=compute(*key)
        print(key,'total',n,'EOP sizes',a,'maximal sizes',b)
