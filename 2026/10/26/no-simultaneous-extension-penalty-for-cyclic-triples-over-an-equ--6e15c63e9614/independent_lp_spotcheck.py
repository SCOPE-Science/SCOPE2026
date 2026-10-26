from fractions import Fraction as F
from scipy.optimize import linprog
import numpy as np
from cyclic_extension_checker import EXTREMES,matrix_dist,metric_ok
from itertools import combinations
samples=[((F(1,2),F(1,2),F(1,2)),F(1,2)),((F(1,2),F(3,5),F(13,20)),F(3,5)),((F(51,100),F(51,100),F(11,10)),F(4,5)),((F(1,2),F(3,5),F(9,10)),F(1,2)),((F(7,10),F(8,10),F(9,10)),F(9,10))]
for d,s in samples:
 assert metric_ok(d,s)
 rows=[];rhs=[]
 for f in EXTREMES:
  v=[]
  for i in range(3):
   ar=np.zeros(10); v.append((ar,float(f[i])))
  for i in range(3):
   ar=np.zeros(10);ar[3*i:3*i+3]=[float(x) for x in f];v.append((ar,0.0))
  for i,j in combinations(range(6),2):
   coef=v[i][0]-v[j][0]; const=v[i][1]-v[j][1]; dij=float(matrix_dist(i,j,d,s))
   for sign in [-1,1]:
    row=np.zeros(10);row[:9]=sign*coef[:9];row[9]=-dij
    rows.append(row);rhs.append(-sign*const)
 Aeq=np.zeros((3,10));Aeq[0,0:3]=1;Aeq[1,3:6]=1;Aeq[2,6:9]=1
 objective=np.zeros(10);objective[9]=1
 res=linprog(objective,A_ub=np.array(rows),b_ub=np.array(rhs),A_eq=Aeq,b_eq=[1]*3,bounds=[(None,None)]*9+[(1,None)],method='highs')
 assert res.success,res.message
 val=float(max(F(1),2/sum(d)))
 assert abs(res.fun-val)<1e-8,(d,s,res.fun,val)
 print('LP_OK',tuple(str(x) for x in d),str(s),res.fun)
