# Exact empty-set saturation of signed CQR in noiseless variable-width regression
## Finding
Consider split conformalized quantile regression (CQR) with a calibration sample of size \(m\ge 1\) and \(\alpha\in[1/(m+1),1)\). Conditional on the proper-training sample, suppose the fitted endpoints are
\[
\hat q_{\rm lo}(x)=c(x)-w(x),\qquad \hat q_{\rm hi}(x)=c(x)+w(x),
\]
while the response is noiseless: \(Y=c(X)\). Assume \(W=w(X)>0\) has a continuous distribution and the calibration and test points are iid. Define
\[
r=\lfloor\alpha(m+1)\rfloor.
\]
Then the signed CQR correction is exactly \(-W_{(r)}\), with \(W_{(r)}\) the \(r\)-th smallest calibration width, and the CQR output at a test point is
\[
C(X)=[\,c(X)-W+W_{(r)},\ c(X)+W-W_{(r)}\,].
\]
Hence \(C(X)=\varnothing\) exactly when \(W<W_{(r)}\), and otherwise \(Y=c(X)\in C(X)\). In particular,
\[
\Pr\{C(X)=\varnothing\}=\frac{\lfloor\alpha(m+1)\rfloor}{m+1},\qquad
\Pr\{Y\in C(X)\}=\frac{\lceil(1-\alpha)(m+1)\rceil}{m+1}.
\]
If \(F\) is the CDF of \(W\) and \(u=F(W)\), then the conditional coverage is exactly
\[
\Pr\{Y\in C(X)\mid F(W)=u\}=\Pr\{\operatorname{Bin}(m,u)\ge r\}.
\]
For fixed \(\alpha\), this converges to \(0\) for every \(u<\alpha\) and to \(1\) for every \(u>\alpha\) as \(m\to\infty\). Thus a global signed conformal correction can concentrate essentially all marginal miscoverage on the lowest-width covariate stratum, even though the center is exact and there is no response noise.

## Assumptions and scope
The statement concerns the original split CQR score and additive conformal correction of Romano, Patterson, and Candès. The proper-training data are conditioned upon, so the fitted functions \(c\) and \(w\) are fixed during calibration. The theorem assumes that the resulting data-generating model satisfies \(Y=c(X)\) and that the fitted endpoints are symmetric around this exact response with strictly positive width \(w(X)\). Continuity of \(W=w(X)\) removes ties. The lower bound \(\alpha\ge 1/(m+1)\) ensures that the finite calibration quantile appearing in the original empirical-quantile convention exists without adding an infinite sentinel.

The result does not assert that ordinary CQR commonly returns empty intervals in typical applications. It identifies an exact finite-sample mechanism in a clean overcoverage regime where all signed conformity scores are negative. It also does not claim distribution-free conditional coverage; the conditional formula is derived for this explicit model.

## Proof
For every calibration point, the CQR score of Romano, Patterson, and Candès is
\[
E_i=\max\{\hat q_{\rm lo}(X_i)-Y_i,\ Y_i-\hat q_{\rm hi}(X_i)\}.
\]
Under \(Y_i=c(X_i)\) and \(\hat q_{\rm lo}=c-w\), \(\hat q_{\rm hi}=c+w\), both arguments equal \(-W_i\), so
\[
E_i=-W_i.
\]
Their correction is the empirical quantile at level \((1-\alpha)(1+1/m)\). Appendix A of the source gives the empirical quantile as the \(\lceil tm\rceil\)-th smallest observation at level \(t\). Therefore the correction is the \(k\)-th smallest score with
\[
k=\lceil(1-\alpha)(m+1)\rceil=m+1-r.
\]
Ordering \(-W_i\) reverses the width order, hence
\[
E_{(k)}=-W_{(m+1-k)}=-W_{(r)}.
\]
Substitution into the CQR output formula gives
\[
C(X)=[\,c(X)-W+W_{(r)},\ c(X)+W-W_{(r)}\,].
\]
Its lower endpoint is no larger than its upper endpoint exactly when \(W\ge W_{(r)}\). In that case both endpoints straddle \(c(X)=Y\); when \(W<W_{(r)}\), the lower endpoint exceeds the upper endpoint, so the set is empty.

