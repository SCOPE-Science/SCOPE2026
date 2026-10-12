"""Finite checks for fixed-observer symbol-locality-one permutation families.
Run with Python 3.9 or later: python verify.py.
The general theorem is established by the proof, not these finite tests.
"""
from itertools import permutations, product
from math import factorial


def exact_limit(n):
    if n % 2 == 0:
        m = n // 2
        return 2**m * factorial(m)
    m = n // 2
    return n * 2**(m-1) * factorial(m-1)


def construct(n):
    if n < 2:
        raise ValueError('n must be at least 2')
    if n % 2 == 0:
        pairs = [tuple(range(2*k, 2*k+2)) for k in range(n//2)]
        f = list(range(n))
        for a, b in pairs:
            f[a], f[b] = b, a
        observer = tuple(i+1 if i % 2 == 0 else i-1 for i in range(n))
        repair = tuple(f for _ in range(n))
        for ordering in permutations(pairs):
            for orientation in product(range(2), repeat=len(pairs)):
                word = tuple(v for p,flip in zip(ordering,orientation)
                             for v in (p if flip == 0 else p[::-1]))
                yield word, observer, repair
    else:
        pairs = [(2*k+1, 2*k+2) for k in range(n//2)]
        f = list(range(n))
        f[:3] = [1, 2, 0]
        for a,b in pairs[1:]:
            f[a],f[b] = b,a
        inverse_f = [0]*n
        for a,b in enumerate(f): inverse_f[b] = a
        g = [f[y] if y < 3 else 0 for y in range(n)]
        h = list(range(n))
        for a,b in pairs: h[a],h[b] = b,a
        obs = (1,0,1) + tuple(4+2*k if i%2 == 0 else 3+2*k
                              for k in range((n-3)//2) for i in (0,1))
        repair = (inverse_f, f, g) + tuple(h for _ in range(n-3))
        for r in range(n):
            triple = (r, f[r], g[f[r]])
            used = set(triple)
            rest = [p for p in pairs if p[0] not in used and p[1] not in used]
            assert len(rest) == (n-3)//2
            for ordering in permutations(rest):
                for orientation in product(range(2), repeat=len(rest)):
                    suffix = tuple(v for p,flip in zip(ordering,orientation)
                                   for v in (p if flip == 0 else p[::-1]))
                    yield triple + suffix, obs, repair


def main():
    for n in range(2,12):
        words = set()
        count = 0
        for word, observers, recovery in construct(n):
            assert sorted(word) == list(range(n)), ('not a permutation', n, word)
            assert len(observers) == n == len(recovery)
            for i in range(n):
                assert i != observers[i]
                assert word[i] == recovery[i][word[observers[i]]], (n, word, i)
            words.add(word)
            count += 1
        expected = exact_limit(n)
        assert count == expected == len(words), (n, count, len(words), expected)
        print('PASS n=%d codewords=%d' % (n, expected))


if __name__ == '__main__': main()
