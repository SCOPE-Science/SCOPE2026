#!/usr/bin/env python3
import mpmath as mp

mp.mp.dps = 45

def fugacity(alpha, r, eta):
    q = 1 - (1-r)*eta/r
    assert 0 < q < 1
    target = q * mp.zeta(alpha)
    lo, hi = mp.mpf('0'), mp.mpf('1')
    for _ in range(100):
        mid = (lo+hi)/2
        if mp.polylog(alpha, mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

def rate(alpha, r, eta):
    z = fugacity(alpha, r, eta)
    return (r/mp.zeta(alpha))*(mp.zeta(alpha+1)-mp.polylog(alpha+1,z)) + (r-(1-r)*eta)*mp.log(z)

def source_phi(alpha, r, eta, z):
    return (r/mp.zeta(alpha))*(mp.polylog(alpha+1,z)-mp.zeta(alpha+1)) - (r-(1-r)*eta)*mp.log(z)

def jprime(alpha, r, eta):
    z=fugacity(alpha,r,eta)
    return -(1-r)*mp.log(z)

def jsecond(alpha, r, eta):
    z=fugacity(alpha,r,eta)
    return (1-r)**2*mp.zeta(alpha)/(r*mp.polylog(alpha-1,z))

def relerr(a,b):
    return abs(a-b)/max(mp.mpf('1e-60'),abs(b))

r=mp.mpf(2)/5
for alpha in (mp.mpf('1.5'),mp.mpf('2'),mp.mpf('3')):
    emax=r/(1-r)
    eta=emax/5
    z=fugacity(alpha,r,eta)
    q=1-(1-r)*eta/r
    assert relerr(mp.polylog(alpha,z), q*mp.zeta(alpha)) < mp.mpf('1e-25')
    J=rate(alpha,r,eta)
    assert J > 0
    assert abs(J + source_phi(alpha,r,eta,z)) < mp.mpf('1e-25')
    h=mp.mpf('2e-6')
    d1=(rate(alpha,r,eta+h)-rate(alpha,r,eta-h))/(2*h)
    d2=(rate(alpha,r,eta+h)-2*rate(alpha,r,eta)+rate(alpha,r,eta-h))/(h*h)
    assert relerr(d1,jprime(alpha,r,eta)) < mp.mpf('5e-8')
    assert relerr(d2,jsecond(alpha,r,eta)) < mp.mpf('2e-7')
    assert jsecond(alpha,r,eta) > 0
    endpoint=r*mp.zeta(alpha+1)/mp.zeta(alpha)
    near=rate(alpha,r,emax-mp.mpf('1e-12'))
    assert abs(near-endpoint) < mp.mpf('2e-10')

# Small-eta asymptotic ratios. Values are chosen small enough for the asymptotic
# regime while retaining stable numerical inversion.
alpha=mp.mpf('1.5')
A=-mp.gamma(1-alpha)
C=(alpha-1)/alpha*(1-r)*(mp.zeta(alpha)*(1-r)/(r*A))**(1/(alpha-1))
eta=mp.mpf('1e-4')
ratio=rate(alpha,r,eta)/(C*eta**(alpha/(alpha-1)))
assert abs(ratio-1) < mp.mpf('0.002')

alpha=mp.mpf('2')
C=(1-r)**2*mp.zeta(2)/(2*r)
eta=mp.mpf('1e-8')
ratio=rate(alpha,r,eta)/(C*eta**2/abs(mp.log(eta)))
assert abs(ratio-1) < mp.mpf('0.20')

alpha=mp.mpf('3')
C=(1-r)**2*mp.zeta(alpha)/(2*r*mp.zeta(alpha-1))
eta=mp.mpf('1e-5')
ratio=rate(alpha,r,eta)/(C*eta**2)
assert abs(ratio-1) < mp.mpf('5e-5')

print('VERIFY_OK')
