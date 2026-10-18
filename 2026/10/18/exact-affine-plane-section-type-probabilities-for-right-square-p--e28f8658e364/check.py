import math
import numpy as np
from scipy.spatial import ConvexHull
from collections import defaultdict

def mean_width_poly(V):
    h=ConvexHull(np.asarray(V,float))
    E=defaultdict(list)
    for k,t in enumerate(h.simplices):
        for i in range(3): E[tuple(sorted((t[i],t[(i+1)%3])))].append(k)
    ans=0.
    for (i,j),F in E.items():
        if len(F)!=2: raise ValueError('nonmanifold hull')
        a,b=h.equations[F,:3]
        angle=math.acos(float(np.clip(a@b,-1,1)))
        ans+=math.dist(V[i],V[j])*angle
    return ans/(4*math.pi)

def closed(h):
    r=math.sqrt(1+h*h);s=math.sqrt(2+h*h)
    D=math.acos(1/r); beta=math.pi-D; gamma=math.acos(1/r**2)
    den=2*beta+s*gamma
    p5=(2*s*math.asin(1/r**2)+4*D-math.pi*math.sqrt(2))/den
    mw=den/math.pi
    EN=2*(2+s)/mw
    p3=4-EN+p5; p4=EN-3-2*p5
    return np.array([p3,p4,p5]),mw

def geometry(h):
    base=np.array([[1,1,0],[-1,1,0],[-1,-1,0],[1,-1,0]],float)
    apex=np.array([0.,0.,h]);P=np.vstack((base,apex))
    Q=np.vstack((base[1:]-apex,base[1:]-base[0]));Q0=np.vstack((Q,[0,0,0]))
    wp=mean_width_poly(P);gap=mean_width_poly(Q0)-mean_width_poly(Q)
    return 4*gap/wp,wp,P

def montecarlo(h,N=280000,seed=567):
    rng=np.random.default_rng(seed)
    q=rng.normal(size=(N,3));q/=np.linalg.norm(q,axis=1)[:,None]
    P=np.array([[1,1,0],[-1,1,0],[-1,-1,0],[1,-1,0],[0,0,h]],float)
    proj=q@P.T;mi=proj.min(axis=1);ma=proj.max(axis=1); widths=ma-mi
    t=mi+rng.random(N)*widths
    signs=proj>t[:,None]
    E=[(0,1),(1,2),(2,3),(3,0),(0,4),(1,4),(2,4),(3,4)]
    edges=np.zeros(N,dtype=int)
    for i,j in E:edges+=signs[:,i]!=signs[:,j]
    return np.array([widths[edges==k].sum()/widths.sum() for k in (3,4,5)])
if __name__=='__main__':
    for h in (0.25,1,2,3,6):
        p,mw=closed(h);p5g,mwg,_=geometry(h);mc=montecarlo(h)
        print(h,'closed',p,'polytope_width',p5g,mwg,'mc',mc,'err',np.max(abs(mc-p)))
        assert abs(mw-mwg)<1e-10
        assert abs(p[2]-p5g)<1e-6
        assert np.max(abs(mc-p))<0.006
