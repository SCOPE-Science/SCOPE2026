#!/usr/bin/env python3
"""Numerical consistency checks for adjacency-Dirac distances on cross-polytope graphs.

Requires only the Python 3 standard library. These finite tests do not prove the
statements for all dimensions or certify originality.
"""
import math


def full_commutator(r, f):
    n = 2 * r
    return [[(f[j] - f[i]) if (i // 2 != j // 2) else 0.0
             for j in range(n)] for i in range(n)]


def spectral_square_skew(b):
    n = len(b)
    s = [[-sum(b[i][k] * b[k][j] for k in range(n)) for j in range(n)]
         for i in range(n)]
    # Symmetric Jacobi diagonalization.
    for _ in range(90 * n * n):
        p, q = 0, 1
        m = 0.0
        for i in range(n):
            for j in range(i+1, n):
                if abs(s[i][j]) > m:
                    m = abs(s[i][j]); p, q = i, j
        if m < 3e-12:
            return max(s[i][i] for i in range(n))
        angle = 0.5 * math.atan2(2 * s[p][q], s[q][q] - s[p][p])
        c, t = math.cos(angle), math.sin(angle)
        app, aqq, apq = s[p][p], s[q][q], s[p][q]
        s[p][p] = c*c*app - 2*c*t*apq + t*t*aqq
        s[q][q] = t*t*app + 2*c*t*apq + c*c*aqq
        s[p][q] = s[q][p] = 0.0
        for k in range(n):
            if k != p and k != q:
                u, v = s[k][p], s[k][q]
                s[k][p] = s[p][k] = c*u - t*v
                s[k][q] = s[q][k] = t*u + c*v
    raise RuntimeError('Jacobi did not converge')


def gram(r, a):
    A = r - 1 + (a+.5)**2
    B = 2*a*a + 2*(r-1)*a + .5
    E = (4*r-3)*a*a + a + .25
    return A, B, E


def F(r, a):
    A,B,E = gram(r,a)
    return (A+E+math.hypot(A-E,2*B))/2


def dF(r, a):
    A,B,E = gram(r,a)
    Ap = 2*a+1; Bp=4*a+2*(r-1); Ep=2*(4*r-3)*a+1
    den = math.hypot(A-E,2*B)
    return (Ap+Ep + ((A-E)*(Ap-Ep)+4*B*Bp)/den)/2


def argmin(r):
    lo, hi = -.5, 0.0
    assert dF(r,lo)<0 and dF(r,hi)>0
    for _ in range(65):
        a=(lo+hi)/2
        if dF(r,a)<0:lo=a
        else:hi=a
    return (lo+hi)/2


def main():
    checks=0
    for r in range(3,12):
        n=2*r
        for j in range(21):
            a=(j-10)/20
            f=[0.5,a,-0.5,-a]+[0.0]*(n-4)
            # Ordering first four are two whole pairs, remaining are other pairs.
            val=spectral_square_skew(full_commutator(r,f))
            assert abs(val-F(r,a))<=2e-8*(1+F(r,a)),(r,a,val,F(r,a))
            checks+=1
        f=[0.5,-0.5]+[0.0]*(n-2)
        val=spectral_square_skew(full_commutator(r,f))
        assert abs(val-(r-1))<2e-8*(1+r)
        checks+=1
        a=argmin(r)
        assert -.5<a<0 and dF(r,a)**2<1e-18
        assert F(r,a)>r-1 and F(r,a)<F(r,0)
        checks+=1
    for r in (50,200,800,3200):
        a=argmin(r)
        assert abs(r*a+3/8)<.30/r
        assert abs(r*(F(r,a)-r+.75)+5/16)<.4/r
        assert abs(r**1.5*((r-1)**(-.5)-F(r,a)**(-.5))-.125)<.01
        checks+=3
    print(f'CHECK_OK {checks} finite comparisons, dimension/asymptotic diagnostics')

if __name__=='__main__':
    main()
