#!/usr/bin/env python3
"""Exact finite checks of the periodic ground-state identity used in the proof.

The infinite-dimensional limit is established analytically, not by these tests.
Run with: python3 VERIFY.py
"""
from fractions import Fraction as F


def verify_one(r, t, q, N):
    # Choosing s-t=r-1/r ensures rational Bloch data.
    s = t + r - 1 / r
    assert s > 0 and t > 0 and 0 < q <= 1
    phi = [F(1), r, r, F(1)]
    sigma = [F(1), s, F(1), t]
    c = [r, s * r * r, r, t]
    L = (r + t) / 2
    mass = [v * v for v in phi]
    for k in range(4):
        assert L * mass[k] == (c[k] + c[(k-1)%4]) / 2
        assert 2 * L * phi[k] == sigma[k]*phi[(k+1)%4] + sigma[(k-1)%4]*phi[(k-1)%4]
    S = sum((1/x for x in c), F(0))
    mbar = sum(mass, F(0)) / 4
    alpha = 2 / (S*mbar)
    D = r + 1/r
    assert alpha == 2*s*t/(L*(s+t)*D)
    assert alpha > 0
    v = [F((7*n*n+3*n+2)%17-6, n+2) for n in range(N)] + [F(0)]
    u = [phi[n%4]*v[n] for n in range(N)]
    norm = sum((mass[n%4]*v[n]*v[n] for n in range(N)), F(0))
    pairing = sum((sigma[n%4]*q**n*u[n]*u[n+1]
                   for n in range(N-1)), F(0))
    left = L*norm-pairing
    grad = sum((c[n%4]*q**n*(v[n+1]-v[n])**2/F(2)
                for n in range(N)), F(0))
    boundary = t*v[0]**2/F(2)
    potential = sum(((c[n%4]*(1-q**n) +
                      c[(n-1)%4]*(1-q**(n-1)))*v[n]**2/F(2)
                     for n in range(1,N)), F(0))
    assert left == grad+boundary+potential
    assert grad >= 0 and boundary >= 0 and potential >= 0
    return alpha, L


def verify_cell_cauchy():
    r=F(2);t=F(1);s=F(5,2)
    c=[r,s*r*r,r,t]; S=sum((1/x for x in c),F(0))
    y0=F(2,7);y4=F(9,5)
    y=[y0]
    for x in c:
        y.append(y[-1]+(y4-y0)/(S*x))
    assert y[-1]==y4
    energy=sum((c[k]*(y[k+1]-y[k])**2 for k in range(4)),F(0))
    assert energy==(y4-y0)**2/S
    ytest=[y0,F(1,9),F(5,4),F(3,2),y4]
    assert sum((c[k]*(ytest[k+1]-ytest[k])**2 for k in range(4)),F(0)) >= energy


if __name__ == '__main__':
    for r,t in [(F(1),F(1)),(F(2),F(1)),(F(3,2),F(2))]:
        for q in (F(1),F(4,5),F(2,3)):
            for N in (13,22):
                verify_one(r,t,q,N)
    verify_cell_cauchy()
    assert verify_one(F(1),F(1),F(3,4),14) == (F(1,2),F(1))
    assert verify_one(F(2),F(1),F(3,4),14) == (F(8,21),F(3,2))
    print('GEOMETRIC_FOUR_PERIODIC_AIRY_EDGE_EXACT_IDENTITIES_OK')
