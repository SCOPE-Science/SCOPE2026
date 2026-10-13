#!/usr/bin/env python3
"""Exact rational projection checks and deterministic geometric tests for planar Kaczmarz sampling.

The checker illustrates the closed-form theorem; the proof covers arbitrary finite spanning frames.
Only Python standard-library modules are required.
"""
from fractions import Fraction as F
from math import atan2, cos, pi, sqrt
from itertools import combinations

ZERO = F(0)
ONE = F(1)


def unit_circle(t):
    """Rational parametrization of unit normals by rational slope t."""
    t = F(t)
    return ((ONE-t*t)/(ONE+t*t), 2*t/(ONE+t*t))


def dot(u, v):
    return u[0]*v[0]+u[1]*v[1]


def zpoint(u):
    return (u[0]*u[0]-u[1]*u[1], 2*u[0]*u[1])


def projection(u):
    return ((ONE-u[0]*u[0], -u[0]*u[1]),
            (-u[1]*u[0], ONE-u[1]*u[1]))


def matmul(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def transpose(A):
    return tuple(tuple(A[j][i] for j in range(2)) for i in range(2))


def mulcov(C, normals, probs):
    ans = [[ZERO, ZERO], [ZERO, ZERO]]
    for u, p in zip(normals, probs):
        P = projection(u)
        S = matmul(matmul(P, C), transpose(P))
        for i in range(2):
            for j in range(2):
                ans[i][j] += p*S[i][j]
    return tuple(tuple(row) for row in ans)


def expect_norm_k(normals, probs, e0, k):
    C = tuple(tuple(e0[i]*e0[j] for j in range(2)) for i in range(2))
    for _ in range(k):
        C = mulcov(C, normals, probs)
    return C[0][0]+C[1][1]


def test_pair_exact():
    rationals = [F(0), F(1, 5), F(1, 3), F(1, 2), F(2, 3), F(1), F(3, 2)]
    normals = [unit_circle(t) for t in rationals]
    seeds = [(F(1), F(0)), (F(0), F(1)), (F(2), F(-3)), (F(3, 7), F(1, 6))]
    count = 0
    for a, b in combinations(normals, 2):
        overlap2 = dot(a,b)**2
        gamma = (ONE+overlap2)/2
        va, vb = (-a[1],a[0]), (-b[1],b[0])
        probs = [F(1, 2), F(1, 2)]
        for e in seeds:
            first = (dot(va, e)**2+dot(vb, e)**2)/2
            for k in range(1, 8):
                got = expect_norm_k([a,b], probs, e, k)
                assert got == first*gamma**(k-1), (a,b,e,k,got)
                count += 1
    return count


def test_isotropic_exact():
    normals = [(ONE, ZERO), (F(3,5),F(4,5)), (F(3,5),-F(4,5))]
    probs = [F(7,32), F(25,64), F(25,64)]
    zz = [zpoint(u) for u in normals]
    assert sum(p*z[0] for p,z in zip(probs,zz)) == 0
    assert sum(p*z[1] for p,z in zip(probs,zz)) == 0
    seeds = [(F(1),F(0)),(F(0),F(1)),(F(2),F(-3)),(F(7,11),F(-6,5))]
    count=0
    for e in seeds:
        energy = dot(e,e)
        for k in range(1,10):
            got=expect_norm_k(normals,probs,e,k)
            assert got == energy/F(2)**k, (e,k,got)
            count+=1
    return count


def test_moment_identity():
    normals = [unit_circle(F(t, 5)) for t in range(-4,5)]
    count=0
    for n in [2,3,4,6,9]:
        us=normals[:n]
        for j in range(1,11):
            weights=[F((i+j)%7+1) for i in range(n)]
            ss=sum(weights)
            probs=[v/ss for v in weights]
            zz=[zpoint(u) for u in us]
            mx=sum(p*z[0] for p,z in zip(probs,zz))
            my=sum(p*z[1] for p,z in zip(probs,zz))
            quadratic=sum(probs[i]*probs[k]*dot(us[i],us[k])**2
                          for i in range(n) for k in range(n))
            assert quadratic == (ONE+mx*mx+my*my)/2
            count+=1
    return count


def min_segment_origin(a,b):
    vx,vy=b[0]-a[0],b[1]-a[1]
    ss=vx*vx+vy*vy
    if ss==0:
        return sqrt(a[0]*a[0]+a[1]*a[1])
    t=max(0.,min(1., -(a[0]*vx+a[1]*vy)/ss))
    return sqrt((a[0]+t*vx)**2+(a[1]+t*vy)**2)


def test_arc_geometry():
    normals=[unit_circle(F(t,7)) for t in range(-10,11)]
    count=0
    for offset in range(0,13,2):
        for span in range(2,9):
            subset=normals[offset:offset+span]
            if len(subset)<2:
                continue
            points=[tuple(map(float,zpoint(u))) for u in subset]
            phases=sorted(atan2(z[1],z[0])%(2*pi) for z in points)
            gaps=[phases[(i+1)%len(phases)]-phases[i] if i<len(phases)-1
                  else phases[0]+2*pi-phases[-1] for i in range(len(phases))]
            biggest=max(gaps)
            r=0. if biggest<=pi+1e-11 else -cos(biggest/2)
            if r>1e-12:
                brute=min(min_segment_origin(a,b) for a,b in combinations(points,2))
                assert abs(r-brute)<2e-10, (r, brute, subset)
            count+=1
    return count


def test_specific_example():
    a=(ONE,ZERO)
    b=(F(3,5),F(4,5))
    interior=(F(4,5),F(3,5))
    assert dot(a,b)**2 == F(9,25)
    assert (ONE+dot(a,b)**2)/2 == F(17,25)
    # Every convex mixture of these doubled angles lies on the short arc;
    # the sharp lower bound comes from the extreme pair.
    for pa in range(0,11):
        for pb in range(0,11-pa):
            p=[F(pa,10),F(pb,10),F(10-pa-pb,10)]
            z=[zpoint(u) for u in [a,b,interior]]
            mx=sum(w*q[0] for w,q in zip(p,z))
            my=sum(w*q[1] for w,q in zip(p,z))
            assert mx*mx+my*my >= F(9,25)
    return 66


if __name__=='__main__':
    checks=(test_pair_exact()+test_isotropic_exact()+test_moment_identity()
            +test_arc_geometry()+test_specific_example())
    print('VERIFY_OK', checks, 'exact/geometry checks')
