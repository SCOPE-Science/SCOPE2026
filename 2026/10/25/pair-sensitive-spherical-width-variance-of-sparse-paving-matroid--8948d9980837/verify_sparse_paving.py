"""Independent finite tests for directional width identities of sparse-paving matroid polytopes.

Run with Python 3 standard library: python verify_sparse_paving.py
"""
from itertools import combinations, permutations
from math import comb, isclose, sqrt
from collections import Counter


def forbidden_family_is_sparse(n, k, forbidden):
    universe = tuple(combinations(range(n), k))
    f = set(map(frozenset, forbidden))
    assert all(len(s) == k and s.issubset(range(n)) for s in f)
    assert all(len(a.intersection(b)) <= k - 2 for a, b in combinations(f, 2))
    bases = set(map(frozenset, universe)) - f
    assert bases
    for a, b in combinations(bases, 2):
        for e in a - b:
            assert any(frozenset((a - {e}) | {g}) in bases for g in b - a)
    return bases


def check_one(n, k, forbidden, scores):
    bases = forbidden_family_is_sparse(n, k, forbidden)
    universe = tuple(combinations(range(n), k))
    optimum_h = max(sum(scores[i] for i in a) for a in universe)
    optimum_p = max(sum(scores[i] for i in a) for a in bases)
    order = sorted(range(n), key=lambda i: scores[i], reverse=True)
    top = frozenset(order[:k]); forbidden = set(map(frozenset, forbidden))
    theoretical = (scores[order[k - 1]] - scores[order[k]]) if top in forbidden else 0
    assert isclose(optimum_h - optimum_p, theoretical, abs_tol=1e-11)
    return theoretical


def exact_example():
    n = 6; k = 3
    f_comp = [frozenset((0,1,2)), frozenset((3,4,5))]
    f_meet = [frozenset((0,1,2)), frozenset((2,3,4))]
    forbidden_family_is_sparse(n,k,f_comp)
    forbidden_family_is_sparse(n,k,f_meet)
    fixed_values = (3., 2., 1., -1., -2., -3.)
    radius = sqrt(sum(v*v for v in fixed_values))
    gap_over_r = 2/radius
    data = {}
    for name, f in [('complementary',f_comp),('intersecting',f_meet)]:
        hits = []
        for score in permutations(fixed_values):
            d_plus = check_one(n,k,f,score)
            d_minus = check_one(n,k,f,tuple(-x for x in score))
            hits.append(round((d_plus+d_minus)/2))
        counts = Counter(hits)
        data[name] = counts
        if name == 'complementary':
            assert counts == {0:648, 2:72}, counts
        else:
            assert counts == {0:576, 1:144}, counts
    # Both families have mean defect (1/5)*gap/radius, while the
    # complementary-family second moment exceeds the other by gap^2/(5R^2).
    e1 = sum(j*ct for j,ct in data['complementary'].items())/720
    e2 = sum(j*ct for j,ct in data['intersecting'].items())/720
    q1 = sum(j*j*ct for j,ct in data['complementary'].items())/720
    q2 = sum(j*j*ct for j,ct in data['intersecting'].items())/720
    assert isclose(e1,e2) and isclose(q1-q2, 0.2)
    return data, (q1-q2)*gap_over_r**2


def exact_ehrhart_counts():
    """Enumerate integer points of the rank-three six-element cuts for small dilates."""
    f_comp = [frozenset((0,1,2)), frozenset((3,4,5))]
    f_meet = [frozenset((0,1,2)), frozenset((2,3,4))]
    checked={}
    from itertools import product
    for t in range(1, 6):
        point_set = [x for x in product(range(t+1), repeat=6) if sum(x)==3*t]
        def count(family):
            return sum(all(sum(x[i] for i in f)<=2*t for f in family) for x in point_set)
        c1=count(f_comp); c2=count(f_meet)
        correction=sum(comb(j+2, 2)**2 for j in range(t))
        assert c1==c2==len(point_set)-2*correction
        checked[t]=(len(point_set), c1, c2)
    return checked


def test_several():
    trials=0
    for n,k,forbidden in [
        (5,2,[{0,1},{2,3}]),
        (6,2,[{0,1},{2,3},{4,5}]),
        (6,3,[{0,1,2},{3,4,5}]),
        (6,3,[{0,1,2},{2,3,4}]),
        (7,3,[{0,1,2},{2,3,4},{0,4,5}]),
        (7,4,[{0,1,2,3},{0,1,4,5}]),
    ]:
        for order in permutations(range(n)):
            scores=tuple(float(n-order[i]) for i in range(n))
            check_one(n,k,forbidden,scores)
            trials+=1
    return trials


if __name__=='__main__':
    counts,difference=exact_example()
    ehrhart=exact_ehrhart_counts()
    total=test_several()
    print('Exact angular ranks:', counts)
    print('Ehrhart dilate counts (hypersimplex, first, second):', ehrhart)
    print('Conditional width-variance gap for values (3,2,1,-1,-2,-3):',difference)
    print('Independent brute-force support comparisons:', total+2*720)
    print('PASS')
