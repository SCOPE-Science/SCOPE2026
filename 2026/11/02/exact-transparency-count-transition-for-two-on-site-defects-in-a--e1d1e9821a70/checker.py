#!/usr/bin/env python3
"""Independent finite-parameter checks for a static two-site lattice scattering theorem.

Uses direct complex transfer matrices, rather than the Green-function proof.
The analytic all-separations assertion is established in RESULT.md, not by these checks.
"""
import cmath
import math

PI = math.pi


def mm(A, B):
    return ((A[0][0]*B[0][0]+A[0][1]*B[1][0],
             A[0][0]*B[0][1]+A[0][1]*B[1][1]),
            (A[1][0]*B[0][0]+A[1][1]*B[1][0],
             A[1][0]*B[0][1]+A[1][1]*B[1][1]))


def mv(A, v):
    return (A[0][0]*v[0]+A[0][1]*v[1],
            A[1][0]*v[0]+A[1][1]*v[1])


def reflection(k, L, U, V, t=1.0):
    """Incoming exp(+ikn) on left; transmission amplitude from transfer."""
    c = 2*math.cos(k)
    free = ((c, -1), (1, 0))
    left = ((c-U/t, -1), (1, 0))
    right = ((c-V/t, -1), (1, 0))
    M = left
    for _ in range(L-1):
        M = mm(free, M)
    M = mm(right, M)
    v0 = mv(M, (1, cmath.exp(-1j*k)))
    vr = mv(M, (1, cmath.exp(1j*k)))
    vt = (cmath.exp(1j*(L+1)*k), cmath.exp(1j*L*k))
    # vr*r - vt*trans = -v0
    a, b, c0, d = vr[0], -vt[0], vr[1], -vt[1]
    determinant = a*d-b*c0
    return ((-v0[0])*d-b*(-v0[1]))/determinant


def function(k, L, U, t=1.0):
    return 2*t*math.sin(k)*math.cos(L*k)-U*math.sin(L*k)


def roots_in_band(L, U, t=1.0):
    M = 480*L
    eps = 1e-7
    points = [eps+(PI-2*eps)*j/M for j in range(M+1)]
    roots = []
    prev_x, prev_y = points[0], function(points[0], L, U, t)
    for x in points[1:]:
        y = function(x, L, U, t)
        if prev_y*y < 0:
            a, b, fa = prev_x, x, prev_y
            for _ in range(55):
                mid = (a+b)/2
                fm = function(mid, L, U, t)
                if fa*fm <= 0:
                    b = mid
                else:
                    a, fa = mid, fm
            roots.append((a+b)/2)
        prev_x, prev_y = x, y
    return roots


def run():
    count = 0
    max_error = 0.0
    for L in range(1, 18):
        for U in (0.08, 0.33, 0.75, 1.6, -0.08, -0.33, -0.75, -1.6):
            roots = roots_in_band(L, U)
            expected = L if abs(U)<2/L else L-1
            assert len(roots)==expected, (L, U, len(roots), expected)
            count += 1
            for k in roots:
                err = abs(reflection(k,L,U,U))
                max_error = max(err, max_error)
                assert err < 2e-10, (L,U,k,err)
                count += 1
            for m in range(1,L):
                k=m*PI/L
                err=abs(reflection(k,L,U,-U))
                max_error=max(max_error,err)
                assert err < 2e-10, (L,U,m,err)
                count += 1
        # unequal magnitudes cannot yield an exact transparent point
        for U,V in ((0.3,0.9),(-1.0,0.6),(1.2,-0.2),(0.0,0.8)):
            for k in (0.32,0.83,1.41,2.17,2.73):
                r=abs(reflection(k,L,U,V))
                assert r>1e-8, (L,U,V,k,r)
                count += 1
    # Critical band-edge mode comes in with square-root scaling.
    for L in (1,2,3,5,8):
        critical=2/L
        for eps in (0.001,0.0002):
            roots=roots_in_band(L,critical-eps)
            assert len(roots)==L
            small=min(roots)
            leading=math.sqrt(3*L*eps/(2*L*L+1))
            assert abs(small/leading-1)<0.04,(L,eps,small,leading)
            count+=1
    print(f'PASS: {count} direct checks; maximum reflection amplitude at predicted transparent points {max_error:.3g}.')
    print('The analytical theorem, not the finite checks, proves completeness for every integer spacing.')

if __name__=='__main__':
    run()
