# Same-model review

## Correctness
PASS. The deterministic identity \(n\widehat R_K=W+K^2B/(K-1)^2\) follows fold by fold from centering. Standard Gaussian ANOVA makes \(W/\sigma^2\) and \(B/\sigma^2\) independent chi-square variables with degrees of freedom \(n-K\) and \(K-1\). Their moments yield the stated expectation and variance. Differentiation gives \(-[6K^2-4K+1]/(K-1)^4\), which is strictly negative for \(K>1\). Exact-arithmetic replay in `verify.py` checks all algebraic identities and deterministic decompositions.

## Originality
PASS with a recorded residual risk. Direct inspection of Haberman (2019) covered the sample-mean examples, the variance discussion, and the traditional \(K\)-fold replication section; the inspected material does not state the exact balanced Gaussian weighted-chi-square law or strict monotonicity in \(K\). Bates, Hastie, and Tibshirani (2021) discuss the estimand of cross-validation and dependence among fold errors, but the inspected full text contains no intercept-only/sample-mean or chi-square specialization. Multiple published-finding corpus searches using the distributional form, ANOVA aliases, and the leave-one-out monotonicity consequence returned no equivalent record. An older or differently worded equivalent remains possible.

## Value
PASS. Cross-validation variance is a practical inferential quantity whose dependence on fold count is often discussed qualitatively. This result gives a sharp finite-sample benchmark in the simplest nontrivial Gaussian prediction model: the fold errors are positively dependent, yet the pooled point-estimate variance decreases with the number of folds. The theorem cleanly separates “correlation makes the naive independent-error standard error wrong” from the different statement “more folds must increase the true sampling variance.”

## Closest literature and limitations
Haberman (2019) is the closest inspected direct predecessor because it explicitly combines the sample-mean predictor with cross-validation and traditional \(K\)-fold replication. Bates, Hastie, and Tibshirani (2021) are closest on the modern estimand/dependence interpretation. The result is deliberately narrow: Gaussian location, balanced folds, squared loss, and a moving natural training-size risk target.

Same-model review: passed. Independent audit: not yet performed.
