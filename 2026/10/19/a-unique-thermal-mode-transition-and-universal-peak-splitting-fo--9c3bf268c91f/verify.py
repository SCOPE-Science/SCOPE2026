"""Independent quadrature checks for Gaussian-smoothed symmetric beta laws.

Requires numpy and scipy. Finite numerical checks support, but do not prove,
the analytic global-mode and critical-scaling statements.
"""
import math
import numpy as np
from scipy.special import hyp1f1, roots_jacobi
from scipy.optimize import brentq


def critical_variance(a):
    assert 0 < a < 1
    def center_equation(lam):
        return 2*lam/(2*a+1)*hyp1f1(1.5, a+1.5, -lam)/hyp1f1(.5, a+.5, -lam)-1
    hi = 1.
    while center_equation(hi) <= 0:
        hi *= 2.
    lam = brentq(center_equation, 1.e-7, hi, xtol=2.e-14)
    return 1/(2*lam)


def derivatives(a, t, x, n=450):
    # Gauss-Jacobi quadrature for (1-u^2)^(a-1), normalized to total mass one.
    u, w = roots_jacobi(n, a-1, a-1)
    w /= sum(w)
    z = (x-u)/math.sqrt(t)
    gaussian = np.exp(-z*z/2)/math.sqrt(2*math.pi*t)
    p = sum(w*gaussian)
    p1 = sum(w*gaussian*(-z/math.sqrt(t)))
    p2 = sum(w*gaussian*(z*z-1)/t)
    p4 = sum(w*gaussian*(z**4-6*z*z+3)/t**2)
    return np.array([p,p1,p2,p4])


def run():
    # Direct quadrature confirms the independently calculated hypergeometric roots.
    A = [.1,.25,.5,.75,.9]
    tc = [critical_variance(a) for a in A]
    assert all(tc[j]>tc[j+1] for j in range(len(tc)-1))
    for a,t in zip(A, tc):
        c = derivatives(a,t,0)
        assert abs(c[2]) < 2e-9, (a,c)
        assert c[3] < 0, (a,c)
        assert derivatives(a, t*.8, 0)[2] > 0
        assert derivatives(a, t*1.2, 0)[2] < 0
        for scale in [.8,1.2]:
            t1=t*scale
            signs=np.array([derivatives(a,t1,x)[1] for x in np.linspace(.025,1.6,150)])
            changes=sum((signs[:-1]*signs[1:])<0)
            assert changes == (1 if scale<1 else 0),(a,t1,changes)
    # Nonzero modes approaching the critical point have x_*^2/(tc-t) -> 3.
    a=.5
    t0=critical_variance(a)
    ratios=[]
    for gap in [1e-2,3e-3,1e-3,3e-4]:
        t=t0-gap
        root=brentq(lambda x:derivatives(a,t,x)[1], 1e-5,1.5)
        ratios.append(root**2/gap)
    assert abs(ratios[-1]-3)<.02,ratios
    assert abs(ratios[-1]-3)<abs(ratios[0]-3)
    print('Critical variances:')
    for a,t in zip(A,tc):print(f'a={a:.2f}, t_c={t:.12f}')
    print('Near-critical x_*^2/(t_c-t):',*[f'{r:.9f}' for r in ratios])
    print('PASS: five critical curvatures, five quartic signs, ten off-critical signs,')
    print('ten numerical mode-count scans, four near-critical peak-position tests.')

if __name__=='__main__':run()
