#!/usr/bin/env python3
"""Supplementary numerical and symbolic checks of a sharp tilted hyperbolic/Bessel integral inequality.

These finite checks illustrate, but do not replace, the analytic uniqueness proof.
"""
import mpmath as mp
mp.mp.dps = 70
count=0

def check(condition, explanation):
    global count
    if not condition: raise AssertionError(explanation)
    count += 1


def R(x,g):
    x=mp.mpf(x);g=mp.mpf(g)
    # all positive x, using high precision near origin
    F=(mp.cosh(x)+g*mp.sinh(x)-mp.exp(g*x))/(1-g*g)
    return F/(mp.cosh(x)-mp.sinh(x)/x)

def D(x,g):
    x=mp.mpf(x);g=mp.mpf(g)
    L=mp.coth(x)-1/x
    return 1-L/x-g*L

def gv(x):
    x=mp.mpf(x)
    L=mp.coth(x)-1/x
    Lp=1/x**2-1/mp.sinh(x)**2
    return (L/x**2-Lp/x)/Lp

def root(g):
    g=mp.mpf(g)
    # R'=0 iff 1/R-D=0; x small numerical stable with 70 digits.
    def h(x): return 1/R(x,g)-D(x,g)
    lo=mp.mpf('0.0001'); hi=mp.mpf(1)
    while h(hi)>0: hi*=2
    for _ in range(200):
        mid=(lo+hi)/2
        if h(mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

# Exact hyperbolic/Bessel normalization and closed primitive.
for g in ['0.01','0.1','0.3','0.7','0.9']:
    for x in ['0.125','0.5','1.5','3.7','8']:
        x=mp.mpf(x); g=mp.mpf(g)
        F_quad=mp.quad(lambda t:mp.exp(-g*t)*mp.sinh(t),[0,x])
        B=mp.cosh(x)-mp.sinh(x)/x
        rr=mp.exp(g*x)*F_quad/B
        check(mp.almosteq(rr,R(x,g),rel_eps=mp.mpf('1e-45')), 'primitive')
        orig_num=mp.quad(lambda t:mp.exp(-g*t)*t**mp.mpf('.5')*mp.besseli(mp.mpf('.5'),t),[0,x])
        orig_den=mp.exp(-g*x)*x**mp.mpf('.5')*mp.besseli(mp.mpf('1.5'),x)
        check(mp.almosteq(rr,orig_num/orig_den,rel_eps=mp.mpf('1e-45')), 'Bessel half orders')

# Log-MGF derivative identity and monotonicity of g(x).
xs=[mp.mpf(t)/10 for t in range(1,301)]+[mp.mpf(50),mp.mpf(100)]
for x in xs:
    Q=lambda y:(mp.sinh(y)**2-y**2)/y**4
    rhs=mp.diff(lambda y:mp.log(Q(y)),x)/2
    check(abs(gv(x)-rhs)<mp.mpf('1e-45'),'log-MGF identity')
for a,b in zip(xs[:-1],xs[1:]):
    check(gv(b)>gv(a),'g increasing grid')
check(gv(mp.mpf('0.0001'))>0,'g positive')
check(gv(mp.mpf('10000'))<1,'g below one')

# Uniqueness-bracketing conditions and strict optimality over both endpoints.
for gam in ['0.01','0.05','0.1','0.3','0.5','0.7','0.9','0.99']:
    g=mp.mpf(gam);r=root(g)
    check(abs(1/R(r,g)-D(r,g))<mp.mpf('1e-45'),'stationary')
    check(R(r,g)>mp.mpf('1.5'),'above zero endpoint')
    check(R(r,g)>1/(1-g),'above infinity endpoint')
    for f in [mp.mpf('.05'),mp.mpf('.2'),mp.mpf('.8'),mp.mpf('1.2'),mp.mpf('2'),mp.mpf('5')]:
        xx=r*f
        check(R(r,g)>R(xx,g),'unique global sample')

# Small-tilt scaling of the global optimizer and sharp constant.
for gam in ['0.002','0.001','0.0005']:
    g=mp.mpf(gam);r=root(g);c=R(r,g)
    check(abs(r/g-10)<mp.mpf(120)*g*g,'small tilt maximizing location')
    check(abs((c-mp.mpf('1.5'))/g**2-mp.mpf('2.5'))<mp.mpf(90)*g*g,'small tilt best constant')

# Near-critical asymptotics in the correct logarithmic scale.
for delt in ['0.001','0.0001','0.00001']:
    d=mp.mpf(delt);g=1-d
    r=root(g);y=d*r;L=mp.log(1/d)
    check(y>L,'near-critical location grows beyond first logarithm')
    check(abs(y-(L+2*mp.log(L)))<mp.mpf(2),'logarithmic location')
    c=R(r,g)
    check(abs((c-1/d)*L-1)<mp.mpf('.6'),'logarithmic additive norm excess')

print('CHECK_OK',count)
