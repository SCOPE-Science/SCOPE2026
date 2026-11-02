"""Deterministic and seeded tests of polygon random missing-perimeter limits.

Run: python verify.py   (requires NumPy and SciPy)
Finite tests corroborate the proof but are not a proof of the limiting theorem.
"""
import math
import numpy as np
from scipy.integrate import quad

CHECKS=0

def check_near(x,y,tol):
    global CHECKS
    assert abs(x-y)<=tol,(x,y,tol)
    CHECKS+=1

def poly_geom(poly):
    area=abs(sum(x*y2-x2*y for (x,y),(x2,y2) in zip(poly,poly[1:]+poly[:1])))/2
    peri=sum(math.hypot(x-x2,y-y2) for (x,y),(x2,y2) in zip(poly,poly[1:]+poly[:1]))
    return area,peri

def convex_hull(points):
    pts=sorted(tuple(map(float,p)) for p in points)
    def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[];hi=[]
    for p in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=1e-12:lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=1e-12:hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]

def draw_boundary(poly,N,rng):
    p=np.asarray(poly,float); vec=np.roll(p,-1,axis=0)-p
    lengths=np.linalg.norm(vec,axis=1); P=sum(lengths)
    t=rng.random(N)*P; cum=np.cumsum(lengths)
    ind=np.searchsorted(cum,t); local=t-np.r_[0,cum[:-1]][ind]
    return p[ind]+(local/lengths[ind])[:,None]*vec[ind],ind,local,lengths,P

def gap_perimeter(poly,ind,local,lengths):
    m=len(poly)
    if len(set(ind))!=m:return None
    first=[local[ind==i].min() for i in range(m)]
    last=[lengths[i]-local[ind==i].max() for i in range(m)]
    loss=0.0
    for i in range(m):
        p=np.asarray(poly[i],float)
        a=np.asarray(poly[(i-1)%m],float)-p
        b=np.asarray(poly[(i+1)%m],float)-p
        cos=float(np.dot(a,b)/np.linalg.norm(a)/np.linalg.norm(b))
        u,v=last[(i-1)%m],first[i]
        loss+=u+v-math.sqrt(max(0.0,u*u+v*v-2*u*v*cos))
    return loss

def corner_mgf(alpha,z):
    s=math.sin(alpha/2);c=math.cos(alpha/2)
    def integrand(x):
        b=1-math.sqrt(s*s+4*c*c*x*x)
        return (1-z*b)**(-2)
    return quad(integrand,-.5,.5,epsabs=1e-8,epsrel=1e-11,limit=700,points=[0])[0]

def run():
    global CHECKS
    rng=np.random.default_rng(962573)
    polys=[[(0,0),(1,0),(.3,.8)],[(0,0),(4,0),(4,1),(0,1)],
           [(0,0),(2,0),(3,1),(2,2),(0,2)],
           [(math.cos(2*math.pi*i/7),math.sin(2*math.pi*i/7)) for i in range(7)]]
    # Exact corner decomposition against an independent monotone-chain hull.
    for poly in polys:
        A,P=poly_geom(poly)
        for N in (50,150):
            for _ in range(110):
                sampled,ind,local,lengths,_=draw_boundary(poly,N,rng)
                deficit=gap_perimeter(poly,ind,local,lengths)
                if deficit is None:continue
                hull=convex_hull(sampled)
                _,p_hull=poly_geom(hull)
                check_near(P-p_hull,deficit,1e-8)
                assert deficit>=-1e-10
                CHECKS+=1
    # The exact singularity is asymptotically constant times delta**(-3/2).
    # This is the key analytic input for angle recovery, checked in five cases.
    for alpha in (math.pi/6,math.pi/3,math.pi/2,2*math.pi/3,5*math.pi/6):
        s=math.sin(alpha/2);c=math.cos(alpha/2)
        pole=1/(1-s)
        analytic=(math.pi/2)*math.sqrt(s/(2*pole*c*c))
        recovered_angle=2*math.asin(1-1/pole)
        check_near(recovered_angle,alpha,1e-14)
        for delta in (.004,.001,.0003):
            scaled=corner_mgf(alpha,pole*(1-delta))*delta**1.5
            assert abs(scaled/analytic-1)<.09,(alpha,delta,scaled,analytic)
            CHECKS+=1
    # A repeated minimum alpha contributes exact exponent 3r/2 in the
    # product MGF, while factors from larger alpha stay finite.
    for angles in ((math.pi/3,math.pi/3,math.pi/2),(.6,.6,.6,1.6),(.7,1.1,1.4)):
        poles=[1/(1-math.sin(alpha/2)) for alpha in angles]
        first=min(poles);r=sum(abs(z-first)<1e-12 for z in poles)
        def log_product(delta):
            return sum(math.log(corner_mgf(alpha,first*(1-delta))) for alpha in angles)
        delta1,delta2=.003,.0003
        exponent=(log_product(delta2)-log_product(delta1))/math.log(delta1/delta2)
        assert abs(exponent-1.5*r)<.045,(angles,exponent,r)
        CHECKS+=1
    # Right-angle one-corner mean and variance; rectangles with different
    # aspect ratios have the same limiting scaled perimeter law.
    v=math.asinh(1)
    mu=1-v/math.sqrt(2)
    var=3-2*math.sqrt(2)*v-v*v/2
    nodes,weights=np.polynomial.legendre.leggauss(240)
    t=(nodes+1)/2;wt=weights/2
    b=1-np.sqrt(t*t+(1-t)*(1-t))
    check_near(2*np.dot(wt,b),mu,1e-12)
    check_near(6*np.dot(wt,b*b)-4*np.dot(wt,b)**2,var,1e-12)
    for rect in ([(0,0),(1,0),(1,1),(0,1)],[(0,0),(4,0),(4,1),(0,1)]):
        N=700; trials=10000; obs=np.empty(trials)
        for j in range(trials):
            sam,inds,local,lengths,P=draw_boundary(rect,N,rng)
            gap=gap_perimeter(rect,inds,local,lengths)
            assert gap is not None
            obs[j]=N*gap/P
        check_near(obs.mean(),4*mu,.045)
        check_near(obs.var(),4*var,.04)
    print(f'VERIFY_OK {CHECKS} geometric, quadrature and seeded checks')
    print(f'right_angle_corner_mean={mu:.12f} variance={var:.12f}')

if __name__=='__main__':run()
