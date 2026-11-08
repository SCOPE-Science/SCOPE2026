import math,itertools
import numpy as np
from scipy.optimize import linprog

def formula(n):
 m=2*(n-1)
 a=math.sqrt((m-1)/m)
 c=math.sqrt((m-2)/(2*m))
 return 1/(2*(a+c))

def run(n):
 m=2*(n-1)
 a=math.sqrt((m-1)/m)
 A=[];B=[]
 for i in range(m):
  row=np.zeros(m+1);row[i]=-1;row[-1]=a;A.append(row);B.append(0)
  row=np.zeros(m+1);row[i]=1;row[-1]=a;A.append(row);B.append(1)
 for k in range(1,n-1):
  b=math.sqrt((2*k)*(m-2*k)/m)
  row=np.zeros(m+1);row[:2*k]=-1;row[-1]=b;A.append(row);B.append(-k)
 eq=np.zeros(m+1);eq[:m]=1
 obj=np.zeros(m+1);obj[-1]=-1
 sol=linprog(obj,A_ub=A,b_ub=B,A_eq=[eq],b_eq=[m/2],bounds=[(None,None)]*(m+1),method='highs')
 assert sol.success,sol.message
 expected=formula(n)
 assert abs(sol.x[-1]-expected)<2e-8,(n,sol.x[-1],expected)
 h=.5-a*expected
 z=np.array([h]*(m//2)+[-h]*(m//2))
 yy=z+.5
 assert np.max(np.array(A)@np.r_[yy,expected]-B)<1e-8
 return expected

for n in range(3,35): run(n)
# compare small n vertex set with direct Dyck enumeration: positive prefix halfspaces exactly characterize 0/1 Dyck incidence vectors
for n in range(3,9):
 m=2*n-2
 legit=[]
 for ups in itertools.combinations(range(m),n-1):
  y=np.zeros(m,dtype=int);y[list(ups)]=1
  good=all(sum(y[:2*k])>=k for k in range(1,n-1))
  orig=np.r_[1,y,0]
  good2=all(sum(orig[:j])>=math.ceil(j/2) for j in range(1,2*n+1))
  assert good==good2,(n,ups)
  if good:legit.append(ups)
 catalan=math.comb(2*n,n)//(n+1)
 assert len(legit)==catalan,(n,len(legit),catalan)
print('CATALAN_INRADIUS_ANALYTIC_LP_VERTEX_CHECKS_PASSED')
print('inradii',[(n,round(formula(n),10)) for n in [3,4,5,10,30,100,10000]])
