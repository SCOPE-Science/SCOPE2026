import numpy as np
from scipy.optimize import linprog

def check(m,n):
 N=m+n
 edges=[(i,j) for i in range(m) for j in range(i+1,m)]+[(i,m+u) for i in range(m) for u in range(n)]
 E=len(edges); d=N-1
 B=np.array([[int(v==a)-int(v==b) for a,b in edges] for v in range(d)],float)
 # vars K d*E, u E*E, t
 V=d*E+E*E+1
 A=[];rhs=[]
 for i in range(E):
  for j in range(E):
   for sig in (1,-1):
    row=np.zeros(V)
    row[np.arange(d)*E+j]=sig*B[:,i]
    row[d*E+i*E+j]=-1
    A.append(row);rhs.append(0)
 for j in range(E):
  row=np.zeros(V);row[d*E+np.arange(E)*E+j]=1;row[-1]=-1
  A.append(row);rhs.append(0)
 Aeq=[];beq=[]
 for i in range(d):
  for j in range(d):
   row=np.zeros(V)
   for k in range(E): row[i*E+k]=B[j,k]
   Aeq.append(row);beq.append(int(i==j))
 obj=np.zeros(V);obj[-1]=1
 res=linprog(obj,A_ub=np.array(A),b_ub=np.array(rhs),A_eq=np.array(Aeq),b_eq=np.array(beq),bounds=[(None,None)]*(d*E)+[(0,None)]*(E*E)+[(0,None)],method='highs')
 D=m*m+4*m*n-3*m+2*n*n-4*n+2
 predicted=2*(N-1)*(m*m+3*m*n-3*m-2*n+2)/(m*D)
 print(m,n,'LP',res.fun if res.success else res.message,'formula',predicted,'err',res.fun-predicted if res.success else None)
 assert res.success and abs(res.fun-predicted)<1e-8

for m,n in [(2,2),(3,2),(3,3),(4,2),(4,3)]: check(m,n)
