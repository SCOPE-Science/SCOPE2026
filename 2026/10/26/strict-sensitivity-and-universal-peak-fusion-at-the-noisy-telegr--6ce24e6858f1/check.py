"""Independent quadrature checks for Gaussian-smoothed symmetric Beta modal transitions.

Run: python check.py
"""
import math
import numpy as np
from scipy.special import roots_jacobi, hyp1f1
from scipy.optimize import brentq


def critical(q):
    assert 0 < q < 1
    c = q + .5
    def residual(z):
        return hyp1f1(.5, c, -z) - (z / c) * hyp1f1(1.5, c + 1, -z)
    lo, hi = 1.e-5, 1.
    while residual(hi) > 0:
        hi *= 2
        if hi >= 100: raise AssertionError('Exceeded bracket')
    return 1 / (2 * brentq(residual, lo, hi, xtol=1e-13))


def derivative(q, delta, x, order, n=250):
    nodes, weights = roots_jacobi(n, q - 1, q - 1)
    weights /= weights.sum()
    z = x - nodes
    expo = np.exp(-z*z/(2*delta)) / np.sqrt(2*np.pi*delta)
    if order == 1: pol = -z / delta
    elif order == 2: pol = (z*z-delta)/delta**2
    elif order == 4: pol = (z**4-6*delta*z*z+3*delta**2)/delta**4
    else: raise ValueError(order)
    return float(np.dot(weights, pol*expo))


def positive_mode(q, delta):
    f = lambda x: derivative(q,delta,x,1)
    assert f(0.02) > 0 and f(2) < 0, (q,delta,f(.02),f(2))
    return brentq(f, 0.02, 2, xtol=1e-13)


def main():
    qs = [.02, .2, .5, .8, .95, .99]
    for q in qs:
        dc=critical(q)
        der_minus = derivative(q, dc*.9, 0, 2)
        der_plus = derivative(q, dc*1.1, 0, 2)
        d_at = derivative(q,dc,0,2)
        fourth=derivative(q,dc,0,4)
        assert der_minus>0 and der_plus<0
        assert abs(d_at) < 1e-8 and fourth < 0, (q,d_at,fourth)
        print(f'q={q:.3f}, delta_c={dc:.12f}, center_curvature={d_at:+.2e}, critical_fourth={fourth:+.7e}')
    q=.5; dc=critical(q)
    for e in [.01,.004,.001,.00025]:
        delta=dc-e
        mode=positive_mode(q,delta)
        ratio=mode/math.sqrt(3*e)
        assert abs(ratio-1)<.15, (e,mode,ratio)
        print(f'pitchfork: epsilon={e:.6f}, mode={mode:.9f}, ratio_to_sqrt3={ratio:.7f}')
    # The rounded asymptotic tests illustrate, rather than certify, convergence.
    for q in [.99,.999,.9999]:
        dc=critical(q); eps=1-q
        print(f'near-uniform q={q}: z={1/(2*dc):.8f}, log_inverse_eps={math.log(1/eps):.8f}')
    print('All independent numerical checks passed.')

if __name__=='__main__': main()

# Independent weighted Gauss-Jacobi and special function checks above.
# Boundary-logarithm sensitivity uses endpoint-adapted quadrature.
def critical_sensitivity(q):
    from scipy.integrate import quad
    d=critical(q); z=1/(2*d)
    def I(n, logarithm=False):
        return quad(lambda t:t**n*np.exp(-z*t),0,1,
                    weight='alg-logb' if logarithm else 'alg',
                    wvar=(-.5,q-1),epsabs=2e-11,epsrel=2e-11)[0]
    norm=I(0); mu=I(1)/norm
    var=I(2)/norm-mu**2
    cov=(I(1,True)-mu*I(0,True))/norm
    return cov/(1-2*z*z*var)

for q in [.1,.25,.5,.75,.9]:
    exact=critical_sensitivity(q)
    fd=(critical(q+1e-4)-critical(q-1e-4))/(2e-4)
    assert exact<0 and abs(fd-exact)<3e-5,(q,exact,fd)
    print('sensitivity q=',q,'formula',exact,'finite_difference',fd)
