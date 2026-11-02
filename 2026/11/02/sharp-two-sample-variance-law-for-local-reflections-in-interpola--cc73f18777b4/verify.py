"""Exact and numerical reproducibility for two-sample interpolatory stratified quadrature.

Run: python verify.py
Uses only the Python standard library. The analytical theorem does not rely on this test.
"""
from fractions import Fraction as F
from math import comb

ZERO = F(0)
ONE = F(1)
HALF = F(1, 2)


def add(*ps):
    n = max(map(len, ps))
    return tuple(sum((p[k] if k < len(p) else ZERO for p in ps), ZERO)
                 for k in range(n))


def scale(p, c):
    return tuple(c * v for v in p)


def mul(p, q):
    r = [ZERO] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] += a*b
    return tuple(r)


def compose(p, c0, c1):
    # Horner evaluation of p(c0+c1*u), represented as a coefficient vector.
    ans = (ZERO,)
    for coefficient in p[::-1]:
        ans = add(mul(ans, (c0,c1)), (coefficient,))
    return ans


def integrate(p, lo=ZERO, hi=ONE):
    return sum((a * (hi**(i+1) - lo**(i+1)) / (i+1)
                for i,a in enumerate(p)), ZERO)


def var_poly(p):
    return integrate(mul(p,p)) - integrate(p)**2


def pair_variance(residual, mode):
    if mode == 'independent':
        return var_poly(residual) / 2
    if mode == 'central':
        avg = scale(add(residual, compose(residual, ONE, -ONE)), HALF)
        return var_poly(avg)
    if mode == 'half-reflection':
        low = scale(add(residual, compose(residual, HALF, -ONE)), HALF)
        high = scale(add(residual, compose(residual, F(3,2), -ONE)), HALF)
        moment = integrate(low, ZERO, HALF) + integrate(high, HALF, ONE)
        second = integrate(mul(low,low), ZERO, HALF) + integrate(mul(high,high), HALF, ONE)
        return second - moment**2
    raise ValueError(mode)


def cell_residual(f, j, m):
    a, h = F(j,m), F(1,m)
    on_u = tuple(sum((f[k] * comb(k, i) * a**(k-i) * h**i
                       for k in range(i, len(f))), ZERO)
                 for i in range(len(f)))
    left = sum((f[k] * a**k for k in range(len(f))), ZERO)
    right = sum((f[k] * (a+h)**k for k in range(len(f))), ZERO)
    return add(on_u, (-left, -(right-left)))


def total_variance(f, m, mode):
    h = F(1,m)
    return h*h*sum((pair_variance(cell_residual(f,j,m), mode)
                    for j in range(m)), ZERO)


def main():
    z = (ZERO, ONE, -ONE)
    assert integrate(z) == F(1,6)
    assert var_poly(z) == F(1,180)
    exact = {'independent':F(1,360), 'central':F(1,180),
             'half-reflection':F(1,2880)}
    for mode, target in exact.items():
        assert pair_variance(z, mode) == target, (mode, pair_variance(z, mode))

    for m in (1,2,3,5,8,17):
        for mode, target in exact.items():
            assert total_variance((ZERO,ZERO,ONE),m,mode) == target/F(m)**5

    # Cubic test is not a proof of the C^2 theorem: it checks exact
    # polynomial integration and convergence toward its predicted constant.
    f = (ZERO,ZERO,ONE,ONE)
    asym = {'independent':F(28,1440),'central':F(28,720),
            'half-reflection':F(28,11520)}
    for m in (16,32,64):
        for mode, target in asym.items():
            scaled = total_variance(f,m,mode)*m**5
            if abs(float(scaled / target - 1)) >= .10/m:
                raise AssertionError((m,mode,scaled,target))

    print('VERIFY_OK: exact rational pair variances; 18 quadratic finite-m identities;'
          ' 9 cubic asymptotic checks; sharp factors 8 and 16')

if __name__ == '__main__':
    main()
