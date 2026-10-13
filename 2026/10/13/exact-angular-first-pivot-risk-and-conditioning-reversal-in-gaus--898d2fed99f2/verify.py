"""Standalone checks of the two-column Gaussian-sketch pivot comparison.
This supplements the analytic proof in RESULT.md; it does not certify it.
Run with: python3 verify.py
"""
from fractions import Fraction as F
from math import comb, sqrt, pi
from random import Random


def beta_equal_cdf_even_rows(z, rows):
    """For even rows=2k, I_z(k,k) as an exact binomial tail."""
    assert rows > 0 and rows % 2 == 0
    k = rows // 2
    return sum(F(comb(2*k-1, j))*z**j*(1-z)**(2*k-1-j)
               for j in range(k, 2*k))


def exact_risk(kappa, rho, rows, delta):
    d = F(kappa*kappa-1)
    assert delta*delta == (F(kappa*kappa+1)**2-4*F(kappa*kappa)*rho*rho)
    z = (1-d/delta)/2
    return beta_equal_cdf_even_rows(z, rows)


assert exact_risk(F(2),F(0),2,F(5)) == F(1,5)
assert exact_risk(F(2),F(3,4),2,F(4)) == F(1,8)
assert exact_risk(F(2),F(0),4,F(5)) == F(13,125)
assert exact_risk(F(2),F(3,4),4,F(4)) == F(11,256)
# Exact diagonalization: for rho=3/4 and kappa=2, eigenvalues 7/2 and -1/2.
assert (F(7,2)-F(1,2)) == F(3)
assert F(7,2)*F(1,2) == F(4)*(1-F(3,4)**2)
for rows in (2,4,6,8,10,12,20,40):
    independent = exact_risk(F(2),F(0),rows,F(5))
    correlated = exact_risk(F(2),F(3,4),rows,F(4))
    assert F(0) < correlated < independent < F(1,2)

# Endpoint Laplace asymptotic for the exact rational beta tails.
for z in (F(1,5),F(1,8)):
    for rows in (100,200):
        true_p = float(beta_equal_cdf_even_rows(z,rows))
        zf = float(z)
        approx = (4*zf*(1-zf))**(rows/2)/((1-2*zf)*sqrt(2*pi*rows))
        assert 0 < abs(approx/true_p-1) < 0.025

# Independent Monte Carlo sampling from the initial sketched QRCP decision.
rng = Random(130122)
for rows, rho, expected in ((2,0.0,0.2),(2,0.75,0.125),
                             (4,0.0,0.104),(4,0.75,11/256)):
    count=0
    reps=60000
    for _ in range(reps):
        xsum=0.0
        ysum=0.0
        for __ in range(rows):
            x=rng.gauss(0,1)
            h=rng.gauss(0,1)
            u=2*x
            v=rho*x+sqrt(1-rho*rho)*h
            xsum += u*u
            ysum += v*v
        if xsum < ysum:
            count += 1
    estimate = count/reps
    print(f'rows={rows}, rho={rho}: estimate={estimate:.6f} exact={expected:.6f}')
    assert abs(estimate-expected) < 0.009
print('VERIFY_OK')
