#!/usr/bin/env python3
"""Standalone reproduction of exact stationary dissipative alignment identities.
Only the Python 3 standard library is required.
"""
from fractions import Fraction as F
from math import sin, cos, pi
from random import Random

def solve(A, b):
    n = len(b)
    a = [list(map(float, A[i])) + [float(b[i])] for i in range(n)]
    for j in range(n):
        i = max(range(j, n), key=lambda q: abs(a[q][j]))
        a[j], a[i] = a[i], a[j]
        piv = a[j][j]
        assert abs(piv) > 1e-14
        a[j] = [u / piv for u in a[j]]
        for i in range(n):
            if i != j:
                d = a[i][j]
                a[i] = [a[i][z] - d * a[j][z] for z in range(n + 1)]
    return [a[i][n] for i in range(n)]

def direct(k1, k2, g1, g2, b, theta, v, D):
    assert 0 < b < min(g1, g2) and k1 < k2 and g1 < g2
    u, w = cos(theta), sin(theta)
    K = [[k1 * u*u + k2*w*w, (k1-k2)*u*w],
         [(k1-k2)*u*w, k1*w*w + k2*u*u]]
    a1, a2 = (g1-b)/2, (g2-b)/2
    Q = [[0.0]*4 for _ in range(4)]
    Q[0][1] = Q[1][0] = a1
    Q[2][3] = Q[3][2] = a2
    for i in (0,1):
        for j in (2,3):
            Q[i][j] = Q[j][i] = b/2
    for i in range(4):
        Q[i][i] = -sum(Q[i])
    directions = ((1,0),(-1,0),(0,1),(0,-1))
    A = [[0.0]*8 for _ in range(8)]
    rhs = []
    for s in range(4):
        for d in range(2):
            rhs.append(v*directions[s][d]/4)
            for t in range(4):
                for e in range(2):
                    A[2*s+d][2*t+e] = (
                       (K[d][e] if s == t else 0.0)
                       -(Q[t][s] if e == d else 0.0))
    m = solve(A, rhs)
    k_dot_m = 0.0
    for s in range(4):
        for d in range(2):
            for e in range(2):
                k_dot_m += directions[s][d]*K[d][e]*m[2*s+e]
    return (v*v-v*k_dot_m)/D

def formula(k1,k2,g1,g2,theta,v,D):
    A = g1/(k1+g1)+g2/(k2+g2)
    B = g2/(k1+g2)+g1/(k2+g1)
    return v*v/(2*D)*(cos(theta)**2*A+sin(theta)**2*B)

def difference(k1,k2,g1,g2):
    return (g1-g2)*(k1-k2)*(g1*g2-k1*k2)/(
        (k1+g1)*(k1+g2)*(k2+g1)*(k2+g2))

checks = 0
rng = Random(418221)
for _ in range(500):
    k1,k2 = sorted((10**rng.uniform(-1,1),10**rng.uniform(-1,1)))
    g1,g2 = sorted((10**rng.uniform(-1,1),10**rng.uniform(-1,1)))
    b = 0.37 * g1
    theta = rng.uniform(0, pi/2)
    v,D = 1.7,0.8
    x = direct(k1,k2,g1,g2,b,theta,v,D)
    y = formula(k1,k2,g1,g2,theta,v,D)
    assert abs(x-y) < 2e-11 * (1+abs(y)), (x,y)
    checks += 1
for _ in range(300):
    k1,k2,g1,g2 = (F(rng.randint(1,20),rng.randint(1,20)) for i in range(4))
    A = g1/(k1+g1)+g2/(k2+g2)
    B = g2/(k1+g2)+g1/(k2+g1)
    assert A-B == difference(k1,k2,g1,g2)
    assert A-1 == (g1*g2-k1*k2)/((g1+k1)*(g2+k2))
    checks += 2
for k1,k2 in ((1,4),(2,7),(0.3,9),(0.1,0.2)):
    # Geometric-mean threshold with each of the two directional rates distinct.
    g1 = (k1*k2)**0.5/2
    g2 = (k1*k2)**0.5*2
    b = g1*0.4
    for theta in (0,0.17,0.6,pi/2):
        p = direct(k1,k2,g1,g2,b,theta,1.7,0.8)
        assert abs(p-1.7**2/(2*0.8)) < 1e-11
        checks += 1
for g1,g2 in ((0.5,2),(1,4),(2,8)):
    A = formula(1,4,g1,g2,0,1,1)
    B = formula(1,4,g1,g2,pi/2,1,1)
    assert (A-B)*(g1*g2-4) >= -1e-13
    checks += 1
print(f'PASS: {checks} reproducible numerical and exact-rational assertions.')
