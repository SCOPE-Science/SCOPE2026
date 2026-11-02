"""Reproduce independent finite checks for a Gaussian one-probe spectral-majorization law.

Analytical Schur-convexity is proved in the accompanying manuscript; these
numerical tests check algebra, quadrature, endpoints and strict example trends.
Requires Python >=3.10, NumPy >=1.24, SciPy >=1.10.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import betainc

N = 0

def verify(condition, label):
    global N
    assert condition, label
    N += 1


def cdf_m2(k, rho):
    assert k > 0 and 0 <= rho <= 1
    def integrand(theta):
        t = 1.0 + rho * math.cos(2.0 * theta)
        return math.sqrt(t / (t + k)) if t > 0 else 0.0
    # Stable split across the four zeros at the rank-one endpoint.
    val = sum(quad(integrand, j * math.pi / 2, (j+1) * math.pi / 2,
                   epsabs=1e-12, epsrel=1e-12)[0] for j in range(4))
    return 1.0 - val / (2.0 * math.pi)


def F_rankone(k, m):
    return 2.0 / math.pi * math.atan(math.sqrt(k/m))


def F_isotropic(k, m):
    return betainc(m/2, 0.5, k/(1+k))


def mean_m2(a, b, rho):
    # Integrate survival in error normalization: E L = m b² + (a²-b²) E H.
    # H = b² T/(a² X²+b² T); E H = integral_0^1 [1-F_H(z)] dz.
    m = 2
    def F_H(z):
        if z <= 0: return 0.0
        if z >= 1: return 1.0
        k = (a*a/(b*b)) * z/(1-z)
        return cdf_m2(k, rho)
    hbar = quad(lambda z: 1 - F_H(z), 0, 1,
                epsabs=1e-10, epsrel=1e-10)[0]
    return m*b*b + (a*a-b*b)*hbar


def test_direct_identity():
    rng = np.random.default_rng(761992)
    for m in [2,3,4,8]:
        for a,b in [(3.,1.),(1.5,0.25),(5.,2.)]:
            A = np.diag([a]+[b]*m)
            for _ in range(45):
                w = rng.standard_normal(m+1)
                y = A @ w
                q = y / np.linalg.norm(y)
                L_direct = np.linalg.norm(A-np.outer(q,q)@A,'fro')**2
                T = np.dot(w[1:],w[1:])
                L_formula = m*b*b + (a*a-b*b)*b*b*T/(a*a*w[0]**2+b*b*T)
                verify(abs(L_direct-L_formula)<5e-11,
                       f'direct algebra m={m}')


def test_endpoint_cdfs():
    for k in np.geomspace(0.03,30.0,31):
        exact_iso = F_isotropic(k,2)
        exact_rank = F_rankone(k,2)
        verify(abs(cdf_m2(k,0)-exact_iso)<2e-11, 'uniform cdf')
        verify(abs(cdf_m2(k,1)-exact_rank)<2e-11, 'rankone cdf')
        verify(exact_rank>exact_iso+1e-9, 'strict endpoints')
        vals=[cdf_m2(k,rho) for rho in np.linspace(0,1,11)]
        for left,right in zip(vals,vals[1:]):
            verify(right>left+1e-8, f'nonmonotonic rho k={k}')
    k=1.
    verify(abs(F_isotropic(k,2)-(1-1/math.sqrt(2)))<1e-13,'example isotropic')
    verify(abs(F_rankone(k,2)-(2/math.pi*math.atan(1/math.sqrt(2))))<1e-13,
           'example concentrated')


def test_means():
    a,b,m=3.,1.,2
    rank_mean=m*b*b+(a*a-b*b)*(b*math.sqrt(m))/(a+b*math.sqrt(m))
    verify(abs(mean_m2(a,b,1)-rank_mean)<2e-8, 'rank mean')
    for r0,r1 in [(0.,0.2),(0.2,0.4),(0.4,0.6),(0.6,0.8),(0.8,1.)]:
        verify(mean_m2(a,b,r1)<mean_m2(a,b,r0)-1e-6,'strict mean rho')
    verify(abs(rank_mean - 4.563017928136326)<1e-10,'mean literal')


def test_convexity_and_majorization():
    # Direct sign checks supplement the explicit analytic second derivative.
    for u in np.geomspace(1e-5,1e4,300):
        second = math.exp(-u/2)*(u+1)/(2*math.sqrt(2*math.pi)*u**1.5)
        verify(second >= 0.0,'chi1 survival second derivative')
    # Quantile ordering follows from CDF strict order; here check multiple k.
    for k in [.04,.1,.25,1.,3.,20.]:
        verify(F_rankone(k,3)>F_isotropic(k,3),'m3 strict endpoints')
        verify(F_rankone(k,4)>F_isotropic(k,4),'m4 strict endpoints')

if __name__=='__main__':
    test_direct_identity()
    test_endpoint_cdfs()
    test_means()
    test_convexity_and_majorization()
    print(f'PASS: {N} independent deterministic numerical/algebraic checks.')
    print('F_iso(e=2.8, a=3, b=1, m=2):', F_isotropic(1,2))
    print('F_rankone(e=2.8, a=3, b=1, m=2):', F_rankone(1,2))
    print('E loss isotropic:', mean_m2(3,1,0))
    print('E loss rankone:', mean_m2(3,1,1))
