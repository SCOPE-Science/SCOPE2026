"""Numerical checks for triangle shape reconstruction from short interpoint distances.
Requires only the Python standard library. Analytic proof is in RESULT.md.
"""
import math
import random

PI=math.pi

def triangle(a,b,c):
    assert a+b>c and a+c>b and b+c>a
    z=(b*b+c*c-a*a)/(2*c)
    h=math.sqrt(max(0.0,b*b-z*z))
    return [(0.,0.),(c,0.),(z,h)]

def area(p):
    return abs(sum(p[i][0]*p[(i+1)%len(p)][1]-p[(i+1)%len(p)][0]*p[i][1]
                   for i in range(len(p)))/2) if p else 0.

def cross(v,w):return v[0]*w[1]-v[1]*w[0]

def clip_convex(poly, q):
    # Intersection with all left halfplanes of CCW polygon q.
    for j in range(len(q)):
        u=q[j];v=q[(j+1)%len(q)]; edge=(v[0]-u[0],v[1]-u[1])
        def signed(p):return cross(edge,(p[0]-u[0],p[1]-u[1]))
        out=[]
        if not poly:return []
        old=poly[-1];fv=signed(old)
        for cur in poly:
            fw=signed(cur)
            if (fv>=0)!=(fw>=0):
                frac=fv/(fv-fw)
                out.append((old[0]+frac*(cur[0]-old[0]),old[1]+frac*(cur[1]-old[1])))
            if fw>=0:out.append(cur)
            old=cur;fv=fw
        poly=out
    return poly

def law(a,b,c,r):
    sides=[a,b,c];P=sum(sides)
    ar=math.sqrt((P/2)*math.prod(P/2-s for s in sides))
    alpha=[math.acos(max(-1.,min(1.,(sum(s*s for s in sides)-2*x*x)/(2*math.prod(y for y in sides if y!=x))))) for x in sides]
    # expression above is unreliable for repeated sides; use direct cosine law instead
    alpha=[math.acos(max(-1.,min(1.,(sides[(i+1)%3]**2+sides[(i+2)%3]**2-sides[i]**2)/
                              (2*sides[(i+1)%3]*sides[(i+2)%3])))) for i in range(3)]
    q=sum(1+(PI-t)/math.tan(t) for t in alpha)
    return PI*r*r/ar-2*P*r**3/(3*ar*ar)+q*r**4/(8*ar*ar), ar, P, q, alpha

def direct(a,b,c,r,angular=1024,radial=40):
    p=triangle(a,b,c); ar=area(p)
    ans=0.
    for j in range(angular):
        phi=2*PI*(j+.5)/angular
        dx=math.cos(phi);dy=math.sin(phi)
        for k in range(radial):
            t=r*(k+.5)/radial
            shifted=[(x+t*dx,y+t*dy) for x,y in p]
            ans+=area(clip_convex(p[:],shifted))*t
    return ans*(2*PI/angular)*(r/radial)/(ar*ar)

def f(x):return 1/math.tan(x/2)
def g(x):return (PI-x)/math.tan(x)
def F(tri):return sum(f(x) for x in tri)
def G(tri):return sum(g(x) for x in tri)
def R(x):
    beta=PI-x
    return (math.sin(beta)-beta*math.cos(beta))/(2*math.sin(beta/2)**4)

def main():
    for sides in [(3.,4.,5.),(1.,1.,1.),(2.,2.,3.),(2.,3.,4.),(0.5,0.7,1.1)]:
        r=.035*min(sides)
        formula,A,P,Q,angles=law(*sides,r)
        empirical=direct(*sides,r)
        rel=abs(empirical-formula)/formula
        print('triangle',sides,'A',round(A,8),'P',round(P,8),
              'Q',round(Q,8),'local_CDF_relative_error',f'{rel:.3g}')
        assert rel<.000035
    rng=random.Random(314159)
    for _ in range(5000):
        z=[rng.random()+.01 for _ in range(3)]
        z=[PI*x/sum(z) for x in z]
        z.sort()
        a,b,c=z
        if b-a<1e-6 or c-b<1e-6:continue
        # Convexity of g' relative to f': strict increase in R=g''/f''.
        assert R(a)<R(b)<R(c)
        h=1e-5
        assert R(a+h)>R(a)
        assert R(b+h)>R(b)
        assert R(c+h)>R(c)
    # For fixed F=perimeter^2/(4 area), G is strictly monotone on the sorted chamber.
    for constant in [5.3,6.,9.,20.,50.]:
        feq=3*math.sqrt(3)
        assert constant>feq
        def bisection(fun,lo,hi):
            for _ in range(65):
                m=(lo+hi)/2
                if fun(m)>constant:lo=m
                else:hi=m
            return (lo+hi)/2
        amin=bisection(lambda a:f(a)+2*f((PI-a)/2),1e-10,PI/3)
        amax=bisection(lambda a:2*f(a)+f(PI-2*a),1e-10,PI/3)
        vals=[]
        for j in range(1,50):
            a=amin+(amax-amin)*j/50
            lo=a;hi=(PI-a)/2
            for _ in range(65):
                b=(lo+hi)/2
                if F([a,b,PI-a-b])>constant:lo=b
                else:hi=b
            b=(lo+hi)/2;c=PI-a-b
            vals.append(G([a,b,c]))
        assert all(u<v+1e-10 for u,v in zip(vals,vals[1:])),(constant,vals)
        print('fixed invariant',constant,'G_interval',round(vals[0],8),round(vals[-1],8))
    print('VERIFY_OK')

if __name__=='__main__': main()
