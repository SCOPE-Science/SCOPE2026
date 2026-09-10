# Universal t-palindromicity of the odd-OSASM r=1 slice is false: minimal witness at n=2 (order 5)

## Context

Refined enumeration of alternating sign matrices (ASMs) under symmetry
(Mills–Robbins–Rumsey, Zeilberger, Kuperberg, Behrend–Di Francesco–Zinn-Justin,
Fischer, Behrend–Fischer–Koutschan, Kumari) is a recognized frontier.
Unrefined off-diagonally symmetric ASM (OSASM) enumeration recently closed
(Kuperberg even product; Kumari 2025 odd product plus even refined-symmetry
proof), leaving the odd-order (r,t)-refined reciprocity generalizing the even
identity of Kumari Theorem 5.1 / Behrend–Fischer–Koutschan (BFK) Proposition 8.1
as the adjacent open parametric symmetry.

## Definitions (solely from open full texts)

- BFK: Behrend–Fischer–Koutschan, arXiv:2309.08446 v2.
- Kumari: Nishu Kumari, arXiv:2503.18685.
- DSASM(n): symmetric n×n ASMs. Statistics: R(A) = number of nonzero
  strictly-upper-triangular entries, S(A) = number of nonzero diagonal
  entries, T(A) = column of the 1 in the first row.
- X_n(r,s,t) = Σ_{A ∈ DSASM(n)} r^{R(A)} s^{S(A)} t^{T(A)}.
- OSASM(n): even n — DSASM with all diagonal entries 0; odd n — DSASM with
  exactly one nonzero diagonal entry (BFK §8).
- X^O_n(r,t) = Σ_{A ∈ OSASM(n)} r^{R(A)} t^{T(A)}, with
  X^O_n(r,t) = X_n(r,0,t) (n even) and
  X^O_n(r,t) = (X_n(r,s,t)/s)|_{s→0} (n odd) — BFK (8.4).
- Kumari odd product (BFK (8.36), Kumari Cor 4.4):
  P_n = |OSASM(2n+1)|
      = 2^{n−1}(3n+2)!/(2n+1)! ∏_{i=1}^n (6i−2)!/(2n+2i+1)!.
- Adjacent proved facts (do not imply the target): even refined symmetry
  X^O_{2n}(r,t) = t^{2n+2} X^O_{2n}(r,1/t); odd unrefined product above;
  odd symplectic-character identity (8.35).

## Result

**Theorem (disproof with minimal witness).**
The universal claim that for every n ≥ 1 the r=1 slice X^O_{2n+1}(1,t) is
t-palindromic (c_k = c_{d_n−k} with d_n its true t-degree) with
X^O_{2n+1}(1,1) = P_n is **false**. At n = 2 (order 5):

    X^O_5(1,t) = 3t + 7t² + 9t³ + 9t⁴ + 4t⁵,

so d_2 = 5 and X^O_5(1,1) = 32 = P_2, but palindromicity fails with minimal
interior witness (n,k) = (2,1): c_1 = 3 ≠ 9 = c_4 (also c_0 = 0 ≠ 4 = c_5,
c_2 = 7 ≠ 9 = c_3). Moreover no shift m ∈ {0,…,9} yields t^m·P(1/t) = P,
so the failure is not a normalization-shift artifact.
By contrast n = 1 (order 3) is palindromic: T-distribution {1:1, 2:2, 3:1}.

## Proof / evidence

Reproducible exhaustive certificate in `output/artifacts/verify_osasm.py`
(stdlib only; replay `python3 output/artifacts/verify_osasm.py` → `VERIFY_OK`):

1. Generate all valid ASM rows (entries in {−1,0,1}, sum 1, nonzero entries
   alternate starting/ending with 1).
2. Backtrack row-by-row with column pruning (partial column sums ∈ {0,1},
   column alternation, first-nonzero-is-1) and first/last-row single-1
   enforcement; verify every completed leaf column-wise.
3. Filter to DSASMs by exact transpose symmetry; filter to OSASMs by the
   diagonal condition above.
4. Cross-validate against five independent published anchors: ASM counts
   1,2,7,42,429; DSASM counts 1,2,5,16,67 (BFK Table 1); OSASM counts
   1,1,4,3,32 (BFK Table 3); BFK (8.3) refined rows for n ≤ 4 including
   X^O_3 = rt+rt²+rt³+r²t² and X^O_4 = r²t²+r²t³+r²t⁴ at r=1;
   Kumari P_1 = 4, P_2 = 32 matching the t=1 sums at orders 3 and 5.
5. Read off exact r=1 T-distributions:
   order 1: {1:1}; order 2: {2:1}; order 3: {1:1,2:2,3:1};
   order 4: {2:1,3:1,4:1}; order 5: {1:3,2:7,3:9,4:9,5:4},
   and test palindromicity including all shifts.

Since only one counterexample is needed, enumeration to order 5 suffices.
The even-symmetry proof (BFK (8.29) via Kuperberg (8.20)) uses an even-size
Pfaffian-term pairing with (−1)^n cancellation; the odd kernel has an extra
row/column and a χ_odd correction term in (8.21) so the substitution does
not close (BFK §8.5 leaves the odd analogue open). Hence the n=2 asymmetry
is consistent with the proved even symmetry and odd product.

## Limitations

- Exhaustive search covers orders ≤ 5 (429 ASMs at n=5); disproof needs only
  the order-5 counterexample.
- No claim about n ≥ 3 palindromicity or any repaired symmetry.
- The enumerator is a validating tool, not an original contribution.

## Reproducibility

- Script: `output/artifacts/verify_osasm.py` (stdlib only:
  itertools, math, collections).
- Command: `python3 output/artifacts/verify_osasm.py` → prints per-order
  counts and T-distributions, Kumari P_1/P_2 match, order-3 symmetry,
  order-5 asymmetry under every shift, `MINIMAL_WITNESS (n,k)=(2,1)`,
  `VERIFY_OK`.
- Independently re-executed at audit with identical output.

## References

- Roger E. Behrend, Ilse Fischer, Christoph Koutschan,
  Diagonally symmetric alternating sign matrices, arXiv:2309.08446.
  https://arxiv.org/abs/2309.08446
- Nishu Kumari, Off-diagonally symmetric alternating sign matrices,
  arXiv:2503.18685. https://arxiv.org/abs/2503.18685
- Greg Kuperberg, Symmetry classes of alternating-sign matrices under one
  roof, math/0008184. https://arxiv.org/abs/math/0008184
- OEIS A005156 — 2n×2n OSASM numbers. https://oeis.org/A005156
