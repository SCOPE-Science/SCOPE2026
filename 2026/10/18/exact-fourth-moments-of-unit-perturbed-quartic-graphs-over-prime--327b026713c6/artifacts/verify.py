"""Independent exact-integer tests of quartic-deformation collision energies."""
from collections import Counter


def character(a, p):
    a %= p
    if a == 0:
        return 0
    e = pow(a, (p - 1) // 2, p)
    assert e in (1, p - 1)
    return 1 if e == 1 else -1


def energy_formula(p, c):
    assert p >= 5 and c % p
    x = character(-3, p)
    y = character(6 * c, p)
    j = 1 + character(-6 * c, p)
    return 6 * p**4 + p**3 * (y - 6 - 2 * x - 2 * j) + p**2 * (4 * x + 3 * j)


def direct_energy(p, c):
    n = p * p
    vals = [(x**4 + c * x*x) % n for x in range(n)]
    fibers = Counter(((x+y) % n, (vals[x]+vals[y]) % n)
                     for x in range(n) for y in range(n))
    return sum(v*v for v in fibers.values())


def residue_geometry(p, c):
    x = character(-3, p)
    y = character(6 * c, p)
    j = 1 + character(-6*c, p)
    H = p - x
    U = 3 * p*p + p * (y - 3) + 2*x + j
    I = 3*p - 2*x - 2*j
    a = b = h1 = h2 = tr = 0
    for s in range(p):
        for t in range(p):
            for u in range(p):
                v = (t-u) % p == 0
                w = (t+u) % p == 0
                z = (t*t + u*u + 6*s*s + 4*c) % p == 0
                k = int(v) + int(w) + int(z)
                a += (k >= 1)
                b += (k >= 2)
                h1 += (v and z)
                h2 += (w and z)
                tr += (v and w and z)
    assert (a,b,h1,h2,tr) == (U,I,H,H,j), (p,c,(a,b,h1,h2,tr),(U,I,H,H,j))
    return a,b


def main():
    direct_tests = 0
    geo_tests = 0
    cases = 0
    for p in (5,7,11,13,17):
        for c in (1,2,1+p,2+p):
            cases += 1
            assert direct_energy(p,c) == energy_formula(p,c), (p,c)
            direct_tests += p**4
    for p in (5,7,11,13,17,19,23,29,31):
        for c in (1,2,3,1+p):
            U,I = residue_geometry(p,c)
            assert p*p*U + (p**3-p*p)*I == energy_formula(p,c)
            geo_tests += p**3
    assert direct_energy(5, 0) == 2225
    for p in (5,7,11,13,17):
        plus = next(c for c in range(1,p) if character(6*c,p) == 1)
        minus = next(c for c in range(1,p) if character(6*c,p) == -1)
        delta = energy_formula(p,plus)-energy_formula(p,minus)
        predicted = -2*p*p*(p-3) if p%4==1 else 6*p*p*(p-1)
        assert delta == predicted
    print(f'PASS direct_fibers={direct_tests} residue_points={geo_tests} cases={cases} moduli=5 geometry_primes=9 pure_comparison=1 phase_split=5')


if __name__ == '__main__':
    main()
