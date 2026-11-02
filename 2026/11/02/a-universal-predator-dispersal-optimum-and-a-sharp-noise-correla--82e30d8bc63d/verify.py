"""Reproduce the stationary-variance and migration-optimization identities.

Requires Python 3.10+ standard library only. The matrix Lyapunov system is
solved independently of the modal covariance formula.
"""
from fractions import Fraction
from math import isclose, sqrt
from random import Random


def elimination(matrix, rhs):
    n = len(rhs)
    aa = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for k in range(n):
        pivot = max(range(k, n), key=lambda j: abs(aa[j][k]))
        if aa[pivot][k] == 0:
            raise ValueError('singular Lyapunov operator')
        aa[pivot], aa[k] = aa[k], aa[pivot]
        coeff = aa[k][k]
        for j in range(k, n + 1):
            aa[k][j] /= coeff
        for i in range(n):
            if i == k:
                continue
            coeff = aa[i][k]
            for j in range(k, n + 1):
                aa[i][j] -= coeff * aa[k][j]
    return [aa[i][n] for i in range(n)]


def patch_variance_from_lyapunov(a, b, c, u, v, q, r, rho_x, rho_y):
    f = [[-a-u, -b, u, 0],
         [c, -v, 0, v],
         [u, 0, -a-u, -b],
         [0, v, c, -v]]
    cov = [[q, 0, q*rho_x, 0],
           [0, r, 0, r*rho_y],
           [q*rho_x, 0, q, 0],
           [0, r*rho_y, 0, r]]
    coeffs, rhs = [], []
    for i in range(4):
        for j in range(4):
            row = [0] * 16
            for k in range(4):
                row[k*4+j] += f[i][k]
                row[i*4+k] += f[j][k]
            coeffs.append(row)
            rhs.append(-cov[i][j])
    return elimination(coeffs, rhs)[0]


def modal_var(A, V, b, c, Q, R):
    return (Q*(V*V+A*V+b*c)+b*b*R)/(2*(A+V)*(A*V+b*c))


def closed_form(a, b, c, u, v, q, r, rho_x, rho_y):
    p_plus = modal_var(a, 0, b, c, q*(1+rho_x), r*(1+rho_y))
    p_minus = modal_var(a+2*u, 2*v, b, c, q*(1-rho_x), r*(1-rho_y))
    return (p_plus+p_minus)/2


def optimal_rate(a, b, c, u, q, r, rho_x, rho_y):
    A = a+2*u
    Q = q*(1-rho_x)
    R = r*(1-rho_y)
    if Q == 0:
        return None
    return (A*b*R+sqrt(b*(A*A*R+Q*c*c)*(Q*c+b*R)))/(2*Q*c)


def assert_close(x,y,tol=1e-10):
    assert isclose(float(x),float(y),rel_tol=tol,abs_tol=tol), (x,y)


def main():
    # Rational independent replay of the full 4x4 system including V=0.
    samples = [(Fraction(2),Fraction(4),Fraction(9),Fraction(1),Fraction(3),Fraction(5),Fraction(0),Fraction(0),Fraction(0)),
               (Fraction(2),Fraction(4),Fraction(9),Fraction(1),Fraction(0),Fraction(5),Fraction(3),Fraction(1,3),Fraction(-1,4)),
               (Fraction(3,2),Fraction(5),Fraction(3),Fraction(2,3),Fraction(4,3),Fraction(8),Fraction(0),Fraction(1),Fraction(-1))]
    for args in samples:
        assert patch_variance_from_lyapunov(*args) == closed_form(*args)

    rng=Random(20261025)
    for _ in range(200):
        a,b,c=[10**rng.uniform(-1,1) for k in range(3)]
        u,v=[10**rng.uniform(-2,1) for k in range(2)]
        q,r=[10**rng.uniform(-1,1) for k in range(2)]
        rx,ry=[rng.uniform(-1,1) for k in range(2)]
        args=(a,b,c,u,v,q,r,rx,ry)
        assert_close(patch_variance_from_lyapunov(*args),closed_form(*args),2e-8)
        # Exact calculus sign change: the candidate beats both neighboring rates.
        vv=optimal_rate(a,b,c,u,q,r,rx,ry)
        assert vv is not None and vv > 0
        at=closed_form(a,b,c,u,vv,q,r,rx,ry)
        for k in (0.01,0.1,0.4):
            assert at < closed_form(a,b,c,u,vv*(1-k),q,r,rx,ry)
            assert at < closed_form(a,b,c,u,vv*(1+k),q,r,rx,ry)
        # Increasing v with R>0 must increase the minimum above the R=0 optimum.
        assert vv > sqrt(b*c)/2

    for _ in range(120):
        a,b,c=[10**rng.uniform(-1,1) for k in range(3)]
        u=10**rng.uniform(-2,1)
        q=10**rng.uniform(-1,1)
        rx=rng.uniform(-1,0.99)
        vv=optimal_rate(a,b,c,u,q,0,rx,0)
        assert_close(vv,sqrt(b*c)/2)
        A=a+2*u
        Q=q*(1-rx)
        baseline=closed_form(a,b,c,u,0,q,0,rx,0)
        asymptote=0.5*(q*(1+rx)/(2*a)+Q/(2*A))
        assert_close(baseline,asymptote)
        reduction=baseline-closed_form(a,b,c,u,vv,q,0,rx,0)
        assert_close(reduction,Q*b*c/(4*A*(A+sqrt(b*c))**2))
        assert reduction>0

    # Perfectly correlated prey noise leaves the antisymmetric prey mode unforced.
    for v in [0,0.1,1,10,100]:
        assert_close(closed_form(2,4,9,1,v,5,0,1,0), 5/(2*2))
    # Predator-only antisymmetric forcing gives strictly monotone decline.
    vals=[closed_form(2,4,9,1,v,5,3,1,-1) for v in [0,0.1,1,10,100]]
    assert all(x>y for x,y in zip(vals,vals[1:])),vals

    # Fully explicit evaluation and gain.
    assert_close(closed_form(2,4,9,1,3,5,0,0,0),0.825)
    assert_close(closed_form(2,4,9,1,0,5,0,0,0),0.9375)
    print('PASS: 3 exact rational Lyapunov solves, 200 full-matrix random solves,')
    print('120 universal-optimum/gain identities, degenerate noise cases and example.')

if __name__ == '__main__':
    main()
