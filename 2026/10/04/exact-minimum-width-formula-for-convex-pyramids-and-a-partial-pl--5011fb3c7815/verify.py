#!/usr/bin/env python3
"""Supplemental numerical checks for the convex-pyramid width formula."""
import math


def dot(p, q):
    return sum(x*y for x, y in zip(p, q))


def support(poly, e):
    return max(dot(p, e) for p in poly)


def formula(poly, h, ne=12000):
    best = h
    for k in range(ne):
        t = 2.0*math.pi*k/ne
        e = (math.cos(t), math.sin(t))
        a = support(poly, e)
        b = support(poly, (-e[0], -e[1]))
        cand = h*(a+b)/math.sqrt(h*h+a*a)
        best = min(best, cand)
    return best


def direct(poly, h, nphi=1600, nr=1200):
    best = h
    for k in range(nphi):
        t = 2.0*math.pi*k/nphi
        e = (math.cos(t), math.sin(t))
        a = support(poly, e)
        b = support(poly, (-e[0], -e[1]))
        for j in range(nr+1):
            r = j/nr
            z = math.sqrt(max(0.0, 1.0-r*r))
            w = r*b + max(r*a, h*z)
            best = min(best, w)
    return best


def branch_check(a, b, h):
    r0 = h/math.sqrt(h*h+a*a)
    target = min(h, h*(a+b)/math.sqrt(h*h+a*a))
    vals = []
    for j in range(20001):
        r = j/20000.0
        vals.append(r*b + max(r*a, h*math.sqrt(max(0.0,1.0-r*r))))
    err = abs(min(vals)-target)
    assert err < 2e-4, (a,b,h,min(vals),target,err,r0)


def main():
    for pars in [(1.2,0.7,1.0),(0.2,2.4,1.6),(3.0,0.4,0.8),(0.0,1.3,0.9)]:
        branch_check(*pars)
    examples = [
        ([(-1.0,-1.0),(1.0,-1.0),(1.0,1.0),(-1.0,1.0)], 2.0),
        ([(-2.0,-1.0),(1.0,-0.5),(1.0,2.0),(-1.0,1.0)], 2.0),
        ([(-1.4,-0.4),(0.7,-1.1),(1.3,0.2),(0.2,1.4),(-1.0,0.8)], 1.1),
    ]
    for poly,h in examples:
        # All listed examples contain the origin in their interior.
        f = formula(poly,h)
        d = direct(poly,h)
        assert abs(f-d) < 6e-3, (f,d)
        print(f'formula={f:.9f} direct-grid={d:.9f} residual={abs(f-d):.3g}')
    print('supplemental checks passed')


if __name__ == '__main__':
    main()
