# Same-model review

## Correctness
The proof was reconstructed from the statistic definition. Conditional exchangeability is exact. The conditional mean follows from the fixed-count first- and second-order inclusion probabilities. The centered statistic has an exact linear plus degenerate quadratic expansion; the quadratic contribution is negligible at the \(k^{-1/2}\) scale, while the linear coefficients satisfy the stated Riemann-sum limits. The fixed-interior-prevalence Lindeberg conditions hold because the Bernoulli increments are bounded and the largest coefficient grows only logarithmically. A standalone exhaustive checker confirms the finite identities and source variance formula on small instances.

## Originality
The closest source, Manzhos–Ianevych–Melnyk, treats the same online AP@k random-ranking model, assumes the Bernoulli prevalence known, gives exact expectation and variance, and explicitly leaves construction of a statistical test for future work. Its fixed-count model makes the conditional reduction natural, but the inspected paper does not state the nuisance-free conditional test, either Gaussian limit, or the \(4+1\) leading variance split. Bestgen covers exact expected AP for fixed-count random rankings; Su–Yuan–Zhu cover an asymptotic AP variance for a different score-strata model; Smucker–Allan–Carterette compare generic paired significance tests for retrieval systems. None of the inspected material implies the specific AP@k theorem without the new decomposition. The classical Bernoulli-conditioning fact itself is not claimed as novel.

## Value
The finding isolates a practically relevant nuisance parameter exactly and gives both exact finite-sample calibration and a simple asymptotic alternative. The factor-five change identifies a substantial source of random-baseline noise that is invisible in the unconditional variance alone. The result is limited to ordering conditional on the observed relevance count and does not treat prevalence improvements as signal.

## Closest literature and limitations
The principal comparison is arXiv:2511.02571v1 / DOI 10.15559/26-VMSTA298. Additional comparisons are DOI 10.1515/pralin-2015-0007, arXiv:1310.5103, and DOI 10.1145/1321440.1321528. The asymptotic statement assumes a fixed \(p\in(0,1)\) and iid homogeneous relevance. A specialized unsurfaced retrieval-testing source remains a residual originality risk.

Same-model review: passed. Independent audit: not yet performed.
