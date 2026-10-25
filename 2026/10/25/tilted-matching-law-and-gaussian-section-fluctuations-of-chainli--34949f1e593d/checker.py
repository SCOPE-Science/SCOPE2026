"""Independent numerical and combinatorial checks of an exponentially tilted chainlink-polytope volume identity.
Run: python chainlink_checker.py. All tests use only the Python standard library.
"""
import itertools
import math


def mass(a, t):
    if abs(t) < 1.e-11:
        return a
    return math.exp(t*a/2) * a * math.sinh(t*a/2)/(t*a/2)


def forbidden_mass(a, ell, t):
    if abs(t) < 1.e-11:
        return ell*ell/2
    return math.exp(t*a) * ell*ell/2 * (math.sinh(t*ell/2)/(t*ell/2))**2


def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def trace_z(a, ell, t):
    M = [[1., 0.], [0., 1.]]
    for ai in a:
        M = matmul(M, [[mass(ai,t), -forbidden_mass(ai,ell,t)], [1.,0.]])
    return M[0][0]+M[1][1]


def matching_z(a, ell, t):
    n=len(a)
    result=0.
    for mask in range(1 << n):
        edges=[i for i in range(n) if mask >> i & 1]
        used=[]
        for i in edges:
            used.extend((i,(i+1)%n))
        if len(set(used)) != len(used):
            continue
        value=(-1)**len(edges)
        for i in edges:
            value*=forbidden_mass(a[i],ell,t)
        for i in set(range(n))-set(used):
            value*=mass(a[i],t)
        result+=value
    return result


def simpson(f,lo,hi,n=80):
    if hi<=lo: return 0.0
    step=(hi-lo)/n
    return step/3*(f(lo)+f(hi)+4*sum(f(lo+step*j) for j in range(1,n,2))+2*sum(f(lo+step*j) for j in range(2,n,2)))


def integrated_z3(a,ell,t,resolution=80):
    """Directly integrate all three inequalities, splitting every kink."""
    a1,a2,a3=a
    def outer(x1):
        upper=min(a3,x1+a3-ell)
        lower_x2=max(0.,x1-a1+ell)
        def integrand(x2):
            lower_x3=max(0.,x2-a2+ell)
            if abs(t)<1.e-11: z=upper-lower_x3
            else: z=(math.exp(t*upper)-math.exp(t*lower_x3))/t
            return math.exp(t*(x1+x2))*z
        return simpson(integrand,lower_x2,a2-ell,resolution)+simpson(integrand,a2-ell,a2,resolution)
    return (simpson(outer,0.,ell,resolution)+simpson(outer,ell,a1-ell,resolution)
            +simpson(outer,a1-ell,a1,resolution))


def gaussian_variance(r, s):
    u=r*r/2
    discriminant=math.sqrt(1-4*u)
    lp=(1+discriminant)/2
    lm=(1-discriminant)/2
    extra=(s*r*r*(1-r*r)/(12*discriminant))*((lp**(s-1)-lm**(s-1))/(lp**s+lm**s))
    return s/12+extra


def run():
    comparisons=0
    for n in range(3,10):
        a=[2. + .17*(i%3) for i in range(n)]
        for ell in (.2,.7,1.):
            for t in (-.45,0.,.35):
                x,y=trace_z(a,ell,t),matching_z(a,ell,t)
                assert abs(x-y) < 1.e-9*max(1,abs(x),abs(y)),(n,ell,t,x,y)
                comparisons+=1
    for a,ell in (((2.4,2.1,2.6),.6),((1.,1.,1.),.5),((2.7,2.0,3.1),1.0)):
        for t in (-.32,0.,.23):
            x,y=trace_z(a,ell,t),integrated_z3(a,ell,t)
            assert abs(x-y)/x < 7.e-5,(a,ell,t,x,y)
            comparisons+=1
    for r in (.1,.25,.5):
        for s in (3,4,7,20):
            a=[1.]*s
            h=.00015
            z0=trace_z(a,r,0.)
            zp=trace_z(a,r,h)
            zm=trace_z(a,r,-h)
            log_second=(math.log(zp)+math.log(zm)-2*math.log(z0))/h**2
            # second derivative of log mgf is variance
            assert abs(log_second-gaussian_variance(r,s))<3.e-6,(r,s,log_second,gaussian_variance(r,s))
            comparisons+=1
    r=.3
    d=math.sqrt(1-2*r*r)
    lam=(1+d)/2
    sigma=1/12+r*r*(1-r*r)/(12*d*lam)
    for s in (100,200,500):
        assert abs(gaussian_variance(r,s)/s-sigma)<1.e-12
        comparisons+=1
    print('CHECK_OK',comparisons,'direct algebra/numerical comparisons')

if __name__=='__main__':
    run()
