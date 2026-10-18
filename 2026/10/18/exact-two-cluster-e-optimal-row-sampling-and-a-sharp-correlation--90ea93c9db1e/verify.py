import numpy as np
from scipy.optimize import minimize_scalar, minimize
from numpy.linalg import eigvalsh
from fractions import Fraction

def theorem(p,q,c,r):
 assert p>=2 and q>=2 and 0<c<1 and r>0
 a=1+(p-1)*c; b=1+(q-1)*c
 assert p*q*r*r<a*b
 if p>q:
  vv,ll,kind=theorem(q,p,c,r)
  return ll,vv,kind
 if p==q or r<=c: return 1/(p+q),1/(p+q),'uniform'
 t0=(b+q*r)/(a+p*r)
 D=a-p*r*r/c
 if D>0:
  R=(1-c)/D
  if R<t0:
   return R/(p*R+q),1/(p*R+q),'crossing'
 return t0/(p*t0+q),1/(p*t0+q),'interior'

def eigs(p,q,c,r,u,v):
 a=1+(p-1)*c;b=1+(q-1)*c
 sub=np.array([[a*u,r*np.sqrt(p*q*u*v)],[r*np.sqrt(p*q*u*v),b*v]])
 return min(u*(1-c),v*(1-c),eigvalsh(sub)[0])

def fullmatrix(p,q,c,r):
 n=p+q; C=np.eye(n);
 C[:p,:p]+=c*(np.ones((p,p))-np.eye(p));C[p:,p:]+=c*(np.ones((q,q))-np.eye(q));C[:p,p:]=r;C[p:,:p]=r
 return C

rng=np.random.default_rng(13941)
count=0; kinds={}
for p in range(2,8):
 for q in range(2,10):
  for j in range(100):
   c=rng.uniform(.05,.87);a=1+(p-1)*c;b=1+(q-1)*c
   r=rng.uniform(.005,.999*np.sqrt(a*b/(p*q)))
   u,v,kind=theorem(p,q,c,r)
   kinds[kind]=kinds.get(kind,0)+1
   x=eigs(p,q,c,r,u,v)
   opt=minimize_scalar(lambda gamma:-eigs(p,q,c,r,gamma/p,(1-gamma)/q), bounds=(1e-11,1-1e-11),method='bounded',options={'xatol':2e-12})
   if abs(x+opt.fun)>2e-8:
    raise AssertionError((p,q,c,r,u,v,kind,x,-opt.fun))
   if j<5 and p+q<=12:
    C=fullmatrix(p,q,c,r)
    # Full eig(P^1/2 C P^1/2) and random asymmetric competitors
    probs=np.array([u]*p+[v]*q)
    vals=eigvalsh(C*np.sqrt(np.outer(probs,probs)))
    assert abs(vals[0]-x)<1e-9
    for k in range(30):
     probs=rng.dirichlet(np.ones(p+q)*rng.uniform(.2,3))
     val=eigvalsh(C*np.sqrt(np.outer(probs,probs)))[0]
     assert val<=x+3e-10, (p,q,c,r,kind,x,val)
   count+=1
print('PASS',count,'parameter cases; phase counts',kinds)
# an exact illustration p=2, q=10, c=1/4, r=7/20
p,q=2,10;c=Fraction(1,4);r=Fraction(7,20)
a=1+(p-1)*c;b=1+(q-1)*c;D=a-p*r*r/c;R=(1-c)/D
u=R/(p*R+q);v=1/(p*R+q)
print('EXACT',{'D':str(D),'R':str(R),'u':str(u),'v':str(v),'lambda':str((1-c)*v)})
