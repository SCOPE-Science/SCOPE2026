from fractions import Fraction as F
from itertools import product
from collections import defaultdict
from math import prod

def circle(a,b,n):
 d=abs(a-b)%n;return min(d,n-d)

def edges(m,n):
 return [('H',i,j,((i,j),((i+1)%m,j))) for i in range(m) for j in range(n)]+ [('V',i,j,((i,j),(i,(j+1)%n))) for i in range(m) for j in range(n)]

def clip(poly,c,a,b):  # retain c+a*x+b*y >= 0
 if not poly:return []
 out=[]
 for u,v in zip(poly,poly[1:]+poly[:1]):
  fu=c+a*u[0]+b*u[1];fv=c+a*v[0]+b*v[1]
  if fu>=0:out.append(u)
  if (fu<0 and fv>0) or (fu>0 and fv<0):
   r=fu/(fu-fv);out.append((u[0]+r*(v[0]-u[0]),u[1]+r*(v[1]-u[1])))
 # remove duplicates optional
 return out

def area(poly):
 if len(poly)<3:return F(0)
 return abs(sum(u[0]*v[1]-u[1]*v[0] for u,v in zip(poly,poly[1:]+poly[:1])))/2

def moment(poly):
 if len(poly)<3:return (F(0),F(0),F(0))
 twice=sum(u[0]*v[1]-u[1]*v[0] for u,v in zip(poly,poly[1:]+poly[:1]))
 if twice==0:return F(0),F(0),F(0)
 orientation=1 if twice>0 else -1
 A=orientation*twice/2
 sx=orientation*sum((u[0]+v[0])*(u[0]*v[1]-u[1]*v[0]) for u,v in zip(poly,poly[1:]+poly[:1]))/6
 sy=orientation*sum((u[1]+v[1])*(u[0]*v[1]-u[1]*v[0]) for u,v in zip(poly,poly[1:]+poly[:1]))/6
 return A,sx,sy

def pieces(e,f,m,n):
 if e==f:return []
 a,b=e[3];c,d=f[3]
 dist=lambda p,q:circle(p[0],q[0],m)+circle(p[1],q[1],n)
 terms=[(F(dist(a,c)),F(1),F(1)),(F(1+dist(a,d)),F(1),F(-1)),(F(1+dist(b,c)),F(-1),F(1)),(F(2+dist(b,d)),F(-1),F(-1))]
 pieces=[]
 for i,term in enumerate(terms):
  poly=[(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(0),F(1))]
  for j,other in enumerate(terms):
   if i!=j:
    poly=clip(poly,other[0]-term[0],other[1]-term[1],other[2]-term[2])
    if not poly:break
  if poly and area(poly):pieces.append((term,poly))
 return pieces

def direct_cdf(t):
 return F(0) if t<=0 else (2*t-t*t if t<1 else F(1))

def cplus(t):return F(0) if t<=0 else (t*t if t<1 else F(1))
def cminus(t):return F(0) if t<=0 else (2*t-t*t if t<1 else F(1))
def Ucdf(t,a):return max(F(0),min(F(1),t/a))
def sumU(t,a,b):
 return (max(F(0),t)**2-max(F(0),t-a)**2-max(F(0),t-b)**2+max(F(0),t-a-b)**2)/(2*a*b)
def cv(k,N):return min(k,N-k)
def predicted_cdf(t,m,n):
 a=F(m,2);b=F(n,2)
 base=sumU(t,a,b)/2 + sum(Ucdf(t-cv(j,n),a) for j in range(n))/F(4*n) + sum(Ucdf(t-cv(i,m),b) for i in range(m))/F(4*m)
 corr=(sum(cplus(t-cv(j,n))-cminus(t-cv(j,n)) for j in range(1,n)) +sum(cplus(t-cv(i,m))-cminus(t-cv(i,m)) for i in range(1,m)))/F(4*m*n)
 return base+corr

def predicted_mean(m,n):
 x=F(m+n,4)+F(m+n-2,12*m*n)
 if m%2:x-=F(1,16*m)
 if n%2:x-=F(1,16*n)
 return x

if __name__=='__main__':
 tests=0
 for m,n in [(3,3),(3,4),(3,5),(4,4),(4,5),(5,5),(6,4)]:
  ee=edges(m,n);M=len(ee)
  moments=F(0);counts=defaultdict(F)
  tlist=[F(1,5),F(1,2),F(1),F(4,3),F(3,2),F(2),F(5,2),F(3),F(7,2),F(4),F(9,2),F(5)]
  for e,f in product(ee,repeat=2):
   if e==f:
    moments+=F(1,3)
    for t in tlist:counts[t]+=direct_cdf(t)
    continue
   for (c,a,b),p in pieces(e,f,m,n):
    aa,sx,sy=moment(p)
    moments+=c*aa+a*sx+b*sy
    for t in tlist:
     pol=clip(p,t-c,-a,-b)
     counts[t]+=area(pol)
  actual=moments/(M*M)
  assert actual==predicted_mean(m,n),(m,n,actual,predicted_mean(m,n))
  tests+=1
  for t in tlist:
   actual=counts[t]/(M*M)
   pred=predicted_cdf(t,m,n)
   assert actual==pred,(m,n,t,actual,pred)
   tests+=1
  print('PASS',m,n,'exact mean',predicted_mean(m,n),'CDF thresholds',len(tlist))
 print('TOTAL independent analytic polytope integration comparisons',tests)
