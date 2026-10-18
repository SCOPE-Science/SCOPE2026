"""Computational cross-checks of exact central-section area formulas for the tricylinder.

Usage: python check_tricylinder.py
Requires NumPy; standard-library math handles the elementary angles.
"""
import math
import numpy as np

E=np.eye(3)

def basis(normal):
    n=np.array(normal, dtype=float)
    n=n/np.linalg.norm(n)
    j=int(np.argmax(abs(n)))
    q=E[(j+1)%3]
    e=np.cross(n,q);e/=np.linalg.norm(e)
    f=np.cross(n,e)
    return n,e,f

def exact_arctangent_area(normal):
    n,e,f=basis(normal)
    if np.min(abs(n))<1e-11:
        raise ValueError('Requires three nonzero normal coordinates; use limit or direct integral at boundary')
    rays=[]
    for i in range(3):
        for j in range(i+1,3):
            for s in [-1,1]:
                w=np.cross(n,E[i]-s*E[j]); w/=np.linalg.norm(w)
                rays.extend((w,-w))
    rays.sort(key=lambda w: math.atan2(w@f,w@e)%(2*math.pi))
    area=0
    for h,a in enumerate(rays):
        b=rays[(h+1)%len(rays)]
        m=(a+b)/np.linalg.norm(a+b)
        i=int(np.argmin(abs(m)))
        d=float(np.dot(n,np.cross(a,b)))
        if d<=0: raise AssertionError(('wedge orientation',d))
        k=abs(n[i]);v=float(a@b-a[i]*b[i])
        area+=math.atan2(k*d,v)/(2*k)
    return area

def polar_area(normal,n_angles=160000):
    n,e,f=basis(normal)
    angles=(np.arange(n_angles)+0.5)*(2*math.pi/n_angles)
    u=np.cos(angles)[:,None]*e+np.sin(angles)[:,None]*f
    return math.pi*np.mean(1/(1-np.min(u*u,axis=1)))

# Another check integrates the planar section's radial boundary as a polygon,
# without reusing the arctangent sector formula.
def polygon_area(normal,n_angles=200000):
    n,e,f=basis(normal)
    a=(np.arange(n_angles)+0.5)*(2*math.pi/n_angles)
    u=np.cos(a)[:,None]*e+np.sin(a)[:,None]*f
    rho=1/np.sqrt(1-np.min(u*u,axis=1))
    vertices=rho[:,None]*u
    return 0.5*np.sum(np.einsum('ij,j->i',np.cross(vertices,np.roll(vertices,-1,axis=0)),n))

if __name__=='__main__':
    rng=np.random.default_rng(81233)
    err1=err2=0
    for t in range(240):
        n=rng.uniform(.02,2,size=3)*rng.choice([-1,1],size=3)
        e=exact_arctangent_area(n)
        p=polar_area(n)
        err1=max(err1,abs(e-p))
        if t<24:
            pg=polygon_area(n,60000)
            err2=max(err2,abs(e-pg))
    assert err1<2e-8,(err1,'quadrature')
    assert err2<1e-6,(err2,'polygon')
    for nn,target in [([1,0,0],math.pi),([1,1,0],math.sqrt(2)*(1+math.pi/2)),([1,1,1],6*math.sqrt(3)*math.atan(1/3))]:
        assert abs(polar_area(nn)-target)<2e-8,(nn,polar_area(nn),target)
        assert abs(polygon_area(nn,100000)-target)<2e-8
    # Directional cubic expansion: error after subtracting through order three is O(delta^4).
    for p,q in [(1,0),(0,1),(1/math.sqrt(2),1/math.sqrt(2)),(.6,.8)]:
        target=-(4/3)*(abs(p)**3+abs(q)**3)
        diagnostics=[]
        for d in [.04,.02,.01]:
            n=[d*p,d*q,math.sqrt(1-d*d)]
            actual=exact_arctangent_area(n) if min(abs(x) for x in n)>1e-11 else polar_area(n)
            coefficient=(actual-math.pi-.5*math.pi*d*d)/(d*d*d)
            diagnostics.append((d,coefficient))
            assert abs(coefficient-target)<3*d,(p,q,d,coefficient,target)
        print('CUBIC_ASYMPTOTIC',p,q,'target',target,'estimates',diagnostics)
    print('ARCTANGENT_VS_QUADRATURE_OK cases=240 max_error=',err1)
    print('ARCTANGENT_VS_POLYGON_OK cases=24 max_error=',err2)
    print('EXACT_SYMMETRY_SECTION_AREAS_OK')
    print('TRICYLINDER_ALL_CHECKS_OK')
