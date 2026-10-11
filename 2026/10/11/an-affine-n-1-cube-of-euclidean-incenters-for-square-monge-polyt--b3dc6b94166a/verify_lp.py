import numpy as np, math
from scipy.optimize import linprog
for n in range(2,12):
 N=n*n;alpha=math.sqrt((N-1)/N);T=N*(N-1)/12;r=1/(N*alpha+2*T)
 A=[];b=[]
 for k in range(N):
  v=np.zeros(N+1);v[k]=-1;v[N]=alpha;A.append(v);b.append(0.)
 for i in range(n-1):
  for j in range(n-1):
   v=np.zeros(N+1);v[i*n+j]=1;v[(i+1)*n+j+1]=1;v[i*n+j+1]=-1;v[(i+1)*n+j]=-1;v[N]=2;A.append(v);b.append(0.)
 obj=np.zeros(N+1);obj[N]=-1
 eq=np.zeros(N+1);eq[:N]=1
 z=linprog(obj,A_ub=A,b_ub=b,A_eq=[eq],b_eq=[1],bounds=[(None,None)]*N+[(0,None)],method='highs')
 assert z.success,(n,z.message)
 assert abs(z.x[-1]-r)<2e-8,(n,z.x[-1],r)
 # check predicted cube center with delta=0.3 for all k
 u=np.arange(n)[::-1]*.3
 DD=np.array([[(j-i)*(j-i-1)/2+u[i]-u[j] for j in range(n)] for i in range(n)])
 CC=r*(alpha+2*DD)
 assert abs(CC.sum()-1)<1e-10
 assert CC.min()>=alpha*r-1e-10
 for i in range(n-1):
  for j in range(n-1):
   assert abs(CC[i,j+1]+CC[i+1,j]-CC[i,j]-CC[i+1,j+1]-2*r)<2e-10
 if n<=7:
  # check each delta_i achieves boundary values 0 and 1 independently via LP at optimal radius
  eq2=np.zeros(N+1);eq2[N]=1
  for i in range(n-1):
   d=np.zeros(N+1);d[(i)*n+i+1]=1
   for sign,expect in [(1,alpha*r),(-1,(alpha+2)*r)]:
    v=linprog(sign*d,A_ub=A,b_ub=b,A_eq=[eq,eq2],b_eq=[1,r],bounds=[(None,None)]*N+[(0,None)],method='highs')
    assert v.success,(n,i,sign,v.message)
    assert abs(v.x[(i)*n+i+1]-expect)<2e-8,(n,i,sign,v.x[(i)*n+i+1],expect)
 print(f'n={n} N={N} T={T:g} radius={r:.10f} cube_dim={n-1} OK')
