#!/usr/bin/env python3
"""Independent finite checks of the RLL binary subsequence-universality formula.
Run with Python 3.10+; no third-party dependencies.
"""
from collections import defaultdict
from itertools import product
from functools import lru_cache


def polynomial_product(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


@lru_cache(maxsize=None)
def _formula_polynomial(R, k):
    A = [1] * R
    T = [2] * (R - 1) + [1] if R > 1 else [1]
    p = A
    for _ in range(k - 1):
        p = polynomial_product(p, T)
    return tuple(polynomial_product(p, [1] + T))


def exact_formula(R, n, k):
    if R < 1 or n < 0 or k < 0:
        raise ValueError('outside parameter domain')
    if k == 0:
        return int(n == 0) if n == 0 else (2 if 1 <= n <= R else 0)
    p = _formula_polynomial(R, k)
    i = n - 2 * k
    return 2 * p[i] if 0 <= i < len(p) else 0


def subsequence_present(pattern, w):
    i = 0
    for c in w:
        if i < len(pattern) and pattern[i] == c:
            i += 1
    return i == len(pattern)


def universality_direct(w):
    k = 0
    while all(subsequence_present(t, w) for t in product('01', repeat=k+1)):
        k += 1
    return k


def valid_run_limit(w, R):
    cur = 0
    previous = None
    for c in w:
        cur = cur + 1 if c == previous else 1
        if cur > R:
            return False
        previous = c
    return True


def counts_from_independent_automaton(R, max_n):
    # Track last bit, current run length, and greedy-arch symbol seen so far:
    # unseen = -1, seen = 0 or 1; completed arch count is the u-exponent.
    state_counts = {(None, 0, -1, 0): 1}
    out = [{0: 1}]
    for n in range(1, max_n + 1):
        nxt = defaultdict(int)
        for (last, run, seen, arches), how_many in state_counts.items():
            for bit in (0, 1):
                r = run + 1 if bit == last else 1
                if r > R:
                    continue
                if seen == -1:
                    nxt[(bit, r, bit, arches)] += how_many
                elif seen != bit:
                    nxt[(bit, r, -1, arches + 1)] += how_many
                else:
                    nxt[(bit, r, seen, arches)] += how_many
        state_counts = nxt
        counts = defaultdict(int)
        for (_, _, _, arches), c in state_counts.items():
            counts[arches] += c
        out.append(counts)
    return out


def main():
    brute_checks = 0
    for R in range(1, 7):
        for n in range(0, 13):
            tab = defaultdict(int)
            for letters in product('01', repeat=n):
                w = ''.join(letters)
                if valid_run_limit(w, R):
                    tab[universality_direct(w)] += 1
                    brute_checks += 1
            for k in range(n + 1):
                assert exact_formula(R, n, k) == tab[k], (R, n, k)

    automaton_cells = 0
    for R in range(1, 13):
        independent = counts_from_independent_automaton(R, 96)
        for n, tab in enumerate(independent):
            for k in range(n + 1):
                assert exact_formula(R, n, k) == tab.get(k, 0), (R, n, k)
                automaton_cells += 1
            smallest = max(0, -((R - n) // (R + 1)))  # ceiling((n-R)/(R+1)), clipped
            assert min(k for k, count in tab.items() if count) == smallest, (R, n)
            if n > 0 and (n - R) % (R + 1) == 0:
                k = (n - R) // (R + 1)
                assert tab[k] == 2, (R, n, k)
    for R in range(1, 13):
        for k in range(0, 15):
            n = (R + 1) * k + R
            assert exact_formula(R, n, k) == 2, (R, n, k)
            assert exact_formula(R, n + 1, k) == 0, (R, n, k)
            w = '0' * R + ('1' + '0' * R) * k
            assert len(w) == n
            assert valid_run_limit(w, R)
            # direct greedy count for large patterns: two symbols close one arch
            seen = set()
            counted = 0
            for c in w:
                seen.add(c)
                if len(seen) == 2:
                    counted += 1
                    seen.clear()
            assert counted == k
    print('RLL_BINARY_UNIVERSALITY_PASS',
          'brute_words=',brute_checks,
          'brute_n=0..12','brute_R=1..6',
          'automaton_cells=',automaton_cells,
          'automaton_n=0..96', 'automaton_R=1..12',
          'extremal_k=0..14', sep=' ')


if __name__ == '__main__':
    main()
