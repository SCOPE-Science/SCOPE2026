#!/usr/bin/env python3
"""Reproduce analytic identities and sample full-matrix tests for two-price cycles.

Requires Python 3, sympy, numpy. This finite test is not a proof of the
all-orders theorem. Mathematical details are in RESULT.md.
"""
import math
import random
import numpy as np
import sympy as sp


def optimal(m, c_a, c_b, budget):
    tau = math.pi / m
    v = math.cos(tau)
    delta = c_a + c_b + 2 * math.sqrt(c_a * c_b) * v
    scale = budget / m
    a = scale * (c_a + math.sqrt(c_a * c_b) * v) / (c_a * delta)
    b = scale * (c_b + math.sqrt(c_a * c_b) * v) / (c_b * delta)
    gap = 2 * scale * math.sin(tau) ** 2 / delta
    return a, b, gap


def laplacian(w):
    n = len(w)
    mat = np.zeros((n, n))
    for j, rate in enumerate(w):
        k = (j + 1) % n
        mat[j, j] += rate
        mat[k, k] += rate
        mat[j, k] -= rate
        mat[k, j] -= rate
    return mat


def run():
    checks = 0
    A, D, C, t = sp.symbols('A D C t', positive=True, real=True)
    den = A**2 + D**2 + 2 * A * D * t
    a = C * (A + D * t) / (A * den)
    b = C * (D + A * t) / (D * den)
    lmb = 2 * C * (1 - t**2) / den
    for value in [sp.simplify(A**2*a + D**2*b - C),
                  sp.simplify(lmb**2 - 2*(a+b)*lmb + 4*a*b*(1-t**2))]:
        assert value == 0, value
        checks += 1
    # Exact full-matrix spectra for m=2 and m=3; square prices make
    # every optimal conductance rational in these two orders.
    for m in (2, 3):
        for p, q in [(1, 1), (1, 4), (9, 1), (4, 25)]:
            B = sp.Integer(m)
            c = sp.Integer(0) if m == 2 else sp.Rational(1, 2)
            s2 = 1-c*c
            z = sp.Integer(p)+sp.Integer(q)+2*sp.sqrt(p*q)*c
            ca = (sp.Integer(p)+sp.sqrt(p*q)*c)/(sp.Integer(p)*z)
            cb = (sp.Integer(q)+sp.sqrt(p*q)*c)/(sp.Integer(q)*z)
            predicted = 2*s2/z
            n = 2*m
            mat = sp.zeros(n)
            for i in range(n):
                j = (i+1)%n
                w = ca if i%2 == 0 else cb
                mat[i,i]+=w; mat[j,j]+=w
                mat[i,j]-=w; mat[j,i]-=w
            vals = sorted([float(x) for x in mat.eigenvals().keys()])
            assert abs(vals[0])<1e-10
            assert abs(vals[1]-float(predicted))<1e-10
            assert sp.simplify(m*(p*ca+q*cb)-B)==0
            checks += 3
    random.seed(117)
    for m in (2, 3, 4, 5, 7, 12):
        for ca, cb in ((1.,1.), (1.,4.), (9.,1.), (0.25,25./9.)):
            for budget in (0.7,3.0):
                a0,b0,gap0=optimal(m,ca,cb,budget)
                w = [a0 if j%2==0 else b0 for j in range(2*m)]
                lam = np.linalg.eigvalsh(laplacian(w))
                assert abs(lam[1]-gap0)<1e-10
                assert abs(sum((ca if j%2==0 else cb)*v for j,v in enumerate(w))-budget)<1e-10
                tau = math.pi/m
                alpha = math.atan2(math.sqrt(ca)*math.sin(tau),math.sqrt(cb)+math.sqrt(ca)*math.cos(tau))
                delta = ca+cb+2*math.sqrt(ca*cb)*math.cos(tau)
                radius = math.sqrt(delta)/(2*math.sin(tau))
                X = np.array([[radius*math.cos(2*j*tau + (2*alpha if i else 0)),
                               radius*math.sin(2*j*tau + (2*alpha if i else 0))]
                              for j in range(m) for i in range(2)])
                assert np.max(abs(X.mean(axis=0)))<1e-10
                for j in range(2*m):
                    norm2=sum((X[(j+1)%(2*m)]-X[j])**2)
                    assert abs(norm2-(ca if j%2==0 else cb))<1e-10
                assert np.max(abs(laplacian(w)@X-gap0*X))<1e-10
                checks += 5
                # Feasible independent (not necessarily alternating) rates.
                for k in range(12):
                    disturbed=[v * math.exp(random.uniform(-3,3)) for v in w]
                    cost=sum((ca if j%2==0 else cb)*v for j,v in enumerate(disturbed))
                    disturbed=[v*budget/cost for v in disturbed]
                    assert np.linalg.eigvalsh(laplacian(disturbed))[1] <= gap0 + 1e-9
                    checks += 1
    print('PASS:', checks, 'asserted algebraic and matrix checks')

if __name__=='__main__':
    run()
