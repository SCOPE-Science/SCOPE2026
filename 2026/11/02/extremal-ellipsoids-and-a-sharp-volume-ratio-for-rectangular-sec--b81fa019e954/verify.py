"""Reproduce numerical checks for the all-dimensional coaxial-cylinder ellipsoid law.
No input files or random-seed dependencies. Requires Python 3 standard library;
optional independent SLSQP solve uses SciPy when installed.
"""
import math, random

def shape(radii):
    radii = list(map(float, radii))
    m=len(radii); d=m+1; b=min(radii)
    c=[(a/b)**2 for a in radii]
    def fun(t): return t*sum(1.0/(d*v-t) for v in c)-1.0
    lo,hi=0.0, d/2
    for _ in range(120):
        mid=(lo+hi)/2
        if fun(mid)>0:hi=mid
        else:lo=mid
    t=(lo+hi)/2
    axes=[math.sqrt(d*a*a-t*b*b) for a in radii]+[b*math.sqrt(t)]
    ratio=math.prod(axes)/(math.prod(radii)*b)
    return t,axes,ratio

def check(radii, rng):
    m=len(radii);d=m+1;b=min(radii)
    t,axes,ratio=shape(radii)
    err=abs(t*sum(b*b/(d*a*a-t*b*b) for a in radii)-1.0)
    w0=(d-t)/d;w1=t/d
    for i,a in enumerate(radii):
        # Isotropic contact measure, diagonal second moments in normalized coords.
        val=(w0*a*a+w1*(a*a-b*b))/axes[i]**2
        err=max(err,abs(val-1/d))
    err=max(err,abs(w1*b*b/axes[-1]**2-1/d))
    for step in range(25):
        z=(2*rng.random()-1)*b
        vals=[(2*rng.random()-1)*math.sqrt(a*a-z*z) for a in radii]
        q=sum((v/s)**2 for v,s in zip(vals+[z],axes))
        err=max(err,max(0,q-1))
    for step in range(20):
        z=(2*rng.random()-1)*b
        ridge=[math.sqrt(a*a-z*z)*(-1 if rng.randrange(2) else 1) for a in radii]
        q=sum((v/s)**2 for v,s in zip(ridge+[z],axes))
        err=max(err,abs(q-1))
    assert abs(t*sum(b*b/(d*a*a-t*b*b) for a in radii)-1)<4e-13
    assert err<2e-12,(radii,err)
    assert m**(m/2)*(1-1e-12) <=ratio<=d**(d/2)/2*(1+1e-12)
    return err

def main():
    rng=random.Random(1729)
    largest=0.; N=0
    for m in range(2,13):
        for j in range(30):
            radii=[1.]+[math.exp(rng.uniform(0,5)) for _ in range(m-1)]
            if j==0:radii=[1.]*m
            rng.shuffle(radii)
            largest=max(largest,check(radii,rng));N+=1
    assert abs(shape([1.,1.])[2]-2)<1e-12
    assert abs(shape([1.,1.,1.])[2]-3**1.5)<1e-12
    assert abs(shape([1.,1e8])[2]-(3**1.5/2))<1e-8
    print('STANDARD-LIBRARY CHECKS PASS; configurations:',N,'largest normalized residual:',largest)
    try:
        import numpy as np
        from scipy.optimize import minimize
    except ImportError:
        print('Independent SciPy constrained solve skipped: unavailable')
        return
    worst=0
    for m in range(2,9):
        for j in range(12):
            a=np.array([1.]+[math.exp(rng.uniform(0,2)) for _ in range(m-1)])
            rng.shuffle(a); b=min(a); d=m+1
            c=(a/b)**2
            t,ax,ratio=shape(a)
            analytic=np.r_[a*a/(np.array(ax[:-1])**2), b*b/(ax[-1]**2)]
            def obj(x):return -float(np.log(x).sum())
            def grad(x):return -1/x
            def cons0(x):return 1-float(np.sum(x[:-1]))
            def cons1(x):return 1-float(np.dot(1-1/c,x[:-1])+x[-1])
            res=minimize(obj,analytic*0.9,jac=grad,
                constraints=[{'type':'ineq','fun':cons0,'jac':lambda x:np.r_[-np.ones(m),0]},
                             {'type':'ineq','fun':cons1,'jac':lambda x:np.r_[-(1-1/c),-1]}],
                bounds=[(1e-12,None)]*(m+1),method='SLSQP',
                options={'maxiter':500,'ftol':1e-12})
            if abs(res.fun-obj(analytic))>4e-9 or min(res.x)<0 or cons0(res.x)<-1e-9 or cons1(res.x)<-1e-9:
                raise AssertionError((m,j,res.message,res.fun,obj(analytic)))
            worst=max(worst,float(np.max(np.abs(res.x/analytic-1))))
            assert worst<4e-5,(worst,m,j)
    print('INDEPENDENT CONVEX OPTIMIZATION CHECKS PASS; cases:',7*12,'max relative precision discrepancy:',worst)
if __name__=='__main__':main()
