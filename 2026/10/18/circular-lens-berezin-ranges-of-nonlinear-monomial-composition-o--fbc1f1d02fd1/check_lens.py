#!/usr/bin/env python3
"""Deterministic finite diagnostics for the lens theorem; not an infinite proof."""
import math, cmath
checks=0
for a in [0.02,0.15,0.5,0.9,0.999999]:
 b=math.sqrt(1-a*a)
 R=1/(2*a)
 for k in range(1,150):
  t=k/151
  for j in range(120):
   th=2*math.pi*j/120
   z=(1-t)/(1-a*t*cmath.exp(1j*th))
   w=(1-z)/z
   assert w.real+1e-9>=b*abs(w)
   assert abs(z-(.5+1j*b/(2*a))) <=R+1e-8
   assert abs(z-(.5-1j*b/(2*a))) <=R+1e-8
   checks+=3
 for j in range(-180,181):
  ang=math.asin(a)*j/180
  for s in [0.01,0.2,1,9,100]:
   u=s*cmath.exp(1j*ang)
   U,V=u.real,u.imag
   assert U>=b*abs(u)-1e-10
   rr=(U+math.sqrt(max(0,a*a*U*U-b*b*V*V)))/(1-a*a)
   z=1/(1+u)
   t=rr/(1+rr)
   v=1-u/rr
   if abs(abs(v)-a)>1e-6: raise AssertionError((a,rr,v))
   zz=(1-t)/(1-t*v)
   assert abs(zz-z)<2e-9
   checks+=3
 # independently sample the chord integral for upper-minus-lower boundary
 def y_of(x):
  return max(0.0, math.sqrt(max(0,R*R-(x-.5)**2))-b/(2*a))
 n=20000
 ar=2*sum(y_of((j+.5)/n) for j in range(n))/n
 exact=(math.asin(a)-a*b)/(2*a*a)
 assert abs(ar-exact)<5e-5
 h=y_of(.5)
 assert abs(h-(1-b)/(2*a))<1e-10
 arc=2*math.asin(a)/a
 assert 2<=arc<=math.pi+1e-12
 checks+=3
# boundary a=1 and degenerate a=0
for t in [0,0.03,.3,.85,.999]:
 assert 0<1-t<=1
 for j in range(1,100):
  z=(1-t)/(1-t*cmath.exp(2j*math.pi*j/100))
  assert (abs(z-.5)<.5+1e-10) or abs(z-1)<1e-10
  checks+=1
print('PASS',checks,'finite diagnostic assertions')
