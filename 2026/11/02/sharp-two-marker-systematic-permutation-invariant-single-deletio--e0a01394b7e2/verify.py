"""Stand-alone certificate checker for short full-systematic permutation codes.

Run: python3 verify.py
Requires only codebooks.json in the same directory and Python standard library.
"""
import itertools
import json
import math
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CODEBOOKS = json.loads((ROOT / 'codebooks.json').read_text(encoding='utf-8'))


def standardize(sequence):
    """Return the 0-based rank permutation induced by distinct entries."""
    return tuple(sorted(sequence).index(x) for x in sequence)


def standardize_independent(sequence):
    """Independent rank implementation, using pairwise comparisons."""
    return tuple(sum(y < x for y in sequence) for x in sequence)


def descendants(word, method=standardize):
    return {method(word[:j] + word[j + 1:]) for j in range(len(word))}


def check_code(n):
    strings = CODEBOOKS[str(n)]
    code = [tuple(int(c) for c in word) for word in strings]
    assert len(code) == math.factorial(n) == len(set(code))
    assert all(len(w) == n + (1 if n == 2 else 2) for w in code)
    length = len(code[0])
    assert all(set(w) == set(range(1, length + 1)) for w in code)
    messages = {tuple(c for c in w if c <= n) for w in code}
    assert messages == set(itertools.permutations(range(1, n + 1)))
    owner = {}
    hist = Counter()
    for w in code:
        d1 = descendants(w)
        d2 = descendants(w, standardize_independent)
        assert d1 == d2
        hist[len(d1)] += 1
        for child in d1:
            assert child not in owner, (n, owner.get(child), w, child)
            owner[child] = w
    print('n=%s codewords=%s distinct_PID_descendants=%s total_possible=%s deck_histogram=%s' %
          (n, len(code), len(owner), math.factorial(length - 1), sorted(hist.items())))


def check_single_child_characterization():
    for length in range(3, 8):
        singleton = []
        comparisons = 0
        for word in itertools.permutations(range(1, length + 1)):
            if len(descendants(word)) == 1:
                singleton.append(word)
            for i in range(length - 1):
                s0 = standardize(word[:i] + word[i + 1:])
                s1 = standardize(word[:i + 1] + word[i + 2:])
                assert (s0 == s1) == (abs(word[i] - word[i + 1]) == 1)
                comparisons += 1
        assert singleton == [tuple(range(1, length + 1)),tuple(range(length, 0, -1))] or set(singleton) == {tuple(range(1,length+1)),tuple(range(length,0,-1))}
        print('length=%s singleton_decks=2 adjacent_delete_comparisons=%s' % (length, comparisons))


if __name__ == '__main__':
    for k in (2, 3, 4):
        check_code(k)
    check_single_child_characterization()
    print('VERIFY_OK')
