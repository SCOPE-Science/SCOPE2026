"""Reproducible checks for a shared-apex sample-diameter limit law.
Requires Python 3 plus SciPy and NumPy; all geometry calculations are independent.
Numerical tests supplement, but do not replace, the analytic proof.
"""
import math
from fractions import Fraction
from scipy.integrate import quad, dblquad
from scipy.spatial import ConvexHull, distance
import numpy as np


def clip(poly, a, b, h):
    """Clip polygon to a*x+b*y<=h using rational arithmetic."""
    if not poly:
        return []
    result=[]
    prev=poly[-1]
    prevf=a*prev[0]+b*prev[1]-h
    for cur in poly:
        curf=a*cur[0]+b*cur[1]-h
        if (prevf<0 and curf>0) or (prevf>0 and curf<0):
            t=prevf/(prevf-curf)
            result.append((prev[0]+t*(cur[0]-prev[0]),prev[1]+t*(cur[1]-prev[1])))
        if curf==0 and (not result or result[-1]!=cur):
            result.append(cur)
        elif curf<0:
            result.append(cur)
        prev,prevf=cur,curf
    return result


def polygon_area(p):
    if not p:
        return Fraction(0)
    return abs(sum(p[i][0]*p[(i+1)%len(p)][1]-p[(i+1)%len(p)][0]*p[i][1]
                   for i in range(len(p)))/2)


def q_formula(c,s,t):
    if t<=c*s:
        return s*s/c
    if s<=c*t:
        return t*t/c
    return ((s*s+t*t)/c-2*s*t)/(1-c*c)


def check_union():
    n=0
    for c in [Fraction(1,2), Fraction(3,5), Fraction(3,4), Fraction(9,10)]:
        for s in [Fraction(i,7) for i in range(1,16)]:
            for t in [Fraction(j,9) for j in range(1,16)]:
                T1=[(Fraction(0),Fraction(0)),(s,Fraction(0)),(Fraction(0),s/c)]
                T2=[(Fraction(0),Fraction(0)),(t/c,Fraction(0)),(Fraction(0),t)]
                cap=clip(T1,c,Fraction(1),t)
                area=polygon_area(T1)+polygon_area(T2)-polygon_area(cap)
                assert 2*area==q_formula(c,s,t),(c,s,t,area)
                n+=1
    return n


def survival(c,z,delta=0):
    lam=1/(1-c)
    w=max(0,z-delta)
    g=lambda y,s:2*lam*(y-s)*math.exp(-lam*(y-s)**2)
    iz=quad(lambda s:g(z,s)*math.exp(-s*s/c),0,z,epsabs=3e-10)[0]
    iw=quad(lambda s:g(w,s)*math.exp(-s*s/c),0,w,epsabs=3e-10)[0]
    both=dblquad(lambda t,s:g(z,s)*g(w,t)*math.exp(-q_formula(c,s,t)),0,z,lambda s:0,lambda s:w,epsabs=3e-9)[0] if w>0 else 0.0
    ans=math.exp(-lam*(z*z+w*w))+math.exp(-lam*w*w)*iz+math.exp(-lam*z*z)*iw+both
    hz=math.exp(-lam*z*z)+iz
    if delta==0:
        assert ans>=hz*hz-1e-9
        if z>0:
            assert ans>hz*hz
    if delta>=z:
        assert abs(ans-hz)<1e-9
    return ans


def hull_diameter(points):
    hull=points[ConvexHull(points).vertices]
    return np.max(distance.pdist(hull))


def monte_carlo_gamma(c, n=700, reps=1000):
    rng=np.random.default_rng(670013)
    sin=math.sqrt(1-c*c)
    B=np.array([1.,0.]); C=np.array([c,sin]); A=np.array([0.,0.])
    limits=[]
    for _ in range(reps):
        uv=rng.random((n,2)); mask=(uv[:,0]+uv[:,1]>1)
        uv[mask]=1-uv[mask]
        pts=uv[:,0,None]*B[None,:]+uv[:,1,None]*C[None,:]
        limits.append(math.sqrt(n)*(1-hull_diameter(pts)))
    out=[]
    for z in [.40,.70,1.0]:
        theo=survival(c,z)
        empirical=np.mean(np.asarray(limits)>z)
        # Quantitative diagnostic tolerance deliberately generous for n finite.
        assert abs(theo-empirical)<.14,(z,theo,empirical)
        out.append((z,round(theo,5),round(empirical,5)))
    return out


if __name__ == '__main__':
    k=check_union()
    print('exact rational union-area identities:',k)
    for c in [.55,.7,.9]:
        print('survivals c=',c,[round(survival(c,z,0),7) for z in [.3,.6,1.0]])
        print('split c=',c,[round(survival(c,.9,delta),7) for delta in [0,.4,.9,1.5]])
    print('finite n hull simulations:',monte_carlo_gamma(.75))
