"""Reproduce tricylinder central-section arc counts and exact area quadratures.
Only Python's standard library is required.
"""
import math
import random

PI=math.pi

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def norm(v): return math.sqrt(dot(v,v))
def unit(v): return tuple(x/norm(v) for x in v)
def linear(a,b,s,t): return tuple(s*x+t*y for x,y in zip(a,b))

def frame(n):
 n=unit(n); es=[(1.,0.,0.),(0.,1.,0.),(0.,0.,1.)]
 j=min(range(3),key=lambda i:abs(n[i])); e=unit(cross(n,es[j])); f=cross(n,e)
 return n,e,f

def direction(th,e,f): return linear(e,f,math.cos(th),math.sin(th))

def area_and_arcs(n,radius=1):
 n,e,f=frame(n)
 if min(abs(c) for c in n)<1e-10: raise ValueError('generic nonzero normal components needed')
 breaks=[]
 for i in range(3):
  for j in range(i+1,3):
   k=3-i-j
   for s in (-1,1):
    a=[0.,0.,0.]; a[i]=1.;a[j]=-s
    v=unit(cross(n,a))
    if abs(v[i])<abs(v[k])-1e-12:
     th=math.atan2(dot(v,f),dot(v,e))%(2*PI)
     breaks.extend((th,(th+PI)%(2*PI)))
 breaks.sort()
 if len(breaks) not in (6,8):raise ArithmeticError(('unexpected count',len(breaks),n))
 total=0.
 for p,th in enumerate(breaks):
  th2=breaks[(p+1)%len(breaks)]+(2*PI if p==len(breaks)-1 else 0.)
  mid=direction((th+th2)/2,e,f)
  i=min(range(3),key=lambda k:mid[k]**2)
  u,v=direction(th,e,f),direction(th2,e,f)
  s=math.sin(th2-th)
  if not s>0:raise ArithmeticError(('nonpositive angle',th,th2))
  c=abs(n[i])
  metric=dot(u,v)-u[i]*v[i]
  ang=math.atan2(c*s,metric)
  total+=ang/c/2
 return len(breaks),radius**2*total

def area_midpoint(n,intervals=30000):
 n,e,f=frame(n)
 s=0.
 for j in range(intervals):
  th=2*PI*(j+.5)/intervals
  u=direction(th,e,f)
  s+=1/(1-min(t*t for t in u))
 return PI*s/intervals

rng=random.Random(560211)
N=2000
max_err=0
hits={6:0,8:0}
for k in range(N):
 n=[rng.gauss(0,1) for j in range(3)]
 n=unit(n)
 ss=sorted((abs(x) for x in n),reverse=True)
 if abs(ss[0]-ss[1]-ss[2])<0.00002: continue
 count,area=area_and_arcs(n)
 assert count==(8 if ss[0]>ss[1]+ss[2] else 6),(n,count,ss)
 hits[count]+=1
 if k<64:
  err=abs(area-area_midpoint(n,intervals=25000))
  max_err=max(max_err,err)
  assert err<3e-6,(n,area,err)
assert hits[6]>100 and hits[8]>100
# Measure independently with Haar random Gaussian normals; no reused formula in counting.
M=100000
freq=0
for k in range(M):
 n=unit([rng.gauss(0,1) for i in range(3)])
 s=sorted((abs(x) for x in n),reverse=True)
 freq+=int(s[0]>s[1]+s[2])
p_exact=12/PI*math.atan(3-2*math.sqrt(2))
p_emp=freq/M
assert abs(p_emp-p_exact)<0.012,(p_emp,p_exact)
print('passed',hits,'sampled 64 area comparisons with max absolute discrepancy',max_err)
print('Haar count Monte Carlo n=',M,'p8 observed',p_emp,'p8 exact',p_exact,'p6 exact',1-p_exact)
for n in [(1,1,1),(1,1,.15),(2,3,4),(1,2,10)]:
 print('normal',n,'arcs and elementary area:',area_and_arcs(n),'independent midpoint area:',area_midpoint(n,50000))
