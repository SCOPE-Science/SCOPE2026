"""Independent finite-state validation of critical capped two-state filament exit laws."""
import math
import numpy as np
from scipy.sparse import lil_matrix, identity
from scipy.sparse.linalg import spsolve
import mpmath as mp
mp.mp.dps=65

def transform_exact(n,j,s,kd,ke,lp,lm,gamma,phase='i'):
    N=mp.mpf(n); s=mp.mpf(str(s));kd=mp.mpf(str(kd));ke=mp.mpf(str(ke));lp=mp.mpf(str(lp));lm=mp.mpf(str(lm));gamma=mp.mpf(str(gamma))
    A=ke*(s+kd+lp)
    C=kd*(s+ke+lm)
    B=ke*kd+(s+ke+lm)*(s+kd+lp)-lm*lp
    disc=mp.sqrt(B*B-4*A*C)
    zp=(B+disc)/(2*A);zm=(B-disc)/(2*A)
    b=1+s/kd*(1+lp/(s+lm+gamma))
    dp=zp**(n-1)*(1-b*zp)
    dm=zm**(n-1)*(1-b*zm)
    fi=(dm*zp**j-dp*zm**j)/(dm-dp)
    if phase=='i':return fi
    fim=(dm*zp**(j-1)-dp*zm**(j-1))/(dm-dp)
    return ((s+kd+lp)*fi-kd*fim)/lp

def transient(n,kd,ke,lp,lm,gamma):
    Q=lil_matrix((2*n,2*n),dtype=float); a=np.zeros(2*n)
    def I(j):return j-1
    def A(j):return n+j-1
    for j in range(1,n+1):
       ii=I(j); aa=A(j)
       Q[ii,aa]+=lp; Q[ii,ii]-=lp+kd
       if j>1:Q[ii,I(j-1)]+=kd
       else:a[ii]=kd
       if j<n:
          Q[aa,A(j+1)]+=ke;Q[aa,ii]+=lm;Q[aa,aa]-=ke+lm
       else:
          Q[aa,ii]+=lm+gamma;Q[aa,aa]-=lm+gamma
    return Q.tocsr(),a

def mean_exact(n,j,kd,ke,lp,lm,gamma,phase='i'):
    kd=mp.mpf(str(kd));ke=mp.mpf(str(ke));lp=mp.mpf(str(lp));lm=mp.mpf(str(lm));gamma=mp.mpf(str(gamma))
    delta=(1+lp/(lm+gamma))/kd
    r=kd*(ke+lm)/(ke*(kd+lp))
    if abs(r-1)<mp.mpf('1e-45'):
       C=(lp+lm)/(ke*(kd+lp))
       mi=delta*j+C*(n*j-j*(j+1)/2)
       mim=delta*(j-1)+C*(n*(j-1)-(j-1)*j/2)
    else:
       mu=(lp+lm)/(kd*lm-ke*lp)
       mi=mu*j+(delta-mu)*sum(r**(v-n) for v in range(1,j+1))
       mim=mu*(j-1)+(delta-mu)*sum(r**(v-n) for v in range(1,j))
    if phase=='i':return mi
    return ((kd+lp)*mi-kd*mim-1)/lp

def test_small():
 count=0
 samples=[(2.,1.,2.,1.), (3.,2.,3.,2.),(1.5,3.,1.5,3.),(5.,1.5,5.,1.5), (2.,1.3,1.1,.7),(.7,2.5,2.,1.),(4.,.4,.3,1.7)]
 for kd,ke,lp,lm in samples:
  for n in ([2,3,5,11] if kd*lm<ke*lp else [2,3,5,11,25]):
   for gamma in [0.,ke,2.3*ke]:
    Q,a=transient(n,kd,ke,lp,lm,gamma)
    for s in [.001,.2,1.7]:
     u=spsolve(s*identity(2*n,format='csr')-Q,a)
     for j in [1,max(1,n//2),n]:
      for phase in ['i','a']:
       k=(j-1) if phase=='i' else n+j-1
       f=float(transform_exact(n,j,s,kd,ke,lp,lm,gamma,phase))
       assert abs(f-u[k])<1e-10,(n,j,s,gamma,phase,f,u[k]);count+=1
    m=spsolve(-Q,np.ones(2*n))
    for j in [1,max(1,n//2),n]:
     for phase in ['i','a']:
      k=(j-1) if phase=='i' else n+j-1
      v=float(mean_exact(n,j,kd,ke,lp,lm,gamma,phase))
      assert abs(v-m[k])<1e-7*max(1,abs(v)),(n,j,gamma,phase,v,m[k]);count+=1
 return count

def test_monotonicity():
 count=0
 for kd,ke,lp,lm in [(2.,1.,2.,1.),(2.,1.3,1.1,.7),(.7,2.5,2.,1.)]:
  for n in [2,3,9,20]:
   for j in [1,(n+1)//2,n]:
    for s in [0.01,0.2,1.]:
     for phase in ['i','a']:
      vals=[transform_exact(n,j,s,kd,ke,lp,lm,g,phase) for g in [0.,.1,ke,4*ke,50*ke]]
      assert all(vals[k]<vals[k+1] for k in range(4)),(n,j,s,phase,vals)
      count+=4
 return count

def test_scaling():
 count=0
 cases=[(2.,1.,2.,1.,0.,1.),(3.,2.,3.,2.,0.2,4.),(1.5,3.,1.5,3.,0.,5.)]
 for kd,ke,lp,lm,ga,gb in cases:
  D=ke*(kd+lp)/(lm+lp)
  da=(1+lp/(lm+ga))/kd
  db=(1+lp/(lm+gb))/kd
  for sigma in [.03, .5, 3.5, 12.]:
   kk=math.sqrt(sigma/D)
   for x in [.17,.5,.9,1.]:
    lim=math.cosh(kk*(1-x))/math.cosh(kk)
    diflim=-sigma*(da-db)*math.sinh(kk*x)/(kk*math.cosh(kk)**2)
    tail=[]
    for n in [100,200,400,800,1600]:
     j=round(x*n)
     t1=transform_exact(n,j,sigma/n**2,kd,ke,lp,lm,ga)
     t2=transform_exact(n,j,sigma/n**2,kd,ke,lp,lm,gb)
     for phase in ['i','a']:
       z=float(transform_exact(n,j,sigma/n**2,kd,ke,lp,lm,ga,phase))
       if n>=800:
        assert abs(z-lim)<.009, (n,x,sigma,z,lim)
       count+=1
     err=abs(float(n*(t1-t2))-diflim)
     tail.append(err)
     count+=1
    assert tail[-1]<max(.004,tail[0]/6), (x,sigma,tail,diflim)
 return count

if __name__=='__main__':
 a=test_small();b=test_scaling();c=test_monotonicity()
 print('PASS',a+b+c,'checks; direct finite CTMC/Laplace/mean, monotonicity, and quadratic-scale cap-sensitive limits')
