"""Standalone finite checks for three-marker circular k-spectrum reconstruction.
Only finite cases are tested; the accompanying proof establishes the infinite assertions.
"""
from collections import Counter, defaultdict
from itertools import combinations


def necklace(bits):
    n = len(bits)
    return min(tuple(bits[i:] + bits[:i]) for i in range(n))


def all_necklaces(n):
    return sorted({necklace([int(i in s) for i in range(n)])
                   for s in combinations(range(n), 3)})


def gap_tuple(w):
    n = len(w)
    positions = [i for i, bit in enumerate(w) if bit]
    assert len(positions) == 3
    return tuple((positions[(i + 1) % 3] - positions[i] - 1) % n
                 for i in range(3))


def spectrum(word, k):
    n = len(word)
    return tuple(sorted(Counter(tuple(word[(start + j) % n]
                                      for j in range(k))
                                for start in range(n)).items()))


def reverse_necklace(w):
    return necklace(list(reversed(w)))


def run_tests():
    # Complete census of all weight-three necklaces and read lengths through 25.
    census = 0
    deck_comp = 0
    for n in range(3, 26):
        words = all_necklaces(n)
        kstar = 1 if n <= 4 else (2 if n == 5 else (2 * n) // 3)
        for k in range(1, kstar + 1):
            fibers = defaultdict(list)
            for w in words:
                fibers[spectrum(w, k)].append(w)
                deck_comp += 1
            assert (len(fibers) == len(words)) == (k >= kstar), (n, k, len(fibers), len(words))
        census += len(words)

    # Verify the proposed exact per-necklace threshold for every chiral triple.
    chiral = 0
    for n in range(6, 51):
        for w in all_necklaces(n):
            gaps = gap_tuple(w)
            if len(set(gaps)) < 3:
                continue
            M = max(gaps)
            k = n - M
            assert w != reverse_necklace(w)
            assert spectrum(w, k - 1) == spectrum(reverse_necklace(w), k - 1), (n, gaps)
            assert spectrum(w, k) != spectrum(reverse_necklace(w), k), (n, gaps)
            chiral += 1
            deck_comp += 2

    # The explicit sharpness pair for each residue class, including the smallest cases.
    witnesses = 0
    for m in range(2, 65):
        for residue in (0, 1, 2):
            n = 3 * m + residue
            if residue == 0:
                x, y, M = m - 2, m - 1, m
            elif residue == 1:
                x, y, M = m - 2, m - 1, m + 1
            else:
                x, y, M = m - 2, m, m + 1
            assert x < y < M and x + y + M + 3 == n
            w = tuple([1] + [0] * x + [1] + [0] * y + [1] + [0] * M)
            v = reverse_necklace(w)
            assert necklace(list(w)) != v
            k = (2 * n) // 3
            assert k == n - M
            assert spectrum(w, k - 1) == spectrum(v, k - 1)
            assert spectrum(w, k) != spectrum(v, k)
            witnesses += 1
            deck_comp += 2

    # Validate the constructive decoder directly: a triple-one window fixes all gaps;
    # otherwise frequencies of 10^d1 recover the gap multiset.
    decoded = 0
    for n in range(6, 31):
        k = 2 * n // 3
        for w in all_necklaces(n):
            sp = dict(spectrum(w, k))
            with_three = [pattern for pattern, count in sp.items()
                          if sum(pattern) == 3 and count]
            if with_three:
                pattern = with_three[0]
                ones = [j for j, bit in enumerate(pattern) if bit]
                gaps = [ones[1] - ones[0] - 1,
                        ones[2] - ones[1] - 1,
                        n - (ones[2] - ones[0] + 1)]
                assert necklace([1] + [0] * gaps[0] + [1] + [0] * gaps[1]
                                + [1] + [0] * gaps[2]) == w
            else:
                short_gap_counts = []
                for d in range(k - 1):
                    c = sum(count for pattern, count in sp.items()
                            if len(pattern) >= d + 2 and
                            # marginalizing over all length-k factors
                            pattern[:d + 2] == (1,) + (0,) * d + (1,))
                    short_gap_counts.extend([d] * c)
                assert len(short_gap_counts) == 3, (n, w, k, short_gap_counts)
                assert sorted(short_gap_counts) == sorted(gap_tuple(w))
                assert len(set(short_gap_counts)) <= 2
            decoded += 1
    print(f'VERIFY_OK exhaustive_necklaces={census} exact_all_length_thresholds_n=3..25 '
          f'chiral_orientation_cases={chiral} explicit_sharpness_pairs={witnesses} '
          f'decoder_cases={decoded} spectrum_comparisons={deck_comp}')


if __name__ == '__main__':
    run_tests()
