from fractions import Fraction
from itertools import permutations
from math import factorial


def monotone_functions(n):
    funcs = [0, 1]
    for k in range(1, n + 1):
        m = 1 << (k - 1)
        nxt = []
        for f0 in funcs:
            for f1 in funcs:
                if f0 & ~f1 == 0:
                    nxt.append(f0 | (f1 << m))
        funcs = nxt
    return funcs


def simple_games(n):
    top = (1 << n) - 1
    return [f for f in monotone_functions(n)
            if ((f >> 0) & 1) == 0 and ((f >> top) & 1) == 1]


def minimal_winning(mask, n):
    out = []
    for S in range(1, 1 << n):
        if not ((mask >> S) & 1):
            continue
        minimal = True
        x = S
        while x:
            b = x & -x
            if (mask >> (S ^ b)) & 1:
                minimal = False
                break
            x -= b
        if minimal:
            out.append(S)
    return out


def indices(mask, n):
    b = [0] * n
    j = [Fraction(0) for _ in range(n)]
    sh = [Fraction(0) for _ in range(n)]

    # Winning-coalition criticality: Banzhaf and Johnston.
    for W in range(1, 1 << n):
        if not ((mask >> W) & 1):
            continue
        crit = [i for i in range(n)
                if (W >> i) & 1 and not ((mask >> (W ^ (1 << i))) & 1)]
        if crit:
            for i in crit:
                b[i] += 1
                j[i] += Fraction(1, len(crit))

    # Losing-predecessor swings: Shapley-Shubik.
    for i in range(n):
        for S in range(1 << n):
            if (S >> i) & 1:
                continue
            if not ((mask >> S) & 1) and ((mask >> (S | (1 << i))) & 1):
                k = S.bit_count()
                sh[i] += Fraction(factorial(k) * factorial(n - k - 1), factorial(n))
    return b, sh, j


def sign(x):
    return (x > 0) - (x < 0)


def same_weak_order(a, b):
    n = len(a)
    return all(sign(a[i] - a[k]) == sign(b[i] - b[k])
               for i in range(n) for k in range(i + 1, n))


def game_from_mwc(mwc, n):
    mask = 0
    for S in range(1 << n):
        if any((S & M) == M for M in mwc):
            mask |= 1 << S
    return mask


def permute_subset(S, p):
    T = 0
    for i, pi in enumerate(p):
        if (S >> i) & 1:
            T |= 1 << pi
    return T


def canonical_mwc(mwc, n):
    best = None
    for p in permutations(range(n)):
        image = tuple(sorted(permute_subset(S, p) for S in mwc))
        if best is None or image < best:
            best = image
    return best


# Exhaustive lower bound and first-order census.
expected_simple = {1: 1, 2: 4, 3: 18, 4: 166, 5: 7579}
for n in range(1, 6):
    games = simple_games(n)
    assert len(games) == expected_simple[n], (n, len(games))
    div = []
    for g in games:
        b, sh, j = indices(g, n)
        db = not same_weak_order(b, j)
        ds = not same_weak_order(sh, j)
        assert db == ds, (n, g, b, sh, j)
        if db:
            div.append(g)
    if n <= 4:
        assert not div, (n, len(div))
    else:
        assert len(div) == 1870, len(div)

# Canonical isomorphism census on five players.
games5 = simple_games(5)
all_classes = {canonical_mwc(minimal_winning(g, 5), 5) for g in games5}
assert len(all_classes) == 208, len(all_classes)

div5 = []
for g in games5:
    b, sh, j = indices(g, 5)
    if not same_weak_order(b, j):
        div5.append(g)

div_classes = {canonical_mwc(minimal_winning(g, 5), 5) for g in div5}
assert len(div_classes) == 34, len(div_classes)

min_mwc = min(len(minimal_winning(g, 5)) for g in div5)
assert min_mwc == 3
sparse = [g for g in div5 if len(minimal_winning(g, 5)) == min_mwc]
assert len(sparse) == 30, len(sparse)
sparse_classes = {canonical_mwc(minimal_winning(g, 5), 5) for g in sparse}
assert len(sparse_classes) == 1, len(sparse_classes)

# Explicit representative.
M = [
    (1 << 1) | (1 << 2) | (1 << 3),  # {2,3,4}
    (1 << 1) | (1 << 2) | (1 << 4),  # {2,3,5}
    (1 << 0) | (1 << 3) | (1 << 4),  # {1,4,5}
]
witness = game_from_mwc(M, 5)
b, sh, j = indices(witness, 5)
assert b == [3, 5, 5, 5, 5]
assert sh == [Fraction(2,15), Fraction(13,60), Fraction(13,60), Fraction(13,60), Fraction(13,60)]
assert j == [Fraction(1,1), Fraction(11,6), Fraction(11,6), Fraction(5,3), Fraction(5,3)]
assert sum(b) == 23
assert sum(sh) == 1
assert sum(j) == 8

bn = [Fraction(x, sum(b)) for x in b]
jn = [x / sum(j) for x in j]
assert bn == [Fraction(3,23), Fraction(5,23), Fraction(5,23), Fraction(5,23), Fraction(5,23)]
assert jn == [Fraction(1,8), Fraction(11,48), Fraction(11,48), Fraction(5,24), Fraction(5,24)]

print('VERIFY_OK')
print('simple_counts', [expected_simple[n] for n in range(1,6)])
print('five_player_total_isomorphism_classes', len(all_classes))
print('five_player_divergent_labeled_games', len(div5))
print('five_player_divergent_isomorphism_classes', len(div_classes))
print('minimum_mwc_count_among_divergent_games', min_mwc)
print('sparsest_divergent_labeled_games', len(sparse))
print('sparsest_divergent_isomorphism_classes', len(sparse_classes))
print('witness_banzhaf_normalized', [str(x) for x in bn])
print('witness_shapley_shubik', [str(x) for x in sh])
print('witness_johnston_normalized', [str(x) for x in jn])
