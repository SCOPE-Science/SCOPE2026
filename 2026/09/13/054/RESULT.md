# Normalized log-unit covering growth for Q16+ vs Q32+

## Context

Let `K_m^+ = Q(zeta_m + zeta_m^{-1})` be the maximal real subfield of the
`m`-th cyclotomic field, for `m in {16, 32}`. Then `d_16 = 4`, `d_32 = 8`
are the degrees, `r_m = d_m - 1` are the unit ranks (`r_16 = 3`,
`r_32 = 7`). Let `Lambda_m = Log(O_{K_m^+}^\times)` be the log-unit
lattice in the sum-zero hyperplane of `R^{d_m}` with the induced standard
Euclidean norm, and `mu(Lambda_m)` its Euclidean covering radius measured
intrinsically in that hyperplane. The question is whether the rank-
normalized covering radius `mu(Lambda_m)/sqrt(r_m)` strictly increases
from `m = 16` to `m = 32`.

## Definitions

- Embeddings: `sigma_j(x) = x(zeta_m^j + zeta_m^{-j})` for odd `j`.
- Generators: cyclotomic units `xi_a = (zeta_m^a - 1)/(zeta_m - 1)`;
  totally positive real units act as
  `eta_a : sin(pi j/m) -> sin(pi a j/m)`.
- Log vectors: `v_a = (log|sin(pi a j/m)| - log|sin(pi j/m)|)_j`, which lie
  in the sum-zero hyperplane.
- Gram matrices: `G_m = M_m^T M_m` from the generator log-vectors in
  coefficient coordinates `Z^{r_m}`; `mu(Lambda_m)` equals the covering
  radius of `(Z^{r_m}, G_m-norm)`, hence basis-independent.
- Full-unit identification: both fields have class number one
  (`h(Q(zeta_32)) = 1`), so by Sinnott's cyclotomic-unit index formula the
  cyclotomic units generate the full unit lattice modulo torsion.

## Result

**Theorem.** With notation above,

    mu(Lambda_32)/sqrt(7)  >  mu(Lambda_16)/sqrt(3),

via the certified bounds

    mu(Lambda_16) <= 1.25675225   (normalized <= 0.72558625),
    mu(Lambda_32) >= 2.20         (normalized >= 0.83152184),

leaving a positive separation gap of at least `0.105935`.

## Proof / Evidence

Gram data: `det G_16 = 23.8494514174`, `det G_32 = 121185.0274745`;
regulators `2.4417950066` and `123.0777333002`, agreeing with LMFDB
`4.4.14641.1` and `8.8.4294967296.1` to all shown digits.

Upper bound (`mu_16`): interval-LDL Gram-Schmidt bound
`mu^2 <= 2.2288107273`, so the relevant-vector threshold is
`Q = 4 mu^2 <= 8.9152429093`. Interval LDL of the shifted matrix
`G_16 - 0.489 I` has `D` infima `3.058262, 2.860945, 1.049179`, all
positive, so `lambda_min(G_16) >= 0.489`; every nonzero `z` outside
`[-4,4]^3` has `q(z) >= 25*0.489 - 1e-9 = 12.225 > Q`. Exhaustive
interval check inside the box lists all 22 lattice vectors with `q <= Q`
(the complete relevant-vector set). The Voronoi cell is contained in the
polytope cut out by these 22 vectors; its maximum is attained at a
vertex. Each triple is solved exactly-first (`V u = rhs` by exact integer
adjugate; `det == 0` triples are exactly singular, 428 skipped), then
`G x = u` by interval-LDL substitution. Result: 24 vertices, deepest
`q* in [1.5794261923, 1.5794261949]`, so
`mu(Lambda_16)^2 <= 1.5794261949`, `mu(Lambda_16) <= 1.25675225`.
The bound is sharp (vertex approximately `(-1/4,-1/4,3/4)`).

Lower bound (`mu_32`): hole
`t = (1/2,0,1/2,1/2,0,1/2,1/2)` in coefficient coordinates has
`G_32`-distance `sqrt(5.1669025993) = 2.27308218` (nearest lattice point
`(1,0,0,0,1,1,0)`). Interval-LDL sphere-decoder DFS proves no integer
vector comes within `2.20` (threshold `R2dec = 4.84 + 1e-6`, `1e-9`
margins, full-interval-endpoint branching plus `+/-1` expansion,
fail-closed leaf recheck): 35 nodes, zero leaves below `4.84`. Hence
`mu(Lambda_32) >= 2.20`.

Comparison: `1.25675225/sqrt(3) = 0.72558625` and
`2.20/sqrt(7) = 0.83152184`; the gap is at least `0.105935 > 0`.

## Limitations

- Full-unit identification relies on the cited class-number-one theorem
  and Sinnott's index formula; the Gram-matrix interval certificate
  itself is self-contained.
- The `mu_16` bound is sharp; the `mu_32` lower bound `2.20` is not
  claimed sharp (numerical hole `2.27308`; true `mu_32` in `[2.20, 3.14]`).

## Reproducibility

Single script `output/artifacts/cert_final.py` (run with `PYTHONPATH=""`
via `python3`; depends only on `mpmath.iv`; seconds) prints the A0-A4/B
lines and writes `output/artifacts/cert_summary.json`.
High-precision reference: `output/artifacts/highprec_reference.py`
(mpmath, dps=80).

## References

- L. Washington, Introduction to Cyclotomic Fields (class number tables,
  Thm 11.1; Sinnott index formula, Thm 8.2).
- R. R. de Araujo, An upper bound on the covering radius of the
  logarithmic lattice for cyclotomic number fields, Discrete Math. 2024
  (doi:10.1016/j.disc.2023.113665).
- J. Punch, An improved upper bound on the covering radius of the
  logarithmic lattice of Q(zeta_n), arXiv:2507.20544 (2025).
- LMFDB NumberField entries 4.4.14641.1 and 8.8.4294967296.1
  (field identity and regulator cross-check).
