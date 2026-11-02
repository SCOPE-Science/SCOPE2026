"""Numerical checks of derivative-order asymptotics for a truncated Bergman trace.
Finite quadrature verifies representative coefficients, not infinite conclusions.
Requires only Python's standard library.
"""
from math import sqrt, exp, lgamma, log, pi, erfc, fsum, gamma

def height(a):
    assert 0 < a < 1
    if a < .25:
        return a
    if a > .75:
        return 1-a
    return sqrt(.125-(a-.5)**2)

def derivative_energy(n, sigma, a, steps=10000):
    b = height(a)
    dx = .5/steps
    def density(x,t):
        den = (x-t)**2+b*b
        if x == 0:
            return 0.
        ratio = x*x/(2*den)
        return x * den**(-sigma) * ratio**n
    pieces=[]
    for t in (a,1-a):
        z = fsum(((1 if j == 0 or j == steps else 4 if j % 2 else 2)*density(j*dx,t)
                  for j in range(steps+1)))*dx/3
        pieces.append(z)
    logpref=n*log(4)+2*lgamma(n+sigma)-2*lgamma(sigma)-lgamma(2*n+2)
    return exp(logpref)*sum(pieces)

def constant(sigma,a):
    if .25 < a < .75:
        c=sqrt(pi)*8**sigma/(4*gamma(sigma)**2)*(1/(16*a-4)+1/(12-16*a))
        e=3.5-2*sigma
    elif a == .25 or a == .75:
        c=pi*8**sigma/(16*gamma(sigma)**2)
        e=3-2*sigma
    else:
        t=min(a,1-a)
        c=pi*2**(1-sigma)*t**(2-2*sigma)/gamma(sigma)**2
        e=3-2*sigma
    return c,e

def moving_constant(sigma, eta):
    return pi*8**sigma/(16*gamma(sigma)**2)*exp(16*max(eta,0)**2)*erfc(4*eta)

def main():
    sigma=1.15
    n=1500
    for a in (.12,.25,.5,.75,.88):
        c,e=constant(sigma,a)
        ratio=derivative_energy(n,sigma,a)*n**e/c
        assert abs(ratio-1) < .045,(a,ratio)
    n=1600
    for eta in (-1.,0.,1.):
        a=.25+eta/sqrt(n)
        ratio=derivative_energy(n,1.1,a)*n**.8/moving_constant(1.1,eta)
        assert abs(ratio-1)<.065,(eta,ratio)
    print('CHECK_OK: five fixed-boundary asymptotics and three junction crossover profiles; finite quadrature only')

if __name__=='__main__':
    main()
