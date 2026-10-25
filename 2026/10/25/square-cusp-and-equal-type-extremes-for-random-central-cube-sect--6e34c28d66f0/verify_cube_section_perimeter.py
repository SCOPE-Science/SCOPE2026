"""Independent geometric checks for a marked near-maximal cube-section perimeter law.
Run with Python 3, NumPy and SciPy installed. Finite tests support, not replace, the proof.
"""
import itertools
import math
import numpy as np

ROOT2=math.sqrt(2)
PMAX=4*(1+ROOT2)
TAILC=3*ROOT2/(8*math.pi)


def perimeter(a,b,c):
    a,b,c=sorted((abs(float(a)),abs(float(b)),abs(float(c))),reverse=True)
    assert b>0 and c>0
    if a>=b+c:
        return 4*(math.hypot(a,b)+math.hypot(a,c))/a,4
    return 2*((a+b-c)*math.hypot(a,b)/(a*b)
             +(a+c-b)*math.hypot(a,c)/(a*c)
             +(b+c-a)*math.hypot(b,c)/(b*c)),6


def perimeter_direct(normal):
    n=np.asarray(normal,dtype=float)
    n=n/np.linalg.norm(n)
    pts=[]
    for i in range(3):
        j,k=[h for h in range(3) if h!=i]
        for y,z in itertools.product((-1.,1.),repeat=2):
            p=np.zeros(3)
            p[j],p[k]=y,z
            p[i]=-(n[j]*y+n[k]*z)/n[i]
            if -1.-1e-12<=p[i]<=1.+1e-12:
                pts.append(p)
    a=np.array([1.,0.,0.])
    if abs(np.dot(n,a))>.9:a=np.array([0.,1.,0.])
    a-=np.dot(a,n)*n;a/=np.linalg.norm(a)
    b=np.cross(n,a)
    coords=sorted({(round(float(np.dot(x,a)),11),round(float(np.dot(x,b)),11)) for x in pts})
    def cross(o,x,y):return (x[0]-o[0])*(y[1]-o[1])-(x[1]-o[1])*(y[0]-o[0])
    lower=[]
    for x in coords:
        while len(lower)>=2 and cross(lower[-2],lower[-1],x)<=0:lower.pop()
        lower.append(x)
    upper=[]
    for x in reversed(coords):
        while len(upper)>=2 and cross(upper[-2],upper[-1],x)<=0:upper.pop()
        upper.append(x)
    hull=lower[:-1]+upper[:-1]
    return sum(math.dist(hull[i],hull[(i+1)%len(hull)]) for i in range(len(hull))),len(hull)


def area_jacobian_numeric(r,q):
    v=np.array([1+r,1.,q])
    return abs(np.linalg.det(np.column_stack((v,[1.,0.,0.],[0.,0.,1.])))) / np.linalg.norm(v)**3


def check():
    rng=np.random.default_rng(2323)
    for _ in range(650):
        n=rng.normal(size=3)
        if min(abs(n))<1e-3:continue
        p,edges=perimeter(*n)
        gd,gn=perimeter_direct(n)
        assert abs(p-gd)<5e-9,(p,gd,n)
        assert edges==gn
    print('INDEPENDENT_FACE_EDGE_HULL_RECONSTRUCTION_OK 650')
    assert abs(area_jacobian_numeric(0.,0.)-1/(2*ROOT2))<1e-14
    for t in (1e-3,1e-4,1e-5):
        for s in np.linspace(0.0,1.0,11):
            for r,q in ((s*t,t),(t,s*t)):
                if q==0:q=1e-14
                loss=PMAX-perimeter(1+r,1,q)[0]
                assert abs(loss-2*ROOT2*max(r,q))<30*t*t
    print('UNIFORM_TWO_CHAMBER_FIRST_ORDER_CUSP_OK')
    # An independent Haar normal check, without reweighting the sorted chambers.
    n=rng.normal(size=(3_200_000,3))
    ab=np.sort(np.abs(n),axis=1)[:,::-1]
    a,b,c=ab.T
    rect=a>=b+c
    p=np.empty(len(a))
    p[rect]=4*(np.hypot(a[rect],b[rect])+np.hypot(a[rect],c[rect]))/a[rect]
    h=~rect
    p[h]=2*((a[h]+b[h]-c[h])*np.hypot(a[h],b[h])/(a[h]*b[h])
          +(a[h]+c[h]-b[h])*np.hypot(a[h],c[h])/(a[h]*c[h])
          +(b[h]+c[h]-a[h])*np.hypot(b[h],c[h])/(b[h]*c[h]))
    for eps in (.25,.16,.11):
        flag=p>PMAX-eps
        count=int(flag.sum())
        ratio=(count/len(n))/(TAILC*eps*eps)
        fraction=float((~rect[flag]).mean())
        assert count>2000,(eps,count)
        assert abs(ratio-1)<.21,(eps,count,ratio)
        assert abs(fraction-.5)<.055,(eps,count,fraction)
        print('HAAR_TAIL_SUPPORT_SPLIT',eps,count,round(ratio,5),round(fraction,5))
    print('ALL_NEAR_MAXIMUM_CUBE_SECTION_CHECKS_OK')

if __name__=='__main__':
    check()
