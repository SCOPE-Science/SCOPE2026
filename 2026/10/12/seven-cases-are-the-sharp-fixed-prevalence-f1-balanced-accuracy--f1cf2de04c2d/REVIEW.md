# Self-review

## Correctness
**PASS.** At fixed total \(N\) and prevalence \(P\), every strictly positive confusion matrix is uniquely determined by \(a=TP\) and \(b=FP\), with \(1\le a\le P-1\) and \(1\le b\le N-P-1\). The formulas reduce exactly to \(F_1=2a/(P+a+b)\) and \(B=\frac12(1+a/P-b/(N-P))\). Exhaustive rational comparison gives no strict reversal through \(N=6\), exactly one weak tie split at \(N=6\), and exactly three strict reversals at \(N=7\). The packaged verifier returns `VERIFY_OK`.

Risk: allowing zero cells or changing prevalence between classifiers changes the domain and can change the boundary.

## Originality
**PASS.** Prior work already establishes that F-measure can disagree with Informedness, and balanced accuracy is affine-equivalent to Informedness. Generic disagreement is therefore not claimed as new. The checked literature and database searches did not state the smallest strictly positive fixed-prevalence sample size, the six-case tie boundary, or the complete three-pair seven-case strict layer.

Risk: an unindexed teaching example or software test could contain one of the seven-case matrices without identifying the minimality theorem.

## Value
**PASS.** F1 and balanced accuracy are both common single-number summaries for binary classifiers, especially under imbalance, but they weight the negative class differently. Fixing both sample size and prevalence removes the most immediate comparability objections. The sharp boundary gives the smallest possible fully nondegenerate data set on which the two metrics can recommend opposite classifiers, together with every minimal mechanism.

Self-review: passed. Independent audit: not yet performed.
