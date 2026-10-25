"""Standalone finite-dimensional tests of enriched two-level polytope identities."""
import itertools, math
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize

PHI = (1 + math.sqrt(5))/2
RIN = 1/PHI
C = 1-RIN

def vertices(p,q):
    a=[(0,)*p + s for s in itertools.product([-1,1],repeat=q)]
    b=[s+(1,)*q for s in itertools.product([-1,1],repeat=p)]
    return np.unique(np.array(a+b,dtype=float),axis=0)

def formulaR(p,q):
    t=min(p/(4*q),1)
    return t,max(q*(1+t)**2,p+q*(1-t)**2)**.5

def formulaV(p,q):
    return 2**(p+q)*math.factorial(p)*math.factorial(q)/math.factorial(p+q)

def halfspaces(p,q):
    dim=p+q
    hs=[]
    for j in range(q):
        v=np.zeros(dim);v[p+j]=1
        hs.append((v,1.))
        for i in range(p):
            for s in [-1,1]:
                w=np.zeros(dim);w[i]=2*s;w[p+j]=-1
                hs.append((w,1.))
    return hs

num_cases=0
num_support=0
for p in range(1,6):
 for q in range(1,5):
    if p+q>6:continue
    vs=vertices(p,q);d=p+q
    expected=2**p+2**q
    assert len(vs)==expected,(p,q,len(vs),expected)
    hs=halfspaces(p,q)
    assert len(hs)==q+2*p*q
    for a,b in hs:
        assert max(vs@a)<=b+1e-10
        # Affine hull of tight vertices is exactly codimension one.
        tight=vs[np.abs(vs@a-b)<1e-9]
        assert np.linalg.matrix_rank(tight[1:]-tight[0],tol=1e-9)==d-1,(p,q,a)
    hull=ConvexHull(vs)
    assert len(hull.vertices)==expected-1,(p,q,len(hull.vertices))
    vol=formulaV(p,q)
    area=(p+q)*PHI*vol
    assert abs(hull.volume/vol-1)<1e-8,(p,q,hull.volume,vol)
    assert abs(hull.area/area-1)<1e-8,(p,q,hull.area,area)
    t,R=formulaR(p,q)
    center=np.array([0]*p+[t]*q)
    dist=np.linalg.norm(vs-center,axis=1)
    assert abs(max(dist)-R)<1e-9
    assert R*R>=max(p,q)-1e-10
    assert (abs(R*R-max(p,q))<1e-9)==(p>=4*q)
    contacts=np.sum(abs(dist-R)<1e-9)
    expected_contacts=2**p+int(p<=4*q)
    assert contacts==expected_contacts,(p,q,contacts,expected_contacts)
    opt=minimize(lambda z: max(np.linalg.norm(vs-z,axis=1)),x0=center+0.12,
         method='Nelder-Mead',options={'maxiter':20000,'xatol':1e-8,'fatol':1e-8})
    assert opt.fun>=R-1e-6,(p,q,opt.fun,R)
    for a,b in hs:
        assert abs((b-a@np.array([0]*p+[C]*q))/np.linalg.norm(a)-RIN)<1e-10
    rng=np.random.default_rng(7100+p*137+q)
    for _ in range(37):
        direction=rng.normal(size=d)
        v=np.max(vs@direction)+np.max(vs@(-direction))
        u=direction[:p];w=direction[p:]
        A=sum(abs(w));B=sum(abs(u));S=sum(w)
        assert abs(v-(A+B+max(abs(A-B),abs(S))))<1e-9
        wc=2*max(A,B)
        assert abs((v-wc)-max(0.,abs(S)-abs(A-B)))<1e-9
        assert v>=wc-1e-9
        num_support+=1
    num_cases+=1
print('FINITE_CHECKS_OK',num_cases,num_support)

# Monte Carlo checks only the proposed scale and shape, not an infinite proof.
rng=np.random.default_rng(271828)
mu=(2/math.pi)**0.5
sigma=(1-2/math.pi)**0.5
for tau in [-2.,0.,2.]:
    p=round(600+tau*math.sqrt(600));q=600
    ns=7000
    gg=rng.standard_normal((ns,p));hh=rng.standard_normal((ns,q))
    A=np.abs(hh).sum(axis=1);B=np.abs(gg).sum(axis=1);S=hh.sum(axis=1)
    W=A+B+np.maximum(np.abs(A-B),np.abs(S))
    X=(W-2*mu*q)/math.sqrt(q)
    z=rng.standard_normal((ns,3))
    predicted=sigma*z[:,0]+mu*tau+sigma*z[:,1]+np.maximum(
        np.abs(sigma*(z[:,0]-z[:,1])-mu*tau), np.abs(z[:,2]))
    assert abs(X.mean()-predicted.mean())<.12,(tau,X.mean(),predicted.mean())
    assert abs(X.std()-predicted.std())<.1,(tau,X.std(),predicted.std())
print('GAUSSIAN_DIAGNOSTICS_OK')

# Zero-window population constants: only a distributional diagnostic.
a=(2*(1-2/math.pi))**0.5
prob=1-2/math.pi*math.atan(a)
expected=(2/math.pi)**0.5*((1+a*a)**0.5-a)
N=200000
z=rng.standard_normal((N,2))
delta=np.maximum(0,np.abs(z[:,0])-a*np.abs(z[:,1]))
assert abs((delta>0).mean()-prob)<0.005
assert abs(delta.mean()-expected)<0.005
print('CRITICAL_GAP_CONSTANTS_OK',round(prob,6),round(expected,6))
print('VERIFY_OK')
