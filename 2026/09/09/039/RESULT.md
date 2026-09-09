# Certified discrete-time power-peak table for the coalescent 4x4 companion family

## Context

How large a transient a stable matrix can produce, and how tightly the
Kreiss constant captures it (the Kreiss Matrix Theorem sharpness program:
`K(A) <= sup_k ||A^k|| <= e n K(A)`), is a recognized question in matrix
analysis, pseudospectra theory, and control. It motivates Kreiss-solver
development (Mitchell, arXiv:1907.06537) and feedback design to tame
transients (Apkarian-Noll, arXiv:1910.12572); invariant-subspace criteria
give only sufficient conditions for transients (Reuter, arXiv:1909.05931).
No published reference gives exact maximal-transient indices, two-sided peak
values, or Kreiss values for the canonical coalescent companion family below.

## Definitions

For `q` in `{0, 1/8, 1/4, 3/8, 1/2, 5/8, 3/4}`, `C_q` is the 4x4 controller-form
companion matrix of `(z-q)^4`: ones on the superdiagonal and last row
`[-q^4, 4q^3, -6q^2, 4q]`. Spectrum `{q}`; Schur-stable.
With `N = C_q - qI`, exact rational arithmetic gives `N^4 = 0` while
`N^3 != 0`, so the characteristic polynomial is `(z-q)^4`.
Let `M(q) = max_{k>=0} ||C_q^k||_2` and `k*(q)` its first maximizing index.
Let `K(q) = sup_{|z|>1} (|z|-1) ||(zI-C_q)^{-1}||_2` be the discrete Kreiss constant.

## Result

The following are proved by exact rational certificates, replayed by the
stdlib-only checker `output/artifacts/verify.py` (prints `VERIFY_OK`):

| q   | k*(q) | certified M(q) interval (width 0.02) |
|-----|-------|--------------------------------------|
| 0   | 0     | [1, 1] (exact; nilpotent shift: norms 1,1,1,1,0,0,...) |
| 1/8 | 2     | [1.133429075, 1.153430000] |
| 1/4 | 3     | [1.630232909, 1.650233000] |
| 3/8 | 4     | [2.999943894, 3.019944000] |
| 1/2 | 5     | [7.098087443, 7.118088000] |
| 5/8 | 7     | [20.739226120, 20.759227000] |
| 3/4 | 11    | [86.375712713, 86.395713000] |

Each row carries an exhibiting integer-vector witness pair `(u, v)` with exact
rational lower bound `a = u^T P_{k*} v`, `nu = ||u||^2`, `nv = ||v||^2` and
`lo^2 <= a^2/(nu nv)`; an exact LDL (no-pivot, all D > 0) certificate of
`hi^2 I - P_{k*}^T P_{k*} >> 0` with `hi - lo = 0.02`; per-runner exclusion for
every other `k` in `0..120`; and a Jordan/Frobenius tail envelope with
`KWIN = 120` proving every tail power `k >= 121` has norm below `lo`.

Certified resolvent point data (exact arithmetic with `R = (rI-C_q)^{-1}` at
committed rational `r*`, same witness mechanism plus Frobenius point-upper):

| q   | r*       | (r*-1)\|\|R\|\|_2 certified point interval |
|-----|----------|------------------------------------------|
| 0   | 101      | [0.998083, 1.980300] |
| 1/8 | 101      | [0.999062, 1.982800] |
| 1/4 | 1115/406 | [1.032617, 1.511445] |
| 3/8 | 719/499  | [1.485012, 1.576968] |
| 1/2 | 536/431  | [3.191900, 3.208131] |
| 5/8 | 471/407  | [9.281926, 9.284416] |
| 3/4 | 23/21    | [39.179047, 39.179277] |

These are one-sided Kreiss data (global lower bounds `K(q) >= Klo`):
`K(1/2) >= 3.191900`, `K(5/8) >= 9.281926`, `K(3/4) >= 39.179047`.

## Proof / evidence

- Exact powers in `Q^{4x4}` (Fractions); numpy used only to propose witnesses
  and bounds; every emitted inequality re-verified exactly before inclusion.
- Upper bounds: `B^2 I - P^T P` positive-definite via exact LDL without pivoting
  (all four D pivots strictly positive rationals).
- Lower bounds: integer vectors from 1e6-rounded SVD factors; exact check
  `lo^2 nu nv <= a^2` with `lo` a 9-decimal floor.
- Tail: with `N = C_q - qI` nilpotent of index 4 and exact bounds
  `U_j^2 >= ||N^j||_F^2`, `S = sum_{j=0..3} C(121,j) q^{121-j} U_j` satisfies
  `S < lo` (2.0e-30 at `q=1/2`, 2.3e-9 at `q=3/4`); for `k >= 121` the map
  `k -> C(k,j) q^{k-j}` is decreasing (ratio `q(k+1)/(k+1-j) <= 1` since
  `(1-q)(k+1) >= 3 > j`), so every tail power has `||.||_2 <= S < lo`.
- `q = 0`: stored rationals give `P_k^T P_k = diag(0/1 projector)` for
  `k = 1, 2, 3` (off-diagonals exactly 0, diagonals in `{0,1}` with max 1,
  hence `||P_k||_2 = 1` exactly); `P_0 = I` has norm 1, `P_k = 0` for `k >= 4`.
- Independent audit re-ran `verify.py` (VERIFY_OK) and cross-checked float SVD
  argmax/values for `k = 0..40`, agreeing with `k*`/floors to 9 decimals.

## Limitations

- The target gap `M(1/2)/K(1/2) >= 1.5` is NOT proved: it needs a certified
  global Kreiss upper bound `K(1/2) <= K_hi`, which was not achieved (adjugate
  triangle majorant gives ~10.2 vs true ~3.19). Numerically
  `M/K ~ 7.098/3.192 ~ 2.22`, stated as conjecture with computed evidence only.
- No claim of a 10%-width two-sided Kreiss interval for any `q`; the resolvent
  point-hi values are Frobenius ceilings at the stated `r*` only.
- Float SVD values are guidance, not proof; proof rests on the exact checks.

## Reproducibility

Run `python3 output/artifacts/verify.py` (stdlib only) from the lane root;
expect per-row OK lines and `VERIFY_OK`. `certificates.json` holds every
rational certificate.

## References

- Mitchell, Computing the Kreiss Constant of a Matrix, arXiv:1907.06537.
- Apkarian & Noll, Optimizing the Kreiss constant, arXiv:1910.12572.
- Reuter, Associating the Invariant Subspaces of a Non-Normal Matrix with Transient Effects, arXiv:1909.05931.
