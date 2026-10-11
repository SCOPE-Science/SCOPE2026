from fractions import Fraction
from itertools import product
import numpy as np
from scipy.optimize import linprog

def discrepancy(aa):
 return min(abs(sum(s*a for s,a in zip(sign,aa))) for sign in product((-1,1), repeat=len(aa)))

def lpmin(aa):
 n=len(aa); val=float('inf')
 for sign in product((-1,1),repeat=n):
  # vars q_i, z_i, t: z_i >= |a_i-q_i|; sum q=1; t >= plus, minus
  A=[];b=[]
  for i,a in enumerate(aa):
   row=[0.]*(2*n+1);row[i]=1;row[n+i]=-1;A.append(row);b.append(a)
   row=[0.]*(2*n+1);row[i]=-1;row[n+i]=-1;A.append(row);b.append(-a)
  for k in (+1,-1):
   row=[0.]*(2*n+1);row[-1]=-1
   for i,s in enumerate(sign):
    if k*s==1:row[i]=1
    else:row[n+i]=1
   A.append(row);b.append(-sum(aa[i] for i,s in enumerate(sign) if k*s==1))
  eq=[[1.]*n+[0.]*(n+1)];c=[0.]*(2*n)+[1.]
  r=linprog(c,A_ub=A,b_ub=b,A_eq=eq,b_eq=[1.],bounds=[(0,None)]*(2*n)+[(0,None)],method='highs')
  if not r.success:raise RuntimeError(r.message)
  val=min(val,r.fun)
 return val

if __name__=='__main__':
 k=0
 for n in range(2,7):
  for t in range(10):
   raw=np.random.default_rng(1000+n*100+t).integers(0,9,size=n)
   if not sum(raw):continue
   a=[float(v/sum(raw)) for v in raw]
   predicted=1+discrepancy(a)
   attained=lpmin(a)
   assert abs(attained-predicted)<1e-7,(a,attained,predicted)
   k+=1
 print('STRESS_OK rational_samples=',k,' n=2..6 LP sign orthants checked exact_formula=True')
