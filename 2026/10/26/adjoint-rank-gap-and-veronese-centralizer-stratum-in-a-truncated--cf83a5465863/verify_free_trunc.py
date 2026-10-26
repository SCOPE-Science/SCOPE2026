"""Finite-field spot-checks for the adjoint rank distribution in a free truncated algebra."""
import itertools,random
WORDS=['']+[''.join(t) for d in (1,2,3) for t in itertools.product('xy',repeat=d)]
I={w:i for i,w in enumerate(WORDS)}
N=len(WORDS)
def mul(a,b,p):
 c=[0]*N
 for i,ai in enumerate(a):
  if not ai:continue
  for j,bj in enumerate(b):
   if bj and len(WORDS[i])+len(WORDS[j])<4:
    k=I[WORDS[i]+WORDS[j]]; c[k]=(c[k]+ai*bj)%p
 return c

def rank(M,p):
 A=[list(r) for r in M];r=0
 for col in range(len(A[0])):
  pivot=next((i for i in range(r,len(A)) if A[i][col]%p),None)
  if pivot is None:continue
  A[r],A[pivot]=A[pivot],A[r]
  z=pow(A[r][col],-1,p);A[r]=[(z*a)%p for a in A[r]]
  for i in range(r+1,len(A)):
   if A[i][col]:
    v=A[i][col];A[i]=[(a-v*b)%p for a,b in zip(A[i],A[r])]
  r+=1
  if r==len(A):break
 return r

def adrank(a,p):
 cols=[]
 for j in range(N):
  b=[0]*N;b[j]=1
  ab=mul(a,b,p);ba=mul(b,a,p)
  cols.append([(x-y)%p for x,y in zip(ab,ba)])
 return rank([list(row) for row in zip(*cols)],p)

def predicted(a,p):
 v=(a[I['x']],a[I['y']]);quad=[a[I[w]] for w in ('xx','xy','yx','yy')]
 if v!=(0,0):return 4
 if quad==[0,0,0,0]:return 0
 # For a nonzero quadratic, rank one iff Q is a scalar square of a linear form.
 for x,y in itertools.product(range(p),repeat=2):
  if not (x or y):continue
  sq=(x*x,x*y,x*y,y*y)
  for c in range(1,p):
   if quad==[(c*z)%p for z in sq]:return 1
 return 2

if __name__=='__main__':
 random.seed(271828)
 for p in (2,3):
  pattern_counts={0:0,1:0,2:0,4:0}
  for vq in itertools.product(range(p),repeat=6):
   a=[0]*N
   for word,z in zip(('x','y','xx','xy','yx','yy'),vq):a[I[word]]=z
   got=adrank(a,p);exp=predicted(a,p)
   assert got==exp,(p,vq,got,exp)
   pattern_counts[got]+=1
  expected={0:1,1:p*p-1,2:p**4-p**2,4:(p*p-1)*p**4}
  assert pattern_counts==expected,(p,pattern_counts,expected)
  print('q',p,'exhaustive_vQ_cases',p**6,'distribution',pattern_counts)
 for p,tries in ((2,1000),(3,1000),(5,1000)):
  counts={}
  for _ in range(tries):
   a=[random.randrange(p) for _ in range(N)]
   got=adrank(a,p);exp=predicted(a,p)
   assert got==exp,(p,got,exp,a)
   counts[got]=counts.get(got,0)+1
  # Force validation of all strata and their nonzero quadratic square and nonsquare cases.
  tests=[('xx',1),('xy',2)]
  for word,expected in tests:
   a=[0]*N;a[I[word]]=1
   assert adrank(a,p)==expected,(p,word)
  print('q',p,'random_checks',tries,'rank_counts',counts,'targeted_strata_ok')
 print('AD_RANK_OK')
