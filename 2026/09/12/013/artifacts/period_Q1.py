"""Exact Gaussian-period polynomial for Q1 = degree-5 subfield of Q(zeta_25).

Q1 = first layer of cyclotomic Z_5-extension of Q.
H = {5th powers mod 25} = {1,7,18,24} (order 4); cosets 2^j*H (j=0..4).
eta_j = sum_{a in 2^j H} zeta^a, P(X) = prod(X - eta_j) in Z[X].
All arithmetic exact in Z[x]/(Phi_25), Phi_25 monic so reduction is exact.
"""
import json
from sympy import symbols, Poly, ZZ, QQ, factorint, gcd as sp_gcd

x = symbols('x')
Phi = Poly(x**20 + x**15 + x**10 + x**5 + 1, x, domain=ZZ)

def mod_phi(p):
    return p.rem(Phi)

def sigma(p, c):
    return mod_phi(Poly(p.as_expr().subs(x, x**c), x, domain=ZZ))

H = [1, 7, 18, 24]
assert sorted((a * b) % 25 for a in H for b in [7]) == H  # H = <7>
# coset representatives 2^j, j=0..4, distinct mod H
reps = [pow(2, j, 25) for j in range(5)]
cosets = [[(r * h) % 25 for h in H] for r in reps]
flat = sorted(sum(cosets, []))
assert flat == sorted((Z for Z in range(1, 25) if Z % 5 != 0)), flat  # partition of (Z/25)^x

eta0 = mod_phi(sum((Poly(x**a, x, domain=ZZ) for a in cosets[0]), Poly(0, x, domain=ZZ)))
etas = [mod_phi(sigma(eta0, r)) for r in reps]

# P(X) = prod(X - eta_j) with coefficients in Z[x]/(Phi); check they are scalars
X = symbols('X')
coeffs = [Poly(1, x, domain=ZZ)]
for e in etas:
    coeffs = [mod_phi(coeffs[k] * (-e) if k == 0 else mod_phi(coeffs[k] * (-e) + coeffs[k - 1]))
              if k < len(coeffs) else coeffs[k - 1] for k in range(len(coeffs) + 1)]
# coeffs[k] = coeff of X^k
Pcoef_int = []
for c in coeffs:
    cl = c.all_coeffs() if not c.is_zero else [0]
    assert len(cl) == 1, f"non-scalar coefficient: {c}"
    Pcoef_int.append(int(cl[0]))
P = Poly(sum(c * X**k for k, c in enumerate(Pcoef_int)), X, domain=ZZ)
assert P.degree() == 5 and P.LC() == 1
print("m_Q1(X) =", P.as_expr())
print("coeffs (X^0..X^4, monic):", Pcoef_int)

# discriminant: expect 5^a * square
D = int(P.discriminant())
print("disc =", D)
fac = factorint(abs(D))
print("disc factors:", fac)
assert D > 0, "totally real field needs positive disc"
rest = abs(D)
a5 = 0
while rest % 5 == 0:
    rest //= 5
    a5 += 1
s = int(rest**0.5 + 0.5)
assert s * s == rest, f"cofactor {rest} not a square -> index/minpoly problem"
print(f"disc = 5^{a5} * {s}^2  (power of 5 times square: only 5 ramifies)")

# Eisenstein at 5?
cs = P.all_coeffs()[1:]
eis = all(int(c) % 5 == 0 for c in cs) and (int(P.eval(0)) % 25 != 0)
print("Eisenstein at 5:", eis)

# mod-5 shape
Pm5 = Poly(P.as_expr(), X, domain='ZZ')
from sympy import GF
P5 = Poly([int(c) % 5 for c in P.all_coeffs()], X, domain=GF(5))
print("mod 5:", P5.factor_list())

# irreducibility: exact factorization over QQ (Berlekamp-Zassenhaus, exact)
flQ = P.factor_list()
print("factor over QQ:", [(str(f), e) for f, e in flQ[1]])
assert len(flQ[1]) == 1 and flQ[1][0][1] == 1 and flQ[1][0][0].degree() == 5
print("IRREDUCIBLE over QQ.")
# mod-p irreducibility witness search (Frobenius certificate, independently checkable)
for p in [2, 3, 7, 11, 13, 17, 19, 23, 29, 31]:
    Pp = Poly([int(c) % p for c in P.all_coeffs()], X, domain=GF(p))
    fl = Pp.factor_list()[1]
    degs = sorted([f.degree() for f, e in fl for _ in range(e)])
    tag = "IRREDUCIBLE" if degs == [5] else ""
    print(f"mod {p}: degrees {degs} {tag}")
    if degs == [5]:
        print(f" Pirmod witness: irreducible mod {p} => irreducible over Q; roots are Galois-conjugate Gaussian periods => splitting field abelian => Gal = C5.")
        break

with open("m_Q1.json", "w") as f:
    json.dump({"coeffs_low_to_high": Pcoef_int, "disc": D, "disc_5exp": a5,
               "disc_cofactor_sqrt": s, "eisenstein_5": eis}, f, indent=1)
print("saved m_Q1.json")
