# Same-model review

## Correctness
PASS. The leave-one-fold-out algebra gives \(\widehat\mu_i-\mu=\sigma(S-Z_i)/(\sqrt m(B-1))\). The range identity is exact. The vector \((S-Z_i)\) is equicorrelated with correlation \((B-2)/(B-1)\), yielding the stated conditional-normal integral. Orthogonal Gaussian decomposition separates the grand-mean coordinate from centered residuals and reduces coverage to a Taylor expansion whose remainder is lower order by standard Gaussian extreme-value moment bounds. The finite numerical anchors are replayed by the supplied verifier.

## Originality
PASS, with a stated residual literature risk. The direct HulC source explicitly assumes independent estimators from disjoint batches and uses that independence in its coverage lemma. Targeted searches for HulC with dependent, overlapping, leave-one-out, leave-one-fold-out, and K-fold estimators did not locate this result. Classical equicorrelated-normal orthant theory covers the probability integral after covariance reduction, but not the leave-one-fold-out confidence-hull mapping, the exact samplewise \(B-1\) width shrinkage, or the combined vanishing-coverage law. The closest database hit on deletion dependence concerns jackknife pseudo-values and does not imply this confidence-hull theorem.

## Value
PASS. Reusing \(B-1\) folds per estimator is a natural attempt to avoid the apparent inefficiency of disjoint splitting. The theorem shows that this seemingly attractive modification can make a confidence interval deterministically much narrower while destroying calibration, and quantifies both effects exactly. The result therefore gives a concrete diagnostic for why the source method's independence condition matters.

## Closest literature and limitations
The HulC paper is the method source; Steck's equicorrelated-normal orthant paper is the main classical probability antecedent. The theorem is restricted to equal-fold Gaussian location data and one explicit reuse rule. It does not claim failure of the published HulC algorithm or a universal result for dependent convex-hull intervals. An older dependent-confidence-region formulation under different terminology remains a residual originality risk.

Same-model review: passed. Independent audit: not yet performed.
