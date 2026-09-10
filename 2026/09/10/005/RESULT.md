# Critical-manifold certificate lemma for the doubly-wound C^3 worm W_{4π}

## Context

The Diederich–Fornaess (DF) index program asks for quantitative
pseudoconvex exhaustion exponents. In ℂ², Liu (arXiv:1701.00293, Thm 3.4)
computed the exact index π/(2β) for the β-worm via a scalar Riccati
comparison on a Levi-flat annulus germ. For higher-dimensional (ℂ³/ℂⁿ)
worms, Barrett–Sahutoglu (arXiv:1007.5513) and Krantz–Peloso–Stoppato
(arXiv:2406.04905, single product twist log|z₂z₃|²) prove only
qualitative Bergman/Sobolev irregularity and Nebenhülle; no DF-index
number, no Levi-critical table, and no boundary psi-system were recorded.
The present certificate fixes the exact critical geometry and the PDE
input for one explicit doubly-wound ℂ³ worm, proving it is not
slice-reducible to ℂ². It does not prove any DF-index bound.

## Definitions

Work in ℂ³ with coordinates (z₁, z₂, w = z₃), w ≠ 0.
Put t = log|w|² ∈ ℝ, β = 4π, L = β − π/2 = 7π/2, and

- φ(t) = 0 for |t| ≤ L; φ(t) = exp(s − 1/s), s = |t| − L, for |t| > L,
- a(t) = e^{it}, b(t) = e^{2it},
- ρ(z₁,z₂,w) = |z₁ − a|² + |z₂ − z₁b|² + φ(t) − 1, W = {ρ < 0},
- M = {(0,0,w) : |t| ≤ L}, p₀ = (0,0,1).

φ is smooth on ℝ with all derivatives vanishing at |t| = L;
φ⁻¹(0) = [−L, L]. Let N₀ = −a ∂/∂z₁ (unit (1,0) normal on M),
X₂ = ∂/∂z₂, X₁ = ∂/∂w.

## Result

Along M ⊂ bW:

(a) M ⊂ {ρ = 0} with complex gradient (−ā, 0, 0) ≠ 0, so M lies in the
smooth boundary. The closed-form Levi matrix is

L(ρ)|_M = [[2, −b, iā/w̄], [−b̄, 1, 0], [−ia/w, 0, 0]].

The complex tangent is {X_{z₁} = 0}; in the tangential frame {X₂, X₁}
the restricted Levi form is diag(1, 0): eigenvalue 1 transverse (fiber),
eigenvalue 0 with explicit kernel field X₁ = ∂/∂w (twist-degenerate
direction).

(b) The center map t ↦ (e^{it}, e^{2it}) has winding rate pair exactly
(1, 2): (1/2L)∫_{−L}^{L} a′/a dt = i, (1/2L)∫ b′/b dt = 2i
(total phases 7π and 14π).

(c) In the Liu-pattern (ρ̃ = ρe^ψ) boundary setup, the transverse
couplings at the unit normal N₀ are exactly

c₁ = Hess_ρ(N₀, X₁) = −i/w̄, |c₁| = e^{−t/2} > 0,
c₂ = Hess_ρ(N₀, X₂) = ab = e^{3it}, |c₂| ≡ 1,

so c₁c̄₂ ≠ 0 everywhere on M. The two tangential boundary inequalities
form a genuinely coupled 2×2 system (joint discriminant on
span{X₁, X₂, N₀} carries the nonzero cross term); setting the coupling
to zero would be required to recover scalar Liu-type Riccati
inequalities, which is impossible since |c₂| ≡ 1.

## Proof / evidence

(i) On M: |z₁−a|² = 1, |z₂−z₁b|² = 0, φ = 0, so ρ = 0. Near interior
points of M, ρ = |z₁−a|² + |z₂−z₁b|² − 1; ∂ρ/∂z₁ = (z̄₁−ā) −
b̄(z̄₂−z̄₁b̄) gives ρ₁ = −ā; ρ₂ = 0; ∂ρ/∂w carries only factors
z₁, z̄₁, z₂, z̄₂, φ′(t), hence ρ₃ = 0 on M.

(ii) Entrywise: L₁₁ = 1 + |b|² = 2, L₂₂ = 1, L₁₂ = −b,
L₁₃ = iā/w̄ (from ∂ā̄/∂w̄ = −iā/w̄), L₂₃ = 0, L₃₃ = 0
(every w-derivative brings a vanishing fiber factor; d(aā) = 0).
Tangentiality X·∇ρ = 0 reads X_{z₁} = 0, satisfied by X₁, X₂;
restricted block [[L₂₂, L₂₃],[L₃₂, L₃₃]] = diag(1,0).

(iii) a′/a = i, b′/b = 2i give the normalized integrals by direct
integration.

(iv) c₁ = −aL₁₃ = −iaā/w̄ = −i/w̄; c₂ = −aL₁₂ = ab = e^{3it};
moduli and nonvanishing as stated (w ≠ 0 on M).

Replay: `python3 output/artifacts/verify_certificate.py`
(stdlib only) — 57 PASS, 0 FAIL, ALL VERIFY_OK:
(i) ρ(0,0,w) = 0 substitution + gradient; (ii) analytic Levi vs central
finite differences (maxerr < 6e−7, 8 points) + restricted block diag(1,0)
+ X₁ tangential kernel; (iii) circular-increment quadrature I₁ = 1,
I₂ = 2 to 1e−9; (iv) exact complex equalities c₁ = −i/w̄, c₂ = ab at
12 (t₀, θ) points plus off-diagonal nonzero.

## Limitations

- The DF-index bound η(W_{4π}) ≤ 1/2 is NOT proved: no Riccati comparison
inequality, no multitype/ε/s₀ datum is logged.
- Pseudoconvexity off M and global smooth boundedness of W are audit
steps, explicitly excluded from this certificate.
- A formal shadow-ODE threshold is uncertified conjecture only.
- "Bidegree (1,2)" is the normalized winding-rate meaning over the open
t-interval (phases 7π/14π), not a closed-loop integer invariant.
- Part (c) certifies the coefficient pair and the Liu-pattern template,
not an existence/well-posedness theory for ψ.

## Reproducibility

Frozen data: β = 4π, L = 7π/2, φ, ρ, M as above.
Single artifact `output/artifacts/verify_certificate.py` (stdlib only).

## References

- B. Liu, The Diederich-Fornaess index I: for domains of non-trivial
index, arXiv:1701.00293.
- D. Barrett, S. Sahutoglu, Irregularity of the Bergman projection on
worm domains in ℂⁿ, arXiv:1007.5513.
- S. G. Krantz, M. M. Peloso, C. Stoppato, On a higher-dimensional worm
domain and its geometric properties, arXiv:2406.04905.
- J. Yum, On the Steinness index, arXiv:1804.04304.
