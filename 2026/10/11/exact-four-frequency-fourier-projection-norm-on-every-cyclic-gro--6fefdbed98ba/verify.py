#!/usr/bin/env python3
import cmath
import math


def direct(N):
    total = 0.0
    for j in range(N):
        z = sum(cmath.exp(2j * math.pi * k * j / N) for k in range(4))
        total += abs(z)
    return total / N


def closed(N):
    u = math.pi / (2 * N)
    q = (N - 1) // 4
    r = 2 * q + 1
    if N % 2:
        T = lambda x: 1.0 / math.sin(x)
    else:
        T = lambda x: math.cos(x) / math.sin(x)
    return (4.0 / N) * (
        math.sin(r * u) / math.sin(u)
        + math.sin(3 * r * u) / math.sin(3 * u)
        - 0.5 * T(u)
        + 0.5 * T(3 * u)
    )


def even_closed(N):
    u = math.pi / (2 * N)
    if N % 4 == 0:
        return (2.0 / N) * ((math.sqrt(2)-1)*math.cos(u)/math.sin(u) + (math.sqrt(2)+1)*math.cos(3*u)/math.sin(3*u))
    return (2.0 / N) * (math.sqrt(2)*(1/math.sin(u)+1/math.sin(3*u)) - math.cos(u)/math.sin(u) + math.cos(3*u)/math.sin(3*u))

for N in range(4, 501):
    a = direct(N)
    b = closed(N)
    assert abs(a-b) < 2e-11, (N, a, b)
    if N % 2 == 0:
        assert abs(b-even_closed(N)) < 2e-11, (N, b, even_closed(N))

L = 8*(2*math.sqrt(2)-1)/(3*math.pi)
c0 = -2*math.pi*(2*math.sqrt(2)+1)/3
c2 = 2*math.pi*(math.sqrt(2)-1)/3
co = math.pi*(math.sqrt(2)+2)/6
checks = [(4000,c0),(4002,c2),(4001,co),(4003,co)]
for N,c in checks:
    scaled = N*N*(closed(N)-L)
    assert abs(scaled-c) < 0.01, (N, scaled, c)

print('VERIFY_OK direct_N=4..500 even_forms=checked asymptotic_classes=4')
