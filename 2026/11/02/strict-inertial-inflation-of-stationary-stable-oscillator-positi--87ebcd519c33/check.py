#!/usr/bin/env python3
"""Reproduce numerical identities for a symmetric-stable linear oscillator.

Requires Python 3 standard library only. These finite checks do not replace
proof of the all-parameter monotonicity or asymptotic theorem.
"""
import math

checks = 0


def check(condition, message):
    global checks
    assert condition, message
    checks += 1


def close(x, y, rtol=1e-9, atol=1e-12):
    return abs(x-y) <= atol + rtol*max(abs(x), abs(y))


def psi(x):
    """Digamma via recurrence and asymptotic Bernoulli expansion."""
    s = 0.0
    while x < 64.0:
        s -= 1.0/x
        x += 1.0
    z = 1.0/x
    return s + math.log(x)-z/2-z*z/12+z**4/120-z**6/252+z**8/240


def scaled_integral(alpha, gamma, kappa, mass):
    delta = math.sqrt(gamma*gamma-4*kappa*mass)
    a = alpha*(gamma-delta)/(2*delta)
    return math.exp((1-alpha)*math.log(gamma)-math.log(kappa)
        +math.lgamma(alpha+1)-(alpha+1)*math.log(alpha)
        +(alpha-1)*math.log(2*a+alpha)
        +math.lgamma(a+1)-math.lgamma(a+alpha))


def beta_integral(alpha, gamma, kappa, mass):
    delta = math.sqrt(gamma*gamma-4*kappa*mass)
    a = alpha*(gamma-delta)/(2*delta)
    return math.exp(math.log(mass)-(alpha+1)*math.log(delta)
        +math.lgamma(a)+math.lgamma(alpha+1)-math.lgamma(a+alpha+1))


def direct_integral(alpha, gamma, kappa, mass):
    delta = math.sqrt(gamma*gamma-4*kappa*mass)
    rs = (-gamma+delta)/(2*mass)
    gap = delta/mass
    # Simpson integration under t = xmax*u*u, u in [0,1].
    # Quadratic time mapping resolves the narrow initial impulse layer.
    xmax = min(200., max(30., 60./abs(rs)))
    n = 48000
    h = 1./n
    total = 0.0
    for j in range(n+1):
        u=j*h
        t=xmax*u*u
        g=math.exp(rs*t)*(-math.expm1(-gap*t))/delta
        f=(g**alpha)*(2*xmax*u)
        total += (1 if j==0 or j==n else 4 if j%2 else 2)*f
    return total*h/3


def I0(alpha, gamma, kappa):
    return gamma**(1-alpha)/(alpha*kappa)


def Ic(alpha, gamma, kappa):
    return gamma**(1-alpha)*2**(alpha-1)*math.gamma(alpha+1)/(kappa*alpha**(alpha+1))


def R(alpha):
    euler_gamma=0.5772156649015328606065120900824
    return 2*alpha-1-alpha*(psi(alpha+1)+euler_gamma)


for alpha in [1.1, 1.25, 1.5, 1.75, 1.9]:
    for gamma,kappa in [(1.,1.),(2.,3.),(3.,0.5)]:
        mcrit=gamma*gamma/(4*kappa)
        vals=[]
        for frac in [0.01,0.1,0.3,0.6,0.9,0.99]:
            mass=mcrit*frac
            ib=beta_integral(alpha,gamma,kappa,mass)
            ig=scaled_integral(alpha,gamma,kappa,mass)
            check(close(ib,ig,rtol=2e-11), 'beta and gamma ratio mismatch')
            vals.append(ig)
            if frac in [0.1,0.6]:
                idirect=direct_integral(alpha,gamma,kappa,mass)
                check(close(ib,idirect,rtol=3e-7), f'integral numerical mismatch alpha={alpha} gamma={gamma} kappa={kappa} frac={frac}: {ib} vs {idirect}')
        check(I0(alpha,gamma,kappa)<vals[0], 'excess versus overdamped')
        check(all(x<y for x,y in zip(vals,vals[1:])), 'strict mass monotonicity')
        check(vals[-1]<Ic(alpha,gamma,kappa), 'critical limit')
    check(R(alpha)>0.,'small-m coefficient positivity')
    alpha0=alpha
    gamma0=2.
    kappa0=3.
    mcrit=gamma0*gamma0/(4*kappa0)
    for delta in [1e-4,3e-5,1e-5]:
        mass=mcrit*delta
        approx=(scaled_integral(alpha0,gamma0,kappa0,mass)/I0(alpha0,gamma0,kappa0)-1) / (mass*kappa0/gamma0**2)
        check(close(approx,R(alpha0),rtol=7e-4,atol=1e-6),'first-order expansion')
# Gaussian boundary: mass-independent exponent integral
for gamma,kappa in [(1.,1.),(2.,3.),(5.,2.)]:
    i0=I0(2.,gamma,kappa)
    for frac in [0.01,0.25,0.6,0.95]:
        mass=frac*gamma*gamma/(4*kappa)
        check(close(scaled_integral(2.,gamma,kappa,mass),i0,rtol=1e-12),
              'Gaussian boundary nonconstancy')

print('PASS:', checks, 'checks. All-parameter conclusions use the written proof.')
