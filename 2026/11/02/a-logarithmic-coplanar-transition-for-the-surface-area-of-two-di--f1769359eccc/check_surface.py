"""Independent numerical checks for the two-disc Minkowski-sum area law.

Requires NumPy and SciPy. Run: python check_surface.py
The analytic results are proved separately; these are finite checks only.
"""
from math import pi, sin, log
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipe
from scipy.spatial import ConvexHull


def j_elliptic(theta):
    t = sin(theta)
    return 4.0 * quad(lambda x: ellipe(1.0 - t*t*sin(x)**2),
                      0.0, pi/2.0, epsabs=1e-11, epsrel=1e-11)[0]


def area_formula(theta, radius1, radius2):
    return 2*pi*(radius1**2+radius2**2) + 2*radius1*radius2*j_elliptic(theta)


def volume_formula(theta, radius1, radius2):
    return 2*pi*radius1*radius2*(radius1+radius2)*sin(theta)


def j_independent_grid(theta, n=1000):
    a = (np.arange(n)+0.5)*pi/n
    aa = a[:, None]
    bb = a[None, :]
    dot = np.cos(aa)*np.cos(bb)+np.cos(theta)*np.sin(aa)*np.sin(bb)
    return (pi/n)**2 * np.sqrt(np.maximum(0.0, 1-dot*dot)).sum()


def polygon_approximant(theta, radius1, radius2, n=160):
    a = 2*pi*np.arange(n)/n
    x = radius1*np.column_stack((np.cos(a), np.sin(a), np.zeros(n)))
    y = radius2*np.column_stack((np.cos(a), np.cos(theta)*np.sin(a),
                                  np.sin(theta)*np.sin(a)))
    vertices = (x[:,None,:]+y[None,:,:]).reshape(-1,3)
    hull = ConvexHull(vertices)
    return hull.area, hull.volume


def main():
    for theta in [0.2, 0.65, 1.35]:
        computed = j_elliptic(theta)
        independently = j_independent_grid(theta)
        assert abs(computed-independently) < 2e-5, (theta, computed, independently)
    for theta in [0.12,0.35,0.8,1.2,pi/2]:
        assert j_elliptic(theta) > 2*pi
    monotone = [area_formula(t, 1.3, 0.8) for t in np.linspace(0,pi/2,32)]
    assert all(a < b for a,b in zip(monotone,monotone[1:])), 'angular order'
    assert abs(area_formula(0,1.3,.8)-2*pi*(1.3+.8)**2)<1e-10
    assert abs(j_elliptic(pi/2)-8.310725840109914)<5e-10

    for theta,r,s in [(0.5,1.0,1.0),(pi/2,1.0,1.0),(.8,1.3,.8)]:
        coarse=polygon_approximant(theta,r,s,80)
        fine=polygon_approximant(theta,r,s,160)
        exact=(area_formula(theta,r,s),volume_formula(theta,r,s))
        for i in range(2):
            e0=exact[i]-coarse[i]
            e1=exact[i]-fine[i]
            assert e0>0 and e1>0, ('inscribed monotonicity',theta,i)
            assert 0.20<e1/e0<0.30, ('quadratic polygonal convergence',theta,i,e1/e0)
            assert e1/exact[i]<0.0005, ('relative error',theta,i,e1/exact[i])
    r,s=1.3,.8
    for theta in [.08,.04,.02,.01]:
        delta=area_formula(theta,r,s)-2*pi*(r+s)**2
        mainterm=pi*r*s*theta**2*(log(8/theta)-1)
        assert abs(delta/mainterm-1)<0.001, (theta,delta/mainterm)
    print('ALL_TWO_DISC_ANGULAR_AREA_CHECKS_PASSED')


if __name__=='__main__':
    main()
