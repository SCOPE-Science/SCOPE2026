"""Numerical reproducibility checks for the rotated-saddle Floquet classification.
Only finite numerical examples are checked here; global statements are proved analytically.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq


def exact_radius(a, p, theta, T, imbalance):
    c2 = math.cos(theta)**2
    S = c2*math.cosh(p*T) + (1-c2)*math.cosh(p*imbalance)
    return math.exp(-a*T + math.acosh(S))


def direct_radius(a, p, theta, T, imbalance):
    H = np.diag([1., -1.])
    C, S = math.cos(theta), math.sin(theta)
    R = np.array([[C, -S], [S, C]])
    A1 = -a*np.eye(2) + p*H
    A2 = -a*np.eye(2) + p*R@H@R.T
    u, v = (T+imbalance)/2, (T-imbalance)/2
    assert u > 0 and v > 0
    return max(abs(np.linalg.eigvals(expm(v*A2) @ expm(u*A1))))


def balanced_cutoff(a, p, theta):
    c = math.cos(theta)
    assert 0 < c < a/p
    def f(T):
        return c*math.sinh(p*T/2)-math.sinh(a*T/2)
    hi = 0.1
    while f(hi) <= 0:
        hi *= 1.5
    return brentq(f, 1.e-8, hi, xtol=1.e-13)


def check():
    tests = 0
    for a, p in [(1., 2.), (0.23, 0.97), (2., 2.7)]:
        for theta in [0., .1, .4, 0.91, 1.1, 1.35, math.pi/2]:
            for T in [0.12, .3, 1.0, 2.4, 3.4]:
                for beta in [-.8,-.25,0,.4,.8]:
                    d = beta*T
                    exact = exact_radius(a, p, theta, T, d)
                    direct = direct_radius(a, p, theta, T, d)
                    assert abs(exact-direct) <= 2.e-9*max(1.,direct), (a,p,theta,T,d,exact,direct)
                    tests+=1
    a,p=1.,2.
    theta=math.acos(1./3.)
    root=balanced_cutoff(a,p,theta)
    expected=2*math.acosh(1.5)
    assert abs(root-expected)<1e-12, (root,expected)
    assert exact_radius(a,p,theta,.5*root,0.)<1
    assert exact_radius(a,p,theta,1.5*root,0.)>1
    T=.5*root
    c2=1/9
    R=(math.cosh(a*T)-c2*math.cosh(p*T))/(1-c2)
    d0=math.acosh(R)/p
    assert 0<d0<T
    assert exact_radius(a,p,theta,T,.9*d0)<1
    assert exact_radius(a,p,theta,T,1.1*d0)>1
    for T in [.5,1,3,10]:
        assert exact_radius(1.,2.,math.pi/2,T,.4*T)<1
        assert abs(exact_radius(1.,2.,math.pi/2,T,.5*T)-1)<1.e-10
        assert exact_radius(1.,2.,math.pi/2,T,.6*T)>1
    for c in [.06,.02,.008]:
        tstar=balanced_cutoff(a,p,math.acos(c))
        asym=2/(p-a)*math.log(1/c)
        assert abs(tstar-asym)<0.5
    # Fixed-duty threshold has one crossing, unlike multiple Floquet tongues.
    theta=1.4
    beta=.3
    assert p*math.sqrt(math.cos(theta)**2+math.sin(theta)**2*beta**2)<a
    z=lambda T: exact_radius(a,p,theta,T,beta*T)-1
    root=brentq(z,.001,20)
    assert all(z(t)<0 for t in [.01,.2,.8*root])
    assert all(z(t)>0 for t in [1.1*root,2*root,3*root])
    # Fractional duty-tolerance shrinks continuously to zero with the period.
    c2 = math.cos(theta)**2  # theta at the fixed-duty test above; reset below.
    theta = math.acos(1./3.)
    Tcut = balanced_cutoff(a,p,theta)
    c2 = math.cos(theta)**2
    def B(t):
        return (math.cosh(a*t)-c2*math.cosh(p*t))/(1-c2)
    def frac(t):
        return math.acosh(B(t))/(p*t)
    vals = [frac(t) for t in [.025, .2, .55, 1., .9*Tcut]]
    assert all(v1>v2 for v1,v2 in zip(vals,vals[1:])), vals
    Bprime = (a*math.sinh(a*Tcut)-p*c2*math.sinh(p*Tcut))/(1-c2)
    assert Bprime < 0
    C = math.sqrt(-2*Bprime)/p
    for h in [.01,.001,.0001]:
        d = math.acosh(B(Tcut-h))/p
        assert abs(d/(C*math.sqrt(h))-1) < .03
    print(f'PASS: {tests} direct 2x2 monodromy comparisons; exact cutoff T*={expected:.12f}; overlap of stable/unstable duty bounds; orthogonal edge; asymptotic and fixed-duty crossing')

if __name__=='__main__':
    check()
