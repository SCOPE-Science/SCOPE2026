#!/usr/bin/env python3
"""Independent arithmetic checks for the signed-cycle IC(0) phase diagram.

Run: python3 verify_cycle_ic.py
Requires numpy, available from https://numpy.org.
All tests are finite consistency checks; the all-size assertions rely on the proof.
"""
from fractions import Fraction
from itertools import product
from math import cos, pi, isclose
import numpy as np


def cycle_matrix(n, t, signs):
    assert n >= 4 and len(signs) == n
    a = np.eye(n, dtype=float)
    for j, sign in enumerate(signs):
        i = (j+1) % n
        a[i, j] = a[j, i] = float(sign) * float(t)
    return a


def ic0_pivots(a):
    """Sparse-pattern IC(0), preserving original pattern even after fill."""
    n = len(a)
    l = np.zeros_like(a)
    ps = []
    for j in range(n):
        p = float(a[j, j] - sum(l[j, k] ** 2 for k in range(j)))
        ps.append(p)
        if p <= 0:
            break
        l[j, j] = p ** 0.5
        for i in range(j+1, n):
            if a[i, j] != 0:
                l[i, j] = (a[i, j] - sum(l[i, k]*l[j, k] for k in range(j)))/l[j, j]
    return ps


def continuant_pivots(n, t):
    d = [1., 1.]
    z = t*t
    for j in range(2, n+2):
        d.append(d[-1]-z*d[-2])
    return [d[j]/d[j-1] for j in range(1, n)] + [d[n+1]/d[n-1]]


def path_det_rational(m, z):
    d0, d1 = Fraction(1), Fraction(1)
    for j in range(2, m+1):
        d0, d1 = d1, d1-z*d0
    return d1


def closeness(a, b):
    return isclose(a, b, rel_tol=4e-10, abs_tol=4e-10)


checks = 0
# Exact rational pivot identities, with no floating determinant assumption.
for n in range(4, 41):
    for z in [Fraction(1, 20), Fraction(1, 9), Fraction(1, 5), Fraction(3, 10)]:
        ds = [path_det_rational(j, z) for j in range(n+2)]
        if any(x == 0 for x in ds[:n]):
            continue
        p1 = Fraction(1)
        seq = [p1]
        for j in range(2, n):
            seq.append(1-z/seq[-1])
        assert all(seq[j-1] == ds[j]/ds[j-1] for j in range(1,n))
        last = 1-z-z/seq[-1]
        assert last == ds[n+1]/ds[n-1]
        checks += 1

# Full matrix checks: all 16 signings at n=4; random signings at larger n.
rng = np.random.default_rng(3435)
for n in range(4, 29):
    lower = 1/(2*cos(pi/(n+2)))
    higher = 1/(2*cos(pi/n))
    signs_list = list(product([-1,1], repeat=n)) if n == 4 else [tuple(rng.choice([-1,1], size=n)) for _ in range(20)]
    for signs in signs_list:
        sign_product = int(np.prod(signs))
        bad = sign_product != (-1)**n
        spd_bound = higher if bad else .5
        for t in sorted(set([.15, .43, .49, .5*(lower+min(higher,.5)), .98*lower, 1.02*lower, (lower+higher)/2])):
            a = cycle_matrix(n,t,signs)
            lam_min = float(np.linalg.eigvalsh(a)[0])
            assert (lam_min > 0) == (t < spd_bound), (n,signs,t,lam_min,spd_bound)
            p = ic0_pivots(a)
            q = continuant_pivots(n,t)
            for u,v in zip(p,q):
                assert closeness(u,v), (n,signs,t,p,q)
            if t < spd_bound:
                if t < lower:
                    assert len(p) == n and min(p)>0
                elif t > lower:
                    assert len(p)==n and p[-1]<0 and min(p[:-1])>0
            checks += 1

# Rational sharp counterexample in size four.
a = cycle_matrix(4, 3/5, [1,1,1,-1])
p = ic0_pivots(a)
assert all(closeness(u,v) for u,v in zip(p,[1,16/25,7/16,-32/175]))
assert np.linalg.eigvalsh(a)[0]>0
checks += 1

# Exact shift threshold and spectral-condition-number cutoff comparisons.
for n in range(4,25):
    c = cos(pi/n)
    d = cos(pi/(n+2))
    lower = 1/(2*d)
    upper = 1/(2*c)
    signs = [1]*n
    signs[-1] = int((-1)**(n+1))
    t = .5*(lower+upper)
    kappa = (d+c)/(d-c) if n % 2 == 0 else (d+1)/(d-c)
    aa = cycle_matrix(n,lower,signs)
    evals = np.linalg.eigvalsh(aa)
    assert closeness(float(evals[-1]/evals[0]),kappa)
    shift = 2*t*d - 1
    for eps in [-.0001, .0001]:
        alpha = shift+eps
        if alpha<0: continue
        q = ic0_pivots(cycle_matrix(n,t,signs)+alpha*np.eye(n))
        assert (len(q)==n and min(q)>0) == (eps>0)
        checks += 1

# Compare leading asymptotic scales on growing even and odd cycles.
for n in [100,200,400,800]:
    c=cos(pi/n);d=cos(pi/(n+2))
    width=1/(2*c)-1/(2*d)
    assert abs(width/(pi*pi/n**3)-1)<.08
    kappa_even=(d+c)/(d-c)
    assert abs(kappa_even/(n**3/pi**2)-1)<.08
    checks += 1
print(f'PASS: {checks} exact-rational recurrence, spectral, sign, shift, and asymptotic consistency checks')
print('n=4 signed edge counterexample (t=3/5), eigenvalues and IC pivots:')
print('eigenvalues =',np.linalg.eigvalsh(a))
print('IC pivots =',p)
print('These checks supplement, but do not replace, the universal proof.')
