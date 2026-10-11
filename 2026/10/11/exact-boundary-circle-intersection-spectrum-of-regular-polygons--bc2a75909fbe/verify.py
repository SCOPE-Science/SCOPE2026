"""Scientific diagnostics for boundary-centered circles on regular polygons.
Run with python verify_geometry21.py (requires sympy and mpmath).
The analytic proof is given in RESULT.md; these tests are not an exhaustive proof.
"""
import sympy as sp
import mpmath as mp

c,s,t=sp.symbols('c s t',real=True)
C=2*c*c-1;S=2*s*c
F=sp.expand((c+C)**2+(t-S)**2-(c*(1+c)+s*t)**2)
F=sp.factor(F.subs(s*s,1-c*c))
# Independent reduction by replacing every even power of s via s^2=1-c^2.
assert sp.simplify((F-(c*c*t*t-2*c*s*(c+3)*t+(1-c)**3*(1+c))).subs(s*s,1-c*c))==0
mp.mp.dps=75

def vertices(n):
 a=mp.pi/n
 return [(mp.cos((2*j+1)*a),mp.sin((2*j+1)*a)) for j in range(n)]

def hits(n,x,r):
 V=vertices(n);r2=r*r; num=0
 for j in range(n):
  ax,ay=V[j];bx,by=V[(j+1)%n]; dx=bx-ax;dy=by-ay
  hx=ax-x[0];hy=ay-x[1]; A=dx*dx+dy*dy;B=hx*dx+hy*dy
  D=B*B-A*(hx*hx+hy*hy-r2)
  if D>0:
   z=mp.sqrt(D)
   for u in [(-B-z)/A,(-B+z)/A]:
    if mp.mpf("1e-50")<u<1-mp.mpf("1e-50"):num+=1
  elif D==0 and mp.mpf("1e-50")<-B/A<1-mp.mpf("1e-50"): num+=1
 return num

def profile(n, frac, samples=0):
 a=mp.pi/n;co=mp.cos(a);si=mp.sin(a);p=(co,si*mp.mpf(frac))
 V=vertices(n);dist=lambda v:mp.sqrt((v[0]-p[0])**2+(v[1]-p[1])**2)
 events={mp.mpf(0)}
 for j,v in enumerate(V):
  events.add(dist(v))
  w=V[(j+1)%n];dx=w[0]-v[0];dy=w[1]-v[1]
  u=((p[0]-v[0])*dx+(p[1]-v[1])*dy)/(dx*dx+dy*dy)
  if 0<u<1:events.add(dist((v[0]+u*dx,v[1]+u*dy)))
 radii=sorted(events)
 counts=[hits(n,p,(r+rr)/2) for r,rr in zip(radii,radii[1:])]
 return max(counts),len(radii)-1

for n in list(range(3,22)) + [25,33,51,101]:
 a=mp.pi/n;co=mp.cos(a);si=mp.sin(a)
 if n%2:
  cutoff=2*si/co*(1-mp.cos(a/2))**2
  assert 0<cutoff<si
  # A radius specifically lying in all three distinct caps.
  mid=cutoff/2;P=(co,mid)
  near=(mp.cos(mp.pi-2*a),mp.sin(mp.pi-2*a))
  weak=mp.sqrt((near[0]-P[0])**2+(near[1]-P[1])**2)
  high=co*(1+co)+si*mid
  assert weak>high
  assert hits(n,P,(weak+high)/2)==6,(n,'missing6')
  if n<=33:
   for f in [mp.mpf(0),cutoff/si/2,cutoff/si*mp.mpf('1.01'),mp.mpf('0.1'),mp.mpf('0.75'),mp.mpf(1)]:
    if f>1:continue
    observed,ev=profile(n,f)
    expect=6 if f<cutoff/si else 4
    assert observed==expect,(n,mp.nstr(f,14),observed,expect)
 else:
  for f in [mp.mpf('0'),mp.mpf('0.001'),mp.mpf('.5'),mp.mpf('.99'),mp.mpf(1)]:
   if n<=33:
    observed,ev=profile(n,f)
    expect=2 if f==1 else 4
    assert observed==expect,(n,f,observed,expect)
 print(n,'OK', ('critical side fraction '+mp.nstr(cutoff/si,17) if n%2 else 'even profile'))
print('VERIFY_OK; proof universal; finite tests only supplementary')
