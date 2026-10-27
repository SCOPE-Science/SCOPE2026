"""Reproducible finite checks of two-perfect-matching temporal forcing formulas.

Uses direct synchronous forcing on each snapshot, independently of the
closed cyclic-gap enumerator. Requires only the Python standard library.
"""
from itertools import product
from math import comb


def coefficient(s, r, d):
    if d < 0:
        return 0
    a = [1] + [0] * d
    for _ in range(s):
        b = [0] * (d + 1)
        for j in range(d + 1):
            b[j] = sum(a[j - h] for h in range(min(j, r - 1) + 1))
        a = b
    return a[d]


def cycle_poly(m, runs):
    p = [0] * (2 * m + 1)
    for s in range(1, m + 1):
        num = m * coefficient(s, runs, m - s)
        assert num % s == 0
        choices = num // s
        for j in range(s + 1):
            p[s + j] += choices * comb(s, j) * 2 ** (s - j)
    return p


def poly_product(polys):
    out = [1]
    for p in polys:
        tmp = [0] * (len(out) + len(p) - 1)
        for i, a in enumerate(out):
            for j, b in enumerate(p):
                tmp[i + j] += a * b
        out = tmp
    return out


def pair_matchings(cycles):
    # Component m: alternating matchings of a 2m-cycle; m=1 means a shared edge.
    n = 2 * sum(cycles)
    out = [[], []]
    offset = 0
    for m in cycles:
        for j in range(m):
            out[0].append((offset + 2 * j, offset + 2 * j + 1))
            out[1].append((offset + 2 * j + 1, offset + (2 * j + 2) % (2 * m)))
        offset += 2 * m
    assert len(out[0]) == n // 2
    return out


def direct_corrupt(n, matchings, word, seed):
    mask = seed
    for label in word:
        for a, b in matchings[label]:
            if mask & ((1 << a) | (1 << b)):
                mask |= (1 << a) | (1 << b)
    return mask


def has_bounded_cyclic_gaps(active, m, runs):
    if not active:
        return False
    return all((active[(j + 1) % len(active)] - active[j]) % m <= runs
               if len(active) > 1 else m <= runs
               for j in range(len(active)))


def direct_gap_condition(cycles, word, seed):
    runs = 1 + sum(word[t] != word[t - 1] for t in range(1, len(word)))
    first = word[0]
    offset = 0
    for m in cycles:
        active = []
        for i in range(m):
            # Reference pairs are the first snapshot's matching.
            if first == 0:
                a, b = offset + 2 * i, offset + 2 * i + 1
            else:
                a, b = offset + 2 * i + 1, offset + (2 * i + 2) % (2 * m)
            if seed & ((1 << a) | (1 << b)):
                active.append(i)
        if not has_bounded_cyclic_gaps(active, m, runs):
            return False
        offset += 2 * m
    return True


def main():
    cases = subsets = words = 0
    families = [(m,) for m in range(1, 7)] + [
        (1, 1), (1, 2), (2, 2), (1, 3), (2, 3), (1, 1, 2)]
    for cycles in families:
        n = 2 * sum(cycles)
        matchings = pair_matchings(cycles)
        for length in range(1, 6 if n <= 8 else 5):
            for word in product((0, 1), repeat=length):
                runs = 1 + sum(word[t] != word[t - 1] for t in range(1, length))
                pred = poly_product([cycle_poly(m, runs) for m in cycles])
                actual = [0] * (n + 1)
                for seed in range(1 << n):
                    success = direct_corrupt(n, matchings, word, seed) == (1 << n) - 1
                    assert success == direct_gap_condition(cycles, word, seed), (cycles, word, seed)
                    if success:
                        actual[seed.bit_count()] += 1
                    subsets += 1
                assert actual == pred, (cycles, word, actual, pred)
                cases += 1
                words += 1
    print('VERIFY_OK', 'schedule_graph_cases', cases, 'initial_sets_checked', subsets)

if __name__ == '__main__':
    main()
