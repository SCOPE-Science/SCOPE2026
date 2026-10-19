#!/usr/bin/env python3
"""Independent exact tests for the minimal-absent-subsequence run theorem."""
from collections import defaultdict
from itertools import product


def fibonacci(n):
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x + y
    return x


def direct_minimal_absent(word):
    # Explicitly build every DISTINCT subsequence; no greedy transitions used.
    present = {""}
    for symbol in word:
        present.update(x + symbol for x in tuple(present))
    missing = set()
    for x in present:
        for symbol in '01':
            candidate = x + symbol
            if candidate in present:
                continue
            if all(candidate[:i] + candidate[i + 1:] in present
                   for i in range(len(candidate))):
                missing.add(candidate)
    return missing


def greedy_path_count(word):
    """Count independently via the published greedy-pair criterion."""
    n = len(word)
    nxt = [[n, n] for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        nxt[i] = nxt[i + 1].copy()
        nxt[i][int(word[i])] = i
    paths = defaultdict(int)
    ending = [0, 0]
    for s in range(2):
        if nxt[0][s] == n:
            ending[s] += 1
        else:
            paths[(-1, nxt[0][s])] += 1
    for p in range(n):
        for a in range(-1, p):
            multiplicity = paths[(a, p)]
            if not multiplicity:
                continue
            allowed = word[a + 1:p + 1]
            for symbol in range(2):
                if str(symbol) not in allowed:
                    continue
                next_position = nxt[p + 1][symbol]
                if next_position == n:
                    ending[symbol] += multiplicity
                else:
                    paths[(p, next_position)] += multiplicity
    return tuple(ending)


def run_word(lengths, first='0'):
    return ''.join(str((int(first) + i) % 2) * length
                   for i, length in enumerate(lengths))


def check_case(lengths, direct=True):
    word = run_word(lengths)
    r = len(lengths)
    endings = greedy_path_count(word)
    final_symbol = (r - 1) % 2
    assert endings[final_symbol] == fibonacci(r), (lengths, endings)
    assert endings[1 - final_symbol] == fibonacci(r + 1), (lengths, endings)
    assert sum(endings) == fibonacci(r + 2)
    if direct:
        brute = direct_minimal_absent(word)
        counts = (sum(w.endswith('0') for w in brute),
                  sum(w.endswith('1') for w in brute))
        assert counts == endings, (lengths, counts, endings)
        # Complementation symmetry independently tests arbitrary first symbol.
        assert greedy_path_count(run_word(lengths, '1')) == endings[::-1]


def main():
    num_direct = 0
    for r in range(2, 7):
        for lengths in product((2, 3), repeat=r):
            check_case(lengths)
            num_direct += 1
    # Check large and highly nonuniform runs without enumerating subsequences.
    for r in range(2, 26):
        check_case(tuple(2 + (i * i + 3 * r) % 13 for i in range(r)), direct=False)
    assert len(direct_minimal_absent('0011')) == 3
    print('ALL_FIBONACCI_RUN_MAS_CHECKS_PASSED',
          'independent_direct_cases', num_direct,
          'nonuniform_large_run_cases', 24)


if __name__ == '__main__':
    main()
