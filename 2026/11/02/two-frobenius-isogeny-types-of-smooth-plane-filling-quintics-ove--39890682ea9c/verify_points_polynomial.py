"""Independent polynomial-basis exact counts over GF(3^n), n=1,...,6.
Uses preselected monic irreducible polynomials, with field-law tests.
"""
from itertools import product
mons=sorted(((i,j,5-i-j) for i in range(6) for j in range(6-i)),reverse=True)
reps=[(432,[0,1,2,2,1,2,2,0,0,1,1,0,0,2,1,0,1,0,2,0,0]),(144,[0,1,2,2,1,2,2,0,0,1,1,1,0,1,1,0,1,0,2,0,0])]
def field(n):
 q=3**n; f={1:(0,1),2:(1,0,1),3:(1,0,2,1),4:(1,0,1,1,1),5:(1,0,0,0,2,1),6:(1,0,0,0,1,1,1)}[n]
 digs=[]
 for a in range(q):
  b=a;d=[]
  for _ in range(n):d.append(b%3);b//=3
  digs.append(d)
 pow3=[3**i for i in range(n)]
 def mul(a,b):
  if a==0 or b==0:return 0
  da=digs[a];db=digs[b];v=[0]*(2*n-1)
  for i in range(n):
   if da[i]:
    for j in range(n):v[i+j]+=da[i]*db[j]
  for k in range(2*n-2,n-1,-1):
   t=v[k]%3
   if t:
    for j in range(n):v[k-n+j]-=t*f[j]
  return sum((v[j]%3)*pow3[j] for j in range(n))
 M=[[mul(a,b) for b in range(q)] for a in range(q)]
 A=[[sum((da[i]+db[i])%3*pow3[i] for i in range(n)) for db in digs] for da in digs]
 P=[[1]*q for _ in range(6)]
 for d in range(1,6):P[d]=[M[P[d-1][a]][a] for a in range(q)]
 return q,f,M,A,P

def count(poly,ctx):
 q,f,M,A,P=ctx
 # affine z=1: fixed x, loop y and Horner in y
 n=0
 for a in range(q):
  cy=[0]*6
  for c,(i,j,k) in zip(poly,mons):
   if c:cy[j]=A[cy[j]][M[c][P[i][a]]]
  for b in range(q):
   v=cy[5]
   for j in range(4,-1,-1):v=A[M[v][b]][cy[j]]
   n+=(v==0)
 # infinity z=0, points [1:y:0] and [0:1:0]
 for b in range(q):
  v=0
  for c,(i,j,k) in zip(poly,mons):
   if c and k==0:v=A[v][M[c][P[j][b]]]
  n+=(v==0)
 v=next((c for c,(i,j,k) in zip(poly,mons) if j==5),0)
 n+=(v==0)
 return n

counts={str(size):[] for size,poly in reps}
for n in range(1,7):
 ctx=field(n)
 for size,poly in reps:counts[str(size)].append(count(poly,ctx))
 assert len(set(range(ctx[0])))==ctx[0]
 print('degree',n,'point_counts',{s:ns[-1] for s,ns in counts.items()},flush=True)
assert counts=={'144':[13,13,55,13,208,913],'432':[13,13,16,117,273,640]}
print('POLYNOMIAL_BASIS_COUNTS_OK')
