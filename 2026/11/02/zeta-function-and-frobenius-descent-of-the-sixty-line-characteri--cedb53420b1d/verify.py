"""Exact arithmetic and divisor-incidence checks for a 60-line quartic over F4.

Requires Python 3.10+ and SymPy (exact rational matrices and Groebner bases).
The polynomial field model is F16=F2[a]/(a^4+a^3+a^2+a+1), a represented by 0b0010.
"""
from itertools import permutations, combinations, product
from collections import Counter
from sympy import Matrix, eye, symbols, expand, diff, groebner, Poly, prod

IRR = 0b11111

def times(x, y):
    z = 0
    while y:
        if y & 1:
            z ^= x
        x <<= 1
        if x & 16:
            x ^= IRR
        y >>= 1
    return z

def power(x, n):
    z = 1
    while n:
        if n & 1:
            z = times(z, x)
        x = times(x, x)
        n //= 2
    return z

def inverse(x):
    assert x
    return power(x, 14)

def rref(rows):
    a = [list(row) for row in rows]
    pivot_row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(pivot_row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot], a[pivot_row] = a[pivot_row], a[pivot]
        d = inverse(a[pivot_row][col])
        a[pivot_row] = [times(d, t) for t in a[pivot_row]]
        for i in range(len(a)):
            if i != pivot_row and a[i][col]:
                c = a[i][col]
                a[i] = [u ^ times(c, v) for u, v in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row, tuple(tuple(row) for row in a)

def e2e4(a):
    e2 = 0
    e4 = 0
    for i, j in combinations(range(5), 2):
        e2 ^= times(a[i], a[j])
    for indices in combinations(range(5), 4):
        t = 1
        for i in indices:
            t = times(t, a[i])
        e4 ^= t
    return e2, e4

def quartic_zero(a, mu):
    e2, e4 = e2e4(a)
    return e4 ^ times(mu, times(e2, e2)) == 0

def points(field, mu):
    ans = []
    examined = 0
    for left_zeros in range(4):
        for tail in product(field, repeat=3 - left_zeros):
            u = (0,) * left_zeros + (1,) + tail
            x = u + (u[0] ^ u[1] ^ u[2] ^ u[3],)
            examined += 1
            if quartic_zero(x, mu):
                ans.append(x)
    q = len(field)
    assert examined == q**3 + q**2 + q + 1
    return ans

def normalize(a):
    d = inverse(next(x for x in a if x))
    return tuple(times(d, x) for x in a)

def orbit_partition(points_list, perm_list):
    points_set = {normalize(p) for p in points_list}
    lengths = []
    while points_set:
        p = next(iter(points_set))
        orb = {normalize(tuple(p[j] for j in permutation)) for permutation in perm_list}
        assert orb <= points_set
        points_set -= orb
        lengths.append(len(orb))
    return Counter(lengths)

def geometric_smoothness():
    # On the patch x0=1, x4=1+x1+x2+x3. The derivative of mu*s2^2
    # vanishes in characteristic 2. All solutions to d(s4)=0 are F2 points.
    x, y, z = symbols('x y z')
    coords = [1, x, y, z, 1+x+y+z]
    e4 = expand(sum(prod(coords[i] for i in ix) for ix in combinations(range(5), 4)))
    basis = groebner([diff(e4, t) for t in (x, y, z)], x, y, z,
                      order='lex', modulus=2)
    expected = [
        x**2+x+z**2+z, x*y+x*z+y*z,
        x*z**2+z**3+z**2, y**2+y+z**2+z,
        y*z**2+z**3+z**2, z**4+z**2
    ]
    got = [Poly(p.as_expr(), x, y, z, modulus=2) for p in basis.polys]
    wanted = [Poly(p, x, y, z, modulus=2) for p in expected]
    assert got == wanted, (got, wanted)
    # The final equation forces z in F2; then the first and fourth force
    # x,y in F2, valid even after extending the coefficient field.
    for u in product((0, 1), repeat=3):
        xx = (1, *u, 1 ^ u[0] ^ u[1] ^ u[2])
        assert e2e4(xx) in ((1, 0), (0, 1))
    print('GEOMETRIC_SMOOTHNESS=YES;GRADIENT_GROEBNER_POLYS=6')

def main():
    alpha = 2
    assert power(alpha, 5) == 1 and alpha != 1
    a2, a3 = power(alpha, 2), power(alpha, 3)
    mu = 1 ^ a2 ^ a3
    assert power(mu, 3) == 1 and mu != 1 and power(mu, 4) == mu
    f4 = [0, 1, mu, power(mu, 2)]
    assert len(set(f4)) == 4
    print('FIELD=F2[a]/(a^4+a^3+a^2+a+1);alpha=2;mu=', mu)
    geometric_smoothness()
    p4 = points(f4, mu)
    p16 = points(range(16), mu)
    assert len(p4) == 20 and len(p16) == 554
    perm_list = list(permutations(range(5)))
    p4_orbits = orbit_partition(p4, perm_list)
    p16_orbits = orbit_partition(p16, perm_list)
    assert p4_orbits == Counter({20: 1})
    assert p16_orbits == Counter({20: 1, 24: 1, 30: 1, 60: 4, 120: 2})
    print('POINTS_F4=20;S5_POINT_ORBITS_F4=20^1')
    print('POINTS_F16=554;S5_POINT_ORBITS_F16=20^1,24^1,30^1,60^4,120^2')

    # A line from Rams and Schuett's explicit Section 8 construction.
    b = a3 ^ a2 ^ alpha ^ 1
    v1 = (a3, 1, 0, a3 ^ alpha ^ 1, alpha)
    v2 = (b, 0, 1, 1, b)
    for r, s in product(range(16), repeat=2):
        xx = tuple(times(r, x) ^ times(s, y) for x, y in zip(v1, v2))
        assert quartic_zero(xx, mu)
    line_dict = {}
    for p in perm_list:
        span = rref([tuple(v1[j] for j in p), tuple(v2[j] for j in p)])[1]
        line_dict.setdefault(span, p)
    lines = sorted(line_dict)
    assert len(lines) == 60
    idx = {v: i for i, v in enumerate(lines)}
    frob = []
    for lin in lines:
        lin2 = rref([[power(x, 4) for x in v] for v in lin])[1]
        assert lin2 in idx
        frob.append(idx[lin2])
    assert all(frob[frob[i]] == i and frob[i] != i for i in range(60))
    print('LINES_GEOMETRIC=60;F4_LINE_ORBITS=2^30;F4_RATIONAL_LINES=0')

    # Intersection of distinct lines is detected by rank <= 3 in F16^5.
    inc = [[0]*60 for _ in range(60)]
    for i in range(60):
        for j in range(i):
            if rref(lines[i] + lines[j])[0] == 3:
                inc[i][j] = inc[j][i] = 1
    assert all(sum(row) == 17 for row in inc)
    adjacency = Matrix(inc)
    spectral = (symbols('T')-17)*(symbols('T')-2)**40*(symbols('T')+3)**5*(symbols('T')+4)**4*(symbols('T')+5)**5*(symbols('T')+8)**4*(symbols('T')+9)
    assert expand(adjacency.charpoly(symbols('T')).as_expr()-spectral) == 0
    gram = adjacency - 2*eye(60)
    assert gram.rank() == 20
    orbits = []
    seen = set()
    for i in range(60):
        if i not in seen:
            orbit = tuple(sorted((i, frob[i])))
            orbits.append(orbit)
            seen.update(orbit)
    assert len(orbits) == 30
    norm = Matrix(60, 30, lambda i, j: int(i in orbits[j]))
    assert (gram*norm).rank() == 10
    print('LINE_MEETING_VALENCY=17;LINE_INTERSECTION_GRAM_RANK=20')
    print('FROBENIUS_INVARIANT_DIVISOR_RANK=10;GEOMETRIC_PICARD_RANK=20')

    # For a smooth quartic K3, dim H^2_et = 22 and H^1=H^3=0.
    # 20 divisor eigenvalues: 4*(+1)^10 and 4*(-1)^10.
    # The two others are fixed by #S(F4)=20 and #S(F16)=554.
    tr1 = len(p4) - (1 + 4**2)
    tr2 = len(p16) - (1 + (4**2)**2)
    trans_trace = tr1 - 4*(10-10)
    trans_sq_trace = tr2 - 16*20
    trans_det = (trans_trace**2 - trans_sq_trace)//2
    assert (tr1, tr2, trans_trace, trans_sq_trace, trans_det) == (3, 297, 3, -23, 16)
    print('H2_FROB_POLYNOMIAL=(1-4T)^10(1+4T)^10(1-3T+16T^2)')
    print('ZETA=1/((1-T)(1-16T)(1-16T^2)^10(1-3T+16T^2))')
    print('GEOMETRIC_PICARD_RANK=20;PICARD_RANK_F4=10;PICARD_RANK_F16=20')
    print('CRYSTALLINE_SLOPES=0^1,1^20,2^1;ORDINARY=YES')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
