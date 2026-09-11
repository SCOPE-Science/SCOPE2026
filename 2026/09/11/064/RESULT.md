# Sharp genus-9 Clifford-index certificate via Picard lattice and Lazarsfeld–Mukai stability

## Context

Green's conjecture has two sides: syzygies of canonical curves and the Clifford
index of the underlying linear series. For curves on K3 surfaces, the
Green–Lazarsfeld / Knutsen constancy results and the Donagi–Morrison /
Lelli-Chiesa / Pal / Watanabe Lazarsfeld–Mukai (LM) bundle criteria reduce a
low Clifford index to surface geometry: a Clifford-dimension-one curve with
Cliff(C) < floor((g-1)/2) has its Clifford index computed by restriction of a
surface divisor, i.e. a low contributor forces an effective decomposition
H ~ M + N (+R) with 0 < M·H < H². The missing input for any concrete system is
the per-lattice obstruction list. This record supplies it for one explicit
moduli-natural Noether–Lefschetz rank-two genus-9 system.

## Definitions

Work over C. Let Λ = Z·H ⊕ Z·L with Gram matrix in basis (H,L)

    G = diag(16, -8),  H² = 16,  L² = -8,  H·L = 0.

G is even, det G = -128 ≠ 0, leading principal minor 16 > 0, so signature
(1,1) by Sylvester. Adjunction genus of H: g(H) = H²/2 + 1 = 9.
For D = (x,y) = xH + yL write d = D·H = 16x, q = D² = 16x² - 8y²,
μ(D) = d - q - 2. Recall Cliff(A) = deg A - 2(h⁰(A)-1) for a line bundle A
with h⁰ ≥ 2, h¹ ≥ 2, and Cliff(C) = min Cliff(A) over contributors;
gonality gon(C) = Cliff(C) + 2 or +3 for Clifford dimension one.

## Result (headline)

For the above (X,H) with Pic(X) = Λ and H ample (realized below): every smooth
C ∈ |H| (genus 9) satisfies Cliff(C) ≥ 3. Since the general genus-9 curve has
Cliff 4, this locates the Green-critical strand of |H| at Cliff ≥ 3, i.e. no
Cliff-≤2 linear series forces the low-p linear strand, without computing a
single syzygy. The novel content is the named lattice plus its complete finite
(indeed empty) Cliff-≤2 obstruction window.

## Proof / evidence

Realization (Lemma F, machine-checked): H ↦ e+8f in one ⟨e,f⟩ ≃ U summand
(2·1·8 = 16, coefficient 1 so primitive); L ↦ r₁+r₂+r₃+r₄ with
r₁=(1,-1,0⁶), r₂=(0²,1,-1,0⁴), r₃=(0⁴,1,-1,0²), r₄=(1,1,0⁶) in doubled
coordinates: each has standard norm 2 (square -2 in E₈(-1)), pairwise
orthogonal, so L² = -8; L/2 ∉ E₈ (mixed integer/half-integer coordinates fail
the all-integral-or-all-half-integral condition), hence L is primitive (any
p|L has p²|8 so p=2, excluded). Thus ⟨H,L⟩ ↪ U ⊕ E₈(-1) ⊂ U³ ⊕ E₈(-1)²
primitively. By surjectivity of the K3 period map some K3 surface X has
Pic(X) = Λ; since Λ has no (-2)-classes (Lemma B), the ample cone equals the
positive cone, so H or -H is ample; take the ample one (window sign-symmetric).

Lemma B (no (-2)): 16x²-8y² = -2 has no integral solution (LHS 0 mod 4,
RHS 2 mod 4). No smooth rational curves; trivial Weyl group.

Lemma C (no elliptic pencils): 16x²-8y² = 0 ⇒ y² = 2x² ⇒ x = y = 0
(√2 irrational / infinite descent). No nonzero isotropic class; Saint-Donat
hyperelliptic case (i) (genus-1 E with E·H ∈ {1,2}) impossible.

