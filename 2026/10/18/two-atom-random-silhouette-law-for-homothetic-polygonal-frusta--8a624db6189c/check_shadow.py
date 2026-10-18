"""Reproducible numerical checks for homothetic polygon-frustum silhouette law.
Uses only numpy and scipy (ConvexHull and quad), not part of the proof.
"""
import math
import numpy as np
from scipy.spatial import ConvexHull
from scipy.integrate import quad

def regular(n,R=1):
    return np.array([(R*math.cos(2*math.pi*k/n),R*math.sin(2*math.pi*k/n)) for k in range(n)])

def p_reg(n,R,lam):
    a=2*math.pi/n
    L=math.hypot(R,lam)
    rat=R*R*math.sin(a)/(R*R*(1+math.cos(a))+2*lam*lam+2*lam*L)
    return n/math.pi * math.atan(rat)

def p_integral(n,R,lam):
    # ray polygon intersection radius in each vertex angular sector
    q=math.pi/n
    apothem=R*math.cos(q)
    def val(phi):
        theta=((phi+q)%(2*q))-q
        rho=apothem/math.cos(theta)
        return 1-lam/math.hypot(lam,rho)
    return n/math.pi * quad(val,-q,q,epsabs=5e-12)[0]/2

def count_hull(poly,t,x):
    q=np.concatenate([poly,t*poly+x],axis=0)
    return len(ConvexHull(q).vertices)

def sample(n,t,lam,N,seed):
    rng=np.random.default_rng(seed)
    P=regular(n)
    d={}
    h=lam*(1-t)
    for _ in range(N):
        normal=rng.normal(size=3)
        if abs(normal[2])<1e-12:continue
        s=-h*normal[:2]/normal[2]
        num=count_hull(P,t,s)
        d[num]=d.get(num,0)+1
    pred=p_reg(n,1.,lam)
    obs=d.get(n,0)/N
    sig=math.sqrt(pred*(1-pred)/N)
    assert set(d).issubset({n,n+2}), (n,d)
    assert abs(obs-pred)<=6*sig+0.003, (n,t,lam,d,pred,sig)
    print(f'n={n:2d} t={t:.2f} lambda={lam:.2f}: observed={obs:.5f} expected={pred:.5f}, counts={d}')

if __name__=='__main__':
    for n in [3,4,5,8,12]:
        for lam in [.1,.5,1.0,3.0]:
            p1=p_reg(n,1,lam);p2=p_integral(n,1,lam)
            assert abs(p1-p2)<1e-11,(n,lam,p1,p2)
    # exact combinatorial checks for irregular polygons & random homothetic copies
    rng=np.random.default_rng(145)
    tested=0
    for npts in [4,5,7,10,15]:
        for _ in range(5):
            pts=rng.normal(size=(npts,2)); P=pts[ConvexHull(pts).vertices]; n=len(P)
            for _ in range(90):
                t=rng.uniform(.02,.98)
                s=rng.normal(size=2)*rng.lognormal(0,1)
                c=count_hull(P,t,s)
                assert c in {n,n+2},(n,c,P.tolist(),t,s.tolist())
                tested+=1
    for i,(n,t,lam) in enumerate([(3,.25,1.),(4,.6,.4),(5,.7,2.),(6,.9,.2),(8,.15,3.),(10,.75,.8)]):
        sample(n,t,lam,3500,2026+i)
    print(f'HOMOTHETIC_FRUSTUM_SHADOW_OK area_integrals={20} irregular_hulls={tested} monte_carlo={6*3500}')
