#!/usr/bin/env python3
"""Finite direct checks for a three-tap prime-cycle cross-STFT equality theorem.

The infinite-family theorem follows from its mathematical proof; this script is
only a reproducible collection of independent finite tests.
"""
import cmath
import itertools
import math
import random


def primes_below(n):
    return [p for p in range(7, n) if all(p % d for d in range(2, math.isqrt(p) + 1))]


def solve_case(p, i, j, ell, t):
    w = cmath.exp(2j * math.pi / p)
    eta, theta, rho = w ** i, w ** j, w ** ell
    T = -(eta + theta)
    assert abs(T) > 1e-8
    sigma = eta * theta / rho
    f = (-rho * t * t / T, t, 1 + 0j)
    g = ((-sigma * T / (t * t)).conjugate(), (T / t).conjugate(), 1 + 0j)
    return f, g, eta, theta, rho, sigma


def transform_values(f, g, p):
    """Direct double enumeration, not the proof's polynomial row formulas."""
    z = cmath.exp(-2j * math.pi / p)
    rows = {}
    for x in range(p):
        vals = []
        for k in range(p):
            val = sum(f[y] * g[(y - x) % p].conjugate() * (z ** (k * y))
                      for y in range(p))
            vals.append(val)
        rows[x] = vals
    return rows


def root_index(p, z):
    omega = cmath.exp(-2j * math.pi / p)
    return min(range(p), key=lambda k: abs(omega ** k - z))


def support_and_zeros(rows, threshold=4e-7):
    zeros = {x: [k for k,v in enumerate(vals) if abs(v) < threshold]
             for x,vals in rows.items()}
    supp = sum(len(vals) - len(zeros[x]) for x,vals in rows.items())
    return supp, zeros


def inspect_case(p,i,j,ell,t):
    f3,g3,eta,theta,rho,sigma = solve_case(p,i,j,ell,t)
    f = list(f3)+[0j]*(p-3)
    g = list(g3)+[0j]*(p-3)
    rows = transform_values(f,g,p)
    supp, zeros = support_and_zeros(rows)
    assert supp == 5*p-4, (p,i,j,ell,t,supp)
    assert set(zeros[0]) == {root_index(p,eta),root_index(p,theta)}
    assert zeros[p-1] == [root_index(p,rho)]
    assert zeros[1] == [root_index(p,sigma)]
    assert zeros[2] == [] and zeros[p-2] == []
    assert all(len(zs) == p for x,zs in zeros.items() if x not in (p-2,p-1,0,1,2))
    return 1


def geometry_test(p):
    """Every two three-element supports giving only 5 shifts are AP pairs."""
    sets = list(itertools.combinations(range(p), 3))
    diff5 = 0
    for a in sets:
        for b in sets:
            shift_set = {(x - y) % p for x in a for y in b}
            assert len(shift_set) >= 5
            if len(shift_set) == 5:
                def steps(q):
                    return {d for d in range(1, p)
                            if any({u, (u+d)%p, (u+2*d)%p}==set(q)
                                   for u in q)}
                assert steps(a) & steps(b), (p,a,b)
                diff5 += 1
    return diff5


def run():
    rng = random.Random(260529)
    cases=0
    for p in primes_below(65):
        for _ in range(14):
            i,j=rng.sample(range(p),2)
            ell=rng.randrange(p)
            t=complex(rng.uniform(-1.7,1.7),rng.uniform(-1.7,1.7))
            if abs(t)<0.3: t+=0.7j
            cases += inspect_case(p,i,j,ell,t)
    for p in (7, 11):
        for i in range(p):
            for j in range(i+1,p):
                for ell in range(p):
                    cases += inspect_case(p,i,j,ell,0.8+0.41j)
    geom=geometry_test(7)+geometry_test(11)
    print(f'VERIFY_OK {cases} direct cross-STFT extremizers; {geom} equal-sumset supports at p=7,11')


if __name__ == '__main__':
    run()
