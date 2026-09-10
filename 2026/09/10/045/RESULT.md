# G = SL₂(ℂ) for the deformed-Airy operator L₁: y″ − (z + 1/z)y = 0, with slope-at-0 correction

## Context

Let L₁ be y″ − r(z)y = 0 with r(z) = z + 1/z = (z²+1)/z over ℂ(z), viewed as the
trace-free rank-2 meromorphic connection D = d − A dz, A = [[0,1],[r,0]], on ℙ¹.
Let G be its Picard–Vessiot differential Galois group over ℂ(z).
The target investigation concerned the SL₂-vs-reduction decision for this cell,
whose topic premise listed Katz slopes (3/2 at ∞, 1/2 at 0) and a witness clause
requiring Stokes matrices at both infinity and zero.

## Definitions

- Kovacic classes for y″ = ry over ℂ(z) (char. 0): (1) reducible (Borel) ⟺
  Riccati u′ + u² = r has a rational solution; (2) irreducible imprimitive
  (dihedral) ⟺ (given Case 1 out) the symmetric square w‴ − 4rw′ − 2r′w = 0 has
  a nonzero rational solution; (3) finite primitive; (4) G = SL₂.
- Katz slope 0 = regular singular; Stokes matrices exist only at irregular
  singularities.

## Result

**Theorem.** The differential Galois group of L₁ over ℂ(z) is G = SL₂(ℂ).

**Premise correction (proved).** z = 0 is a *regular* singular point of L₁
(Katz slope 0; resonant exponents {0,1} with a logarithmic second solution),
not a slope-1/2 irregular point. Hence there are no Stokes matrices at 0, and
the topic's literal witness clause "Stokes matrices at infinity and zero" is
unsatisfiable as written. The group decision is unaffected: the only irregular
singularity is ∞ (Airy-type, slope 3/2).

## Proof / evidence

G ⊆ SL₂(ℂ): no y′ term, so the Wronskian W satisfies W′ = 0 and G preserves the
alternating form.

Singularities (exact). r has the single finite pole z = 0, simple
(ord₀ r = −1); zeros at ±i are ordinary points. At 0, z²r = z³ + z is analytic,
so 0 is regular singular with indicial equation ρ(ρ−1) = 0, exponents {0,1}
(resonant). Frobenius recursion (n+ρ)(n+ρ−1)aₙ = aₙ₋₁ + aₙ₋₃ gives for ρ = 1:
a₁ = 1/2, a₂ = 1/12 (analytic solution exists); for ρ = 0 the n = 1 equation
reads 0·a₁ = a₀ = 1, impossible — the second local solution contains log z.
At ∞ (w = 1/z): w⁻⁴r(1/w) = w⁻⁵ + w⁻³ has pole order 5 > 2, so ∞ is irregular
with Katz slope 3/2. Formal Riccati ansatz
u = εz^{1/2} + c₀ + c₁z^{−1/2} + c₂z^{−1} + c₃z^{−3/2} + c₄z^{−2} + …
in u′ + u² = z + z⁻¹ yields c₀ = 0, c₁ = 0, c₂ = −1/4 (prefactor z^{−1/4}),
c₃ = ε/2, c₄ = 0; exponential parts q± = ±(2/3)z^{3/2}.

Kovacic elimination (exact):
- Case 1 (reducible): deg r = 1, v∞(r) = −1. For u ∼ azᵉ: e > 1 gives
  v∞(u′+u²) = −2e ≤ −4; e = 1 gives u² ∼ a²z² dominant (no cancellation);
  e = 0 gives limit a² ≠ 0 (valuation 0); e < 0 gives valuation ≥ 2. Never −1
  over all integer e. No rational Riccati solution; not reducible.
- Case 2 (dihedral): for w ∼ azᵉ the symmetric-square leading zᵉ coefficient
  is −2a(2e+1) (w‴ is O(z^{e−3}), subdominant); 2e+1 is odd for every integer e,
  never 0. No nonzero rational w; not dihedral.
- Case 3 (finite): a finite Picard–Vessiot group has only algebraic solutions
  hence moderate growth everywhere, so every singularity is regular singular.
  But ∞ is irregular. Contradiction; G infinite; not finite.

With G ⊆ SL₂(ℂ) and all proper Kovacic classes excluded, G = SL₂(ℂ). ∎

Stokes corollary (no new computation): by the Ramis density theorem, the Stokes
matrices at ∞ together with formal monodromy and exponential torus generate a
Zariski-dense subgroup of SL₂ — the formal data alone (diagonal torus plus
sheet-exchanging formal monodromy, inside a solvable group) cannot generate
SL₂, so wild monodromy at ∞ is nontrivial. Exact multiplier values s± are not
computed.

## Limitations

- Exact Stokes multipliers s± at ∞ are not computed; only joint nontriviality
  follows as a corollary.
- Formal monodromy stated in one fixed ordered formal basis with
  sheet-exchange convention; sector/branch conventions for any future
  multiplier log are not fixed here.
- Kovacic classification, Riccati/symmetric-square criteria, Ramis density,
  and the finite-group regularity criterion are cited as standard theory.

## Reproducibility

`python3 output/artifacts/verify_kovacic.py` (stdlib only, exact rationals)
prints VERIFY_OK with 49 checks: census, Frobenius coefficients and the ρ = 0
obstruction, Riccati valuation table, symmetric-square leading coefficients,
pole order at ∞, and formal recursion coefficients.

## References

- M. F. Singer, Introduction to the Galois Theory of Linear Differential
  Equations, arXiv:0712.4124.
- M. van der Put, M. F. Singer, Galois Theory of Linear Differential
  Equations (book): Kovacic classification and algorithmic background.
- N. Katz single-slope rigidity, arXiv:2309.11742 (inapplicable: this cell is
  non-rigid, irregular at ∞ plus regular-singular at 0).
- Horrobin–Mazzocco, Stokes phenomenon in Gauss-to-Kummer confluence,
  arXiv:2009.07607 (different cell, slope 1).
- Classical Airy t = 0 tables (DLMF/nLab/Sibuya): different global connection
  (no singularity at 0 for t = 0), no transfer to t = 1.
