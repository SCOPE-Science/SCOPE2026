# Self-review

## Correctness
**PASS.** At fixed total \(N\), HHI is ordered by the exact integer \(Q=\sum_i n_i^2\), while Hall–Tideman is ordered oppositely to \(R=\sum_i i d_i\) after sorting sizes \(d_i\) from largest to smallest. The packaged verifier generates every profile through \(N=12\) independently as partitions and canonicalized compositions, checks all \(762\) admissible within-\((k,N)\) pairs, and reproduces the unique tie split at \(N=10\), absence of strict reversal through \(N=11\), and unique strict reversal at \(N=12\). It returns `VERIFY_OK`.

Risk: the cutoff is specific to the positive-integer grid and fixed-\((k,N)\) comparisons.

## Originality
**PASS.** Hall and Tideman introduced the rank-weighted concentration measure and compared it with Herfindahl; Bikker and Haaf and later Anbarci and Katzman explicitly distinguish the weighting structures. Generic differences between the indices are therefore prior work and are not claimed as new. Searches using Hall–Tideman, Rosenbluth, HHI, fixed-total, exact-profile, and rank-reversal formulations did not locate the sharp \(10/12\) finite boundary or the unique first strict pair.

Risk: the original 1967 full text was not retrievable in the checked routes, and an unindexed exercise or software fixture could contain an individual witness.

## Value
**PASS.** HHI is a standard market-concentration benchmark, whereas Hall–Tideman was designed to incorporate firm rank and the number of firms. Fixing firm count and total removes two obvious scale effects and isolates the difference between squared-share weighting and rank weighting. The exact first strict reversal is therefore a natural diagnostic for interpretation and implementation, not an arbitrary numerical slice.

Self-review: passed. Independent audit: not yet performed.
