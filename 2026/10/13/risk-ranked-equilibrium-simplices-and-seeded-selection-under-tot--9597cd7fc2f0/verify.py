#!/usr/bin/env python3
"""Exact rational checks for a two-patch infected-lockdown SIS theorem.

No third-party packages required. Finite examples corroborate the analytic proof.
"""
from fractions import Fraction as F


def mul(A, B):
    n = len(A)
    return [[sum(A[i][q] * B[q][j] for q in range(n)) for j in range(n)]
            for i in range(n)]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def charpoly_desc(A):
    """Exact Faddeev-LeVerrier coefficients, highest degree first."""
    n = len(A)
    B = eye(n)
    coeffs = [F(1)]
    for k in range(1, n + 1):
        AB = mul(A, B)
        c = -sum(AB[i][i] for i in range(n)) / k
        coeffs.append(c)
        B = [[AB[i][j] + (c if i == j else F(0))
              for j in range(n)] for i in range(n)]
    return coeffs


def poly_mul_desc(A, B):
    out = [F(0)] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            out[i + j] += a * b
    return out


def poly_product(*factors):
    p = [F(1)]
    for factor in factors:
        p = poly_mul_desc(p, [F(v) for v in factor])
    return p


def jacobian(risks, infected, d=F(2)):
    """Order: S1, S2, I11, I12, I21, I22; beta_v=1."""
    assert len(risks) == 4 and len(infected) == 4
    assert sum(infected) + 2 * risks[0] == 8 or sum(infected) == 0
    s = risks[0] if sum(infected) else F(4)
    patch = (0, 1, 0, 1)
    J = [[F(0) for _ in range(6)] for _ in range(6)]
    for j in range(2):
        J[j][j] -= d
        J[j][1-j] += d
    for v, j in enumerate(patch):
        risk = F(risks[v])
        I = F(infected[v])
        J[j][j] -= I
        J[j][v+2] -= s-risk
        J[v+2][j] += I
        J[v+2][v+2] += s-risk
    return J


def run():
    # Unique minimum-risk cell, r=1, N=8, two patches.
    r = tuple(map(F, (1, 2, 3, 4)))
    J = jacobian(r, tuple(map(F, (6, 0, 0, 0))))
    want = poly_product((1,0),(1,1),(1,2),(1,3),(1,10,12))
    assert charpoly_desc(J) == want

    # Higher-risk equilibrium: one positive invasion eigenvalue, 1-2 < 0.
    # The equilibrium at r=2 has positive invasion rate 2-1=1.
    J = jacobian_at_r(r, F(2), (0, 4, 0, 0))
    want = poly_product((1,0),(1,-1),(1,1),(1,2),(1,8,8))
    assert charpoly_desc(J) == want

    # Two minimum-risk cells at distinct patches: interior of a continuum.
    r_tie = tuple(map(F, (1, 1, 3, 4)))
    J = jacobian_at_r(r_tie, F(1), (2, 4, 0, 0))
    want = poly_product((1,0),(1,0),(1,2),(1,3),(1,10,20))
    assert charpoly_desc(J) == want
    # The double zero is semisimple: two independent equilibrium tangent
    # directions in full 6-space, one eliminated on the mass hyperplane.
    assert nullity(J) == 2

    # A vertex on the same tie-simplex also has two semisimple zeros.
    J = jacobian_at_r(r_tie, F(1), (6, 0, 0, 0))
    want = poly_product((1,0),(1,0),(1,2),(1,3),(1,10,12))
    assert charpoly_desc(J) == want
    assert nullity(J) == 2

    # Verify the DFE spectrum and the equality-threshold neutral cell r=4.
    J = jacobian_at_r(r, F(4), (0, 0, 0, 0))
    want = poly_product((1,0),(1,0),(1,4),(1,-3),(1,-2),(1,-1))
    assert charpoly_desc(J) == want

    # Exact mass balance and dissipation at an arbitrary rational state.
    S1, S2 = F(2), F(1)
    I = tuple(map(F, (1, 1, 1, 2)))
    d = F(2)
    ds1 = d*(S2-S1)-(S1-r[0])*I[0]-(S1-r[2])*I[2]
    ds2 = d*(S1-S2)-(S2-r[1])*I[1]-(S2-r[3])*I[3]
    dI = [(S1-r[0])*I[0], (S2-r[1])*I[1],
          (S1-r[2])*I[2], (S2-r[3])*I[3]]
    assert ds1+ds2+sum(dI) == 0
    Vdot = S1*ds1+S2*ds2+sum(r[v]*dI[v] for v in range(4))
    squared = -d*(S1-S2)**2-sum(I[v]*(
        (S1 if v in (0,2) else S2)-r[v])**2 for v in range(4))
    assert Vdot == squared
    assert Vdot < 0
    print('VERIFY_OK')
    print('unique_minimum_polynomial', poly_product((1,0),(1,1),(1,2),(1,3),(1,10,12)))
    print('higher_risk_positive_invasion_rate', F(1))
    print('tied_risk_zero_multiplicity', 2)
    print('dissipation', Vdot)


def jacobian_at_r(risks, s, infected, d=F(2)):
    assert sum(F(v) for v in infected) + 2*s == F(8)
    patch = (0, 1, 0, 1)
    J = [[F(0) for _ in range(6)] for _ in range(6)]
    for j in range(2):
        J[j][j] -= d
        J[j][1-j] += d
    for v, j in enumerate(patch):
        rv = F(risks[v])
        Iv = F(infected[v])
        J[j][j] -= Iv
        J[j][v+2] -= s-rv
        J[v+2][j] += Iv
        J[v+2][v+2] += s-rv
    return J


def nullity(A):
    """Exact Gaussian elimination over rationals."""
    B = [[F(v) for v in row] for row in A]
    m, n = len(B), len(B[0])
    pivotrow = 0
    for col in range(n):
        pivot = next((i for i in range(pivotrow, m) if B[i][col]), None)
        if pivot is None:
            continue
        B[pivotrow], B[pivot] = B[pivot], B[pivotrow]
        factor = B[pivotrow][col]
        B[pivotrow] = [x / factor for x in B[pivotrow]]
        for row in range(m):
            if row != pivotrow:
                factor = B[row][col]
                if factor:
                    B[row] = [a-factor*b for a,b in zip(B[row],B[pivotrow])]
        pivotrow += 1
        if pivotrow == m:
            break
    return n-pivotrow


if __name__ == '__main__':
    run()
