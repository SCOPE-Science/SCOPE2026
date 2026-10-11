"""Independent finite global LP stress test of the local multiplier formula."""
import random
from itertools import product
from scipy.optimize import linprog
from fractions import Fraction
random.seed(24019)
count=0
for n in range(3,9):
 for t in range(120):
  d=[[0 if i==j else random.randint(1,8) for j in range(n)] for i in range(n)]
  for i in range(n):
   for j in range(i+1,n):d[i][j]=d[j][i]=min(d[i][j],d[j][i])
  for k in range(n):
   for i in range(n):
    for j in range(n): d[i][j]=min(d[i][j],d[i][k]+d[k][j])
  lamb=[0]+[random.randint(-3,3) for i in range(n-1)]
  rows=[];rhs=[]
  for i in range(n):
   for j in range(i+1,n):
    row=[(1 if k==i else -1 if k==j else 0) for k in range(1,n)]
    rows += [row,[-e for e in row]]
    rhs += [d[i][j]]*2
  truth=0
  for i in range(n):
   for j in range(i+1,n):
    row=[(lamb[i] if k==i else -lamb[j] if k==j else 0) for k in range(1,n)]
    for sign in (-1,1):
     res=linprog([-sign*e for e in row],A_ub=rows,b_ub=rhs,bounds=[(None,None)]*(n-1),method='highs')
     assert res.success
     truth=max(truth,-res.fun/d[i][j])
  predicted=max(abs(x) for x in lamb)
  for i in range(1,n):
   for j in range(i+1,n):
    a,b,c=d[0][i],d[0][j],d[i][j]
    x,y=lamb[i],lamb[j]
    predicted=max(predicted,abs(a*x-b*y)/c,abs(a*(x-y)+c*y)/c,abs(b*(x-y)-c*x)/c)
  assert abs(predicted-truth)<1e-8,(n,t,predicted,truth)
  count+=1
print('DIRAC_MULTIPLIER_GLOBAL_LP_OK',count)
