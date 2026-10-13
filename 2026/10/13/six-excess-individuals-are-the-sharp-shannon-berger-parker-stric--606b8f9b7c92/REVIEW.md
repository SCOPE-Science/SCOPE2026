# Self-review

## Correctness
**PASS.** At fixed census total \(N\), Shannon entropy is \(\log N-N^{-1}\log Q\) with \(Q=\prod_i n_i^{n_i}\), while reciprocal Berger–Parker diversity is \(N/\max_i n_i\). Hence both rankings reduce to exact integer comparisons. Subtracting one mandatory individual per species turns every profile into a partition of the excess \(r\); once \(k\ge r\), larger richness only pads profiles with ones and changes neither invariant. Exhaustive exact enumeration proves weak-order identity through \(r=3\), a first tie split at \(r=4\), no strict reversal through \(r=5\), and exactly the stated first strict layer at \(r=6\). The packaged verifier returns `VERIFY_OK`.

Risk: the threshold is specific to exact positive-integer census data and fixed richness.

## Originality
**PASS.** Prior ecology literature explicitly places Shannon and Berger–Parker at different points of the Hill/Rényi diversity spectrum and documents that choosing among diversity indices can change ecological interpretation and ranking. The checked literature therefore owns non-interchangeability in general. Targeted searches by index names, Hill orders, fixed richness, exact abundance vectors, and rank-reversal language did not locate the universal excess-\(6\) strict boundary, the excess-\(4\) tie boundary, or the complete first-layer classification.

Risk: a small witness pair could occur in an unindexed teaching example or software fixture.

## Value
**PASS.** Order \(1\) and order \(\infty\) are natural, widely interpretable points on the Hill diversity profile: one uses the full abundance distribution while the other sees only the dominant species. Fixing richness removes the most obvious confounder. The theorem quantifies the smallest amount of abundance heterogeneity needed before these two canonical summaries can make genuinely opposite community comparisons and identifies every minimal mechanism.

Self-review: passed. Independent audit: not yet performed.
