# Certified dimer-induced Sturm gap for 10×10 disordered Jacobi matrices

## Context

Sharp eigenvalue localization for Jacobi (real symmetric tridiagonal)
matrices underlies inverse eigenvalue problems, quadrature nodes, and
discretized Sturm–Liouville spectra. Classical Gershgorin discs and Brauer
Cassini ovals ignore tridiagonal oscillation structure and can remain
connected even when a dimerized chain has a robust bulk gap (SSH-type).
This record gives a concrete uniform gap certificate for a small disordered
box, with a short recurrence-induction proof plus machine-checkable finite
cases, and a reusable template for certifying gaps/counts where textbook
ovals give only a connected union.

## Definitions

Let `J` be the box of real symmetric tridiagonal `10×10` matrices `T` with:

- diagonal `d_i ∈ [-1/10, 1/10]`, `i = 1,…,10`,
- odd off-diagonals `e_1,e_3,e_5,e_7,e_9 ∈ [7/5, 8/5]` (strong bonds),
- even off-diagonals `e_2,e_4,e_6,e_8 ∈ [2/5, 3/5]` (weak bonds).

For `λ ∈ ℝ` define `p_0 = 1`, `p_{-1} = 0` and

```text
p_k(λ) = (λ − d_k)·p_{k−1}(λ) − e_{k−1}²·p_{k−2}(λ),  k = 1,…,10
```

with the `k = 1` correction term understood as `0`.
Put `r_k = p_k / p_{k−1}` when defined, so
`r_1 = λ − d_1` and `r_k = (λ − d_k) − e_{k−1}² / r_{k−1}` for `k ≥ 2`.

Classical Sturm theorem (Jacobi case, all `e_j ≠ 0` on `J`): the number
`N(λ)` of eigenvalues of `T` strictly below `λ` equals the number of sign
agreements `p_k·p_{k−1} > 0`, `k = 1,…,10`, whenever no `p_k(λ)` vanishes
(i.e. `λ` is not an eigenvalue of `T` or of a leading principal submatrix).

## Result

**Theorem.** For every `T ∈ J`, `spec(T) ∩ (−3/5, 3/5) = ∅`.
Equivalently the Sturm sign-agreement counts at `λ = ±3/5` are both exactly
`5`: every `T ∈ J` has `5` eigenvalues below `−3/5` and `5` above `+3/5`.

Moreover:

- (a) the Gershgorin union of every `T ∈ J` is connected and covers
  `[−3/5, 3/5]` (no gap);
- (b) the Brauer Cassini union of every `T ∈ J` contains `[−3/5, 3/5]`
  (no gap);
- (c) row-wise Gershgorin applied to `T²` has uniform lower edge
  `min_i min_J(C_i − R_i) = 13/100`, certifying at best
  `spec(T²) ≥ 13/100`, i.e. the gap
  `(−√13/10, √13/10) ≈ (−0.3606, 0.3606)`.
  The Sturm `0.6` certificate is therefore `≥ 66%` sharper
  (`0.6/0.3606 > 1.66`) and adds exact `5/5` eigenvalue counts.

## Proof / Evidence

Two-endpoint exact-rational Riccati interval induction (all numbers are
exact `Fraction`s; see `artifacts/sturm_gap_certificate.py`, stdlib only).

At `λ = +3/5`, take `R_o = [1/2, 11/10] > 0`, `R_e = [−5, −1] < 0`.
Then `λ − d_1 ∈ [1/2, 7/10] ⊂ R_o`. With strong-bond squares
`E_s² = [49/25, 64/25]`, weak-bond squares `E_w² = [4/25, 9/25]`, and the
four-corner subtraction rule, the even-step image of `R_o` and odd-step
image of `R_e` are:

```text
E(R_o) = [1/2 − 64/25·2, 7/10 − 49/25·10/11] = [−231/50, −119/110] ⊂ R_e,
O(R_e) = [1/2 + 4/125, 7/10 + 9/25] = [133/250, 53/50] ⊂ R_o.
```

Explicitly `−231/50 ≥ −5`, `−119/110 ≤ −1`, `133/250 ≥ 1/2`,
`53/50 ≤ 11/10`. By induction for every `T ∈ J`: `r_odd ∈ R_o > 0`,
`r_even ∈ R_e < 0`, no `p_k` vanishes, and with `p_0 > 0` the sign word is
forced to `(+,+,−,−,+,+,−,−,+,+,−)` with exactly **5** agreements.
Hence `N(+3/5) = 5` uniformly and `+3/5 ∉ spec(T)`.

At `λ = −3/5`, mirror boxes `R_o = [−11/10, −1/2]`, `R_e = [1, 5]` give
`E(R_o) = [119/110, 231/50] ⊂ R_e`,
`O(R_e) = [−53/50, −133/250] ⊂ R_o`,
sign word `(+ ,−,−,+,+,−,−,+,+,−,−)` with exactly **5** agreements.
Hence `N(−3/5) = 5` uniformly.

Since `N(−3/5) = N(+3/5) = 5` and endpoints are never eigenvalues,
no eigenvalue lies in `[−3/5, +3/5]` for any `T ∈ J`.

Baselines (exact rationals, same script): (a) each Gershgorin disc has
`R ≥ 7/5` (edge) or `≥ 9/5` (interior) with center in `±1/10`, hence covers
`[−3/5, 3/5]`; (b) Brauer oval `(1,3)` has `min R_1·R_3 = 7/5·9/5 = 63/25`
while `max |z−d_1||z−d_3| = (7/10)² = 49/100 ≤ 63/25` over the window, so the
whole window lies in one oval; (c) `(T²)_{ii} = d_i² + e_L² + e_R²`,
`(T²)_{i,i±1} = e(d+d)`, `|(T²)_{i,i±2}| = ee`, and joint minimization over
`J` gives row minima `17/20` (rows 1,10), `97/100` (rows 2,9), `13/100`
(rows 3–8) via aligned `±1/10` diagonals, outer bonds at hi, weak-at-hi /
strong-at-lo endpoint minima with vertex-outside checks.

Numerical sampling (60k uniform + bond-corner sweep, numpy) is sanity only,
not proof: worst observed `min|eig|` `0.915` (random) / `0.808` (corners),
consistent with the `0.6` certificate.

## Limitations

- Fixed box only (`n = 10`, stated intervals); generalization to larger `n`
  or wider disorder is not proved.
- Not sharp: numerics suggest the true uniform gap is `≈ 0.8`, so `0.6` is
  safe but not optimal.
- No physics novelty over SSH claimed beyond the disorder-uniform finite-`n`
  certificate plus oval comparison.
- Sturm agreement-count convention stated explicitly and cross-checked
  numerically; reader can verify sign convention independently.

## Reproducibility

```text
python3 artifacts/sturm_gap_certificate.py   # exact proof (stdlib only)
```

Reproduces `CLOSED: True` at both endpoints with the fractions above and
the `5/5` counts, plus all baseline row minima.

## References

- Horn & Johnson, *Matrix Analysis* (Gershgorin discs, Brauer Cassini ovals).
- Teschl, *Jacobi Operators and Completely Integrable Nonlinear Lattices*
  (Jacobi/Sturm oscillation theory).
- Su–Schrieffer–Heeger model reviews (physics origin of the dimer gap,
  infinite periodic case only).
