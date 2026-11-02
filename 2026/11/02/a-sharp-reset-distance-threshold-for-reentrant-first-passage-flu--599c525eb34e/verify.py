#!/usr/bin/env python3
"""Reproducible numerical and symbolic checks of the Brownian reset-distance threshold."""
import math
import sympy as sp
import mpmath as mp

mp.mp.dps = 60

def h(t, q):
    return t * mp.exp(-(q-1)*t) * (q + 1/mp.expm1(t))

def log_h_prime(t, q):
    b = 1/mp.expm1(t)
    return 1/t - (q-1) - b*(1+b)/(q+b)

def cv_squared(t, q):
    return 1 + mp.exp(-t)/(-mp.expm1(-t))*(2-h(t, q))

def moment1(t, q, r):
    return mp.exp(q*t)*(-mp.expm1(-t))/r

def moment2(t, q, r):
    n = -mp.expm1(-t)
    return (2*mp.exp(2*q*t)*n-q*t*mp.exp(q*t)*n-t*mp.exp((q-1)*t))/(r*r)

def survival_transform(s, a, b, d, r):
    k = mp.sqrt((r+s)/d)
    return -mp.expm1(-a*k)/(s+r*mp.exp(-b*k))

q_c, t_c = mp.findroot((lambda q,t:h(t,q)-2,
                         lambda q,t:log_h_prime(t,q)), (mp.mpf('1.23'), mp.mpf('4.1')))
assert mp.mpf('1.22863140048') < q_c < mp.mpf('1.22863140049')
assert mp.mpf('4.1334526383') < t_c < mp.mpf('4.1334526384')
assert abs(h(t_c,q_c)-2) < mp.mpf('1e-48')
assert abs(log_h_prime(t_c,q_c)) < mp.mpf('1e-48')

# A separate exact moment check via the backward generator.
x, a, b, D, r = sp.symbols('x a b D r', positive=True)
k = sp.sqrt(r/D)
m1 = sp.exp(k*b)*(1-sp.exp(-k*x))/r
m2 = ((2*sp.exp(2*k*b)-k*b*sp.exp(k*b))*(1-sp.exp(-k*x))-
      k*x*sp.exp(k*b)*sp.exp(-k*x))/r**2
assert sp.simplify(D*sp.diff(m1,x,2)-r*m1+r*m1.subs(x,b)+1) == 0
assert sp.simplify(D*sp.diff(m2,x,2)-r*m2+r*m2.subs(x,b)+2*m1) == 0
assert sp.simplify(m1.subs(x,0)) == 0
assert sp.simplify(m2.subs(x,0)) == 0

cases = 0
for q in ['0.25','0.7','1','1.05','1.2','1.25','2','3']:
  for t in ['0.25','0.6','1.5','2.75','4','7.5']:
    q, t = mp.mpf(q), mp.mpf(t)
    r = mp.mpf('0.7'); d=mp.mpf('1.3'); a=t*mp.sqrt(d/r); b=q*a
    f=lambda s:survival_transform(s,a,b,d,r)
    M1=moment1(t,q,r); M2=moment2(t,q,r)
    assert mp.almosteq(M1,f(0),rel_eps=mp.mpf('1e-43'))
    assert mp.almosteq(M2,-2*mp.diff(f,0),rel_eps=mp.mpf('1e-43'))
    assert mp.almosteq(M2/M1**2-1,cv_squared(t,q),rel_eps=mp.mpf('1e-40'))
    cases+=1

# Compare exact crossing signs in every analytically identified phase.
assert cv_squared(mp.mpf('0.1'),mp.mpf('1.2')) > 1
assert cv_squared(mp.mpf('4'),mp.mpf('1.2')) < 1
assert cv_squared(mp.mpf('18'),mp.mpf('1.2')) > 1
assert cv_squared(mp.mpf('2'),mp.mpf('1.5')) > 1
assert cv_squared(mp.mpf('10'),mp.mpf('0.75')) < 1
assert abs(cv_squared(t_c,q_c)-1) < mp.mpf('1e-45')

for q in [mp.mpf('1.01'),mp.mpf('1.1'),mp.mpf('1.2'),mp.mpf('1.23'),mp.mpf('2')]:
  for t in [mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('1'),mp.mpf('3'),mp.mpf('8')]:
    z=mp.exp(t); s=1/(z-1)
    curvature=-1/t**2+s*(1+s)*(q*(1+2*s)+s*s)/(q+s)**2
    assert curvature < 0

print('Symbolic backward-generator identities: PASS')
print('Independent Laplace derivative and moment comparisons:', cases, 'PASS')
print('Crossing signs and log-concavity samples: PASS')
print('q_c =', mp.nstr(q_c,35))
print('t_c =', mp.nstr(t_c,35))
for q in [mp.mpf('1.2')]:
    t1=mp.findroot(lambda t:h(t,q)-2, (mp.mpf('2'),mp.mpf('3')))
    t2=mp.findroot(lambda t:h(t,q)-2, (mp.mpf('7'),mp.mpf('8')))
    print('q =',q,', crossing t =',mp.nstr(t1,20),mp.nstr(t2,20))
