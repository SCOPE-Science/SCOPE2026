"""Reproduce finite consistency tests for Szego-kernel circle configurations.

The all-degree and optimality conclusions require the analytic argument;
these computations are finite checks, not substitutes for that argument.
"""
from __future__ import annotations

import cmath
import math
import random


def gram(r, angles):
    points = [r * cmath.exp(1j * t) for t in angles]
    return [[(1-r*r)/(1-points[i]*points[j].conjugate())
             for j in range(len(points))] for i in range(len(points))]


def determinant(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    det = 1+0j
    for i in range(n):
        j = max(range(i,n), key=lambda k: abs(a[k][i]))
        if abs(a[j][i]) < 1e-14:
            return 0+0j
        if j != i:
            a[j], a[i] = a[i], a[j]
            det = -det
        pivot = a[i][i]
        det *= pivot
        for k in range(i+1,n):
            factor = a[k][i]/pivot
            for l in range(i+1,n):
                a[k][l] -= factor*a[i][l]
    return det


def circulant_eigenvalues(d, r):
    return [d*(1-r*r)*r**(2*l)/(1-r**(2*d)) for l in range(d)]


def deficit(r, angles):
    d = len(angles)
    offsets = [angles[j]-2*math.pi*j/d for j in range(d)]
    mean = sum(offsets)/d
    dev2 = sum((x-mean)**2 for x in offsets)
    reg_det = math.prod(circulant_eigenvalues(d,r))
    this_det = determinant(gram(r, angles)).real
    assert this_det > 0
    loss = math.log(reg_det/this_det)
    c = (1-r*r)**2/(4*(1+r*r)**2)
    return loss, c*d*dev2


def run():
    trials = 0
    for d in range(2, 10):
        for r in (0.18, 0.42, 0.71, 0.87):
            angles = [2*math.pi*j/d for j in range(d)]
            g = gram(r, angles)
            lambdas = circulant_eigenvalues(d,r)
            assert abs(determinant(g).real-math.prod(lambdas)) < 2e-9
            for l in range(d):
                v = [cmath.exp(2j*math.pi*l*j/d) for j in range(d)]
                errors = [abs(sum(g[i][j]*v[j] for j in range(d))-lambdas[l]*v[i])
                          for i in range(d)]
                assert max(errors) < 1e-8
            trials += 1
    rng = random.Random(202611)
    jitter_trials = 0
    for d in range(2, 9):
        for r in (0.28,0.58,0.82):
            for _ in range(45):
                gaps0 = [0.4 + rng.random() for _ in range(d)]
                gaps = [2*math.pi*u/sum(gaps0) for u in gaps0]
                angles = [0.0]
                for k in range(d-1):
                    angles.append(angles[-1]+gaps[k])
                loss, lower = deficit(r, angles)
                assert loss + 2e-9 >= lower, (d,r,loss,lower)
                jitter_trials += 1
    for r in (0.2, 0.5, 0.8):
        c = (1-r*r)**2/(4*(1+r*r)**2)
        ratios=[]
        for h in (0.05, 0.025, 0.0125):
            loss, lower = deficit(r, [0,math.pi+h])
            ratios.append(loss/lower)
        assert abs(ratios[-1]-1) < 1e-4, (r,ratios)
    print(f'PASS: {trials} regular spectra, {jitter_trials} jittered configurations, 3 sharpness sequences')


if __name__ == '__main__':
    run()
