from fractions import Fraction as F
from bisect import bisect_left
import random

def profile(items):
 # items: (rho,positive-weight) positive rational
 agg={}
 for radius,weight in items:agg[radius]=agg.get(radius,F(0))+weight
 rr=sorted(agg);n=len(rr)
 xx=[F(0)]+rr
 tails=[];s=sum(agg.values(),F(0))
 pp=[F(0)]
 for k in range(n):
  tails.append(s)
  pp.append(pp[-1]+(rr[k]-xx[k])*s)
  s-=agg[rr[k]]
 assert s==0
 return xx,pp,tails

def optimal_piece(prof,threshold):
 xx,pp,tails=prof
 # first zero-or-negative slope, with tails descending. use manual binary search
 l=0;h=len(tails)
 while l<h:
  k=(l+h)//2
  if 2*tails[k]<=threshold:h=k
  else:l=k+1
 k=l
 return 2*pp[k]-threshold*xx[k]

def fast_dual(mu,rho):
 M=sum(mu);low=abs(M);high=sum(map(abs,mu));
 pos=profile([(rho[i],mu[i+1]) for i in range(len(rho)) if mu[i+1]>0])
 neg=profile([(rho[i],-mu[i+1]) for i in range(len(rho)) if mu[i+1]<0])
 def H(r):return optimal_piece(pos,M+r)+optimal_piece(neg,r-M)-2*r
 if high==low or H(low)<=0:return low
 breaks={low,high}
 for tail in pos[2]:
  v=2*tail-M
  if low<v<high:breaks.add(v)
 for tail in neg[2]:
  v=2*tail+M
  if low<v<high:breaks.add(v)
 breaks=sorted(breaks)
 # find first H(r)<=0; monotonic, binary-search over breakpoints
 l=0;h=len(breaks)-1
 assert H(breaks[l])>0 and H(breaks[h])<=0,(mu,rho,breaks,H(breaks[l]),H(breaks[h]))
 while h-l>1:
  mid=(l+h)//2
  if H(breaks[mid])>0:l=mid
  else:h=mid
 a=breaks[l];b=breaks[h];fa=H(a);fb=H(b)
 return a+(b-a)*fa/(fa-fb)

def grid_dual(mu,rho):
 m=len(rho);M=sum(mu);P=[i for i,v in enumerate(mu[1:]) if v>0];N=[i for i,v in enumerate(mu[1:]) if v<0]
 xs={F(0)}|{rho[i] for i in P};ys={F(0)}|{rho[i] for i in N}
 return max([abs(M)]+[(M*(y-x)+2*sum(mu[i+1]*min(x,rho[i]) for i in P)+2*sum(-mu[j+1]*min(y,rho[j]) for j in N))/(2+x+y) for x in xs for y in ys])

r=random.Random(34090)
for m in range(1,13):
 for t in range(400):
  rho=[F(r.randint(1,12),r.randint(1,10)) for _ in range(m)]
  mu=[F(r.randint(-40,40)) for _ in range(m+1)]
  a=grid_dual(mu,rho);b=fast_dual(mu,rho)
  assert a==b,(m,rho,mu,a,b)
print('PASS 4800 exact rational fast-root versus grid comparisons, with ties and signed masses')

# Verify that every selected finite candidate really has an attaining BL potential.
r2=random.Random(28493)
for m in range(1,13):
 for _ in range(100):
  rho=[F(r2.randint(1,9),r2.randint(1,8)) for i in range(m)]
  mu=[F(r2.randint(-8,8)) for i in range(m+1)]
  M=sum(mu)
  xs={F(0)}|{rho[i] for i in range(m) if mu[i+1]>0}
  ys={F(0)}|{rho[i] for i in range(m) if mu[i+1]<0}
  candidates=[]
  for x in xs:
   for y in ys:
    val=(M*(y-x)+2*sum(mu[i+1]*min(x,rho[i]) for i in range(m) if mu[i+1]>0)+2*sum(-mu[i+1]*min(y,rho[i]) for i in range(m) if mu[i+1]<0))/(2+x+y)
    candidates.append((val,x,y))
  val,x,y=max(candidates)
  if val<abs(M):
   potential=[F(1 if M>=0 else -1)]*(m+1)
   val=abs(M)
  else:
   t=F(2)/(2+x+y);b=F(1)-t;c=(y-x)/(2+x+y)
   potential=[c]
   for i,u in enumerate(mu[1:]):
    potential.append(min(b,c+rho[i]*t) if u>0 else max(-b,c-rho[i]*t) if u<0 else c)
  lip=max(abs(potential[i+1]-potential[0])/rho[i] for i in range(m))
  norm=max(map(abs,potential))+lip
  assert norm<=1,(rho,mu,potential,norm)
  assert sum(a*b for a,b in zip(mu,potential))==val,(rho,mu,potential,val)
  assert val==fast_dual(mu,rho)
print('PASS 1200 exact rational attaining-potential and norm-bound checks')
