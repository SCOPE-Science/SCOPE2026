"""Independent exhaustive checks for four-coordinate limited-permutation codes.

Python 3 standard library only; run `python3 verify.py`.
The infinite-alphabet statement is proved in RESULT.md, not by finite tests.
"""
from collections import Counter
from itertools import combinations, permutations

SWAP_SETS = ((), (0,), (1,), (2,), (0, 2))
SEEDS = {
    (4,): ("aaaa",),
    (3, 1): ("aaab", "baaa"),
    (2, 2): ("aabb", "bbaa"),
    (2, 1, 1): ("aabc", "acba", "bcaa"),
    (1, 1, 1, 1): ("abcd", "bcda", "cdab", "dabc"),
}


def ball(word):
    out = set()
    for swaps in SWAP_SETS:
        v = list(word)
        for i in swaps:
            v[i], v[i + 1] = v[i + 1], v[i]
        out.add(tuple(v))
    return frozenset(out)


def distinct_permutations(word):
    return sorted(set(permutations(word)))


def profile(word):
    return tuple(sorted(Counter(word).values(), reverse=True))


def separated(words):
    seen = set()
    for w in words:
        b = ball(w)
        if b & seen:
            return False
        seen.update(b)
    return True


def check_component(shape, seed):
    words = distinct_permutations(seed[0])
    optimum = len(seed)
    assert len(set(seed)) == optimum
    assert all(tuple(s) in words for s in seed)
    assert separated(seed)
    # A code with optimum+1 vertices would itself be a disjoint-ball packing.
    # Every size-(optimum+1) subset is examined, not just a sample.
    rejected = 0
    for sample in combinations(words, optimum + 1):
        assert not separated(sample), (shape, sample)
        rejected += 1
    return len(words), rejected


def total_code(q):
    A = tuple(range(q))
    code = []
    for a in A:
        code.append((a, a, a, a))
    for a in A:
        for b in A:
            if b != a:
                code.extend(((a, a, a, b), (b, a, a, a)))
    for a, b in combinations(A, 2):
        code.extend(((a, a, b, b), (b, b, a, a)))
    for a in A:
        for b, c in combinations((x for x in A if x != a), 2):
            code.extend(((a, a, b, c), (a, c, b, a), (b, c, a, a)))
    for a, b, c, d in combinations(A, 4):
        code.extend(((a, b, c, d), (b, c, d, a), (c, d, a, b), (d, a, b, c)))
    assert len(code) == q * q * (q + 1) * (q + 2) // 6
    assert len(set(code)) == len(code)
    assert separated(code)
    return len(code)


def main():
    expect = {(4,): (1, 0), (3, 1): (4, 4), (2, 2): (6, 20),
              (2, 1, 1): (12, 495), (1, 1, 1, 1): (24, 42504)}
    for shape, seeds in SEEDS.items():
        got = check_component(shape, seeds)
        assert got == expect[shape], (shape, got)
    for q, expected in [(2, 8), (3, 30), (4, 80), (5, 175), (6, 336)]:
        assert total_code(q) == expected
    print('VERIFY_OK; 43023 forbidden subsets; q=2..6 complete constructions')


if __name__ == '__main__':
    main()
