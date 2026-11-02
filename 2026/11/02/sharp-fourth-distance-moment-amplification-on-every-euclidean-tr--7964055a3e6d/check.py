"""Independent symbolic and sampling checks for a triangle fourth-distance-moment inequality."""
from fractions import Fraction
from itertools import product
import random
import sympy as S
u,v,w,t,z=S.symbols('u v w t z', nonnegative=True)
a,b,c=u+v,u+w,v+w
s=u+v+w
p=(u*v+u*w+v*w)/s**2
q=u*v*w/s**3
# Edge parameters in the affine basis of triangle vertices (0,0),(1,0),(0,1).
k=(b*b+c*c-a*a)/2
edges=((c,(t,0)),(b,(0,t)),(a,(1-t,t)))
B_num=0
for length,(f,g) in edges:
 for length2,(h,j) in edges:
  hh=h.subs(t,z) if hasattr(h,'subs') else h
  jj=j.subs(t,z) if hasattr(j,'subs') else j
  x=f-hh; y=g-jj
  dsq=S.expand(c*c*x*x+b*b*y*y+2*k*x*y)
  B_num+=length*length2*S.integrate(S.integrate(S.expand(dsq*dsq),(t,0,1)),(z,0,1))
B=S.factor(B_num/(2*s)**2)
I=S.factor((a**4+b**4+c**4)/60)
expected_B=s**4*(S.Rational(1,15)+(p-8)*q/9)
expected_I=s**4*((1-p)**2-4*q)/30
assert S.factor(B-expected_B)==0
assert S.factor(I-expected_I)==0
assert S.factor((S.Rational(32,9)*I-B)-s**4*(7-32*p+16*p*p+(56-15*p)*q)/135)==0
assert S.factor((B-2*I)-s**4*(6*p-3*p*p+(5*p-28)*q)/45)==0
print('SYMBOLIC_EDGE_INTEGRALS_AND_BOUNDS_IDENTITIES_PASSED')
# At equilateral, and in the two different degenerate limits.
ratio=S.factor(B/I)
assert ratio.subs({u:1,v:1,w:1})==S.Rational(32,9)
assert S.limit(ratio.subs({u:1,v:0}),w,0)==2
assert S.limit(ratio.subs({u:0,v:1}),w,1)==S.Rational(32,9)
print('SHARP_ENDPOINTS_AND_EQUILATERAL_EQUALITY_PASSED')
# Check the fixed-p product minimum and the exact positive upper-bound factor.
x=S.symbols('x',nonnegative=True)
p0=(1-x*x)/3
qmin=(1-3*x*x-2*x**3)/27
Q=S.factor(7-32*p0+16*p0**2+(56-15*p0)*qmin)
assert S.factor(Q-x**2*(1-2*x)*(5*x*x-14*x+44)/27)==0
print('FIXED_PAIR_SUM_PRODUCT_MINIMUM_FACTOR_PASSED')
# Independent direct point samples: perimeter-edge sampling versus barycentric area sampling.
rng=random.Random(6173)
for U,V,W in [(1.,1.,1.),(.24,.31,.45),(.90,.06,.04)]:
 aa,bb,cc=U+V,U+W,V+W
 xx=(bb*bb+cc*cc-aa*aa)/(2*cc)
 yy=(bb*bb-xx*xx)**.5
 vertices=((0.,0.),(cc,0.),(xx,yy))
 elens=(cc,aa,bb)
 total=sum(elens)
 def point_boundary():
  r=rng.random()*total
  j=0 if r<cc else (1 if r<cc+aa else 2)
  ij=((0,1),(1,2),(0,2))[j]
  t0=rng.random(); a0,b0=vertices[ij[0]],vertices[ij[1]]
  return ((1-t0)*a0[0]+t0*b0[0],(1-t0)*a0[1]+t0*b0[1])
 def point_interior():
  r1,r2=rng.random(),rng.random()
  if r1+r2>1:r1,r2=1-r1,1-r2
  return (r1*vertices[1][0]+r2*vertices[2][0],r1*vertices[1][1]+r2*vertices[2][1])
 def trial(fn):
  n=180000
  ss=ss2=0.
  for _ in range(n):
   x1,y1=fn();x2,y2=fn()
   d=((x1-x2)**2+(y1-y2)**2)**2
   ss+=d;ss2+=d*d
  mean=ss/n;se=max(0,(ss2/n-mean**2)/n)**.5
  return mean,se
 subs={u:U,v:V,w:W}
 for tag,fn,expr in [('boundary',point_boundary,B),('interior',point_interior,I)]:
  obs,se=trial(fn); theory=float(expr.subs(subs))
  assert abs(obs-theory)<6*se+0.001, (tag,obs,theory,se)
 print('INDEPENDENT_PAIR_POINT_MONTE_CARLO_PASSED',U,V,W)
print('ALL_CHECKS_PASSED')
