#!/usr/bin/env python3
"""Exact-rational checks for the two-cycle bifurcation theorem.

Run with Python 3. No nonstandard packages are required. This checks the
algebraic identities and interval-sign certificates; proof of exhaustive
root counts uses the Descartes and monotonicity arguments in RESULT.md.
"""
from fractions import Fraction as Q

A = Q(1, 100)
B = Q(1, 10)
D = Q(1, 10)
K = 8*B/(1+B)**2 + 2*D
C_INF = (1+B/2)/2
C_FOLD = C_INF - A*A/(2*K)
H_COEFF = (1+B)/2
R2 = Q(48, 121)
assert K == Q(521, 605)
assert C_INF == Q(21, 40)
assert C_FOLD == Q(1093979, 2084000)


def c_of_t(t):
    return C_INF + K/(2*t*t) - A/t


def map_f(p,c):
    x,y = p
    return (x+y,y-A*abs(y)-x*y+B*x*x-c*y*y+D)


def matmul(u,v):
    return tuple(tuple(sum(u[i][k]*v[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def jac(p,c):
    x,y = p
    assert y != 0
    sign = 1 if y > 0 else -1
    return ((Q(1),Q(1)),(-y+2*B*x,Q(1)-A*sign-x-2*c*y))


def det(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]


def poly(t):
    return (44289025*t**4 - 350885359*t*t
            -2521640*t + 108576400)


def w(t):
    return K/t - A


def h(t):
    return H_COEFF*t


def v(t):
    return w(t)-h(t)


def trdet(t):
    return Q(290,121)-(w(t)+h(t))**2, Q(169,121)-v(t)**2


# Verified branches at exact rational sample amplitudes, both inside and
# outside the attracting bands. Checking the literal map and Jacobians
# independently guards against symbolic expression/transcription errors.
for t in [Q(1, 3),Q(1, 2),Q(3, 5),Q(7, 10),Q(4, 5),Q(1),
          Q(3, 2),Q(2),Q(5, 2),Q(3),Q(4),Q(30),Q(50),Q(80),Q(90)]:
    c = c_of_t(t)
    X = Q(2)/(1+B)
    p,q = (X-t/2,t),(X+t/2,-t)
    assert map_f(p,c) == q, (t,c,'first return')
    assert map_f(q,c) == p, (t,c,'second return')
    J = matmul(jac(q,c),jac(p,c))
    trace, determinant = trdet(t)
    assert trace == J[0][0]+J[1][1]
    assert determinant == det(J)
    assert 1-trace+determinant == 2*(1+B)*(K-A*t)
    assert (t*t * (w(t)*w(t)+h(t)*h(t)-Q(290,121))
            == poly(t)/Q(146410000))

# Descartes: the quartic has sign changes +,-,-,+, hence at most two
# positive roots. These disjoint sign-changing rational brackets show
# two exist, so they exhaust all positive roots.
fl = (Q(564,1000),Q(565,1000))
fu = (Q(2760,1000),Q(2761,1000))
assert poly(fl[0]) > 0 > poly(fl[1])
assert poly(fu[0]) < 0 < poly(fu[1])

# V is strictly decreasing, with derivative -K/t**2-(1+B)/2<0.
# It meets +/-4 sqrt(3)/11 exactly once, at the enclosed amplitudes.
up = (Q(798,1000),Q(799,1000))
um = (Q(1935,1000),Q(1937,1000))
assert v(up[0]) > 0 and v(up[0])**2 > R2
assert v(up[1]) > 0 and v(up[1])**2 < R2
assert v(um[0]) < 0 and v(um[0])**2 < R2
assert v(um[1]) < 0 and v(um[1])**2 > R2
assert fl[1] < up[0] < up[1] < um[0] < um[1] < fu[0]
assert fu[1] < K/(2*A)

# Exact Jury sign witnesses on each of the five alternating stability
# sectors. All bracket endpoints correspond to nonzero branch states.
for t,stable in [(Q(1,2),False),(Q(3,5),True),
                 (Q(1),False),(Q(5,2),True),(Q(3),False)]:
    tr,de=trdet(t)
    jury = (1-tr+de>0 and 1+tr+de>0 and 1-de>0)
    assert jury == stable, (t,jury,stable)

# Global count: L is positive between the fold and escape boundaries.
# Both roots are positive there. At and above the escape boundary only
# the finite-amplitude branch persists. This verifies exact witness
# values but the proof covers every real c>0 analytically.
for c,expected in [(Q(1,2),0),(C_FOLD,1),
                   (C_FOLD/2+C_INF/2,2),(C_INF,1),
                   (Q(3,5),1),(Q(2),1)]:
    L=1+B/2-2*c
    discr=A*A-L*K
    if L>0:
        count=0 if discr<0 else (1 if discr==0 else 2)
    else:
        count=1
    assert count==expected,(c,count,expected)

print('PASS: 15 exact full-map returns, two-step Jacobians, derivative identities;')
print('      two Descartes root brackets, two unit-modulus root brackets;')
print('      five Jury sectors, six orbit-census witnesses, all exact rationals.')
