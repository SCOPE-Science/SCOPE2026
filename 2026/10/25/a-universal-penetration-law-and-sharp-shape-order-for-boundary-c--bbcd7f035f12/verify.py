"""Independent numerical checks for the centroidal triangle-core chord law.

Run with Python >=3.9; uses standard library only. Numerical checks are
supplementary, not a proof of the continuum formula.
"""
import math
import random


def q(t):
    if t <= 0:
        return 0.0
    if t >= 1:
        return 1.0
    a = (1-t)/3
    c = 1 - 2*a
    return 1 - 2*a - 3*a*a - 2*a*a*math.log((1-a)/a) + 2*a*c*math.log((1-a)/c)


def sides_and_weights(verts):
    length = [math.dist(verts[i], verts[(i+1) % 3]) for i in range(3)]
    perimeter = sum(length)
    return length, [x/perimeter for x in length]


def random_edge_point(verts, weights, rng):
    r=rng.random()
    edge = 0 if r < weights[0] else (1 if r < weights[0]+weights[1] else 2)
    u=rng.random()
    a,b=verts[edge],verts[(edge+1)%3]
    return edge, ((1-u)*a[0]+u*b[0], (1-u)*a[1]+u*b[1])


def barycentric(verts, x):
    a,b,c=verts
    det=(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    y1=((x[0]-a[0])*(c[1]-a[1])-(x[1]-a[1])*(c[0]-a[0]))/det
    y2=((b[0]-a[0])*(x[1]-a[1])-(b[1]-a[1])*(x[0]-a[0]))/det
    return (1-y1-y2,y1,y2)


def hits_core(verts, p0, p1, t):
    a=(1-t)/3
    lower,upper=0.0,1.0
    b0,b1=barycentric(verts,p0),barycentric(verts,p1)
    for x,y in zip(b0,b1):
        delta=y-x
        if delta>1.e-13:
            lower=max(lower,(a-x)/delta)
        elif delta < -1.e-13:
            upper=min(upper,(a-x)/delta)
        elif x<a-1.e-13:
            return False
    return lower<=upper+1.e-12


def check_one(verts, nsim, seed):
    rng=random.Random(seed)
    _,weights=sides_and_weights(verts)
    sigma=sum(w*w for w in weights)
    ts=[0.05,0.2,0.5,0.8,0.95]
    hits=[0]*len(ts)
    for _ in range(nsim):
        i,p=random_edge_point(verts,weights,rng)
        j,z=random_edge_point(verts,weights,rng)
        for k,t in enumerate(ts):
            hits[k]+=hits_core(verts,p,z,t)
    for t,k in zip(ts,hits):
        observed=k/nsim
        predicted=(1-sigma)*q(t)
        zscore=abs(observed-predicted)/math.sqrt(max(predicted*(1-predicted),1.e-8)/nsim)
        print(f't={t:.2f} observed={observed:.6f} predicted={predicted:.6f} z={zscore:.2f}')
        assert zscore<5, 'Failed Monte Carlo sanity check'


def check_conditional_direct(n=100000):
    rng=random.Random(8421)
    ts=[0.05,0.20,0.50,0.80,0.95]
    counts=[0]*len(ts)
    for _ in range(n):
        u,v=rng.random(),rng.random()
        for i,t in enumerate(ts):
            a=(1-t)/3
            mn=a*(1/u+1/v)
            mx=(1-2*a)/min(u,v)+a/max(u,v)
            counts[i]+=mn<=1<=mx
    for t,k in zip(ts,counts):
        observed=k/n
        theoretical=q(t)
        zscore=abs(observed-theoretical)/math.sqrt(theoretical*(1-theoretical)/n)
        print(f'conditional t={t:.2f}, observed={observed:.6f}, theoretical={theoretical:.6f}, z={zscore:.2f}')
        assert zscore<5


if __name__=='__main__':
    check_conditional_direct(100000)
    for j,v in enumerate([
        [(0.,0.),(1.,0.),(0.5, math.sqrt(3)/2)],
        [(0.,0.),(3.,0.),(0.5,1.7)],
        [(0.,0.),(4.,0.),(1.0,.08)]
    ]):
        print('Triangle',j+1)
        check_one(v, nsim=35000, seed=103+j)
    print('All supplementary checks passed.')
