"""Self-contained numerical and rational checks of a two-matrix joint-diagonalization result.

Runs with Python >=3.9 and the standard library. All finite checks are corroboration,
not proofs of the general probability asymptotics.
"""
from fractions import Fraction as F
from math import atan2, sin, cos, pi, asin, sqrt, log, isclose
import random


def offdiag_energy(d, x, a, b):
    """Exact squared Frobenius off-diagonal energy in an eigenbasis of [[a,b],[b,-a]]."""
    return 2*(d*d+x*x) - 2*(d*a+x*b)**2/(a*a+b*b)


def one_loss(eps, u, v):
    a, b = u, eps*v
    return offdiag_energy(F(1), F(0), a, b) + offdiag_energy(F(0), eps, a, b)


def direct_loss(eps, u, v):
    a, b = float(u), float(eps*v)
    theta = 0.5*atan2(b, a)
    s, c = sin(theta), cos(theta)
    # Columns of R(theta) are eigenvectors of a*D+b*X.
    # Offdiagonal entry after rotation of d*D+x*X is x*cos(2theta)-d*sin(2theta).
    return 2*((-sin(2*theta))**2 + (float(eps)*cos(2*theta))**2)


def tail(eps, z):
    if z <= 1: return 1.0
    if z >= 1/eps: return 0.0
    y = (1/z**2-eps**2)/(1-eps**2)
    return 2/pi*asin(sqrt(max(0.0, min(1.0, y))))


def angular_moment(eps, trials, power, n=180000):
    # Quantile quadrature avoids Monte Carlo noise and remains independent of the proof.
    # For one trial the angle to the closest multiple of pi is uniform on [0,pi/2].
    # For the minimum of L trials, the CDF of that angle is 1-(1-2*theta/pi)^L.
    # Integrate over the uniform probability-coordinate u of its quantile.
    out = 0.0
    for i in range(n):
        u = (i+0.5)/n
        # Quantile of minimum of L uniforms on [0, pi/2].
        theta = (pi/2)*(1-(1-u)**(1/trials))
        z = 1/sqrt(cos(theta)**2+eps**2*sin(theta)**2)
        out += z**power
    return out/n


def log_tail_moment(eps, trials, power, n=160000):
    """Numerically integrate the exact finite-epsilon tail in log coordinates."""
    horizon=log(1/eps)
    delta=horizon/n
    acc=0.0
    for j in range(n):
        s=(j+0.5)*delta
        acc += power*__import__('math').exp(power*s)*tail(eps,__import__('math').exp(s))**trials
    return 1+delta*acc


def run():
    exact = 0
    for eps in (F(1,10), F(1,2), F(2,3), F(3,4)):
        for u in range(-7, 8):
            for v in range(-7, 8):
                if not (u or v): continue
                z = one_loss(eps, F(u), F(v))
                oracle = 2*eps**2*(u*u+v*v)/(u*u+eps**2*v*v)
                assert z == oracle, (eps,u,v,z,oracle)
                assert isclose(float(z),direct_loss(eps,u,v),rel_tol=3e-13,abs_tol=3e-13)
                exact += 1
    rng=random.Random(5355)
    angular = 0
    for eps in (0.05,0.2,0.6,0.9):
        for _ in range(600):
            u,v=rng.gauss(0,1),rng.gauss(0,1)
            z=1/sqrt((u*u+eps*eps*v*v)/(u*u+v*v))
            exact_loss=2*eps*eps*z*z
            assert isclose(exact_loss,direct_loss(eps,u,v),rel_tol=2e-12,abs_tol=2e-12)
            angular += 1
    # Check CDF against deterministic angle-grid frequencies (not statistical simulation).
    cdf=0
    n=120000
    for eps in (0.05,0.2,0.7):
        for z in (1.1,1.4,2.,3.,6.):
            if z>=1/eps:continue
            freq=sum(1 for j in range(n) if 1/sqrt(cos(pi*(j+.5)/n)**2+eps**2*sin(pi*(j+.5)/n)**2)>z)/n
            assert abs(freq-tail(eps,z))<1.3e-5, (eps,z,freq,tail(eps,z))
            cdf+=1
    # Check the exact mean of the squared one-trial loss via angular quadrature.
    for eps in (0.1,0.25,0.5):
        ex=2*eps**2*angular_moment(eps,1,2,n=120000)
        assert abs(ex-2*eps)<2e-6, (eps,ex,2*eps)
    # Compare expected squared best-of-three normalized loss with the limiting constant.
    limit=24*log(2)/pi**2
    eps=0.003
    m3=log_tail_moment(eps,3,2,n=80000)
    assert abs(m3-limit)<0.006, (m3,limit)
    # First-moment two-trial limiting constant = 16 Catalan/pi^2.
    catalan=0.91596559417721901505460351493238411
    mu2=16*catalan/pi**2
    m2=log_tail_moment(eps,2,1,n=80000)
    assert abs(m2-mu2)<0.006, (m2,mu2)
    print('VERIFY_OK exact rational eigenbasis energies:',exact,
          'direct Gaussian trials:',angular,
          'angular CDF checks:',cdf,
          'one-trial exact mean checks: 3',
          'two/three-trial asymptotic coefficient checks: 2')

if __name__=='__main__':
    run()
