# Self-review

## Correctness
PASS. Conditional on \(K=k\), the source fixed-size theorem applies exactly, and \(K\) is observed from \(S\) while remaining independent of \(T\). The operator-norm upper bound therefore averages the squared fixed-size norms. A single centered coordinate indicator attains every conditional bound, so the average is exact. The marked-subvector identity follows from the source two-subvector reduction together with the exact calculation \(r_j=\sqrt p\). Boundary cases and normalization were checked separately.

## Originality
PASS. The closest inspected source, Chang--Chen, states the fixed-size nested-subset formula and describes it as a partial answer for dependent random subsets. It does not state Bernoulli random-size thinning. The classical Csáki--Fischer full text covers fixed polyhypergeometric laws, not the binomial mixture. Focused searches under maximal-correlation/HGR, random-subset, Bernoulli-thinning, Johnson-scheme, Boolean-slice, inclusion-matrix, and erasure terminology found no covering statement. Residual risk remains that an equivalent result is hidden in older association-scheme language.

## Value
PASS. Bernoulli thinning is the most natural random-size counterpart of uniform fixed-size nested sampling. The result identifies the exact dependence loss, yields sharp finite-population bounds and a proportional-size limit, and shows that adding independent nondegenerate marks collapses the exact answer to \(\sqrt p\), independent of \(n\) and \(m\).

## Closest literature and limitations
Chang--Chen, arXiv:2411.17109 / DOI:10.1214/25-AAP2293, supplies the fixed-size theorem and general marked-subvector reduction. Csáki--Fischer (1963) supplies classical fixed polyhypergeometric eigenvalues. The present theorem does not address unequal retention rates, thinning dependent on subset labels beyond membership, arbitrary dependent nested subsets, or dependent marks.

Self-review: passed. Independent audit: not yet performed.
