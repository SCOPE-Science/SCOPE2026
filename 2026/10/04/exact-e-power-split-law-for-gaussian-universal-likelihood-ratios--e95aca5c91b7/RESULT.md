# Exact e-power split law for Gaussian universal likelihood ratios
## Finding
For iid \(N(\mu,1)\) data of total size \(n\ge2\), form the one-split Gaussian universal likelihood-ratio e-value by fitting the mean on \(m\in\{1,\ldots,n-1\}\) training observations and evaluating that fitted mean against the simple null \(\mu=0\) on the remaining \(n-m\) observations. Its e-power is exactly \((n-m)(\mu^2-1/m)/2\). Hence the maximizing integer training size is characterized by \(n/[m(m+1)]\le\mu^2\le n/[(m-1)m]\) for interior \(m\), with the evident one-sided boundary conditions; adjacent maximizers occur only at an equality. Positive oracle e-power is possible exactly when \(\mu^2>1/(n-1)\). Under local alternatives \(\mu_n=h/\sqrt n\), every maximizing split satisfies \(m_n/n\to1/|h|\) and the maximal e-power converges to \((|h|-1)^2/2\) when \(|h|>1\), while \(m_n/n\to1\) and maximal e-power converges to \(0\) when \(|h|\le1\). For fixed nonzero \(\mu\), \(m_n=\sqrt n/|\mu|+O(1)\) and the maximal e-power is \(n\mu^2/2-\sqrt n|\mu|+O(1)\), so e-power-optimal splitting uses a vanishing training fraction even though published power- and confidence-radius-based split criteria commonly favor nonvanishing fractions.

## Assumptions and scope
Let \(Y_1,\ldots,Y_n\) be independent \(N(\mu,1)\) observations, with known unit variance and \(n\ge2\). Choose a training set of size \(m\in\{1,\ldots,n-1\}\), let \(\widehat\mu\) be its sample mean, and let \(\overline Y_0\) be the mean of the independent evaluation set of size \(k=n-m\). The split likelihood-ratio e-value for the simple null \(H_0:\mu=0\) is
\[
E_m=\exp\left\{k\widehat\mu\overline Y_0-\frac{k}{2}\widehat\mu^2\right\}.
\]
The quantity optimized here is e-power, \(\mathbb E_\mu[\log E_m]\). It is an expected-log-growth criterion, not the rejection probability at a fixed threshold and not confidence-set width. The split is treated as a design choice informed by the alternative magnitude; no data-dependent post hoc choice of \(m\) is claimed to preserve validity.

## Proof
Under the null, conditional on the training estimate, \(\overline Y_0\sim N(0,1/k)\), so
\[
\mathbb E_0[E_m\mid\widehat\mu]
=\exp\left(-\frac{k}{2}\widehat\mu^2\right)
\mathbb E_0\exp(k\widehat\mu\overline Y_0)=1.
\]
Thus \(E_m\) is an exact e-value for the simple Gaussian null.

Under the true mean \(\mu\), independence of the two data parts gives \(\mathbb E_\mu[\widehat\mu\overline Y_0]=\mu^2\) and \(\mathbb E_\mu[\widehat\mu^2]=\mu^2+1/m\). Therefore
\[
G_n(m,\mu):=\mathbb E_\mu[\log E_m]
=\frac{n-m}{2}\left(\mu^2-\frac1m\right).
\]
The exact forward difference is
\[
G_n(m+1,\mu)-G_n(m,\mu)
=\frac12\left(\frac{n}{m(m+1)}-\mu^2\right).
\]
Because \(n/[m(m+1)]\) is strictly decreasing in \(m\), the sequence \(m\mapsto G_n(m,\mu)\) is unimodal. For \(2\le m\le n-2\), an integer \(m\) is maximizing exactly when
\[
\frac{n}{m(m+1)}\le\mu^2\le\frac{n}{(m-1)m}.
\]
For \(m=1\), only the left inequality is needed, namely \(\mu^2\ge n/2\); for \(m=n-1\), only the right inequality is needed, namely \(\mu^2\le n/[(n-2)(n-1)]\) when \(n>2\). Equality in a forward difference gives the only possible two-point tie. Since \(G_n(m,\mu)>0\) exactly when \(m>1/\mu^2\), some admissible split has positive e-power exactly when \(\mu^2>1/(n-1)\).

