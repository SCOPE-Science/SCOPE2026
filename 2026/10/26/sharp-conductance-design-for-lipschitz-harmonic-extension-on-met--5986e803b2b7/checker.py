"""Exact rational checks for the metric-star harmonic-extension norm law.

Requires only Python 3 standard library. Run: python checker.py.
"""
from fractions import Fraction as F
from itertools import combinations

from random import Random


def formula(lengths):
    lengths = sorted(F(x) for x in lengths)
    n = len(lengths)
    assert n >= 3 and min(lengths) > 0
    roots = []
    for k in range(3, n + 1):
        z = F(k - 2, 1) / sum(lengths[:k])
        if sum(max(F(0), 1 - z*x) for x in lengths) == 2:
            roots.append(z)
    assert roots and len(set(roots)) == 1
    z0 = roots[0]
    choices = {z0} | {1/x for x in lengths if 1/x >= z0}
    result = None
    for z in choices:
        lower = [max(F(0), 1 - z*x)/2 for x in lengths]
        surplus = 1 - sum(lower)
        assert surplus >= 0
        a = lower[:]
        a[0] += surplus
        denom = sum(a_i/x for a_i, x in zip(a, lengths))
        w = [a_i/x/denom for a_i, x in zip(a, lengths)]
        candidate = 1 + z/denom
        if result is None or candidate < result[0]:
            result = (candidate, w, z)
    return result


def direct_norm(lengths, weights):
    return max(sum(weights[j]*(lengths[i] + lengths[j])/lengths[i]
                   for j in range(len(lengths)) if i != j)
               for i in range(len(lengths)))


def solve_square(A, b):
    n = len(b)
    C = [list(row) + [b_i] for row, b_i in zip(A, b)]
    for j in range(n):
        p = next((i for i in range(j, n) if C[i][j]), None)
        if p is None:
            return None
        C[j], C[p] = C[p], C[j]
        u = C[j][j]
        C[j] = [v/u for v in C[j]]
        for i in range(n):
            if i == j:
                continue
            u = C[i][j]
            if u:
                C[i] = [C[i][k] - u*C[j][k] for k in range(n+1)]
    return [C[i][-1] for i in range(n)]


def independent_vertex_lp(lengths):
    """Enumerate vertices of the ORIGINAL minimax linear program.

    Variables are the leaf weights and the norm bound. Only rational
    Gaussian elimination is used. No water-filling reparameterization.
    """
    l = [F(x) for x in lengths]
    n = len(l)
    eq = [F(1)]*n + [F(0)]
    inequalities = []
    for i in range(n):
        inequalities.append(([F(0) if i == j else (l[i]+l[j])/l[i]
                              for j in range(n)] + [F(-1)], F(0)))
    for j in range(n):
        inequalities.append(([-F(int(k == j)) for k in range(n)] + [F(0)], F(0)))
    minimum = None
    for active in combinations(range(2*n), n):
        A = [eq] + [inequalities[k][0] for k in active]
        b = [F(1)] + [inequalities[k][1] for k in active]
        v = solve_square(A, b)
        if v is None:
            continue
        if any(sum(a*x for a, x in zip(row, v)) > b0
               for row, b0 in inequalities):
            continue
        if minimum is None or v[-1] < minimum:
            minimum = v[-1]
    assert minimum is not None
    return minimum


def check():
    rng = Random(1752016)
    exact_cases = [
        [1,1,1], [1,2,3], [1,1,10], [1,1,1,100],
        [1,1,1,1], [1,2,5,20], [1,1,3,4],
        [1,3,10,20,100], [1,2,3,4,5],
        [F(1,100),1,1,1], [F(1,3),1,1,1], [F(1,2),1,1,1]
    ]
    for n in (3,4,5):
        for _ in range(10):
            exact_cases.append([F(rng.randint(1,7), rng.randint(1,7))
                               for _ in range(n)])
    count = 0
    for data in exact_cases:
        l = sorted(F(x) for x in data)
        val, w, z = formula(l)
        assert sum(w) == 1 and all(v >= 0 for v in w)
        assert direct_norm(l, w) == val, (l, val, direct_norm(l,w), z)
        exact_lp = independent_vertex_lp(l)
        assert val == exact_lp, (l, val, exact_lp)
        assert val > 1
        count += 1
    for n in range(3,11):
        val, weights, _ = formula([1]*n)
        assert val == F(2*(n-1),n)
        assert weights == [F(1,n)]*n
    for k in range(2,9):
        critical = F(k-2,k)
        for r in (F(1,20), F(1,4), F(1,2), F(3,4), F(1)):
            val, weights, _ = formula([r]+[F(1)]*k)
            t_balanced = F(2*(k-1))*r/(k+2*r+k*r*r)
            assert val == 1 + min(r, t_balanced)
            if 0 < r < critical:
                assert weights[0] == 1, (k,r,weights)
    print(f"PASS: {count} exact-rational minimax vs independent LP vertex enumerations")
    print("PASS: eight equilateral arm-count cases and 35 sharp phase-law cases")


if __name__ == '__main__':
    check()
