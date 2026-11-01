#!/usr/bin/env python3
"""Numerical diagnostics for the exact finite-dimensional polygon theorem.

All-dimensional conclusions are proved analytically in RESULT.md.
"""
import math
import random


def vertices(support):
    N = len(support)
    step = 2 * math.pi / N
    def pair(a, b):
        xa, ya = math.cos(a * step), math.sin(a * step)
        xb, yb = math.cos(b * step), math.sin(b * step)
        D = xa * yb - xb * ya
        return ((support[a] * yb - support[b] * ya) / D,
                (xa * support[b] - xb * support[a]) / D)
    return [pair((j - 1) % N, j) for j in range(N)]


def signed_area(poly):
    return .5 * sum(poly[j][0] * poly[(j + 1) % len(poly)][1] -
                      poly[(j + 1) % len(poly)][0] * poly[j][1]
                      for j in range(len(poly)))


def perimeter(poly):
    return sum(math.dist(poly[j], poly[(j + 1) % len(poly)])
               for j in range(len(poly)))


def close(a, b, atol=1e-8, rtol=1e-9):
    assert abs(a - b) <= atol + rtol * max(abs(a), abs(b)), (a, b)


def green(n):
    alpha = math.pi / n
    c = math.cos(alpha)
    G = 1 / (n * (1 - c))
    return [G - math.sin(j * alpha) / math.sin(alpha)
            for j in range(n)]


def energy(vec, n):
    c = math.cos(math.pi / n)
    return sum(c * vec[j] ** 2 - vec[j] * vec[(j + 1) % n]
               for j in range(n))


def verify():
    rng = random.Random(20261027)
    checks = 0
    for n in range(3, 101):
        g = green(n)
        alpha = math.pi / n
        c = math.cos(alpha)
        G = 1 / (n * (1 - c))
        close(sum(g), 0, atol=3e-10)
        checks += 1
        for j in range(n):
            lhs = c * g[j] - .5 * (g[(j - 1) % n] + g[(j + 1) % n])
            rhs = (1 if j == 0 else 0) - 1 / n
            close(lhs, rhs, atol=3e-12)
            checks += 1
        close(energy(g, n), G, atol=1e-8)
        checks += 1

    for n in range(3, 25):
        alpha = math.pi / n
        c = math.cos(alpha)
        tangent = math.tan(alpha / 2)
        C = 16 * n * n * tangent * tangent
        H = 2.0
        g = green(n)
        for factor in (-1, 1):
            t = factor * 0.003 / n
            q = [H + t * g[j % n] for j in range(2 * n)]
            poly = vertices(q)
            lengths = [math.dist(poly[j], poly[(j + 1) % (2 * n)])
                       for j in range(2 * n)]
            assert min(lengths) > 0.0
            width_max = max(abs(q[j] - H) for j in range(n))
            deficit = perimeter(poly) ** 2 - 8 * n * tangent * signed_area(poly)
            close(deficit, C * width_max ** 2, atol=1e-9)
            checks += 2
        for _ in range(12):
            # Independent facet perturbations; all facets survive for small amplitude.
            s = [H + rng.uniform(-1, 1) * .008 / (n*n)
                 for _ in range(2 * n)]
            p = vertices(s)
            q = [0.5 * (s[j] + s[(j + n) % (2*n)]) for j in range(2 * n)]
            qp = vertices(q)
            width_means = sum(q[:n]) / n
            wig = [((p[j][0]+p[j+n][0])*0.5,
                    (p[j][1]+p[j+n][1])*0.5)
                   for j in range(n)]
            a_p = signed_area(p)
            a_q = signed_area(qp)
            a_w = signed_area(wig)
            close(2*a_w, a_p-a_q, atol=3e-9)
            close(perimeter(p), perimeter(qp), atol=1e-9)
            dd = perimeter(p) ** 2 - 8*n*tangent*(a_p+2*abs(a_w))
            delta = max(abs(q[j]-width_means) for j in range(n))
            assert dd >= C*delta*delta-1e-8, (n,dd,C*delta*delta)
            checks += 3
    for n in (30, 50, 100, 1000):
        C = 16*n*n*math.tan(math.pi/(2*n))**2
        assert C > 4*math.pi**2
        checks += 1
    print('PASS', checks, 'checks: recurrence, sharp witnesses, Wigner identity, stability, asymptotic bound')

if __name__ == '__main__':
    verify()
