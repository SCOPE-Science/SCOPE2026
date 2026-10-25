"""Reproduce finite-step and analytic diagnostics for the aging--Konno law.

Requires numpy and scipy; run `python verify_aging_konno.py`.
The analytic limit theorem uses renewal and Fourier arguments, not these checks.
"""
import math
import numpy as np
from scipy import integrate, special


def params(ell):
    assert ell > 0
    return math.sqrt(ell / (ell + 2)), math.sqrt(2 / (ell + 2))


def konno(v, ell):
    a, b = params(ell)
    if abs(v) >= a:
        return 0.0
    return b / (math.pi * (1 - v * v) * math.sqrt(a * a - v * v))


def limit_density(x, alpha, ell):
    assert 0 < alpha < 1
    a, b = params(ell)
    x = abs(x)
    if not 0 < x < a:
        return 0.0
    h = 1 - x / a
    factor = math.sin(math.pi * alpha) * b / (math.pi**2 * a) * h ** (alpha - 0.5)

    def smooth(t):
        u = 1 - h * t
        return factor * u ** (2 - alpha) / ((u*u - x*x) * math.sqrt(2 - h*(1+t)))

    return integrate.quad(smooth, 0, 1, weight='alg',
                          wvar=(alpha-1, -0.5),
                          epsabs=1e-10, epsrel=1e-9, limit=180)[0]


def central_coefficient(alpha, ell):
    a, b = params(ell)
    return (math.sin(math.pi*alpha)*b*a**(alpha-1) /
            (2 * math.pi**2) * special.beta(alpha/2, .5) *
            special.hyp2f1(1, alpha/2, (alpha+1)/2, a*a))


def front_coefficient(alpha, ell):
    a, b = params(ell)
    return (math.sin(math.pi*alpha) * special.beta(alpha,.5) /
            (math.pi**2 * b * math.sqrt(2*a) * a**alpha))


def finite_position_distribution(n, alpha, ell):
    """Exact finite-time renewal mixture of directly propagated coin amplitudes."""
    s = 1+alpha
    normalizer = special.zeta(s)
    steps = np.arange(1, n+1, dtype=float)
    p = steps**(-s)/normalizer
    surv = np.array([special.zeta(s, a+1)/normalizer for a in range(n+1)])
    renew = np.zeros(n+1)
    renew[0] = 1.0
    for k in range(1, n+1):
        renew[k] = np.dot(renew[:k][::-1],p[:k])
    ages = renew[::-1] * surv
    assert abs(ages.sum()-1) < 1e-10
    root = math.sqrt(ell)
    coin = np.array([[-ell, 2*root, 2],
                     [2*root, ell-2, 2*root],
                     [2, 2*root, -ell]], dtype=float)/(ell+2)
    dark = np.array([root,-2,root])/math.sqrt(2*(ell+2))
    psi = np.zeros((3,2*n+1),dtype=np.complex128)
    psi[:,n] = dark
    distribution = np.zeros(2*n+1)
    for age in range(n+1):
        distribution += ages[age]*np.sum(np.abs(psi)**2,axis=0)
        if age<n:
            evolved = coin@psi
            psi[0,:-1] = evolved[0,1:]
            psi[0,-1] = 0
            psi[1,:] = evolved[1,:]
            psi[2,1:] = evolved[2,:-1]
            psi[2,0] = 0
    return distribution


def run():
    count=0
    for alpha in (0.3, 0.5, 0.7):
        ell=2.0
        a,_ = params(ell)
        for dx in (1e-3, 1e-4):
            z=limit_density(a-dx,alpha,ell)
            approx=front_coefficient(alpha,ell)*dx**(alpha-0.5)
            assert abs(z/approx-1)<0.006, (alpha,dx,z,approx)
            count+=1
        for x in (1e-3, 1e-4):
            z=limit_density(x,alpha,ell)
            approx=central_coefficient(alpha,ell)*x**(-alpha)
            assert abs(z/approx-1)<0.08, (alpha,x,z,approx)
            count+=1
    ell=2.0
    alpha=.3
    n=650
    dist=finite_position_distribution(n,alpha,ell)
    assert abs(sum(dist)-1) < 1e-10
    count+=1
    positions=np.arange(-n,n+1)/n
    msd=np.dot(positions**2,dist)
    _,b=params(ell)
    prediction=(1-alpha)*(2-alpha)*(1-b)/2
    assert abs(msd/prediction-1)<0.008,(msd,prediction)
    count+=1
    a,_=params(ell)
    for threshold in (.05,.15,.3,.5):
        actual=dist[np.abs(positions) <= threshold+1e-12].sum()
        tail=2*integrate.quad(lambda x:limit_density(x,alpha,ell),threshold,a,
                               epsabs=5e-7,epsrel=1e-6,limit=180)[0]
        expected=1-tail
        assert abs(actual-expected)<0.006, (threshold,actual,expected)
        count+=1
    print('PASS',count,'analytic-edge/center and independent finite-walk comparisons')
    print('finite-n second moment',repr(float(msd)), 'limit',repr(float(prediction)))

if __name__=='__main__':
    run()
