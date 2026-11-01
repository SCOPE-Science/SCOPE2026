#!/usr/bin/env python3
"""Scientific diagnostics for the Gaussian interval-map boundary; not infinite proofs."""
import mpmath as mp
import sympy as sp

mp.mp.dps = 55
x,a = sp.symbols('x a', real=True, positive=True)
# Negative Schwarzian for the centered exponential, away from its critical point.
y = sp.symbols('y', real=True, nonzero=True)
f = sp.exp(-y**2/a)
f1,f2,f3 = (sp.diff(f,y,i) for i in (1,2,3))
S = sp.factor(sp.simplify(f3/f1-sp.Rational(3,2)*(f2/f1)**2))
assert sp.simplify(S + sp.Rational(3,2)/y**2 + 2*y**2/a**2)==0


def configuration(aval):
    av=mp.mpf(aval); h=mp.exp(-1/(4*av)); d=1-h; k=h/(av*d); z=1/k
    uc=(z+mp.lambertw(-z*mp.exp(-z),0 if k<1 else -1)).real
    sc=uc/d
    B=1/av-3+mp.exp(-uc)
    assert B>0
    def F(p,s):
        f=mp.exp(-(p-mp.mpf('.5'))**2/av)-h
        return mp.expm1(-s*f)/mp.expm1(-s*d) if abs(s)>mp.mpf('1e-40') else f/d
    return sc,B,k,F

for av in ['0.06','0.08','0.10','0.11','0.2','0.5','1.0','3.0']:
    sc,B,k,F=configuration(av)
    d=1-mp.exp(-1/(4*mp.mpf(av)))
    uc=sc*d
    lam=k*uc/(-mp.expm1(-uc)) if abs(uc)>mp.mpf('1e-35') else k
    assert mp.almosteq(lam,1,rel_eps=mp.mpf('1e-42'),abs_eps=mp.mpf('1e-40'))
    for diff in [mp.mpf('-.4'),mp.mpf('.4')]:
        s=sc+diff
        y0=mp.mpf('1e-9')
        slope=F(y0,s)/y0
        assert (s<sc and slope<1) or (s>sc and slope>1)
        assert mp.almosteq(F(mp.mpf('.5'),s),1,abs_eps=mp.mpf('1e-45'))
        assert mp.almosteq(F(mp.mpf('1.0'),s),0,abs_eps=mp.mpf('1e-45'))
        left=[mp.mpf(j)/4000 for j in range(1,2001)]
        crosses=sum((F(t,s)-t)*(F(w,s)-w)<0 for t,w in zip(left[:-1],left[1:]))
        assert crosses==(1 if diff<0 else 0)
    # Verify the Taylor quadratic coefficient by high precision differentiation.
    d2=mp.diff(lambda xx:F(xx,sc),0,2)
    assert mp.almosteq(B,d2,rel_eps=mp.mpf('1e-40'))

# Critical slowing numerical ratio N(x)*x -> 2/B at one representative width.
sc,B,k,F=configuration('0.08')
delta=mp.mpf('0.009')
for x0 in [mp.mpf('0.0005'),mp.mpf('0.00025'),mp.mpf('0.000125')]:
    xx=x0; N=0
    while xx<delta:
        xx=F(xx,sc); N+=1
        assert N<100000
    ratio=N*x0*B/2
    assert abs(ratio-1)<mp.mpf('.09')
print('PASS: Schwarzian identity, threshold checks, fixed-point counts, quadratic coefficients, residence time diagnostics.')
