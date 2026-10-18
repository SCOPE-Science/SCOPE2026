#!/usr/bin/env python3
"""Reproduce finite combinatorial and numerical checks for near-cubic distance tails.
Standard-library only. This is a finite checker, not an infinite-dimensional proof.
"""
import itertools
import math
from fractions import Fraction


def graph_H(d, edges):
    H = [[0] * d for _ in range(d)]
    for i, j, weight in edges:
        assert 0 <= i < j < d and weight > 0
        H[i][j] = H[j][i] = weight
    return H


def energy(H, signs):
    return sum(signs[i] * signs[j] * H[i][j]
               for i in range(len(H)) for j in range(len(H)))


def cut_weight(edges, signs):
    return sum(w for i, j, w in edges if signs[i] != signs[j])


def limiting_profile(d, edges, t):
    H = graph_H(d, edges)
    S = list(itertools.product((-1, 1), repeat=d))
    en = [energy(H, s) for s in S]
    top = max(en)
    f_energy = sum(Fraction(max(0, t - (top - e)) ** (2*d))
                   for e in en) / (4**d * math.factorial(2*d))
    f_cut = sum(Fraction(max(0, t - 4*cut_weight(edges, s)) ** (2*d))
                for s in S) / (4**d * math.factorial(2*d))
    assert f_energy == f_cut
    assert sum(en) == 0
    gaps = [top - e for e in en]
    assert Fraction(sum(gaps), len(gaps)) == top
    return f_cut, gaps


def components(d, edges):
    parent = list(range(d))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for i, j, _ in edges:
        parent[root(i)] = root(j)
    return len({root(i) for i in range(d)})


def fixed_tail_coefficient(d, edges, h):
    degrees = [0] * d
    for i, j, w in edges:
        degrees[i] += w
        degrees[j] += w
    assert h > 0
    return (2**components(d, edges) /
            (4**d * math.factorial(2*d) *
             math.prod((1+h*a)**2 for a in degrees)))


def integrate_2d(h, delta, steps=1200):
    """Exact triangular joint density integrated with composite Simpson quadrature.

    Gram matrix [[1,h],[h,1]]; threshold is squared diameter minus delta.
    The integration variable v_i=1-|X_i-Y_i| has density v_i at either sign.
    For 0<delta<0.2 and h<0.4 the valid regions lie near the corners.
    """
    assert 0 <= h < 0.4 and 0 < delta < 0.2 and steps % 2 == 0
    total = 0.0
    for sign in (1, -1):
        base = 2*h*(1-sign)
        if delta <= base:
            continue
        aa = 1+h*sign
        B0 = 2*aa
        rest = delta-base
        v1max = 2*rest/(B0+math.sqrt(B0*B0-4*rest))
        def integrand(v1):
            L = B0-2*h*sign*v1
            C = base+B0*v1-v1*v1
            rhs = max(0.0, delta-C)
            root = 2*rhs/(L+math.sqrt(max(0.0, L*L-4*rhs)))
            return 0.5*v1*root*root
        step = v1max/steps
        subtotal = integrand(0)+integrand(v1max)
        for i in range(1, steps):
            subtotal += (4 if i % 2 else 2)*integrand(i*step)
        total += 2 * subtotal*step/3 # two sign vectors for each product
    return total


def run():
    examples = [
        (2, [(0,1,1)]),
        (3, [(0,1,1),(1,2,2)]),
        (4, [(0,1,1),(1,2,2),(2,3,1),(0,3,3)]),
        (5, [(0,1,2),(2,3,3)])
    ]
    for d, edges in examples:
        gaps = None
        for t in (0,1,4,5,10,25):
            _, gaps = limiting_profile(d, edges, t)
        c = components(d, edges)
        assert gaps.count(0) == 2**c
        positive_h_limit = (2**c)/(4**d*math.factorial(2*d))
        cube_coefficient = (2**d)/(4**d*math.factorial(2*d))
        assert positive_h_limit / cube_coefficient == 2**(c-d)
        print('exact-cut-check d={} components={} energy-levels={} ground-multiplicity={}'.format(
            d,c,len(set(gaps)),gaps.count(0)))

    # Independent quadrature of the original joint difference density.
    for t in (1,3,5,8):
        limit=(t**4+max(0,t-4)**4)/192.
        errors=[]
        for h in (0.02,0.01,0.003):
            observed=integrate_2d(h,h*t)/h**4
            relative=abs(observed/limit-1)
            errors.append(relative)
            assert relative < 0.11
            print('boundary-layer h={:.3f}, t={}, observed={:.10f}, limit={:.10f}, relative-error={:.5f}'.format(
                h,t,observed,limit,relative))
        assert errors[2] < errors[1] < errors[0]

    # Separately fix the geometry before shrinking the distance tolerance.
    for h in (0.05,0.15,0.35):
        for delta in (0.0015,0.003):
            measured=integrate_2d(h,delta)
            predicted=(delta**4)*fixed_tail_coefficient(2,[(0,1,1)],h)
            assert abs(measured/predicted-1)<0.008
            print('fixed-geometry h={}, delta={}, relative-error={:.5f}'.format(
                  h,delta,abs(measured/predicted-1)))
    print('VERIFY_OK')

if __name__=='__main__':run()
