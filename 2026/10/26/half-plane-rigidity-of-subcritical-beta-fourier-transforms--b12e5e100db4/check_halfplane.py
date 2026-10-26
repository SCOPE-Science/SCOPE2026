#!/usr/bin/env python3
"""Diagnostic tests of subcritical Kummer zero location, not a global proof."""
import mpmath as mp
mp.mp.dps=50
cases=[('0.35','0.08'),('0.60','0.25'),('1.00','0.15'),('1.50','0.20'),('1.80','0.80')]
count=0
for st,at in cases:
    s=mp.mpf(st);a=mp.mpf(at)
    b=s-a
    for sign in (1,-1):
        aa=a if sign==1 else b
        for n in (1,2,3,5,10,20):
            z0=(s-2*aa)*mp.log(2*mp.pi*n) + 1j*(2*mp.pi*n+mp.pi*(s/2-1))
            z=mp.findroot(lambda zz:mp.hyp1f1(aa,s,zz),(z0,z0+mp.mpf('.15')))
            assert mp.fabs(mp.hyp1f1(aa,s,z))<mp.mpf('1e-35')
            assert mp.re(z)*(s-2*aa)>0, (s,aa,n,z)
            count+=1
    print('PASS:',st,at,'and reflected parameter; six root indices each')
print('PASS:',count,'complex zero checks; no numerical test proves all zeros')
