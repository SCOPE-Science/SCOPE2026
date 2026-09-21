#!/usr/bin/env python3
import mpmath as mp

mp.mp.dps = 60

def coeffs(beta, N):
    a = (1-beta)/(N-beta)
    A = 1-N*a
    B = -N*(N-1)*a
    c = -B/(3*A)
    return a, A, B, c

def H(z, beta, N):
    a = (1-beta)/(N-beta)
    return z-a*z**N-z**2/2+(N*a/(N+1))*z**(N+1)

def starlike_real(z, beta, N):
    a = (1-beta)/(N-beta)
    return mp.re((1-N*a*z**(N-1))/(1-a*z**(N-1)))

samples = [(mp.mpf('0.5'),2), (mp.mpf('0.9'),14), (mp.mpf('0.99'),149)]
for beta,N in samples:
    a,A,B,c = coeffs(beta,N)
    assert A > 0 and c > mp.mpf('0.5')
    # Check the exact algebraic identity at representative interior points.
    for rho in [mp.mpf('0.2'), mp.mpf('0.7'), mp.mpf('0.99')]:
        for theta in [mp.mpf('0'), mp.mpf('0.7'), mp.mpf('2.1')]:
            z = rho*mp.e**(1j*theta)
            assert starlike_real(z,beta,N) > beta
    # Locate the nonreal local level branch Im(H)=0 near z=1.
    y = mp.mpf('1e-4')
    F = lambda x: mp.im(H(1-(x+1j*y), beta, N))
    x0 = c*y*y
    x = mp.findroot(F, (mp.mpf('0.8')*x0, mp.mpf('1.2')*x0))
    margin = 2*x-x*x-y*y
    assert margin > 0
    assert abs(F(x)) < mp.mpf('1e-45')
    print('beta=', beta, 'N=', N, 'a=', mp.nstr(a,16),
          'c=', mp.nstr(c,16), 'x/y^2=', mp.nstr(x/y**2,16),
          'disk_margin=', mp.nstr(margin,12))
print('all checks passed')
