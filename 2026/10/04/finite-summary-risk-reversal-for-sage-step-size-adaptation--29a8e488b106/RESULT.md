# Finite-summary risk reversal for SAGE step-size adaptation
## Finding
In an exact Gaussian mean-estimation specialization of the SAGE update, the data-adaptive step-size from Algorithm 2 has a finite-summary risk penalty that can reverse the improvement over the source-only estimator even when the source and target distributions are identical.

Let the source observations \(V^{(s)}_1,\ldots,V^{(s)}_{n_s}\) and target observations \(V^{(t)}_1,\ldots,V^{(t)}_{n_t}\) be independent \(N_r(\theta,\sigma^2 I_r)\), with \(n_s\ge r+1\). Only the target mean is needed from the target sample. Define
\[
S_s=\frac1{n_s}\sum_{i=1}^{n_s}(V^{(s)}_i-\bar V_s)(V^{(s)}_i-\bar V_s)^\mathsf T,
\]
\[
Q=(\bar V_t-\bar V_s)^\mathsf T\{(n_s^{-1}+n_t^{-1})S_s\}^{-1}(\bar V_t-\bar V_s),
\]
\[
T=(Q/r-1)_+,
\qquad
\rho=\frac{n_t}{n_s+n_t},
\qquad
\widehat\gamma=\frac{\rho+T}{1+T},
\]
and
\[
\widehat\theta_A=\bar V_s+\widehat\gamma(\bar V_t-\bar V_s).
\]
These are exactly the published SAGE step-size calculations in the Gaussian mean specialization, including the source covariance estimate.

For \(U\sim\operatorname{Beta}(r/2,(n_s-r)/2)\), set \(\lambda=r/n_s\), \(u_0=r/(n_s+r)\), and
\[
K_{r,n_s}=n_s\,\mathbb E\left[\frac{\{(1+\lambda)U-\lambda\}^2}{U}\,\mathbf 1\{U>u_0\}\right].
\]
Then
\[
\mathbb E\|\widehat\theta_A-\theta\|^2
=\frac{r\sigma^2}{n_s+n_t}+\frac{\sigma^2 n_s}{n_t(n_s+n_t)}K_{r,n_s}.
\]
The source-only risk is \(r\sigma^2/n_s\), so the adaptive estimator improves on source-only if and only if
\[
\frac{n_t}{n_s}>\sqrt{\frac{K_{r,n_s}}r}.
\]
Below this threshold, step-size adaptation is strictly harmful despite exact absence of distribution shift.

For example, when \(r=4\) and \(n_s=100\), numerical quadrature gives \(K_{4,100}=0.608779058977728\) and the exact risk boundary is \(n_t/n_s\approx0.390121474344123\). As \(n_s\to\infty\) with \(r=4\), the boundary tends to \(e^{-1}\approx0.367879441171442\).

## Assumptions and scope
The result is finite-sample and exact within the stated Gaussian location model. It uses a quadratic location loss for which the source empirical risk minimizer is \(\bar V_s\), the target summary mean supplies the exact gradient correction \(\bar V_t-\bar V_s\), and the retained SAGE summary coordinates are the \(r\) Gaussian mean coordinates. The source and target covariance matrices are both \(\sigma^2 I_r\), there is no distribution shift, and \(n_s\ge r+1\) so \(S_s\) is invertible almost surely.

The theorem does not claim a finite-sample guarantee for nonlinear prediction models, non-Gaussian summaries, shifted populations, learned encoders, or singular source covariance estimates. It isolates the finite-\(r\) cost of estimating the SAGE step-size in the clean null-shift benchmark.

## Proof
Write \(D=\bar V_t-\bar V_s\), \(c=n_s^{-1}+n_t^{-1}\), and
\[
M=\bar V_s+\rho D
=\frac{n_s\bar V_s+n_t\bar V_t}{n_s+n_t}.
\]
Joint Gaussianity gives \(M\perp D\). For a Gaussian source sample, \(\bar V_s\) is independent of its centered scatter matrix, and the target sample is independent of the source sample; hence \(M\) is independent of the pair \((D,S_s)\). Also
\[
M\sim N_r\left(\theta,\frac{\sigma^2}{n_s+n_t}I_r\right).
\]

Let
\[
W=\frac{n_s}{\sigma^2}S_s.
\]
Then \(W\sim\operatorname{Wishart}_r(I_r,n_s-1)\), independently of \(Z=D/(\sigma\sqrt c)\sim N_r(0,I_r)\), and
\[
Q=n_s Z^\mathsf T W^{-1}Z.
\]
Write \(Z=RU_0\), with \(R^2=X\sim\chi_r^2\) and \(U_0\) uniform on the unit sphere, independently. Orthogonal invariance of \(W\), followed by the Schur-complement representation of an inverse-Wishart quadratic form, gives
\[
\{U_0^\mathsf T W^{-1}U_0\}^{-1}\stackrel d=Y,
\qquad
Y\sim\chi^2_{n_s-r},
\]
independently of \(X\). Thus
\[
Q\stackrel d=n_s\frac{X}{Y}.
\]
Equivalently, if \(S=X+Y\) and \(U=X/(X+Y)\), then \(S\sim\chi^2_{n_s}\), \(U\sim\operatorname{Beta}(r/2,(n_s-r)/2)\), and \(S\perp U\).

