#!/usr/bin/env python3
"""High-precision checks for a finite-server resetting crossover asymptotic.

Requires mpmath. Run `python verify_crossover.py`.
These numerical checks supplement, but do not prove, the asymptotic theorem.
"""
from mpmath import mp

mp.dps = 90


def parameters(c, D=1, L=2, mu=1):
    c, D, L, mu = map(mp.mpf, (c, D, L, mu))
    q = c * mu
    a = q * L * L / D
    assert a > mp.mpf('2.5')
    b = mp.sqrt(1 - 2/a)
    eps = (2/a)/(1+b)  # stable version of 1-b
    x0 = L * eps
    assert mp.almosteq((2*L-x0)*x0/(2*D), 1/q)
    return q, a, b, eps, x0, D, L


def difference(u, a, b, eps):
    theta = u/eps
    # The hyperbolic addition formula avoids cosh(theta) overflow.
    g = 2*mp.sinh(u/2)**2 + mp.tanh(b*theta)*mp.sinh(u)
    return g - theta**2/a


def solve(c, D=1, L=2, mu=1):
    q, a, b, eps, x0, D, L = parameters(c, D, L, mu)
    lo = eps  # theta=1; small-reset region
    hi = 4*mp.log(a) + 40
    assert difference(lo,a,b,eps) < 0
    assert difference(hi,a,b,eps) > 0
    for _ in range(360):
        mid = (lo+hi)/2
        if difference(mid,a,b,eps) > 0:
            hi = mid
        else:
            lo = mid
    u = (lo+hi)/2
    theta = u/eps
    r = D*theta*theta/(L*L)
    g1 = 2*mp.sinh(u/2)**2 + mp.tanh(b*theta)*mp.sinh(u)
    g2 = mp.exp(u)*(1+mp.exp(-2*theta))/(1+mp.exp(-2*b*theta))-1
    # Independent algebraic evaluations of the same mean hitting time.
    assert abs(g1-g2) < mp.mpf('1e-65')*max(1,abs(g1))
    assert abs(g1/r-1/q) < mp.mpf('1e-65')/q
    assert abs(difference(u,a,b,eps)) < mp.mpf('1e-65')*max(1,g1)
    assert difference(u*mp.mpf('0.9999'),a,b,eps) < 0
    assert difference(u*mp.mpf('1.0001'),a,b,eps) > 0
    z = mp.sqrt(D*r)/(q*L)
    A = mp.log(a)
    B = mp.log(A)
    expansion2 = A + 2*B
    expansion3 = expansion2 + 4*B/A
    return dict(c=c,a=a,x0=x0,r=r,u=u,z=z,expansion2=expansion2,
                expansion3=expansion3,third_error=z-expansion3,
                scaled=r*D/(q*q*L*L*A*A))


def main():
    cs = [1,2,5,10,20,50,100,1000,10000,100000,1000000,10**8,10**10]
    rows = [solve(c) for c in cs]
    for row in rows:
        print('c={:>11} r={:>17.7f} z={:>11.7f} z-3term={:>+11.7f} '.format(
            row['c'],float(row['r']),float(row['z']),float(row['third_error'])))
    errors = [abs(row['third_error']) for row in rows[6:]]
    assert errors[-1] < errors[0]
    assert all(row['scaled'] > 1 for row in rows)
    # Dimensionless crossover scaling must be invariant under matched changes
    # of length, diffusion, and service rate with the same a.
    for c in [2,10,100,1000]:
        r0=solve(c,1,2,1)
        r1=solve(c,3,6,mp.mpf('1')/3)
        a1=solve(c,mp.mpf('0.25'),1,1)
        assert mp.almosteq(r0['a'],r1['a'])
        assert mp.almosteq(r0['a'],a1['a'])
        assert mp.almosteq(r0['z'],r1['z'])
        assert mp.almosteq(r0['z'],a1['z'])
    print('PASS: {} crossover roots, exact MFPT identities and 8 rescaling tests.'.format(len(rows)))

if __name__ == '__main__':
    main()
