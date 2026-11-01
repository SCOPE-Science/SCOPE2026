"""Independent finite checks for the singular weighted-perimeter rectangle theorem.

Analytic proof is contained in RESULT.md; finite computations do not certify
universal assertions. Usage: python verify.py (requires mpmath).
"""
from __future__ import annotations

import mpmath as mp

mp.mp.dps = 48
checks = 0


def verify(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)


def cost(alpha, t):
    a, q = mp.mpf(alpha), mp.mpf(t)
    return 4 * (
        mp.quad(lambda y: (q*q+y*y)**(-a/2), [0,q,1])
        + mp.quad(lambda x: (1+x*x)**(-a/2), [0,q])
    )


def H(alpha, t):
    a, q = mp.mpf(alpha), mp.mpf(t)
    cos_theta = q/mp.sqrt(1+q*q)
    integral=mp.betainc(mp.mpf(1)/2,(a+1)/2,0,1/(1+q*q))/2
    return a * cos_theta**(-a) * integral


def deriv_formula(alpha,t):
    a, q = mp.mpf(alpha), mp.mpf(t)
    return 4*(1+q*q)**(-a/2)*(1-H(a,q))


def root(alpha):
    lo = mp.mpf('1e-100')
    hi = mp.mpf(1)
    for i in range(190):
        mid=(lo+hi)/2
        if H(alpha,mid)>1:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def direct_bdry(alpha,t):
    """Arclength integration on all four sides independently of the formula."""
    a, q = mp.mpf(alpha),mp.mpf(t)
    side_x = mp.quad(lambda y:(q*q+y*y)**(-a/2), [-1,0,1])
    side_y = mp.quad(lambda x:(x*x+1)**(-a/2), [-q,0,q])
    return 2*(side_x+side_y)


alphas=['0.1','0.2','0.3','0.5','0.75','0.9','0.99']
roots=[]
for ap in alphas:
    a=mp.mpf(ap)
    t=root(a)
    roots.append(t)
    verify(abs(H(a,t)-1)<mp.mpf('1e-34'), 'stationarity')
    verify(0<t<1,'interior root')
    verify(cost(a,t)<cost(a,1),'square strictly nonoptimal')
    verify(cost(a,t)<4/(1-a),'segment strictly nonoptimal')
    for q in [mp.mpf('0.08'),mp.mpf('0.53'),mp.mpf('0.91')]:
        verify(abs(cost(a,q)-direct_bdry(a,q))<mp.mpf('1e-34'), 'boundary integral')
        dt=mp.mpf('1e-7')
        numerical=(cost(a,q+dt)-cost(a,q-dt))/(2*dt)
        verify(abs(numerical-deriv_formula(a,q))<mp.mpf('1e-10'), 'independent numerical derivative')
        verify(mp.sign(deriv_formula(a,q))==mp.sign(1-H(a,q)), 'derivative sign')
    for q in [t/3,t/2,(1+t)/2,(1+3*t)/4]:
        verify((q<t and deriv_formula(a,q)<0) or (q>t and deriv_formula(a,q)>0), 'root sign')
        verify(cost(a,q)>cost(a,t),'strict global minimum sampled')
    # Homogeneous scaling of the radial perimeter from the side integral.
    for scale in [mp.mpf('0.7'),mp.mpf('2.2')]:
        x=scale*t; y=scale
        arbitrary=4*(mp.quad(lambda v:(x*x+v*v)**(-a/2),[0,y])
                     +mp.quad(lambda u:(u*u+y*y)**(-a/2),[0,x]))
        verify(abs(arbitrary-scale**(1-a)*cost(a,t))<mp.mpf('1e-34'),'scale')
for l,r in zip(roots[:-1],roots[1:]):
    verify(l<r,'critical aspect monotonic in exponent')
for a in [mp.mpf('0.15'),mp.mpf('0.35'),mp.mpf('0.7')]:
    for t in [mp.mpf('0.11'),mp.mpf('0.52'),mp.mpf('0.9')]:
        verify(H(a+mp.mpf('0.00001'),t)>H(a,t),'H monotonic in exponent')
        verify(H(a,t+mp.mpf('0.00001'))<H(a,t),'H antitonic in aspect')
for ap in ['0.2','0.1','0.06','0.04']:
    a=mp.mpf(ap)
    t=root(a)
    asym=mp.mpf('0.5')*(mp.pi*a/2)**(1/a)
    verify(mp.mpf('0.98')<t/asym<mp.mpf('1.1'),'essential singular asymptotic')
k=mp.sqrt(2)*mp.atanh(1/mp.sqrt(2))
for ap in ['0.9','0.99','0.999']:
    a=mp.mpf(ap)
    t=root(a)
    verify(abs((1-t)/(1-a)-k)<mp.mpf('0.03'),'unit exponent boundary asymptotic')
verify(abs(H(1,1)-1)<mp.mpf('1e-48'),'upper endpoint normalization')
verify(abs(H(mp.mpf('0.3'),1))<1,'lower exponent strictness')
print('RECTANGLE_POWER_PERIMETER_FINITE_CHECKS_OK', checks)
print('a=0.5 critical aspect',mp.nstr(root(mp.mpf('0.5')),20))
print('upper-endpoint slope',mp.nstr(k,20))
