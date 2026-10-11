"""Finite-dimensional diagnostic checks for the two-colour Chebyshev orbit.

Run with Python 3 without third-party dependencies. Finite tests supplement,
but do not replace, the analytic proof of the all-size result.
"""
import cmath
import math

U = (math.sqrt(5.0) - 1.0) / 4.0
V = (-math.sqrt(5.0) - 1.0) / 4.0


def cheb(x):
    return 2.0 * x * x - 1.0


def evolve(x, a):
    n = len(x)
    return [(1-a) * cheb(x[j]) + a * (x[(j-1) % n] + x[(j+1) % n]) / 2 for j in range(n)]


def jacobian(x, a):
    n = len(x)
    mat = [[0.0] * n for _ in range(n)]
    for i, v in enumerate(x):
        mat[i][i] += 4 * (1-a) * v
        mat[i][(i-1) % n] += a/2
        mat[i][(i+1) % n] += a/2
    return mat


def mm(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def mv(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(v))]


def err(x, y):
    return max(abs(a - b) for a, b in zip(x, y))


def check():
    checks = 0
    assert abs(cheb(U)-V) < 1e-14
    assert abs(cheb(V)-U) < 1e-14
    checks += 2
    for n in (2, 4, 6, 8, 10, 12):
        state = [U if j % 2 == 0 else V for j in range(n)]
        alternate = [V if j % 2 == 0 else U for j in range(n)]
        for a in (0, 0.12, 0.4, 0.6, 0.7, 0.8, 0.95, 1.0):
            assert err(evolve(state,a),alternate) < 3e-14
            assert err(evolve(alternate,a),state) < 3e-14
            checks += 2
            m2 = mm(jacobian(alternate,a), jacobian(state,a))
            c = 1-a
            for r in range(n//2):
                k = 2*math.pi*r/n
                t = math.cos(k)
                # The period-two Fourier sector is represented by a pair of
                # amplitudes on the even and odd lattice sites.
                w_even = [cmath.exp(1j*k*j) if j%2==0 else 0j for j in range(n)]
                w_odd = [cmath.exp(1j*k*j) if j%2 else 0j for j in range(n)]
                e0 = mv(m2,w_even)
                e1 = mv(m2,w_odd)
                # Block columns measured at representatives 0,1.
                col0 = (e0[0], e0[1]/cmath.exp(1j*k))
                col1 = (e1[0], e1[1]/cmath.exp(1j*k))
                K = a*a*t*t - 4*c*c
                block = ((K, 2*a*c*t*(-1-math.sqrt(5))),
                         (2*a*c*t*(-1+math.sqrt(5)), K))
                assert max(abs(col0[i]-block[i][0]) for i in range(2))<1e-12
                assert max(abs(col1[i]-block[i][1]) for i in range(2))<1e-12
                checks += 2
                # Verify all coordinates, not just the two representatives.
                for z, cols in ((w_even,e0),(w_odd,e1)):
                    X = block[0][0] * (z[0]) + block[0][1] * (z[1] / cmath.exp(1j*k))
                    Y = block[1][0] * (z[0]) + block[1][1] * (z[1] / cmath.exp(1j*k))
                    predicted = [cmath.exp(1j*k*j) * (X if j%2==0 else Y) for j in range(n)]
                    assert err(cols,predicted)<1e-11
                    checks += 1
                determinant = block[0][0]*block[1][1]-block[0][1]*block[1][0]
                predicted_radius = 4*c*c + a*a*t*t
                assert abs(determinant - predicted_radius**2)<3e-12
                checks += 1
            assert abs(4*c*c+a*a - (5*a*a-8*a+4)) < 1e-12
            checks+=1
    for a in (0.0,.5,.59,.6,.6001,.75,.8,.85,.99,1):
        radius=5*a*a-8*a+4
        stable=(0.6<a<1)
        assert (radius<1)==stable
        checks+=1
    assert abs((5*(.8**2)-8*.8+4)-.8)<1e-12
    checks+=1
    print(f"CHECKS_OK: {checks} direct lattice identities and Floquet determinant tests")

if __name__=='__main__':
    check()
