# Strict Dirichlet-concentration ordering of Hilbert distances in every simplex

## Finding
Let \(S\) be the interior of any nondegenerate Euclidean \(d\)-simplex, \(d\geq1\). Equip \(S\) with the Hilbert distance \(h_S\) defined as the **logarithm of the full boundary cross-ratio** (without a factor of one-half). For each \(\alpha>0\), independently sample \(X_\alpha,Y_\alpha\in S\) so that their barycentric coordinate vectors have the symmetric Dirichlet distribution with parameter \(\alpha\) on each of the \(d+1\) coordinates, and set \(D_\alpha=h_S(X_\alpha,Y_\alpha)\). Then for every \(0<\alpha<\beta\) and every finite \(r>0\),

\[
\Pr(D_\alpha\leq r)<\Pr(D_\beta\leq r).
\]

This strict stochastic comparison holds in **every dimension and for every simplex shape**, at every positive threshold. The proof yields an explicit additive-noise coupling: if \(L_\alpha\) has density
\[
 f_\alpha(x)=\frac{\Gamma(2\alpha)}{\Gamma(\alpha)^2}[2\cosh(x/2)]^{-2\alpha},\qquad x\in\mathbb R,
\]
then for \(\alpha<\beta\), independently of \(L_\beta\),
\[
L_\alpha\ \overset{\mathrm d}=\ L_\beta+\sum_{k=0}^{\infty}B_kV_k,
\]
where \(B_k\) are independent Bernoulli variables with success probabilities \(1-(\alpha+k)^2/(\beta+k)^2\), \(V_k\) are independent centered Laplace variables of rates \(\alpha+k\), and all variables are mutually independent. The series converges almost surely and in mean square.

The distance law is the range of \(d+1\) independent copies of \(L_\alpha\). Consequently, with \(m=d+1\) and \(G_\alpha\) its distribution function,
\[
\Pr(D_\alpha\le r)=m\int_{-\infty}^{\infty} f_\alpha(x)[G_\alpha(x+r)-G_\alpha(x)]^{m-1}\,dx,\quad r\geq0,
\]
where \(G_\alpha(x)=I_{(1+e^{-x})^{-1}}(\alpha,\alpha)\), the regularized incomplete beta function. At \(\alpha=1\) the sampling is uniform Euclidean volume and the classical logistic-range identity gives \(\mathbb E D_1=2H_d\), where \(H_d=\sum_{j=1}^{d}1/j\). For fixed \(d\) and \(r>0\), the displayed distribution probability tends to \(0\) as \(\alpha\downarrow0\) and to \(1\) as \(\alpha\to\infty\).

## Assumptions and scope
The simplex is open and full-dimensional in its affine span; sampling almost surely avoids its boundary. The symmetric Dirichlet law is defined in barycentric coordinates, not by assigning an intrinsic Hilbert-volume measure. The metric convention is the full logarithmic cross-ratio; under the alternative half-cross-ratio convention every distance and every threshold scales by one-half. All probabilistic independence stated above is genuine. The result does not compare nonsymmetric Dirichlet vectors or sampling measures outside this family.

## Proof
**1. Metric and gamma reduction.** The projective simplex distance formula (also derivable by intersecting the line through two points with the simplex facets) is
\[
h_S(x,y)=\max_i\log\frac{\lambda_i(x)}{\lambda_i(y)}-\min_i\log\frac{\lambda_i(x)}{\lambda_i(y)},
\]
where \(\lambda_i\) are positive barycentric coordinates and \(i\) runs through \(1,\ldots,m\). Sample independent \(A_i,B_i\sim\operatorname{Gamma}(\alpha,1)\) and set \(\lambda_i(X_\alpha)=A_i/\sum_jA_j\), \(\lambda_i(Y_\alpha)=B_i/\sum_jB_j\). The normalizing sums contribute a common additive constant to every logarithm, which cancels from its range. Hence \(D_\alpha\) is the range of the independent variables \(L_i=\log(A_i/B_i)\). A change of variables in the beta-prime density gives \(f_\alpha\) as displayed; it is positive, even, real analytic, and strictly log-concave since
\[
 (\log f_\alpha)''(x)=-\frac\alpha2\operatorname{sech}^2(x/2)<0.
\]
The standard minimum-order-statistic density formula yields the stated one-dimensional CDF integral, with \(G_\alpha\) obtained by beta-ratio transformation.

**2. Nondegenerate additive-noise ordering.** The Euler product for the gamma function yields the characteristic function
\[
\phi_\alpha(t)=\mathbb E e^{itL_\alpha}=\prod_{k=0}^{\infty}\left(1+\frac{t^2}{(\alpha+k)^2}\right)^{-1}.
\]
Write \(a_k=\alpha+k\), \(b_k=\beta+k\), and \(c_k=a_k^2/b_k^2\). For an independent Bernoulli\((1-c_k)\) variable \(B_k\) and a centered Laplace(rate \(a_k\)) variable \(V_k\),
\[
\mathbb E e^{itB_kV_k}=c_k+(1-c_k)\frac{a_k^2}{a_k^2+t^2}=\frac{1+t^2/b_k^2}{1+t^2/a_k^2}.
\]
The noise terms have mean zero and their total variance is
\[
\sum_{k\ge0}\frac{2(1-c_k)}{a_k^2}=2\sum_{k\ge0}\left(\frac1{a_k^2}-\frac1{b_k^2}\right)<\infty.
\]
Thus their independent sum converges almost surely and in \(L^2\). Multiplication of characteristic functions gives \(\phi_\alpha=\phi_\beta\prod_k\mathbb E e^{itB_kV_k}\), proving the coupling. Its independent coordinate copies provide the vector relation \(\mathbf L_\alpha\overset{\mathrm d}=\mathbf L_\beta+\mathbf Z\). Every coordinate noise is nondegenerate, so \(\mathbf Z\) is not almost surely a multiple of the all-ones vector.

