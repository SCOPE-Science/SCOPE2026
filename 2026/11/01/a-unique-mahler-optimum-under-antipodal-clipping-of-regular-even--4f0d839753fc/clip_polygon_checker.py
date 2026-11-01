"""Standalone numerical cross-check of opposite-corner clipping of regular even polygons.
Only standard Python modules are used. Finite tests complement, rather than prove,
the all-parameter geometric and derivative arguments in RESULT.md.
"""
import math


def shoelace(vertices):
    return abs(sum(x*y2-x2*y for (x,y),(x2,y2) in zip(vertices, vertices[1:]+vertices[:1])))/2


def clip(poly, bound, sign):
    # Retain points satisfying sign*x <= bound.
    out=[]
    for p,q in zip(poly, poly[1:]+poly[:1]):
        a=sign*p[0]-bound
        b=sign*q[0]-bound
        if a <= 1e-14:
            out.append(p)
        if (a < -1e-14 and b > 1e-14) or (a > 1e-14 and b < -1e-14):
            k=a/(a-b)
            out.append((p[0]+k*(q[0]-p[0]),p[1]+k*(q[1]-p[1])))
    # Remove equal consecutive vertices, if any, and zero-length edges.
    dedup=[]
    for v in out:
        if not dedup or math.dist(v,dedup[-1])>1e-10:dedup.append(v)
    if len(dedup)>1 and math.dist(dedup[0],dedup[-1])<1e-10:dedup.pop()
    return dedup


def polygon_and_polar_areas(n,h):
    poly=[(math.cos(2*math.pi*j/n),math.sin(2*math.pi*j/n)) for j in range(n)]
    poly=clip(clip(poly,h,1),h,-1)
    dual=[]
    for p,q in zip(poly,poly[1:]+poly[:1]):
        nx=q[1]-p[1]; ny=p[0]-q[0]
        c=nx*p[0]+ny*p[1]
        assert c>0
        dual.append((nx/c,ny/c))
    return shoelace(poly),shoelace(dual)


def formula(n,h):
    a=math.pi/n
    A=n*math.sin(2*a)/2 - 2*(1-h)**2/math.tan(a)
    B=n*math.tan(a)+2*math.tan(a)*(1/h-1)
    M=(n-2+2/h)*(n*math.sin(a)**2-2*(1-h)**2)
    return A,B,M


def g(n,h):
    q=math.sin(math.pi/n)**2
    return 2+(2*n-6)*h*h+(4-2*n)*h**3-n*q


def optimum(n):
    if n==4:return .5
    lo=math.cos(2*math.pi/n);hi=1.
    assert g(n,lo)>0 and g(n,hi)<0
    for _ in range(90):
        mid=(lo+hi)/2
        if g(n,mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def test():
    count=0
    for n in [4,6,8,10,12,16,24,50]:
        left=max(1e-3,math.cos(2*math.pi/n))
        for k in range(1,26):
            h=left+(1-left)*k/26
            A,B=polygon_and_polar_areas(n,h)
            a,b,m=formula(n,h)
            assert abs(A-a)<1e-8,(n,h,'area',A,a)
            assert abs(B-b)<1e-8,(n,h,'polar',B,b)
            assert abs(A*B-m)<1e-7,(n,h,'product',A*B,m)
            count+=3
        opt=optimum(n)
        assert left<opt<1
        ml=formula(n,left)[2]; mo=formula(n,opt)[2]; mr=formula(n,1)[2]
        assert mo>ml and mo>mr
        count+=3
    assert abs(formula(4,.5)[2]-9)<1e-12
    count+=1
    for n in [100,200,400,800]:
        opt=optimum(n)
        q=math.sin(math.pi/n)**2
        assert abs((1-opt)/q-.5)<.001
        count+=1
    print('PASS:',count,'independent geometric, optimization, and asymptotic checks')
    for n in [4,6,8,10,20]:
        o=optimum(n)
        print(n,'opt=',format(o,'.12g'),'Mmax=',format(formula(n,o)[2],'.12g'))

if __name__=='__main__': test()
