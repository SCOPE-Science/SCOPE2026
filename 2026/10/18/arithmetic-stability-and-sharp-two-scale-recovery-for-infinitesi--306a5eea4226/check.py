"""Exact spectral arithmetic and independent geometric finite-difference checks.

This finite program checks the displayed examples, not the infinite theorems.
"""
from fractions import Fraction
from math import gcd, lcm, cos, sin, pi, sqrt

cos2_6=[Fraction(1),Fraction(3,4),Fraction(1,4),Fraction(0),Fraction(1,4),Fraction(3,4)]
cos2_4=[Fraction(1),Fraction(1,2),Fraction(0),Fraction(1,2)]
spectrum=[16*cos2_6[m%6]+8*cos2_4[m%4] for m in range(12)]
assert min(spectrum)==4 and max(spectrum)==24
assert set(m for m in range(12) if spectrum[m]==4)=={2,3,9,10}
assert set(m for m in range(12) if spectrum[m]==24)=={0}
assert spectrum==[24,16,4,4,12,16,16,16,12,4,4,16]
for q1 in range(3,23):
 for p1 in [p for p in [1,2,3,4,5,6,7] if p<q1/2]:
  if gcd(p1,q1)>1:continue
  for q2 in range(3,23):
   for p2 in [p for p in [1,2,3,4,5,6,7] if p<q2/2]:
    if gcd(p2,q2)>1:continue
    N=lcm(q1,q2)
    z1={m for m in range(N) if 2*m*p1% (2*q1)==q1}  # tests cos=0
    z2={m for m in range(N) if 2*m*p2%(2*q2)==q2}
    def v2(n):
     count=0
     while n%2==0:count+=1;n//=2
     return count
    expected=(q1%2==0 and q2%2==0 and v2(q1)==v2(q2))
    assert bool(z1&z2)==expected,(p1,q1,p2,q2,z1&z2,expected)

# independently compute chords by finding the y>0 and y<0 roots of
# R(arg(t+iy))^2=t^2+y^2, valid for small epsilon and strictly convex curves.
def chord(theta,alpha,epsilon,f):
 t=cos(alpha)
 def h(y):
  x=t*cos(theta)-y*sin(theta)
  yy=t*sin(theta)+y*cos(theta)
  phi=__import__('math').atan2(yy,x)
  return x*x+yy*yy-(1+epsilon*f(phi))**2
 def root(sign):
  lo,hi= (0.0,2.0) if sign==1 else (-2.0,0.0)
  # top h(0)<0 and h(2)>0; bottom h(-2)>0 and h(0)<0
  for _ in range(85):
   mid=(lo+hi)/2
   if (h(mid)>0)==(sign==1):hi=mid
   else:lo=mid
  return (lo+hi)/2
 return root(1)-root(-1)
for alpha in [pi/6,pi/4,pi/7]:
 for mode in [1,2,3,4,7,11]:
  f=lambda phi:cos(mode*phi)+0.15*sin(2*phi)
  for theta in [0.23, 0.77,2.51]:
   eps=1e-5
   derivative=(chord(theta,alpha,eps,f)-chord(theta,alpha,-eps,f))/(2*eps)
   theoretical=(f(theta+alpha)+f(theta-alpha))/sin(alpha)
   assert abs(derivative-theoretical)<1e-6,(alpha,mode,theta,derivative,theoretical)
# Exact algebraic identity for the universal coupled-offset pair.
# Here q=sin(alpha)^2 and z=cos(m alpha)^2, independently taking
# rational test points in (0,1); the manuscript gives a symbolic proof.
for iq in range(1,20):
 q=Fraction(iq,20)
 for iz in range(21):
  z=Fraction(iz,20)
  w=4*z/q+(2*z-1)**2/(q*(1-q))
  certificate=1+1/q+(2*z-q)**2/(q*(1-q))
  assert w==certificate
  assert w>=1+1/q

# The upper bound of the paired operator is at m=0 for all alpha.
for alpha in [pi/10,pi/8,pi/6,pi/5,pi/4-0.03]:
 lo=1+1/sin(alpha)**2
 hi=4/sin(alpha)**2+4/sin(2*alpha)**2
 for m in range(1500):
  w=4*cos(m*alpha)**2/sin(alpha)**2+4*cos(2*m*alpha)**2/sin(2*alpha)**2
  assert lo-1e-9 <= w <= hi+1e-9

print('FINITE_CHORD_TOMOGRAPHY_CHECKS_OK')
