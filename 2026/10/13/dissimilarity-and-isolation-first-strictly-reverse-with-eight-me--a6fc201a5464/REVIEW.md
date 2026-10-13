# Self-review

## Correctness
**PASS.** In the equal-total two-tract setting, direct substitution gives
\[
D=\frac dN
\]
and
\[
I=\frac12+\frac{d^2}{2t(2N-t)}.
\]
The symmetry reduction to feasible \((t,d)\) pairs is bijective. Exact rational enumeration of every raw configuration and every canonical pair gives no strict reversal through \(N=7\), exactly one at \(N=8\), and the displayed values. The continuation family is proved by two explicit quadratic inequalities, not inferred from finite computation.

Risk: the theorem is intentionally restricted to two tracts and equal citywide group totals.

## Originality
**PASS.** Classical segregation research already distinguishes dissimilarity as an evenness measure from isolation as an exposure measure, and Lieberson–Carter explicitly report that the approaches can lead to substantially different substantive conclusions. That broad disagreement is not claimed as new. The accepted claim is the exact two-tract equal-composition reduction, the first weak-order split at \(N=3\), the sharp first strict reversal at \(N=8\), uniqueness of the first pair, and an explicit continuation family. Semantic-result searches and exact-parameter literature searches did not locate those statements.

Risk: small-sample segregation measurement has a long literature. An unindexed exercise or specialized finite-sample note could contain the witness even though the sharp boundary theorem was not found.

## Value
**PASS.** Dissimilarity and isolation are canonical segregation indicators representing different dimensions of residential separation. Fixing equal group totals removes the standard citywide-composition explanation for isolation differences, so the theorem isolates a cleaner mechanism: concentration of the same local group imbalance in a very small tract can outweigh a larger global distributional mismatch. The unique minimal witness is therefore a compact diagnostic example for interpretation, teaching, and software validation.

Self-review: passed. Independent audit: not yet performed.
