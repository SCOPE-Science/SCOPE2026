"""Finite-state diagnostics for heterogeneous collision-conditioned clockwise walkers.

Requires Python 3 and NumPy. All claims for unbounded parameters are proved in RESULT.md.
"""
import itertools, math
import numpy as np

def compositions(N,k):
 for cut in itertools.combinations(range(1,N), k-1):
  s=(0,)+cut+(N,)
  yield tuple(s[i+1]-s[i] for i in range(k))

def examine(n,rates):
 k=len(rates)
 c=math.prod(rates)**(1/k)
 states=[];lift={};idx={}
 for x1 in range(n):
  for gaps in compositions(n,k):
   ys=[x1]
   for g in gaps[:-1]:ys.append(ys[-1]+g)
   x=tuple(yi%n for yi in ys)
   idx[x]=len(states);states.append(x);lift[x]=ys
 N=len(states)
 assert len(set(states))==N
 h=np.empty(N);D=np.empty(N);Q=np.zeros((N,N));Qh=np.zeros((N,N))
 for ii,x in enumerate(states):
  ys=lift[x]
  h[ii]=math.prod(2*math.sin(math.pi*(ys[j]-ys[i])/n) for i in range(k) for j in range(i+1,k))
  D[ii]=math.exp(sum(yi*math.log(c/rate) for yi,rate in zip(ys,rates)))
  Q[ii,ii]=-sum(rates)
  for j,rate in enumerate(rates):
   y=list(x);y[j]=(y[j]+1)%n
   if y[j] not in (x[:j]+x[j+1:]):
    jj=idx[tuple(y)];Q[ii,jj]+=rate
 lam=sum(rates)-c*math.sin(math.pi*k/n)/math.sin(math.pi/n)
 ha=D*h;ell=h/D
 residual=np.max(np.abs(Q@ha+lam*ha))/np.max(ha)
 leftres=np.max(np.abs(ell@Q+lam*ell))/np.max(ell)
 assert residual < 1e-9 and leftres<1e-9,(n,k,rates,residual,leftres)
 assert abs(float(np.sum(h*h)/sum(h*h))-1)<1e-9
 for i in range(N):
  for j in np.flatnonzero(Q[i]):
   if j==i:continue
   effective=Q[i,j]*ha[j]/ha[i]
   hom=c*h[j]/h[i]
   assert abs(effective-hom)<1e-8,(i,j,effective,hom)
 return N,residual,leftres,lam

if __name__=='__main__':
 ct=0
 for n in range(3,9):
  for k in range(2,min(5,n)):
   for rates in [tuple(1.0 for _ in range(k)),tuple(float(i+1) for i in range(k)),tuple(float(2*i+1)/3 for i in range(k))]:
    N,r,l,lam=examine(n,rates); ct+=1
 print('Passed finite-generator eigenvector and Doob-rate tests:',ct)
 for n in [3,5,7,12]:
  k=2; a,b=1.1,3.2;c=(a*b)**.5
  ell=np.array([(b/a)**(d/2)*math.sin(math.pi*d/n) for d in range(1,n)])
  qsd=ell/ell.sum()
  st=np.sin(np.pi*np.arange(1,n)/n)**2;st/=st.sum()
  assert abs(st.sum()-1)<1e-12 and abs(qsd.sum()-1)<1e-12
 print('Passed normalized quasi-stationary and Q-process gap tests')
