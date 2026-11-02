"""Independent finite checks for a theorem on the low-factor-complexity word census.

Public scientific verification code, with no external dependencies.
Run: python3 verify.py
"""
from itertools import product
from math import gcd


def primitive_count(q, p):
    total = 0
    for d in range(1, p + 1):
        if p % d:
            continue
        # Moebius coefficient via square-free prime factorization.
        n, mu, r = d, 1, 2
        while r * r <= n:
            if n % r == 0:
                n //= r
                if n % r == 0:
                    mu = 0
                    break
                mu = -mu
            else:
                r += 1
        if mu and n > 1:
            mu = -mu
        total += mu * q ** (p // d)
    return total


def f(q, t):
    return 1 if t == 0 else (q - 1) * q ** (t - 1)


def expected(q, k):
    return sum(primitive_count(q, p) *
               sum(f(q, a) * f(q, b)
                   for a in range(k - p + 1)
                   for b in range(k - p - a + 1))
               for p in range(1, k + 1))


def complexity(word, k):
    return len({word[i:i + k] for i in range(len(word) - k + 1)})


def direct(q, k, n):
    return sum(complexity(w, k) <= k for w in product(range(q), repeat=n))


def primitive(v):
    p = len(v)
    return not any(p % d == 0 and all(v[i] == v[i % d] for i in range(p))
                   for d in range(1, p))


def normal_form_words(q, k, n):
    """Enumerate boundary-normal periodic cores, not arbitrary overlapping templates."""
    for p in range(1, k + 1):
        for v in product(range(q), repeat=p):
            if not primitive(v):
                continue
            for a in range(k - p + 1):
                for b in range(k - p - a + 1):
                    for left in product(range(q), repeat=a):
                        if a and left[-1] == v[-1]:
                            continue
                        for right in product(range(q), repeat=b):
                            middle_size = n - a - b
                            if b and right[0] == v[middle_size % p]:
                                continue
                            middle = tuple(v[i % p] for i in range(middle_size))
                            yield left + middle + right


def test():
    assert [expected(2, k) for k in range(1, 10)] == [2, 8, 28, 86, 250, 680, 1792, 4562, 11344]
    assert [expected(3, k) for k in range(1, 6)] == [3, 21, 117, 561, 2481]
    assert [expected(4, k) for k in range(1, 5)] == [4, 40, 304, 1972]

    # Formula simplification: coefficient of (1-z)/(1-qz)^2.
    for q in range(1, 8):
        for m in range(9):
            h = sum(f(q, a) * f(q, b) for a in range(m + 1) for b in range(m + 1 - a))
            rhs = 1 if m == 0 else (m + 1) * q ** m - m * q ** (m - 1)
            assert h == rhs

    # Independent literal enumeration of full q-ary word spaces.
    cases = [(2, k, 2 * k + j) for k in range(1, 9) for j in (0, 1) if 2 * k + j <= 17]
    cases += [(3, k, 2 * k + j) for k in range(1, 5) for j in (0, 1, 2)]
    cases += [(4, k, 2 * k + j) for k in range(1, 4) for j in (0, 1)]
    cases += [(5, 3, 6)]
    for q, k, n in cases:
        got = direct(q, k, n)
        want = expected(q, k)
        assert got == want, (q, k, n, got, want)
    print('EXHAUSTIVE_CASES_OK', len(cases))

    # Separate canonical-core reconstruction; duplicate-free and complete by comparison
    # with literal enumeration in the overlap range.
    tests = [(2, k, 2 * k + j) for k in range(1, 9) for j in range(3)]
    tests += [(3, k, 2 * k + j) for k in range(1, 6) for j in range(3)]
    tests += [(4, k, 2 * k + j) for k in range(1, 5) for j in range(2)]
    for q, k, n in tests:
        forms = list(normal_form_words(q, k, n))
        assert len(forms) == len(set(forms)), (q, k, n, 'duplicate')
        assert len(forms) == expected(q, k), (q, k, n, 'formula')
        assert all(complexity(w, k) <= k for w in forms), (q, k, n, 'invalid')
    print('NORMAL_FORM_CASES_OK', len(tests))
    print('BINARY_CENSUS', [expected(2, k) for k in range(1, 10)])
    print('TERNARY_CENSUS', [expected(3, k) for k in range(1, 6)])
    print('QUATERNARY_CENSUS', [expected(4, k) for k in range(1, 5)])
    print('VERIFY_OK')


if __name__ == '__main__':
    test()
