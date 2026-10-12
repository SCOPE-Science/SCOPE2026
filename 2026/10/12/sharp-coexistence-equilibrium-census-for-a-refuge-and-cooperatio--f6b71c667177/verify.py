#!/usr/bin/env python3
"""Reproduce curvature identities and an illustrative equilibrium calculation.

Requires sympy and mpmath. The universal theorem is proved analytically in RESULT.md.
"""
import sympy as sp
import mpmath as mp

s,b,r,c,y=sp.symbols('s b r c y', positive=True)
G=s*(r+sp.log(1-b*s))
assert sp.simplify(sp.diff(G,s,2)+b*(2-b*s)/(1-b*s)**2)==0
assert sp.simplify(sp.diff(G,s,3)+b**2*(3-b*s)/(1-b*s)**3)==0
u=y+c*y**2
w=1+2*c*y
Q=sp.exp(u)*(2*c/w**2-1)
assert sp.simplify(sp.diff(Q,y)+sp.exp(u)*((w**2-c)**2+7*c**2)/w**3)==0
assert sp.simplify(sp.limit((sp.diff((1-sp.exp(-u))*(r+sp.log(1-b*(1-sp.exp(-u))))/(r*y),y)), y,0)-(c-sp.Rational(1,2)-b/r))==0

mp.mp.dps=45
bb=mp.mpf('0.49'); cc=mp.mpf(3); rr=mp.mpf(1); R=mp.mpf('0.98')
def xval(z):
    S=-mp.expm1(-(z+cc*z*z))
    return 1+mp.log(1-bb*S)/rr
def qval(z):
    S=-mp.expm1(-(z+cc*z*z))
    return S*xval(z)/z
peak=mp.findroot(lambda z:mp.diff(qval,z), (mp.mpf('.1'),mp.mpf('.3')))
low=mp.findroot(lambda z:R*qval(z)-1, (mp.mpf('.006'),mp.mpf('.02')))
high=mp.findroot(lambda z:R*qval(z)-1, (mp.mpf('.3'),mp.mpf('.6')))
assert mp.mpf('.17479')<peak<mp.mpf('.17481')
assert mp.mpf('1.17528')<qval(peak)<mp.mpf('1.17530')
assert mp.mpf('.01')<low<mp.mpf('.011') and mp.mpf('.36')<high<mp.mpf('.37')
assert abs(R*qval(low)-1)<mp.mpf('1e-38')
assert abs(R*qval(high)-1)<mp.mpf('1e-38')
assert xval(low)>0 and xval(high)>0
print('VERIFY_OK')
print('peak y:',mp.nstr(peak,22))
print('peak q:',mp.nstr(qval(peak),22))
print('two y values:',mp.nstr(low,22),mp.nstr(high,22))
