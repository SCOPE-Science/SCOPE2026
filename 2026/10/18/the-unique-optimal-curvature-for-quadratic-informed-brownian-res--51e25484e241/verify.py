"""Independent numerical checks for quadratic-position-reset first passage.

Requires Python 3, NumPy and SciPy. Analytic proofs appear in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gamma, kv
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

C = math.sqrt(2.0) / gamma(0.25)

def u(x):
    return 1.0 if x == 0 else C * math.sqrt(x) * kv(0.25, x*x/2.0)

def I(x):
    return quad(u, x, 12.0, epsabs=1e-13, epsrel=2e-13, limit=100)[0]

def h(x):
    return I(x) / u(x)**2

def m(x):
    return quad(h, 0.0, x, epsabs=1e-12, epsrel=2e-13, limit=100)[0]

def F(x):
    return x * h(x) - 2.0 * m(x)

def phi(x):
    return m(x) / x**2

def finite_difference(kappa, dx, endpoint=7.0):
    n = round(endpoint/dx)
    reset_index = round(1.0/dx) - 1
    assert abs(n*dx-endpoint)<1e-10 and abs((reset_index+1)*dx-1)<1e-10
    A = lil_matrix((n,n))
    rhs = np.ones(n)
    for i in range(1,n+1):
        row = i-1
        x = i*dx
        A[row,row] = 2.0/dx**2 + kappa*x*x
        if i > 1:
            A[row,row-1] = -1.0/dx**2
        if i < n:
            A[row,row+1] = -1.0/dx**2
        else:
            A[row,row-1] = -2.0/dx**2  # remote Neumann endpoint
        A[row,reset_index] -= kappa*x*x  # resetting to x=1
    return float(spsolve(A.tocsc(),rhs)[reset_index])

def main():
    zstar = brentq(F,1.5,1.6,xtol=1e-13)
    curvature = zstar**4
    best = phi(zstar)
    assert abs(F(zstar))<1e-10
    assert 1.54848 < zstar < 1.54849
    assert 5.74947 < curvature < 5.74949
    assert 0.93928 < best < 0.93930
    # Confirm the computed global minimum's local sign at independent points.
    for z in [0.2,0.5,1.0,1.3,1.5]:
        assert F(z)<0
    for z in [1.6,1.9,2.5,3.0]:
        assert F(z)>0
    for k in [1.,3.,curvature,10.,20.]:
        truth = phi(k**.25)
        e1=abs(finite_difference(k,0.025)-truth)
        e2=abs(finite_difference(k,0.0125)-truth)
        assert e2<2.3e-5 and 3.8<e1/e2<4.2,(k,e1,e2)
        print('curvature',round(k,9),'analytic',format(truth,'.12g'),
              'FD_errors',format(e1,'.3g'),format(e2,'.3g'))
    print('unique-root numerical estimate',format(zstar,'.12g'))
    print('optimal dimensionless curvature',format(curvature,'.12g'))
    print('optimal dimensionless mean time',format(best,'.12g'))
    print('PASS: 9 stationary-sign tests, 5 FD comparisons, 5 mesh-refinement checks, 4 root/value checks')

if __name__ == '__main__':
    main()
