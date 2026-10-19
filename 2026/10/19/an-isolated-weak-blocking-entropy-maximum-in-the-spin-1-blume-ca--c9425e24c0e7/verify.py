#!/usr/bin/env python3
"""Exact verification of finite-ring one-site stability in a spin-1 chain.

Run with Python 3 and SymPy (tested with SymPy 1.13). The infinite-size
statements require the proof in RESULT.md; this program checks algebraic
identities and finite instances without claiming to replace that proof.
"""
from itertools import product
import sympy as sp

SPINS = (-1, 0, 1)
PAIRS = tuple(product(SPINS, repeat=2))
x = sp.symbols('x')


def is_locally_minimal(a, b, c, delta):
    field = a+c
    local = lambda v: delta*v*v-field*v
    return all(local(b) <= local(v) for v in SPINS)


def transfer(delta):
    return sp.Matrix(9, 9, lambda i, j: int(
        PAIRS[i][1] == PAIRS[j][0]
        and is_locally_minimal(PAIRS[i][0], PAIRS[i][1], PAIRS[j][1], delta)
    ))


def energy(s, delta):
    n = len(s)
    return sum(delta*s[i]*s[i] - s[i]*s[(i+1)%n] for i in range(n))


def direct_count(n, delta):
    cnt=0
    for s in product(SPINS, repeat=n):
        e = energy(s, delta)
        if all(all(
            energy(s[:i]+(v,)+s[i+1:], delta) >= e
            for v in SPINS
        ) for i in range(n)):
            cnt += 1
    return cnt


def main():
    expected={
        sp.Rational(1,2): x**2*(x-1)*(x**3-x**2-1)*(x**3-x**2+1),
        sp.Integer(1): x**2*(x**3-x**2+1)*(x**4-2*x**3+x**2-x-1),
        sp.Rational(3,2): x**6*(x-1)**3,
        sp.Integer(2): x**6*(x-1)**3,
        sp.Rational(5,2): x**8*(x-1),
    }
    matrix_checks=0
    exhaustive_comparisons=0
    for delta, polynomial in expected.items():
        t = transfer(delta)
        assert sp.expand(t.charpoly(x).as_expr()-polynomial) == 0
        matrix_checks+=1
        power=sp.eye(9)
        for n in range(1, 9):
            power=power*t
            if n>=3:
                brute=direct_count(n,delta)
                count=sp.trace(power)
                assert int(count)==brute, (delta,n,count,brute)
                exhaustive_comparisons+=1
    low=sp.Poly(x**3-x**2-1,x)
    peak=sp.Poly(x**4-2*x**3+x**2-x-1,x)
    assert sp.rem(peak, low) == sp.Poly(-2,x)
    assert peak.eval(2)>0
    assert low.eval(1)<0 and low.eval(2)>0
    assert peak.eval(sp.Rational(18,10)) < 0
    assert peak.eval(sp.Rational(19,10)) > 0
    assert [direct_count(8,d) for d in expected] == [27,171,3,3,1]
    print('PASS',matrix_checks,'exact characteristic polynomials;',
          exhaustive_comparisons,'exhaustive finite-length count comparisons; polynomial identity verified')

if __name__ == '__main__':
    main()
