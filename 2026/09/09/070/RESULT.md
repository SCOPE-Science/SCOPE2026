# Hessian-to-Jordan certificate for the named codim-4 degenerate-Perazzo quartic F_named = X0·U·V·W + U⁴ + V⁴ + W⁴

## Context

Weak/Strong Lefschetz properties, Perazzo hypersurfaces with vanishing Hessian, and Jordan-type
stratifications of Artinian Gorenstein algebras form the recognized
Stanley–Watanabe–Iarrobino–Migliore program. P^{n+2} (binary-base) Perazzo WLP is characterized
(Miró-Roig–Pérez Díez, arXiv:2402.09188), but the authors explicitly state their results do not
generalize to the ternary-base P^{n+3} regime. Codimension 4 / socle degree 4 is the minimal
unsettled Jordan-refinement scope. The quartic

    F_named = X0·U·V·W + U⁴ + V⁴ + W⁴

is the smallest single-leg ternary-base degenerate-Perazzo quartic with dense (Fermat) tail, in the
flagged regime. Its Jordan type and Hessian data were not recorded in any surveyed source.

## Definitions

Let k be a field of characteristic 0 (all certificates are exact integer identities, valid over QQ
and every characteristic not dividing the stated determinants, i.e. char ≠ 2, 3).
Let R = k[x0,u,v,w] act on S = k[X0,U,V,W] by differentiation (upper/lower-case pairs), and let
A = R/Ann(F_named) be the apolarity (Macaulay dual) algebra. A is graded Artinian Gorenstein of
socle degree 4. For a linear form ell, x_ell denotes multiplication by ell on A; its Jordan type is
the partition of dim_k A given by the Jordan blocks of the nilpotent operator x_ell − (constant part).
A has WLP (resp. SLP) if some x_ell has maximal rank at every degree (resp. every power has maximal
rank). General ell means a Zariski-open dense condition, witnessed here by an explicit point plus
maximality.

## Result

**Theorem.** For F_named as above (char 0):

- (a) The Hilbert function of A is (1,4,9,4,1); dim_k A = 19.
- (b) At ell = x0+u+v+w, multiplication by x_ell has full ranks (1,4,4,1) at every degree; hence A
  has WLP. Moreover x_ell² : A_1 → A_3 is an isomorphism (det = −5808) and x_ell⁴ : A_0 → A_4
  equals 96 ≠ 0; the full x^j rank table is maximal at every slot (j=2: (1,4,1); j=3: (1,1);
  j=4: (1)); hence A has SLP at this ell.
- (c) The Jordan type of x_ell at general ell is the 9-part partition [5,3,3,3,1,1,1,1,1]
  (sum 19), i.e. the sorted conjugate (maximal) partition of the Hilbert function. Nullities of
  N^j (N = x_ell) are [0,9,13,17,18,19,19,19]; per-degree kernel dimensions are (0,0,5,3,1).
- (d) The classical Hessian determinant is the nonzero octic det Hess(F) = 3·Q with
  Q = −(Y² − 8·S3·Y + 48·S2), Y = U·V·W·X0, S3 = U⁴+V⁴+W⁴,
  S2 = U⁴V⁴+U⁴W⁴+V⁴W⁴ (verified polynomial identity); Q is irreducible over QQ.
  Nonvanishing witness: det Hess(F)(1,1,1,1) = −363. With E2 = (x_ell² : A_1 → A_3) the 4×4
  quadratic matrix in ell-coefficients, the exact bridge identity det(E2) = 16·det Hess(F) holds
  as polynomials, with det E2(1,1,1,1) = −5808 = 16·(−363).
- (e) The previously admitted target partition [5,3,3,3,1,1] (sum 16) is impossible for this F in
  characteristic 0: it sums to 16 ≠ 19 = dim A, and a general ell has 9 Jordan blocks, not 6.
  Exhaustive exact scans (624-cell integer box in char 0; 80-cell scans in char 0/2/3/5) never
  produce it. The 6-part partition is exactly the conjugate of (1,4,6,4,1).
- (f) Characteristic sensitivity (same F): in char 2 and 3 the Hilbert function drops to
  (1,4,6,4,1) (dim 16), because the Fermat-tail second derivatives carry coefficient 12;
  80-cell Jordan censuses are recorded in the artifacts. The target partition occurs in none of
  the characteristics.

## Proof / evidence

All steps are exact integer/Fraction linear algebra on catalecticant matrices (differentiation of
one explicit quartic); no Gröbner bases, no floats.

1. **Hilbert function.** For each k = 0..4, the k-th catalecticant (operators R_k vs monomials
   S_{4−k}) has exact ranks 1,4,9,4,1. Compact certificates: in degree 2, Ann(F)_2 = span(x0²)
   (image table x0u→VW, x0v→UW, x0w→UV, uu→12U², uv→WX0, uw→VX0, vv→12V², vw→UX0, ww→12W²,
   x0²→0) and the complementary 9×9 minor has det −1728 ≠ 0; in degree 3 the pivot operator
   columns {x0uv,x0uw,x0vw,uvw} against rows {X0,U,V,W} give a 4×4 minor of det 1. Socle: every
   operator of degree 5,6 kills F, so socle degree is exactly 4 with socle value x0·u·v·w → 1.
