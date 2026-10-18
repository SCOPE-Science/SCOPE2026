from fractions import Fraction as F
from scipy.optimize import linprog
import random,math

def formula(mu,rho):
 m=len(rho);plus=[i for i,v in enumerate(mu[1:]) if v>0];minus=[i for i,v in enumerate(mu[1:]) if v<0]
 pts={(F(0),F(-1)),(F(0),F(1)),(F(1),F(0))}
 for i in plus:
  t=F(2)/(2+rho[i]);pts.add((t, -rho[i]*t/2))
 for i in minus:
  t=F(2)/(2+rho[i]);pts.add((t, rho[i]*t/2))
 for i in plus:
  for j in minus:
   t=F(2)/(2+rho[i]+rho[j]);pts.add((t,(rho[j]-rho[i])*t/2))
 best=(F(-100000),None)
 for t,c in pts:
  b=1-t
  val=mu[0]*c
  for i,u in enumerate(mu[1:]):
   if u>0:val+=u*min(b,c+rho[i]*t)
   elif u<0:val+=u*max(-b,c-rho[i]*t)
  if val>best[0]:best=(val,(t,c))
 return best

def zero_formula(mu,rho):
 plus=[i for i,v in enumerate(mu[1:]) if v>0];minus=[i for i,v in enumerate(mu[1:]) if v<0]
 xs=[F(0)]+[rho[i] for i in plus];ys=[F(0)]+[rho[i] for i in minus]
 return max(2*(sum(mu[i+1]*min(x,rho[i]) for i in plus)+sum(-mu[i+1]*min(y,rho[i]) for i in minus))/(2+x+y) for x in xs for y in ys)

def lp(mu,rho):
 m=len(rho);n=m+3; A=[];b=[]
 r=[0]*n;r[-2]=1;r[-1]=1;A.append(r);b.append(1)
 for i in range(m+1):
  for sign in (1,-1):
   r=[0]*n;r[i]=sign;r[-2]=-1;A.append(r);b.append(0)
 for i in range(m):
  for sign in (1,-1):
   r=[0]*n;r[i+1]=sign;r[0]=-sign;r[-1]=-rho[i];A.append(r);b.append(0)
 c=[-float(v) for v in mu]+[0,0]
 out=linprog(c,A_ub=A,b_ub=b,bounds=[(None,None)]*(m+1)+[(0,None),(0,None)],method='highs')
 assert out.success, out.message
 return -out.fun

r=random.Random(593)
for m in range(1,8):
 for k in range(150):
  rho=[F(r.randint(1,16),r.randint(1,9)) for _ in range(m)]
  mu=[F(r.randint(-12,12)) for _ in range(m+1)]
  f,pt=formula(mu,rho)
  l=lp(mu,rho)
  assert abs(float(f)-l)<1e-7,(rho,mu,f,pt,l)
  mu[0]=-sum(mu[1:]);f,pt=formula(mu,rho);z=zero_formula(mu,rho)
  assert f==z,(mu,rho,f,z)
  l=lp(mu,rho)
  assert abs(float(f)-l)<1e-7,(rho,mu,f,pt,l)
print('PASSED 2100 exact/general and zero-total LP comparisons; 1050 exact closed formula equivalences')
