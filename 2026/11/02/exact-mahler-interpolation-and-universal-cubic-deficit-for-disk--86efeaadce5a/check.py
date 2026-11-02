"""Numerical checks for the polar-area interpolation theorem.

Python 3 standard library only.  These finite tests are not an infinite-dimensional
or all-parameter proof; the proof is analytical.
"""
import math


def polygon_hull(points):
    pts = sorted(set(points))
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    lo = []
    for p in pts:
        while len(lo)>1 and cross(lo[-2],lo[-1],p)<=0:
            lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(pts):
        while len(hi)>1 and cross(hi[-2],hi[-1],p)<=0:
            hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]


def shoelace(points):
    return abs(sum(x*y2-x2*y for (x,y),(x2,y2) in zip(points,points[1:]+points[:1])))/2


def expressions(n,beta):
    a=math.pi/n
    u=a-beta
    r=1/math.cos(beta)
    A=n*(math.tan(beta)+r*r*u)
    B=n*(math.sin(beta)*math.cos(beta)+u*math.cos(beta)**2)
    M=A*B
    compact=n*n*(u+math.sin(beta)*math.cos(beta))*(u+math.tan(beta))
    deriv=n*n*math.sin(beta)**2*(u*(math.tan(beta)**2-1)-math.tan(beta))
    return A,B,M,compact,deriv


def independent_area(n,beta,m=16000):
    a=math.pi/n
    r=1/math.cos(beta)
    # Uniform midpoint integration of the squared radial function.
    A=0
    for k in range(m):
        theta=(k+0.5)*a/m
        A+=min(r*r, 1/math.cos(theta)**2)
    A*=n*a/m
    return A


def independent_polar_area(n,beta,m=12000):
    s=math.cos(beta)
    pts=[(math.cos(2*math.pi*j/n), math.sin(2*math.pi*j/n)) for j in range(n)]
    pts.extend((s*math.cos(2*math.pi*j/m),s*math.sin(2*math.pi*j/m)) for j in range(m))
    return shoelace(polygon_hull(pts))


def check():
    tests=0
    for n in (3,4,5,7,11,30):
        a=math.pi/n
        prev=None
        for k in range(1,19):
            beta=a*k/19
            A,B,M,C,deriv=expressions(n,beta)
            assert abs(M-C)<2e-12
            assert deriv<0
            if prev is not None:
                assert M<prev
            prev=M
            tests+=3
        for t in (.12,.4,.75,.95):
            beta=a*t
            A,B,M,C,deriv=expressions(n,beta)
            An=independent_area(n,beta)
            Bn=independent_polar_area(n,beta)
            assert abs(A-An)<1.2e-7,(n,t,'area',A,An)
            assert abs(B-Bn)<3e-6,(n,t,'polar',B,Bn)
            tests+=2
        assert abs(expressions(n,0)[2]-math.pi**2)<5e-13
        assert abs(expressions(n,a)[2]-n*n*math.sin(a)**2)<5e-13
        tests+=2

    # Endpoint exponents, checked by asymptotic ratios, with an appropriately
    # scaled beta parameter to avoid loss of precision in inverse cosine.
    for n in (3,4,9):
        a=math.pi/n
        for beta in (.015,.0075,.00375):
            M=expressions(n,beta)[2]
            r=1/math.cos(beta)
            leading=(2*math.sqrt(2)*math.pi*n/3)*(r-1)**1.5
            assert abs((math.pi**2-M)/leading-1)<.15
            tests+=1
        R=1/math.cos(a)
        for delta in (.0004,.0002,.0001):
            beta=a-delta
            M=expressions(n,beta)[2]
            r=1/math.cos(beta)
            leading=n*n*math.sin(a)**2*math.cos(a)*(R-r)
            assert abs((M-n*n*math.sin(a)**2)/leading-1)<.01
            tests+=1
    for n in (100,300,900):
        a=math.pi/n
        den=math.pi**2-n*n*math.sin(a)**2
        for t in (.05,.2,.5,.75,1):
            ratio=(math.pi**2-expressions(n,t*a)[2])/den
            correction=(2*t**3/15-4*t**5/5+2*t**6/3)*a*a
            assert abs(ratio-(t**3+correction))<4e-6,(n,t,ratio,t**3+correction)
            tests+=1
    print('PASS',tests,'independent area/polar, monotonicity, endpoints and large-n comparisons')

if __name__=='__main__':
    check()
