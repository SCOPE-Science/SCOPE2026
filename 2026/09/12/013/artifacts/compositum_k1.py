"""k1 compositum polynomial: resultant construction + discriminant/ramification data.

k  = Q(y)/(y^2 - y - 7)            (y = omega = (1+sqrt29)/2)
Q1 = Q(x)/(x^5 - 10x^3 + 5x^2 + 10x + 1)   (from period_Q1.py, Gal C5, only 5 ramifies)
k1 = k*Q1, [k1:Q] = 10 (linearly disjoint: k ramified at {2? no: 29} only... k=Q(sqrt29)
ramified at 29; Q1 ramified only at 5; 29 unramified in Q1, 5 unramified in k).
Compositum polynomial via resultant in y appended to sympy check; discriminant factorization.
"""
import json
from sympy import symbols, Poly, ZZ, factorint, GF, QQ

x, y, T = symbols('x y T')
mQ1 = Poly(x**5 - 10*x**3 + 5*x**2 + 10*x + 1, x, domain=ZZ)
mk = Poly(y**2 - y - 7, y, domain=ZZ)

# compositum minimal polynomial of x + y over Q: resultant_y(mk(y), mQ1(T - y))
inner = Poly(mQ1.as_expr().subs(x, T - y), y, domain=ZZ[T])
res = mk.resultant(inner, y)[0]  # (resultant, cofactors...)
from sympy import expand
R = Poly(expand(res), T, domain=ZZ)
print("deg =", R.degree(), " monic:", R.LC() == 1)
flQ = R.factor_list()
print("factors over QQ:", [(str(f), e) for f, e in flQ[1]])
assert len(flQ[1]) == 1 and flQ[1][0][1] == 1 and flQ[1][0][0].degree() == 10
print("IRREDUCIBLE degree 10 => [k1:Q]=10, [k1:k]=5.")

D = int(R.discriminant())
print("disc =", D)
print("factors:", factorint(abs(D)))
# ramification: only primes dividing disc
print("prime divisors:", sorted(factorint(abs(D)).keys()))
# mod-5 factorization shape (expect powers of degree-1/2 factors: 5 totally ramified in Q1,
# splits in k -> two totally ramified primes => residue degrees 1 each, e=5 each)
R5 = Poly([int(c) % 5 for c in R.all_coeffs()], T, domain=GF(5))
print("mod 5:", [(str(f), e) for f, e in R5.factor_list()[1]])
# mod-29 shape (unramified in Q1 tower direction... 29 ramified in k/quadratic subfield)
R29 = Poly([int(c) % 29 for c in R.all_coeffs()], T, domain=GF(29))
print("mod 29:", [(str(f), e) for f, e in R29.factor_list()[1]])
# mod-7 witness irreducibility? (7 splits in k? (29/7)=(1/7)=1 yes; Frobenius test)
for p in [7, 11, 13]:
    Rp = Poly([int(c) % p for c in R.all_coeffs()], T, domain=GF(p))
    fl = Rp.factor_list()[1]
    print(f"mod {p}:", [(str(f), e) for f, e in fl])

with open("m_k1.json", "w") as f:
    json.dump({"coeffs_low_to_high": [int(c) for c in reversed(R.all_coeffs())],
               "disc": D, "disc_factors": {str(k): v for k, v in factorint(abs(D)).items()}},
              f, indent=1)
print("saved m_k1.json")
print("poly:", R.as_expr())
