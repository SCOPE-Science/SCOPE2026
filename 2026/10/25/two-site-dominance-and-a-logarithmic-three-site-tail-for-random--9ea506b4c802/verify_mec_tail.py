"""Numerical diagnostics for rare large minimum-enclosing circles of three uniform disk points.

Requires NumPy and SciPy. These computations corroborate, but do not replace,
the mathematical asymptotic proof in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import quad

PI=math.pi

def angular_measure(eta):
    # Exact angular integration of the absolute circumcircle Jacobian
    # over acute triples lying in a circular arc of length pi+eta.
    return 6*(eta*eta + eta*math.sin(eta) + PI*(eta-math.sin(eta)))

def acute_exact(eps):
    """Exact 2D quadrature for P(acute, MEC radius > 1-eps)."""
    def at_deficit(s):
        if s==0:
            return 0.0
        r=1-s
        dmax=math.sqrt(1-r*r)
        # Center distance d <= s: entire circumcircle lies inside unit disk.
        enclosed=angular_measure(PI)*s*s/2
        upper=math.log(dmax/s)
        def log_distance_integrand(u):
            d=s*math.exp(u)
            c=(1-r*r-d*d)/(2*r*d)
            c=max(0.,min(1.,c))
            eta=2*math.asin(c)
            return d*d*angular_measure(eta)
        crescent=quad(log_distance_integrand,0,upper,epsabs=2e-14,
                      epsrel=2e-10,limit=150)[0]
        return r**3*(enclosed+crescent)
    return 2/PI**2*eps*quad(lambda t: at_deficit(eps*t),0,1,
                            epsabs=1e-16,epsrel=1e-9,limit=150)[0]

def pair_long(eps):
    """Exact P(distance of two uniform disk points > 2(1-eps))."""
    def overlap_integrand(deficit):
        d=2-deficit
        area=2*math.acos(d/2)-d*math.sqrt(max(0.,1-d*d/4))
        return 2*d*area/PI
    return quad(overlap_integrand,0,2*eps,epsabs=1e-15,limit=150)[0]

def test_circumcircle_jacobian():
    for i in range(13):
        angles=np.array([0.12+i*.011, 1.1+i*.014, 3.4+i*.013])
        r=1.35
        M=np.zeros((6,6))
        for j,t in enumerate(angles):
            M[2*j:2*j+2,0:2]=np.eye(2)
            M[2*j:2*j+2,2]=[math.cos(t),math.sin(t)]
            M[2*j:2*j+2,3+j]=r*np.array([-math.sin(t),math.cos(t)])
        unit=np.array([[math.cos(t),math.sin(t)] for t in angles])
        target=r**3*abs(np.linalg.det(np.array([unit[1]-unit[0],unit[2]-unit[0]])))
        assert abs(abs(np.linalg.det(M))-target)<1e-11
    print('INDEPENDENT_SIX_BY_SIX_CHANGE_OF_VARIABLES_JACOBIAN_OK')

def test_angular_integral():
    # Exact derivation: six orders of the angles, outer angular gap pi+v,
    # interior angle x in (v,pi). Integrate the unit-triangle determinant.
    for eta in (.025,.2,.9,2.,PI):
        def inner(v):
            def det(x):
                return math.sin(x)+math.sin(x-v)+math.sin(v)
            return (eta-v)*quad(det,v,PI,epsabs=1e-12)[0]
        numerical=6*quad(inner,0,eta,epsabs=1e-11)[0]
        formula=angular_measure(eta)
        assert abs(numerical-formula)<2e-10
    assert abs(angular_measure(PI)-12*PI**2)<1e-10
    print('EXACT_ACUTE_ARC_ANGULAR_INTEGRAL_OK')

def test_tail_quadratures():
    expected_acute=16/PI**2
    expected_pair=128*math.sqrt(2)/(15*PI)
    for eps in (.1,.03,.01):
        a=acute_exact(eps)
        p=pair_long(eps)
        assert 0<a<1 and 0<p<1
        print('EXACT_QUADRATURE',eps,round(a,12),round(p,12))
    a=acute_exact(1e-8)
    assert abs(a/(1e-24*math.log(1e8))-expected_acute)<.31
    p=pair_long(1e-3)
    assert abs(p/(1e-3)**2.5-expected_pair)<.005
    # Analytic constants in the conditional 3-contact limit.
    assert abs(expected_acute/(3*expected_pair)-5/(8*math.sqrt(2)*PI))<1e-14
    print('ACUTE_LOG_TAIL_AND_TWO_POINT_ENDPOINT_CONSTANTS_OK')

def test_direct_uniform_triangle_sampling():
    rng=np.random.default_rng(871)
    n=1200000
    acute_count=0
    obtuse_count=0
    batch=200000
    for _ in range(n//batch):
        ang=rng.uniform(0,2*PI,size=(batch,3))
        rad=np.sqrt(rng.random((batch,3)))
        x=rad*np.cos(ang); y=rad*np.sin(ang)
        a=(x[:,0]-x[:,1])**2+(y[:,0]-y[:,1])**2
        b=(x[:,1]-x[:,2])**2+(y[:,1]-y[:,2])**2
        c=(x[:,2]-x[:,0])**2+(y[:,2]-y[:,0])**2
        longest=np.maximum(np.maximum(a,b),c)
        acute=(2*longest<a+b+c)
        doublearea=np.abs((x[:,1]-x[:,0])*(y[:,2]-y[:,0])-(x[:,2]-x[:,0])*(y[:,1]-y[:,0]))
        radius=np.where(acute,np.sqrt(a*b*c)/(2*np.maximum(doublearea,1e-18)),np.sqrt(longest)/2)
        acute_count+=np.count_nonzero(acute & (radius>.9))
        obtuse_count+=np.count_nonzero((~acute) & (radius>.9))
    acute_observed=acute_count/n
    acute_expected=acute_exact(.1)
    sigma=math.sqrt(acute_expected*(1-acute_expected)/n)
    assert abs(acute_observed-acute_expected)<6*sigma
    # A two-contact event is not exactly the union of long-pair events,
    # because an acute triangle can also contain a long side.
    assert .02<obtuse_count/n<.04
    print('INDEPENDENT_UNIFORM_TRIANGLE_SUPPORT_COUNT_SIMULATION_OK',n)

if __name__=='__main__':
    test_circumcircle_jacobian()
    test_angular_integral()
    test_tail_quadratures()
    test_direct_uniform_triangle_sampling()
    print('ALL_MINIMUM_ENCLOSING_DISK_UPPER_TAIL_CHECKS_OK')
