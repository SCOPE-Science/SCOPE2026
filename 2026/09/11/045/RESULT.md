# Certified indefinite nested ghost blocking the linearized monotonicity test

## Context

Linearized monotonicity tests are fast, widely used inclusion detectors in
electrical impedance tomography (EIT). Abstract theory (Harrach; Garde–Staboulis;
Candiani–Dardé–Garde–Hyvönen) extends monotonicity reconstruction to indefinite
(sign-changing) and even extreme inclusions, but no prior work logs a fixed,
replayable geometry where the linearized test provably goes blind. This record
certifies one such obstruction: a nested-square ghost pair whose 16-cell
linearized verdicts coincide while the nonlinear data remain separated.

## Definitions

- Domain: `Ω = B_1` (unit disk).
- Fixed squares: `S = (-0.4,0.4)^2`, `K = (-0.2,0.2)^2`.
- Conductivities:
  - `σ_A = 1 + 2·1_S` (value 3 on `S`, 1 elsewhere);
  - `σ_B = 1 + 2·1_{S\K} − 0.5·1_K` (value 3 on `S\K`, value 0.5 on `K`, 1 elsewhere).
- Test family `F`: 16 dyadic squares tiling `[-0.8,0.8]^2` (side 0.4).
- Test level: `α = 1.5`.
- For `X ∈ {A,B}`, `C ∈ F`, in the 16-mode (`k = 1..8` Fourier cos/sin)
  Neumann-to-Dirichlet (NtD) Galerkin basis:
  `M_X(C) = Λ(σ_X) − Λ_0 − α·DΛ_0(1_C)`,
  where `Λ` is the NtD map, `Λ_0` the background (`σ ≡ 1`) NtD map, and
  `DΛ_0(1_C) = −∫_C ∇u^0_m · ∇u^0_n` the Fréchet derivative at background.
- Linearized verdict per cell: sign of `min spec M_X(C)`
  (nonnegative = inclusion detected in `C`; negative = not detected).

## Result

For every `C ∈ F`, the smallest eigenvalues of `M_A(C)` and `M_B(C)` agree in
sign (both negative) with certified margin, so the linearized test at `α = 1.5`
reconstructs the identical (empty) pixel image for two distinct conductivities,
while the nonlinear NtD gap satisfies `‖Λ(σ_A) − Λ(σ_B)‖_2 ≥ 0.02`:

- Fine-mesh (`N_r,N_t = 64,224`) minima group by cell position:
  corner cells `(−0.15188, −0.10379)`, edge cells `(−0.13596, −0.08937)`,
  central cells `(−0.11859, −0.06864)` (pairs `(minA, minB)`).
- Full 16-row table in `output/artifacts/ledger_final.json`.
- Per-cell error bar (fine-vs-mid mesh discrepancy + symmetric eigen-residual)
  `≤ 7.6×10⁻⁴ < 10⁻³` tolerance; `|λ_min| ≥ 0.068` on both sides, i.e. margin
  exceeds `bar + TOL` by ~40×: 16/16 CERT.
- Nonlinear gap `‖Λ_A − Λ_B‖_2 = 0.05329 / 0.05375 / 0.05392` across the three
  meshes (`32×128 / 48×176 / 64×224`), monotone convergent, all `≥ 0.02`.

Mechanism: at `α = 1.5` the `α·DΛ_0` penalty dominates the `Λ − Λ_0` signal on
every 0.4-cell, while the `A`-vs-`B` core difference (`~0.05` in NtD norm)
shifts eigenvalues by only `~0.05` — never enough to cross zero. An α-scan
diagnostic (central cell, coarse mesh: minima moving together and staying
negative for `α ∈ [0.25, 2]`) confirms it.

## Proof / evidence

Replayable computation with stdlib + numpy only:

1. `output/artifacts/fem_cg.py` — matrix-free P1 FEM on polar disk meshes with
   CG solves (tolerance `10⁻¹¹`, residuals verified `< 10⁻¹¹`).
2. `output/artifacts/verify_ledger.py` — assembles `Λ_A, Λ_B, Λ_0` and
   `DΛ_0(1_C)` from background gradients with 64-subcell quadrature; symmetric
   eigen-residuals `~10⁻¹⁶`.
3. `output/artifacts/ledger3.json` — raw three-mesh ledger.
4. `output/artifacts/ledger_final.json` + `output/artifacts/final_verdict.py` —
   certification: `python3 output/artifacts/final_verdict.py` prints `VERIFY_OK`.
5. Independent audit replay of the coarse mesh reproduced the gap `0.05328728`
   and row values exactly; audit recomputation confirmed `Λ_A − Λ_0` and
   `Λ_B − Λ_0` negative-definite leading spectra (`~−0.19/−0.14`), `−D ⪰ 0`,
   and the α-scan negativity.

## Limitations

- Certificate is Galerkin + mesh-convergence based (three documented meshes,
  16 Fourier modes `k ≤ 8`), not formal interval arithmetic; error bars are
  fine-vs-mid discrepancy plus eigen-residuals, not analytic FEM a-priori bounds.
- Gap claim is the spectral norm of the Galerkin difference within this basis.
- Uniform-negative verdict means the collision is a shared blind spot (both
  images empty) at the fixed level `α = 1.5`; other levels, regularization, or
  nonlinear tests may separate the pair. Scope must not be overstated beyond
  the logged pair, family, level, and basis.

## Reproducibility

- `python3 output/artifacts/final_verdict.py` → `VERIFY_OK` (recomputes all
  three meshes; minutes on a laptop).
- Meshes: `(N_r, N_t) = (32,128), (48,176), (64,224)`; CG tol `10⁻¹¹`;
  conductivity values and 16-cell tiling exactly as in Definitions.
- Artifacts: `fem_cg.py`, `verify_ledger.py`, `final_verdict.py`,
  `ledger3.json`, `ledger_final.json`.

## References

- H. Garde, S. Staboulis, The regularized monotonicity method: detecting
  irregular indefinite inclusions, arXiv:1705.07372 (Inverse Probl. Imaging 2019).
  https://arxiv.org/abs/1705.07372
- V. Candiani, J. Dardé, H. Garde, N. Hyvönen, Monotonicity-based reconstruction
  of extreme inclusions in EIT, arXiv:1909.12110 (SIAM J. Imaging Sci. 2020).
  https://arxiv.org/html/1909.12110v2 ; https://doi.org/10.1137/19m1299219
- B. Harrach et al., Monotonicity-Based Shape Reconstruction in EIT (foundational
  definite-case method).
  https://www.math.uni-frankfurt.de/~harrach/publications/monotonicity.pdf
