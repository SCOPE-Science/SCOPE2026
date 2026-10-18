"""Brute truth assignments against the exact modal-approximation spectrum.

Only the Python standard library is used. The infinite parameter claim is
proved in RESULT.md; enumeration supplies finite cross-checks, not a proof.
"""

from collections import Counter
from itertools import product
from math import comb


def predicted(m, n):
    k = m + n
    r = Counter()
    r[(0, 0)] += 1
    for ell in range(k + 1):
        r[(ell, k)] += comb(k, ell)
    for j in range(1, m):
        for ell in range(j + 1):
            r[(ell, n + j)] += comb(m, j) * comb(j, ell)
    for j in range(1, n):
        for ell in range(j + 1):
            r[(ell, m + j)] += comb(n, j) * comb(j, ell)
    return +r


def enumerate_pairs(m, n, sizes):
    k = m + n
    assert len(sizes) == k and all(t >= 2 for t in sizes)
    starts = []
    p = 0
    for t in sizes:
        starts.append((p, (1 << t) - 1 << p))
        p += t
    relation = [(1 << i) | sum(1 << j for j in range(m, k))
                if i < m else
                (1 << i) | sum(1 << j for j in range(m))
                for i in range(k)]
    found = set()
    for mask in range(1 << p):
        full = 0
        active = 0
        for i, (start, block_mask) in enumerate(starts):
            if mask & block_mask:
                active |= 1 << i
            if mask & block_mask == block_mask:
                full |= 1 << i
        upper = 0
        for i in range(k):
            if active & (1 << i):
                upper |= relation[i]
        found.add((full, upper))
    return Counter((f.bit_count(), u.bit_count()) for f, u in found), len(found)


def polynomial_profile(m, n):
    # Coefficients of P(z,1), using the directly specified case formula.
    c = Counter()
    for (i, j), count in predicted(m, n).items():
        c[i] += count
    return tuple(c[i] for i in range(m + n + 1))


def run():
    brute_cases = 0
    valuations_checked = 0
    pairs_checked = 0
    for m in range(1, 5):
        for n in range(1, 5):
            k = m + n
            if k > 6:
                continue
            for sizes in ([2] * k, [2 + (i % 2) for i in range(k)] if k <= 4 else None):
                if sizes is None:
                    continue
                empirical, total = enumerate_pairs(m, n, sizes)
                assert empirical == predicted(m, n), (m, n, sizes, empirical, predicted(m, n))
                assert total == (2**k + 3**m + 3**n - 2**m - 2**n - 1)
                brute_cases += 1
                valuations_checked += 2**sum(sizes)
                pairs_checked += total
    profiles = {}
    for m in range(1, 16):
        for n in range(m, 16):
            profile = polynomial_profile(m, n)
            assert profile not in profiles or profiles[profile] == (m, n)
            profiles[profile] = (m, n)
            # Inverse theorem: degree = m+n, and after subtraction, degree = n-1.
            k = m + n
            h = [profile[i] - comb(k, i) + (i == 0) for i in range(k + 1)]
            degree = max(i for i, coefficient in enumerate(h) if coefficient)
            assert (degree + 1, k - degree - 1) == (n, m)
    print("VERIFY_OK brute_cases", brute_cases,
          "valuations", valuations_checked,
          "distinct_pairs", pairs_checked,
          "inverse_profiles", len(profiles))


if __name__ == "__main__":
    run()
