#!/usr/bin/env python3
"""Independent finite consistency checks for the phase-kick parity threshold.

Standard-library only.  Numerical tests do not prove the infinite theorem.
"""
from math import cos, sin, pi, acos, exp, isclose
from random import Random


def T(n, x):
    assert -1.000000001 <= x <= 1.000000001
    x = max(-1.0, min(1.0, x))
    if n == 0:
        return 1.0
    p, q = 1.0, x
    for _ in range(1, n):
        p, q = q, 2.0 * x * q - p
    return q


def rate(n, g):
    assert n >= 2 and 0 <= g <= 2
    if n % 2 == 0:
        return 0.0
    c = 1 + cos(pi / n)
    return 0.0 if g <= c else 1.0 - T(n, 1.0-g)


def optimal_law(n, g):
    # Returns (probability, phase) pairs.  Values are positive and sum to one.
    if n % 2 == 0:
        return [(1.0-g/2.0, 0.0), (g/2.0, pi)]
    c = 1 + cos(pi/n)
    if g <= c:
        p = g/c
        phase = pi-pi/n
        return [(1-p, 0.0), (p/2.0, phase), (p/2.0, -phase)]
    phase = acos(1.0-g)
    return [(0.5, phase), (0.5, -phase)]


def observed_law(n, law):
    return (sum(p*(1-cos(th)) for p,th in law),
            sum(p*(1-cos(n*th)) for p,th in law))


def majorant(n, x):
    if n % 2 == 0:
        return 1.0
    x0 = -cos(pi/n)
    return T(n, x) if x < x0 else 1.0

rng = Random(114531)
checks = 0
for n in range(2, 41):
    c = 1+cos(pi/n) if n % 2 else 2
    grid = [0, 1e-11, 0.01, 0.1, 0.4, 1.0, 1.5, 1.9, 2.0, c, max(0.0,c-1e-5), min(2.0,c+1e-5)]
    grid += [2*k/51 for k in range(52)]
    for g in grid:
        law = optimal_law(n, g)
        local, full = observed_law(n, law)
        assert abs(local-g) < 1e-10, (n,g,local)
        assert abs(full-rate(n,g)) < 2e-9, (n,g,full,rate(n,g))
        assert full >= -1e-12
        checks += 1
    # Pointwise majorant and concavity checks on a deterministic dense mesh.
    for j in range(401):
        x=-1+j/200
        assert T(n,x) <= majorant(n,x)+1e-8
        checks+=1
    if n % 2:
        for j in range(1,399):
            x=-1+j/200
            d=majorant(n,x)-0.5*(majorant(n,x-0.005)+majorant(n,x+0.005))
            assert d > -2e-9,(n,j,d)
            checks+=1
    # Random finite-support laws check universal lower bound.
    for _ in range(100):
        angles=[rng.uniform(-pi, pi) for __ in range(5)]
        raw=[rng.expovariate(1) for __ in range(5)]
        z=sum(raw)
        law=list(zip([p/z for p in raw],angles))
        local, full = observed_law(n,law)
        assert full+2e-8 >= rate(n,local),(n,local,full,rate(n,local))
        checks+=1
# Verify curvature in the nonflat odd branch for representative n.
for n in [3,5,7,9,13,21]:
    c=1+cos(pi/n)
    a=n*n/(2*sin(pi/n)**2)
    eps=1e-5
    assert abs(rate(n,c+eps)/(eps**2)/a-1)<2e-3,(n,rate(n,c+eps),a)
    checks+=1
# GHZ two-dimensional phase-encoding QFI equals (n*t*visibility)^2.
# The SLD matrix can be formed explicitly: rho=(I + v(cos phi X + sin phi Y))/2;
# its derivative is (n*t*v/2)(-sin phi X + cos phi Y); SLD=2*d rho.
for n in (2,3,7,14):
    for g in (.3,1.2,1.99):
        t=.7
        Gamma=.9
        v=exp(-Gamma*t*rate(n,g))
        predicted=n*n*t*t*v*v
        # Assemble the full 2x2 density matrix, derivative, and its SLD.
        phi = 0.73 * n * t
        off=0.5*v*complex(cos(phi),-sin(phi))
        rho=((0.5,off),(off.conjugate(),0.5))
        deriv_off=(-1j*n*t)*off
        drho=((0j,deriv_off),(deriv_off.conjugate(),0j))
        L=tuple(tuple(2*z for z in row) for row in drho)
        mul=lambda a,b: tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
        rL=mul(rho,L)
        Lr=mul(L,rho)
        for i in range(2):
            for j in range(2):
                assert abs(0.5*(rL[i][j]+Lr[i][j])-drho[i][j]) < 2e-13
        L2=mul(L,L)
        rL2=mul(rho,L2)
        traceq=(rL2[0][0]+rL2[1][1]).real
        assert isclose(predicted,traceq,rel_tol=1e-12,abs_tol=1e-13)
        checks+=1
print('VERIFY_OK', checks, 'finite numerical tests')
