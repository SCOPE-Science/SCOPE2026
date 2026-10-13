# Self-review

## Correctness
**PASS.** At fixed prevalence, balanced accuracy is the arithmetic mean of sensitivity and specificity and squared G-mean is their product. The exact identity \(G^2=B^2-\delta^2\) is immediate after writing \(\delta=|s-c|/2\). The above-chance condition is exactly \(TP\,TN>FP\,FN\). Exhaustive exact-rational enumeration covers every positive-cell table and every same-\((N,P)\) unordered pair through \(N=11\), proving no strict reversal through ten cases and exactly six at eleven. The packaged verifier returns `VERIFY_OK`.

Risk: the finite cutoff changes if zero cells or chance-or-worse classifiers are admitted.

## Originality
**PASS.** Kubat–Matwin establish the sensitivity-specificity G-mean, Brodersen et al. establish balanced accuracy, and later comparative literature directly contrasts arithmetic and geometric class-accuracy aggregation and gives tie-splitting examples. Generic non-equivalence is therefore prior art. The checked primary material, exact-witness searches, database searches, and prior-file deduplication did not state or imply the sharp above-chance fixed-prevalence cutoff \(N=11\) or the complete first strict layer.

Risk: an unindexed tutorial or unit test could contain a witness without presenting the minimality theorem.

## Value
**PASS.** Balanced accuracy and G-mean are canonical class-balanced summaries used specifically when ordinary accuracy can be misleading. Their distinction is often described qualitatively as arithmetic versus geometric aggregation. The smallest above-chance fixed-prevalence reversal gives an exact operational limit on interchangeability, and the identity \(G^2=B^2-\delta^2\) identifies the mechanism: sufficiently unequal class accuracies can overturn a higher balanced accuracy.

Self-review: passed. Independent audit: not yet performed.
