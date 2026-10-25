import math
import numpy as np
from scipy.integrate import quad
from shapely.geometry import Polygon

# Independent polygon boundary intersection for the rounded polygon: piecewise straight segments approximate the circular arcs.
def chord_at_depth(polyverts, theta, depth):
    c,s=math.cos(theta),math.sin(theta)
    n=np.array([c,s]); t=np.array([-s,c])
    v=np.asarray(polyverts)
    coords=v@n; y=v@t
    p=coords.max()-depth
    va=coords; vb=np.roll(coords,-1)
    q=(p-va)/(vb-va+1e-300)
    ix=(q>=0)&(q<=1)&(np.abs(vb-va)>1e-12)
    ys=y[ix]+q[ix]*(np.roll(y,-1)[ix]-y[ix])
    return (ys.max()-ys.min()) if len(ys)>=2 else 0.0

def direct_cdf(poly,r,s,N=600):
    ring=Polygon(poly).buffer(r,quad_segs=128).exterior.coords
    v=np.array(ring[:-1])
    total=0.
    for i in range(N):
        theta=2*math.pi*(i+.5)/N
        lo,hi=0.,r*s*10
        # chord should increase at small depth; if side normals very close, root starts at depth zero; ignore negligible measure.
        for _ in range(27):
            mid=(lo+hi)*.5
            if chord_at_depth(v,theta,mid) < r*s: lo=mid
            else: hi=mid
        total+=.5*(lo+hi)
    edges=np.roll(np.array(poly),-1,axis=0)-np.array(poly)
    P=np.linalg.norm(edges,axis=1).sum()
    return 2*math.pi*total/N/(P+2*math.pi*r)

def h_c(s): return 1-math.sqrt(1-s*s/4)
def h_m(s,a): return 1-(1-s*math.sin(a))*math.cos(a) - math.sin(a)*math.sqrt(max(0,s*math.sin(a)*(2-s*math.sin(a))))
def B(s):
    A=math.asin(s/2)
    val=quad(lambda a:h_m(s,a)-h_c(s),0,A,epsabs=1e-13)[0]
    return 2*val

def theory(P,m,r,s): return r*(2*math.pi*h_c(s)+m*B(s))/(P+2*math.pi*r)

if __name__=='__main__':
    sq=[(-.5,-.5),(.5,-.5),(.5,.5),(-.5,.5)]
    rec=[(-.75,-.25),(.75,-.25),(.75,.25),(-.75,.25)]
    tri=[(0,1),(-math.sqrt(3)/2,-.5),(math.sqrt(3)/2,-.5)]
    eqtri=np.array(tri)*4/(3*math.sqrt(3)) # perimeter four
    pars=[('square',sq),('rectangle',rec),('triangle',eqtri)]
    r=.025;s=.6
    for name,vs in pars:
        p=np.sum(np.linalg.norm(np.roll(np.asarray(vs),-1,axis=0)-vs,axis=1))
        d=direct_cdf(vs,r,s,N=200)
        a=theory(p,len(vs),r,s)
        assert abs(d-a)/a < .016,(name,d,a)
        print(name,'direct',d,'formula',a,'relative_error',abs(d-a)/a)
    for s in [.04,.07,.11]:
        assert abs(B(s)/(s**3)+1/30)<.0002
    print('ROUNDED_POLYGON_CROFTON_NUMERICAL_CHECKS_OK')
