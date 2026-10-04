# Exact Gaussian law and fold-monotone variance of balanced K-fold cross-validation
## Finding
Let \(Y_1,\ldots,Y_n\) be iid \(N(\mu,\sigma^2)\), and fix a balanced partition into \(K\) folds, where \(2\le K\le n\) and \(K\mid n\). Write \(q=n/K\) for the fold size. For each observation, predict it by the sample mean computed from all observations outside its fold, and define \(\widehat R_K\) as the average squared prediction error over all \(n\) observations.

Then
\[
\frac{\widehat R_K}{\sigma^2}\overset{d}{=}\frac1n\left(X+\frac{K^2}{(K-1)^2}Z\right),
\]
where \(X\sim\chi^2_{n-K}\) and \(Z\sim\chi^2_{K-1}\) are independent; for \(K=n\), \(X\) is the degenerate zero variable. Therefore
\[
\mathbb E\widehat R_K=\sigma^2\left(1+\frac{K}{n(K-1)}\right)
\]
and
\[
\operatorname{Var}(\widehat R_K)=\frac{2\sigma^4}{n^2}\left(n-K+\frac{K^4}{(K-1)^3}\right).
\]
The expectation is exactly the prediction risk for a fresh \(N(\mu,\sigma^2)\) observation when the predictor is a sample mean trained on \(n(K-1)/K\) observations. The variance is strictly decreasing as a function of real \(K>1\). Hence, among the balanced divisors of \(n\), leave-one-out cross-validation has the smallest sampling variance for its corresponding training-size risk target.

This conclusion does not rely on independence of the held-out errors. In fact, if \(e_i\) is the squared held-out error, then distinct observations in the same fold have covariance \(2\sigma^4/m^2\), while observations in different folds have covariance
\[
\frac{2\sigma^4K^4}{n^2(K-1)^4},
\]
where \(m=n(K-1)/K\) is the training size. Both are positive.

## Assumptions and scope
The partition is fixed and balanced. Because the observations are iid, the same conditional law holds for a random balanced partition chosen independently of the data. The fitting rule is the intercept-only least-squares predictor, equivalently the training-sample mean, and the loss is squared error. The comparison across \(K\) concerns the raw cross-validation score at its natural training size \(n(K-1)/K\); different values of \(K\) therefore estimate slightly different prediction risks. No claim is made that leave-one-out minimizes mean-squared error for a common full-sample target, for general regression, or for non-Gaussian data.

## Proof
For fold \(k\), let \(\bar Y_k\) be its mean, let \(\bar Y\) be the overall mean, and let \(\bar Y_{-k}\) be the mean outside the fold. Define the within-fold and between-fold sums of squares
\[
W=\sum_{k=1}^K\sum_{i\in F_k}(Y_i-\bar Y_k)^2,
\qquad
B=q\sum_{k=1}^K(\bar Y_k-\bar Y)^2.
\]
For \(i\in F_k\), the cross term vanishes after summing within the fold, and
\[
\bar Y_k-\bar Y_{-k}=\frac{K}{K-1}(\bar Y_k-\bar Y).
\]
Consequently the cross-validation score has the deterministic ANOVA decomposition
\[
n\widehat R_K=W+\frac{K^2}{(K-1)^2}B.
\]
Under Gaussian sampling, orthogonal ANOVA decomposition gives
\[
\frac W{\sigma^2}\sim\chi^2_{n-K},
\qquad
\frac B{\sigma^2}\sim\chi^2_{K-1},
\qquad
W\perp B.
\]
This proves the distributional identity. Taking the first two moments of independent chi-square variables yields the displayed expectation and variance.

For monotonicity, set
\[
g(K)=n-K+\frac{K^4}{(K-1)^3}.
\]
A direct derivative calculation gives
\[
g'(K)=-1+\frac{K^3(K-4)}{(K-1)^4}
=-\frac{6K^2-4K+1}{(K-1)^4}<0
\]
for every real \(K>1\), since \(6K^2-4K+1\) has negative discriminant and positive leading coefficient.

For the covariance statement, let \(r_i=Y_i-\bar Y_{-k}\) for \(i\in F_k\). The vector of residuals is jointly Gaussian. Distinct residuals in the same fold have covariance \(\sigma^2/m\), whereas residuals from different folds have covariance \(-\sigma^2K^2/[n(K-1)^2]\). The identity \(\operatorname{Cov}(U^2,V^2)=2\operatorname{Cov}(U,V)^2\) for centered jointly Gaussian variables gives the two positive squared-error covariances above.

## Verification
The accompanying `verify.py` checks, using exact rational arithmetic, the deterministic fold decomposition on many balanced sizes and folds, the expectation simplification, the variance coefficient, the derivative identity proving strict monotonicity, the leave-one-out specialization, and the same-fold/different-fold covariance algebra. It terminates with `VERIFY_OK` when every check passes.

The probabilistic step that \(W/\sigma^2\) and \(B/\sigma^2\) are independent chi-square variables is the standard Gaussian one-way ANOVA orthogonal decomposition; the checker does not replace that theorem with simulation.

## Relationship to prior work
Haberman (2019) studies cross-validation through U-statistics, includes the sample mean as a basic example, and explicitly discusses traditional \(K\)-fold replication. The inspected relevant sections provide holdout/sample-mean variance formulas and an incomplete-U-statistic treatment, but they do not state the balanced Gaussian \(K\)-fold weighted-chi-square law above or its strict variance monotonicity in \(K\). Bates, Hastie, and Tibshirani (2021) emphasize that cross-validation targets average prediction error and that dependence across fold errors invalidates naive independent-error variance calculations; their inspected text likewise does not give this exact intercept-only distribution or the fold-monotonic variance formula.

The present result is therefore a finite-sample benchmark: positive dependence among fold errors does not by itself imply that the sampling variance of the cross-validation point estimate rises with the number of folds. This does not contradict general impossibility or undercoverage results for estimating cross-validation variance, which concern much broader classes of learning procedures and data distributions.

## Limitations
The exact law uses Gaussianity and the intercept-only sample-mean predictor. The strict variance comparison changes the natural training-size target with \(K\), so it is not a comparison at one fixed estimand. The targeted literature searches and direct source inspections did not locate the same weighted-chi-square law or monotonicity theorem, but that is not a proof that no older or differently worded source contains an equivalent specialization.

## References
1. Shelby J. Haberman, “Cross-Validation and U-Statistics,” ETS Research Report Series (2019), DOI: 10.1002/ets2.12263. First published 2019-06-26.
2. Stephen Bates, Trevor Hastie, Robert Tibshirani, “Cross-validation: what does it estimate and how well does it do it?”, arXiv:2104.00673 (first submitted 2021-04-01), later Journal of the American Statistical Association, DOI: 10.1080/01621459.2023.2197686.
