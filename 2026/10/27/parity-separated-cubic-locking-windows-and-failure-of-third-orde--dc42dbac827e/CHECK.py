#!/usr/bin/env python3
"""High-precision finite diagnostics for the exact affine-iterate formulas."""
import mpmath as mp
mp.mp.dps=85
L=2*mp.log(mp.mpf(3)/2)
params={
 1:(-L**4/16-L**3/12+L**2/4, L**4/16-L**3/12-L**2/4),
 0:(-L**4/16+L**3/6, L**4/16-L**3/3),
}
for q in [41,42,101,102,401,402,1001,1002]:
 a,b=params[q%2]
 assert a>b
 eps=(a-b)/4
 for gamma in [b+eps, (a+b)/2, a-eps]:
  h=L/q+gamma/q**3
  m=q//2
  if q%2:
   d0=1+((1+h)**(m+1)-3)*(1-h)**m
   dh=(2-mp.mpf('1.5')*(1-h)**(m+1))*(1+h)**m-mp.mpf('1.5')
  else:
   d0=1+((1+h)**(m+1)-3)*(1-h)**(m-1)
   dh=(2-mp.mpf('1.5')*(1-h)**m)*(1+h)**m-mp.mpf('1.5')
  assert d0<0<dh, (q,gamma,d0,dh)
  assert abs(q*q*d0-(gamma-a))<mp.mpf('20')/q
  assert abs(q*q*dh-mp.mpf('1.5')*(gamma-b))<mp.mpf('20')/q
 print('PARITY_DENOMINATOR_CHECK',q,'W=',mp.nstr(a-b,16))
print('LOCKING_WINDOW_DIAGNOSTICS_PASS')
