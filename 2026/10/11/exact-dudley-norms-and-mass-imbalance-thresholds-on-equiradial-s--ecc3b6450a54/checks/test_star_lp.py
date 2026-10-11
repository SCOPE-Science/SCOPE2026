import numpy as np
from scipy.optimize import linprog
from random import Random
rng=Random(49271)
for n in [1,2,3,5,8]:
 for rho in [.1,.3,1,2,7,20]:
  for case in range(50):
   a=[rng.uniform(-3,3) for _ in range(n)]
   P=sum(max(v,0) for v in a);Q=sum(max(-v,0) for v in a)
   exact=max(rho/(1+rho)*(P+Q),2*rho/(2+rho)*max(P,Q))
   sz=n+3; A=[];b=[]
   for j in range(n+1):
    for sign in [1,-1]:
     row=[0.]*sz;row[j]=sign;row[-2]=-1;A.append(row);b.append(0.)
   for i in range(n+1):
    for j in range(i+1,n+1):
     for sign in [1,-1]:
      row=[0.]*sz;row[i]=sign;row[j]=-sign;row[-1]= -(rho if i==0 else 2*rho);A.append(row);b.append(0.)
   row=[0.]*sz;row[-2]=1;row[-1]=1;A.append(row);b.append(1.)
   c=[sum(a)]+[-v for v in a]+[0.,0.]
   r=linprog(c,A_ub=A,b_ub=b,bounds=[(None,None)]*(n+1)+[(0,None)]*2,method='highs')
   if not r.success or abs(-r.fun-exact)>1e-7: raise AssertionError((n,rho,a,exact,r.message,r.fun))
 print('PASS',n)
print('ALL scaled-star independent LP tests PASS')
