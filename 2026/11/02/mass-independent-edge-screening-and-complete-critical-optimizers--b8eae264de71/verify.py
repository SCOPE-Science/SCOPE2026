"""Reproduce algebraic and numerical checks for heterogeneous cycle spectral-gap screening.
Requires Python 3, NumPy and SciPy. This finite checker supports, but does not prove,
the universally quantified theorem in RESULT.md.
"""
from fractions import Fraction as F
import numpy as np
from scipy.linalg import null_space, eigh
from scipy.optimize import minimize

def data(mass, length, budget=1.):
    m=np.asarray(mass,dtype=float); ell=np.asarray(length,dtype=float)
    n=len(m); assert n>=3 and len(ell)==n-1 and np.all(m>0) and np.all(ell>0)
    z=np.r_[0.,np.cumsum(ell)]; mu=np.dot(m,z)/sum(m)
    f=z-mu; V=np.dot(m,f*f); G=np.cumsum(m*(mu-z))[:-1]
    lam=budget/V; wp=lam*G/ell; S=sum(ell)
    assert np.min(wp)>0
    return f,V,G,S,lam,wp

def lap(w,t):
    n=len(w)+1; L=np.zeros((n,n))
    for i,a in enumerate(w):
        L[i,i]+=a;L[i+1,i+1]+=a;L[i,i+1]-=a;L[i+1,i]-=a
    L[0,0]+=t; L[-1,-1]+=t;L[0,-1]-=t;L[-1,0]-=t
    return L

def eiggap(m,w,t):
    d=1/np.sqrt(m); A=lap(w,t)*d[:,None]*d[None,:]
    return np.linalg.eigvalsh(A)[1]

def endpoint(m,ell,B=1):
    f,V,G,S,lam,w0=data(m,ell,B)
    n=len(m); D=lap(-S/ell,1)
    K=lap(w0,0)-lam*(np.diag(m)-np.outer(m,m)/sum(m))
    basis=null_space(np.vstack([m,m*f]))
    KC=basis.T@K@basis; DC=-(basis.T@D@basis)
    te=float(np.min(w0*ell/S)); ts=float(np.min(eigh(KC,DC,eigvals_only=True)))
    return min(te,ts),te,ts,K,D

def exact_checks():
    count=0
    for n in range(3,11):
      for seed in range(50):
        rng=np.random.default_rng(193*n+seed)
        ma=[int(x) for x in rng.integers(1,11,size=n)]
        ell=[int(x) for x in rng.integers(1,7,size=n-1)]
        z=[F(0)]
        for x in ell:z.append(z[-1]+x)
        mass=list(map(F,ma)); tot=sum(mass); mu=sum(a*b for a,b in zip(mass,z))/tot
        f=[x-mu for x in z]; V=sum(a*b*b for a,b in zip(mass,f))
        B=F(7,3);lam=B/V; S=sum(ell)
        G=[sum(mass[j]*(mu-z[j]) for j in range(i+1)) for i in range(n-1)]
        w=[lam*G[i]/ell[i] for i in range(n-1)]
        assert all(x>0 for x in w)
        assert sum(ell[i]**2*w[i] for i in range(n-1))==B
        d=[F(0)]*n
        for i,c in enumerate(w):
            d[i]+=c*(f[i]-f[i+1]);d[i+1]+=c*(f[i+1]-f[i])
        assert d==[lam*mass[i]*f[i] for i in range(n)]
        t=min(w[i]*ell[i]/S for i in range(n-1))/F(5)
        wc=[w[i]-t*S/ell[i] for i in range(n-1)]
        assert all(x>0 for x in wc)
        assert sum(ell[i]*ell[i]*wc[i] for i in range(n-1))+S*S*t==B
        d=[F(0)]*n
        for i,c in enumerate(wc):
            d[i]+=c*(f[i]-f[i+1]);d[i+1]+=c*(f[i+1]-f[i])
        d[0]+=t*(f[0]-f[-1]);d[-1]+=t*(f[-1]-f[0])
        assert d==[lam*mass[i]*f[i] for i in range(n)]
        count+=5
    return count

def numeric_checks():
    count=0;opt=0
    for n in range(3,10):
      for seed in range(45):
        rng=np.random.default_rng(seed+220*n)
        m=np.exp(rng.uniform(-1.3,1.3,size=n));ell=np.exp(rng.uniform(-1.0,1.0,size=n-1))
        p=ell**2; B=float(rng.uniform(.7,3.)); f,V,G,S,lam,w0=data(m,ell,B)
        assert abs(eiggap(m,w0,0)-lam)<=2e-8*max(1,lam)
        assert np.linalg.norm(lap(w0,0)@f-lam*m*f) < 1e-8*max(1,np.linalg.norm(lam*m*f))
        tstar,te,ts,K,D=endpoint(m,ell,B)
        assert tstar>0 and tstar<=te+1e-9
        for t in [0,tstar*.31,tstar*.79,tstar]:
          wc=w0-t*S/ell
          assert min(wc)>=-2e-9*max(1,max(w0))
          assert abs(np.dot(p,wc)+S*S*t-B)<1e-8*max(1,B)
          assert abs(eiggap(m,wc,t)-lam)<2e-8*max(1,lam)
          count+=3
        # expensive edge is not profitable; cheap edge strictly improves
        ep=min(te/1000,B/(2*S*S))
        qhigh=S*S*1.1
        assert eiggap(m,w0*(1-qhigh*ep/B),ep)<lam-1e-5*ep/V
        qlow=S*S*.9
        assert eiggap(m,w0*(1-qlow*ep/B),ep)>lam+1e-5*ep/V
        count+=4
        # Rayleigh certificate for random feasible alternatives above the threshold.
        for j in range(10):
          zz=rng.dirichlet(np.ones(n));w=B*zz[:-1]/p;t=B*zz[-1]/qhigh
          assert eiggap(m,w,t)<=lam+2e-8*max(1,lam)
          count+=1
        if n<=6 and seed<6:
          qlow=S*S*.75
          bounds=[(0,None)]*n
          x0=np.r_[w0,0.]
          def obj(a):return -eiggap(m,a[:-1],a[-1])
          cons=({'type':'eq','fun':lambda a: np.dot(p,a[:-1])+qlow*a[-1]-B},)
          res=minimize(obj,x0,bounds=bounds,constraints=cons,method='SLSQP',options={'ftol':1e-10,'maxiter':350})
          assert res.success, res.message
          assert res.x[-1]>1e-9
          assert -res.fun>lam+1e-9
          opt+=1
    return count,opt

if __name__=='__main__':
  a=exact_checks(); b,c=numeric_checks()
  print('exact-rational test groups: 400; exact rational assertions:',a)
  print('numerical assertions:',b,'constrained optimizations:',c)
  print('ALL CHECKS PASSED; tests are finite evidence, not an all-parameter proof')