2. **Quotient bases.** A0={1}; A1={x0,u,v,w}; A2={x0u,x0v,x0w,uu,uv,uw,vv,vw,ww};
   A3={x0uv,x0uw,x0vw,uvw}; A4={x0uvw} (RREF pivot sets of the catalecticants).
3. **Multiplication maps.** Coordinates in the quotient by exact projection (CPᵀCP)⁻¹CPᵀC·v.
   At ell=(1,1,1,1) the four maps have ranks 1,4,4,1 (all maximal): WLP. Composed maps give
   det(x_ell²:A1→A3) = −5808 ≠ 0 and x_ell⁴ = 96 ≠ 0: SLP. Maximal rank at one point implies the
   general-ell statement by Zariski-openness.
4. **Jordan type.** The 19×19 nilpotent N = x_ell has nullities [0,9,13,17,18,19,19,19], i.e.
   partition [5,3,3,3,1,1,1,1,1], the sorted conjugate of (1,4,9,4,1): the absolute maximal type,
   so attaining it at one point proves it is the general type. Stability: identical partition at
   (1,2,3,5), (0,1,1,1), (2,−1,3,1) and 560/624 cells of the {−2..2}⁴ box (drops only on
   coordinate/small-support loci). Certificates: min-poly t⁵ (rank N⁴=1, N⁵=0) with explicit
   nonzero chain 1→l→l²→l³→l⁴=96; A2 = im(A1)+ker(A2→A3) splitting via nonzero 9×9 det (−2904).
5. **Hessians.** Classical Hessian by direct differentiation; det factors as above (sympy
   factor_list singleton ⇒ irreducible Q). Mixed E2 determinant in the quotient bases satisfies
   the bridge identity term-by-term. The A1→A2 mixed matrix M1 (9×4, linear) has rank 4 at
   ell-sum with explicit nonzero 4×4 minors; its Gram determinant is an irreducible octic
   (value 135), the sum of squares of 90 biquadratic minors (Cauchy–Binet) — in particular not
   a monomial, which is why the preset fallback's monomial-factor demand fails.
6. **Target impossibility.** (i) sum = 16 ≠ 19; (ii) #blocks = dim ker N = 9 ≠ 6;
   (iii) exhaustive scans produce it nowhere, in any tested characteristic.

## Limitations

- Char-0 statements need 2,3 invertible where divisions by the recorded determinants occur
  (explicit values given).
- The Jordan claim is "general ell" (explicit dense census + named general point attaining the
  absolute maximal type, which rigorously implies generality); the drop locus is documented by
  cell counts but not classified as a variety.
- Hessian-factor irreducibility is a sympy factor_list computation over QQ.
- Char-2/3 census is a finite-box (80-cell) probe, honestly labeled.

## Reproducibility

- output/artifacts/emergent_audit.py → EMERGENT_AUDIT_OK (stdlib only, ~0.1 s): Hilbert,
  impossibility, WLP/SLP numbers, Jordan partition + conjugate check, Hessian evaluations.
- output/artifacts/verify_target_fast.py → VERIFY_OK: same checks, independent code path.
- output/artifacts/char_scan.py → VERIFY_OK (~5 s): char-0/2/3/5 Hilbert + 80-cell Jordan
  censuses, target-never-occurs.
- output/artifacts/jordan_chains.py → CHAINS_OK: explicit length-5 chain, min-poly data,
  A2 splitting det.
- output/artifacts/target_deepening.py → DEEPENING_OK: bases, socle cap, Perazzo shape,
  x^j table.

## References

- Miró-Roig, Pérez Díez, "Perazzo hypersurfaces and the weak Lefschetz property",
  arXiv:2402.09188 — settles P^{n+2}, flags P^{n+3} as non-generalizing.
- Costa, Gondim, "The Jordan type of graded Artinian Gorenstein algebras",
  arXiv:1811.02072 — mixed-Hessian-to-Jordan machine.
- Abdallah, Schenck, "Free resolutions and Lefschetz properties of some Artin Gorenstein rings
  of codimension four", arXiv:2208.01536 — records Gondim c=4 r≤4 WLP.
- Marques, Miró-Roig, Pérez, "Jordan type of full Perazzo algebras", arXiv:2506.23904 — full
  Perazzo only (n+1=10 for d=4,m=3), disjoint from single-leg n=0 F_named.
- Abdallah et al., "Hilbert functions and Jordan type of Perazzo Artinian algebras",
  arXiv:2303.16768 — binary-base Perazzo threefolds, disjoint family.
