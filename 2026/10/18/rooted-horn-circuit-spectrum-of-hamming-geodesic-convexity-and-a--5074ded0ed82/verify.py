"""Independent finite tests for Hamming box-hull rooted circuit spectrum.
Python 3, standard library only. This verifier is not an infinite proof.
"""
from itertools import product, combinations
from math import comb, factorial


def count_formula(d,q,r):
    return sum((-1)**j*comb(r,j)*(q**r-(q-1)**r-j*(q-1)**(r-1))**d
               for j in range(r+1))//factorial(r)


def inclusion_hull(points, subset):
    if not subset:
        return frozenset()
    return frozenset(x for x in points
        if all(any(x[i] == p[i] for p in subset) for i in range(len(x))))


def interval_hull(points, subset):
    current=set(subset)
    while True:
        nxt=set(current)
        for a,b in combinations(current,2):
            nxt.update(x for x in points if all(x[i] in (a[i],b[i]) for i in range(len(x))))
        if current == nxt:
            return frozenset(current)
        current=nxt


def run():
    tested=0
    for d,q in ((2,2),(3,2),(4,2),(2,3),(3,3),(2,4),(3,4)):
        points=list(product(range(q),repeat=d))
        root=(0,)*d
        others=[v for v in points if v != root]
        found={r:0 for r in range(2,d+1)}
        for r in range(2,d+1):
            for group in combinations(others,r):
                if not all(any(v[i]==root[i] for v in group) for i in range(d)):
                    continue
                if all(any(not any(v[i]==root[i] for v in group if v!=x)
                           for i in range(d)) for x in group):
                    found[r]+=1
            assert found[r]==count_formula(d,q,r), (d,q,r,found[r],count_formula(d,q,r))
        assert found[d] == (q-1)**(d*(d-1))
        total=q**d*sum(found.values())
        if d<=3 and q<=3:
            for mask in range(1<<len(points)):
                if d==3 and q==3 and mask>=200:
                    break
                ss=[points[i] for i in range(len(points)) if mask>>i&1]
                assert inclusion_hull(points,ss)==interval_hull(points,ss)
                tested+=1
        print('CASE',d,q,'per_root',found,'direct_unit',total,'PASS')
    print('VERIFY_OK cases=7 independent_subset_hulls=',tested,'direct_stem_counts=PASS extremal_counts=PASS')

if __name__=='__main__': run()
