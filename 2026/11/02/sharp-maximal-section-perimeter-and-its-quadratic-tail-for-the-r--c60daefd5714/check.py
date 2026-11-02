#!/usr/bin/env python3
"""Independent finite checks of the rhombic-dodecahedron section-perimeter theorem.
Only Python's standard library; the theorem's infinite assertions are proved in RESULT.md.
"""
import itertools, math, random
V=[]
for i in range(3):
    for s in (-1.,1.):
        p=[0.,0.,0.];p[i]=2*s;V.append(tuple(p))
for signs in itertools.product((-1.,1.),repeat=3): V.append(tuple(signs))
E=[(i,j) for i in range(6) for j in range(6,14) if abs(sum(V[i][k]*V[j][k] for k in range(3))-2)<1e-12]
assert len(E)==24

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def section_perimeter(n):
    nm=math.sqrt(dot(n,n));n=tuple(z/nm for z in n)
    basis=(1.,0.,0.) if abs(n[0])<.7 else (0.,1.,0.)
    e=cross(n,basis);t=math.sqrt(dot(e,e));e=tuple(z/t for z in e);f=cross(n,e)
    vals=[dot(n,p) for p in V]
    pts=[]
    for i,j in E:
        a,b=vals[i],vals[j]
        if a*b<-1e-14:
            t=a/(a-b)
            x=tuple(V[i][k]+t*(V[j][k]-V[i][k]) for k in range(3))
            pts.append((dot(x,e),dot(x,f)))
        elif abs(a)<1e-14:pts.append((dot(V[i],e),dot(V[i],f)))
        elif abs(b)<1e-14:pts.append((dot(V[j],e),dot(V[j],f)))
    pts=sorted(set((round(x,12),round(y,12)) for x,y in pts))
    def ccw(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    low=[]
    for p in pts:
        while len(low)>=2 and ccw(low[-2],low[-1],p)<=1e-11:low.pop()
        low.append(p)
    high=[]
    for p in reversed(pts):
        while len(high)>=2 and ccw(high[-2],high[-1],p)<=1e-11:high.pop()
        high.append(p)
    hull=low[:-1]+high[:-1]
    assert 4<=len(hull)<=8,(n,len(hull),hull)
    return sum(math.hypot(hull[(i+1)%len(hull)][0]-hull[i][0],hull[(i+1)%len(hull)][1]-hull[i][1]) for i in range(len(hull)))

def check():
    rng=random.Random(314159)
    top=8*math.sqrt(2)
    for a in [(1,0,0),(0,1,0),(0,0,1),(-1,0,0)]:
        assert abs(section_perimeter(a)-top)<1e-9
    for i in range(12000):
        n=[rng.gauss(0,1) for _ in range(3)]
        p=section_perimeter(n)
        assert p<top+1e-8,(n,p)
    c=8*(math.sqrt(2)-1)
    for slope in (0.,.1,.5,1.,2.):
        for t in (1e-2,1e-3,1e-4):
            n=(math.sqrt(1-(1+slope*slope)*t*t),t,slope*t)
            err=(top-section_perimeter(n))/(c*t*(1+slope))
            assert abs(err-1)<.08,(slope,t,err)
    print('PASS: 24 edges; 4 exact-axis cases; 12000 random upper-bound cases; 15 cusp checks')
    print('perimeter max',top,'cusp',c,'tail coefficient',3/(math.pi*c*c))
if __name__=='__main__':check()

def near_axis_exact(a,u,v):
    assert a>u+v and a>0 and u>=0 and v>=0
    sm=math.sqrt(2+((u-v)/a)**2);sp=math.sqrt(2+((u+v)/a)**2)
    def corner(U,V):
        zp=2*U/(a+U-V);zm=2*U/(a+U+V)
        chord=math.sqrt(2*(zp*zp+zm*zm)+(((U-V)*zp-(U+V)*zm)/a)**2)
        return zp*sm+zm*sp-chord
    return 4*(sm+sp)-2*corner(u,v)-2*corner(v,u)

def crosscheck_exact():
    rg=random.Random(20261026)
    for k in range(500):
        u=rg.random()*.27;v=rg.random()*.27;a=math.sqrt(1-u*u-v*v)
        assert a>u+v
        exact=near_axis_exact(a,u,v)
        generic=section_perimeter((a,u,v))
        assert abs(exact-generic)<5e-10,(a,u,v,exact,generic)
    print('PASS: exact local polygon formula versus independent 24-edge intersections (500 cases)')
if __name__=='__main__':crosscheck_exact()
