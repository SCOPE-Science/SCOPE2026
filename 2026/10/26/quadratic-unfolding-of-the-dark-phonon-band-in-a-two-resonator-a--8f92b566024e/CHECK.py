"""Direct Bloch-matrix numerical checks for a two-resonator acoustic chain.

Usage: python CHECK.py (requires numpy). All assertions use positive parameters.
Numerical tests support, but do not replace, the analytic proof.
"""
import numpy as np


def matrix(z, a, b, r1, r2):
    return np.array([
        [z + a*r1 + b*r2, -np.sqrt(a)*r1, -np.sqrt(b)*r2],
        [-np.sqrt(a)*r1, r1, 0.0],
        [-np.sqrt(b)*r2, 0.0, r2],
    ])


def middle(z, a, b, r1, r2):
    eigvals, eigvecs = np.linalg.eigh(matrix(z, a, b, r1, r2))
    return eigvals[1], eigvecs[0, 1] ** 2


def theoretical(z, a, b, r, eps):
    s = a+b
    return (r + (a-b)/s*eps
            + 4*a*b/(r*r*s**3)*(z-r*(1+s))*eps**2)


def run():
    count = 0
    cases = [(1., 2., 3., 5.), (.1, 3., 2., 9.), (4., 4., 7., 5.),
             (.6, .7, 4., 8.), (3., .15, 1.5, 2.)]
    for a, b, r, c in cases:
        coef = 4*a*b/(r*r*(a+b)**3)
        previous_err = None
        for eps in [.04, .02, .01, .005]:
            x = np.linspace(0, c, 17)
            vals = [middle(z, a, b, r-eps, r+eps) for z in x]
            eig = np.array([pair[0] for pair in vals])
            host = np.array([pair[1] for pair in vals])
            assert np.all(np.diff(eig) > 0), (a,b,r,c,eps)
            assert np.all((eig > r-eps) & (eig < r+eps))
            # Uniform, second-order mode and projector limits.
            err = np.max(np.abs(eig-np.array([theoretical(z,a,b,r,eps) for z in x])))
            if previous_err is not None:
                assert err < previous_err * .5, (err,previous_err,a,b,r,eps)
            previous_err = err
            assert np.max(np.abs(host/eps**2-coef)) < max(3.,coef)*eps*120, (a,b,r,eps)
            width = eig[-1]-eig[0]
            assert abs(width / eps**2 - c*coef) < max(1.,c*coef) * eps * 100, (a,b,r,eps)
            # Non-asymptotic host share upper bound; also finite difference gradient.
            A=(a*(r-eps)**2)**(1./3.)
            B=(b*(r+eps)**2)**(1./3.)
            bound=1./(1.+(A+B)**3/(2*eps)**2)
            assert np.all(host <= bound*(1.+1.e-9))
            for i in range(1,len(x)-1):
                slope=(eig[i+1]-eig[i-1])/(x[i+1]-x[i-1])
                assert abs(slope-host[i]) < 0.015, (slope,host[i])
            count += 1
    print('PASS:',count,'parameter/detuning combinations; monotonicity, eigenvalue interlacing,')
    print('second-order asymptotics, normalized host energy and uniform slope bound.')

if __name__ == '__main__':
    run()
