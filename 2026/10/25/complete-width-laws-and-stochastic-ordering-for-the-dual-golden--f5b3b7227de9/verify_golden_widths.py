"""Reproduce exact directional-width laws for the two dual golden Platonic solids.

No nonstandard packages are needed. All simulated widths are computed by maximizing
raw scalar products with independently enumerated Cartesian vertices.
"""
from math import pi, sin, cos, sqrt, acos, atan2
from random import Random

PHI = (1 + sqrt(5))/2
R = sqrt((5+2*sqrt(5))/15)


def parameters(name):
    if name == 'icosahedron':
        return 12,5,1/sqrt(PHI+2)
    if name == 'dodecahedron':
        return 20,3,1/(sqrt(3)*PHI)
    raise ValueError(name)


def segment(t,c):
    if t>=c: return 0.0
    k=sqrt(1-c*c)
    b=sqrt(max(0,c*c-t*t))
    a=k*t/(c*sqrt(1-t*t))
    return 2*atan2(b,k)-2*t*acos(max(-1,min(1,a)))


def survival(name,t):
    v,q,k=parameters(name)
    c=sqrt(1-k*k)
    if t<=R: return 1.0
    if t>=1: return 0.0
    return v*(1-t)/2 -v*q*segment(t,c)/(4*pi)


def points(name):
    x=[]
    if name=='icosahedron':
        for s in (-1,1):
            for t in (-1,1):
                x.extend(((0,s,t*PHI),(s,t*PHI,0),(t*PHI,0,s)))
    else:
        for s in (-1,1):
            for t in (-1,1):
                for r in (-1,1): x.append((s,t,r))
                x.extend(((0,s/PHI,t*PHI),(s/PHI,t*PHI,0),(t*PHI,0,s/PHI)))
    assert len(x)==parameters(name)[0]
    return [tuple(a/sqrt(sum(b*b for b in y)) for a in y) for y in x]


def sim_survival(pts,thresholds,N,seed):
    rng=Random(seed)
    cnt=[0]*len(thresholds)
    for j in range(N):
        z=2*rng.random()-1
        a=2*pi*rng.random()
        s=sqrt(1-z*z)
        ux,uy,uz=s*cos(a),s*sin(a),z
        w=max(v[0]*ux+v[1]*uy+v[2]*uz for v in pts)
        for i,t in enumerate(thresholds):
            if w>t: cnt[i]+=1
    return [m/N for m in cnt]


def run():
    assert abs(R-0.7946544722917662)<1e-14
    data={}
    for name in ('icosahedron','dodecahedron'):
        V,q,k=parameters(name)
        c=sqrt(1-k*k)
        assert abs(acos(k*R/(c*sqrt(1-R*R)))-pi/q)<1e-13
        assert abs(survival(name,R)-1)<1e-12
        assert abs(survival(name,c)-V/2*(1-c))<1e-12
        assert abs(survival(name,1))<1e-12
        test=[R+0.01, R+0.03, (R+c)/2, c-0.004, c+0.004, 0.92, 0.96]
        test=sorted(set(t for t in test if R<t<1))
        values=sim_survival(points(name),test,220000,63813+V)
        for t,observed in zip(test,values):
            predicted=survival(name,t)
            sd=sqrt(max(predicted*(1-predicted),0)/220000)
            assert abs(predicted-observed)<0.0015+5*sd, (name,t,predicted,observed)
        print(name.upper()+'_EXACT_CDF_VS_RAW_VERTEX_MONTE_CARLO_OK',len(test),220000)
        data[name]=(V,q,k,c)
    for j in range(1,2000):
        t=R+(1-R)*j/2000
        assert survival('dodecahedron',t)>survival('icosahedron',t)+1e-12
    print('STRICT_STOCHASTIC_ORDER_GRID_CHECK_OK 1999')
    Vi,qi,ki,ci=data['icosahedron']
    Vd,qd,kd,cd=data['dodecahedron']
    assert Vi*qi==Vd*qd==60 and R<ci<cd<1
    def aperture(t,k):
        c=sqrt(1-k*k)
        if t>=c:return 0.0
        return acos(k*t/(c*sqrt(1-t*t)))
    assert abs(aperture(R,kd)-pi/3)<1e-13
    assert abs(aperture(R,ki)-pi/5)<1e-13
    for j in range(1,1000):
        t=R+(ci-R)*j/1000
        assert aperture(t,kd)-aperture(t,ki) > 2*pi/15
    print('ANALYTIC_STOCHASTIC_DOMINANCE_DERIVATIVE_BOUND_CHECK_OK')
    for name,(v,q,k,c) in data.items():
        coefficient=v*q*k/(4*pi*(1-R*R)*sqrt(c*c-R*R))
        assert coefficient>0
        print(name.upper()+'_LOWER_ENDPOINT_QUADRATIC_CONSTANT',format(coefficient,'.12f'))
        print(name.upper()+'_UPPER_ENDPOINT_EXACT_LINEAR_CONSTANT',v/2)
    print('ALL_GOLDEN_DUAL_PLATONIC_WIDTH_CHECKS_OK')

if __name__=='__main__':
    run()
