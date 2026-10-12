# Self-review

## Correctness
**PASS.** At fixed \(N\), Shannon diversity is \(\log N-N^{-1}\log Q\) with \(Q=\prod_i n_i^{n_i}\), while Brillouin diversity is \(N^{-1}[\log(N!)-\log F]\) with \(F=\prod_i n_i!\). Both rankings therefore reduce to exact integer comparisons. Exhaustive enumeration of all integer partitions through \(N=8\), with independent partition-number cross-checks, proves weak-order identity through \(N=6\), the unique tie split at \(N=7\), and exactly two strict reversals at \(N=8\). The packaged verifier returns `VERIFY_OK`.

Risk: this is an exact finite-census theorem, not a statement about estimated diversity under sampling error.

## Originality
**PASS.** Peet directly compares the Brillouin and Shannon formulas and their sample-size behavior, and Palaghianu reports extremely close empirical behavior while treating them as distinct indices. Those sources do not state ordinal equivalence or a sharp reversal threshold. Searches using both index names, exact vectors, rank-reversal language, and the multinomial formulation did not locate the \(6/7/8\) boundary or the complete two-pair first strict layer.

Risk: the small profiles could occur in an unindexed classroom example or software fixture.

## Value
**PASS.** Shannon's formula is often described as an approximation or large-sample counterpart to Brillouin's finite-collection formula. Whether that approximation can change an ecological comparison rather than merely its numerical magnitude is a natural question. The result gives the exact smallest census where strict ordering changes and the complete first layer, providing a compact diagnostic case for diversity software and methodological interpretation.

Self-review: passed. Independent audit: not yet performed.
