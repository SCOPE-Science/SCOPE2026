"""Stand-alone numerical/exact-incidence checks for central sections of cube-octahedron intersections.
Only the Python standard library is required. This is finite corroboration, not an infinite proof.
"""
import itertools
import math
import random
from collections import Counter

PI = math.pi


def section_type_formula(c, normal):
    a, b, d = sorted(map(abs, normal), reverse=True)
    if c < 2:
        s = c - 1
        return 4 + 2 * (d > s * b) + 2 * (b < s * a) + 2 * (d < s * a)
    if c > 2:
        z = c - 2
        return (4 + 2 * (a < b + z * d)
                + 2 * (b > d + z * a)
                + 2 * (b + d > z * a and a > d + z * b))
    return 8


def graph(c):
    if c == 2:
        seed = (1, 1, 0)
    elif c < 2:
        seed = (1, c - 1, 0)
    else:
        seed = (1, 1, c - 2)
    vv = set()
    for v in set(itertools.permutations(seed)):
        for signs in itertools.product((-1, 1), repeat=3):
            vv.add(tuple(float(s * x) for x, s in zip(v, signs)))
    vv = sorted(vv)
    if c == 2:
        edges = [(i, j) for i in range(len(vv)) for j in range(i+1, len(vv))
                 if abs(sum((vv[i][k] - vv[j][k])**2 for k in range(3)) - 2) < 1e-9]
    else:
        labels = []
        for v in vv:
            aset = set()
            for i in range(3):
                for s in [-1, 1]:
                    if abs(s * v[i] - 1) < 1e-8:
                        aset.add(('cube', i, s))
            for signs in itertools.product((-1, 1), repeat=3):
                if abs(sum(x*s for x,s in zip(v, signs)) - c) < 1e-8:
                    aset.add(('octa',) + signs)
            labels.append(aset)
        edges = [(i, j) for i in range(len(vv)) for j in range(i+1, len(vv))
                 if len(labels[i].intersection(labels[j])) >= 2]
    assert (len(vv), len(edges)) == ((12, 24) if c == 2 else (24, 36))
    return vv, edges


def section_type_by_edges(vv, edges, normal):
    values = [sum(x*u for x,u in zip(v, normal)) for v in vv]
    return sum(values[i] * values[j] < 0 for i,j in edges)


def quadrilateral_probability(delta):
    q = math.sqrt(1 + delta*delta)
    return 12/PI * math.atan((q-1)/(q+1))


def simpson(f, n=20000):
    assert n % 2 == 0
    h = 1.0/n
    return h/3*(f(0)+f(1)+4*sum(f((2*k-1)*h) for k in range(1,n//2+1))
                +2*sum(f((2*k)*h) for k in range(1,n//2)))


def check():
    rng = random.Random(20261020)
    for c in [1.2, 1.5, 1.93, 1.997, 2., 2.003, 2.07, 2.5, 2.9]:
        vv,ee=graph(c)
        for _ in range(1500):
            normal=tuple(rng.gauss(0,1) for _ in range(3))
            lhs=section_type_by_edges(vv,ee,normal)
            rhs=section_type_formula(c,normal)
            assert lhs==rhs,(c,normal,lhs,rhs)
    print('INDEPENDENT_POLYHEDRAL_EDGE_ENUMERATION_ALL_CHAMBERS_SAMPLED_OK')

    # Evaluate independent smooth spherical-interface quadratures and their closed forms.
    integrals = [
        (lambda t:(2+t*t)**(-1.5), 1/(2*math.sqrt(3))),
        (lambda t:t/(1+2*t*t)**1.5, (1-1/math.sqrt(3))/2),
        (lambda t:(1+2*t*t)**(-1.5), 1/math.sqrt(3)),
        (lambda t:t/(2+t*t)**1.5, 1/math.sqrt(2)-1/math.sqrt(3)),
    ]
    for f,ans in integrals:
        assert abs(simpson(f)-ans) < 2e-12
    print('FOUR_SPHERICAL_INTERFACE_INTEGRALS_OK')

    # Independently measure octagon-breakdown probabilities in the Haar model.
    n=550000
    deltas=(0.04,0.025)
    observed={('left',z):Counter() for z in deltas}
    observed.update({('right',z):Counter() for z in deltas})
    for _ in range(n):
        u=(rng.gauss(0,1),rng.gauss(0,1),rng.gauss(0,1))
        for z in deltas:
            observed['left',z][section_type_formula(2-z,u)] += 1
            observed['right',z][section_type_formula(2+z,u)] += 1
    L6=2*math.sqrt(3)/PI
    L10=6/PI*(1-1/math.sqrt(3))
    R6=4*math.sqrt(3)/PI
    R10=12/PI*(1/math.sqrt(2)-1/math.sqrt(3))
    for z in deltas:
        l=observed['left',z];r=observed['right',z]
        assert set(l) <= {6,8,10} and set(r) <= {4,6,8,10}
        for label,prob in [('left',L6*z+L10*z),('right',R6*z+R10*z)]:
            empirical=1-observed[label,z][8]/n
            # Controlled O(z^2) bias plus a conservative eight-standard-error interval.
            stderr=(max(prob*(1-prob),0)/n)**.5
            assert abs(empirical-prob)< 1.1*z*z+8*stderr,(z,label,empirical,prob)
        empirical4=r[4]/n
        exact4=quadrilateral_probability(z)
        assert abs(empirical4-exact4)<8*math.sqrt(max(exact4*(1-exact4),1e-15)/n)+2/n
    print('HAAR_TWO_SIDED_OCTAGON_BREAKDOWN_AND_EXACT_QUADRILATERAL_LAW_OK',n)
    # Exact cone-probability identity interpolates the cuboctahedron and cube.
    assert abs(quadrilateral_probability(1)-(6*math.asin(1/3)/PI))<1e-14
    for z in [0.001,0.01,0.04,0.1]:
        assert abs(quadrilateral_probability(z)-(3/PI)*z*z)<z**4
    for z in [0.2, 0.5, 0.8]:
        trials = 70000
        hits = sum(section_type_formula(2+z, tuple(rng.gauss(0,1) for _ in range(3))) == 4
                   for _ in range(trials))
        p4 = quadrilateral_probability(z)
        assert abs(hits/trials-p4) < 6*math.sqrt(p4*(1-p4)/trials)+2/trials
    print('EXACT_QUADRILATERAL_SOLID_ANGLE_AND_CUBE_ENDPOINT_OK')
    print('ALL_CUBOCTAHEDRAL_PHASE_TRANSITION_CHECKS_OK')

if __name__=='__main__':
    check()
