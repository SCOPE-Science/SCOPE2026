"""Independent numerical consistency checks for the six-normal brightness theorem.

These finite tests supplement, but do not replace, the analytic classification
and majorization proof provided in RESULT.md.  Python 3 standard library only.
"""
from math import acos, asin, cos, sin, pi, sqrt, isclose


def normal_family(phi):
    rho = sqrt(2.0 / 3.0)
    z = 1.0 / sqrt(3.0)
    top = [(rho*cos(2*pi*j/3),rho*sin(2*pi*j/3),z) for j in range(3)]
    bottom = [(rho*cos(phi+2*pi*j/3),rho*sin(phi+2*pi*j/3),-z) for j in range(3)]
    return top + bottom


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def H(t):
    return sqrt(max(0.,1.-t*t))+t*asin(max(-1.,min(1.,t)))


def formula(phi):
    t=[(2*cos(phi+2*pi*j/3)-1)/3 for j in range(3)]
    F=sum(H(x) for x in t)
    return pi*(8+4*F-7*pi)/9


def brightness(normals,v):
    return (pi/3)*sum(abs(dot(a,v)) for a in normals)


def direct_integral(normals, nz=240, nt=720):
    # Equal-area spherical product quadrature: z uniform [-1,1], theta uniform [0,2pi].
    # Midpoint quadrature works with absolute-value ridges without other packages.
    mean=0.
    second=0.
    for iz in range(nz):
        z=-1+(2*iz+1)/nz
        rad=sqrt(max(0.,1-z*z))
        for it in range(nt):
            angle=2*pi*(it+0.5)/nt
            b=brightness(normals,(rad*cos(angle),rad*sin(angle),z))
            mean+=b
            second+=b*b
    count=nz*nt
    return mean/count,second/count-(mean/count)**2


def run():
    phis=[0., pi/12,pi/6,pi/4,pi/3]
    expected_min=pi*(8+4*((2*sqrt(2)+2*sqrt(5)+asin(1/3)+4*asin(2/3))/3)-7*pi)/9
    expected_max=pi*(16-5*pi)/9
    assert isclose(formula(0.),expected_min,rel_tol=0,abs_tol=1e-12)
    assert isclose(formula(pi/3),expected_max,rel_tol=0,abs_tol=1e-12)
    vals=[]
    for phi in phis:
        u=normal_family(phi)
        assert all(abs(dot(v,v)-1)<1e-13 for v in u)
        assert all(abs(sum(v[k] for v in u))<1e-13 for k in range(3))
        assert all(abs(sum(v[i]*v[j] for v in u)-(2 if i==j else 0))<1e-13
                   for i in range(3) for j in range(3))
        actual_mean,actual_variance=direct_integral(u)
        expected=formula(phi)
        assert abs(actual_mean-pi)<3e-4,(phi,actual_mean)
        assert abs(actual_variance-expected)<2e-3,(phi,actual_variance,expected)
        vals.append(expected)
    assert all(b>a+1e-4 for a,b in zip(vals,vals[1:])),vals
    for k in range(1,300):
        phi=k*pi/(3*300)
        t0,t1,t2=[(2*cos(phi+2*pi*j/3)-1)/3 for j in range(3)]
        assert 0<t0<-t2<-t1
        assert abs(t0*t0+t1*t1+t2*t2-1)<2e-14
    print('PASS: normal balance, second moments, five direct sphere quadratures, endpoint constants, and sampled ordering.')
    print('Variance range: %.12f <= Var(B) <= %.12f' % (vals[0], vals[-1]))
    print('Finite checks do not certify the continuum inequality; see analytic proof.')


if __name__=='__main__': run()
