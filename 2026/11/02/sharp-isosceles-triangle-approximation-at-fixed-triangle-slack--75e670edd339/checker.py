"""Independent symbolic and numerical checks for a triangle approximation profile."""
from math import sqrt
from random import Random
import sympy as sp

s=sp.sqrt(2)
d=sp.symbols('d', real=True)
y=sp.symbols('y', positive=True)
rho=sp.symbols('rho', positive=True)
r0=1/s
k=(s-1)/4
h=r0+k*d
G=sp.expand(1-2*(1-d)*h**2-d*(2-d)*h**3)
expected=d**2*((11-6*s)/8+(12-7*s)*d/16+(4*s-5)*d**2/32+(5*s-7)*d**3/64)
assert sp.simplify(G-expected)==0
assert all(float(c)>0 for c in [(11-6*s)/8,(12-7*s)/16,(4*s-5)/32,(5*s-7)/64])
print('SHARP_LINEAR_CERTIFICATE_EXACT_PASSED')
# The cubic root crossing must become a quartic root at the phase switch.
sub=1+1/y-y
phase=sp.factor(y**3-2*(1-sub)*y-sub*(2-sub))
assert sp.simplify(phase-(y-1)*(y**4-y-1)/y**2)==0
print('QUARTIC_PHASE_TRANSITION_IDENTITY_PASSED')

def bisect(f,lo,hi):
 for _ in range(110):
  mid=(lo+hi)/2
  if f(mid)>0:hi=mid
  else:lo=mid
 return (lo+hi)/2

def exact_profile(t):
 assert 0<t<=1
 y1=(1-t+sqrt((1-t)**2+4))/2
 if t<1:
  y2=bisect(lambda w:w**3-2*(1-t)*w-t*(2-t),1,2-t)
 else:y2=1
 yy=min(y1,y2)
 return 1/yy,yy,y1,y2

rr=bisect(lambda v:v**4-v-1,1,2)
tcrit=1+1/rr-rr
assert 1.22<rr<1.23 and .59<tcrit<.61
q1=2/(5*rr**2+rr-2)
q2=1/(1+rr**2)
assert 0<q1<q2<.5
assert sp.simplify((1/(1+rho**2)-2/(5*rho**2+rho-2))-(3*rho**2+rho-4)/((1+rho**2)*(5*rho**2+rho-2)))==0
assert sp.simplify(sp.diff(y**3-2*(1-d)*y-d*(2-d),d).subs({y:s,d:0}))==2*(s-1)
assert sp.simplify(sp.diff(y**3-2*(1-d)*y-d*(2-d),y).subs({y:s,d:0}))==4
print('EXACT_ONE_SIDED_SLOPES_AND_CUSP_PASSED')
for dd in [1e-5,.05,.1,.2,.3,.4,.5,tcrit,.61,.7,.8,.9,1]:
 val,yy,y1,y2=exact_profile(dd)
 assert abs((yy-1+dd)+1-yy-dd)<1e-12
 assert abs(val-max(yy-1+dd,1/yy,yy**2/(2*(1-dd)*yy+dd*(2-dd))))<1e-11
 assert val>1/sqrt(2)+float(k)*dd-1e-10
 assert abs(val-1/min(y1,y2))<1e-11
assert abs(exact_profile(1e-6)[0]-1/sqrt(2)-float(k)*1e-6)<3e-12
print('PHASE_PROFILE_AND_SHARP_FIRST_ORDER_PASSED')

# Independent sample on the full side-shape triangle domain.
rng=Random(419)
for i in range(12000):
 x=rng.uniform(1e-5,1)
 yy=rng.uniform(1,min(2,1+x-1e-7))
 dd=1+x-yy
 J=max(x,1/yy,yy**2/(1+yy**2-x**2))
 val,_,_,_=exact_profile(dd)
 assert J>=val-2e-11,(x,yy,dd,J,val)
 assert J>1/sqrt(2)+float(k)*dd-1e-10
print('TWELVE_THOUSAND_TRIANGLES_NUMERICAL_CONSISTENCY_PASSED')

# Independent coordinate construction of the two decisive inscribed triangles.
# A=(0,0), B=(c,0), C=(b cos A,b sin A), normalized b=1.
for x,yy in [(.75,1.11),(.43,1.32),(.9,1.71),(.6,1.29)]:
 if yy>=1+x:continue
 cosA=(1+yy**2-x**2)/(2*yy)
 assert 0<cosA<1
 C=(cosA,sqrt(1-cosA*cosA)); B=(yy,0)
 # Triangle AB'C, B'=(1,0). Ratio of determinant areas =1/c.
 areaT=abs(B[0]*C[1])/2
 areaFirst=abs(C[1])/2
 assert abs(areaFirst/areaT-1/yy)<1e-12
 # Perpendicular bisector AB intersects AC at C1 = C * (c/(2 cosA)).
 alpha=yy/(2*cosA)
 assert 0<alpha<=1
 C1=(alpha*C[0],alpha*C[1]); areaSecond=yy*C1[1]/2
 assert abs(areaSecond/areaT-yy**2/(1+yy**2-x**2))<1e-12
print('INDEPENDENT_EUCLIDEAN_VERTEX_CONSTRUCTIONS_PASSED')
print('ALL_CHECKS_PASSED')
