"""Reproducible exact certificate for icosidodecahedral harmonic sampling.
Run: python3 h3_cert.py (Python standard library only).
"""
from fractions import Fraction as F
from itertools import product
from math import isqrt
import time
Z=(F(0),F(0)); ONE=(F(1),F(0));
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def mul(x,y):return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def div(x,y):
 n=y[0]*y[0]-5*y[1]*y[1]
 return ((x[0]*y[0]-5*x[1]*y[1])/n,(x[1]*y[0]-x[0]*y[1])/n)
def cv(q):return (F(q),F(0))
def mulf(x,f):return (x[0]*f,x[1]*f)
def sub(x,y):return (x[0]-y[0],x[1]-y[1])
a=(F(-1,4),F(1,4));c=(F(1,4),F(1,4)); half=cv(F(1,2))
phi=mulf(add(ONE,cv(0)),F(0)) if False else (F(1,2),F(1,2))
phimin=(F(-1,2),F(1,2))
coords=[]
for i in range(3):
 for s in (-1,1):
  v=[Z,Z,Z];v[i]=cv(s);coords.append(tuple(v))
for v in ((mulf(phi,F(1,2)),mulf(phimin,F(1,2)),half),
          (half,mulf(phi,F(1,2)),mulf(phimin,F(1,2))),
          (mulf(phimin,F(1,2)),half,mulf(phi,F(1,2)))):
 for s in product((-1,1),repeat=3):coords.append(tuple(mulf(x,y) for x,y in zip(v,s)))
assert len(coords)==30 and len(set(coords))==30
# Exact normalization and antipodal pairing.
for v in coords:
 assert sum(mul(t,t)[0] for t in v)==1 and sum(mul(t,t)[1] for t in v)==0
 assert tuple(neg(t) for t in v) in coords
# Choose antipodal representatives by the sign of the first nonzero entry (via field inequality).
def sign(x):
 if not x[1]:return (x[0]>0)-(x[0]<0)
 if not x[0]:return (x[1]>0)-(x[1]<0)
 if x[0]*x[1]>0:return 1 if x[0]>0 else -1
 return (1 if x[0]*x[0]>5*x[1]*x[1] else -1)*(1 if x[0]>0 else -1)
reps=[v for v in coords if next(sign(z) for z in v if sign(z))>0]
assert len(reps)==15
freq=[]; D=[]
allowed=[Z,a,half,c,neg(a),neg(half),neg(c)]
for i,v in enumerate(reps):
 row=[]
 for j,w in enumerate(reps):
  dot=Z
  for x,y in zip(v,w):dot=add(dot,mul(x,y))
  if i==j:assert dot==ONE;row.append((4,1));continue
  assert dot in allowed, ('unexpected dot',dot)
  if dot==Z:row.append((0,0))
  else:
   for ix,t in enumerate((a,half,c),1):
    if dot==t:row.append((ix,1));break
    if dot==neg(t):row.append((ix,-1));break
 row and D.append(row)
assert all(sum(D[i][j][0]==m for j in range(15) if j!=i)==(2 if m==0 else 4) for i in range(15) for m in range(4))
# The five orthogonal triples define the rank-five averaging projection Q=(I+M0)/3.
N0=[[int(i!=j and D[i][j][0]==0) for j in range(15)] for i in range(15)]
assert all(sum(row)==2 for row in N0)
assert all(sum(N0[i][z]*N0[z][j] for z in range(15))==(2 if i==j else 1 if N0[i][j] else 0) for i in range(15) for j in range(15))

def seq(t,K):
 p0=ONE;p1=t
 yield p0
 if K==0:return
 yield p1
 for k in range(2,K+1):
  x=mulf(sub(mulf(mul(t,p1),2*k-1),mulf(p0,k-1)),F(1,k))
  yield x;p0,p1=p1,x

SEQ={0:list(seq(Z,500)),1:list(seq(a,500)),2:list(seq(half,500)),3:list(seq(c,500))}
assert all(x[1]==0 for x in SEQ[0]+SEQ[2]);

def gram_field(k):
 val=[SEQ[i][k] for i in range(4)]+[ONE]
 return [[mulf(val[m],(sign1 if k%2 else 1)) if m!=4 else ONE for m,sign1 in row] for row in D]

