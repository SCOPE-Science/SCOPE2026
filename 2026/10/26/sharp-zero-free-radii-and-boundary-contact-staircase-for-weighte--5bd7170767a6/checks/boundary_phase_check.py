import math
import numpy as np
from scipy.optimize import brentq

def predicted(p):
 k=1; maxima=0; tangent=0
 while 2*k < (p-1)/2:
  if abs(k-(p-1)/6)<1e-10: tangent+=1
  if k>(p-1)/6+1e-10:maxima+=1
  k+=1
 ang=p*math.pi/2
 cs=math.cos(ang)
 if abs(cs)>1e-11: tail=int(cs>0)
 else: tail=int(math.sin(ang)>0)
 return 2*maxima+tangent+tail, maxima,tangent,tail

def direct(p):
 # count at boundary x=1/2. H=cos(p th)/(cos th)^p
 # compute H with scaled form Q=cos(p th) - 2^(p-1)*cos(th)^p; at pi/2 sign of cos(p*pi/2) complicated for odd p -> p derivative.
 xs=np.linspace(0,math.pi/2-1e-10,40000)
 vals=np.cos(p*xs)-2**(p-1)*np.cos(xs)**p
 roots=[]
 for i in range(len(xs)-1):
  if vals[i]*vals[i+1]<0: roots.append(brentq(lambda t:math.cos(p*t)-2**(p-1)*math.cos(t)**p,xs[i],xs[i+1]))
 # exactly tangent
 for k in range(1,int((p-1)/4)+2):
  t=2*math.pi*k/(p-1)
  if 0<t<math.pi/2 and abs(math.cos(p*t)-2**(p-1)*math.cos(t)**p)<1e-7:
   if min([abs(r-t) for r in roots]or [100])>1e-5: roots.append(t)
 roots=sorted(roots)
 roots_unique=[]
 for rr in roots:
  if not roots_unique or abs(rr-roots_unique[-1])>1e-5: roots_unique.append(rr)
 return len(roots_unique),roots_unique

for p in [2,3,3.1,4,4.5,5,5.1,5.7,6,6.9,7,7.1,8,9,10,11,12,13,14,19,20,25,31,40,50]:
 a=predicted(p);b=direct(p)
 print(p,a,b[0],"OK" if a[0]==b[0] else 'MISMATCH')
 assert a[0]==b[0]

import random
random.seed(2040)
for z in range(150):
 p=random.uniform(1.02,50)
 if predicted(p)[0]!=direct(p)[0]: raise AssertionError((p,predicted(p),direct(p)))
print('150 deterministic random parameters PASS')

# Sharp inner radius monotonic comparison: Re f(r exp i theta) min always at theta=pi for r<=rho.
for p in [1.01,1.1,1.5,2,2.5,3,5,7,20,100]:
 rho=2**(1/p)-1
 assert p*rho<1+1e-13
 angs=np.linspace(0,math.pi,2501)
 for r in [rho*.3,rho*.7,rho]:
  val=np.real((1-r*np.exp(1j*angs))**(-p))
  assert val.min() >= (1+r)**(-p)-1e-9
print('inner zero-free checks PASS')

# Local tangency: the two roots at p=7-epsilon obey the square-root law.
from scipy.optimize import brentq
P=7.0
C=math.sqrt(2*math.pi*math.sqrt(3)/(3*P*(P-1)))
for eps in [1e-3,1e-4,1e-5]:
 p=P-eps
 f=lambda y:(0.25+y*y)**(p/2)*math.cos(p*math.atan2(y,0.5))-0.5
 xs=np.linspace(0.7,1.0,2001)
 rs=[brentq(f,x,y) for x,y in zip(xs[:-1],xs[1:]) if f(x)*f(y)<0]
 assert len(rs)==2
 assert max(abs((rs[0]-(math.sqrt(3)/2-C*math.sqrt(eps)))/eps),abs((rs[1]-(math.sqrt(3)/2+C*math.sqrt(eps)))/eps))<0.3
print('square-root boundary splitting PASS')
