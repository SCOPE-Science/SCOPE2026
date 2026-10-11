#!/usr/bin/env python3
"""Finite consistency checks for single-linear-form approximation in radial Dirichlet norms.

The universal phase transition is established analytically, not by these tests.
"""
from fractions import Fraction
from math import comb, factorial, lgamma, log, exp, pi, prod, sqrt


def compositions(n, s):
    if s == 1:
        yield (n,)
    else:
        for k in range(n + 1):
            for tail in compositions(n - k, s - 1):
                yield (k,) + tail


def v_exact(n, p):
    total = Fraction(0)
    for multi in compositions(n, len(p)):
        coeff = factorial(n) // prod(factorial(k) for k in multi)
        term = Fraction(coeff * coeff)
        for prob, k in zip(p, multi):
            term *= prob ** (2*k)
        total += term
    return total


def v_numeric(n, p):
    lp = [log(float(q)) for q in p]
    out = 0.0
    for multi in compositions(n, len(p)):
        v = lgamma(n + 1.0)
        for k, lq in zip(multi, lp):
            v -= lgamma(k + 1.0)
            v += k * lq
        out += exp(2*v)
    return out


def target_constant(p):
    return (4*pi)**(-(len(p)-1)/2) / sqrt(prod(float(x) for x in p))


def exact_error(N, beta, p):
    weights = [Fraction((n+1)**beta) * v_exact(n, p) for n in range(N+2)]
    invsum = sum((1/w for w in weights), Fraction())
    error = [Fraction(1,w*invsum) for w in weights]
    assert sum(error) == 1
    # Directly compute the full norm using orthogonality of homogeneous powers.
    energy = sum((w * x*x for w, x in zip(weights, error)), Fraction())
    return 1/invsum, energy, weights, error


def main():
    for p in [(Fraction(1),), (Fraction(1,2),Fraction(1,2)),
              (Fraction(1,4),Fraction(3,4)),
              (Fraction(1,6),Fraction(1,3),Fraction(1,2))]:
        for n in range(0, 9):
            ve = v_exact(n, p)
            vf = v_numeric(n, p)
            assert abs(float(ve) - vf) < 5e-12, (p,n)
        for N in range(0, 4):
            val, check, weights, error = exact_error(N, 2, p)
            assert val == check
            # Euler-Lagrange: all weighted error coefficients are equal.
            assert len(set(w*x for w,x in zip(weights,error))) == 1
    p = (Fraction(1,2), Fraction(1,2))
    for n in (1,2,5,20,80):
        assert v_exact(n,p) == Fraction(comb(2*n,n),4**n)
    for p in [(0.5,0.5),(0.2,0.3,0.5),(0.1,0.2,0.3,0.4)]:
        n = 100 if len(p)==2 else (100 if len(p)==3 else 40)
        ratio = v_numeric(n,p)*n**((len(p)-1)/2)/target_constant(p)
        print('s={}, n={}, ratio V_n / (C n^(-(s-1)/2)) = {:.9f}'.format(len(p),n,ratio))
        assert 0.91 < ratio < 1.10, (p,n,ratio)
    print('PASS: exact rational minimizers, direct energies, central binomial reduction,')
    print('      finite-dimensional coefficient identities and Laplace scaling checks.')


if __name__ == '__main__':
    main()
