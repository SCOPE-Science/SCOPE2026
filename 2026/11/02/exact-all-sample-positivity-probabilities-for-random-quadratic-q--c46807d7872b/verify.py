"""Independent elementary checks for an exact random-node quadratic quadrature law.

Python >=3.9, standard library only.  This program checks finite algebra,
independent convex-hull predicates, and numerical quadrature; the asymptotic
claim is proved analytically in RESULT.md rather than by finite tests.
"""
from fractions import Fraction as Q
from math import comb, log
from random import Random

B = Q(1, 2)
b = Q(1, 6)
tau = Q(1, 12)


def integrate_laurent(poly):
    """Integrate sum_e poly[e]*u**e from 1/6 to 1/2.

    Returns (rational_part, coefficient_of_log_3).
    """
    rational, logcoef = Q(0), Q(0)
    for e, c in poly.items():
        if e == -1:
            logcoef += c
        else:
            rational += c * (B ** (e + 1) - b ** (e + 1)) / (e + 1)
    return rational, logcoef


def phi_power(n):
    """(u + 1/(12*u))**n as an integer-exponent Laurent polynomial."""
    ans = {}
    for k in range(n + 1):
        e = n - 2*k
        ans[e] = ans.get(e, Q(0)) + Q(comb(n, k), 12**k)
    return ans


def coefficients(m):
    """Return exact (A,B) with p_m=A+B*log(3), for m >= 2."""
    assert m >= 2
    n = m - 1
    poly = {}
    for j in range(n + 1):
        sign_coeff = Q((-1)**j * comb(n, j))
        for e, c in phi_power(j).items():
            poly[e] = poly.get(e, Q(0)) + sign_coeff*c
    for e, c in phi_power(n).items():
        poly[e] = poly.get(e, Q(0)) + c
    rational, lc = integrate_laurent(poly)
    rational = 1 - Q(2, 3)**m + Q(1, 3)**m - m*rational
    return rational, -m*lc


def probability(m):
    a, c = coefficients(m)
    return float(a) + float(c)*log(3)


def criterion(nodes):
    """Exact geometric criterion for a nondegenerate, non-boundary sample."""
    left = sorted((Q(1,2) - v for v in nodes if v < Q(1,2)))
    right = sorted((v - Q(1,2) for v in nodes if v > Q(1,2)))
    return bool(left and right and left[-1]*right[-1] > tau and
                left[0]*right[0] < tau)


def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]


def in_triangle(a, b, c):
    """Independently computed barycentric containment in curved 2D support."""
    pa, pb, pc = [(v, v*v) for v in (a, b, c)]
    t = (Q(1,2), Q(1,3))
    dif = lambda p,q: (p[0]-q[0],p[1]-q[1])
    den = cross(dif(pb,pa), dif(pc,pa))
    return den != 0 and all(z*den > 0 for z in (
        cross(dif(pb,t),dif(pc,t)),
        cross(dif(pc,t),dif(pa,t)),
        cross(dif(pa,t),dif(pb,t))))


def brute_triples(nodes):
    n = len(nodes)
    return any(in_triangle(nodes[i], nodes[j], nodes[k])
               for i in range(n) for j in range(i+1,n)
               for k in range(j+1,n))


def integrate_simpson(fn, a, z, n=8000):
    h = (z-a)/n
    return h/3*(fn(a)+fn(z) +
                4*sum(fn(a+(2*k-1)*h) for k in range(1,n//2+1)) +
                2*sum(fn(a+2*k*h) for k in range(1,n//2)))


def independent_probability(m):
    # Integrates the two disjoint geometric failure mechanisms separately.
    def f_ext(u):
        return (u + tau/float(u))**(m-1)
    def f_near(u):
        return (1-u-tau/float(u))**(m-1)
    return 1 - (2/3)**m + (1/3)**m - m * (
        integrate_simpson(f_ext,1/6,1/2)+
        integrate_simpson(f_near,1/6,1/2))


def main():
    expected = {
        2:(Q(0),Q(0)),
        3:(Q(-1,3),Q(1,2)),
        4:(Q(-2,3),Q(1)),
        5:(Q(-410,243),Q(25,12)),
        6:(Q(-275,81),Q(15,4)),
    }
    for m, pair in expected.items():
        assert coefficients(m) == pair, (m, coefficients(m))

    old = 0
    for m in range(2, 18):
        p = probability(m)
        assert -2e-11 <= p <= 1+2e-11, (m,p)
        assert p >= old - 2e-11, (m,p,old)
        old = p
        independent = independent_probability(m)
        assert abs(p-independent) < 3e-9, (m,p,independent)

    # Rational atanh bounds certify the sharp 95% sample cutoff.
    K = 25
    low = sum((Q(2, (2*k+1)*2**(2*k+1)) for k in range(K)), Q(0))
    omitted = Q(2, (2*K+1)*2**(2*K+1))
    high = low + Q(4,3)*omitted
    a10, b10 = coefficients(10)
    a11, b11 = coefficients(11)
    assert b10 > 0 and b11 > 0
    assert a10 + b10*high < Q(19,20) < a11 + b11*low
    assert probability(10) < .95 < probability(11)
    assert abs(probability(10) - .9411269334147931) < 2e-11
    assert abs(probability(11) - .9603356140490007) < 2e-11

    # Independent convex-polygon enumeration on exact rational sampling grids.
    rng = Random(20261023)
    trials = 0
    for m in range(2, 11):
        for _ in range(500):
            nodes = [Q(rng.randrange(1,100000),100001) for j in range(m)]
            if len(set(nodes)) != len(nodes):
                continue
            a, b_ = criterion(nodes), brute_triples(nodes)
            assert a == b_, (m, nodes, a, b_)
            trials += 1
    assert trials >= 4300
    print('PASS: 5 exact formula identities, 16 independent Simpson integrations,')
    print('      16 finite-sample monotonicity/range checks, exact 95% cutoff,')
    print('      and', trials, 'exact-rational geometric comparisons.')
    print('p_10=', probability(10), 'p_11=',probability(11))


if __name__ == '__main__':
    main()
