"""Independent finite checks for longest letter-duplicated subsequences.

No external packages or input files. Python 3.10+.
The proofs for arbitrary lengths are given separately in RESULT.md.
"""
from itertools import product
from collections import Counter

NEG = -10**9


def is_ld(word):
    if len(word) < 2:
        return False
    run = 1
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            run += 1
        else:
            if run < 2:
                return False
            run = 1
    return run >= 2


def all_ld_subseq(word):
    """Explicit subsets of positions; only intended for short input."""
    n = len(word)
    out = set()
    for mask in range(1 << n):
        p = tuple(word[i] for i in range(n) if mask & (1 << i))
        if is_ld(p):
            out.add(p)
    return out


def dp_llds(word, q):
    """Independent two-state-per-symbol dynamic program."""
    complete = [NEG] * q
    pending = [NEG] * q
    for letter in word:
        prev_pending = pending[letter]
        prev_complete = complete[letter]
        pending[letter] = max(prev_pending, 1,
                              max([complete[c] + 1 for c in range(q) if c != letter],
                                  default=NEG))
        complete[letter] = max(prev_complete + 1, prev_pending + 1)
    return max(0, *complete)


def bound(n, q):
    t, s = divmod(n, q + 1)
    return 2 * t + (1 if t >= 1 and s == q else 0)


def first_embed(p, q):
    """Scan the infinite cyclic source; return the greedy final position."""
    position = 0
    for a in p:
        while (position % q) != a:
            position += 1
        position += 1
    return position


def first_embed_formula(p, q):
    if not p:
        return 0
    runs = []
    for a in p:
        if not runs or a != runs[-1][0]:
            runs.append([a, 1])
        else:
            runs[-1][1] += 1
    length = len(p)
    return (runs[0][0] + 1 + q * (length - len(runs))
            + sum((runs[j][0] - runs[j-1][0]) % q
                  for j in range(1, len(runs))))


def spectrum_by_recurrence(q, n_max):
    # E[n][length]: distinct LD words whose first cyclic embedding ends at n.
    # (1-z^q y-z^q(z+...+z^(q-1))y^2) E
    #      = z^q(z+...+z^q)y^2.
    E = [[0] * (n_max + 1) for _ in range(n_max + 1)]
    for n in range(1, n_max + 1):
        for length in range(2, n_max + 1):
            v = int(length == 2 and q + 1 <= n <= 2*q)
            if n >= q and length >= 1:
                v += E[n-q][length-1]
            if length >= 2:
                for delta in range(1, q):
                    if n >= q + delta:
                        v += E[n-q-delta][length-2]
            E[n][length] = v
    return E


def main():
    word_tests = 0
    for q, max_n in ((2, 13), (3, 9), (4, 7)):
        for n in range(max_n + 1):
            cyc = tuple(i % q for i in range(n))
            assert dp_llds(cyc, q) == bound(n, q), (q, n, 'cyclic')
            minimum = n
            for word in product(range(q), repeat=n):
                val = dp_llds(word, q)
                assert val >= bound(n, q), (q, n, word, val)
                if n <= 7:
                    all_out = all_ld_subseq(word)
                    assert val == max(map(len, all_out), default=0), (q, n, word)
                minimum = min(minimum, val)
                word_tests += 1
            assert minimum == bound(n, q), (q, n, minimum)

    subset_tests = 0
    recurrence_tests = 0
    for q, n_cap in ((2, 12), (3, 11), (4, 10), (5, 9)):
        E = spectrum_by_recurrence(q, 80)
        for n in range(n_cap + 1):
            cyc = tuple(i % q for i in range(n))
            outputs = all_ld_subseq(cyc)
            actual = Counter(map(len, outputs))
            for L in range(n+1):
                expected = sum(E[e][L] for e in range(n+1))
                assert expected == actual[L], (q, n, L, expected, actual[L])
                recurrence_tests += 1
            subset_tests += len(outputs)
        # Independent target-word construction checks first embedding.
        for L in range(2, 8):
            for p in product(range(q), repeat=L):
                if is_ld(p):
                    assert first_embed(p, q) == first_embed_formula(p, q), (q, p)
    print('LLDS_MINIMAX_SPECTRUM_PASS',
          'qary_source_words_tested=' + str(word_tests),
          'distinct_subsequence_occurrences_tested=' + str(subset_tests),
          'spectrum_entries_checked=' + str(recurrence_tests),
          'generating_coefficients_n=0..80',
          'q=2..5')


if __name__ == '__main__':
    main()
