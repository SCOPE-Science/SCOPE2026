# Exact Schrijver-sharpness census of D(6,3): minimum permanent 17, one minimizer orbit, full distribution

## Context

Let D(6,3) be the set of 6x6 (0,1)-matrices with every row sum and every
column sum equal to 3 (adjacency matrices of 3-regular bipartite graphs on
6+6 vertices). Schrijver's theorem (via Gurvits capacity methods; extended
by Csikvari's proof of Friedland's Lower Matching Conjecture and Lelarge's
lift bounds) gives the general lower bound per(M) >= ((d-1)^{d-1}/d^{d-2})^n,
i.e. for d=3, n=6: per >= (4/3)^6 ~= 5.619, so per >= 6. The Bregman-Minc
bound gives per <= 36. Only general bounds and expected/asymptotic formulae
were previously known at this order; the exact minimum, minimizer
classification, and permanent distribution over D(6,3) were not recorded
(OEIS A001501 gives only the count |D(6,3)|=297200; OEIS A089479 gives
permanent data only for full cubes through n=5).

## Definitions

- D(6,3) = {6x6 binary matrices, all row sums 3, all column sums 3}.
- per(M) = sum over the 720 permutations sigma of prod_i M[i,sigma(i)].
- Ryser formula: per(M) = sum_{S subset of columns} (-1)^{6+|S|} prod_i
  sum_{j in S} M[i,j] (64 terms).
- Row/column-permutation equivalence: M ~ P M Q for permutation matrices
  P, Q (group S_6 x S_6 of order 518400). Transpose is NOT quotiented in
  the orbit count.
- Schrijver ratio of M: per(M)/(4/3)^6.

## Result

Exhaustive enumeration gives |D(6,3)| = 297200.

**Theorem.** Over D(6,3):

- The exact minimum permanent is m = 17.
- The permanent takes exactly four values, with distribution:
  per = 17: 21600; per = 18: 216000; per = 20: 59400; per = 36: 200
  (summing to 297200).
- The 21600 minimizers form a single orbit under independent row and
  column permutations (orbit size 21600; point stabilizer of order 24
  in S_6 x S_6).
- One minimizer is

  M* = [[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,1,1],
        [0,1,0,0,1,1],[0,0,1,1,1,0],[0,0,1,1,0,1]],

  with per(M*) = 17. All row sums and column sums of M* are 3.
- The Schrijver bound is (4/3)^6 ~= 5.619 (i.e. per >= 6); hence
  per(M*)/((4/3)^6) = 17 x 729/4096 = 12393/4096 ~= 3.026. The Schrijver
  bound is therefore not sharp on D(6,3) (gap of 11 above the bound).
  The maximum 36 satisfies the Bregman-Minc bound and is attained
  (200 matrices of block-diagonal 3+3 type).

## Proof / evidence

Computational proof by complete finite enumeration (not an analytic proof):

1. Generation: row-by-row backtracking over the 20 weight-3 patterns of
   length 6 with column-sum pruning (reject colsum > 3; reject when
   remaining rows cannot fill a column to 3). Produces exactly 297200
   matrices, agreeing with OEIS A001501 a(6). The auditor independently
   re-ran this generation and reproduced N = 297200.
2. Permanent: Ryser inclusion-exclusion over all 64 column subsets per
   matrix. The auditor independently re-evaluated all 297200 permanents
   by vectorized Ryser and reproduced the 4-value distribution above,
   summing to 297200, so the minimum 17 is exhaustive.
3. Cross-checks: brute-force definition expansion over 720 permutations
   on random samples of each permanent value agreed with Ryser in every
   sample; the full 64-term Ryser transcript for M* (stored in
   artifacts/certificate.json) was recomputed term-by-term from the
   entries and sums to 17; brute force on M* gives 17.
4. Orbits: canonical key = lexicographically minimal sorted row-mask
   6-tuple over all 720 column permutations (row order quotiented by
   sorting). All 21600 minimizers share one key, hence one orbit. Direct
   S_6 x S_6 orbit enumeration of M* gives size 21600 and stabilizer
   518400/21600 = 24. The auditor reproduced both computations.

## Limitations

- Evidence is exhaustive computation with replayable certificates, not a
  by-hand proof; it covers D(6,3) only.
- The orbit count quotients by S_6 x S_6 only, not including transpose.
  Transpose maps D(6,3) to itself and the minimizer class is
  transpose-closed in the census sense, but orbit counting does not
  quotient by it.
- No claim on full B(n) cubes or other degrees/orders.

## Reproducibility

- artifacts/Mstar.csv: entries of M*.
- artifacts/distribution.csv: the 4-value frequency table.
- artifacts/certificate.json: N, distribution, minimum, orbit data, M*,
  full 64-term Ryser transcript (per-subset rowsums, products, signs),
  Schrijver ratio.
- Audit procedure: (1) check M* entries and row/column sums; (2) recompute
  per(M*) by Ryser terms and by 720-permutation brute force; (3) regenerate
  D(6,3) by pruned backtracking and confirm N = 297200; (4) recompute all
  permanents by Ryser and confirm the distribution sums to N with minimum
  17; (5) recompute canonical keys for minimizers and the S_6 x S_6 orbit
  of M*; (6) check Schrijver ceil and Bregman consistency. Standard
  scientific Python (itertools, numpy) suffices; enumeration plus full
  Ryser replay runs in about a minute.

## References

- OEIS A001501 — number of n x n (0,1)-matrices with all row/column sums 3.
  https://oeis.org/A001501
- OEIS A089479 — permanent distributions for full n x n (0,1)-matrices
  (rows 0-5). https://oeis.org/A089479
- P. Csikvari, Lower matching conjecture, and a new proof of Schrijver's
  and Gurvits's theorems. https://arxiv.org/abs/1406.0766
- L. Gurvits and J. Leake, Counting Matchings via Capacity Preserving
  Operators. https://arxiv.org/abs/1804.04351
- M. Lelarge, Counting matchings in irregular bipartite graphs and random
  lifts. https://arxiv.org/abs/1507.04739
- C. Greenhill et al., Asymptotic enumeration of constrained bipartite,
  directed and oriented graphs by degree sequence.
  https://arxiv.org/abs/2601.04822
- B. D. McKay and I. M. Wanless, On the number of Latin squares
  (extremal 1-factorisations, a distinct invariant).
  https://arxiv.org/abs/0909.2101
