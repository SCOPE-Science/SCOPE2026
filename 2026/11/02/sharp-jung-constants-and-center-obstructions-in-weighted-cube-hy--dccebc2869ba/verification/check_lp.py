from scipy.optimize import linprog
from fractions import Fraction as F
import random
rnd=random.Random(1445)
checks=0
for n in range(2,10):
 for case in range(150):
  w=[rnd.choice([-1,1])*rnd.randint(0,6) for _ in range(n)]
  if not any(w):w[0]=1
  j=max(range(n),key=lambda i:abs(w[i])); pts=[]
  for k in range(2+rnd.randrange(5)):
   x=[rnd.randint(-6,6) for _ in range(n)]
   x[j]=-sum(w[i]*x[i] for i in range(n) if i!=j)/w[j]
   pts.append(x)
  c=[0.]*n+[1.]
  A=[];b=[]
  for x in pts:
   for i in range(n):
    z=[0.]*(n+1);z[i]=1;z[n]=-1; A.append(z);b.append(x[i])
    z=[0.]*(n+1);z[i]=-1;z[n]=-1;A.append(z);b.append(-x[i])
  res=linprog(c,A_ub=A,b_ub=b,A_eq=[[float(u) for u in w]+[0]],b_eq=[0.],bounds=[(None,None)]*n+[(0,None)],method='highs')
  assert res.success,(n,w,res.message)
  s=[1 if z>=0 else -1 for z in w]
  v=[[s[i]*z for i,z in enumerate(x)] for x in pts]
  ww=[abs(z) for z in w]
  M=[max(z[i] for z in v) for i in range(n)]
  m=[min(z[i] for z in v) for i in range(n)]
  W=sum(ww)
  d=max(M[i]-m[i] for i in range(n))
  formula=max(d/2,sum(ww[i]*M[i] for i in range(n))/W,-sum(ww[i]*m[i] for i in range(n))/W)
  assert abs(res.fun-formula)<1e-7,(n,w,res.fun,formula)
  checks+=1
print('PASS external LP independent,',checks,'instances')
