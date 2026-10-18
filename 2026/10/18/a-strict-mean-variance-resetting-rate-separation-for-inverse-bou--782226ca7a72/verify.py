#!/usr/bin/env python3
"""Independent numerical checks of the half-line boundary-local-time formulas."""
import mpmath as mp
mp.mp.dps=80
checks=0

def ok(test,msg):
 global checks
 checks+=1
 if not test: raise AssertionError(msg)

def formulas(z,xi):
 ez=mp.exp(z)
 mean=(ez-1)/z**2+xi*ez/z
 var=(ez**2-z*ez-1)/z**4+xi*ez*(2*ez-1-z)/z**3
 return mean,var

def transforms(z,xi):
 r=z*z
 def H(s):
  q=mp.sqrt(r+s); w=mp.exp(-q)
  return (r+s)*w/(s+r*w)
 def psi(s):
  q=mp.sqrt(r+s); w=mp.exp(-q)
  return s*q/(s+r*w)
 def loglap(s):
  return mp.log(H(s))-xi*psi(s)
 return -mp.diff(loglap,mp.mpf('0'),1),mp.diff(loglap,mp.mpf('0'),2)

for zs in ['0.2','0.5','0.9','1','1.2','1.3309178942733855','2','4']:
 z=mp.mpf(zs)
 for xis in ['0','0.5','1','3','50']:
  xi=mp.mpf(xis); m,v=formulas(z,xi); md,vd=transforms(z,xi)
  ok(mp.almosteq(m,md,rel_eps=mp.mpf('1e-48')),(zs,xis,'mean'))
  ok(mp.almosteq(v,vd,rel_eps=mp.mpf('1e-48')),(zs,xis,'variance'))
  ok(m>0 and v>0,(zs,xis,'moment positivity'))

def F(z): return 2*mp.exp(z)*(2*z-3)-z*z+z+3
root=mp.findroot(F,(mp.mpf('1.3'),mp.mpf('1.4')))
ok(1<root<mp.mpf('1.5'),'root bracket')
ok(abs(F(root))<mp.mpf('1e-65'),'root equation')
ok(abs(root-mp.mpf('1.3309178942733855'))<mp.mpf('1e-15'),'root decimal')
ok(F(mp.mpf('1'))<0 and F(mp.mpf('1.5'))>0,'sign bracket')
def C(z): return (2-(1+z)*mp.exp(-z))/z
for zs in ['0.1','0.5','0.9','1','1.3','2','5','10']:
 z=mp.mpf(zs)
 ok(mp.diff(C,z)<0,('Cprime',zs))
 ok(C(z)>0,('Cpositive',zs))
ok((root**2>mp.mpf('1.77') and root**2<mp.mpf('1.78')),'rate ratio')
print('PASS',checks,'assertions; variance optimum z=',mp.nstr(root,40),'ratio=',mp.nstr(root**2,30))
