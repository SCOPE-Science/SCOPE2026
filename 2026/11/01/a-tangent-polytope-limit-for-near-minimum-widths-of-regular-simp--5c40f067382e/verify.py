"""Independent reproducible finite and analytic checks of the stated geometric formulas."""
import math
import numpy as np
from scipy.integrate import quad

def c_exact(n):
    a=n//2; b=n-a
    count=math.comb(n,a)*(1 if a==b else 2)
    ball_surf=2*math.pi**((n-1)/2)/math.gamma((n-1)/2)
    volume=(a**(a-.5))*(b**(b-.5))/math.factorial(n-2)
    return count*(2**((n-2)/2))*volume/ball_surf

def minimizing_vector(n,A):
    a=len(A); b=n-a
    u=np.full(n,-math.sqrt(a/(n*b)))
    u[list(A)]=math.sqrt(b/(n*a))
    return u

def width(u):return (u.max()-u.min())/math.sqrt(2)

def tests():
    for n in range(3,11):
        a=n//2; b=n-a
        u=minimizing_vector(n,range(a))
        assert abs(u.sum())<1e-13
        assert abs(np.dot(u,u)-1)<1e-13
        assert abs(width(u)-math.sqrt(n/(2*a*b)))<1e-13
        print(f'n={n}: coefficient={c_exact(n):.11f}, minimizer={width(u):.11f}')
    assert abs(c_exact(3)-12/math.pi)<1e-12
    assert abs(c_exact(4)-12/math.pi)<1e-12
    assert abs(c_exact(5)-120*math.sqrt(3)/math.pi**2)<1e-11
    print('EXACT_CLOSED_FORM_CONSTANTS_PASSED')
    # Direct exact three-vertex directional-width CDF for small excess.
    w0=math.sqrt(3)/2
    for eps in [0.0001,0.001,0.005,0.01]:
        exact=1-(6/math.pi)*math.acos(w0+eps)
        assert abs(exact/(eps*c_exact(3))-1)<0.025
    print('EXACT_TRIANGLE_LOWER_TAIL_PASSED')
    # Independent two-dimensional local-area integration for the tetrahedron.
    # Uses the exact nonlinear spherical chart (not tangent asymptotics).
    for eps in [0.00005,0.0002,0.0005]:
        delta=math.sqrt(2)*eps
        q=(1+delta)**2
        c=q-1
        def radial_area(theta):
            g=(abs(math.cos(theta))+abs(math.sin(theta)))/math.sqrt(2)
            h=q-g*g
            dis=g*g-h*c
            assert dis>=0
            r=c/(g+math.sqrt(dis))
            return 1-1/math.sqrt(1+r*r)
        spherical_area=quad(radial_area,0,2*math.pi,epsabs=2e-13)[0]
        prob=6*spherical_area/(4*math.pi)
        ratio=prob/(c_exact(4)*eps**2)
        assert abs(ratio-1)<0.01,(eps,ratio)
    print('EXACT_TETRAHEDRON_SPHERICAL_AREA_PASSED')
    # Compare exact max/min width with the local tangent expression and first-order cone.
    rng=np.random.default_rng(314159)
    for n in range(3,11):
        a=n//2
        u=minimizing_vector(n,range(a))
        for _ in range(100):
            v=rng.normal(size=n)
            v[:a]-=v[:a].mean()
            v[a:]-=v[a:].mean()
            v*=1e-5/np.linalg.norm(v)
            phi=max(v[:a])-min(v[a:])
            us=(u+v)/math.sqrt(1+np.dot(v,v))
            exact=(math.sqrt(n/(a*(n-a)))+phi)/(math.sqrt(2)*math.sqrt(1+np.dot(v,v)))
            assert abs(width(us)-exact)<1e-13
            slope=(width(us)-width(u))/np.linalg.norm(v)
            low=1/math.sqrt(2*(n-a)*(n-a-1))
            high=math.sqrt(((a-1)/a+((n-a)-1)/(n-a))/2)
            assert low-5e-5<=slope<=high+5e-5,(n,slope,low,high)
    print('NONLINEAR_TANGENT_CHART_AND_SHARP_SLOPES_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':tests()
