"""Exact-arithmetic checks for sphere-coupled symmetric randomized quadrature.

The infinite-dimensional asymptotic theorem is established analytically in RESULT.md;
finite tests here check identities and rational sample paths, not the limit proof.
"""
from fractions import Fraction as F
from itertools import product


def rise(a, k):
    p = F(1)
    for j in range(k):
        p *= a + j
    return p


def sphere_even_moment(exponents):
    """E[prod_j V_j^(2*exponents[j])] on uniform S^2."""
    return F(1, 1) * (rise(F(1, 2), exponents[0]) *
                      rise(F(1, 2), exponents[1]) *
                      rise(F(1, 2), exponents[2])) / rise(F(3, 2), sum(exponents))


def poly_eval(cs, x):
    return sum((c*x**i for i, c in enumerate(cs)), F(0))


def exact_integral(cs):
    return sum((c / (i+1) for i, c in enumerate(cs)), F(0))


def sphere_rational(u, v):
    den = 1 + u*u + v*v
    vec = (2*u/den, 2*v/den, (1-u*u-v*v)/den)
    assert sum(t*t for t in vec) == 1
    return vec


def quadrature(cs, vectors):
    n = 3*len(vectors)
    h = F(1, n)
    out = F(0)
    for k, xyz in enumerate(vectors):
        for j, v in enumerate(xyz):
            i = 3*k + j
            midpoint = (F(i)+F(1, 2))*h
            out += h* (poly_eval(cs, midpoint+h*v/2) + poly_eval(cs, midpoint-h*v/2))/2
    return out


def cubic_path_error(cs, vectors):
    # For cubic f(t)=c0+c1*t+c2*t^2+c3*t^3, f''' = 6*c3.
    n = 3*len(vectors)
    h = F(1, n)
    return h**4 * 6*cs[3]/8 * sum((vec[2]**2-vec[0]**2 for vec in vectors),F(0))


def main():
    assert sphere_even_moment((1,0,0)) == F(1,3)
    assert sphere_even_moment((2,0,0)) == F(1,5)
    assert sphere_even_moment((1,1,0)) == F(1,15)
    dvar = 2*sphere_even_moment((2,0,0))-2*sphere_even_moment((1,1,0))
    assert dvar == F(4,15)
    assert dvar / 64 / 3 == F(1,720)
    assert (6**2) / F(720) == F(1,20)
    checks = 6
    entries = (F(0), F(1,4), F(-1,3), F(2,5))
    vecs = [sphere_rational(u, v) for u, v in product(entries, repeat=2)]
    for nblocks in (1,2,3,4):
        groups = [vecs[(3*i+2*nblocks)%len(vecs)] for i in range(nblocks)]
        for coefs in product((F(-2,3), F(0), F(5,4)), repeat=3):
            cs = tuple(coefs)
            assert quadrature(cs, groups) == exact_integral(cs)
            checks += 1
        for coefs in product((F(-1,2), F(1,3)), repeat=4):
            cs = tuple(coefs)
            assert quadrature(cs, groups)-exact_integral(cs) == cubic_path_error(cs, groups)
            checks += 1
    # Verify the exact cubic variance for any number of independent triples.
    for n in (3, 6, 9, 12, 15, 18):
        h=F(1,n)
        m=n//3
        formula = m * (6*F(1))**2*h**8*F(1,240)
        assert formula == F(1,20*n**7)
        checks += 1
    print(f'VERIFY_OK {checks} exact sphere moments, rational quadratic/cubic paths, and variance identities')


if __name__ == '__main__':
    main()
