# Certified vanishing obstruction at the Saxl-adjacent staircase-vs-two-row boundary

## Context

The Saxl conjecture and the Geometric Complexity Theory (GCT) program need exact
Kronecker-coefficient boundary data: which triples of partitions of $n$ have
$g(\lambda,\mu,\nu) > 0$ and which vanish. Two-row families are a controlled
laboratory (quasipolynomial and stability theorems exist), but mixed
staircase-by-two-row triples at triangular $n$ sit outside every closed-form
regime. The admitted target predicted a positivity/vanishing minimal gap at
$n = 28$; exact computation refutes the nominated positive and reveals a
stronger structural obstruction instead.

## Definitions

- $n = 28$, $\rho_7 = (7,6,5,4,3,2,1)$ (staircase, $|\rho_7| = 28$),
  $\alpha = (14,14)$ (balanced two-row),
  $\beta_+ = (16,8,4)$, $\beta_- = (17,8,3)$.
- Kronecker coefficient by the exact class-algebra formula:
  $$g(\lambda,\mu,\nu) = \frac{1}{n!}\sum_{C} |C|\,
    \chi^\lambda(C)\chi^\mu(C)\chi^\nu(C), \quad |C_\mu| = n!/z_\mu.$$
- $p(28) = 3718$ conjugacy classes.
- Box-distance between partitions (padded with zeros to equal length):
  half the $\ell^1$ distance; one box move changes it by 1.
- First-row-padded ray: $\rho_7^{(k)} = (7+k,6,5,4,3,2,1)$,
  $\alpha^{(k)} = (14+k,14)$, $\beta_+^{(k)} = (16+k,8,4)$ at $n = 28+k$.

## Result

1. $g(\rho_7, \alpha, \beta_+) = 0$ and $g(\rho_7, \alpha, \beta_-) = 0$,
   each by an exact character sum $S = 0$ over all 3718 classes
   (115 / 122 nonzero summands respectively).
2. Full-row vanishing: for fixed first two factors $(\rho_7, \alpha)$,
   $g(\rho_7, \alpha, \nu) = 0$ for EVERY partition $\nu$ of 28 with at
   most 3 rows (80/80 exact zeros). The row has 2557 positive / 1161 zero
   entries and no negatives.
3. Local form: all 43 partitions within box-distance $\le 2$ of $(16,8,4)$
   vanish; the nearest positives lie at box-distance exactly 3 (9 partitions,
   e.g. $g(\rho_7,\alpha,(13,8,4,3)) = 9$,
   $g(\rho_7,\alpha,(13,8,4,2,1)) = 22$).
4. Ray persistence: the padded ray has value 0 at $k = 1$ ($n = 29$,
   4565 classes, 1302 nonzero terms) and $k = 2$ ($n = 30$, 5604 classes,
   228 nonzero terms).

Hence the conjectured positivity/vanishing minimal gap does not exist: the
nominated triple sits inside a certified zero neighbourhood. The staircase-vs-
balanced-two-row product at triangular $n$ sees no $\le 3$-row constituent.

## Proof / evidence

All arithmetic is exact integer arithmetic (Python integers); no floating point.

- Two independent exact Murnaghan-Nakayama engines: R1 beta-set rim-hook
  removal (`kron.py`); R2 adding-rim-hook Pieri expansion with connectivity +
  2x2-free test (`mn_add.py`); no shared code.
- Engine validation: identity-class values equal hook-formula dimensions in
  both routines ($\dim\rho_7 = 48608795688960$, $\dim(14,14) = 2674440$,
  $\dim(16,8,4) = 3444816375$, $\dim(17,8,3) = 1105104000$); full row/column
  character orthogonality for $S_n$, $0 \le n \le 8$; known values
  $((4,3,2,1)^3) = 117$, $((3,2,1)^3) = 5$; auditor re-verified R1-vs-R2
  agreement on 40 random $n=28$ classes x 4 shapes (0 mismatches).
- Certificates (a): per-class logs `full_plus.json` / `full_minus.json`
  (partition, $z_\mu$, three character values, summand); every term
  rechecked $t = (28!//z)abc$ from committed JSON; class-size sum $= 28!$;
  $S = 0$, hence $g = 0$; auditor fresh R1 resummation agrees.
- Certificate (b): exhaustive `fullrow_rho_alpha.json` (3718 exact values);
  independently enumerated 80 $\le 3$-row partitions of 28 are all 0,
  confirmed by auditor fresh R1 evaluation of all 80; tensor-dimension
  identity $\sum_\nu g\dim\nu = \dim\rho_7\dim\alpha
  = 130001307542382182400$ holds exactly.
- Certificate (c): auditor-recomputed box-distance census: 43 partitions at
  distance $\le 2$, all zero; 9 positives at distance exactly 3.
- Certificate (d): ray sparse logs `rayk1.json` / `rayk2.json` term-consistent
  with sparse sums 0; auditor fresh full R1 sums at $n=29,30$ give $g=0$.
- Reproduction: `python3 output/artifacts/verify.py` (stdlib only) prints
  `CERT_OK / ROW_OK / NBHD_OK / RAY_OK / DIM_OK / VERIFY_OK`.

## Limitations

- Computational (exact integer class-algebra) obstruction certificate; no
  general representation-theoretic proof of WHY the $\le 3$-row family
  vanishes is offered.
- Certified only for second factor $(14,14)$; no claim about other two-rows.
- Ray vanishing computed only at $k = 1, 2$, not all $k$.
- Reported 4-row positives (e.g. 9, 22 above) are computed spot values
  consistent with the row, not separately dual-certified parts of the claim.

## Reproducibility

- Engines: `output/artifacts/kron.py`, `output/artifacts/mn_add.py`.
- Logs: `output/artifacts/full_plus.json`, `output/artifacts/full_minus.json`,
  `output/artifacts/fullrow_rho_alpha.json`, `output/artifacts/rayk1.json`,
  `output/artifacts/rayk2.json`.
- Verifier: `python3 output/artifacts/verify.py` (stdlib only).

## References

- E. Briand, R. Orellana, M. Rosas, Quasipolynomial formulas for the Kronecker
  coefficients indexed by two two-row shapes. https://arxiv.org/abs/0812.0861
  (needs two two-row inputs; here only one).
- M. Rosas, The Kronecker product of Schur functions indexed by two-row shapes
  or hook shapes. https://arxiv.org/abs/math/0001084 (needs both mu,nu
  hook/two-row; staircase is neither).
- C. Ikenmeyer, The Saxl Conjecture and the Dominance Order.
  https://arxiv.org/abs/1410.6549 (concerns the Saxl square rho^2, not the
  mixed triple).
- S. V. Sam, A. Snowden, Proof of Stembridge's conjecture on stability of
  Kronecker coefficients. https://arxiv.org/abs/1501.00333 (abstract stability;
  computes no n=28 value).
