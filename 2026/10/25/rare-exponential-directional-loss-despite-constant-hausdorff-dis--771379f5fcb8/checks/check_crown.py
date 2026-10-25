import numpy as np
from scipy.linalg import null_space
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from math import comb, sqrt

rng=np.random.default_rng(1729)
for n in (3,4,5):
    V=np.array([np.r_[np.eye(n)[i],np.eye(n)[j]] for i in range(n) for j in range(n)])
    W=np.array([np.r_[np.eye(n)[i],np.eye(n)[j]] for i in range(n) for j in range(n) if i!=j])
    T=null_space(np.vstack([np.r_[np.ones(n),np.zeros(n)],np.r_[np.zeros(n),np.ones(n)]]))
    vp=ConvexHull((V-V.mean(axis=0))@T).volume
    vq=ConvexHull((W-V.mean(axis=0))@T).volume
    expected=1-n/comb(2*n-2,n-1)
    assert abs(vq/vp-expected)<1e-9,(n,vq/vp,expected)
    for i in range(n):
        target=np.r_[np.eye(n)[i],np.eye(n)[i]]
        fun=lambda z: np.sum((z@W-target)**2)
        res=minimize(fun, np.ones(len(W))/len(W),method='SLSQP',bounds=[(0,1)]*len(W),constraints=[{'type':'eq','fun':lambda z:np.sum(z)-1}],options={'maxiter':1500,'ftol':1e-13})
        assert res.success or res.fun<(n/(2*(n-1)))+1e-7
        assert abs(res.fun-n/(2*(n-1)))<1e-7,(n,i,res.fun)
    checks=0
    for _ in range(500):
        u=rng.normal(size=2*n)
        u[:n]-=u[:n].mean();u[n:]-=u[n:].mean();u/=np.linalg.norm(u)
        g=u[:n];h=u[n:]
        a=sorted(g, reverse=True); b=sorted(h,reverse=True)
        amin=sorted(g);bmin=sorted(h)
        pos=min(a[0]-a[1],b[0]-b[1]) if np.argmax(g)==np.argmax(h) else 0
        neg=min(amin[1]-amin[0],bmin[1]-bmin[0]) if np.argmin(g)==np.argmin(h) else 0
        direct=(np.max(V@u)-np.min(V@u))-(np.max(W@u)-np.min(W@u))
        assert abs(direct-pos-neg)<1e-11,(n,direct,pos+neg)
        checks+=1
    print('n',n,'volume ratio',round(vq/vp,12),'Hausdorff squared',n/(2*(n-1)),'support checks',checks)
for n in (20,50,100):
    N=25000
    g=rng.normal(size=(N,n));h=rng.normal(size=(N,n))
    gap_top=np.partition(g,-2,axis=1)[:,-1]-np.partition(g,-2,axis=1)[:,-2]
    gap_h_top=np.partition(h,-2,axis=1)[:,-1]-np.partition(h,-2,axis=1)[:,-2]
    gap_bot=np.partition(g,1,axis=1)[:,1]-np.partition(g,1,axis=1)[:,0]
    gap_h_bot=np.partition(h,1,axis=1)[:,1]-np.partition(h,1,axis=1)[:,0]
    top=np.argmax(g,axis=1)==np.argmax(h,axis=1)
    bot=np.argmin(g,axis=1)==np.argmin(h,axis=1)
    R=np.sqrt(np.sum((g-g.mean(axis=1,keepdims=True))**2+(h-h.mean(axis=1,keepdims=True))**2,axis=1))
    delta=(np.minimum(gap_top,gap_h_top)*top+np.minimum(gap_bot,gap_h_bot)*bot)/R
    p=2/n-1/(n*(n-1))
    print('n',n,'Pdefect empirical',round(float(np.mean(delta>0)),5),'exact',round(p,5),'mean scaled gap positive using sqrt(2n) sqrt(2logn)',round(float(np.mean(delta[delta>0])*np.sqrt(2*n)*np.sqrt(2*np.log(n))),4))
print('ALL CHECKS PASSED')
