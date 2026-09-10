# Degree-≤4 dominant-arc exclusion for the fixed mixed cell X (preset fallback)

## Context
Target: uniform log-power Pila–Wilkie bound N(X^{trans},T) ≤ C(log(T+2))^κ with
explicit κ (e.g. ≤ 8) for one fixed mixed exponential–elliptic definable set,
via one cell count plus one mixed Ax–Schanuel step. The full counting exponent
is not closed here. This record is the admitted preset fallback: the
algebraic-locus lemma for the same fixed X, reusable by any later counting
attempt.

## Definitions (all fixed before counting)
- E0: Y² = X³ − 2 over Q. In Weierstrass normal form (X,Y) = (x,2y):
  Y² = 4x³ − 8, i.e. g2 = 0, g3 = 8.
- Λ = period lattice of E0; F0 = {a·w1 + b·w2 : |a|,|b| ≤ 1/2} a fixed closed
  fundamental parallelogram.
- Identify C ≅ R² by the fixed R-linear map z = u + iv.
- ℘ = Weierstrass x-coordinate for (C/Λ, 0); (℘′)² = 4℘³ − 8.
  ℘-tilde(u,v) = Re/Im pair of ℘|Int(F0) where defined.
- P0(x) = x² + 1; E(x) = exp(x) + P0(x) on I = (−1,1).
- X = {(x,u,v) ∈ I × Int(F0) : E(x) − Re(℘)(u,v) = 0 AND Im(℘)(u,v) = 0},
  i.e. X = {(x,z) ∈ I × Int(F0) : E(x) − ℘(z) = 0}.
- "Degree ≤ 4" = total degree of Zariski closure in A³_{(x,u,v)} ≤ 4.
  "Dominant onto (−1,1)" = projection x|Γ nonconstant (infinite image).

## Result
X contains NO irreducible real-algebraic curve Γ of total degree ≤ 4
projecting dominantly onto (−1,1). Equivalently every irreducible
real-algebraic curve of degree ≤ 4 in X lies in a fiber {x = const} or
projects non-dominantly onto the elliptic-log factor. In fact the proof never
uses the degree bound, so the exclusion holds at every degree. The
alternative success branch (explicit certified degree-≤4 dominant witness) is
therefore empty.

## Proof / evidence
- Lemma 1 (script-certified enclosures, certify_ranges.py → CERT_RANGES_OK):
  E′(x) = eˣ + 2x strictly increasing (E″ ≥ 2) with unique zero
  xc ∈ [−0.351733711249, −0.351733711249]; E(I) ⊂ [1.8271840251, 4.7182815576]
  ⊂ (−∞, 5); slope margins |E′| ≥ 0.134/0.136 off a 0.05-neighbourhood of xc;
  on X, ℘(z) = E(x) real in that interval so |℘′| ≤ 20.70 via
  |℘′|² = |4w³ − 8|. Pole gap: ℘(z) → ∞ as z → 0, and E is bounded, so X
  avoids 0 < |z| < ρ for some ρ > 0 and ℘ is holomorphic near X. X avoids the
  critical locus {℘′ = 0}: ℘′ = 0 forces ℘ ∈ {e_i}, e_i³ = 2 (e1 = 2^{1/3} ≈
  1.26, others nonreal), disjoint from E(I).
- Lemma 2 (constant cases, elementary + verify_b2_algebra.py → VERIFY_B2_OK):
  for Γ ⊂ X dominant, complexify and take a germ x(s), z(s) algebraic over
  C(s) with exp(x(s)) + x(s)² + 1 − ℘(z(s)) = 0. x ≡ c contradicts dominance.
  z ≡ z0 with x nonconstant gives e^{x(s)} = R(x(s)) = −x(s)² + c; differentiating
  and cancelling x′ (not ≡ 0) gives e^{x(s)} = R′(x(s)) = −2x(s), so x(s) takes
  values among the ≤ 2 roots of the fixed nonzero quadratic X² − 2X − c = 0,
  hence is constant — contradiction.
- Lemma 3 (both-nonconstant case, upper bound + cited black box): with
  M = C(x(s),z(s)) (trdeg ≤ 1), eˣ ∈ M(℘(z)) and ℘′(z) algebraic over M(℘(z)),
  so L = C(x,z,eˣ,℘(z),℘′(z)) has trdeg ≤ 2. Translating to vanishing germs
  (X,Z) preserves trdeg (e^X = e^{−x(s0)}eˣ; ℘(z(s)) ∈ C0(℘(Z),℘′(Z)) by the
  Weierstrass addition formula). Cited one-parameter mixed Ax–Schanuel for
  Gm × E0 (Ax/Bertrand/Kirby; Gao arXiv:1806.01408) gives trdeg ≥ dim + 1 = 3
  since Hom(Gm,E0) = 0 makes analytic subgroups products and the germ lies in
  no proper one. 2 ≥ 3 is absurd.
- Theorem: dominance gives an infinite arc with nonconstant x; Lemmas 2–3
  exclude constant-z and both-nonconstant cases. Degree ≤ 4 never used.

## Limitations
- Full target N(X^{trans},T) ≤ C(log(T+2))^κ with κ ≤ 8 NOT claimed.
- Relies on cited one-parameter mixed Ax–Schanuel black box (not re-proved).
- Lemma 1(f) smooth-point/nonemptiness half-neighbourhood phrasing has a
  boundary nuance if the lift of 2 lies on ∂F0; inessential to the exclusion.
- Interval script uses float exp with explicit padding; margins exceed padding
  by orders of magnitude.

## Reproducibility
- python3 output/artifacts/certify_ranges.py → CERT_RANGES_OK
- python3 output/artifacts/verify_b2_algebra.py → VERIFY_B2_OK
- Stdlib only, seconds.

## References
- Z. Gao, Mixed Ax–Schanuel for the universal abelian varieties
  (arXiv:1806.01408) — cited general black box.
- Ax (1971) / Bertrand / Kirby — semiabelian Ax–Schanuel background.
- Binyamini–Novikov–Zak, Annals 2024 — general polylog existence (no locus).
- J. Pila, Ann. Inst. Fourier 2010 — different surface log x log y = log z.
- Masser–Zannier; Habegger–Pila; Pila–Tsimerman (Duke 2016, j-function) —
  pure-family inputs, disjoint from this fixed mixed equation.
- Jones–Schmidt — Pfaffian format for restricted ℘ (definability context).