On \(Q\le r\), \(T=0\) and \(\widehat\gamma=\rho\). On \(Q>r\), direct algebra gives
\[
\widehat\gamma-\rho
=(1-\rho)\left(1-\frac rQ\right).
\]
Therefore
\[
\widehat\theta_A
=M+(1-\rho)\left(1-\frac rQ\right)D\,\mathbf 1\{Q>r\}.
\]
The cross term in the quadratic risk vanishes because \(M-\theta\) is centered and independent of \((D,S_s)\). Since \(\|D\|^2=\sigma^2 cX\),
\[
\mathbb E\|\widehat\theta_A-\theta\|^2
=\frac{r\sigma^2}{n_s+n_t}
+(1-\rho)^2\sigma^2c\,\mathbb E\left[X\left(1-\frac{rY}{n_sX}\right)^2\mathbf 1\{n_sX>rY\}\right].
\]
The event is \(U>u_0=r/(n_s+r)\). With \(\lambda=r/n_s\), the expectation in brackets equals
\[
\mathbb E\left[S\frac{\{(1+\lambda)U-\lambda\}^2}{U}\mathbf 1\{U>u_0\}\right]=K_{r,n_s},
\]
because \(S\perp U\) and \(\mathbb E S=n_s\). Substitution of \(1-\rho=n_s/(n_s+n_t)\) and \(c=(n_s+n_t)/(n_sn_t)\) gives the displayed exact risk formula.

Finally,
\[
\frac{r\sigma^2}{n_s}-\frac{r\sigma^2}{n_s+n_t}
=\frac{r\sigma^2 n_t}{n_s(n_s+n_t)}.
\]
Comparing this gain with the adaptive penalty proves the if-and-only-if boundary.

For fixed \(r\), the source sample covariance converges to \(\sigma^2I_r\), and the preceding representation gives
\[
K_{r,n_s}\longrightarrow H_r
=\mathbb E\left[\frac{(X-r)^2}{X}\mathbf 1\{X>r\}\right],
\qquad X\sim\chi_r^2.
\]
Writing \(X=r+\sqrt{2r}Z_r\) with standardized chi-square \(Z_r\), the central limit theorem and bounded fourth moments yield uniform integrability and
\[
H_r\to2\,\mathbb E[Z^2\mathbf 1\{Z>0\}]=1.
\]
For \(r=4\), direct integration against the \(\chi_4^2\) density gives \(H_4=4e^{-2}\).

## Verification
The included `verify.py` evaluates the one-dimensional beta integral for \(K_{r,n_s}\), checks the stated \((r,n_s)=(4,100)\) value and threshold, independently evaluates the limiting \(\chi_r^2\) integral, and verifies \(H_4=4e^{-2}\) numerically. It also checks the risk ordering on both sides of the derived boundary. The computation is a finite numerical sanity check; the theorem itself is proved analytically above.

## Relationship to prior work
Zhang and Rothenhäusler introduce SAGE, derive fixed-step asymptotic risk guarantees, and propose the positive-part variance-inflation estimator used here for \(\widehat\gamma\). Their consistency result takes an iterated limit in which the summary dimension grows, and their discussion explicitly leaves finite-sample risk guarantees open. Their experiments also note that finite-sample rankings are not implied by the asymptotic results. The present theorem addresses that stated gap only in an exact Gaussian mean specialization and quantifies when finite-\(r\) step-size adaptation reverses the source-only risk improvement.

Classical James-Stein work and more recent external-summary integration methods provide different adaptive shrinkage rules. Green and Strawderman construct a James-Stein-type combination of unbiased and possibly biased estimators with a sample-mean dominance guarantee. Han, Li, Park, Mukherjee, and Taylor construct positive-part James-Stein external-information estimators with prediction-risk dominance guarantees in their regression setting. Those results do not imply the risk of the specific SAGE step-size estimator analyzed here; instead, they show that finite-sample safeguards are possible for different shrinkage geometries.

## Limitations
This is a deliberately narrow finite-sample theorem. It does not establish that practical SAGE is harmful in general, nor does it contradict SAGE's asymptotic random-shift guarantees. The exact threshold relies on Gaussianity, isotropy, a mean-estimation loss, an exactly observed target mean summary, and the published source-covariance normalization. The result identifies one clean finite-dimensional mechanism and a sharp boundary; extension to general SAGE predictors requires separate work.

## References
1. I. Zhang and D. Rothenhäusler, “Summary-powered prediction under distribution shift,” arXiv:2609.30908v1, 25 September 2026. https://arxiv.org/abs/2609.30908
2. P. Han, H. Li, S. K. Park, B. Mukherjee, and J. M. G. Taylor, “Improving prediction of linear regression models by integrating external information from heterogeneous populations: James-Stein estimators,” Biometrics 80(3), 2024, DOI:10.1093/biomtc/ujae072.
3. E. J. Green and W. E. Strawderman, “A James-Stein Type Estimator for Combining Unbiased and Possibly Biased Estimators,” Journal of the American Statistical Association 86(416), 1991, DOI:10.1080/01621459.1991.10475144.
