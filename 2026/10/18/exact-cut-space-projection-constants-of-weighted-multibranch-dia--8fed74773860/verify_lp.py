import numpy as np
from scipy.optimize import linprog

def solve_cut(weights):
 m=len(weights);n=2*m;k=m-1
 cmat=np.zeros((k,n))
 for j in range(k):
  cmat[j,2*j:2*j+2]=.5
  cmat[j,2*k:2*k+2]=-.5
 w=np.repeat(weights,2)
 Nu=n*k;Na=n*n; N=Nu+Na+1;tidx=N-1
 # index (row i, rank factor a) of U and |Pij|
 idxU=lambda i,a:i*k+a
 idxAbs=lambda i,j:Nu+i*n+j
 eq=[];rhs=[]
 for a in range(k):
  for b in range(k):
   row=np.zeros(N)
   for i in range(n):row[idxU(i,b)]+=cmat[a,i]
   eq.append(row);rhs.append(float(a==b))
 ub=[];ubrhs=[]
 for i in range(n):
  for j in range(n):
   # P_ij = δ_ij - Σ_a U_ia C_aj 
   row=np.zeros(N)
   for a in range(k):row[idxU(i,a)]-=cmat[a,j]
   row[idxAbs(i,j)]-=1
   ub.append(row);ubrhs.append(-float(i==j))
   row=np.zeros(N)
   for a in range(k):row[idxU(i,a)]+=cmat[a,j]
   row[idxAbs(i,j)]-=1
   ub.append(row);ubrhs.append(float(i==j))
 for j in range(n):
  row=np.zeros(N);row[tidx]=-1
  for i in range(n): row[idxAbs(i,j)]=w[i]/w[j]
  ub.append(row);ubrhs.append(0)
 cost=np.zeros(N);cost[tidx]=1
 bounds=[(None,None)]*Nu + [(0,None)]*Na +[(0,None)]
 res=linprog(cost,A_ub=np.array(ub),b_ub=np.array(ubrhs),A_eq=np.array(eq),b_eq=np.array(rhs),bounds=bounds,method='highs')
 if not res.success:raise RuntimeError(res.message)
 return res.fun

def proposed(w):
 W=sum(w);return 1+1/sum(v/(W-v) for v in w)

if __name__=='__main__':
 import random
 random.seed(12)
 for m in range(2,7):
  for t in range(10):
   w=[random.randint(1,12)/random.randint(1,5) for _ in range(m)]
   v1=solve_cut(w);v2=proposed(w)
   print(m,w,round(v1,10),round(v2,10),'difference',abs(v1-v2))
   assert abs(v1-v2)<1e-8
 print('PASS')
