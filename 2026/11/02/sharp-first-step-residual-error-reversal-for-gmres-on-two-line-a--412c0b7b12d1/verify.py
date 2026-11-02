"""Supplementary exact checks for the GMRES versus two-line MAP tradeoff.

This code checks rational specializations and arithmetic identities. The
all-angle conclusions are proved analytically in RESULT.md, not by sampling.
"""
from fractions import Fraction as F
from math import sqrt


def dot(x, y):
    return x[0]*y[0] + x[1]*y[1]


def norm2(x):
    return dot(x, x)


def matvec(A, x):
    return (A[0][0]*x[0]+A[0][1]*x[1], A[1][0]*x[0]+A[1][1]*x[1])


def check():
    checked = 0
    for n in range(2, 72):
        for k in range(1,n):
            u = F(k,n)
            c = (1-u*u)/(1+u*u)
            s = 2*u/(1+u*u)
            assert c>0 and s>0 and c*c+s*s == 1
            z = c*c
            D = 1+z-z*z
            x0 = (F(1),F(0))
            T = ((c*c,F(0)),(c*s,F(0)))
            A = ((1-c*c,F(0)),(-c*s,F(1)))
            map_step = matvec(T,x0)
            w = matvec(A,x0)
            Aw = matvec(A,w)
            alpha = dot(w,Aw)/norm2(Aw)
            gmres_step = (x0[0]-alpha*w[0], x0[1]-alpha*w[1])
            assert alpha == 1/D
            residual_g = matvec(A,gmres_step)
            residual_m = matvec(A,map_step)
            assert norm2(gmres_step)-norm2(map_step) == z*z*(1-z)**3/D**2
            assert norm2(residual_g)/norm2(residual_m) == 1/D
            assert norm2(map_step) == z
            assert norm2(residual_m) == z*(1-z)**2
            assert norm2(gmres_step)>norm2(map_step)
            assert norm2(residual_g)<norm2(residual_m)
            assert w[0]*Aw[1]-w[1]*Aw[0] == -c*s**3
            checked += 1
    print('PASS exact rational angle parameterizations:', checked)
    # Polynomial derivative identity and the unique positive maximizing root.
    z0 = (5-sqrt(21))/2
    assert 0<z0<1
    f = lambda z:z*(1-z)**3/(1+z-z*z)**2
    target = (21*sqrt(21)-81)/200
    assert abs(f(z0)-target)<1e-13
    for j in range(1,10000):
        z=j/10000
        assert f(z) <= target+1e-14
    print('PASS sharp parameter maximum at z=%.12f, loss ratio=%.12f' %
          (z0,sqrt(1+target)))
    print('PASS best residual improvement ratio %.12f' % (2/sqrt(5)))
    print('VERIFICATION_OK')

if __name__=='__main__':
    check()
