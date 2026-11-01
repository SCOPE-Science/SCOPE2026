"""Reproduction checks for four-dimensional cross-polytope lattice Fourier data.

Requires Python 3 and SymPy. Tests are finite corroboration, not proofs.
"""
import itertools
import math
import random
import sympy as sp


def multiplicity(u, m):
    windows = [range(math.floor(x - m), math.ceil(x + m) + 1) for x in u]
    return sum(
        sum(abs(x-z) for x,z in zip(u, lattice_point)) < m - 1e-12
        for lattice_point in itertools.product(*windows)
    )


def formula(k):
    assert len(k) == 4
    a = sorted(map(abs, k))
    if a == [0]*4:
        return sp.Rational(2, 3)
    if a[:3] == [0,0,0]:
        return 2/(sp.pi**2 * a[3]**2)
    if a[1] == a[2] == a[3]:
        repeated = a[2]
        if a[0] == repeated:
            return -1/(4*sp.pi**2*repeated**2)
        return 1/(2*sp.pi**2*(a[0]**2-repeated**2))
    if a[0] == a[1] == a[2] and a[3] != a[2] and a[2] > 0:
        return 1/(2*sp.pi**2*(a[3]**2-a[2]**2))
    return sp.S(0)


def residue_coeff(k):
    """Direct Laurent-coefficient extraction of the inverse Laplace transform."""
    s, t = sp.symbols('s t')
    R = s**3
    for v in k:
        R /= s*s + v*v
    orders = {}
    for v in set(map(abs, k)):
        if v:
            orders[sp.I*v] = sum(abs(x)==v for x in k)
            orders[-sp.I*v] = orders[sp.I*v]
        else:
            orders[0] = 2*sum(x==0 for x in k)
    total = 0
    for pole, order in orders.items():
        analytic = sp.cancel((s-pole)**order * R)
        for j in range(order):
            coeff = sp.limit(sp.diff(analytic, s, j), s, pole)/sp.factorial(j)
            total += coeff * t**(order-1-j)/sp.factorial(order-1-j)
    # k coordinates are integers, so each exp(2*pi*i*k) equals one.
    return sp.simplify(16*total.subs(t, 2*sp.pi)/(2*sp.pi)**4)


def run():
    vectors = [(0,0,0,0),(0,0,0,1),(0,0,0,2),(1,1,1,1),
               (1,1,1,2),(1,1,1,0),(1,2,3,4),(1,1,2,2),
               (0,0,1,1),(0,1,2,3),(2,2,2,0),(2,2,2,3)]
    for k in vectors:
        computed = residue_coeff(k)
        assert sp.simplify(computed-formula(k)) == 0, (k,computed,formula(k))
    assert all(sum(1 for k in itertools.product(range(-N,N+1), repeat=4)
                   if formula(k)!=0) == 64*N*N-8*N+1
               for N in [0,1,2])
    rng = random.Random(160802417)
    checked = 0
    for m in range(1,6):
        for _ in range(60):
            u = [rng.random() for _ in range(4)]
            predicted = m*m*multiplicity(u, 1) + 2*(m**4-m*m)//3
            assert multiplicity(u,m) == predicted, (m,u)
            checked += 1
    print('PASS:',len(vectors),'symbolic frequency tests, 3 support counts,',checked,'periodization samples')

if __name__=='__main__':
    run()
