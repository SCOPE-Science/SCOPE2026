# Self-review

## Correctness
**PASS.** The finite domain is completely parameterized by \(TP\) and \(FP\) once \(N\) and \(P\) are fixed. Exact enumeration covers every positive-cell table through \(N=7\), every within-prevalence pair, and compares Matthews coefficients without floating-point arithmetic. The counts are \(0,0,0,3\) strict reversals for \(N=4,5,6,7\). The positive-Matthews witness has \(F_1\) values \(4/7<2/3\) and Matthews squares \(1/36>1/120\). The odd and even all-larger-size families follow from explicit positive factorizations, and the packaged verifier returns `VERIFY_OK`.

Risk: zero-cell matrices are outside the theorem, and changing that boundary condition creates a different finite problem.

## Originality
**PASS.** Prior work directly compares Matthews correlation and \(F_1\), explains why they can disagree, exhaustively studies large confusion-matrix sets, and reports real classifier rankings that change with the metric. Those results dominate any claim that disagreement itself is new. The accepted statement is instead the sharp fixed-prevalence positive-cell support boundary: no reversal through six observations, exactly three first-layer pairs at seven, and a same-prevalence positive-Matthews family for every larger sample size. Targeted published-result and web searches did not locate this boundary or the exact witness.

Risk: because the finite boundary is elementary once the two formulas are juxtaposed, an unindexed teaching exercise or software regression test could contain an equivalent seven-case example.

## Value
**PASS.** Matthews correlation and \(F_1\) are widely used competing summaries for binary biomedical classification, and published work documents that they can rank real classifiers differently. Fixing both sample size and class prevalence removes the most obvious source of incomparable evaluations. The smallest nondegenerate sample on which the metrics can still reverse is therefore a natural structural benchmark. The first layer contains a reversal with both classifiers positively correlated with truth, and the explicit all-size family shows the conflict is not a one-off pathology.

Self-review: passed. Independent audit: not yet performed.
