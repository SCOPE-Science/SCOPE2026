"""Independent computational checks for isotropic affine sections of rectangular boxes.
Run: python checker.py ; requires numpy and mpmath. Finite checks complement an analytic proof.
"""
import math
import numpy as np


def exact_type_law(a,b,c):
    assert min(a,b,c)>0
    s=a+b+c
    d=math.sqrt(a*a*b*b+b*b*c*c+c*c*a*a)
    pairs=((a,b),(a,c),(b,c))
    t=s/2-sum(math.hypot(x,y)*math.acos(min(1.,x*y/d)) for x,y in pairs)/math.pi
    def defect(x,y,z):
        xy=math.hypot(x,y); xz=math.hypot(x,z)
        return (math.sqrt(x*x+y*y+z*z)*math.acos(y*z/(xy*xz))
                -z*math.atan2(x,y)-y*math.atan2(x,z))/math.pi
    q=1.5*s-sum(math.hypot(x,y) for x,y in pairs)-2*t
    q+=defect(a,b,c)+defect(b,a,c)+defect(c,a,b)
    p3=4*t/s; p6=2*q/s
    return np.array((p3,1-2*p3+p6,p3-2*p6,p6))


def independent_edge_count(u,t,half):
    # For each edge of the solid, intersect the defining plane with its endpoints.
    counts=np.zeros(u.shape[0],dtype=np.int16)
    for i in range(3):
        j,k=[l for l in range(3) if l!=i]
        for sj in (-1,1):
            for sk in (-1,1):
                base=sj*half[j]*u[:,j]+sk*half[k]*u[:,k]-t
                counts+=((base-half[i]*u[:,i])*(base+half[i]*u[:,i])<0)
    return counts


def check():
    rng=np.random.default_rng(20261017)
    cases=((1.,1.,1.),(.8,1.,1.2),(.3,1.1,1.6),(.10,.8,1.9),(2.6,.2,.2))
    checked=0
    for half in cases:
        p=exact_type_law(*half)
        assert (p>0).all() and abs(sum(p)-1)<2e-13
        assert abs(np.dot(p,np.arange(3,7))-4)<2e-13
        n=250000
        u=rng.standard_normal((n,3));u/=np.linalg.norm(u,axis=1)[:,None]
        h=np.abs(u*half).sum(axis=1)
        t=(rng.random(n)*2-1)*h
        nverts=independent_edge_count(u,t,half)
        assert nverts.min()==3 and nverts.max()==6
        # Invariant kinematic measure: normal density weighted by its hitting width.
        observed=np.array([(h*(nverts==k)).sum()/h.sum() for k in range(3,7)])
        assert np.max(np.abs(p-observed))<0.006,(half,p,observed)
        checked+=n
    cube=exact_type_law(1.,1.,1.)
    phi=math.acos(1/math.sqrt(3))
    assert abs(cube[0]-(2-4*math.sqrt(2)*phi/math.pi))<1e-13
    assert abs(cube[3]-(2/math.sqrt(3)-2*math.sqrt(2)+4*math.sqrt(2)*phi/math.pi))<1e-13
    assert exact_type_law(1.,1.,1.)[0]>exact_type_law(.8,1.,1.2)[0]
    assert exact_type_law(.8,1.,1.2)[0]>exact_type_law(.3,1.1,1.6)[0]
    # Independent arbitrary-precision near-flat evaluation of the closed formula.
    import mpmath as mp
    mp.mp.dps=65
    flat_checks=0
    for aa,bb in ((1,1),(.7,1.5),(3,2)):
        a,b,c=mp.mpf(str(aa)),mp.mpf(str(bb)),mp.mpf('0.0001')
        s=a+b+c; delta=mp.sqrt(a*a*b*b+a*a*c*c+b*b*c*c)
        pairs=((a,b),(a,c),(b,c))
        t=s/2-sum(mp.sqrt(x*x+y*y)*mp.acos(x*y/delta) for x,y in pairs)/mp.pi
        def defect(x,y,z):
            return (mp.sqrt(x*x+y*y+z*z)*mp.acos(y*z/(mp.sqrt(x*x+y*y)*mp.sqrt(x*x+z*z)))-z*mp.atan(x/y)-y*mp.atan(x/z))/mp.pi
        q=3*s/2-sum(mp.sqrt(x*x+y*y) for x,y in pairs)-2*t+defect(a,b,c)+defect(b,a,c)+defect(c,a,b)
        ratio=(2*q/s)/(c*c)
        predicted=1/((a+b)*mp.sqrt(a*a+b*b))
        assert abs(ratio/predicted-1)<mp.mpf('0.0003'),(aa,bb,ratio,predicted)
        flat_checks+=1
    print('AFFINE_BOX_SECTION_LAW_OK independent_edge_checks=',checked,' flattening_checks=',flat_checks,' cube=',','.join(f'{x:.10f}' for x in cube))

if __name__=='__main__':check()
