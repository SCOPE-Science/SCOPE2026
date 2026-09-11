# First coexact Hodge 1-form eigenvalue of the Berger lens space (L(3,1), g_{1/2})

## Context

Exact Hodge–Laplace spectra under Riemannian collapse and inverse-spectral
determination of spherical space forms are recognized open directions.
Henkel–Lauret (arXiv:2605.05406, 2026) settled the full 1-form spectrum,
first-eigenvalue formula, and inverse result for left-invariant metrics on
SU(2) ≅ S³ and SO(3) ≅ RP³ only. Round-lens p-spectra (Lauret 2018) cover
constant-curvature quotients only, with no Berger fiber-scaling parameter.
Collapsing theory gives vanishing criteria or inequalities, not exact
Berger-lens values. The Hopf-Berger lens quotient L(3,1), where S³
eigenspaces need not descend intact, was open at this level.

## Definitions

- `L(3,1) = S³ / Z_3`: lens space with deck generator `diag(w,w̄) =
  exp(2π E_1/3) ∈ SU(2)`, `w = e^{2πi/3}`, acting by left multiplication.
- `S³ ≅ SU(2)` with Lie basis `E_1,E_2,E_3`, `[E_1,E_2] = 2E_3` (cyclic),
  orthonormal for `⟨X,Y⟩_0 = -½tr(XY)`.
- Berger metric `g_{(a,b,b)}`, `a,b > 0`: left-invariant metric with
  orthonormal frame `X_1 = aE_1, X_2 = bE_2, X_3 = bE_3`. Fiber-scale
  parameter `ε = b/a`; `ε = 1/2` is `(a,b) = (2,1)`.
- The `Z_3` action is a free isometry of every left-invariant metric, so
  `(S³,g_{(a,b,b)}) → (L(3,1),g_{(a,b,b)})` is a Riemannian covering and
  `Spec(Δ_1^{L(3,1)}) ⊆ Spec(Δ_1^{S³})` via pullback with the same
  eigenvalues. `H¹(L(3,1);R) = H¹(S³;R) = 0` (finite fundamental group),
  so there are no nonzero harmonic 1-forms.
- `λ_1^1` denotes the first nonzero (hence coexact) Hodge 1-form eigenvalue.

## Result

Let `(L(3,1), g_{1/2})` be the Berger lens space with Hopf fiber scaled
`ε = 1/2`. Then the first coexact Hodge 1-form eigenvalue is exactly

```
λ_1^1(g_{1/2}) = 1,
```

attained by the descended `Z_3`-invariant Hopf-vertical 1-form of
eigenvalue `4ε²`, and no nonzero invariant coexact 1-form has smaller
eigenvalue.

## Proof / Evidence

1. **Vertical eigenpair (value 1).** Maurer–Cartan `dE_1* = -2E_2*∧E_3*`
   (cyclic) with `X_1* = E_1*/a`, etc., gives
   `dX_1* = -(2b²/a) X_2*∧X_3*`. Since `d(X_2*∧X_3*) = 0` (repeated factor),
   `X_1*` is coclosed (`δX_1* = 0`); with `b_1 = 0` and `dX_1* ≠ 0` it is
   coexact. `dX_1*` is a constant multiple of the orthonormal 2-form
   `X_2*∧X_3*`, so `Δ_1 X_1* = (2b²/a)² X_1*`. At `(a,b) = (2,1)`,
   `dX_1* = -X_2*∧X_3*` and `Δ_1 X_1* = 1·X_1* = 4ε² X_1*`. `X_1*` is
   left-invariant hence `Z_3`-invariant, so it descends to `L(3,1)`.

2. **Lower bound (no eigenvalue below 1).** Use the Henkel–Lauret full
   Berger-sphere spectrum (Thm 4.1, Cor 4.2–4.4): nonzero `Δ_1`
   eigenvalues on `(SU(2), g_{(a,b,b)})` are `ν_{k,j} =
   a²(k-2j)² + b²((4j+2)k - 4j²)` (`0 ≤ j ≤ k`, exact/function branch),
   `μ_{k,-1} = (k+2)²a²`, `μ_{k,0} = k²a² + 4kb² + 4b⁴/a²`, and
   `μ_{k,j}^± = (√(ν_{k,j}+κ) ± √κ)²` with `κ = b⁴/a²`, valid only for
   `k ≥ 2, 1 ≤ j ≤ k-1`. At `(2,1)` (`κ = 1/4`): exact branch
   `ν_{k,j} = 2k + 4(k²-3kj+3j²) ≥ 2k`, census `k ≤ 8` minimum `6` at
   `(1,0)`, tail `≥ 18`; `μ_{k,-1} = 4(k+2)² ≥ 16`;
   `μ_{k,0} = 4k²+4k+1` minimum `1` at `k = 0` (the vertical mode);
   `μ^+ ≥ 4κ = 1`; valid pm-modes have `ν ≥ 8` (census min `8` at
   `(2,1)`, tail `≥ 18`) so
   `μ^- ≥ (√(8+1/4)-√(1/4))² = (17-√33)/2 > 5.5 > 1`.
   Every nonzero cover eigenvalue is therefore `≥ 1`, with equality only
   for the vertical mode. The quotient spectrum being a subset and
   `b_1(L(3,1)) = 0` gives the same lower bound on the quotient.

3. **Conclusion.** The descended vertical form attains `1` and nothing is
   below `1`, so `λ_1^1 = 1` on `(L(3,1), g_{1/2})`.

## Limitations

- Proves only the single-point exact value at `ε = 1/2`, not the full
  `ε_c` crossover. The cover-level crossing competitor `ν_{1,0}` is not
  `Z_3`-invariant (`k = 1` weights `{±1}` contain no multiple of 3), so
  the single-switch crossover as originally stated is blocked; only the
  preset-fallback point claim is made here.
- The lower bound uses the published Henkel–Lauret Berger-S³ spectrum
  formulas as a black-box lemma plus the elementary covering-subset fact.
- Branch attribution (exact vs coexact) is not needed at this point since
  even the exact-branch minimum (6) exceeds 1.

## Reproducibility

`output/artifacts/verify_fallback.py` replays the frame eigenpair, the
exact-rational census for `k ≤ 8`, certified tail bounds, and the `k = 1`
weight check, printing `VERIFY_OK` (auditor re-executed).

## References

- J. Henkel, E. A. Lauret, Hodge Laplacian on 1-forms of homogeneous
  3-spheres, arXiv:2605.05406 (2026). — full Berger S³/SO(3) spectrum,
  Thm 4.1 / Cor 4.2–4.4; SU(2)/SO(3)-only.
- E. A. Lauret, The spectrum on p-forms of a lens space,
  Geom. Dedicata 197 (2018), 107–122; arXiv:1604.02471. — round-lens
  p-spectrum only, no Berger deformation.
- A. Podobryaev, Cut loci and diameters of the Berger lens spaces,
  arXiv:2603.27769. — Berger-lens metric geometry, no Hodge spectrum.
- B. Shatto, Coexact Spectral Gaps of Flat Bundles on Spherical Space
  Forms and the Mckay Distance (2026). — round-metric gaps only.
