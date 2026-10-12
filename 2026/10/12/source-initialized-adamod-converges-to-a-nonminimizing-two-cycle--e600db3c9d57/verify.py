"""Standalone checks for the scalar source AdaMod two-cycle theorem."""
from fractions import Fraction as Q
from math import isclose

Fmin=Q(18000,54289)
Fmax=Q(22000,29929)
Hpmax=Q(22000,27889)
dlo=Q(7,100)
dhi=Q(13,100)
umin=Q(7,10)
umax=Q(13,10)
assert Q(0)<Fmin<Fmax<Q(1)
assert Q(0)<Hpmax<Q(1)
assert max(abs(2*Fmin-1),abs(2*Fmax-1))<Q(12,25)
# The clipped branch derivative in u is increasing in F and z. Its
# endpoint extrema are obtained by checking dependence on d jointly.
clipped_min=2*dlo*umin+2*(1-dlo)*Fmin-1
clipped_max=2*dhi*umax+2*(1-dhi)*Fmax-1
assert clipped_min<0<clipped_max
assert abs(clipped_min)<clipped_max
clipped_row=clipped_max+2*dhi*umax
assert clipped_row<Q(24,25)
memory_row=dhi+(1-dhi)*Hpmax
assert memory_row<Q(24,25)
# Branch extrema remain on these endpoints: z-F has positive or negative
# possible range, but the minimizing F/z combination gives positive
# derivative in d, and the maximizing F/z combination likewise does.
for d in (Q(7,100),Q(1,10),Q(13,100)):
 for kap in (Q(9,20),Q(1,2),Q(11,20)):
  for u in (Q(7,10),Q(1),Q(13,10)):
   H=1/(1+kap*(u-1))
   F=(1-kap)/(1+kap*(u-1))**2
   Hprime=-kap/(1+kap*(u-1))**2
   assert Fmin<=F<=Fmax
   assert abs(Hprime)<=Hpmax
   for z in (Q(7,10),Q(1),Q(13,10)):
    zp=d*z+(1-d)*H
    assert min(H,zp)>Q(1,2)
    grad=2*d*z+2*(1-d)*F-1
    assert abs(grad)+2*d*u<Q(24,25)

# The published algorithm including the actual bias corrections and cap.
def source(n, h=1., eps=1., alpha=4., b1=0., b2=0., d=.1, initial=None):
 k=(1-b1)/(1+b1)
 r=alpha*k/2-eps/h
 x=r if initial is None else initial
 m=v=s=0.
 history=[(x,m,v,s)]
 for t in range(1,n+1):
  g=h*x
  m=b1*m+(1-b1)*g
  v=b2*v+(1-b2)*g*g
  rate=alpha/((v/(1-b2**t))**.5+eps)
  s=d*s+(1-d)*rate
  x-=min(rate,s)*m/(1-b1**t)
  history.append((x,m,v,s))
 return r,history

for d in (.07,.1,.13):
 for gamma in (40/11,4.,40/9):
  r,hist=source(160,alpha=gamma,d=d)
  assert abs(hist[1][0]-(2*d-1)*r)<1e-13
  assert (hist[1][0]/r)**2<1
  for t,(x,m,v,s) in enumerate(hist[1:],1):
   assert x*((-1)**t)>0
   bound=13/50*(24/25)**(t-1)+1e-12
   assert abs(x-((-1)**t)*r)/r<=bound,(d,gamma,t,x,bound)
  assert abs(hist[-1][0]-r)<.0004

# Positive moments: test only, no logical dependence of infinite proof on test.
for b1,b2 in ((.0002,.0001),(.001,.002),(.004,.004)):
 r,hist=source(600,b1=b1,b2=b2,d=.1,alpha=4.)
 assert r>0
 assert abs(hist[1][0])<r
 assert abs(hist[-1][0]-r)<1e-8
 k=(1-b1)/(1+b1)
 mom_amplitude=k*r
 assert abs(hist[-1][1]+mom_amplitude)<1e-8
 assert abs(hist[-1][2]-r*r)<1e-8
 assert abs(hist[-1][3]-2/k)<1e-8
 # Exact autonomous-tail fixed-point algebra for the same parameters.
 W=(1-b1)-b1*k
 Vnext=b2+(1-b2)*1
 assert isclose(W,k,rel_tol=0,abs_tol=5e-16)
 assert isclose(Vnext,1.,rel_tol=0,abs_tol=5e-16)
 assert isclose((2/k)*W-1,1,rel_tol=0,abs_tol=2e-15)
print('verification passed')
