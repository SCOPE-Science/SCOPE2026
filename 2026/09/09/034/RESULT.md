# 2-step nilpotent compatible Lie algebras in dimension 5 with joint centre dimension ≥ 2

## Context

A compatible Lie algebra is a vector space with two Lie brackets satisfying the
mixed Jacobi identity; such pairs govern bi-Hamiltonian structures, Poisson
pencils, and compatible deformations. Ladra–Leite da Cunha–Lopes extended the
Skjelbred–Sund central-extension method to this setting and closed the algebraic
classification up to dimension 4; the geometric classification also stops at
(complex) dimension 4. Dimension 5 is the next open boundary. The full
dimension-5 census (including the k=1 stratum and nilpotency class ≥ 3) remains
open; the result below closes exactly the 2-step, centre ≥ 2 stratum.

## Definitions

- Base field F: algebraically closed, char F ≠ 2.
- Compatible Lie algebra: (V, [·,·]₁, [·,·]₂), each bracket Lie, with
  cyclic_{x,y,z} ([[x,y]₁,z]₂ + [[x,y]₂,z]₁) = 0 (mixed Jacobi).
- 2-step: every triple product [[·,·]_a,·]_b = 0 for a,b ∈ {1,2}.
  Then Jacobi and mixed Jacobi hold automatically.
- Joint centre Z(V) = {x : [x,V]₁ = 0 = [x,V]₂}; k = dim Z(V).
- Derived algebra D = [V,V]₁ + [V,V]₂ ⊆ Z(V) in the 2-step case.
- Q = V/Z(V); ordered bracket pairs throughout (no bracket-swap quotient).

## Result

Let F be algebraically closed with char F ≠ 2. Let (V,[·,·]₁,[·,·]₂) be 2-step
nilpotent compatible of dimension 5 with k = dim Z(V) ≥ 2. Then k ∈ {2,3,5};
k = 4 is impossible; k = 5 is the abelian algebra alone. Up to ordered-pair
isomorphism:

- k = 3 (Q dim 2; ([x,y]₁,[x,y]₂) = (v₁,v₂) ∈ F³⊕F³):
  - F-family over P¹: F_[a:b] = (a·e₁, b·e₁), i.e. [x,y]₁ = a·f₁,
    [x,y]₂ = b·f₁; distinct points are non-isomorphic as ordered pairs;
    derived dim 1.
  - Discrete H = (e₁,e₂): [x,y]₁ = f₁, [x,y]₂ = f₂; derived dim 2.
- k = 2 (Q dim 3, Z = F²; brackets = 2×3 pencil P(s,t) = sΦ₁+tΦ₂, columns on
  e₁₂,e₁₃,e₂₃ in basis d₁,d₂ of Z): classes biject with Kronecker
  strict-equivalence classes of faithful pencils (common right kernel dim ≤ 1):
  - Discrete L₂: [[s,t,0],[0,s,t]] (Kronecker L₂ block).
  - Discrete M: [[s,t,0],[0,0,0]] (L₁ ⊕ zero block); derived dim 1.
  - K-family over P¹: K(λ) = L₁ ⊕ J₁(λ), e.g. K(0) = [[s,t,0],[0,0,s]].
  - J-family over P¹: J(μ) = J₂(μ) ⊕ L₀, e.g. J(0) = [[s,t,0],[0,s,0]]
    (includes N₂⊕L₀ at ∞).
  - E-family over Sym²P¹ ≅ P²: E({λ₁,λ₂}) = diag(s−λ₁t,s−λ₂t) ⊕ 0-column,
    e.g. E({0,∞}) = [[s,0,0],[0,t,0]]; scalar points E({λ,λ}) included.
  - All non-M members have derived dim 2 and joint centre dim 2.
- Separation: by k; F vs H and M vs rest by derived dim; L₂/K/J/E by 2×2-minor
  gcd degree and minimal P¹-rank (L₂: gcd 1, rank always 2; K: linear gcd,
  min-rank 1; J: squared-linear gcd, min-rank 1; E-distinct: split quadratic
  gcd with two rank-1 points; E-scalar: squared gcd, min-rank 0); within
  families by eigenvalue/root multiset of the minor gcd (standard Kronecker
  uniqueness).

