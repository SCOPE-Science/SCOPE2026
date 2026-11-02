"""Reproduce exact rational and numerical checks for a two-stage gradient scheme.

Run: python3 verify_rk2.py
Requires only Python's standard library.
"""
from fractions import Fraction as F
from itertools import product
from math import isfinite


def q_formula(a, b, z):
    c = 1 + a - 2 * (a - 1) * b * (1 - b)
    return 1 - 2*z + c*z*z - a*z*z*z + a*a*z*z*z*z/4


def q_from_two_point_law(u, v, p, b, z):
    # P(Y=u)=p, P(Y=v)=1-p; different stages are independent.
    total = F(0)
    for y1, w1 in ((u, p), (v, 1-p)):
        for y2, w2 in ((u, p), (v, 1-p)):
            stage = 1 - z*y1/(2*b)
            mult = 1 - z*((1-b)*y1+b*y2*stage)
            total += w1*w2*mult*mult
    return total


def h(a, b, z):
    c = 1 + a - 2*(a-1)*b*(1-b)
    return a*a*z**3 - 4*a*z*z + 4*c*z - 8


def frontier(a, b):
    lo, hi = 0.0, 4.0
    while h(a, b, hi) <= 0:
        hi *= 2
    for _ in range(130):
        mid = (lo + hi)/2
        if h(a, b, mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def run():
    laws = [
        (F(1,2), F(3,2), F(1,2)),
        (F(1,4), F(7,4), F(1,2)),
        (F(1,2), F(5,4), F(1,3)),
    ]
    bs = [F(-2), F(-1), F(1,8), F(1,4), F(1,2), F(3,4), F(1), F(3,2), F(2)]
    zs = [F(1,10), F(1,4), F(1,2), F(1), F(2), F(3)]
    counts = {'exact_laws': 0, 'variance_identity': 0, 'frontiers': 0, 'matrix_cases': 0, 'shared_vs_independent': 0}
    for u, v, p in laws:
        mu = p*u + (1-p)*v
        assert mu == 1
        a = p*u*u + (1-p)*v*v
        for b, z in product(bs, zs):
            direct = q_from_two_point_law(u, v, p, b, z)
            analytic = q_formula(a, b, z)
            assert direct == analytic, (u, v, p, b, z, direct, analytic)
            gap = analytic - q_formula(a, F(1,2), z)
            assert gap == 2*(a-1)*z*z*(b-F(1,2))**2
            counts['exact_laws'] += 1
            counts['variance_identity'] += 1
    for a in (F(1), F(9,8), F(4,3), F(5,4), F(2), F(5), F(100)):
        af = float(a)
        sgd = 2/af
        zstar = frontier(af, 0.5)
        assert abs(h(af, 0.5, zstar)) < 1e-6
        if af == 1:
            assert abs(zstar-2) < 1e-12
        else:
            assert zstar > sgd and zstar < 4/af
        for b in (-2, -1, 0.125, 0.25, 0.5, 0.75, 1, 1.5, 2):
            root=frontier(af, b)
            assert isfinite(root) and root > 0
            assert q_formula(af, b, root*0.999) < 1
            assert q_formula(af, b, root*1.001) > 1
            assert root <= zstar + 1e-10
            if af > 1 and b != 0.5:
                assert root < zstar - 1e-10
            counts['frontiers'] += 1
    # Independent matrix check. Rotate a two-eigenvalue SPD Hessian by a
    # rational orthogonal matrix; enumerate all stage-noise outcomes exactly.
    rot = ((F(3,5),F(-4,5)), (F(4,5),F(3,5)))
    def mv(mat, vec):
        return tuple(sum(mat[i][j]*vec[j] for j in range(2)) for i in range(2))
    def norm2(vec):
        return sum(t*t for t in vec)
    for a1,a2 in ((F(1,2),F(3,2)), (F(1),F(2)), (F(1,3),F(9,4))):
        hh = tuple(tuple(sum(rot[i][k] * (a1,a2)[k] * rot[j][k]
                             for k in range(2)) for j in range(2)) for i in range(2))
        for initial in ((F(1),F(0)),(F(2),F(-1)),(F(1,3),F(2,5))):
            coeff = tuple(sum(rot[j][i]*initial[j] for j in range(2)) for i in range(2))
            for b in (F(1,4),F(1,2),F(1),F(2)):
                for z in (F(1,10),F(1,2),F(1)):
                    direct = F(0)
                    for y1 in (F(1,2),F(3,2)):
                        for y2 in (F(1,2),F(3,2)):
                            k1 = tuple(y1*t for t in mv(hh, initial))
                            stage = tuple(initial[i] - z*k1[i]/(2*b) for i in range(2))
                            k2 = tuple(y2*t for t in mv(hh, stage))
                            after = tuple(initial[i]-z*((1-b)*k1[i]+b*k2[i]) for i in range(2))
                            direct += F(1,4)*norm2(after)
                    spectral = sum(coeff[i]**2*q_formula(F(5,4), b, z*(a1,a2)[i])
                                   for i in range(2))
                    assert direct == spectral, (a1,a2,b,z,initial,direct,spectral)
                    counts['matrix_cases'] += 1
    # Midpoint has exactly the SGD frontier: (a*z-2)*(a*z*z-2*z+4).
    for a in (F(1), F(9,8), F(4,3), F(2), F(10)):
        for z in zs:
            assert h(a, F(1), z) == (a*z-2)*(a*z*z-2*z+4)
    # A Pareto(3) example has E[Y]=1, E[Y^2]=4/3, E[Y^4]=+infinity.
    # With independent stages at z=1/4 the finite amplification is exactly 355/576.
    assert q_formula(F(4,3), F(1,2), F(1,4)) == F(355,576)
    counts['shared_vs_independent'] += 1
    # Normalized optimal horizon r(a)=a*z(a) is strictly increasing and tends to 4.
    aa = [1, 1.0001, 1.1, 4/3, 2, 5, 10, 100, 1000, 1000000]
    rr = [a*frontier(a, 0.5) for a in aa]
    assert abs(rr[0]-2)<1e-12 and all(2-1e-12 <= x < 4 for x in rr)
    assert all(x<y for x,y in zip(rr,rr[1:]))
    assert abs(rr[-1]-4) < 3e-5
    print('VERIFY_OK', ', '.join(f'{k}={v}' for k,v in counts.items()), 'normalized_horizon_last=%.9f'%rr[-1])

if __name__ == '__main__':
    run()