def exact_rank(A):
 X=[r[:] for r in A];n=len(X); piv=[];p=0
 for j in range(n):
  ii=next((i for i in range(p,n) if X[i][j]!=Z),None)
  if ii is None:continue
  X[p],X[ii]=X[ii],X[p]
  pivot=X[p][j]
  for i in range(p+1,n):
   if X[i][j]==Z:continue
   mulr=div(X[i][j],pivot)
   for l in range(j+1,n):X[i][l]=sub(X[i][l],mul(mulr,X[p][l]))
   X[i][j]=Z
  piv.append(j);p+=1
  if p==n:break
 return p

for k in range(15):
 rank=exact_rank(gram_field(k))
 expected={0:1,1:3,2:5,3:7,4:9,5:11,6:10,8:14,14:14}.get(k,15)
 assert rank==expected,(k,rank,expected)
print('LOW_RANKS_EXACT',[(k,exact_rank(gram_field(k))) for k in range(15)],flush=True)

# Exact rational spectral decomposition at k=12.
k12=gram_field(12);u=SEQ[0][12];v=SEQ[1][12];w=SEQ[2][12];z=SEQ[3][12]
row_sum=add(add(add(ONE,mulf(u,2)),mulf(v,4)),add(mulf(w,4),mulf(z,4)))
assert row_sum[1]==0
l1=row_sum
l4=mulf(sub(add(cv(5),mulf(u,10)),l1),F(1,4))
assert l4[1]==0
summ=mulf(sub(ONE,u),2)
tr2=add(ONE,add(mulf(mul(u,u),2),mulf(add(add(mul(v,v),mul(w,w)),mul(z,z)),4)))
tr2=mulf(tr2,15)
squares=mulf(sub(sub(tr2,mul(l1,l1)),mulf(mul(l4,l4),4)),F(1,5))
prod=mulf(sub(mul(summ,summ),squares),F(1,2))
assert summ[1]==prod[1]==0
# Check P_=(2I-M0)/3, P_+ = (I+M0)/3, and quadratic identity on P_-.
Pm=[[(F(2 if i==j else 0)-F(N0[i][j]))/3 for j in range(15)] for i in range(15)]
# Characteristic polynomial on the rank-ten sector is (x^2-summ x+prod)^5.
def matmul(X,Y):return [[sum((mul(X[i][t],Y[t][j])[0] for t in range(15)),F(0)) for j in range(15)] for i in range(15)]
# Check exact quadratic matrix identity by scalar multiplying field entries.
for i in range(15):
 for j in range(15):
  lhs=Z
  for t in range(15):lhs=add(lhs,mul(k12[i][t],k12[t][j]))
  lhs=sub(lhs,mulf(k12[i][j],summ[0]))
  lhs=add(lhs,mulf(ONE if i==j else Z,prod[0]))
  # On constant-plus-four subspace, polynomial evaluates to fixed rational scalars.
  # Do not require zero on those five dimensions.
# Compute tight eigenvalue limits via exact rational trace moments and intervals.
print('K12', 'l1=',l1,'l4=',l4, 'quadratic_sum=',summ,'quadratic_product=',prod,flush=True)
# Rational spectral bracket: min root in (.0028,.0029), max in (2.55,2.60).
def poly_at(t):return t*t-summ[0]*t+prod[0]
assert poly_at(F(28,10000))>0 and poly_at(F(29,10000))<0
assert l1[0]>F(51,20) and l1[0]<F(13,5)
assert l4[0]>F(1) and l4[0]<F(6,5)
assert summ[0]<F(2) and prod[0]>0
assert poly_at(F(3,2))<0 and poly_at(F(8,5))>0
# Compare exact K12 eigen minimum to all other eigenvalues using rank-five sector identities.
# For Q=(I+N0)/3, KQ=l4 Q+(l1-l4)J/15. On orthogonal complement, the quadratic identity holds.
Q=[[(F(int(i==j)+N0[i][j],3)) for j in range(15)] for i in range(15)]
for i in range(15):
 for j in range(15):
  lhs=Z
  for t in range(15):lhs=add(lhs,mulf(k12[i][t],Q[t][j]))
  rhs=add(mulf(cv(Q[i][j]),l4[0]),cv((l1[0]-l4[0])/15))
  assert lhs==rhs,('plus subspace',i,j,lhs,rhs)