**3. A strict convex-set probability comparison.** Let \(C_r=\{x\in\mathbb R^m:\max_i x_i-\min_i x_i\le r\}\). This is closed, centrally symmetric, convex, and invariant under common-coordinate translation. If \(\mathbf W\) has independent density \(f_\beta\), define \(g_z(t)=\Pr(\mathbf W+t z\in C_r)\). The product density is symmetric and log-concave. The Prékopa marginal log-concavity theorem applied to the joint log-concave integrand \(\mathbf1_{C_r}(x)\prod_i f_\beta(x_i-tz_i)\) shows that \(g_z\) is log-concave. Symmetry makes it even, so \(g_z(t)\le g_z(0)\).

For completeness, the comparison is **strict** whenever \(z\) is not constant across coordinates. The density \(f_\beta\) has a holomorphic continuation to a strip around the real axis with exponential decay in its real argument; dominated local holomorphic integration therefore makes \(g_z(t)\) real analytic in \(t\). If equality \(g_z(1)=g_z(0)\) held, evenness and log-concavity would force \(g_z\) to be constant on an interval, hence everywhere by analyticity. But for any pair \(i,j\) with \(z_i\ne z_j\), the event in \(C_r\) implies \(|W_i-W_j+t(z_i-z_j)|\le r\); its probability tends to zero as \(t\to\infty\), a contradiction. Therefore \(g_z(1)<g_z(0)\). Conditioning on \(\mathbf Z\) from step 2 and then averaging proves \(\Pr(D_\alpha\le r)<\Pr(D_\beta\le r)\) for every \(r>0\).

**4. Limits and Euclidean-volume baseline.** As \(\alpha\to\infty\), \(\operatorname{Var}(L_\alpha)=2\psi_1(\alpha)\to0\); a finite range converges to zero in probability. As \(\alpha\downarrow0\), \(\|f_\alpha\|_\infty=f_\alpha(0)\sim\alpha/2\); since the difference of two independent variables of density \(f_\alpha\) has density bounded by \(\|f_\alpha\|_\infty\), one has \(\Pr(D_\alpha\le r)\le2r f_\alpha(0)\to0\). At \(\alpha=1\), \(L_1\) is standard logistic, and its maximum among \(m\) samples has expectation \(H_{m-1}\) by a beta order-statistic integral; symmetry gives \(\mathbb E D_1=2H_{m-1}=2H_d\).

## Verification
The standalone `check.py` generates an independently seeded finite Monte Carlo sample from the underlying gamma variables, numerically integrates the exact range CDF, and compares the infinite-product characteristic function of the coupling with the gamma-function ratio. In the recorded run, 12 parameter/dimension/threshold monotonicity grids (each with five concentration values), five Monte Carlo comparisons, and 12 product-versus-gamma comparisons passed. These numerical checks corroborate but do not replace the proofs above. Execute `python check.py` with NumPy and SciPy to reproduce; `check.log` contains the observed results.

## Relationship to prior work
The simplex Hilbert-to-variation-metric reduction is classical; Foertsch and Karlsson (2004 preprint, 2005 journal) prove the more general characterization of Hilbert geometries isometric to normed spaces, while Nielsen and Sun's Hilbert-simplex treatment explicitly records the coordinate-ratio formula. Gupta and Shah (1965) studied order statistics and the range of *ordinary* logistic samples: their results cover the \(\alpha=1\) marginal law and its mean, so these are not claimed as new. Anderson's (1955) moving-convex-set inequality underlies the probability comparison, independently reproduced here through log-concavity. The contribution asserted here is the explicit all-positive-parameter independent Bernoulli–Laplace degradation and its *strict every-threshold Dirichlet Hilbert-distance ordering*, rather than the known logarithmic-coordinate formula, a standard sample-range identity, or Anderson's inequality alone.

## Limitations
The theorem addresses fixed simplex dimension and a symmetric common Dirichlet concentration; it does not cover arbitrary independent nonidentical gamma shapes, other convex bodies, or Hilbert-invariant volume measures. Its exact one-dimensional integral is not an elementary closed formula for generic \(\alpha\). The stochastic result is established analytically; finite tests alone do not establish it. The 1965 logistic-range paper and original 1955 Anderson paper were only accessible in abstract/secondary-text form during the literature comparison, leaving residual risk from less accessible generalized-logistic and stochastic-order literature. Independent external scientific audit has not been performed.

## References
1. T. Foertsch and A. Karlsson, *Hilbert metrics and Minkowski norms*, arXiv:math/0407197v1, first publicly posted 2004-07-12; *Journal of Geometry* 83 (2005), 22–31. https://arxiv.org/abs/math/0407197
2. F. Nielsen and K. Sun, *Clustering in Hilbert simplex geometry*, arXiv:1704.00454 (2017), especially the projective-coordinate distance formula and variation-norm representation. https://arxiv.org/abs/1704.00454
3. S. S. Gupta and B. K. Shah, *Exact moments and percentage points of the order statistics and the distribution of the range from the logistic distribution*, *Annals of Mathematical Statistics* 36 (1965), 907–920. https://doi.org/10.1214/aoms/1177700063
4. T. W. Anderson, *The integral of a symmetric unimodal function over a symmetric convex set and some probability inequalities*, *Proceedings of the AMS* 6 (1955), 170–176. https://doi.org/10.1090/S0002-9939-1955-0069229-1
