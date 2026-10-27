#!/usr/bin/env python3
"""Standalone finite transport checks for cross-polytope facet-centroid interpolation.

Requires only Python 3's standard library. The full-dimensional theorem uses
an analytic symmetry and transport proof; these are finite corroborations.
"""
import itertools
import math


def distance(u, v):
    if u == v:
        return 0.0
    if u[0] == v[0]:
        return 2.0
    return math.sqrt(2.0)


def run(d):
    unit = [(i, sign) for i in range(d) for sign in (-1, 1)]
    facets = list(itertools.product((-1, 1), repeat=d))
    lower_vertex = math.sqrt(2.0*(d-1)/d)
    opposite_facets = math.sqrt(d/2)
    face_vertex_distance = math.sqrt((d-1)/d)
    b = (opposite_facets - lower_vertex)/(2/face_vertex_distance+2*d*opposite_facets)
    a = 1/d-b
    optimum = opposite_facets*(1-2*d*b)
    assert 0 < b < a
    assert abs((lower_vertex+2*b/face_vertex_distance)-optimum) < 1e-12
    assert math.sqrt(2.0*(d-1)/d)+2*b/face_vertex_distance > lower_vertex

    def weights(s):
        return {u:(a if u[1] == s[u[0]] else b) for u in unit}

    # There is only one sink in the vertex-facet transport problem.
    vc = 0
    for s in facets:
        w = weights(s)
        for u in unit:
            dist_to_f = math.sqrt((d-1)/d) if u[1] == s[u[0]] else math.sqrt(1+3/d)
            cost = sum(coeff*distance(v, u) for v, coeff in w.items())
            assert cost/dist_to_f <= optimum + 1e-10, (d, s, u, cost, optimum)
            vc += 1

    # Compare finite transportation matchings independently of the derangement proof.
    fc = 0
    matching_perms = 0
    for i, s in enumerate(facets):
        w = weights(s)
        for t in facets[i+1:]:
            difference = [w[u]-weights(t)[u] for u in unit]
            positive = [u for u, val in zip(unit, difference) if val > 1e-12]
            negative = [u for u, val in zip(unit, difference) if val < -1e-12]
            amount = max(difference)
            # All nonzero source and sink masses are identical.
            assert len(positive) == len(negative)
            assert all(abs(abs(v)-amount)<1e-12 for v in difference if abs(v)>1e-12)
            best = min(sum(distance(positive[j], negative[k]) for j,k in enumerate(perm))
                       for perm in itertools.permutations(range(len(negative))))
            matching_perms += math.factorial(len(positive))
            dist_to_t = (2/d)*math.sqrt(sum(x != y for x,y in zip(s,t)))
            assert amount*best/dist_to_t <= optimum+1e-10
            fc += 1
    print(f'd={d}: vertex-face pairs={vc}, face-face pairs={fc}, '
          f'matchings checked={matching_perms}, norm={optimum:.12f}')
    return vc,fc


def main():
    total_vc=total_fc=0
    for d in (3,4,5,6):
        x,y=run(d)
        total_vc+=x;total_fc+=y
    print(f'PASS finite checks: {total_vc} vertex-face; {total_fc} facet-facet')

if __name__=='__main__':
    main()
