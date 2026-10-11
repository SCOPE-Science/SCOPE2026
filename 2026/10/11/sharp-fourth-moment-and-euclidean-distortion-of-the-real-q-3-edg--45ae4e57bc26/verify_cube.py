"""Exhaustive exact certificate for cube-face edge quadratic inequality."""
from itertools import product, combinations
from fractions import Fraction as F
vertices=list(product((0,1),repeat=3))
edges=[(i,j) for i,a in enumerate(vertices) for j,b in enumerate(vertices) if i<j and sum(x!=y for x,y in zip(a,b))==1]
assert len(edges)==12
faces=[]
for axis in range(3):
 for bit in (0,1):
  u={i for i,v in enumerate(vertices) if v[axis]==bit}
  face=[k for k,(i,j) in enumerate(edges) if i in u and j in u]
  assert len(face)==4
  faces.append(face)
A=[[0]*12 for _ in range(12)]
for face in faces:
 for i in face:
  for j in face:
   if i!=j:A[i][j]=1
M=[[3 if i==j else (-1 if A[i][j] else 1) for j in range(12)] for i in range(12)]
def candidate(S):
 if len(S)==1:return True,F(3),[F(1)]
 k=len(S)-1; t=S[-1]
 H=[[F(M[S[i]][S[j]]-M[S[i]][t]-M[t][S[j]]+M[t][t]) for j in range(k)] for i in range(k)]
 h=[F(M[S[i]][t]-M[t][t]) for i in range(k)]
 # exact LDL decomposition H=LDL^T: positivity test 
 L=[[F(int(i==j)) for j in range(k)] for i in range(k)]
 D=[F(0)]*k
 for j in range(k):
  D[j]=H[j][j]-sum(L[j][r]*L[j][r]*D[r] for r in range(j))
  if D[j]<=0:return False,None,None
  for i in range(j+1,k):
   L[i][j]=(H[i][j]-sum(L[i][r]*L[j][r]*D[r] for r in range(j)))/D[j]
 # solve Hx=-h by exact triangular factors
 y=[F(0)]*k
 for i in range(k):y[i]=-h[i]-sum(L[i][j]*y[j] for j in range(i))
 z=[y[i]/D[i] for i in range(k)]
 x=[F(0)]*k
 for i in reversed(range(k)):x[i]=z[i]-sum(L[j][i]*x[j] for j in range(i+1,k))
 b=x+[F(1)-sum(x)]
 value=sum(b[i]*b[j]*M[S[i]][S[j]] for i in range(k+1) for j in range(k+1))
 return True,value,b
count=0;positive=0;minvalue=F(10**10);zeros=[];fail=[];skipped=0
for k in range(1,13):
 for S in combinations(range(12),k):
  pd,val,b=candidate(S)
  if not pd:
   skipped+=1;continue
  count+=1
  if all(x>0 for x in b):
   positive+=1
   if val <minvalue:minvalue=val
   if val==0:zeros.append(S)
   if val<0:fail.append((S,val,b))
 print('k',k,'pass_so_far',count, 'supported',positive)
print('CERTIFICATE:', 'candidate_PDs',count,'skipped',skipped,'positive_stationary',positive,'minimum',minvalue,'zero_supports',len(zeros),'failures',len(fail));print('zero supports',zeros)
assert not fail and minvalue==0
assert set(zeros)=={tuple(sorted(f)) for f in faces}
# On each face: unique strictly positive stationary vector is uniform;
# different face supports have strictly positive mixed quadratic form.
for f in faces:
 pd,v,b=candidate(sorted(f))
 assert pd and v==0 and b==[F(1,4)]*4
for f,g in combinations(faces,2):
 z=sum(F(M[i][j],16) for i in f for j in g)
 assert z>0
print('FACE_RIGIDITY_OK')
# Exact fourth-power identity check as polynomial over all 12 edge coefficients:
from collections import Counter
terms=Counter()
for quad in combinations(range(12),4):
 xored=[0]*8
 for edge in quad:
  i,j=edges[edge];xored[i]^=1;xored[j]^=1
 if not any(xored):terms[tuple(quad)]+=24
assert len(terms)==6
assert {tuple(sorted(f)) for f in faces}==set(terms)
# Check the complete quartic identity coefficient-by-coefficient, not just its distinct-edge term.
from itertools import combinations_with_replacement
from math import factorial
mon=Counter()
for inds in combinations_with_replacement(range(12),4):
 parity=[0]*8
 for edge in inds:
  u,v=edges[edge];parity[u]^=1;parity[v]^=1
 if not any(parity):
  counts=Counter(inds)
  mon[inds]+=factorial(4)//__import__('math').prod(factorial(k) for k in counts.values())
left=Counter()
for i in range(12):left[(i,)*4]+=4
for i,j in combinations(range(12),2):left[(i,i,j,j)]+=8
for k,v in mon.items():left[k]-=v
right=Counter()
for i in range(12):right[(i,)*4]+=M[i][i]
for i,j in combinations(range(12),2):right[(i,i,j,j)]+=2*M[i][j]
for face in faces:
 for a,b in ((0,1),(0,2),(0,3)):
  c,d=[q for q in range(4) if q not in (a,b)]
  i,j=sorted((face[a],face[b]))
  k,l=sorted((face[c],face[d]))
  right[(i,i,j,j)]+=4
  right[(k,k,l,l)]+=4
  right[tuple(sorted(face))]-=8
assert all(left[k]==right[k] for k in set(left)|set(right))
print('QUARTIC_COEFFICIENT_IDENTITY_OK')
print('EXACT_CUBE_CERTIFICATE_OK')
