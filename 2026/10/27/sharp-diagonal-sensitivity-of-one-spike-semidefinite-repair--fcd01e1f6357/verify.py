"""Reproducible numerical and exact checks for the one-spike PSD projection theorem.
Only the analytical proof establishes the statements for all dimensions."""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
import math
import numpy as np
from scipy.optimize import brentq
count=0

def check(condition,msg):
 global count
 count+=1
 if not condition: raise AssertionError(msg)

def fracP(w):
 n=len(w);d=sum(x*x for x in w)
 return [[Q(w[i]*w[j],d) for j in range(n)] for i in range(n)]

def mm(A,B):
 n=len(A);return [[sum((A[i][k]*B[k][j] for k in range(n)),Q(0)) for j in range(n)] for i in range(n)]

def add(A,B,a=Q(1),b=Q(1)):
 n=len(A);return [[a*A[i][j]+b*B[i][j] for j in range(n)] for i in range(n)]

def derivative(P,alpha,H):
 PH=mm(P,H);HP=mm(H,P);PHP=mm(PH,P)
 return add(add(PH,HP,alpha,alpha),PHP,Q(1),Q(1)-2*alpha)

def coeffs(P,alpha,row):
 n=len(P);ret=[]
 for i,j in combinations_with_replacement(range(n),2):
  H=[[Q(int((k==i and l==j) or (k==j and l==i))) for l in range(n)] for k in range(n)]
  ret.append(derivative(P,alpha,H)[row][row])
 return ret

for w in ((1,2),(1,2,3),(3,1,2,4),(2,3,4,5,6)):
 n=len(w);P=fracP(w);r=0
 for alpha in (Q(0),Q(1,5),Q(1,2),Q(3,4),Q(1)):
  c=coeffs(P,alpha,r)
  L=sum(map(abs,c),Q(0))
  z=P[r][r]
  s=sum(abs(Q(w[j],1)) for j in range(n) if j!=r)/math.sqrt(sum(x*x for x in w))
  zz=float(z)
  expect=zz*zz+2*float(alpha)*zz*(1-zz)+2*math.sqrt(zz)*(zz+float(alpha)*(1-2*zz))*s+abs(1-2*float(alpha))*zz*s*s
  check(abs(float(L)-expect)<3e-12, f'coefficient row {w},{alpha}')
  check(float(L)<len(w)+1e-12, f'Frobenius upper bound {w},{alpha}')

def f(n,t):
 return (t**4+(n+1)*t*t+2*math.sqrt(n-1)*t)/(1+t*t)**2

def poly(n,t):
 return (n+1)*t-(n-1)*t**3+math.sqrt(n-1)*(1-3*t*t)

def optimal(n):
 t=brentq(lambda t:poly(n,t),0,5)
 return t,f(n,t)
for n in list(range(2,101))+[250,1000,10000,100000]:
 t,val=optimal(n)
 check(poly(n,t)<1e-7 and poly(n,t)>-1e-7*n, f'root n{n}')
 check(val >= f(n,1)-1e-10,f'opt n{n}')
 G=(1+math.sqrt(n))**2/4
 check(f(n,1)>G, f'strict one-spike n{n}')
 for frac in (.01,.05,.125,.5,1,2,4,10,50):
  check(val+1e-8>=f(n,t*frac), f'local grid n{n},frac{frac}')
 check((n/4+math.sqrt(n)/2+.75-val)/math.sqrt(n)<=5,f'asymp weak n{n}')

for n in range(2,11):
 t,K=optimal(n)
 for delta in (.01,.1,1,10):
  u=np.array([t]+[1/math.sqrt(n-1)]*(n-1),dtype=float)/math.sqrt(1+t*t)
  P=np.outer(u,u);A=P-delta*(np.eye(n)-P)
  alpha=1/(1+delta)
  C=[]
  for i,j in combinations_with_replacement(range(n),2):
   H=np.zeros((n,n));H[i,j]=1;H[j,i]=1
   pred=alpha*(P@H+H@P)+(1-2*alpha)*(P@H@P)
   C.append(pred[0,0])
   if n<=6:
    eps=1e-7*min(delta,1)
    ep,vp=np.linalg.eigh(A+eps*H);em,vm=np.linalg.eigh(A-eps*H)
    pp=(vp*np.maximum(ep,0))@vp.T;pm=(vm*np.maximum(em,0))@vm.T
    check(abs((pp[0,0]-pm[0,0])/(2*eps)-pred[0,0])<4e-7,f'finite difference n{n},d{delta}')
  L=sum(abs(x) for x in C)
  check(L<=K+1e-9,f'upper n{n},d{delta}')
  check(L>=0,f'nonnegative n{n},d{delta}')
print(f'ALL CHECKS PASSED: {count} assertions')
print('dimension, maximizing t, sharp restricted condition number, asymptotic comparator')
for n in [2,3,4,5,10,20,100,1000,10000]:
 t,K=optimal(n)
 print(n, f'{t:.10f}',f'{K:.10f}',f'{n/4+math.sqrt(n)/2+.75:.10f}')
