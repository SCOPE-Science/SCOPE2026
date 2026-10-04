#!/usr/bin/env python3
from itertools import permutations
from fractions import Fraction
from math import factorial
from collections import Counter
import hashlib


def antichains_recursive(n):
    subs = list(range(1, 1 << n))
    out = set()
    def rec(cands, cur):
        if not cands:
            if cur:
                out.add(tuple(sorted(cur)))
            return
        m = cands[0]
        rec(cands[1:], cur)
        rec([x for x in cands[1:] if not ((x & m) == x or (x & m) == m)], cur + [m])
    rec(subs, [])
    return out


def monotone_tables(n):
    # Independent Dedekind-style recursion.  A monotone function in n variables
    # is a pair (f0,f1) of monotone functions in n-1 variables with f0 <= f1.
    tables = {(0,), (1,)}
    for _ in range(n):
        prev = sorted(tables)
        new = set()
        for a in prev:
            for b in prev:
                if all(x <= y for x, y in zip(a, b)):
                    new.add(tuple(a + b))
        tables = new
    return tables


def mwcs_from_table(tab, n):
    fam = []
    for S, v in enumerate(tab):
        if not v or S == 0:
            continue
        if all(tab[S ^ (1 << i)] == 0 for i in range(n) if (S >> i) & 1):
            fam.append(S)
    return tuple(sorted(fam))


def simple_games_via_tables(n):
    out = set()
    for tab in monotone_tables(n):
        if tab[0] != 0 or tab[-1] != 1:
            continue
        out.add(mwcs_from_table(tab, n))
    return out


def winning(mwcs, S):
    return any((M & S) == M for M in mwcs)


def proper(mwcs, n):
    full = (1 << n) - 1
    return all(not (winning(mwcs, S) and winning(mwcs, full ^ S)) for S in range(1 << n))


def dp_raw(mwcs, n):
    return tuple(sum((Fraction(1, M.bit_count()) for M in mwcs if (M >> i) & 1), Fraction(0)) for i in range(n))


def ss_subset(mwcs, n):
    vals = []
    den = factorial(n)
    for i in range(n):
        x = Fraction(0)
        for S in range(1 << n):
            if (S >> i) & 1:
                continue
            if not winning(mwcs, S) and winning(mwcs, S | (1 << i)):
                k = S.bit_count()
                x += Fraction(factorial(k) * factorial(n - k - 1), den)
        vals.append(x)
    return tuple(vals)


def ss_permutations(mwcs, n):
    piv = [0] * n
    for p in permutations(range(n)):
        S = 0
        for i in p:
            before = winning(mwcs, S)
            S2 = S | (1 << i)
            after = winning(mwcs, S2)
            if (not before) and after:
                piv[i] += 1
                break
            S = S2
    den = factorial(n)
    return tuple(Fraction(x, den) for x in piv)


def weak_order(v):
    return tuple((v[i] > v[j]) - (v[i] < v[j]) for i in range(len(v)) for j in range(i + 1, len(v)))


def has_strict_reversal(a, b):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            sa = (a[i] > a[j]) - (a[i] < a[j])
            sb = (b[i] > b[j]) - (b[i] < b[j])
            if sa * sb == -1:
                return True
    return False


def permute_mask(mask, p):
    out = 0
    for i, j in enumerate(p):
        if (mask >> i) & 1:
            out |= 1 << j
    return out


def canonical(mwcs, n):
    return min(tuple(sorted(permute_mask(M, p) for M in mwcs)) for p in permutations(range(n)))


def game_from_weights(q, w):
    n = len(w)
    mins = []
    for S in range(1, 1 << n):
        wt = sum(w[i] for i in range(n) if (S >> i) & 1)
        if wt < q:
            continue
        minimal = True
        for i in range(n):
            if (S >> i) & 1:
                T = S ^ (1 << i)
                tw = sum(w[j] for j in range(n) if (T >> j) & 1)
                if tw >= q:
                    minimal = False
                    break
        if minimal:
            mins.append(S)
    return tuple(sorted(mins))


