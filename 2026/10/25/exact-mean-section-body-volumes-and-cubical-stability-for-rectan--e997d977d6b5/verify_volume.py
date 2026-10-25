"""Independent numerical checks of the volume identity for sums of three orthogonal disks.
Requirements: numpy, scipy, mpmath. Prints convergence results; the proof is analytic.
"""
import math
import numpy as np
from scipy.spatial import ConvexHull
import mpmath as mp

def coeff(dps=45):
    mp.mp.dps=dps
    H=mp.hyper([-mp.mpf(1)/4,mp.mpf(1)/4,mp.mpf(1)/2],[1,1],1)
    return float(mp.sqrt(2)*mp.pi**2*H)

def exact_volume(r):
    r1,r2,r3=map(float,r)
    return 2*math.pi*sum(r[i]**2*r[j] for i in range(3) for j in range(3) if i!=j)+coeff()*r1*r2*r3

def vertices_disk(n,i,r=1.0):
    t=2*math.pi*np.arange(n)/n
    p=np.zeros((n,3),dtype=float)
    j,k=[x for x in range(3) if x!=i]
    p[:,j]=r*np.cos(t)
    p[:,k]=r*np.sin(t)
    return p

def approximate_volume(r,n):
    p=[vertices_disk(n,i,r[i]) for i in range(3)]
    pts=(p[0][:,None,None,:]+p[1][None,:,None,:]+p[2][None,None,:,:]).reshape(-1,3)
    return float(ConvexHull(pts).volume)

def check():
    c=coeff()
    # Independent double-circle quadrature of the triple mixed-volume coefficient.
    nquad=512
    ang=2*math.pi*(np.arange(nquad)+.5)/nquad
    sq=(np.cos(ang)[:,None]**2*np.sin(ang)[None,:]**2+
        np.sin(ang)[:,None]**2*np.cos(ang)[None,:]**2)
    cquad=0.5*math.sqrt(1.)*np.sqrt(sq).mean()*(2*math.pi)**2
    print('direct circle-quadrature triple coeff:',format(cquad,'.13f'))
    assert abs(cquad-c)<1e-4
    print('triple coefficient:',format(c,'.13f'))
    print('equal disk analytic:',format(exact_volume([1,1,1]),'.13f'))
    for r in ([1,1,1],[1,1.5,0.7],[0.4,1.4,2.3]):
        target=exact_volume(r)
        for n in (12,20,28):
            v=approximate_volume(r,n)
            gap=(target-v)/target
            print('r=',r,'n=',n,'poly-volume=',format(v,'.12f'),'relative deficit=',format(gap,'.7f'))
            assert 0<=gap<0.10
        assert exact_volume(r)>0
    for a,b,c in ((1,1,1),(.7,1.2,3),(3,.5,2)):
        r=[b*c,a*c,a*b]
        lo=exact_volume([1,1,1])*(a*b*c)**2
        got=exact_volume(r)
        print('box half-sides',a,b,c,'relative deficit:',got/lo-1)
        assert got>=lo-1e-10
    print('all checks passed')

if __name__=='__main__': check()