## Proof / evidence

Central-extension reduction: 2-step ⇒ triple products vanish; D ⊆ Z; Q is
abelian; with B² = 0, H²_comp = pairs Alt²(Q,Z); shear automorphisms Hom(Q,Z)
act trivially, so Aut-orbits = GL(Q)×GL(Z)-orbits on cocycle pairs.
Centre lemma: dim Q = 1 forces both brackets zero (abelian, k = 5); hence
k ∈ {1,2,3,5} and k = 4 is impossible.
k = 3: Alt²Q is 1-dimensional with det-scale; rank 0 = abelian, rank 1 = line
in F³ plus invariant ratio [a:b] ∈ P¹ (isomorphisms preserve each bracket
separately and scale both sides equally), rank 2 = single orbit H by GL₃
transitivity on 2-planes.
k = 2: the right column action via ∧²: GL₃ → GL₃ is onto, since
∧²S = det(S)(S⁻¹)ᵀ gives ∧²(SL₃) = SL₃ (inverse-transpose automorphism,
char ≠ 2) and scalars dI = ∧²(√d·I) exist as F is algebraically closed; hence
orbits = Kronecker strict-equivalence classes. Faithful ⟺ common right kernel
dim ≤ 1 (a 2-plane in ∧²Q is q∧Q, so dim ≥ 2 centralises a Q-lift).
Kronecker's theorem for 2×3 pencils (Gantmacher Vol. 2, Ch. XII) then yields
exactly L₂; L₁⊕J₁; M = L₁⊕[0]; J₂⊕L₀; regular-diagonal⊕L₀ = E; J₁⊕N₁⊕L₀ and
N₁⊕N₁⊕L₀ are the E-points {λ,∞}, {∞,∞}; L₁ᵀ⊕L₀⊕L₀ and the zero pencil are
unfaithful (k = 3 stratum). Invariants above separate all cases.
Machine certificate: output/artifacts/laws.json holds integer structure
constants (abelian; F-samples F₀,F₁,F₂,G₀=[0:1]; H; L₂; M; K₀,K₁,K_inf;
J,J₁,J_inf; E-samples D=E({0,∞}), E₁=E({1,1}), R₀=E({∞,∞}), R₁=E({−1,−1}),
R_inf=E({0,0})); output/artifacts/verify.py (stdlib only) checks skew,
all-triple-vanishing, joint-centre/derived dims, minor-gcd types, and a
random-pencil spot check → VERIFY_OK. Independently re-executed and
recomputed from scratch during audit.

## Limitations

- Only 2-step algebras with joint centre dim ≥ 2 (strata k = 3, k = 2) plus
  abelian. The k = 1 stratum (4×4 skew pencils, wild moduli) is NOT covered.
- Nilpotency class ≥ 3 (non-2-step) in dimension 5 is NOT covered.
- Ordered bracket pairs; unordered (swap-permitting) identification not
  quotiented.
- Field hypotheses essential: algebraically closed (eigenvalues,
  ∧²-surjectivity) and char ≠ 2.

## Reproducibility

Run `python3 output/artifacts/verify.py` (stdlib only) → expect VERIFY_OK
(all entries pass skew, triple-vanishing, centre/derived dims, minor-gcd
spot checks).

## References

- M. Ladra, B. Leite da Cunha, S. A. Lopes, A classification of nilpotent
  compatible Lie algebras, arXiv:2406.04036 (algebraic, to dim 4).
- K. Abdurasulov, A. Khudoyberdiyev, F. Toshtemirova, The geometric
  classification of nilpotent Lie-Yamaguti, Bol and compatible Lie algebras,
  arXiv:2506.05353 (geometric, complex dim 4).
- F. R. Gantmacher, The Theory of Matrices, Vol. 2, Ch. XII (Kronecker
  pencils; completeness authority for the 2×3 case).