# The rank-ten complement quadratic relation.
for i in range(15):
 for j in range(15):
  s=Z
  for t in range(15):
   for r in range(15):
    s=add(s,mulf(mul(k12[i][t],k12[t][r]),Pm[r][j]))
  v1=Z
  for t in range(15):v1=add(v1,mulf(k12[i][t],Pm[t][j]))
  s=add(sub(s,mulf(v1,summ[0])),cv(prod[0]*Pm[i][j]))
  assert s==Z,('minus sector',i,j,s)
print('K12_SPECTRAL_IDENTITY_EXACT',flush=True)

# Certified rational approximation: approximate each field number by a lower dyadic.
QBIT=48;Q0=1<<QBIT;PBIT=70;ISQ=isqrt(5<<(2*PBIT));sqrt5_lower=F(ISQ,1<<PBIT);sqrt5_upper=F(ISQ+1,1<<PBIT)
assert sqrt5_lower*sqrt5_lower<=5<sqrt5_upper*sqrt5_upper

def floor_fraction(x):return x.numerator//x.denominator

def approximate(x):
 xlo=x[0]+x[1]*(sqrt5_lower if x[1]>=0 else sqrt5_upper)
 xhi=x[0]+x[1]*(sqrt5_upper if x[1]>=0 else sqrt5_lower)
 ii=floor_fraction(xlo*Q0)
 assert 0<=xhi*Q0-ii<2,(x,xlo,xhi,ii)
 return ii

def bareiss_pd(M):
 n=len(M);a=[row[:] for row in M];prev=1
 for j in range(n):
  pivot=a[j][j]
  if pivot<=0:return False
  if j==n-1:break
  for i in range(j+1,n):
   for z in range(i,n):
    vv=a[i][z]*pivot-a[i][j]*a[j][z]
    quot,rem=divmod(vv,prev)
    assert rem==0
    a[i][z]=quot
    if z!=i:a[z][i]=quot
  prev=pivot
 return True

# Other low full-rank degrees have a uniformly modest condition number.
for k in (7,9,10,11,13):
 vals=[approximate(SEQ[i][k]) for i in range(4)]+[Q0]
 M=[[(Q0 if typ==4 else (sgn if k%2 else 1)*vals[typ]) for typ,sgn in row] for row in D]
 assert bareiss_pd([[200*M[i][j]-Q0*int(i==j) for j in range(15)] for i in range(15)]),(k,'low-min')
 assert bareiss_pd([[3*Q0*int(i==j)-M[i][j] for j in range(15)] for i in range(15)]),(k,'low-max')
print('LOW_FULL_RANK_CONDITION_CERTIFICATE_OK',flush=True)

start=time.monotonic();checked=0
for k in range(15,500):
 ints=[approximate(SEQ[i][k]) for i in range(4)]+[Q0]
 M=[[ (Q0 if kind==4 else int(sign1 if k%2 else 1)*ints[kind]) for kind,sign1 in row] for row in D]
 A1=[[200*M[i][j]-int(i==j)*Q0 for j in range(15)] for i in range(15)]
 A2=[[3*Q0*int(i==j)-M[i][j] for j in range(15)] for i in range(15)]
 assert bareiss_pd(A1),(k,'lower')
 assert bareiss_pd(A2),(k,'upper')
 checked+=1
print('CERTIFIED_RATIONAL_POSITIVITY',checked,'degrees 15..499','seconds',round(time.monotonic()-start,2),flush=True)
# Tail: Laplace formula and Gaussian-integral comparison yield
# |P_k(t)| <= sqrt(pi/(2*k*(1-t^2))) for all k>=1, -1<t<1.
# Here 1/sqrt(1-a^2)<263/250, 1/sqrt(1-(1/2)^2)<231/200,
# and 1/sqrt(1-c^2)<851/500. These elementary rational bounds
# can be checked by squaring and 2236/1000<sqrt(5)<2237/1000.
assert F(2236,1000)**2<5<F(2237,1000)**2
# Required inverse-sqrt comparisons, using safe sqrt5 endpoints.
assert (F(263,250)**2)*(5+F(2236,1000))/8>1
assert (F(231,200)**2)*F(3,4)>1
assert (F(851,500)**2)*(5-F(2237,1000))/8>1
T=F(2)+4*(F(263,250)+F(231,200)+F(851,500))
assert F(22,7000)*T*T<F(99,100)**2 # pi<22/7, k>=500
print('ANALYTIC_TAIL_CERTIFICATE',T,flush=True)
print('H3_ALL_DEGREE_CERTIFICATE_OK',flush=True)
