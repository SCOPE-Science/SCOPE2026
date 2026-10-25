"""Deterministic checks for a one-mode stochastic phase-splitting mass theorem.

Python 3 standard library only. Run: python mass_variance_verify.py
The numerical integration checks finite Gaussian integrals; the proof of the
continuum claims is analytical and is given separately.
"""
import math
import cmath


def exact(theta, beta):
    return 6 + 2 * (cmath.exp(2j*theta) * (1 - 4j*beta)**(-1.5)).real


def envelope(beta):
    a = 2 * (1 + 16*beta*beta)**(-0.75)
    return 6-a, 6+a


def phase_min(beta):
    return math.pi/2 - 0.75*math.atan(4*beta)


def integral(theta, beta, n=40000, bound=9.0):
    # Simpson quadrature for E[G^2 cos^2(theta+beta G^2)]
    assert n % 2 == 0
    dx = 2*bound/n
    ss = 0.0
    for i in range(n+1):
        z = -bound + i*dx
        pdf = math.exp(-z*z/2) / math.sqrt(2*math.pi)
        value = z*z * math.cos(theta+beta*z*z)**2 * pdf
        ss += (1 if i==0 or i==n else (4 if i%2 else 2))*value
    return 4+4*ss*dx/3


def run():
    checks = 0
    betas = (0.0, 0.05, 0.15, 0.5, 0.7694208842938133, 1.0, 2.0, 4.0)
    for beta in betas:
        lo, hi = envelope(beta)
        for theta in (0.0, 0.13, math.pi/6, math.pi/4, math.pi/2, phase_min(beta), phase_min(beta)-math.pi/2):
            val = exact(theta, beta)
            numerical = integral(theta, beta)
            assert abs(val-numerical) < 2e-9, (theta, beta, val, numerical)
            assert lo-1e-12 <= val <= hi+1e-12
            checks += 2
        assert abs(exact(phase_min(beta), beta)-lo) < 1e-12
        assert abs(exact(phase_min(beta)-math.pi/2,beta)-hi) < 1e-12
        checks += 2
    beta_star=math.tan(2*math.pi/5)/4
    minimum=6-2*math.cos(2*math.pi/5)**2.5
    assert abs(exact(0,beta_star)-minimum) < 2e-14
    checks+=1
    for k in range(1,501):
        b=k/180
        assert exact(0,b) >= minimum - 1e-12
        if b < beta_star-0.02:
            assert exact(0,b+1e-4) < exact(0,b)
        if b > beta_star+0.02:
            assert exact(0,b+1e-4) > exact(0,b)
        checks+=1
    assert exact(math.pi/2,0) == 4
    assert exact(0,0) == 8
    assert abs(minimum-5.893833889735546) < 1e-12
    assert abs(beta_star-0.7694208842938133) < 1e-13
    checks+=4
    print('PASS:',checks,'deterministic checks. beta*=',beta_star,'zero-phase minimum=',minimum)

if __name__=='__main__':
    run()
