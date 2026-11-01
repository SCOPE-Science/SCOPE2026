#!/usr/bin/env python3
"""Exact-rational finite checks of triangular modular-map periodic grids.
All-period formulas and the continuum discrepancy bound are proved in
RESULT.md; these examples only test the implementation and identities.
Requires Python 3 standard library.
"""
from fractions import Fraction as Q


def mod(t, width):
    return t % width


def step(point, degrees, couplings, exponent, shift, width):
    x, y, z = point
    a, c, e = degrees
    b, d = couplings
    return (mod(a*x + b*y**exponent, width),
            mod(c*y + d*z**exponent, width),
            mod(e*z + shift, width))


def fixed_points(n, degrees, couplings, exponent, shift, width):
    a, c, e = degrees
    b, d = couplings
    nx, ny, nz = a**n-1, c**n-1, e**n-1
    sz = sum(e**(n-1-k) for k in range(n))
    for jz in range(nz):
        z0 = mod((width*jz-shift*sz)/nz, width)
        zs = [z0]
        for _ in range(1, n):
            zs.append(mod(e*zs[-1]+shift, width))
        sy = sum(c**(n-1-k)*d*zs[k]**exponent for k in range(n))
        for jy in range(ny):
            y0 = mod((width*jy-sy)/ny, width)
            ys = [y0]
            for k in range(1, n):
                ys.append(mod(c*ys[-1]+d*zs[k-1]**exponent, width))
            sx = sum(a**(n-1-k)*b*ys[k]**exponent for k in range(n))
            for jx in range(nx):
                x0 = mod((width*jx-sx)/nx, width)
                yield (x0, y0, z0)


def check(degrees, couplings, exponent, shift, width, n):
    a, c, e = degrees
    points = list(fixed_points(n, degrees, couplings, exponent, shift, width))
    expected = (a**n-1)*(c**n-1)*(e**n-1)
    assert len(points) == expected and len(set(points)) == expected
    for point in points:
        orbit_point = point
        for _ in range(n):
            orbit_point = step(orbit_point, degrees, couplings, exponent, shift, width)
        assert orbit_point == point, (n, point, orbit_point)
    bound = width*Q(1,2)*sum((Q(1, d**n-1) for d in degrees), Q(0))
    for k in range(3):
        empirical_mean = sum((point[k] for point in points), Q(0))/expected
        assert abs(empirical_mean - width/2) <= bound
    print('PASS width=',width,'degrees=',degrees,'n=',n,'points=',expected)


def fixed_points_borel(n, degrees, phi, psi, shift, width):
    """Exact construction with potentially discontinuous Borel shifts."""
    a,c,e=degrees
    nx,ny,nz=a**n-1,c**n-1,e**n-1
    sz=sum(e**(n-1-k) for k in range(n))
    for jz in range(nz):
        z0=mod((width*jz-shift*sz)/nz,width)
        zs=[z0]
        for _ in range(1,n):
            zs.append(mod(e*zs[-1]+shift,width))
        sy=sum(c**(n-1-k)*psi(zs[k]) for k in range(n))
        for jy in range(ny):
            y0=mod((width*jy-sy)/ny,width)
            ys=[y0]
            for k in range(1,n):
                ys.append(mod(c*ys[-1]+psi(zs[k-1]),width))
            sx=sum(a**(n-1-k)*phi(ys[k],zs[k]) for k in range(n))
            for jx in range(nx):
                yield (mod((width*jx-sx)/nx,width),y0,z0)


def check_borel():
    width=Q(5,3)
    degrees=(2,2,2)
    shift=Q(1,7)
    def phi(y,z):
        return (Q(2,7) if y>=width/3 else -Q(1,5)) + (Q(1,11) if z<width/2 else Q(0))
    def psi(z):
        return Q(1,13) if z>=width/2 else -Q(3,17)
    a,c,e=degrees
    for n in (1,2,3):
        pts=list(fixed_points_borel(n,degrees,phi,psi,shift,width))
        count=(a**n-1)*(c**n-1)*(e**n-1)
        assert len(pts)==count and len(set(pts))==count
        for original in pts:
            x,y,z=original
            for _ in range(n):
                x,y,z=(mod(a*x+phi(y,z),width),mod(c*y+psi(z),width),mod(e*z+shift,width))
            assert (x,y,z)==original
        print('PASS discontinuous Borel forcing, n=',n,'points=',count)


if __name__ == '__main__':
    cases = [
        ((2,3,2), (Q(1,2),-Q(1,3)), 2,Q(1,7),Q(1)),
        ((3,2,2), (Q(-2,5),Q(4,7)), 3,Q(-1,11),Q(5,3)),
        ((2,2,3), (Q(1,4),Q(1,5)), 2,Q(0),Q(7,4)),
    ]
    for case in cases:
        for n in (1,2,3):
            check(*case, n)
    a,c,e = (2,2,3)
    width=Q(7,4)
    n=3
    pts=list(fixed_points(n, (a,c,e), (Q(1,4),Q(1,5)), 2,Q(0),width))
    mean_z=sum((p[2] for p in pts), Q(0))/len(pts)
    assert abs(mean_z-width/2) == width/Q(2*(e**n-1))
    print('PASS sharp lower bound for z-observable with zero last-coordinate shift')
    check_borel()
