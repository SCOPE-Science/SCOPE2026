from fractions import Fraction as F
from itertools import product,combinations

def solve(A,b):
 n=len(b)
 M=[[F(x) for x in row]+[F(v)] for row,v in zip(A,b)]
 for k in range(n):
  i=next((i for i in range(k,n) if M[i][k]),None)
  if i is None:return None
  M[i],M[k]=M[k],M[i]
  t=M[k][k];M[k]=[v/t for v in M[k]]
  for i in range(n):
   if i!=k and M[i][k]:
    t=M[i][k];M[i]=[u-t*v for u,v in zip(M[i],M[k])]
 return [r[-1] for r in M]

def bounds_formula(p,q):
 S=sum(p);y=S-q
 lo=max(F(0),2*q-S)
 f=lambda x:sum(min(v,x) for v in p)-x
 if not y:return lo,q
 breaks=sorted(set([F(0),q]+list(p)))
 for a,b in zip(breaks,breaks[1:]):
  fa,fb=f(a),f(b)
  if fa>=y:return lo,q-a
  if fb>=y:
   x=a+(b-a)*(y-fa)/(fb-fa)
   return lo,q-x
 raise AssertionError('no root')

def bounds_lp(p,q):
 d=len(p);atoms=list(product((0,1),repeat=d))
 col=[[F(1),F(int(any(a)))]+[F(v) for v in a] for a in atoms]
 eq=[F(1),q]+list(p)
 vals=[]
 for idx in combinations(range(2**d),d+2):
  sol=solve([[col[j][i] for j in idx] for i in range(d+2)],eq)
  if sol is not None and min(sol)>=0:
   vals.append(sum(x for j,x in zip(idx,sol) if sum(atoms[j])==1))
 assert vals, (p,q)
 return min(vals),max(vals)

if __name__=='__main__':
 count=0
 for p in product([F(0),F(1,4),F(1,2),F(3,4),F(1)],repeat=3):
  for q in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
   if max(p)<=q<=min(F(1),sum(p)):
    a=bounds_formula(p,q);b=bounds_lp(p,q)
    assert a==b,(p,q,a,b)
    count+=1
 print('Exact rational extremal LP comparisons:',count,'PASS')
 print('Asymmetry witness 1:',bounds_formula([F(9,10),F(9,10),F(1,10)],F(19,20)))
 print('Asymmetry witness 2:',bounds_formula([F(19,30)]*3,F(19,20)))
