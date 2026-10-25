"""Independent finite regression checks for the triangle intersection-body area formula.
This uses the Python standard library only; the analytic proof is in RESULT.md.
"""
import math
from fractions import Fraction


def chord_x_span(p, q, m):
    s = 1 + p + q
    if m < 0:
        return s * (q - p*m) / ((q-(p+1)*m)*(q+1-p*m))
    if m < q/p:
        return s / ((1+m)*(q+1-p*m))
    return s*m / ((1+m)*((p+1)*m-q))


def integrate(f, left, right, tolerance=1e-9, depth=28):
    """Adaptive Simpson quadrature with an explicit local error estimate."""
    def simp(a,b,fa,fm,fb):return (b-a)*(fa+4*fm+fb)/6
    a,b=left,right;fa=f(a);fb=f(b);fm=f((a+b)/2)
    def go(a,b,fa,fm,fb,old,eps,n):
        m=(a+b)/2;lm=(a+m)/2;rm=(m+b)/2
        fl=f(lm);fr=f(rm)
        l=simp(a,m,fa,fl,fm);r=simp(m,b,fm,fr,fb)
        if n==0 or abs(l+r-old)<15*eps:return l+r+(l+r-old)/15
        return go(a,m,fa,fl,fm,l,eps/2,n-1)+go(m,b,fm,fr,fb,r,eps/2,n-1)
    return go(a,b,fa,fm,fb,simp(a,b,fa,fm,fb),tolerance,depth)


def numerical_area(p, q):
    # theta parametrization avoids infinite slope endpoints.
    # A(I)=int_{-pi/2}^{pi/2} chord(theta)^2 dtheta.
    # chord(theta)^2 = span(tan(theta))^2 / cos(theta)^2.
    cuts=[-math.pi/2,0.0,math.atan(q/p), math.pi/2]
    def integrand(t):
        if t <= -math.pi/2:
            return ((1+p+q)/(p+1))**2
        if t >= math.pi/2:
            return ((1+p+q)/(p+1))**2
        m=math.tan(t)
        return (chord_x_span(p,q,m)/math.cos(t))**2
    return sum(integrate(integrand,a,b) for a,b in zip(cuts,cuts[1:]))


def formula(p,q):
    s=1+p+q
    return s+2/s*(p*q*math.log((1+p)*(1+q)/(p*q))
                   +p*math.log((p+q)*(1+q)/p)
                   +q*math.log((p+q)*(1+p)/q))


def g(t):
    return 0.0 if t in (0.,1.) else t*(1-t)*math.log((1-t)/t)


def verify():
    tested=0
    for p,q in [(1,1),(.5,.6),(2,3),(7,.1),(.1,7),(1/17,13),(10,.005)]:
        a=numerical_area(p,q); b=formula(p,q)
        assert abs(a-b) < 5e-6*(1+abs(b)),(p,q,a,b)
        s=1+p+q
        bary=(p/s,q/s,1/s)
        assert abs(2+4*sum(g(t) for t in bary)-a/(s/2)) < 5e-6
        tested+=1
    # Exact rational chord-cross-section check at the three interval types.
    def crossing_span(p,q,m):
        # Intersect line (x,m*x) with each segment of the triangle.
        vs=[(Fraction(1),Fraction(0)),(Fraction(0),Fraction(1)),(-p,-q)]
        xs=[]
        for (x0,y0),(x1,y1) in zip(vs,vs[1:]+vs[:1]):
            u0=y0-m*x0;u1=y1-m*x1
            if u0*u1<0:
                t=-u0/(u1-u0)
                xs.append(x0+t*(x1-x0))
            elif u0==0:xs.append(x0)
            elif u1==0:xs.append(x1)
        return max(xs)-min(xs)
    for p,q in [(Fraction(1),Fraction(1)),(Fraction(2,3),Fraction(7,4)),(Fraction(3),Fraction(2,5))]:
        for i in range(-18,19):
            m=Fraction(i,7)
            if m==q/p:continue
            assert crossing_span(p,q,m)==chord_x_span(p,q,m),(p,q,m)
            tested+=1
    # Inequality stress tests are not a proof of the quantified assertion.
    for i in range(1,151):
        a=(1+i%17)/(7+i%23)
        b=(1+(i*13)%19)/(4+(i*7)%29)
        c=(1+(i*11)%31)/(8+(i*5)%37)
        s=a+b+c;a/=s;b/=s;c/=s
        v=2+4*(g(a)+g(b)+g(c))
        assert 2<v<=2+(8/3)*math.log(2)+1e-12
        tested+=1
    assert abs(2+4*3*g(1/3)-(2+(8/3)*math.log(2)))<1e-12
    print('PASS:', tested, 'regression checks; analytic proof not replaced by finite tests.')

if __name__=='__main__':verify()
