"""Exact-integer spot checks of the two-prime checkerboard zero relations.
Usage: python3 research07_gap_verifier.py. Requires only Python's standard library.
These finite checks corroborate, but do not prove, the general theorem.
"""
from itertools import combinations


def support(p, q, amask, bmask):
    n = 2 * p * q
    out = []
    for e in range(n):
        a = bool(amask & (1 << (e % p)))
        b = bool(bmask & (1 << (e % q)))
        if (e % 2 == 0 and a and b) or (e % 2 == 1 and not a and not b):
            out.append(e)
    return out


def vanishes(s, p, q):
    c = [[0] * q for _ in range(p)]
    for e in s:
        c[e % p][e % q] += 1 if e % 2 == 0 else -1
    return all(c[i][j] - c[i][0] - c[0][j] + c[0][0] == 0
               for i in range(p) for j in range(q))


def max_gap(s, n):
    return max((s[(i + 1) % len(s)] - s[i]) % n for i in range(len(s)))


def main():
    cases = [(3, 5), (3, 7), (3, 11), (5, 7)]
    count = 0
    for p, q in cases:
        n = 2 * p * q
        bound = q + 2*p - 1
        max_seen = 0
        witness = None
        for a in range(1, (1 << p) - 1):
            for b in range(1, (1 << q) - 1):
                s = support(p, q, a, b)
                assert vanishes(s, p, q)
                assert all(((e + n // 2) % n) not in s for e in s)
                g = max_gap(s, n)
                assert g <= bound
                if g > max_seen:
                    max_seen = g
                    witness = (a, b, s)
                count += 1
        assert max_seen == bound, (p, q, max_seen, bound)
        s = witness[2]
        # Independently check no nonempty proper zero subsum for two short cases.
        if len(s) <= 18:
            for k in range(1, len(s)):
                for v in combinations(s, k):
                    assert not vanishes(v, p, q), (p, q, witness, v)
        print('p', p, 'q', q, 'max_gap', max_seen,
              'min_diameter', n - max_seen, 'witness_weight', len(s))
    print('CERTIFICATE_OK configurations=', count)

if __name__ == '__main__':
    main()
