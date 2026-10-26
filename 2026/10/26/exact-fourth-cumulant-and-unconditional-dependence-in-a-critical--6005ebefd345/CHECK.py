"""Exact-rational checks of a stationary telegraph-filter fourth-cumulant identity.

No dependencies beyond the Python standard library. These finite checks are
illustrative verification of algebra; the accompanying proof covers the full
parameter domain.
"""
from fractions import Fraction as F


def check(a, c, delta, b):
    r = 1-a
    k = 2*a-1
    ell = 2*b-1
    assert F(1,2) < a <= 1 and c > 0 and delta > 0
    assert r+2*delta < 1 and b >= a
    D, E = a+2*c, 3*a+2*c
    m11 = delta/D
    m20 = delta**2/(a*D)
    m31 = 3*delta**3/(a*D*E)
    m40 = 3*delta**4/(a*a*D*E)
    S11, S12, S22 = m40-m20**2, m31-m20*m11, m20-m11**2
    assert S11 == 4*c*delta**4/(a*a*D*D*E)
    assert S12 == 4*c*delta**3/(a*D*D*E)
    assert S22 == 2*c*delta**2/(a*D*D)
    v1, v2 = r*r, 2*r*delta

    def laplace_cov(z):
        # The inverse of zI - M.T; M=[[-2a,2delta],[0,-D]].
        R11 = 1/(z+2*a)
        R21 = 2*delta/((z+2*a)*(z+D))
        R22 = 1/(z+D)
        w1, w2 = R11*v1, R21*v1+R22*v2
        return (v1*(S11*w1+S12*w2)+v2*(S12*w1+S22*w2))/4

    avg_Q = F(1,8)-delta**2*(1+2*a*c)/(2*a*D)
    Q0 = F(1,8)-delta**2/2
    assert avg_Q == Q0-r*r*m20/2-r*delta*m11
    EV = avg_Q/k
    # Independent calculation via the stationarity equations for (U,E,V).
    Q_ue = Q0*m11-r*r*m31/2-r*delta*m20
    Q_u2 = Q0*m20-r*r*m40/2-r*delta*m31
    EVue = (delta*EV+Q_ue)/(D+k)
    EVu2 = (2*delta*EVue+Q_u2)/(2*a+k)
    EVQ = Q0*EV-r*r*EVu2/2-r*delta*EVue
    var_V_direct = EVQ/k-EV**2
    var_V_resolvent = laplace_cov(k)/k
    assert var_V_direct == var_V_resolvent
    polynomial = 9*a**3+10*a*a*c+7*a*a+3*a+2*c-1
    fourth_cumulant = 3*c*delta**4*(a-1)**2*polynomial / (
        a*a*D*D*(2*a-1)*(3*a+2*c)*(4*a-1)*(3*a+2*c-1)
    )
    assert fourth_cumulant == 3*var_V_direct
    assert (fourth_cumulant > 0) == (a < 1)
    # Given their shared background, independent Gaussian modes have this
    # exact covariance of squared magnitudes.
    square_cov = (laplace_cov(k)+laplace_cov(ell))/(k+ell)
    assert (square_cov > 0) == (a < 1)
    if k == ell:
        assert square_cov == var_V_direct
    return fourth_cumulant, square_cov


def main():
    trials = 0
    for a in [F(3,5),F(2,3),F(3,4),F(4,5),F(9,10),F(1)]:
        for c in [F(1,10),F(1,3),F(2,3),F(2)]:
            for d in [F(1,16),F(1,8)]:
                if (1-a)+2*d >= 1:
                    continue
                for b in [a,F(1)]:
                    check(a,c,d,b)
                    trials += 1
    assert check(F(3,5),F(1,10),F(1,8),F(3,5))[0] == F(13,24576)
    assert check(F(3,4),F(2,3),F(1,20),F(1))[0] == F(8103,16662500000)
    print(f"PASS: {trials} rational parameter/mode tests, 2 regression identities")


if __name__ == "__main__":
    main()
