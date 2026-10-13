"""Finite replay of sharp forward-only modal-depth bounds on directed cycles.

Plain Python 3, standard library only. The proof for all sizes is in RESULT.md.
"""
from itertools import combinations, product
from math import gcd, lcm


def models(lengths):
    return [(r, word, word[-1]) for r in lengths
            for word in product((0, 1), repeat=r)]


def prefix(word, d):
    return tuple(word[i % len(word)] for i in range(d + 1))


def booleans_separate(data, d):
    seen = {}
    for _, word, truth in data:
        x = prefix(word, d)
        if x in seen and seen[x] != truth:
            return False
        seen[x] = truth
    return True


def positive_separate(data, d):
    true_words = [prefix(word, d) for _, word, truth in data if truth]
    false_words = [prefix(word, d) for _, word, truth in data if not truth]
    return not any(all(x <= y for x, y in zip(a, b))
                   for a in true_words for b in false_words)


def positive_formula(lengths, word):
    r = len(word)
    return any(all(word[(lcm(a, b) - 1) % r] for b in lengths)
               for a in lengths)


def binary_witness(n):
    assert n >= 2
    u = (1,) * (n - 2) + (0, 1)
    v = (1,) * (n - 2) + (0,)
    d = 2 * n - 4
    return prefix(u, d) == prefix(v, d) and u[-1] == 1 and v[-1] == 0


def positive_witness(r, s):
    l = lcm(r, s)
    first = tuple(int(i == r - 1) for i in range(r))
    second = tuple(int(i != s - 1) for i in range(s))
    return (first[-1] == 1 and second[-1] == 0 and
            all(first[i % r] <= second[i % s] for i in range(l - 1)) and
            first[(l - 1) % r] > second[(l - 1) % s])


def verify_set(lengths):
    data = models(lengths)
    l = max(lcm(a, b) for a in lengths for b in lengths)
    assert all(positive_formula(lengths, word) == bool(truth)
               for _, word, truth in data)
    assert positive_separate(data, l - 1)
    assert not positive_separate(data, l - 2) if l > 1 else True
    r, s = next((r, s) for r in lengths for s in lengths if lcm(r, s) == l)
    assert positive_witness(r, s)
    return len(data), l - 1


def main():
    total_sets = 0
    total_valuations = 0
    for n in range(1, 8):
        lengths = tuple(range(1, n + 1))
        data = models(lengths)
        bool_depth = max(0, 2 * n - 3)
        expected_positive_depth = 0 if n == 1 else n * (n - 1) - 1
        assert booleans_separate(data, bool_depth)
        assert (n == 1 or not booleans_separate(data, bool_depth - 1))
        assert n == 1 or binary_witness(n)
        size, positive_depth = verify_set(lengths)
        assert positive_depth == expected_positive_depth
        print(f"n={n} models={size} Boolean={bool_depth} positive={positive_depth}")
        total_sets += 1
        total_valuations += size
    for n in range(1, 7):
        for mask in range(1, 1 << n):
            lengths = tuple(r for r in range(1, n + 1) if mask & (1 << (r - 1)))
            count, _ = verify_set(lengths)
            total_sets += 1
            total_valuations += count
    print(f"VERIFY_OK sets={total_sets} valuations={total_valuations}")


if __name__ == "__main__":
    main()
