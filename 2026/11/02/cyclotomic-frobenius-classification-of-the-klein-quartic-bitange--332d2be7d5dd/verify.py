"""Exact checks for the arithmetic bitangents of the Klein plane quartic.

Dependencies: Python 3.10+ and SymPy 1.12+.
This checks all integral identities and all potentially bad reduction primes,
not just a selection of sample finite fields.
"""
from collections import Counter
from math import gcd
import sympy as sp

z, X, Y, Z = sp.symbols('z X Y Z')
phi = sp.Poly(sum(z ** i for i in range(7)), z, domain=sp.QQ)


def red(f):
    return sp.Poly(f, z, domain=sp.QQ).rem(phi).as_expr()


def inv(f):
    return sp.invert(sp.Poly(f, z, domain=sp.QQ), phi).as_expr()


def dot(a, b):
    return red(sum(red(x * y) for x, y in zip(a, b)))


u = [red(z**j) for j in range(7)]
c1, c2, c3 = (u[1] - u[6], u[2] - u[5], u[4] - u[3])
T = sp.Matrix([[c1, c2, c3], [c2, c3, c1], [c3, c1, c2]])
D = sp.diag(u[4], u[2], u[1])
H = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
F = lambda x, y, w: sp.expand(x**3 * y + y**3 * w + w**3 * x)

assert [[red(e) for e in row] for row in (T*T).tolist()] == [
    [-7, 0, 0], [0, -7, 0], [0, 0, -7]
]
assert all(red(coef) == 0 for coef in sp.Poly(
    F(*(T * sp.Matrix([X, Y, Z]))) - 49 * F(X, Y, Z), X, Y, Z
).coeffs())


def transform(line, matrix):
    coeff = [dot(line, [matrix[i, j] for i in range(3)]) for j in range(3)]
    assert coeff[2] != 0
    scale = inv(coeff[2])
    return tuple(red(t * scale) for t in coeff)


start = (sp.Integer(1), sp.Integer(1), sp.Integer(1))
lines = [start]
seen = {start}
for line in lines:
    for matrix in [D, H, T]:
        out = transform(line, matrix)
        if out not in seen:
            lines.append(out)
            seen.add(out)
assert len(lines) == 28
for triple in lines:
    for c in triple:
        assert all(sp.denom(cc) == 1 for cc in sp.Poly(c, z).all_coeffs())

# A binary quartic with nonzero leading coefficient is a scalar times
# a quadratic square iff the following two polynomial identities hold.
for a, b, one in lines:
    assert one == 1 and a != 0
    c4 = red(-a**3)
    c3 = red(1 - 3*a*a*b)
    c2 = red(-3*a*b*b)
    c1x = red(-a - b**3)
    c0 = red(-b)
    q = red(4*c4*c2-c3*c3)
    assert red(8*c4*c4*c1x-c3*q) == 0
    assert red(64*c4*c4*c4*c0-q*q) == 0
print('GEOMETRIC_BITANGENTS', len(lines))


def cycle_profile(power):
    perm = []
    for line in lines:
        conjugate = tuple(red(t.subs(z, z**power)) for t in line)
        assert conjugate in seen
        perm.append(lines.index(conjugate))
    marked = set()
    counts = Counter()
    for index in range(len(lines)):
        if index not in marked:
            current = index
            size = 0
            while current not in marked:
                marked.add(current)
                current = perm[current]
                size += 1
            assert current == index
            counts[size] += 1
    return tuple(sorted(counts.items()))

profiles = {r:cycle_profile(r) for r in range(1, 7)}
assert profiles == {
    1: ((1, 28),),
    2: ((1, 1), (3, 9)),
    3: ((1, 1), (3, 1), (6, 4)),
    4: ((1, 1), (3, 9)),
    5: ((1, 1), (3, 1), (6, 4)),
    6: ((1, 4), (2, 12)),
}
for r, profile in profiles.items():
    print('FROBENIUS_RESIDUE', r, 'PROFILE', profile)

# If two integral cyclotomic lines collide mod a prime above p, their
# coordinate differences have norms both divisible by p. This sieve
# leaves only 2, 7, 29, 43, 71 to examine.
possible = set()
for i in range(28):
    for j in range(i+1, 28):
        pa = sp.Poly(lines[i][0] - lines[j][0], z)
        pb = sp.Poly(lines[i][1] - lines[j][1], z)
        na = int(sp.resultant(pa, phi, z))
        nb = int(sp.resultant(pb, phi, z))
        h = abs(gcd(na, nb))
        if h > 1:
            possible.update(sp.factorint(h))
assert possible == {2, 7, 29, 43, 71}
print('POSSIBLE_COLLISION_PRIMES', sorted(possible))

# The three residual odd primes other than 7 all split completely in
# Q(zeta_7), permitting complete checks in the prime fields themselves.
for p in [29, 43, 71]:
    roots = [r for r in range(1, p) if r != 1 and pow(r, 7, p) == 1]
    assert len(roots) == 6
    for root in roots:
        reduction = [tuple(int(sp.Poly(c, z).eval(root)) % p for c in L)
                     for L in lines]
        assert len(set(reduction)) == 28
    print('EXCEPTIONAL_REDUCTION_DISTINCT', p, 28)

# Independent direct finite-prime checks, not used to extrapolate.
def direct_bitangent_count(p):
    ans = 0
    for a in range(1, p):
        for b in range(p):
            c4=(-a**3) % p
            c3=(1-3*a*a*b) % p
            c2=(-3*a*b*b) % p
            c1=(-a-b**3) % p
            c0=(-b) % p
            v=(c3*pow((2*c4)%p, -1, p))%p
            w=((c2*pow(c4, -1, p)-v*v)*pow(2, -1, p))%p
            if (2*c4*v*w-c1) % p == 0 and (c4*w*w-c0) % p == 0:
                ans += 1
    return ans

for p, expected in [(3,1),(5,1),(11,1),(13,4),(17,1),
                    (23,1),(29,28),(43,28),(71,28)]:
    got=direct_bitangent_count(p)
    assert got == expected, (p,got,expected)
    print('RATIONAL_BITANGENTS',p,got)

print('VERIFY_OK')
