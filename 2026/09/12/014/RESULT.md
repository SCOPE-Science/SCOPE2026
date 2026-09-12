# P8 six-reflection Coxeter lift: finite-order rigidity (negative resolution)

## Context
Let f be an Arnold simple-elliptic singularity of type P8 (Dolgachev numbers (3,3,3)).
Its Milnor lattice M has rank 8 (Milnor number mu(P8)=8) with a rank-2 radical
R = ker(<,>) and a rank-6 quotient Q = M/R of E6 type. The finite-to-infinite
monodromy transition at the simple-elliptic threshold is sharpest in Coxeter lifts:
the quotient product may be finite Weyl while the full lattice lift could carry an
elliptic translation along the radical. The admitted target asked whether the
distinguished six-reflection Coxeter product has quotient order 12 with the E6
Coxeter characteristic polynomial and its full-lattice 12th power is a nontrivial
translation, versus the 12th power being the identity (finite-lift rigidity).

## Definitions (fixed before computation)
- M = Z^8 with symmetric Gabrielov Gram matrix G, all diagonal entries -2.
  Quotient block G11 = -C(E6) on e_0..e_5 (Bourbaki chain 1-3-4-5-6, branch 2 on 4),
  with det(-G11)=3 and leading principal minors 2,4,6,5,4,3 (negative-definite).
  Mixed columns G[e_i,e_6]=(0,1,0,0,0,0), G[e_i,e_7]=(0,1,0,-1,0,0);
  corner [[G66,G67],[G76,G77]]=[[-2,1],[1,-2]].
- Radical basis r0=(1,2,2,3,2,1,1,0), r1=(-1,-1,-2,-3,-2,-1,0,1):
  G*r0=G*r1=0, isotropic plane, each primitive, jointly saturated
  (gcd of 2x2 minors of the 8x2 matrix = 1). Projection Phi: M -> Z^6 kills R with
  [e_6]=-(e_0+2e_1+2e_2+3e_3+2e_4+e_5), [e_7]=(e_0+e_1+2e_2+3e_3+2e_4+e_5).
- Picard-Lefschetz reflections S_i(x)=x+<x,e_i>e_i (i.e. x-2<x,e_i>/<e_i,e_i> e_i
  since <e_i,e_i>=-2), verified involutive G-isometries, hence in O(M).
  For i<6 each S_i preserves R and induces s_i in O(Q).
- c_M = S_5 S_4 S_3 S_2 S_1 S_0 (apply S_0 first); c_Q its induced quotient map.
  Quotient matrices agree entrywise with the standard E6-Cartan reflection product.
  No braid-group element is evaluated; all operators lie in O(M) and O(Q).

## Result
On the fixed Gabrielov data, the quotient-order half holds and the
nontrivial-translation half is false:
1. c_Q has exact order 12: c_Q^12=I_6, with c_Q^k != I for k=1,2,3,4,6
   (logged nonzero witness entries; every proper divisor of 12 divides 1,2,3,4 or 6).
2. chi(c_Q)=x^6+x^5-x^3+x+1 = Phi_12(x)*Phi_3(x) with Phi_12=x^4-x^2+1,
   Phi_3=x^2+x+1, the E6 Coxeter polynomial (exponents 1,4,5,7,8,11).
3. c_M has exact order 12: c_M^12=I_8 (all 64 entries of c_M^12-I zero), with
   c_M^k != I for k=1,2,3,4,6 (logged witnesses).
4. Hence the radical translation component is trivial: v0=0 with Seifert
   divisibility 0 (every integer divides 0; no primitive isotropic direction), and
   chi(c_M)=(x^6+x^5-x^3+x+1)(x-1)^2, consistent with identity on R.
This is the finite-lift rigidity (negative) resolution of the target: the claimed
nontrivial primitive-isotropic translation is disproved on the fixed data, while the
exact order-12 quotient certificate holds.

## Proof / evidence
Exact integer-matrix certificate, replayable via `python3 output/artifacts/compute7.py`:
- G*r0=G*r1=0, det G=0, rank G=6; gcd(r0)=gcd(r1)=1; 2x2-minor gcd=1 (saturated).
- Each S_i verified involution and G-isometry (S^T G S=G).
- c_M isometry; c_M^12==I with order loop first hitting 12; non-identity witnesses
  at 1,2,3,4,6.
- Quotient Cq obtained via Phi with intertwining Cq*Phi=Phi*cM verified; Cq order 12
  with witnesses at 1,2,3,4,6.
- Characteristic polynomials via Bareiss determinants at n+1 integer points plus
  Vandermonde interpolation: Cq coeffs [1,1,0,-1,0,1,1]; cM coeffs
  [1,-1,-1,0,2,0,-1,-1,1]=chi_Q*(x-1)^2, independently rechecked at t=0,1,2 (1,3,91).
- det(-G11)=3 with leading principal minors 2,4,6,5,4,3.
- Quotient reflections cross-checked entrywise against the standard E6 Cartan
  construction S[j][k]=delta-C[i][k] delta_{j,i} (compute5.py); Phi_12*Phi_3 expansion
  checked (compute6.py). The audit independently re-executed compute7.py and
  Fraction-determinant spot checks with identical results.

## Limitations
The rigidity verdict is tied to the fixed published Gabrielov Gram data and the
ordered distinguished product S_5...S_0. A 720-ordering scan suggested the same
rigidity for all orderings but carries a known charpoly-print bug, so only the
distinguished product bears the full audited certificate. Analytic Torelli, period-map,
or deformation consequences beyond the matrix identity are not proved.

## Reproducibility
Run `python3 output/artifacts/compute7.py` (final certificate: order witnesses,
charpolys, radical/saturation checks, discriminant), `python3
output/artifacts/compute5.py` (Cartan cross-check), `python3
output/artifacts/compute6.py` (factorisation check) with Python 3 stdlib only
(Fraction arithmetic; no external packages).

## References
- W. Ebeling, The Milnor lattices of the elliptic hypersurface singularities,
  Proc. London Math. Soc. (3) 53 (1986), 85-111 (P8 Gram/radical/E6-quotient inputs).
- V. Goryunov, D. Kerner, Automorphisms of P8 singularities and the complex
  crystallographic groups, arXiv:0806.1720.
- W. Ebeling, Distinguished bases and monodromy of complex hypersurface
  singularities, arXiv:1905.12435.
- T. A. Springer, Regular elements of finite reflection groups (E6 Coxeter order 12).
