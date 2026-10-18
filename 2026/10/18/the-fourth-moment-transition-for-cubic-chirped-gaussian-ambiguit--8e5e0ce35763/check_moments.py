#!/usr/bin/env python3
"""Independent numerical checks of cubic-phase Gaussian ambiguity identities."""
import mpmath as mp
mp.mp.dps = 48


def ambiguity_direct(lam, tau, nu):
    root2 = mp.sqrt(2)
    def f(x):
        return 2**mp.mpf('0.25') * mp.exp(-mp.pi*x*x + 1j*lam*x**3)
    return mp.quad(lambda t: f(t+tau/2)*mp.conj(f(t-tau/2))*mp.exp(-2j*mp.pi*nu*t), [-mp.inf, 0, mp.inf])


def ambiguity_formula(lam, tau, nu):
    c=3*lam/(2*mp.pi)
    z=1-1j*c*tau
    return mp.exp(-mp.pi*tau*tau/2 + 1j*lam*tau**3/4) / mp.sqrt(z) * mp.exp(-mp.pi*nu*nu/(2*z))


def moment_integral(p,c):
    p=mp.mpf(p); c=mp.mpf(c)
    f=lambda x: mp.exp(-p*mp.pi*x*x/2)*(1+c*c*x*x)**((2-p)/4)
    return mp.sqrt(2/p)*2*mp.quad(f,[0,1,mp.inf])


def moment_hyperu(p,c):
    p=mp.mpf(p); c=abs(mp.mpf(c))
    if c==0: return 2/p
    return mp.sqrt(2*mp.pi/p)/c*mp.hyperu(mp.mpf('0.5'),2-p/4,p*mp.pi/(2*c*c))


def asymptotic(p,c):
    p=mp.mpf(p);c=mp.mpf(c)
    if p<4: return mp.sqrt(2/p)*(p*mp.pi/2)**(p/4-1)*mp.gamma(1-p/4)*c**(1-p/2)
    if p>4: return mp.sqrt(2*mp.pi/p)*mp.gamma(p/4-1)/mp.gamma(p/4-mp.mpf('0.5'))/c
    return (2*mp.log(c)+mp.log(2/mp.pi)-mp.euler)/(mp.sqrt(2)*c)

for lam,tau,nu in [(-1,mp.mpf('.25'),mp.mpf('.3')),(mp.mpf('.35'),mp.mpf('.7'),mp.mpf('1.2')),(1,mp.mpf('1.1'),mp.mpf('-.6')),(0,1,1)]:
    a=ambiguity_direct(lam,tau,nu); b=ambiguity_formula(lam,tau,nu)
    assert abs(a-b)<mp.mpf('1e-35'),(lam,tau,nu,a,b)
print('4 defining ambiguity integrals: PASS')

for p in [1,2,3,4,5,6,8]:
    for c in [mp.mpf('.5'),3,100]:
        a=moment_integral(p,c); b=moment_hyperu(p,c)
        assert abs(a-b)<mp.mpf('1e-35')
    x=moment_integral(p,100);y=asymptotic(p,100)
    print('p',p,'M_p(100)',mp.nstr(x,13),'asymptotic_ratio',mp.nstr(x/y,11))
for c in [0,mp.mpf('.1'),1,10]:
    assert abs(moment_integral(2,c)-1)<mp.mpf('1e-35')
    if c:
        b=mp.exp(mp.pi/c**2)*mp.besselk(0,mp.pi/c**2)/(mp.sqrt(2)*c)
        assert abs(moment_integral(4,c)-b)<mp.mpf('1e-35')
print('Moyal, Hypergeometric U, Bessel K0 identities: PASS')
print('Asymptotic regimes are numerically consistent (not a proof).')
