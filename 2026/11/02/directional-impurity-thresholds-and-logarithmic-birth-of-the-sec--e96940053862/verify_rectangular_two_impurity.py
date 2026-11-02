"""Finite numerical checks for anisotropic two-site lattice bound-state threshold.
Run with Python 3 plus scipy/numpy; no external files or network are required.
"""
import json
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import eigsh


def gdiff(E, r, tx, ty):
    """Half of antisymmetric Birman--Schwinger eigenvalue at E>2(tx+ty)."""
    assert tx>0 and ty>0 and E>2*(tx+ty)
    m,n=map(abs,r)
    def f(x):
        A=E-2*tx*math.cos(x)
        root=math.sqrt((A-2*ty)*(A+2*ty))
        z=(2*ty)/(A+root)
        return (1-math.cos(m*x)*z**n)/root
    return quad(f,0,math.pi,epsabs=4e-13,epsrel=4e-13,limit=300)[0]/math.pi


def directional_threshold(tx,ty,axis):
    if axis=='x':return math.pi*tx/math.atan(math.sqrt(tx/ty))
    return math.pi*ty/math.atan(math.sqrt(ty/tx))


def finite_box_second(L, V, r, tx, ty):
    N=L*L
    h=lil_matrix((N,N),dtype=float)
    def ix(x,y):return x*L+y
    for x in range(L):
        for y in range(L):
            for u,v,t in ((x+1,y,tx),(x,y+1,ty)):
                if u<L and v<L:
                    h[ix(x,y),ix(u,v)]=t
                    h[ix(u,v),ix(x,y)]=t
    a=(L//2,L//2)
    b=(a[0]+r[0],a[1]+r[1])
    h[ix(*a),ix(*a)]=V
    h[ix(*b),ix(*b)]=V
    return sorted(eigsh(h.tocsr(),k=2,which='LA',tol=1e-11,return_eigenvectors=False,
                       v0=np.random.default_rng(2077).normal(size=N)))


def gdiff_grid(E,r,tx,ty,N=160):
    """Independent full two-dimensional trapezoidal quadrature, away from band edge."""
    u=2*math.pi*(np.arange(N)+0.5)/N-math.pi
    X,Y=np.meshgrid(u,u,indexing='ij')
    integrand=(1-np.cos(r[0]*X+r[1]*Y))/(E-2*tx*np.cos(X)-2*ty*np.cos(Y))
    return float(np.mean(integrand))


def run():
    cases=[(1.,1.,(1,0),'x'),(1.,1.,(0,1),'y'),
           (3.,1.,(1,0),'x'),(3.,1.,(0,1),'y'),
           (2.,5.,(1,0),'x'),(2.,5.,(0,1),'y')]
    checks=[]
    for tx,ty,r,ax in cases:
        Vc=directional_threshold(tx,ty,ax)
        E0=2*(tx+ty)
        assert abs(gdiff(E0+1e-8,r,tx,ty)-1/Vc)<2e-8,(tx,ty,r,Vc)
        E=E0+1.75
        a=gdiff(E,r,tx,ty)
        b=gdiff_grid(E,r,tx,ty)
        assert abs(a-b)<2e-10,(a,b)
        checks.append(dict(tx=tx,ty=ty,r=r,Vc=Vc,integral_match_error=abs(a-b)))
    assert abs(directional_threshold(3,1,'x')-9)<1e-13
    assert abs(directional_threshold(3,1,'y')-6)<1e-13
    roots=[]
    for tx,ty,r,Vc in [(3.,1.,(1,0),9.),(3.,1.,(0,1),6.),(3.,1.,(1,1),None)]:
        E0=2*(tx+ty)
        if Vc is None:
            Vc=1/gdiff(E0+1e-10,r,tx,ty)
        V=Vc+2
        root=brentq(lambda E:gdiff(E,r,tx,ty)-1/V,E0+1e-9,E0+V+10,xtol=5e-13)
        box=finite_box_second(41,V,r,tx,ty)
        assert abs(box[0]-root)<0.001,(r,box,root)
        roots.append(dict(r=r,Vc=Vc,V=V,E2_infinite=root,E2_finite=box[0],error=abs(box[0]-root)))
    # Gap slope: positive difference, with slowly convergent logarithmic coefficient.
    slopes=[]
    for tx,ty,r,ax in cases[2:4]:
        E0=2*(tx+ty)
        gcrit=1/directional_threshold(tx,ty,ax)
        predicted=(r[0]**2/tx+r[1]**2/ty)/(16*math.pi*math.sqrt(tx*ty))
        last=None
        for delta in [1e-3,1e-5]:
            c=(gcrit-gdiff(E0+delta,r,tx,ty))/(delta*math.log((tx+ty)/delta))
            assert predicted*0.8<c<predicted*1.8,(r,delta,c,predicted)
            if last is not None: assert abs(c/predicted-1)<abs(last/predicted-1)
            last=c
            slopes.append(dict(r=r,delta=delta,coefficient_numeric=c,coefficient_exact=predicted))
    print(json.dumps(dict(status='PASS',directional=checks,roots=roots,edge_slopes=slopes),indent=2))

if __name__=='__main__':run()