For the local sequence \(\mu_n=h/\sqrt n\), the interior balance equation is \(m(m+1)\asymp n^2/h^2\). If \(|h|>1\), any maximizer satisfies \(m_n/n\to1/|h|\), and substitution gives
\[
G_n(m_n,\mu_n)\longrightarrow\frac{(|h|-1)^2}{2}.
\]
If \(|h|\le1\), the continuous optimum lies at or beyond the boundary and the maximizing integer satisfies \(m_n/n\to1\); the maximal e-power tends to \(0\). For fixed \(\mu\ne0\), the same threshold characterization gives \(m_n=\sqrt n/|\mu|+O(1)\), and substitution yields
\[
\max_m G_n(m,\mu)=\frac{n\mu^2}{2}-\sqrt n|\mu|+O(1).
\]

## Verification
The accompanying `verify.py` checks the exact forward-difference identity, exhaustively compares the threshold characterization with brute-force maximization for a deterministic grid of \(n\) and \(\mu\), checks the positivity threshold, and checks the local and fixed-signal asymptotics numerically. The proof itself is algebraic; the computations are consistency checks rather than substitutes for the argument.

As concrete values, when \(n=1000\) and \(\mu=0.1\), the maximizing training size is \(m=316\), with e-power approximately \(2.337721519\), compared with \(2.000000000\) for the half split. When \(n=10000\) and \(\mu=0.05\), the maximizer is \(m=2000\), with e-power \(8\), compared with \(5.75\) for the half split.

## Relationship to prior work
Wasserman, Ramdas, and Balakrishnan introduced universal inference and the split likelihood ratio, using equal splits for the basic exposition. Dunn, Ramdas, Balakrishnan, and Wasserman analyzed the Gaussian universal likelihood-ratio test and optimized a different quantity: expected squared confidence-set radius. Tse and Davison derived exact rejection power for the scalar Gaussian split test and studied how that power changes with the split proportion. Strieder and Drton optimized asymptotic rejection power under local alternatives. A later paper by Delong and Wüthrich explicitly treats expected log e-values as e-power and studies training/validation splitting in a broader mean-calibration problem, but its inspected split-ratio analysis is numerical and tied to isotonic calibration rather than the scalar Gaussian-location law above.

These criteria are not equivalent. In particular, the present fixed-signal e-power optimizer has training fraction tending to \(0\), whereas the published rejection-power and confidence-radius analyses generally use nonvanishing split fractions. A prior Gaussian universal-inference result on the same data model established the null moment spectrum of cross-fitted and \(K\)-fold averaged e-values; that result concerns null tail robustness and explicitly does not optimize alternative e-power.

## Limitations
The result assumes known variance, a scalar Gaussian location model, a simple null, and one deterministic split size. It does not say that an e-power-optimal split maximizes finite-threshold rejection probability. It does not justify choosing \(m\) after looking at the same observations. The 2025 mean-calibration preprint is a residual overlap risk because it studies e-power and sample splitting in a broader exponential-dispersion setting; the inspected material did not state this exact Gaussian integer optimizer, the \(|h|=1\) local phase boundary, or the fixed-signal vanishing-training-fraction law.

## References
1. L. Wasserman, A. Ramdas, and S. Balakrishnan, “Universal Inference,” arXiv:1912.11436, first posted 2019-12-24.
2. R. Dunn, A. Ramdas, S. Balakrishnan, and L. Wasserman, “Gaussian Universal Likelihood Ratio Testing,” arXiv:2104.14676; Biometrika, DOI 10.1093/biomet/asac064.
3. T. Tse and A. C. Davison, “A note on universal inference,” Stat 11 (2022), e501, DOI 10.1002/sta4.501.
4. D. Strieder and M. Drton, “On the choice of the splitting ratio for the split likelihood ratio test,” arXiv:2203.06748; Electronic Journal of Statistics 16 (2022), 6631–6650.
5. Ł. Delong and M. Wüthrich, “Universal Inference for Testing Calibration of Mean Estimates within the Exponential Dispersion Family,” arXiv:2510.23821, first posted 2025-10-27.
