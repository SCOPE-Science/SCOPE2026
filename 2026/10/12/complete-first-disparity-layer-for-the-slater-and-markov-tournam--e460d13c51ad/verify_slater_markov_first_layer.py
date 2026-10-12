#!/usr/bin/env python3
from itertools import permutations
from fractions import Fraction
from collections import Counter
from functools import lru_cache


def tournament(n, bits):
    out = [0] * n
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (bits >> k) & 1:
                out[i] |= 1 << j
            else:
                out[j] |= 1 << i
            k += 1
    return out


def slater_by_permutations(out):
    n = len(out)
    if n == 1:
        return (0,), 0
    best = -1
    winners = set()
    for p in permutations(range(n)):
        score = 0
        for a in range(n):
            for b in range(a + 1, n):
                score += (out[p[a]] >> p[b]) & 1
        if score > best:
            best = score
            winners = {p[0]}
        elif score == best:
            winners.add(p[0])
    return tuple(sorted(winners)), best


def slater_by_subset_dp(out):
    n = len(out)
    if n == 1:
        return (0,), 0

    @lru_cache(None)
    def opt(mask):
        if mask == 0:
            return 0
        z = -1
        for i in range(n):
            if (mask >> i) & 1:
                rest = mask ^ (1 << i)
                z = max(z, (out[i] & rest).bit_count() + opt(rest))
        return z

    full = (1 << n) - 1
    best = opt(full)
    winners = []
    for i in range(n):
        rest = full ^ (1 << i)
        if (out[i] & rest).bit_count() + opt(rest) == best:
            winners.append(i)
    return tuple(winners), best


def solve_fraction(A, b):
    A = [[Fraction(x) for x in row] + [Fraction(bb)] for row, bb in zip(A, b)]
    m, n = len(A), len(A[0]) - 1
    r = 0
    pivots = []
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c]), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        z = A[r][c]
        A[r] = [x / z for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                z = A[i][c]
                A[i] = [A[i][j] - z * A[r][j] for j in range(n + 1)]
        pivots.append(c)
        r += 1
    assert len(pivots) == n
    x = [Fraction(0)] * n
    for i, c in enumerate(pivots):
        x[c] = A[i][n]
    return tuple(x)


def markov_by_linear_system(out):
    n = len(out)
    if n == 1:
        return (0,), (Fraction(1),)
    # Brandt-Dau-Seedig convention: M_ij=1 when i defeats j and
    # N=(M+diag(outdegree))/(n-1).  N is column-stochastic.
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = out[i].bit_count()
        for j in range(n):
            if (out[i] >> j) & 1:
                A[i][j] = 1
    # Solve (A-(n-1)I)p=0, replacing the last equation by sum p=1.
    eq = []
    rhs = []
    for i in range(n - 1):
        eq.append([A[i][j] - ((n - 1) if i == j else 0) for j in range(n)])
        rhs.append(0)
    eq.append([1] * n)
    rhs.append(1)
    p = solve_fraction(eq, rhs)
    assert all(x >= 0 for x in p) and sum(p) == 1
    m = max(p)
    return tuple(i for i, x in enumerate(p) if x == m), p


def det_bareiss(M):
    n = len(M)
    if n == 0:
        return 1
    A = [list(map(int, row)) for row in M]
    sign = 1
    prev = 1
    for k in range(n - 1):
        p = next((r for r in range(k, n) if A[r][k] != 0), None)
        if p is None:
            return 0
        if p != k:
            A[k], A[p] = A[p], A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * pivot - A[i][k] * A[k][j]) // prev
        prev = pivot
    return sign * A[n - 1][n - 1]


def markov_by_tree_cofactors(out):
    n = len(out)
    if n == 1:
        return (0,), (Fraction(1),)
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = out[i].bit_count()
        for j in range(n):
            if (out[i] >> j) & 1:
                A[i][j] = 1
    # L=(n-1)I-A has zero column sums. Diagonal cofactors give the
    # stationary weights (directed matrix-tree theorem).
    L = [[((n - 1) if i == j else 0) - A[i][j] for j in range(n)] for i in range(n)]
    w = []
    for r in range(n):
        minor = [[L[i][j] for j in range(n) if j != r] for i in range(n) if i != r]
        w.append(det_bareiss(minor))
    if max(w) <= 0:
        w = [-x for x in w]
    assert all(x >= 0 for x in w) and sum(w) > 0
    total = sum(w)
    p = tuple(Fraction(x, total) for x in w)
    m = max(p)
    return tuple(i for i, x in enumerate(p) if x == m), p


def relabel_bits(n, bits, perm):
    out = tournament(n, bits)
    out2 = [0] * n
    for i in range(n):
        for j in range(n):
            if (out[i] >> j) & 1:
                out2[perm[i]] |= 1 << perm[j]
    z = 0
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (out2[i] >> j) & 1:
                z |= 1 << k
            k += 1
    return z


def canonical(n, bits):
    return min(relabel_bits(n, bits, p) for p in permutations(range(n)))


def neigh(out):
    return tuple(tuple(j for j in range(len(out)) if (out[i] >> j) & 1) for i in range(len(out)))


diff = {}
hist5 = Counter()
classes = Counter()
for n in range(1, 6):
    d = 0
    total = 1 << (n * (n - 1) // 2)
    for bits in range(total):
        out = tournament(n, bits)
        s1 = slater_by_permutations(out)
        s2 = slater_by_subset_dp(out)
        assert s1 == s2
        m1 = markov_by_linear_system(out)
        m2 = markov_by_tree_cofactors(out)
        assert m1 == m2
        S, M = s1[0], m1[0]
        if n == 5:
            hist5[(len(S), len(M), S == M)] += 1
        if S != M:
            d += 1
            assert set(M) < set(S)  # complete first-layer relation
            if n == 5:
                classes[canonical(n, bits)] += 1
    diff[n] = d

assert diff == {1: 0, 2: 0, 3: 0, 4: 0, 5: 240}
assert hist5 == Counter({(1,1,True):720, (3,1,False):120, (2,1,False):120, (3,3,True):40, (5,5,True):24})
assert classes == Counter({10:120, 12:120})

expected = {
    10: {
        'neighbors': ((2,4),(0,),(1,),(0,1,2),(1,2,3)),
        'slater': (0,3,4),
        'markov': (4,),
        'p': (Fraction(9,43),Fraction(3,43),Fraction(1,43),Fraction(13,43),Fraction(17,43)),
    },
    12: {
        'neighbors': ((3,4),(0,),(0,1),(1,2),(1,2,3)),
        'slater': (0,4),
        'markov': (4,),
        'p': (Fraction(1,4),Fraction(1,12),Fraction(1,6),Fraction(1,8),Fraction(3,8)),
    },
}
for bits, e in expected.items():
    out = tournament(5, bits)
    assert neigh(out) == e['neighbors']
    assert slater_by_permutations(out)[0] == e['slater']
    assert markov_by_linear_system(out) == (e['markov'], e['p'])
    orbit = {relabel_bits(5, bits, p) for p in permutations(range(5))}
    assert len(orbit) == 120

print('VERIFY_OK')
print('disparities_by_order', diff)
print('order5_joint_histogram', dict(hist5))
print('order5_disparity_probability', '240/1024 = 15/64')
print('order5_classes', dict(classes))
for bits in (10,12):
    out=tournament(5,bits)
    print('class', bits, 'neighbors', neigh(out), 'SL', slater_by_permutations(out)[0], 'MA', markov_by_linear_system(out)[0], 'stationary', markov_by_linear_system(out)[1], 'orbit', classes[bits])
