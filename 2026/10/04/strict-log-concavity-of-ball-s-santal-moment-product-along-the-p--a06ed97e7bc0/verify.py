#!/usr/bin/env python3
import mpmath as mp
mp.mp.dps = 60

def moment_formula(n,p):
    t=mp.mpf(1)/p
    return (mp.mpf(2)**n/3)*mp.gamma(1+3*t)*mp.gamma(1+t)**(n-1)/mp.gamma(1+(n+2)*t)

def ball_volume(n,p):
    t=mp.mpf(1)/p
    return (2*mp.gamma(1+t))**n/mp.gamma(1+n*t)

def moment_quad(n,p):
    # Slice B_p^n by x_1=x; remaining cross-section is a scaled B_p^(n-1).
    v=ball_volume(n-1,p)
    f=lambda x: x*x*v*(1-x**p)**((n-1)/p)
    return 2*mp.quad(f,[0,1])

def logF_second(n,t):
    N=n+2
    psi1=lambda x: mp.polygamma(1,x)
    phi2=lambda a: a*a*(psi1(1+a*t)+psi1(1+a*(1-t)))
    return phi2(3)+(n-1)*phi2(1)-phi2(N)

def endpoint(n):
    g=mp.gamma(n/2+1)
    return 2**(2*n+1)*(n+2)**2*g*g/(3*mp.factorial(n+2)*mp.pi**n)

for n,p in [(2,mp.mpf('1.3')),(3,mp.mpf('2.7')),(5,mp.mpf('4.2'))]:
    a=moment_formula(n,p); b=moment_quad(n,p)
    assert mp.almosteq(a,b, rel_eps=mp.mpf('1e-45'), abs_eps=mp.mpf('1e-45'))
for n in [2,3,5,10,25]:
    for t in [mp.mpf('0.07'),mp.mpf('0.21'),mp.mpf('0.37'),mp.mpf('0.5'),mp.mpf('0.83')]:
        assert logF_second(n,t) < 0
    i2=moment_formula(n,2)
    for p in [mp.mpf('2.2'),mp.mpf('3'),mp.mpf('7'),mp.mpf('25')]:
        q=p/(p-1)
        F=moment_formula(n,p)*moment_formula(n,q)/(i2*i2)
        assert F < 1
    eps=mp.mpf('1e-7')
    pinf=1/eps
    q=pinf/(pinf-1)
    F=moment_formula(n,pinf)*moment_formula(n,q)/(i2*i2)
    assert abs(F-endpoint(n)) < mp.mpf('1e-5')
print('VERIFY_OK')