Among the \(m\) calibration widths and one test width, continuity makes all \(m+1\) ranks equiprobable. The test width is smaller than the calibration \(r\)-th order statistic exactly when its rank among all \(m+1\) widths is at most \(r\). Thus
\[
\Pr\{C(X)=\varnothing\}=\frac r{m+1},
\]
and the complementary coverage probability is \((m+1-r)/(m+1)\), equal to \(\lceil(1-\alpha)(m+1)\rceil/(m+1)\).

For the conditional formula, fix a test width with \(F(W)=u\). The number of calibration widths not exceeding the test width is \(\operatorname{Bin}(m,u)\). Coverage is equivalent to at least \(r\) such widths, proving
\[
\Pr\{Y\in C(X)\mid F(W)=u\}=\Pr\{\operatorname{Bin}(m,u)\ge r\}.
\]
Finally \(r/m\to\alpha\). The weak law of large numbers for the binomial count yields the stated \(0\)-or-\(1\) limit for \(u\ne\alpha\).

## Verification
A standalone checker enumerates every possible test rank for multiple calibration sizes and miscoverage levels. It independently constructs the signed scores, selects the source paper's finite-sample order statistic, builds the CQR endpoints, and confirms that emptiness occurs exactly for the first \(r\) ranks and that the response is covered for the remaining ranks. It also checks the exact \(m=99\), \(\alpha=0.1\) frequency and evaluates the conditional binomial probabilities.

For \(m=99\) and \(\alpha=0.1\), \(r=10\): the empty-set probability is exactly \(0.1\). At width quantiles \(u=0.05,0.10,0.15\), the exact conditional coverage probabilities are approximately \(0.0265167058\), \(0.5355232999\), and \(0.9404700914\), respectively.

## Relationship to prior work
Romano, Patterson, and Candès define the signed CQR score and the additive correction, explicitly noting that a response inside the plug-in interval has a non-positive score. Their Theorem 1 proves finite-sample marginal coverage, and Appendix A specifies the order-statistic quantile convention. The same paper emphasizes that signed scores can mitigate overcoverage and shorten overly conservative quantile-regression bands. The inspected full text contains no discussion of empty CQR outputs or the exact rank law above.

Sesia and Candès compare CQR variants and emphasize that conformal coverage is marginal rather than conditional. They describe the same additive CQR correction and study asymptotic efficiency and empirical width, but the inspected full text does not derive an empty-set probability or the binomial conditional profile above. Sousa, Tomé, and Moreira explicitly discuss negative CQR corrections as band shrinkage and motivate clustered calibration because the global step lacks adaptiveness; their inspected full text likewise contains no empty-set calculation. General impossibility results for distribution-free conditional predictive inference explain why marginal validity need not imply conditional validity, but they do not imply this exact CQR-specific finite-sample law.

## Limitations
The construction is deliberately idealized: the center is exact, the response is deterministic given \(X\), and the fitted half-width \(w(X)\) is assumed continuous. These assumptions isolate the signed-score shrinkage mechanism rather than model-fitting error. The theorem concerns the additive CQR method and does not automatically transfer to multiplicative, locally calibrated, clustered, or other conformal variants. With ties in \(W\), the exact rank probabilities change and require tie accounting. At the boundary \(u=\alpha\), the limiting conditional coverage depends on central binomial fluctuations and is not claimed here.

## References
1. Romano, Y., Patterson, E., and Candès, E. J. *Conformalized Quantile Regression*. arXiv:1905.03222v1, 8 May 2019. Equations (14)--(16), Theorem 1, Appendix A.
2. Sesia, M., and Candès, E. J. *A comparison of some conformal quantile regression methods*. arXiv:1909.05433v1, 12 September 2019; Stat 9(1), e261 (2020).
3. Sousa, M., Tomé, A. M., and Moreira, J. *Improved conformalized quantile regression*. arXiv:2207.02808, 2022.
4. Barber, R. F., Candès, E. J., Ramdas, A., and Tibshirani, R. J. *The limits of distribution-free conditional predictive inference*. arXiv:1903.04684, 2019; Information and Inference 10(2), 455--482 (2021).
