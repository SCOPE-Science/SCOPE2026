"""Numerical cross-checks of the thermal--squeezing Wigner-volume theorem.

The general proof is analytic; finite numerical tests do not certify its
limit statements. Run: python verify.py (requires scipy, see requirements).
"""
import math
from scipy.integrate import quad
from scipy.special import i0

PI = math.pi


def qint(f, a, b):
    return quad(f, a, b, epsabs=1e-12, epsrel=2e-11, limit=160)[0]


def exact_negative_volume(t, r):
    """Integrate the exact ellipse via an angular Bessel identity."""
    assert 0 < t <= 1 and r >= 0
    s = t * math.exp(2*r)
    z = t * math.exp(-2*r)
    gamma = math.cosh(2*r)
    c = 1 + t*gamma
    a = (1+s)**2/s
    b = (1+z)**2/z
    pref = t/((gamma+t)*math.sqrt(a*b))
    return pref*qint(lambda u: (c-u)*math.exp(-u*(1/a+1/b)/2)*i0(u*(1/a-1/b)/2), 0, c)


def direct_negative_volume(t, r):
    """Independent double polar integration without the Bessel identity."""
    s=t*math.exp(2*r)
    z=t*math.exp(-2*r)
    c=1+(s+z)/2
    a=(1+s)**2/s
    b=(1+z)**2/z
    gamma=math.cosh(2*r)
    angular=lambda theta: qint(lambda u:(c-u)*math.exp(-u*(math.cos(theta)**2/a+math.sin(theta)**2/b)),0,c)
    return t/(2*PI*(gamma+t)*math.sqrt(a*b))*qint(angular,0,2*PI)


def g(s):
    """Exact joint limit profile."""
    assert s>0
    c=1+s/2
    inv_a=s/(1+s)**2
    return 2/(s*(1+s))*qint(lambda u:(c-u)*math.exp(-u*inv_a/2)*i0(u*inv_a/2),0,c)


def f_strong(t):
    """Fixed-thermal-parameter strong-squeeze disk integral."""
    assert 0<t<=1
    edge=1/math.sqrt(2)
    inner=lambda w:qint(lambda v:(.5-w*w-v*v)*math.exp(-w*w-t*t*v*v),0,math.sqrt(max(0,.5-w*w)))
    return 8*t**3/PI*qint(inner,0,edge)


def kappa():
    return 2*qint(lambda u:(.5-u)*math.exp(-u/2)*i0(u/2),0,.5)


def gaussian_normalization(t,r):
    """Check normalized polynomial-Gaussian integral by exact moments."""
    gamma=math.cosh(2*r)
    s=t*math.exp(2*r)
    z=t*math.exp(-2*r)
    bracket_mean=(1+s)**2/(2*s)+(1+z)**2/(2*z)-(1+t*gamma)
    return t/(gamma+t)*bracket_mean


def assert_close(a,b,tol=1e-7):
    assert abs(a-b) <= tol*max(1,abs(a),abs(b)), (a,b,tol)


def run():
    normalized=0
    for t in (.03,.3,.8,1):
        for r in (0,.4,1.2,2.5):
            assert_close(gaussian_normalization(t,r),1,1e-12)
            normalized+=1
    pairs=0
    for t,r in ((.1,0),(.3,.7),(.8,1.2),(.5,2),(.05,2.4),(1,0),(1,1.2)):
        assert_close(exact_negative_volume(t,r),direct_negative_volume(t,r),2e-10)
        pairs+=1
    assert_close(exact_negative_volume(1,0),2*math.exp(-.5)-1,2e-11)
    fixed=0
    for r in (0,.5,1,2):
        t=1e-5
        observed=exact_negative_volume(t,r)/t**2
        predicted=1/(2*math.cosh(2*r))
        assert abs(observed/predicted-1)<.0006, (r,observed,predicted)
        fixed+=1
    boundary=0
    for s in (.1,.5,1,2,10):
        t=1e-4
        r=math.log(s/t)/2
        ratio=exact_negative_volume(t,r)/(t**3*g(s))
        assert abs(ratio-1)<1.5e-4,(s,ratio)
        boundary+=1
    k=kappa()
    assert_close(k,.230968177814117,1e-12)
    assert_close(f_strong(1),2*math.exp(-.5)-1,1e-11)
    prev=float('inf')
    envelope=0
    for t in (.01,.1,.3,.6,1):
        ratio=f_strong(t)/t**3
        assert ratio<prev
        assert (2*math.exp(-.5)-1)-1e-12<=ratio<=k+1e-12
        assert abs(exact_negative_volume(t,9)-f_strong(t))<2e-7
        prev=ratio
        envelope+=1
    relative_bound=0
    for t in (.02,.1,.4,.9):
        for r in (0,.7,1.6,3,5):
            s=t*math.exp(2*r)
            relative_error=abs(exact_negative_volume(t,r)/(t**3*g(s))-1)
            theoretical=12*(math.exp(-4*r)+t*math.exp(-2*r)+t*t)
            assert relative_error <= theoretical+2e-11,(t,r,relative_error,theoretical)
            relative_bound+=1
    print('VERIFY_OK',f'normalization={normalized}',f'direct_quadrature={pairs}',
          f'fixed_squeezing={fixed}',f'joint_crossover={boundary}',
          f'sharp_envelope={envelope}',f'relative_bound={relative_bound}',f'kappa={k:.15f}')


if __name__=='__main__':
    run()
