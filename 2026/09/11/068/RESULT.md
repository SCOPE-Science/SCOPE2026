# Fixed-strip observability for golden-slope torus quasimodes: limit 1/4, hence liminf ≥ 1/8

## Context

Observability and control of Schrödinger eigenfunctions on the flat torus
without geometric control is a recognized program (Jaffard–Haraux for exact
modes, Lebeau, Anantharaman–Macià–Léautaud for evolving solutions and damped-wave
decay). What was missing was a fixed-constant bound for *stationary narrow
quasimodes* that can scar on an unobserved closed geodesic. This record closes
that gap for the canonical hardest direction on the square torus.

## Definitions

Let `T^2 = R^2/Z^2` with the flat metric and Laplacian `Δ`.
Let `ω = {x : |x2 − 1/2| < 1/8}`, the fixed open strip of area `1/4`,
disjoint from the closed geodesic `γ0 = {x2 = 0}`.
Let `φ = (1+√5)/2`, `ξ* = (1,φ)/|(1,φ)|` with second component
`s* ≈ 0.8507`, and `R = 1/(2πh)`.
Let `C_h = {k ∈ Z^2∖{0} : |k/|k| − ξ*| < h^{1/2}}` be the golden Fourier cone.
A sequence `u_h` is admissible if it is L2-normalized,
`‖(−h^2 Δ − 1)u_h‖ = r(h)·h^2` with `r(h) → 0` (i.e. `o(h^2)`),
and microlocalized near `ξ*` in the sense
`Σ_{k ∉ C_h} |c_k|^2 → 0` for Fourier coefficients `u_h = Σ_k c_k e_k`,
`e_k(x) = e^{2πik·x}`.

## Result

**Theorem.** Every admissible golden-slope `o(h^2)` quasimode satisfies
`‖u_h‖²_{L^2(ω)} → 1/4`, hence `liminf ≥ 1/8` with margin `1/8`.
Equivalently, every semiclassical defect measure of an admissible sequence
gives mass exactly `1/4` to `ω × S^1` (x-marginal `dx ⊗ δ_{ξ=ξ*}` on `ω`);
in particular no admissible defect measure is supported in the closed
complement of `ω`. The constant `1/4` is sharp.

**Nonvacuity.** Fibonacci modes `k_n = (F_n,F_{n+1})`, `h_n = 1/(2π|k_n|)`,
`u_n = e_{k_n}` are exact eigenfunctions (residual `0`), satisfy
`|k_n/|k_n| − ξ*| = O(h_n^2) ≪ h_n^{1/2}` (cone PASS for `n = 3…12`),
and have `|u_n|^2 ≡ 1` so strip mass exactly `area(ω) = 1/4`.

## Proof / evidence

Closed-form analytic proof. The residual gives the shell estimate
`Σ_k E_k²|c_k|² = r(h)²/(2π)^4 =: S(h) → 0` with `E_k = |k|^2 − R^2`.
Since `ω` depends only on `x2`, integrating `|u|²` over `x1` gives
`‖u‖²_{L^2(ω)} = Σ_m χ̂(m) a_m` with `χ = 1_{(3/8,5/8)}`,
`χ̂(0) = 1/4`, `a_m = Σ_k c̄_k c_{k+(0,m)}`.
Lemma A (inner trig minorant): for every `ε > 0` there is a real trig
polynomial `p ≤ χ` with `∫p ≥ 1/4 − ε`, via a trapezoid `f` and uniform
approximation. Since `|u|² ≥ 0`, `‖u‖² ≥ Σ_{|m|≤M} p̂(m)a_m`.
Lemma B (fixed off-diagonal decay): for fixed `m ≠ 0`, `a_m(h) → 0`.
Indeed with `c0 = s*/2 ≈ 0.4253`, every `k ∈ C_h` has `k2 ≥ c0|k|`,
so the vertical-shift gap `D_k = 2mk2 + m²` satisfies
`|D_k| ≥ c0|m|R/2 → ∞` at large frequency; splitting into
out-of-cone, bounded-frequency (both killed by shell plus microlocalization
mass vanishing), and large-frequency parts (killed by
`max(|E_k|,|E_{k+v}|) ≥ |D_k|/2` plus Cauchy–Schwarz against `S(h)`)
gives decay. Hence `∫|u_h|²p → p̂(0) ≥ 1/4 − ε` for all `ε`,
so `liminf ≥ 1/4`; an outer majorant gives the matching upper bound.
Only `o(h)`-smallness of `S(h)` is used, so `o(h^2)` has room to spare.

Replayable verifier `output/artifacts/verify_target.py` → `VERIFY_OK`:
Fibonacci modes `n = 3…12` admissible with exact strip mass `1/4`;
`N = 1999` midpoint quadrature gives `0.24962…`, error `3.75e−4 ≤ 1/N`;
vertical `cos(2π·3x2)` beam (strip ≈ 0.197) rejected by cone screen
(direction error `0.55`); periodized Gaussian scar at `x2 = 0`
(strip ≈ 2.6e−26) rejected by cone plus residual screens
(`residual/h² ≈ 566`). Numerics are confirmatory only.

## Limitations

Proof uses flat-torus Fourier structure essentially; no transfer to variable
metrics, boundaries, or non-Diophantine directions is claimed.
Microlocalization is read as vanishing out-of-cone Fourier mass.
Numerics are confirmatory quadrature, not interval arithmetic.
No convergence rates or wider-cone uniformity are claimed.

## Reproducibility

Run `python3 output/artifacts/verify_target.py` (stdlib + numpy,
deterministic) and compare with `output/artifacts/verify_log.txt`.
Check cone errors `O(h^2)` vs `h^{1/2}`, residuals, mesh quadrature,
and avoidance-trial rejections. Proof steps above are self-contained.

## References

- N. Anantharaman, F. Macià, Semiclassical measures for the Schrödinger
  equation on the torus, JEMS 2014.
- N. Anantharaman, M. Léautaud, Sharp polynomial decay rates for the damped
  wave equation on the torus, APDE 2014.
- C. Jaffard et al., observability/control of torus Schrödinger group.
- Burq–Germain, trace and observability inequalities for torus eigenfunctions.
