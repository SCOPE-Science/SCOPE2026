"""Independent integer unit-pivot reduction of the Morse boundary."""
from VERIFY import enumerate_by_degree,greedy_matching,morse_complex
from functools import reduce
from math import gcd

def reduce_units(m):
 m=[[int(m[i,j]) for j in range(m.cols)] for i in range(m.rows)]
 nr=len(m);nc=len(m[0]);k=0
 while k<min(nr,nc):
  found=None
  for i in range(k,nr):
   for j in range(k,nc):
    if abs(m[i][j])==1:
     found=(i,j);break
   if found:break
  if not found:break
  i,j=found
  m[k],m[i]=m[i],m[k]
  for row in m:row[k],row[j]=row[j],row[k]
  pivot=m[k][k]
  for i in range(k+1,nr):
   t=m[i][k]//pivot
   if t:
    for j in range(k,nc):m[i][j]-=t*m[k][j]
  for j in range(k+1,nc):
   t=m[k][j]//pivot
   if t:
    for i in range(k,nr):m[i][j]-=t*m[i][k]
  k+=1
 return k, [row[k:] for row in m[k:]]

if __name__=='__main__':
 levels=enumerate_by_degree();pairs,c=greedy_matching(levels)
 _,B=morse_complex(pairs,c)
 k,a=reduce_units(B[3]);print('UNIT_PIVOTS',k,'RESIDUAL_SIZE',len(a),len(a[0]));print('RESIDUAL_ROW_SUPPORTS',[sum(x!=0 for x in row) for row in a]);
 assert k==40
 assert sum(any(row) for row in a)==1
 assert reduce(gcd,(abs(x) for row in a for x in row),0)==2
 print('INDEPENDENT_UNIMODULAR_REDUCTION=PASS')
