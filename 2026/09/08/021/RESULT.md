# Exact separated star-discrepancy minima over the noble-tail bounded-quotient window at N = 512, 1024, 2048

## Context

Which badly-approximable irrational minimizes the finite-N star discrepancy of
a one-dimensional Kronecker sequence is a recognized extremal question
(Roth/Schmidt lower bounds, bounded-partial-quotient theory, QMC benchmark
selection, three-distance structure). General theory and asymptotics do not
determine fixed-N minima. This record certifies the exact minima over an
explicit finite noble-tail window.

## Definitions

- Let `w` range over finite words over `{1,2,3,4}` with convergent denominator
  `q([0;w]) <= 200`. Strip trailing `1`s (same infinite expansion); the empty
  word is allowed.
- `S` = set of `alpha(w) = [0; w, 1, 1, 1, ...]`, the noble-tail irrationals
  with bounded prefix. `|S| = 2313`.
- Every `alpha` in `S` is exactly `alpha = (P + Q*sqrt(5))/R` with integers
  `P`, `Q in {+2,-2}`, `R > 0` (prefix convergents composed with
  `phi = (1+sqrt(5))/2`). Full records are in `artifacts/alpha_table.json`.
- For `alpha` in `S`, `P_N(alpha) = {{n*alpha} : 1 <= n <= N}` and `D*_N(alpha)`
  is the usual star discrepancy:
  `max over sorted points x_(i) of (i/N - x_(i), x_(i) - (i-1)/N)`.

## Result

Exact star discrepancies over all 2313 irrationals at N = 512, 1024, 2048
attain separated minima, each by exactly one twin pair `alpha, 1-alpha`
(mirror point sets, hence identical `D*`):

| N | min D* | winner C pair (D* = (C1+C2*sqrt5)/(R*N)) | R | winner words | runner-up D* | exact gap |
|---|---|---|---|---|---|---|
| 512 | 0.0019514109 | (27032, -1024) | 24764 | [3,1,3,1,4] and [1,2,1,3,1,4] | 0.0019514287 ([3,2,3,2,2]) | 1.78642e-08 |
| 1024 | 0.0009761345 | (76352, -2048) | 71804 | [2,1,3,1,3,3] and [1,1,1,3,1,3,3] | 0.0009761364 ([1,4,1,2,1,1,2]) | 1.86733e-09 |
| 2048 | 0.0005378969 | (9467008, -4198400) | 71804 | same twin pair as N=1024 | 0.0005398109 ([1,4,1,2,1,1,2]) | 1.91401e-06 |

Winner data: N=512: `alpha = [0;3,1,3,1,4,1,...] ~= 0.26367016088051204`,
`(P,Q,R) = (6534,-2,24764)`, `q = 91`.
N=1024/2048: `alpha = [0;2,1,3,1,3,3,1,...] ~= 0.35839886546647814`,
`(P,Q,R) = (25730,2,71804)`, `q = 173`.
The twin satisfies `alpha + (1-alpha) = 1` exactly
(`P0*R1+P1*R0-R0*R1 = 0`, `Q0*R1+Q1*R0 = 0`). `N*D*_min`:
0.99912 (512), 0.99956 (1024), 1.10161 (2048).
Full 2313-row exact tables are in `artifacts/Dstar_N512.json`,
`artifacts/Dstar_N1024.json`, `artifacts/Dstar_N2048.json`.

## Proof / evidence

Exact integer arithmetic over `Q(sqrt5)`; no floating-point verdict and no
handbook constant enters the proof chain:

- Floors `floor(n*alpha)` from a float guess corrected by exact sign tests of
  `A + B*sqrt5` (`B = 0`: sign of `A`; same nonzero signs: that sign; opposite
  signs: sign of `A^2 - 5*B^2`, negated if `A < 0`).
- Sorting of `{n*alpha}` by the same exact comparator; `D*_N` one-sided maxima
  `i/N - x_(i)`, `x_(i) - (i-1)/N` each of the form `(C1+C2*sqrt5)/(R*N)`,
  maximized by exact comparison.
- Cross-irrational comparisons (different `R`) by
  `(A1*R0-A0*R1) + (B1*R0-B0*R1)*sqrt5` vs 0.
- Three-distance cross-check on circular consecutive gaps (including wrap gap):
  element sums exactly `(R, 0)`; distinct values `<= 3`. Winners:
  N=512 `{311, 201}` (2 values); N=1024 `{625, 399}` (2 values);
  N=2048 `{1024, 625, 399}` (3 values).
- Auditor independently recounted the scope (4954 raw words collapsing to 2313),
  re-derived the `(P,Q,R)` formula, fully recomputed all 2313 `D*` values at
  N=512 and N=1024 with 0 mismatches, spot-recomputed 20/20 at N=2048, and
  exhaustively verified the winner `C`-group strictly beats every other
  `C`-group by exact sign at all three N.

## Limitations

- Scope `S` is the noble-tail (eventual all-ones) subset of the quotient-`<=4`
  window, not the full infinite bounded-quotient-4 class.
- Minimizer is unique only up to the exact mirror symmetry `alpha <-> 1-alpha`;
  as labelled irrationals it is a twin pair, not a singleton.
- Finite-N statements only (`N` in `{512, 1024, 2048}`); no asymptotic or
  uniform-in-N bound.
- The N=1024 separation (1.87e-09) is thin but exact: an integer sign
  certificate, not a floating-point verdict.

## Reproducibility

Stdlib-only Python. Scripts expect to run from the workspace root with paths
`output/artifacts/...` as coded in `verify.py` / `replay.py`:

```
python3 output/artifacts/enumerate.py
python3 output/artifacts/verify.py
python3 output/artifacts/replay.py 512 1024 2048   # -> REPLAY PASS
```

(`enumerate.py` writes `output/artifacts/alpha_table.json`; adjust paths if
invoking from another working directory.)

## References

- R. Hofer and F. Puchhammer, Sharp general and metric bounds for the star
  discrepancy of perturbed Halton--Kronecker sequences, arXiv:1611.01288.
- I. A. Abderrahim, C. Doerr, M. Durand, Finding Low Star Discrepancy 3D
  Kronecker Point Sets Using Algorithm Configuration Techniques,
  arXiv:2604.00786.
- L. Kuipers and H. Niederreiter, Uniform Distribution of Sequences,
  https://doi.org/10.1002/9781118031649 (general Kronecker/Ostrowski/
  three-distance theory).
- Greedy 1D low-discrepancy constructions, arXiv:2406.18132 (active 1D
  extremal context).
