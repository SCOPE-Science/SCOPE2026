from fractions import Fraction as F
from random import Random
import numpy as np

def opt(r,a):
 a=F(a);b=1-a; T=2*r-3
 if a<=F(1,2*r-1):
  x=a; mu=(1-2*a)/(T*b);regime='A-saturated'
 elif a<=F(1,r):
  x=a*b*(T+1)/(T+a); mu=b/(T+a);regime='light-contrast'
 elif a<=F(2,3):
  x=2*a*b/(2-a); mu=a/(2-a);regime='mass-contrast'
 else:
  x=b;mu=(2*a-1)/a;regime='light-saturated'
 t=2*(r-1)*(1-x/b)/T
 return x,t,mu,regime

def mat(r,m,a,x,t):
 a,b=F(a),1-F(a); N=r*m; pi=[a/m]*m+[b/((r-1)*m)]*(N-m)
 P=[[F(0) for i in range(N)] for i in range(N)]
 for i in range(N):
  for j in range(N):
   if i==j:continue
   p=i//m;q=j//m
   if p==q:continue
   if 0 in (p,q):flow=x/((r-1)*m*m)
   else:flow=b*t/((r-1)**2*m*m)
   P[i][j]=flow/pi[i]
  P[i][i]=1-sum(P[i])
 return P,pi

def vect_eq(P,v,l):
 return all(sum(P[i][j]*v[j] for j in range(len(v)))==l*v[i] for i in range(len(v)))

cnt=0
for r in range(4,9):
 for m in range(2,5):
  for a in [F(1,100),F(1,2*r-1),F(1,2*r-1)+F(1,1000),F(1,r),F(1,r)+F(1,1000),F(1,2),F(2,3),F(4,5),F(99,100)]:
   x,t,mu,regime=opt(r,a);P,pi=mat(r,m,a,x,t);b=1-a;T=2*r-3
   assert all(0<=v<=1 for row in P for v in row)
   assert all(sum(row)==1 for row in P)
   assert all(pi[i]*P[i][j]==pi[j]*P[j][i] for i in range(r*m) for j in range(r*m))
   eigA=1-x/a;eigB=1-x/b-F(r-2,r-1)*t;eigC=1-x/b-t;eigD=1-x/(a*b)
   assert max(map(abs,[eigA,eigB,eigC,eigD]))==mu,(r,m,a,regime,mu)
   N=r*m;ones=[F(1)]*N;v=[F(0)]*N
   assert vect_eq(P,ones,F(1))
   v[0]=1;v[1]=-1;assert vect_eq(P,v,eigA)
   v=[F(0)]*N;v[m]=1;v[m+1]=-1;assert vect_eq(P,v,eigB)
   v=[F(0)]*N
   for i in range(m,2*m):v[i]=1
   for i in range(2*m,3*m):v[i]=-1
   assert vect_eq(P,v,eigC)
   v=[b]*m+[-a]*(N-m)
   assert vect_eq(P,v,eigD)
   # grid global scalar min,
   for j in range(101):
    xx=min(a,b)*j/100;uu=1-xx/b
    # ideal lower envelope over light-part conductance t
    target=max(abs(1-xx/a),abs(1-xx/(a*b)),uu/T)
    assert target>=mu
   cnt+=1
print('exact instances',cnt)
# numerical arbitrary asymmetric conductance comparison
for r,m,a in [(4,2,.01),(4,2,.1),(4,2,.25),(4,2,.8),(4,3,.67),(5,2,.04),(5,2,.18),(6,2,.3),(7,2,.9)]:
 x,t,mu,_=opt(r,F(str(a)));rng=Random(1228)
 N=r*m;pi=np.array([float(F(str(a))/m)]*m+[float((1-F(str(a)))/((r-1)*m))]*(N-m))
 v=np.sqrt(pi);J=np.outer(v,v)
 # construct feasible random symmetric edge-flows via scaling
 for it in range(100):
  flow=np.zeros((N,N));
  for i in range(N):
   for j in range(i+1,N):
    if i//m!=j//m: flow[i,j]=flow[j,i]=rng.random()
  scales=np.sqrt(pi/(np.maximum(flow.sum(axis=1),1e-20)));flow*=np.outer(scales,scales)
  # normalize down to feasible
  ratio=np.max(flow.sum(axis=1)/pi)
  if ratio>1: flow/=ratio
  np.fill_diagonal(flow,pi-flow.sum(axis=1))
  S=flow/np.sqrt(np.outer(pi,pi))
  eigs=np.linalg.eigvalsh(S-J)
  mm=np.max(abs(eigs))
  assert mm+1e-10>=float(mu),(r,m,a,mm,mu)
print('asymmetric random comparisons',9*100)
# Metropolis-Hastings uses uniform-neighbor proposals and rejection to the diagonal.
# Its inter-part flow and B-part contrast parameter are x=min(a,b/(r-1)), t=1.
metchecks=0
for r in range(4,11):
 for a in [F(1,101),F(1,2*r-1),F(1,2*r-1)+F(1,1000),F(1,r),F(2,2*r-1),F(1,2),F(2,3),F(8,9)]:
  if a>=1:continue
  b=1-a;x,t,mu,_=opt(r,a)
  xm=min(a,b/(r-1));
  mh=max(abs(1-xm/a),abs(1-xm/b-F(r-2,r-1)),abs(1-xm/b-1),abs(1-xm/(a*b)))
  assert mh>=mu
  assert (mh==mu)==(a==F(1,2*r-1)),(r,a,mh,mu)
  metchecks+=1
print('exact Metropolis checks',metchecks)