expected_simple = {1:1, 2:4, 3:18, 4:166, 5:7579}
expected_proper = {1:1, 2:3, 3:11, 4:80, 5:2645}
divergence = {}
digest = hashlib.sha256()
all5_div = []

for n in range(1, 6):
    A = antichains_recursive(n)
    B = simple_games_via_tables(n)
    assert A == B
    assert len(A) == expected_simple[n]
    props = sorted(g for g in A if proper(g, n))
    assert len(props) == expected_proper[n]
    div = []
    for g in props:
        dp = dp_raw(g, n)
        ss1 = ss_subset(g, n)
        ss2 = ss_permutations(g, n)
        assert ss1 == ss2
        same = weak_order(dp) == weak_order(ss1)
        if not same:
            assert has_strict_reversal(dp, ss1)
            div.append(g)
        digest.update(repr((n, g, dp, ss1, same)).encode('utf-8'))
        digest.update(b'\n')
    divergence[n] = len(div)
    if n < 5:
        assert not div
    else:
        all5_div = div
        assert len(div) == 460

classes = Counter(canonical(g, 5) for g in all5_div)
expected_classes = Counter({
    (3,5,14,22):30,
    (3,13,14,21):120,
    (3,13,14,21,22):30,
    (3,13,14,21,22,25):60,
    (3,13,14,21,25):60,
    (3,13,21):60,
    (3,13,21,25):20,
    (3,13,21,25,30):20,
    (3,13,21,30):60,
})
assert classes == expected_classes

weighted = {
    (3,5,14,22):(7,(4,3,3,1,1)),
    (3,13,14,21):(9,(5,4,3,2,1)),
    (3,13,14,21,22):(6,(3,3,2,1,1)),
    (3,13,14,21,22,25):(9,(5,4,3,2,2)),
    (3,13,14,21,25):(7,(4,3,2,2,1)),
    (3,13,21):(8,(5,3,2,1,1)),
    (3,13,21,25):(6,(4,2,1,1,1)),
    (3,13,21,25,30):(5,(3,2,1,1,1)),
    (3,13,21,30):(7,(4,3,2,1,1)),
}
assert set(weighted) == set(expected_classes)
for g, (q,w) in weighted.items():
    assert game_from_weights(q,w) == g
    assert proper(g,5)
    assert weak_order(dp_raw(g,5)) != weak_order(ss_subset(g,5))
    assert has_strict_reversal(dp_raw(g,5), ss_subset(g,5))

# A smallest concrete witness with a strict pair reversal.
w = (3,13,14,21)
assert game_from_weights(9,(5,4,3,2,1)) == w
assert dp_raw(w,5) == (Fraction(7,6),Fraction(5,6),Fraction(1,1),Fraction(2,3),Fraction(1,3))
assert ss_subset(w,5) == (Fraction(11,30),Fraction(17,60),Fraction(1,5),Fraction(7,60),Fraction(1,30))
# DP ranks player 3 above player 2; SS reverses that pair.
assert dp_raw(w,5)[2] > dp_raw(w,5)[1]
assert ss_subset(w,5)[2] < ss_subset(w,5)[1]

# Properness really changes the threshold: unrestricted divergence occurs at n=4.
all4 = antichains_recursive(4)
unrestricted4 = [g for g in all4 if weak_order(dp_raw(g,4)) != weak_order(ss_subset(g,4))]
assert len(unrestricted4) == 16
assert all(not proper(g,4) for g in unrestricted4)

print('VERIFY_OK')
print('simple_counts', expected_simple)
print('proper_counts', expected_proper)
print('proper_divergence_counts', divergence)
print('five_player_divergent_labeled', len(all5_div))
print('five_player_isomorphism_classes', len(classes))
print('orbit_hist', dict(Counter(classes.values())))
print('classes', dict(sorted(classes.items())))
print('weighted_representatives', weighted)
print('unrestricted_four_player_divergence', len(unrestricted4))
print('digest', digest.hexdigest())
