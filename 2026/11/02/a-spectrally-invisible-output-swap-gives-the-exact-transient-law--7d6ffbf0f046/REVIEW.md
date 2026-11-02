# Scientific review

## Correctness: PASS

The characteristic-polynomial lemma is proved for symmetric, zero-diagonal binary matrices with zero row sums using the power-series resolvent and rank-one determinant identity. The proof then derives the two nilpotent Jordan-block partitions by an explicit cyclic-polynomial factorization and by the dimension of the kernel/image intersection after swapping two outputs. Differences of kernel sizes on the nilpotent component produce exactly the preperiod counts and means. All boundary regimes are included, particularly dimensions divisible by two but not four. A standalone program independently computes update maps, finite-field power ranks, and all-state preperiods on small rings. Finite tests are supporting checks, not infinite proofs.

## Originality: PASS under inspected evidence

Suzuki, Okuyama, Takahashi and Saito, arXiv:2609.34542v1 (2026), define precisely the partial-shift permutation XOR family. Their Section 3.2 restricts analysis to odd dimensions and focuses long periodic orbits, while this result treats the even-dimensional two-output-swap case and its complete preperiod distribution. The classical unpermuted Rule-90 analysis by Martin, Odlyzko and Wolfram (1984) does not by itself imply the changed Jordan blocks after an output swap. Li, Wang and Zhang, arXiv:2410.09833 (2024), provide a strong annihilator for symmetric Eulerian adjacency matrices; their theorem cannot be applied to the nonsymmetric output-permuted map. Searches of relevant mathematical records and literature did not identify an equivalent statement. The full text of Onuki, Suzuki and Saito (2025) could not be inspected; potential specialized priority remains a residual risk, so novelty is asserted only relative to the evidence assessed.

## Value: PASS

The originating partial-shift automata literature explicitly leaves even dimensions difficult. For an infinite natural family, an exactly one-output-pair permutation leaves every eigenvalue invariant yet changes the largest nilpotent Jordan block from half of the dyadic divisor to nearly the whole divisor. This gives a complete exact census of all finite-state transient lengths, including a nearly twofold worst-case extinction delay on power-of-two rings. The conclusion clarifies why characteristic polynomials alone cannot resolve convergence times in these network dynamical systems.

## Scope and limitations

The result does not count primitive cycles in the nonzero spectral component when the ring length is not a power of two, and does not handle other permutations, fields, stochasticity, or asynchronous updates. Priority remains open against relevant unavailable complete manuscripts; finite verification is not independent validation.

Self-review: passed. Independent audit: not yet performed.