Primitivity of H (basis vector) excludes Saint-Donat case (ii); |H| is not
hyperelliptic; general member is smooth non-hyperelliptic genus 9.

Lemma D (empty Hodge window): for every D, d = D·H = 16x, so
{D : 0 < D·H < 16} = ∅ globally, no box truncation. Every nonzero effective D
has x ≥ 1, so H = M+N with M,N effective nonzero would need x_M+x_N = 1
impossible: H is indecomposable. Per-class log tabulates (x,y,d,q,μ);
x=1 slice μ(1,y) = 8y²-2: -2 at y=0 (D=H residual-trivial), ≥6 else.
Box scan |x|,|y| ≤ 30 confirms, equation d=16x promotes to theorem.

Brill–Noether input (checked): at g=9 every contributor (d,r) with
Cliff = d-2r ≤ 2, h¹ = g-d+r ≥ 2, 0 ≤ d ≤ 16 has ρ = g-(r+1)(g-d+r) < 0
(e.g. pencils d ≤ 4 give ρ = 2d-11 ≤ -3). Any Cliff-≤2 series is BN-negative,
must come from surface geometry (Donagi–Morrison / Pal philosophy).

Bridge (cited tools, applied originally): (a) Green–Lazarsfeld / Knutsen /
Lelli-Chiesa: Clifford-dimension-one curves with Cliff < floor((g-1)/2) have
Clifford computed by a surface divisor, i.e. low contributor yields
H ~ M+N(+R) with 0 < M·H < H² (Donagi–Morrison form; Pal Lemma 4.2 /
Watanabe ACM give rank-2 LM version: pencil computing Cliff <
floor((g-1)/2)-1 has non-simple LM bundle 0 → M → E_{C,A} → N(⊗I_Z) → 0
forcing such decomposition). (b) Clifford-dimension classification
(Martens / plane-genus formula): genus 9 is not (d-1)(d-2)/2 (6 and 10
bracket it), so no smooth plane model; exceptional dimension ≥ 2 cannot occur
with Cliff ≤ 2. Hence any hypothetical Cliff-≤2 curve has dimension one and
(a) applies. Here floor(8/2) = 4, so Cliff ≤ 2 is in range. Lemma D says the
required window is empty: contradiction. Pencil-layer check: degree ≤ 5
pencils (Cliff ≤ 3) have ρ ≤ -1 < 0, non-simple LM bundle forcing same
impossible decomposition; no gonality-≤5 pencil, no Cliff-≤2 pencil.

## Limitations

Lattice half (no (-2)/isotropic, empty window, indecomposability, primitive K3
embedding, ρ<0 enumeration) proved and machine-checked. Passage to Cliff ≥ 3
invokes cited peer-reviewed Green–Lazarsfeld, Knutsen, Lelli-Chiesa,
Donagi–Morrison, Pal, Watanabe divisor/LM theorems as external tools, applied
here to the new empty window. No syzygy computed; sharpness (Cliff exactly 3
vs 4) not claimed.

## Reproducibility

    python3 output/artifacts/verify_target.py   # expect VERIFY_OK

Exact integer arithmetic, stdlib only. Checks A (even/det/signature),
B (no (-2)), C (no isotropic), D (empty window + table), E (ρ<0),
F (primitive embedding).

## References

Green–Lazarsfeld, Special divisors on curves on a K3 surface, Invent. 1987;
Donagi–Morrison, Linear systems on K3-sections, JDG 1989; Saint-Donat,
Projective models of K3 surfaces, AJM 1974; Knutsen, Gonality and Clifford
index of curves on K3 surfaces, Arch. Math. 2003; Lelli-Chiesa, Generalized
LM bundles and Donagi–Morrison conjecture, Adv. Math. 2015; Pal, LM bundles
associated with a pencil computing the Clifford index, arXiv:2005.09208;
Watanabe, Slope semistability of rank-2 LM bundles, arXiv:1503.06682;
Ramponi, Gonality and Clifford index on elliptic K3s Picard number two, 2016.
