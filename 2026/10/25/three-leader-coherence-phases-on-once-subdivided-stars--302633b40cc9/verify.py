#!/usr/bin/env python3
"""Exact rational checks for three grounded vertices on length-two spiders.
Requires only Python's standard library.  Finite checks supplement, not replace, the proof.
"""
from fractions import Fraction as Q
from itertools import combinations


def graph_laplacian(k):
    n = 2*k + 1
    a = [[0]*n for _ in range(n)]
    for j in range(k):
        for u, v in ((0, 2*j+1), (2*j+1, 2*j+2)):
            a[u][u] += 1
            a[v][v] += 1
            a[u][v] -= 1
            a[v][u] -= 1
    return a


def exact_trace_inverse(a):
    n = len(a)
    rows = [[Q(x) for x in r] + [Q(i == j) for j in range(n)]
            for i, r in enumerate(a)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if rows[i][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        factor = rows[col][col]
        rows[col] = [x/factor for x in rows[col]]
        for i in range(n):
            if i != col and rows[i][col]:
                f = rows[i][col]
                rows[i] = [x-f*y for x, y in zip(rows[i], rows[col])]
    return sum((rows[i][n+i] for i in range(n)), Q(0))


def direct_cost(k, leaders):
    a = graph_laplacian(k)
    follower = [i for i in range(2*k+1) if i not in leaders]
    return exact_trace_inverse([[a[i][j] for j in follower] for i in follower])


def classify(k, leaders):
    if 0 in leaders:
        inner = leaf = both = 0
        for j in range(k):
            x = 2*j+1 in leaders
            y = 2*j+2 in leaders
            inner += x and not y
            leaf += y and not x
            both += x and y
        return ('hub', inner, leaf, both)
    inner = leaf = both = 0
    for j in range(k):
        x = 2*j+1 in leaders
        y = 2*j+2 in leaders
        inner += x and not y
        leaf += y and not x
        both += x and y
    return ('no_hub', inner, leaf, both)


def orbit_cost(k, kind):
    root, ni, nl, nb = kind
    z = k-ni-nl-nb
    assert z >= 0
    if root == 'hub':
        assert ni + nl + 2*nb == 2
        return 3*z + Q(nl, 2) + ni
    assert ni + nl + 2*nb == 3
    s = Q(ni+nb) + Q(nl, 2)
    assert s > 0
    return 3*z + Q(nl, 2) + ni + (1+2*z+Q(nl,4))/s


def optimum(k):
    if k == 3: return Q(8,3), ('no_hub',0,3,0)
    if k == 4: return Q(27,4), ('no_hub',1,2,0)
    return Q(3*k-5), ('hub',0,2,0)

counts = {'orbit_full_inverse': 0, 'exhaustive_full_inverse': 0,
          'analytical_profile_comparisons': 0, 'optimal_counts': 0}

for k in range(3, 12):
    seen = {}
    for leaders in combinations(range(2*k+1),3):
        kind = classify(k,leaders)
        seen[kind] = seen.get(kind,0)+1
    expected_j, expected_kind = optimum(k)
    assert min((orbit_cost(k,t),t) for t in seen)[0] == expected_j
    actual_opt = [t for t in seen if orbit_cost(k,t) == expected_j]
    assert actual_opt == [expected_kind]
    required_count = (1 if k==3 else k*(k-1)*(k-2)//2 if k==4
                      else k*(k-1)//2)
    assert seen[expected_kind] == required_count
    counts['optimal_counts'] += 1
    counts['analytical_profile_comparisons'] += len(seen)
    for kind in seen:
        if kind[0] == 'hub':
            if kind == ('hub',0,2,0): leader=(0,2,4)
            elif kind == ('hub',2,0,0): leader=(0,1,3)
            elif kind == ('hub',1,1,0): leader=(0,1,4)
            else: leader=(0,1,2)
        else:
            if kind[3]:
                leader=(1,2,3 if kind[1] else 4)
            else:
                leader=tuple(2*j+1 if j<kind[1] else 2*j+2 for j in range(3))
        assert classify(k,leader)==kind
        assert direct_cost(k,leader)==orbit_cost(k,kind)
        counts['orbit_full_inverse']+=1

for k in (3,4,5):
    expected_j,expected_kind=optimum(k)
    for leader in combinations(range(2*k+1),3):
        assert direct_cost(k,leader)==orbit_cost(k,classify(k,leader))
        assert direct_cost(k,leader)>=expected_j
        counts['exhaustive_full_inverse']+=1

print('VERIFY_OK '+ ' '.join(f'{a}={b}' for a,b in counts.items()))
