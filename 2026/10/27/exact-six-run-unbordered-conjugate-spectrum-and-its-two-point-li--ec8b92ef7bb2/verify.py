"""Independent finite checks for the six-run unbordered-conjugate spectrum.

Requires only Python 3 standard library. Exact polynomial equalities use integer
coefficient arithmetic; the infinite proof is in RESULT.md.
"""
from collections import Counter
from itertools import product
from math import comb


def unbordered_bruteforce(s):
    n = len(s)
    return sum(not any((s[i:] + s[:i])[:k] == (s[i:] + s[:i])[-k:]
                       for k in range(1, n)) for i in range(n))


def predicted(a, b, c, d, e, f):
    return sum((a > e or b < f,
                b > f or c < a,
                c > a or d < b,
                d > b or e < c,
                e > c or f < d,
                f > d or a < e))


def multiply(x, y):
    result = [0] * (len(x) + len(y) - 1)
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            result[i + j] += a * b
    return result


def add(x, y):
    n = max(len(x), len(y))
    return [(x[i] if i < len(x) else 0) +
            (y[i] if i < len(y) else 0) for i in range(n)]


def shift(x, k):
    return [0] * k + x


def pow_poly(poly, k):
    p = [1]
    for _ in range(k):
        p = multiply(p, poly)
    return p


def order_patterns():
    return sorted(v for v in product(range(3), repeat=3)
                  if set(v) == set(range(max(v) + 1)))


def pattern_weight(p):
    # Each level strictly exceeds the previous positive level by >=1.
    m = [p.count(j) for j in range(max(p) + 1)]
    tails = [sum(m[j:]) for j in range(len(m))]
    return sum(tails), Counter(tails)


def check_rational_spectrum():
    # Common denominator D=(1-z)^2(1-z^2)^2(1-z^3)^2.
    poly = {k: [1] + [0] * (k - 1) + [-1] for k in (1, 2, 3)}
    found = {j: [0] for j in range(7)}
    pats = order_patterns()
    assert len(pats) == 13
    for A in pats:
        pow_a, exp_a = pattern_weight(A)
        for B in pats:
            pow_b, exp_b = pattern_weight(B)
            a, c, e = A
            b, d, f = B
            j = predicted(a, b, c, d, e, f)
            exps = exp_a + exp_b
            assert all(exps[k] <= 2 for k in (1, 2, 3))
            q = [1]
            for k in (1, 2, 3):
                q = multiply(q, pow_poly(poly[k], 2 - exps[k]))
            found[j] = add(found[j], shift(q, pow_a + pow_b))

    # All rational generating functions are checked in the same denominator D.
    # The j=0 expression is z^6/(1-z^3)^2.
    expected = {
        0: multiply(shift([1], 6), multiply(pow_poly(poly[1], 2), pow_poly(poly[2], 2))),
        2: multiply(shift([6, 12, -6, -9], 7), pow_poly(poly[1], 2)),
        3: multiply(shift([6, 30, -6, -18], 8), poly[1]),
        4: shift([3, 6, 30, -6, -15], 8),
        5: shift([12, 6], 11)
    }
    for j in range(7):
        target = expected.get(j, [0])
        n = max(len(found[j]), len(target))
        assert (found[j] + [0] * (n - len(found[j])) ==
                target + [0] * (n - len(target))), (j, found[j], target)
    D = [1]
    for k in (1, 2, 3):
        D = multiply(D, pow_poly(poly[k], 2))
    L = [0]
    for j in range(7):
        L = add(L, found[j])
    # Since sum_j F_j=z^6/(1-z)^6, multiply by D to get z^6(1-z^2)^2(1-z^3)^2.
    expected_total = shift(multiply(pow_poly([1, 1], 2), pow_poly([1, 1, 1], 2)), 6)
    n = max(len(L), len(expected_total))
    assert L + [0]*(n-len(L)) == expected_total + [0]*(n-len(expected_total))
    return found


def main():
    total = 0
    for a, b, c, d, e, f in product(range(1, 5), repeat=6):
        s = '0'*a + '1'*b + '0'*c + '1'*d + '0'*e + '1'*f
        assert unbordered_bruteforce(s) == predicted(a, b, c, d, e, f), (a,b,c,d,e,f)
        total += 1
    found = check_rational_spectrum()
    for n in range(6, 19):
        actual = Counter()
        for vals in product(range(1, n-4), repeat=5):
            if sum(vals) >= n:
                continue
            p = (*vals, n-sum(vals))
            if p[-1] < 1:
                continue
            actual[predicted(*p)] += 1
        assert sum(actual.values()) == comb(n-1, 5)
        # Check the distributions against the rational generating functions by
        # multiplying their numerator with the inverse-denominator series.
        for j in range(7):
            numerator = found[j]
            # coefficients of (1-z)^-2 (1-z^2)^-2 (1-z^3)^-2
            coeff = 0
            for u in range(n+1):
                for v in range((n-u)//2+1):
                    rem = n-u-2*v
                    for t in range(rem//3+1):
                        m = u+2*v+3*t
                        if m <= n and n-m < len(numerator):
                            coeff += (u+1)*(v+1)*(t+1)*numerator[n-m]
            assert actual[j] == coeff, (n,j,actual[j],coeff)
    print(f'VERIFY_OK rotations={total} weak_order_pairs=169 generating_functions=5 fixed_lengths=6..18')

if __name__ == '__main__':
    main()
