# Explicit enumeration of 1152 polarized automorphisms by point evaluation/interpolation, independent of generator-BFS.
import itertools,json,collections
from pathlib import Path
res=json.load(open(str(Path(__file__).resolve().parent / 'biquad3_results.json')));reps=[r for r in res if r['smooth']]
P=3; vec=((1,0),(0,1),(1,1));

def mm(a,b):return sum(x*y for x,y in zip(a,b))%3

def evalpoly(c,xx,yy):
 x=(xx[0]**2%3,xx[0]*xx[1]%3,xx[1]**2%3);y=(yy[0]**2%3,yy[0]*yy[1]%3,yy[1]**2%3)
 return sum(c[3*i+j]*x[i]*y[j] for i in range(3) for j in range(3))%3
V=[(x,y) for x in vec for y in vec]
mat=[]
for x,y in V:
 c=[0]*9
 for j in range(9):
  v=[0]*9;v[j]=1;c[j]=evalpoly(v,x,y)
 mat.append(c)
# Gaussian inverse mod3
aug=[a+[int(i==j) for j in range(9)] for i,a in enumerate(mat)]
for i in range(9):
 piv=next(t for t in range(i,9) if aug[t][i])
 aug[i],aug[piv]=aug[piv],aug[i]
 inv=pow(aug[i][i],-1,3);aug[i]=[k*inv%3 for k in aug[i]]
 for row in range(9):
  if row!=i:
   fac=aug[row][i];aug[row]=[(aug[row][k]-fac*aug[i][k])%3 for k in range(18)]
invm=[a[9:] for a in aug]
ms=[]
for a,b,c,d in itertools.product(range(3),repeat=4):
 if (a*d-b*c)%3:
  t=(a,b,c,d);t2=tuple(v*2%3 for v in t)
  if t>t2:continue
  ms.append(t)
assert len(ms)==24

def action(M,v):return ((M[0]*v[0]+M[1]*v[1])%3,(M[2]*v[0]+M[3]*v[1])%3)

def transform(code,A,B,swap):
 ds=[(code//(3**j))%3 for j in range(9)]
 vals=[]
 for xx,yy in V:
  if swap: xx,yy=yy,xx
  vals.append(evalpoly(ds,action(A,xx),action(B,yy)))
 out=[sum(invm[i][j]*vals[j] for j in range(9))%3 for i in range(9)]
 i=next(i for i,x in enumerate(out) if x)
 if out[i]==2:out=[2*x%3 for x in out]
 return sum(out[i]*3**i for i in range(9))
A=[]
for rep in reps:
 orb={transform(rep['mask'],m,n,t) for m in ms for n in ms for t in (0,1)}
 assert len(orb)==rep['size'],(rep['mask'],len(orb),rep['size'])
 assert min(orb)==rep['mask'],(rep['mask'],min(orb))
 A.append(orb)
for i in range(len(A)):
 for j in range(i):assert not(A[i]&A[j])
assert sum(map(len,A))==5184
print('CHECK_OK','GL2_projective',len(ms),'ambient_group',1152,'smooth_orbits',len(A),'total_smooth',sum(map(len,A)))
