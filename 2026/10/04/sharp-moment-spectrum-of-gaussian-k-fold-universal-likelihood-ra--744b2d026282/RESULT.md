# Sharp moment spectrum of Gaussian \(K\)-fold universal likelihood-ratio e-values
## Finding
For iid \(N(0,1)\) observations split into \(K\ge2\) equal folds, let \(E_j\) be the universal likelihood-ratio e-value obtained by fitting the mean on the other \(K-1\) folds and evaluating it on fold \(j\), and let \(\bar E_K=K^{-1}\sum_{j=1}^K E_j\). Then for every real \(q\ge0\), \(\mathbb E[\bar E_K^q]<\infty\) if and only if \(q<q_K=(1+\sqrt{4K-3})/2\). In fact, \(\mathbb E[E_j^q]=(1-q(q-1)/(K-1))^{-1/2}\) exactly whenever finite. Consequently, \(\bar E_K\) has finite variance exactly for \(K\ge4\), and its integer \(p\)-th moment is finite exactly for \(K\ge p(p-1)+2\). For two-way cross-fitting with fold sizes \(n_0,n_1\), the critical exponent is \((1+\sqrt{1+4m})/2\), where \(m=\min\{n_0/n_1,n_1/n_0\}\), so the balanced split uniquely maximizes moment robustness and yields the golden-ratio boundary \((1+\sqrt5)/2\). Despite these raw-e-value heavy tails, \(\log \bar E_K\) has finite moments of every finite order.

## Assumptions and scope
Let \(Y_1,\ldots,Y_n\) be iid \(N(0,1)\), with \(K\ge2\) dividing \(n\), and let every fold have size \(s=n/K\). For fold \(j\), fit the Gaussian mean on the complement, obtaining \(\widehat\theta_{-j}\), and evaluate the likelihood ratio against the simple null mean \(0\) on the held-out fold:
\[
E_j=\exp\left\{s\widehat\theta_{-j}\overline Y_j-\frac{s}{2}\widehat\theta_{-j}^{2}\right\}.
\]
The averaged statistic is \(\bar E_K=K^{-1}\sum_{j=1}^K E_j\). The theorem concerns null moments of this statistic. It does not claim an optimal power choice of \(K\), nor does it cover estimated variance, non-Gaussian data, nuisance parameters, or overlapping/repeated random splits.

For the two-way extension, the two disjoint fold sizes are arbitrary positive integers \(n_0,n_1\), and the cross-fit statistic is the average of the two oriented held-out likelihood ratios.

## Proof
For each balanced fold define
\[
A_j=\sqrt{s}\,\overline Y_j,
\qquad
B_j=\frac{1}{\sqrt{K-1}}\sum_{\ell\ne j}A_\ell.
\]
The variables \(A_j\) and \(B_j\) are independent standard Gaussians. Since
\[
\widehat\theta_{-j}=\frac{1}{\sqrt{s}(K-1)}\sum_{\ell\ne j}A_\ell,
\]
direct substitution gives
\[
\log E_j=\frac{A_jB_j}{\sqrt{K-1}}-\frac{B_j^2}{2(K-1)}.
\]
Fix real \(q\ge0\). Conditional on \(B_j\), the standard-normal moment generating function yields
\[
\mathbb E[E_j^q\mid B_j]=\exp\left\{\frac{q(q-1)}{2(K-1)}B_j^2\right\}.
\]
Hence
\[
\mathbb E[E_j^q]=\left(1-\frac{q(q-1)}{K-1}\right)^{-1/2}
\]
when \(q(q-1)<K-1\), while the Gaussian square integral diverges when \(q(q-1)\ge K-1\). The positive root of \(q(q-1)=K-1\) is
\[
q_K=\frac{1+\sqrt{4K-3}}{2}.
\]

For \(q\ge1\), convexity gives
\[
\bar E_K^q\le\frac1K\sum_{j=1}^K E_j^q.
\]
Thus \(\mathbb E[\bar E_K^q]\) is finite whenever the component \(q\)-moments are finite. Conversely, positivity gives \(\bar E_K\ge E_j/K\), so divergence of one component \(q\)-moment forces divergence of the averaged \(q\)-moment. For \(0\le q\le1\), \(x^q\le1+x\) for \(x\ge0\), and \(\mathbb E[\bar E_K]=1\), so those moments are finite. This proves the exact spectrum.

