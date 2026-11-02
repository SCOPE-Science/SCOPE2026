"""Reproduce the finite computations supporting the frustrated-matching XY theorem.

Requires numpy and scipy; computations test examples and finite-dimensional optimization,
not an external proof of the global theorem.
"""
import numpy as np
from scipy.optimize import differential_evolution


def prediction(k):
    k=np.asarray(k,dtype=float)
    assert np.all(k>0)
    a=1+k; m=len(a)
    S=np.sum(1/a)
    if S<=1+1.e-12:
        return 0.,np.zeros(m),m-np.sum(a)
    lo=float(np.min(a)); hi=float(m)
    assert sum(np.minimum(1,lo/a))-lo>0
    for _ in range(90):
        mid=(lo+hi)/2
        if np.sum(np.minimum(1,mid/a))>mid:lo=mid
        else: hi=mid
    t=(lo+hi)/2
    x=np.minimum(1,t/a)
    E=m-np.sum(a)+2*(np.dot(a,x*x)-t*t)
    return t,x,E


def energy(theta,k):
    z=np.exp(1j*np.asarray(theta)); n=len(z)
    E=0.
    for j in range(n):
        for i in range(j):
            coeff=float(k[i//2]) if (i%2==0 and j==i+1) else -1.
            E+=coeff*np.real(z[i]*np.conj(z[j]))
    return E


def construct(k):
    t,x,e=prediction(k)
    th=[]
    for xi in x:
        ang=np.arccos(xi)
        th.extend([ang,-ang])
    return np.array(th)


def check():
    checks=0
    rng=np.random.default_rng(447211)
    sets=[np.array([.5,2.]),np.array([.8,.8]), np.array([1.,1.]),
          np.array([2.,2.]),np.array([.2,.5,4.]),
          np.array([1.,2.,5.])]
    for m in (2,3,4):
        for j in range(9):
            sets.append(np.exp(rng.uniform(-2,2.3,m)))
    max_gap=-np.inf
    for k in sets:
        t,x,e=prediction(k)
        E=energy(construct(k),k)
        assert abs(E-e)<2.e-11*(1+abs(e)),('constructed energy',k,e,E)
        checks+=1
        assert abs(2*t-np.abs(np.exp(1j*construct(k)).sum()))<1.e-10
        checks+=1
        m=len(k)
        result=differential_evolution(lambda th:energy(th,k),
                        bounds=[(-np.pi,np.pi)]*(2*m),seed=110+checks,
                        popsize=9,maxiter=450,tol=1.e-9,polish=True)
        gap=result.fun-e
        max_gap=max(max_gap,abs(gap))
        assert gap > -1.e-7*max(1,abs(e)),('optimizer undercut theorem',k,gap)
        assert gap < 2.e-5*max(1,abs(e)),('optimizer missed prediction',k,gap)
        checks+=1
    for m in (2,3,4,6,10):
        critical=np.full(m,m-1.,dtype=float)
        t,x,e=prediction(critical)
        assert t==0
        for z in np.linspace(0,1,13):
            # Equal-strength critical manifold, all pair midpoints have length z.
            angles=np.array([sg*np.arccos(z) for _ in range(m) for sg in (1,-1)])
            assert abs(energy(angles,critical)-e)<1.e-9
            checks+=1
        for eps in (1.e-3,1.e-4,1.e-5):
            r=critical-eps
            t,x,e=prediction(r)
            assert abs(t-m)<1.e-10 and np.allclose(x,1)
            checks+=1
            r=critical+eps
            t,x,e=prediction(r)
            assert t==0 and np.allclose(x,0)
            checks+=1
    a=np.array([2.,3.,6.]); k=a-1
    assert abs(np.sum(1/a)-1)<1.e-14
    for delta in (1.e-2,1.e-3,1.e-4,1.e-5):
        aa=a.copy(); aa[2]-=delta
        t,x,e=prediction(aa-1)
        assert t>2 and t<2.1
        assert x[0]==1 and x[1]<1 and x[2]<1
        checks+=1
    print('PASS',checks,'checks. max differential-evolution energy gap',max_gap)

if __name__=='__main__':check()
