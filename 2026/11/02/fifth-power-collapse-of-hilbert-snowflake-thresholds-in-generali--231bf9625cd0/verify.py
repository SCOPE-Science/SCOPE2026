"""Standalone finite consistency checks for the generalized-hexagon negative-type theorem.

Uses only the Python standard library. This finite verification supplements, but
cannot replace, the uniform analytic proof in RESULT.md.
"""
from decimal import Decimal, localcontext
from fractions import Fraction


def add(a, b):
    return [((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0))
            for i in range(max(len(a), len(b)))]


def scale(a, k):
    return [v * k for v in a]


def mul(a, b):
    r = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r


def val(a, x):
    ans = 0
    for c in reversed(a):
        ans = ans * x + c
    return ans


def polys(q):
    p = [[Fraction(1)], [Fraction(0), Fraction(1)]]
    for j in range(1, 6):
        back = q + 1 if j == 1 else q
        divisor = q + 1 if j == 5 else 1
        p.append(scale(add(mul(p[j], [0, 1]), scale(p[j-1], -back)), Fraction(1, divisor)))
    return p


def spectrum(q, t, prec=65):
    with localcontext() as ctx:
        ctx.prec = prec
        x = Decimal(t)
        p0, p1 = Decimal(1), x
        p = [p0, p1]
        for j in range(1, 6):
            back = q + 1 if j == 1 else q
            div = q + 1 if j == 5 else 1
            p.append((x * p[j] - Decimal(back) * p[j-1]) / Decimal(div))
        return p


def power_sum(p, exponent):
    return sum((Decimal(j).ln() * exponent).exp() * p[j]
               for j in range(1, 7))


def root(q):
    with localcontext() as ctx:
        ctx.prec = 75
        kvals = [Decimal((q+1) * q**(j-1) * (-1)**j)
                 for j in range(1, 6)] + [Decimal(q**5)]
        def ff(x):
            return sum((Decimal(j).ln()*x).exp()*kvals[j-1]
                       for j in range(1, 7))
        lo, hi = Decimal(0), Decimal(10) / Decimal(q)**5
        assert ff(lo) == -1 and ff(hi) > 0
        for _ in range(200):
            mid = (lo+hi)/2
            if ff(mid) < 0:
                lo = mid
            else:
                hi = mid
        return (lo+hi)/2


def run():
    identities = 0
    for q in range(2, 130):
        p = polys(q)
        shell = [1]+[(q+1)*q**(j-1) for j in range(1, 6)]+[q**5]
        assert [val(v, q+1) for v in p] == shell
        assert [val(v, -q-1) for v in p] == [(-1)**j*shell[j] for j in range(7)]
        # Characteristic recurrence, verified as a polynomial identity at each q.
        r = add(mul(p[6], [0, 1]), scale(p[5], -q))
        f = mul([0, -1], mul([q, 0, -1], mul([3*q, 0, -1],
            mul([q+1, -1], [q+1, 1]))))
        f = scale(f, Fraction(1, q+1))
        assert add(r, scale(f, -1)) == [0]*len(r)
        # Distance matrices sum to J, so sum P_j vanishes at other roots.
        s = [Fraction(0)]
        for pj in p:
            s = add(s, pj)
        expect = scale(mul([0,1], mul([q,0,-1],
            mul([3*q,0,-1], [q+1,1]))), Fraction(1,q+1))
        assert add(s, scale(expect, -1)) == [0]*len(s)
        identities += 4

    spectral = 0
    with localcontext() as ctx:
        ctx.prec = 75
        L = (Decimal(6)/Decimal(5)).ln()
        A = (Decimal(5)/Decimal(4)).ln()
        for q in [100, 101, 127, 128, 256, 512, 1000]:
            alpha = root(q)
            approx = Decimal(1)/(Decimal(q)**5*L) + A/(Decimal(q)**6*L**2)
            assert abs(alpha - approx) < Decimal(1) / Decimal(q)**7
            for x in [Decimal(3*q).sqrt(), Decimal(q).sqrt(), Decimal(0),
                      -Decimal(q).sqrt(), -Decimal(3*q).sqrt()]:
                assert power_sum(spectrum(q, x, 85), alpha) < Decimal('-.9')
                spectral += 1
        # Additional small orders are exploratory, not a uniform certificate.
        for q in range(2, 21):
            alpha = root(q)
            for x in [Decimal(3*q).sqrt(), Decimal(q).sqrt(), Decimal(0),
                      -Decimal(q).sqrt(), -Decimal(3*q).sqrt()]:
                assert power_sum(spectrum(q, x, 85), alpha) < Decimal(0)
                spectral += 1
    print('CHECK_OK exact_polynomial_identities=', identities,
          'finite_spectral_checks=', spectral,
          'uniform_proof_applies_q>=100')

if __name__ == '__main__':
    run()