Setting \(q=2\) shows that the variance is finite exactly when \(2<K-1\), namely \(K\ge4\). More generally, for an integer \(p\ge2\), strict integrability \(p(p-1)<K-1\) is equivalent to \(K\ge p(p-1)+2\).

For a two-way split, set \(r=n_0/n_1\). With independent standard Gaussians \(A_0,A_1\), the first oriented log e-value is
\[
\sqrt r\,A_0A_1-\frac r2 A_1^2,
\]
so its \(q\)-moment is finite exactly when \(r q(q-1)<1\). The reversed orientation replaces \(r\) by \(1/r\). The average therefore has finite \(q\)-moment exactly when
\[
q(q-1)<\min\{r,r^{-1}\}.
\]
The right side is at most \(1\), with equality only at \(r=1\). Thus balance uniquely maximizes the critical exponent and gives \(q=(1+\sqrt5)/2\).

Finally, each \(\log E_j\) is a quadratic polynomial in finitely many Gaussian fold means and hence has moments of every finite order. Because
\[
\min_j\log E_j\le\log\bar E_K\le\max_j\log E_j,
\]
we have \(|\log\bar E_K|\le\max_j|\log E_j|\), which proves all finite polynomial moments of the log statistic.

## Verification
The accompanying `verify.py` checks the Gaussian quadratic-form determinant underlying the component moment formula with exact rational arithmetic, verifies the strict integer-moment thresholds \(K\ge p(p-1)+2\), checks the golden-ratio boundary for \(K=2\), and confirms the balanced two-way split maximizes the critical exponent on an exact rational grid. It returns `VERIFY_OK`.

The proof itself is analytic: the verifier is a consistency check rather than a substitute for the Gaussian integral, convexity argument, or divergence proof.

## Relationship to prior work
Wasserman, Ramdas, and Balakrishnan introduced split universal likelihood-ratio inference and cross-fitting, and explicitly framed exponential moments of the log split statistic as a Chernoff-style object. Dunn, Ramdas, Balakrishnan, and Wasserman studied Gaussian universal likelihood-ratio variants, including cross-fitting and repeated splitting. Tse and Davison then studied the variance of cross-fit and \(K\)-fold likelihood-ratio averages in the Gaussian case; this is the closest direct predecessor located. A 2023 discussion by Wasserman, Ramdas, and Balakrishnan highlighted the infinite variance of the Gaussian cross-fit likelihood ratio and said its consequences were unclear, while suggesting the logarithm as the more relevant object.

The inspected articles do not state the all-real-order moment spectrum above, the threshold \(K\ge p(p-1)+2\) for integer moments, the golden-ratio cross-fit boundary, or the balanced-split optimality for moment integrability. These statements are elementary consequences of a Gaussian quadratic-form integral once the foldwise statistic is normalized, so older or differently phrased Gaussian quadratic-form literature may imply them abstractly; no historical priority beyond the stated literature comparison is claimed.

## Limitations
The result is exact only for the simple-null, known-unit-variance Gaussian mean model and the specified disjoint-fold construction. Finite moments do not imply good power, and increasing \(K\) can improve moment integrability while degrading power, as prior work has emphasized. The inaccessible supporting-information file for Tse and Davison was not inspected; the main article describes that supplement as deriving the \(K\)-fold variance, so a residual risk remains that it contains additional moment calculations not visible in the article. A negative literature search is not a proof of historical novelty.

## References
1. L. Wasserman, A. Ramdas, and S. Balakrishnan, “Universal Inference,” arXiv:1912.11436, first posted 2019-12-24; later PNAS 117 (2020), 16880–16890.
2. R. Dunn, A. Ramdas, S. Balakrishnan, and L. Wasserman, “Gaussian Universal Likelihood Ratio Testing,” arXiv:2104.14676, first posted 2021-04-29.
3. T. Tse and A. C. Davison, “A note on universal inference,” Stat 11 (2022), e501, DOI:10.1002/sta4.501.
4. L. Wasserman, A. Ramdas, and S. Balakrishnan, “A Discussion of ‘A Note on Universal Inference’ by Tse and Davison,” Stat 12 (2023), e573, DOI:10.1002/sta4.573.
