#!/usr/bin/env python3
from math import floor


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def convolve(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def trim(v):
    while len(v) > 1 and v[-1] == 0:
        v.pop()
    return v


def hstar_direct(r, a, b):
    Q = r + a + b
    q = [1] * (r - 1) + [a, b]
    out = [0] * (r + 2)
    for m in range(Q):
        w = m - sum((m * qi) // Q for qi in q)
        assert 0 <= w < len(out), (r, a, b, m, w)
        out[w] += 1
    return trim(out)


def predicted_boundary_hstar(r, t):
    assert (2 * r) % t == 0
    a = 2 * r // t
    if t % 2 == 0:
        c = t // 2
        base = [1] + [2] * c + [1]
        shifts = [0] * ((a - 1) * c + 1)
        for j in range(a):
            shifts[j * c] = 1
    else:
        assert r % t == 0
        p = r // t
        u = (t + 1) // 2
        base = [1] + [2] * t + [1]
        base[u] += 2
        shifts = [0] * ((p - 1) * t + 1)
        for j in range(p):
            shifts[j * t] = 1
    return trim(convolve(shifts, base))


def is_unimodal(v):
    # A weakly unimodal sequence can have a plateau. Check every possible peak cut.
    for k in range(len(v)):
        if all(v[i] <= v[i + 1] for i in range(k)) and all(v[i] >= v[i + 1] for i in range(k, len(v) - 1)):
            return True
    return False


def predicted_unimodal(r, t):
    a = 2 * r // t
    if t in (1, 2, 4):
        return True
    if t % 2 == 1:
        return r == t
    return a <= 2


def age_numerators(r, a, b):
    for j in range(1, a):
        yield r * j + (j * b) % a, a
    for j in range(1, b):
        yield r * j + (j * a) % b, b


def canonical_terminal_direct(r, a, b):
    pairs = list(age_numerators(r, a, b))
    canonical = all(num >= den for num, den in pairs)
    terminal = all(num > den for num, den in pairs)
    return canonical, terminal


def gorenstein(r, a, b):
    Q = r + a + b
    return Q % a == 0 and Q % b == 0


def predicted_gorenstein_boundary(r):
    ans = {(r, r)}
    for t in divisors(2 * r):
        a = 2 * r // t
        ans.add((a, r + a))
    return ans


def main():
    # Independent boundary reconstruction in a box containing the canonical triangle.
    for r in range(2, 61):
        actual = set()
        for a in range(1, 2 * r + 1):
            for b in range(a, 3 * r + 1):
                if not gorenstein(r, a, b):
                    continue
                can, term = canonical_terminal_direct(r, a, b)
                if can and not term:
                    actual.add((a, b))
        expected = predicted_gorenstein_boundary(r)
        assert actual == expected, (r, sorted(actual ^ expected))

    # Direct h* floor formula versus closed products and threshold.
    for r in range(2, 401):
        for t in divisors(2 * r):
            a = 2 * r // t
            b = r + a
            direct = hstar_direct(r, a, b)
            closed = predicted_boundary_hstar(r, t)
            assert direct == closed, (r, t, direct, closed)
            assert sum(direct) == r + a + b
            assert direct == list(reversed(direct))  # reflexive symmetry
            assert is_unimodal(direct) == predicted_unimodal(r, t), (r, t, direct)

        direct_equal = hstar_direct(r, r, r)
        closed_equal = convolve([1] * r, [1, 1, 1])
        assert direct_equal == closed_equal, (r, direct_equal, closed_equal)
        assert is_unimodal(direct_equal)
        assert direct_equal == list(reversed(direct_equal))

    print('VERIFY_OK r=2..400; boundary r=2..60; exact h*-factorizations and unimodality criterion agree')


if __name__ == '__main__':
    main()
