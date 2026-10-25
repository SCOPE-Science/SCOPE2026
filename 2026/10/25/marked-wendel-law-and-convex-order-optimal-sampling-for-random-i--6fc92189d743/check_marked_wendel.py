#!/usr/bin/env python3
"""Independent finite-n geometric and analytic checks for rare convex-hull miss depths.
Runs with numpy/scipy only, deterministic RNG. This is corroboration, not a proof.
"""
import math
import numpy as np
from scipy.special import ellipk
from scipy.integrate import quad
from scipy.spatial import ConvexHull

rng=np.random.default_rng(250602)
pi=math.pi

def r_ellipse(theta,a=2.0,b=1.0):
    return a*b/np.hypot(b*np.cos(theta),a*np.sin(theta))

# Test the exact circle miss-depth formula against UNCONDITIONED independent points.
for n in (4,7,11):
    T=np.sort(rng.uniform(0,2*pi,size=(230000,n)),axis=1)
    gaps=np.diff(np.concatenate((T,T[:,0:1]+2*pi),axis=1),axis=1)
    D=np.maximum(0,-np.cos(gaps.max(axis=1)/2))
    for cutoff in (0.01,0.25):
        theoretical=n*(math.acos(cutoff)/pi)**(n-1)
        empirical=np.mean(D>cutoff)
        tol=6*math.sqrt(max(theoretical*(1-theoretical),0.001)/len(D))+0.0004
        assert abs(empirical-theoretical)<tol,(n,cutoff,empirical,theoretical,tol)
print('UNCONDITIONED_CIRCLE_EXACT_FINITE_N_TAIL_OK')

# A general symmetric density is sampled by exact inverse-CDF to numerical precision.
# In the ellipse case theta is the RADIAL angle (not eccentric anomaly).
def make_inverse_density(density, N=50001):
    grid=np.linspace(0,2*pi,N)
    f=density(grid)
    c=np.concatenate(([0],np.cumsum((f[1:]+f[:-1])*.5*np.diff(grid))))
    c/=c[-1]
    assert abs(c[-1]-1)<1e-12
    return lambda u: np.interp(np.asarray(u)%1,c,grid)+2*pi*np.floor(np.asarray(u))

def check_model(density, label, reps=11000, a=2.0, b=1.0):
    inv=make_inverse_density(density)
    t=inv(rng.uniform(size=reps))
    R=r_ellipse(t,a,b)
    target=quad(lambda z:r_ellipse(z,a,b),0,2*pi,epsabs=1e-10)[0]/4
    target_second=quad(lambda z:r_ellipse(z,a,b)**2/density(z),0,2*pi,epsabs=1e-9)[0]/8
    target_tail=quad(lambda z:density(z)*np.exp(-4*density(z)*2/r_ellipse(z,a,b)),0,2*pi,epsabs=1e-9)[0]
    print('DENSITY',label,'limit mean/second/tail',target,target_second,target_tail)
    for n in (60,250):
        # Conditional on the hull missing the origin, the semicircle starting
        # at t contains every other point and is the unique empty-gap complement.
        # Use numerical integrated density to find the mass cdf(t); for nonuniform density,
        # anchor generation v uniform means cdf(t)=v, but easier reconstruct inverse CDF at each draw.
        # regenerate anchors alongside their cumulative masses.
        v=rng.uniform(size=reps)
        t=inv(v)
        other=inv(v[:,None]+.5*rng.uniform(size=(reps,n-1)))
        delta=t+pi-other.max(axis=1)
        X=r_ellipse(t,a,b)[:,None]*np.column_stack((np.cos(t),np.sin(t)))
        phi=t+pi-delta
        Y=r_ellipse(phi,a,b)[:,None]*np.column_stack((np.cos(phi),np.sin(phi)))
        V=Y-X
        projection=np.clip(-(X*V).sum(axis=1)/(V*V).sum(axis=1),0,1)
        distance=np.linalg.norm(X+projection[:,None]*V,axis=1)
        z=n*distance
        # The separating chord foot lies in the segment in this regime.
        assert (projection>.01).all() and (projection<.99).all()
        meanerr=abs(z.mean()-target)
        stderr=z.std(ddof=1)/math.sqrt(reps)
        assert meanerr<6*stderr +.07,(label,n,z.mean(),target,stderr)
        second_error=abs(np.mean(z*z)-target_second)
        second_se=np.std(z*z,ddof=1)/math.sqrt(reps)
        assert second_error<6*second_se +.6,(label,n,second_error,second_se)
        p=(z>2).mean()
        p_se=math.sqrt(max(0.01,p*(1-p))/reps)
        assert abs(p-target_tail)<6*p_se+.018,(label,n,p,target_tail)
        if n==250:
            print('ASYMPTOTIC_MODEL',label,'n',n,'mean',round(z.mean(),6),'second',round(np.mean(z*z),6),'P(nD>2)',round(p,6))
        # Compare with direct, independent geometric convex hull computation.
        for k in range(40):
            pts=np.vstack((X[k],r_ellipse(other[k],a,b)[:,None]*np.column_stack((np.cos(other[k]),np.sin(other[k])))))
            hull=ConvexHull(pts)
            corners=pts[hull.vertices]
            W=np.roll(corners,-1,axis=0)-corners
            w=np.clip(-np.sum(corners*W,axis=1)/np.sum(W*W,axis=1),0,1)
            D=np.min(np.linalg.norm(corners+w[:,None]*W,axis=1))
            assert abs(D-distance[k])<1e-9, (label,n,k,D,distance[k])
    print('DIRECT_HULL_AND_MARKED_OVERSHOOT',label,'OK')

circle=lambda t:np.zeros_like(np.asarray(t))+1/(2*pi)
check_model(circle,'circle',a=1,b=1)
uniform=lambda t: np.zeros_like(np.asarray(t))+1/(2*pi)
check_model(uniform,'ellipse_uniform_angle')
Z=quad(lambda t:r_ellipse(t),0,2*pi)[0]
optimal=lambda t:r_ellipse(t)/Z
check_model(optimal,'ellipse_radial_optimal')
# Strict second-moment minimizer by Cauchy-Schwarz, numerically illustrated.
I_uniform=quad(lambda t:r_ellipse(t)**2/uniform(t),0,2*pi)[0]/8
I_optimal=quad(lambda t:r_ellipse(t)**2/optimal(t),0,2*pi)[0]/8
assert I_uniform>I_optimal+1e-3 and abs(I_optimal-2*(Z/4)**2)<1e-9
print('DENSITY_FREE_FIRST_MOMENT_AND_UNIQUE_MINIMAL_SECOND_MOMENT_OK')
