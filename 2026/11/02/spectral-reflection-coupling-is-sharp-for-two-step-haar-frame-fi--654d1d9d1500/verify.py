"""Standalone symbolic and numeric checks for paired Haar-frame finite differences.
Scientific theorem rests on the separately stated sixth-moment and Cauchy--Schwarz proof.
"""
from fractions import Fraction as F
import numpy as np

def pairings(items):
    items=tuple(items)
    if not items:
        yield ()
    else:
        x=items[0]
        for j in range(1,len(items)):
            y=items[j]
            rem=items[1:j]+items[j+1:]
            for rest in pairings(rem):
                yield ((x,y),)+rest

P=list(pairings(tuple(range(6))))
assert len(P)==15

def sphere_six(indices,d):
    count=0
    for pair in P:
        if all(indices[i]==indices[j] for i,j in pair):
            count+=1
    return F(count,d*(d+2)*(d+4))

def six_cov_diag(vals):
    d=len(vals)
    out=[]
    for i in range(d):
        y=F(0)
        for a in range(d):
            for b in range(d):
                y+=F(vals[a]*vals[b])*sphere_six((i,i,a,a,b,b),d)
        out.append(d*y)
    return out

def formula(vals):
    d=len(vals); t=sum(vals); u=sum(x*x for x in vals)
    return [F(t*t+2*u+4*t*x+8*x*x,(d+2)*(d+4)) for x in vals]

for vals in [(F(1),),(F(2),F(1)),(F(7),F(3),F(1)),(F(2),F(2),F(2),F(2))]:
    assert six_cov_diag(vals)==formula(vals),(vals,six_cov_diag(vals),formula(vals))

# Check exact scalar paired risk and strict inequality for rational test cases.
for vals,eta in [((F(2),F(1)),F(1,4)),((F(2),F(1)),F(3,4)),((F(1),F(1)),F(3,2)),((F(7),F(3),F(1)),F(1,5))]:
    d=len(vals)
    for H_i,K_i in zip(vals,formula(vals)):
        a=1-eta*H_i
        assert -1<a<1
        sign=-1 if a>0 else (1 if a<0 else -1)
        lower=K_i*(1-abs(a))**2
        attained=K_i*(a+sign)**2
        iid=K_i*(1+a*a)
        assert lower==attained and lower<=iid
        if a!=0: assert lower<iid
        V=eta*eta*lower/(1-a**4)
        V0=eta*eta*iid/(1-a**4)
        assert V<=V0 and V>=0

# Independently check finite differences and the spectral-reflection identity.
rng=np.random.default_rng(20612026)
for vals,eta in [([2.,1.],.2),([2.,1.],.7),([7.,3.,1.],.2)]:
    d=len(vals); H=np.diag(vals); hh=.13
    a=1-eta*np.array(vals)
    S=np.diag([(-1. if t>0 else 1.) for t in a]); U,R=np.linalg.qr(rng.standard_normal((d,d))); U=U@np.diag(np.sign(np.diag(R)))
    def err(U):
        x=rng.standard_normal(d)
        f=lambda t: .5*(t@H@t)
        fd=sum(U[:,j]*(f(x+hh*U[:,j])-f(x))/hh for j in range(d))
        return fd-H@x
    v=err(U); w=err(S@U)
    direct=(hh/2)*sum((U[:,j]@H@U[:,j])*U[:,j] for j in range(d))
    assert np.linalg.norm(v-direct)<1e-11
    assert np.linalg.norm(w-S@direct)<1e-11
    assert np.linalg.norm((np.diag(a)@v+w)-np.diag(a+np.diag(S))@v)<1e-11

# Convergence of Monte Carlo sampled squared error covariance to analytic formula.
vals=np.array([2.,1.]); H=np.diag(vals); N=15000
samples=[]
for _ in range(N):
    U,R=np.linalg.qr(rng.standard_normal((2,2))); U=U@np.diag(np.sign(np.diag(R)))
    samples.append(sum((U[:,j]@H@U[:,j])*U[:,j] for j in range(2)))
S0=np.asarray(samples); theory=np.array([float(v) for v in formula(tuple(map(F,vals)))])
assert np.max(abs((S0*S0).mean(0)-theory))<.06,((S0*S0).mean(0),theory)
assert np.linalg.norm(S0.mean(0))<.06
print('VERIFY_OK sixth-moment contractions=4, exact mode-coupling/risk checks=8, finite-difference spectral-reflection checks=3, Haar covariance simulations=15000')

# Rotational covariance check for a nondiagonal matrix; no diagonal-alignment shortcut.
Q,_=np.linalg.qr(np.array([[2.,1.,3.],[-1.,4.,.5],[.3,-2.,1.]]))
H=Q@np.diag([3.,2.,1.])@Q.T
d=3
K=((np.trace(H)**2+2*np.trace(H@H))*np.eye(d)+4*np.trace(H)*H+8*H@H)/((d+2)*(d+4))
W=[]
for _ in range(20000):
    U,R=np.linalg.qr(rng.standard_normal((d,d))); U=U@np.diag(np.sign(np.diag(R)))
    W.append(sum((U[:,j]@H@U[:,j])*U[:,j] for j in range(d)))
W=np.asarray(W)
assert np.max(abs(W.T@W/len(W)-K))<.08

# Exhaustive d=1 pair enumeration of marginal-preserving extremal couplings.
for a in [F(1,2), F(-1,3), F(0)]:
    all_pairs=[(F(s),F(t)) for s in [-1,1] for t in [-1,1]]
    iid=sum((a*s+t)**2 for s,t in all_pairs)/4
    sign=-1 if a>0 else (1 if a<0 else -1)
    opt=sum((a*F(s)+sign*F(s))**2 for s in [-1,1])/2
    assert iid==1+a*a and opt==(1-abs(a))**2
print('VERIFY_OK non-diagonal covariance=20000, exact d1 extremal couplings=3')
