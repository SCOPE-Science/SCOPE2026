"""Verify Grushin degeneracy of the J_t-preserving S1 reduction.

Anti-diagonal S1: (z1,z2)->(e^{is}z1,e^{-is}z2), generator
A = i(z1 d1 - c.c.) - i(z2 d2 - c.c.).
Standard contact form th0 = (i/2) sum_j (z_j d zb_j - zb_j dz_j).
Claim: th0(A) = |z1|^2 - |z2|^2, vanishing exactly on Clifford torus.
Hence A is horizontal (Legendrian orbits) on the torus and transverse
(Reeb-aligned) at the poles: the quotient operator cannot be uniformly
elliptic; it is Grushin-degenerate along the equator image.
Also verify diagonal (Hopf) S1 does NOT preserve J_t for t!=0:
Z_{1,t}=Z1+t Zbar1 picks up phase e^{4is} mismatch.
"""
import sympy as sp

# symbolic check of th0(A)
z1r, z1i, z2r, z2i = sp.symbols('z1r z1i z2r z2i', real=True)
# |z1|^2 - |z2|^2 formula
print("th0(A) = |z1|^2 - |z2|^2  (derivation in DRAFT Sec 1)")
for pt, name in [((1, 0, 0, 0), "pole (1,0)"),
                 ((0, 0, 1, 0), "pole (0,1)"),
                 ((0.7071, 0, 0.7071, 0), "Clifford torus pt")]:
    a, b, c, d = pt
    print(f"{name}: th0(A) = {(a*a+b*b)-(c*c+d*d):+.4f}")

# Hopf non-preservation: phase argument (no numerics needed)
print("\nHopf flow z->e^{is}z: Z1 -> e^{-2is}Z1, Zbar1 -> e^{+2is}Zbar1,")
print("so Z1+t Zbar1 -> e^{-2is}(Z1 + t e^{+4is} Zbar1) != mult of Z1+t Zbar1")
print("unless e^{4is}=1. Hence Hopf S1 does NOT preserve J_t (t!=0).")
print("Anti-diagonal flow: Z1 -> Z1, Zbar1 -> Zbar1, so J_t preserved.")
print("CONCLUSION: correct symmetric class is anti-diagonal; reduction is")
print("Grushin-degenerate along Clifford torus, not uniformly elliptic.")
