#!/usr/bin/env python3
"""Finite-dimensional and special-function checks for the stated covariance limits.

Uses only mpmath.  Finite checks support, but do not replace, the analytical proof.
Run: python verify_stochastic_rate_temporal.py
"""
import mpmath as mp

mp.mp.dps = 45
checks = 0

def close(a,b,rel=mp.mpf('2e-9'),abs_tol=mp.mpf('1e-12')):
    global checks
    checks += 1
    if abs(a-b) > abs_tol+rel*max(abs(a),abs(b)):
        raise AssertionError(f'check {checks}: {mp.nstr(a,18)} vs {mp.nstr(b,18)}')

def gt(a,b):
    global checks
    checks += 1
    if not a>b: raise AssertionError(f'check {checks}: {a} <= {b}')

def g(shape,z):
    return mp.exp(z)*z**(shape-1)*mp.gammainc(1-shape,z,mp.inf)

def h(shape,z):
    return (1-(z+shape-1)*g(shape,z))/z

def renewal_g(p, rates, z):
    return sum((w/(r+z) for w,r in zip(p,rates)),mp.mpf('0'))

def renewal_h(p, rates, z):
    return sum((w/(r+z)**2 for w,r in zip(p,rates)),mp.mpf('0'))

# Matrix generator check independent of renewal transform and survival formula.
for rate1,rate2 in [(mp.mpf('.13'),mp.mpf('1.7')),(mp.mpf('.7'),mp.mpf('6.2'))]:
  for p1 in [mp.mpf('.2'),mp.mpf('.65')]:
    p=mp.matrix([[p1,1-p1]])
    rates=[rate1,rate2]
    ones=mp.matrix([1,1])
    for mu in [mp.mpf('.025'),mp.mpf('.5'),mp.mpf('3.1')]:
      K=mp.matrix([[rate1+mu*(1-p1),-mu*(1-p1)],[-mu*p1,rate2+mu*p1]])
      inv=K**(-1)
      gmu=renewal_g([p1,1-p1],rates,mu)
      hmu=renewal_h([p1,1-p1],rates,mu)
      R=gmu/(1-mu*gmu)
      close((p*inv*ones)[0],R)
      tau=hmu/(gmu*(1-mu*gmu))
      close((p*inv*inv*ones)[0]/(p*inv*ones)[0],tau)
      for t in [mp.mpf('0'),mp.mpf('.3'),mp.mpf('3.2')]:
        S=(p*mp.expm(-K*t)*ones)[0]
        gt(S,mp.mpf('-1e-30'))
        corr=(p*inv*mp.expm(-K*t)*ones)[0]/R
        close(corr,(p*mp.expm(-K*t)*inv*ones)[0]/R)
        if t==0: close(corr,mp.mpf(1))
        gt(corr,mp.mpf('-1e-30'))
        phi=p1*mp.exp(-rate1*t)+(1-p1)*mp.exp(-rate2*t)
        gt(S+mp.mpf('1e-25'),mp.exp(-mu*t)*phi)
        gt(phi+mp.mpf('1e-25'),S)

# Gamma rate laws, check closed Stieltjes transform and derivative.
for a in [mp.mpf('.45'),mp.mpf('1'),mp.mpf('1.5'),mp.mpf('2'),mp.mpf('3.5')]:
 for z in [mp.mpf('.003'),mp.mpf('.04'),mp.mpf('.4')]:
    quadrature=mp.quad(lambda r: (r**(a-1)*mp.exp(-r)/mp.gamma(a))/(r+z),[0,1,mp.inf])
    close(g(a,z),quadrature)
    close(h(a,z),-mp.diff(lambda zz: g(a,zz),z))

# Sharp asymptotic numerical trends at mu=1e-6 or 1e-7.
mu=mp.mpf('1e-7')
for a in [mp.mpf('.4'),mp.mpf('.7')]:
    c=1/mp.gamma(a)
    predicted=c*mp.gamma(a)*mp.gamma(1-a)*mu**(a-1)
    actual=g(a,mu)/(1-mu*g(a,mu))
    close(actual/predicted,1,rel=mp.mpf('.03'))
    tau=h(a,mu)/(g(a,mu)*(1-mu*g(a,mu)))
    close(mu*tau,1-a,rel=mp.mpf('.02'))
for a in [mp.mpf('1.25'),mp.mpf('1.65')]:
    m1=1/(a-1)
    c=1/mp.gamma(a)
    tau=h(a,mu)/(g(a,mu)*(1-mu*g(a,mu)))
    constant=c*mp.gamma(a)*mp.gamma(2-a)/m1
    close(tau*mu**(2-a),constant,rel=mp.mpf('.05'))
for a in [mp.mpf('3'),mp.mpf('4')]:
    tau=h(a,mu)/(g(a,mu)*(1-mu*g(a,mu)))
    close(tau,1/(a-2),rel=mp.mpf('.005'))
for a in [mp.mpf('1'),mp.mpf('2')]:
    tau=h(a,mu)/(g(a,mu)*(1-mu*g(a,mu)))
    if a==1:
       close(tau*mu*mp.log(1/mu),1,rel=mp.mpf('.15'))
    else:
       close(tau/mp.log(1/mu),1,rel=mp.mpf('.15'))

# Exact constant-rate special case: no dependence on environmental refresh rate.
for lam in [mp.mpf('.1'),mp.mpf('2.1')]:
 for mu in [mp.mpf('.01'),mp.mpf('1.2'),mp.mpf('7')]:
    G=1/(lam+mu)
    H=1/(lam+mu)**2
    close(G/(1-mu*G),1/lam)
    close(H/(G*(1-mu*G)),1/lam)

# Numerical Laplace inversion probes for the two profile laws.
def normalized_corr_laplace(a,mu,t):
    r0=g(a,mu)/(1-mu*g(a,mu))
    def ltcov(z):
        rz=g(a,mu+z)/(1-mu*g(a,mu+z))
        return (r0-rz)/(z*r0)
    return mp.invertlaplace(ltcov,t,method='dehoog')

mu_profile=mp.mpf('1e-7')
close(normalized_corr_laplace(mp.mpf('.5'),mu_profile,1/mu_profile),
      mp.erfc(1),rel=mp.mpf('.025'))
for q in [mp.mpf('.25'),mp.mpf('.6')]:
    close(normalized_corr_laplace(mp.mpf('1'),mu_profile,mu_profile**(-q)),
          1-q,rel=mp.mpf('.1'))

print(f'PASS: {checks} deterministic mathematical consistency assertions.')
