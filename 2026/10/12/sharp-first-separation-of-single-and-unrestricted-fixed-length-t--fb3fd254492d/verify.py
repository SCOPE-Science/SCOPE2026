#!/usr/bin/env python3
"""Exhaustive checks of length-seven fixed-two tandem duplication classification.

Use only Python's standard library. The unrestricted alphabet theorem is
proved mathematically in RESULT.md; this checker tests q=2 and q=3 exhaustively.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb


def words(q, n):
    return product(range(q), repeat=n)


def derivative(x, q):
    return x[:2], tuple((x[i+2] - x[i]) % q for i in range(len(x)-2))


def invert(h, z, q):
    a = list(h)
    for i, t in enumerate(z):
        a.append((a[i] + t) % q)
    return tuple(a)


def tandem(x, i):
    return x[:i+2] + x[i:i+2] + x[i+2:]


def insert00(z, i):
    return z[:i] + (0, 0) + z[i:]


def root_and_signature(z):
    nz = [v for v in z if v != 0]
    zero_runs = []
    zeros = 0
    for v in z:
        if v == 0:
            zeros += 1
        else:
            zero_runs.append(zeros)
            zeros = 0
    zero_runs.append(zeros)
    trunk = []
    for i, cnt in enumerate(zero_runs):
        trunk.extend([0] * (cnt % 2))
        if i < len(nz):
            trunk.append(nz[i])
    sig = tuple(cnt // 2 for cnt in zero_runs)
    return tuple(trunk), sig


def independent_optima(fiber, incompatible):
    """Exhaustive subset enumeration, separate from any structural formula."""
    best = 0
    witness_sets = []
    for k in range(1, len(fiber)+1):
        for subset in combinations(fiber, k):
            if all(frozenset((u, v)) not in incompatible for u, v in combinations(subset, 2)):
                if k > best:
                    best = k
                    witness_sets = [subset]
                elif k == best:
                    witness_sets.append(subset)
    return best, witness_sets


def irreducible_count(q, length):
    return sum(1 for z in words(q, length) if (0, 0) not in tuple(zip(z, z[1:])))


def expected_opt(q, n):
    a = {ell: irreducible_count(q, ell) for ell in range(n-1)}
    return q*q*sum(a[ell] for ell in range(n-2, -1, -2))


def verify(q, n):
    fibers = defaultdict(list)
    sigs = {}
    all_words = list(words(q, n))
    by_output = defaultdict(list)
    for x in all_words:
        h, z = derivative(x, q)
        assert len(h) == 2 and len(z) == n - 2
        assert invert(h, z, q) == x
        r, s = root_and_signature(z)
        assert sum(s) * 2 + len(r) == len(z)
        fibers[(h, r)].append(x)
        sigs[x] = s
        for i in range(n-1):
            out = tandem(x, i)
            hh, zz = derivative(out, q)
            assert hh == h and zz == insert00(z, i)
            rr, ss = root_and_signature(zz)
            assert rr == r
            assert sum(ss) == sum(s) + 1
            by_output[out].append(x)

    # Direct-channel collision relation, constructed without using signatures.
    direct_conflicts = set()
    for inputs in by_output.values():
        for u, v in combinations(sorted(set(inputs)), 2):
            direct_conflicts.add(frozenset((u, v)))

    # Independent signature adjacency formula, checked on every within-fiber pair.
    signature_conflicts = set()
    max_size, count_maxima = 0, 1
    profile = Counter()
    num_special = 0
    for (h, r), fiber in fibers.items():
        for u, v in combinations(fiber, 2):
            l1 = sum(abs(a-b) for a,b in zip(sigs[u], sigs[v]))
            assert l1 % 2 == 0
            if l1 == 2:
                signature_conflicts.add(frozenset((u, v)))
        local_conflicts = {pair for pair in signature_conflicts if pair <= set(fiber)}
        alpha, solutions = independent_optima(fiber, local_conflicts)
        best_count = len(solutions)
        profile[(len(r),len(fiber),alpha,best_count)] += 1
        max_size += alpha
        count_maxima *= best_count
        if n <= 6:
            assert alpha == 1
        if n == 7:
            w = sum(v != 0 for v in r)
            if len(r) == 5:
                assert (len(fiber),alpha,best_count) == (1,1,1)
            elif len(r) == 3:
                assert (len(fiber),alpha,best_count) == (w+1,1,w+1)
            else:
                assert len(r) == 1
                if r == (0,):
                    assert (len(fiber),alpha,best_count) == (1,1,1)
                else:
                    assert (len(fiber),alpha,best_count) == (3,2,1)
                    nonzero = r[0]
                    sigsets = {sigs[x] for x in solutions[0]}
                    assert sigsets == {(2,0),(0,2)}
                    num_special += 1
    assert direct_conflicts == signature_conflicts

    # All different-root pairs are ruled out by the root invariance of each
    # duplicated output, checked above.
    if n < 7:
        assert max_size == expected_opt(q,n)
    else:
        a3, a5 = irreducible_count(q,3), irreducible_count(q,5)
        expected = q*q*(a5+a3+2*q-1)
        assert expected == q**7-3*q**5+3*q**4+q**3-q*q
        assert max_size == expected
        assert num_special == q*q*(q-1)
        expected_count = (2**(q-1) * 3**(3*(q-1)**2) * 4**((q-1)**3))**(q*q)
        assert count_maxima == expected_count
        assert max_size - expected_opt(q,n) == q*q*(q-1)
    print(
        'Q',q,'N',n,'words',len(all_words),'fibers',len(fibers),
        'conflicts',len(direct_conflicts),'maximum',max_size,
        'maxima',count_maxima,
        'profiles',sorted((k,v) for k,v in profile.items())
    )
    return max_size, count_maxima


if __name__ == '__main__':
    for q in (2, 3):
        for n in range(2, 8):
            verify(q, n)
    assert verify(2, 7) == (84, 2176782336)
    assert verify(3, 7)[0] == 1719
    print('VERIFY_OK q2_n7_maximum=84 q2_n7_maxima=2176782336 '
          'q3_n7_maximum=1719 first_strict_length=7 '
          'direct_signature_conflicts_agree=true')
