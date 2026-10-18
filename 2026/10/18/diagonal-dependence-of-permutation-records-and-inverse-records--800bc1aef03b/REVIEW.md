# Scientific review: diagonal record/inverse-record dependence

## Correctness — PASS

Conditioning on the unordered initial \(i\)-element value set separates the initial and complementary permutation orders. The first record event retains conditional expectation \(1/i\), so the between-set covariance vanishes. The inverse record event is determined entirely by the complementary suffix, impossible, or independent of the location of the largest prefix value except at the unique exceptional prefix set \(\{1,\ldots,i\}\) when \(i=j\). There the indicators coincide and yield covariance \((i-1)/i^2\); multiplying by the exact exceptional-set probability \(\binom ni^{-1}\) proves the full finite matrix. Binomial bounds prove the stated asymptotic, and relative-rank independence yields the record-count variance. An independent exhaustive checker corroborated every pair through size eight, including the boundary coordinates.

## Originality — PASS, with residual risk

The closest full-text comparison is Gnedin (2006), on upper and lower record values in a single permutation and coherent biased laws; Gnedin and Gorin (2012), on record-dependent measures and inverse constructions; Gnedin and Marynych (2012), on planar record symmetries; and Gessel and Zhuang (2023), on descent-composition statistics of permutations and inverses. The latter framework does not directly cover record sets. None of the inspected statements gives the exact uniformly random upper-record/inverse-upper-record cross-covariance or its off-diagonal pairwise independence. Related published mathematical research records and accessible prior scientific claims were also compared by their statistical objects and implications, not just titles. A classical implicit joint record-set enumeration might still imply this law and is a priority risk. This is a best-knowledge self-review, not independent priority certification.

## Mathematical value — PASS

The simultaneous upper-record patterns of a permutation and its inverse are natural dual ranking observables. Marginal record independence alone does not predict dependence across the two arrays. The exact sparsity and rank of their cross-covariance matrix, the localization of all pairwise dependence to a rare complete-prefix-block event, and the aggregate correlation decay quantify a nontrivial structural separation between two linked ranking processes. This is a complete all-size indexed dependence law, not a chosen small parameter example.

## Limitations

Uniform permutations only; the theorem concerns pairwise cross-dependence and not complete vector independence. Full priority verification against every historical implicit enumeration remains open. Finite computer tests support but cannot replace the all-size conditional argument.

Self-review: passed. Independent audit: not yet performed.
