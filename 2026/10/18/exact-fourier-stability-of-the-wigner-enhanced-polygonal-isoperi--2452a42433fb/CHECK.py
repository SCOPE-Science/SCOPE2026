#!/usr/bin/env python3
"""Independent numerical checks for the equiangular CPPOS spectral identity.

Uses Python's standard library. Tests are finite consistency checks, not a proof.
"""
import cmath
import math
import random


def signed_area(vertices):
    return sum((vertices[j].conjugate() * vertices[(j + 1) % len(vertices)]).imag
               for j in range(len(vertices))) / 2


def polygon(n, pair_sums, differences):
    lengths = ([(pair_sums[j] + differences[j]) / 2 for j in range(n)]
               + [(pair_sums[j] - differences[j]) / 2 for j in range(n)])
    assert min(lengths) > 0
    edges = [lengths[j] * cmath.exp(1j * j * math.pi / n)
             for j in range(2*n)]
    vertices = [0j]
    for edge in edges:
        vertices.append(vertices[-1] + edge)
    assert abs(vertices[-1]) < 1e-9
    return vertices[:-1], lengths


def spectral_deficit(n, pair_sums):
    theta = math.pi/(2*n)
    b = [a/2 for a in pair_sums]
    total = 0.
    for k in range(1, n):
        amplitude = sum(b[j] * cmath.exp(-2j * math.pi * k * j/n)
                        for j in range(n))/n
        eigenvalue = (4*n*math.sin(theta)**2
                      / (math.sin(k*math.pi/n)**2-math.sin(theta)**2))
        total += n*eigenvalue*abs(amplitude)**2
    return total


def best_coefficient(n):
    theta = math.pi/(2*n)
    return (4*n*math.tan(theta)**2 if n % 2 == 0
            else 4*n*math.sin(theta)**2/math.cos(2*theta))


def check():
    tests = 0
    worst = 0.
    for n in range(2, 22):
        for trial in range(70):
            rng = random.Random(345000 + n*1000 + trial)
            p = [rng.uniform(2., 7.) for j in range(n)]
            d = [0.]*n
            if n >= 3:
                d = [rng.uniform(-.4, .4) for j in range(n)]
                alpha = math.pi/n
                tail_x = sum(d[j]*math.cos(j*alpha) for j in range(2, n))
                tail_y = sum(d[j]*math.sin(j*alpha) for j in range(2, n))
                d[1] = -tail_y/math.sin(alpha)
                d[0] = -tail_x - d[1]*math.cos(alpha)
                if any(abs(d[j])>=p[j] for j in range(n)):
                    continue
            verts, lengths = polygon(n,p,d)
            W = [(verts[j]+verts[j+n])/2 for j in range(n)]
            Q = [(verts[j]-verts[(j+n)%(2*n)])/2 for j in range(2*n)]
            ap, aq, aw = (signed_area(verts), signed_area(Q), signed_area(W))
            l = sum(lengths)
            c = 8*n*math.tan(math.pi/(2*n))
            geometric = l*l-c*(ap+2*abs(aw))
            fourier = spectral_deficit(n,p)
            assert aw <= 1e-9
            assert abs(aq-ap+2*aw)<1e-9
            error = abs(geometric-fourier)
            tolerance = 3e-9*max(1., abs(geometric))
            assert error < tolerance, (n,trial,geometric,fourier,error)
            deviation = sum((pi-sum(p)/n)**2 for pi in p)
            assert geometric+1e-9 >= best_coefficient(n)*deviation/4
            worst = max(worst,error)
            tests += 1
        # The soft frequency attains equality for a positive, centrally symmetric polygon.
        mode = n//2
        soft = [4 + 0.25*math.cos(2*math.pi*mode*j/n) for j in range(n)]
        verts,lengths=polygon(n,soft,[0.]*n)
        pp = sum(lengths)
        eq_deficit = pp**2-8*n*math.tan(math.pi/(2*n))*signed_area(verts)
        variance=sum((s-sum(soft)/n)**2 for s in soft)
        assert abs(eq_deficit-best_coefficient(n)*variance/4)<1e-9
    print(f'PASS: {tests} polygons, orders 2..21; max absolute residual {worst:.3g}')
    print('PASS: sharp soft-mode constructions at all orders 2..21')


if __name__ == '__main__':
    check()
