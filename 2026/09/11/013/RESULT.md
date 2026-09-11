# Corrected WLP certificate for the non-monomial type-(2,3,3) complete intersection over F7

## Context

The weak Lefschetz property (WLP) for graded Artinian algebras is a recognized program
(Stanley, Watanabe, Migliore-Nagel, Gondim, Iarrobino). In characteristic zero the
codimension-3 complete-intersection story is closed and socle-≤6 Gorenstein algebras have
WLP, while in positive characteristic only monomial complete intersections have been
classified (Brenner-Kaid, Kustin-Vraciu, Cook). The admitted investigation targeted the
smallest mixed-degree codimension-3 complete-intersection type (2,3,3) in characteristic
p≥7 with sharp witnesses in characteristics 2, 3, 5, and pre-registered a fallback
certificate for one explicit triple over F7. Executing that exact fallback audit showed
its linear-form clause to be deterministically false and produced the corrected
certificate below as an emergent finding on the same triple.

## Definitions

Let k = F7, R = k[x,y,z], and

I = (x^2+yz, y^3+xz^2, z^3),   A = R/I,

of type (2,3,3) (degrees 2, 3, 3). For a linear form L = ax+by+cz write
×L : [A]2 → [A]3 for multiplication. Let D(a,b,c) = det(×L) in fixed quotient bases.
A has WLP if some L makes every ×L : Ai → A(i+1) have maximal rank; here the middle map
[A]2 → [A]3 is the deciding degree. The Macaulay dual generator F ∈ k[X,Y,Z]5 satisfies
Ann(F) = I with x,y,z acting as ∂X,∂Y,∂Z; its second Hessian Hess^2(F) is the 5×5 matrix
of second-order mixed partials in the degree-2 operator basis below.

## Result

1. A is Artinian (dim(R/I) = 0) with Hilbert function (1,3,5,5,3,1) and socle degree 5;
   hence I is a complete intersection.
2. ℓ = x+y+z is NOT a weak Lefschetz element: ×ℓ : [A]2 → [A]3 has rank 4 < 5
   (det = 0), with explicit kernel element v = 4xy+2xz+3y^2+yz+z^2, (x+y+z)v = 0 in A.
3. ℓ = y IS a weak Lefschetz element: ×y : [A]2 → [A]3 is the 5×5 identity (det = 1),
   and the full rank profile of ×y is (1,3,5,3,1), maximal in every degree. Hence A
   has WLP. (ℓ = x also gives full ranks; ℓ = z drops to middle rank 4.)
4. The Macaulay dual generator is, up to scale, F = X^5 − 20X^3YZ + 30XY^2Z^2 − Y^5,
   and over Q the exact bridge identity holds:
   det Hess^2(F) = −24883200000 · D_Q,
   where D_Q(a,b,c) = −a^5 − 4a^3bc − 3ab^2c^2 + b^5 is the universal middle-map
   determinant. Since 24883200000 = 2^15·3^5·5^5 ≡ 1 (mod 7), the Hessian certificate
   is valid and nonzero mod 7 (det 6 at the y-point, 0 at (1,1,1)).

Consequence: the admitted fallback triple and its WLP are correct, but the prescribed
linear form L = x+y+z provably fails; the certified Lefschetz element is L = y
(equivalently L = x). Any regression row for this triple must use y (or x).

## Proof / evidence

Quotient monomial bases (agree in Macaulay-matrix and Gröbner paths):
[A]2 = {xy, xz, y^2, yz, z^2}; [A]3 = {xy^2, xyz, y^3, y^2z, yz^2}.
Macaulay matrices over F7 in degrees 0..6 give quotient dims (1,3,5,5,3,1,0);
independently the lex Gröbner basis {x^2+yz, xy^3, xz^2+y^3, y^6, y^3z, z^3} yields the
same standard monomials. CI Hilbert-series check: (1−t^2)(1−t^3)^2/(1−t)^3 gives
[1,3,5,5,3,1,0].
Multiplication by x+y+z is [[1,0,1,0,0],[1,1,0,1,0],[0,6,1,0,6],[6,0,1,1,0],[0,6,0,1,1]],
det 0, rank 4 by exact F7 RREF; kernel v above verified by Gröbner reduction.
Multiplication by y is the 5×5 identity (y·xy=xy^2, y·xz=xyz, y·y^2=y^3, y·yz=y^2z,
y·z^2=yz^2 are basis monomials directly), det 1; full ranks (1,3,5,3,1) by exact RREF.
Universal determinant D(a,b,c) = 6a^5+3a^3bc+4ab^2c^2+b^5 over F7 matches the numeric
5×5 determinant on all 343 F7 points (0 mismatches); D(1,1,1) = 14 = 0, D(0,1,0) = 1.
Dual generator: ansatz F ∈ S5 (21 unknowns) annihilated by the three generators acting
as differential operators gives 22 equations of rank 20, nullspace dimension 1 spanned
by F above (exact over Q; valid mod 7 since all differentiations involve integers ≤5).
With A2-operators {dxdy,dxdz,dy^2,dydz,dz^2},
det Hess^2(F) = 24883200000·(X^5+4X^3YZ+3XY^2Z^2−Y^5) = −24883200000·D_Q exactly
(symbolic check); constant 2^15·3^5·5^5 ≡ 1 mod 7.
Replay: output/artifacts/verify_fallback.py prints VERIFY_OK (HF, dim, identity matrix,
det 1); output/artifacts/verify_hessian.py prints HESSIAN_OK (dual annihilation +
evaluated Hessian dets 6 at y, 0 at (1,1,1)).

## Limitations

Proves WLP for this one algebra only; no uniform p≥7 theorem is claimed. The
~12000-trial negative search in characteristics 2 and 5 (F2/F4/F8/F5/F25) is supporting
context, not a non-existence proof, and is not part of the claim. All algebra is exact
finite-field/rational arithmetic in stdlib Python plus SymPy Gröbner crosschecks; no
Macaulay2/Singular was available.

## Reproducibility

- output/artifacts/ci_wlp.py — exact finite-field Macaulay/HF/middle-det pipeline.
- output/artifacts/verify_fallback.py — stdlib-only replay: HF + dim + identity middle
  matrix at L=y + det 1 (prints VERIFY_OK).
- output/artifacts/verify_hessian.py — stdlib-only replay: dual annihilation +
  evaluated second-Hessian dets (prints HESSIAN_OK).
- output/artifacts/certificates.json — machine log: char-3 monomial failure +
  char-7 audit-triple success values.

## References

- A. Kustin, A. Vraciu, The Weak Lefschetz Property for monomial complete intersections,
  arXiv:1110.2822 / Trans. Amer. Math. Soc. 2014 (monomial equigenerated scope only).
- H. Brenner, A. Kaid, A note on the weak Lefschetz property of monomial complete
  intersections in positive characteristic.
- D. Cook II, The Lefschetz properties of monomial complete intersections in positive
  characteristic, arXiv:1111.4979.
- R. Miró-Roig, Q. Tran, The weak Lefschetz property for Artinian Gorenstein algebras
  of codimension three, arXiv:1912.04866 (char-0 background; "only monomial CIs studied"
  in positive characteristic).
- M. Boij et al., On the Weak Lefschetz Property for artinian Gorenstein algebras of
  codimension three, J. Algebra 2014 (char-0 socle≤6 WLP).
