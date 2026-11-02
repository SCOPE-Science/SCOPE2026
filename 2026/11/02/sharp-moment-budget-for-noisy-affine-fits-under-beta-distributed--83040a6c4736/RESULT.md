# Sharp moment budget for noisy affine fits under beta-distributed sampling

## Finding
Let \(m\ge4\) be an integer, \(\alpha,\beta>0\), and let \(X_1,\ldots,X_m\) be independent \(\operatorname{Beta}(\alpha,\beta)\) random variables on \((0,1)\). Observe \(Y_j=\theta_0+\theta_1X_j+\varepsilon_j\), where the errors are independent \(N(0,\sigma^2)\), \(\sigma>0\), and independent of the sampling nodes. Let \(\widehat\theta_1\) be the unweighted ordinary least-squares slope, with a fitted intercept. Almost surely the design has full rank. Define
\[
\gamma_m=\min\{m-1,m\alpha,m\beta\}.
\]
For every real \(q>0\), the exact finite-moment criterion is
\[
\boxed{\mathbb E|\widehat\theta_1-\theta_1|^q<\infty\ \Longleftrightarrow\ q<\gamma_m.}
\]
The equality boundary \(q=\gamma_m\) is divergent. More precisely, the sample range \(R_m=\max_jX_j-\min_jX_j\) obeys, as \(r\downarrow0\),
\[
\Pr(R_m\le r)\asymp r^{\gamma_m}\bigl(1+\log(1/r)\bigr)^{\kappa_m},
\]
where \(\kappa_m=1\) precisely if \(\gamma_m=m-1\) and at least one of \(m\alpha,m\beta\) equals \(m-1\); otherwise \(\kappa_m=0\). The implied comparison constants depend on \(m,\alpha,\beta\) but not on \(r\).

The minimum sample count for a *finite unconditional slope mean-squared error* is therefore the least integer \(m\ge4\) for which \(m\alpha>2\), \(m\beta>2\), and \(m-1>2\). In particular, four independent uniform nodes have a finite slope MSE, whereas **four independent arcsine/Chebyshev-distributed nodes have an infinite slope MSE**; five arcsine nodes restore finiteness. Quantitatively, for four arcsine nodes,
\[
\boxed{\Pr(R_4\le r)\sim\frac{48}{\pi^4}r^2,}
\]
whereas for four uniform nodes the exact probability is \(4r^3-3r^4\), for \(0\le r\le1\).

## Assumptions and scope
The nodes are iid with the stated beta density; each response contains independent additive centered Gaussian noise of fixed nonzero variance. The estimator is the ordinary *unweighted* least-squares affine fit using an intercept; it is not a Christoffel-weighted, conditioned, rejected-design, or deterministic-node estimator. The moment criterion covers all real \(q>0\), all parameters \(\alpha,\beta>0\), all integers \(m\ge4\), and arbitrary true affine coefficients. The normalization is the usual beta density \(f(x)=x^{\alpha-1}(1-x)^{\beta-1}/B(\alpha,\beta)\) for \(0<x<1\).

## Proof
**1. Conditional noise and the random design energy.** Let \(\overline X=m^{-1}\sum_jX_j\) and \(S_m=\sum_j(X_j-\overline X)^2\). Independent absolutely continuous nodes are distinct almost surely, so \(S_m>0\) almost surely. The least-squares normal equations give
\[
\widehat\theta_1-\theta_1=\frac{\sum_j(X_j-\overline X)\varepsilon_j}{S_m}.
\]
Conditionally on all nodes this is Gaussian with variance \(\sigma^2/S_m\). Hence for each \(q>0\),
\[
\mathbb E|\widehat\theta_1-\theta_1|^q=\sigma^q\mathbb E|Z|^q\,\mathbb E S_m^{-q/2},\qquad Z\sim N(0,1),
\]
with the equality interpreted in \([0,\infty]\). Since every normal absolute moment is finite and positive, only the negative moment of \(S_m\) matters.

**2. Sample variance versus range.** Put \(R_m=\max_jX_j-\min_jX_j\). The two extreme observations alone contribute at least \(R_m^2/2\) to the sum of squared deviations, because for every real \(c\), \((\min X-c)^2+(\max X-c)^2\ge R_m^2/2\). Popoviciu's variance inequality gives the opposite bound:
\[
\frac12R_m^2\le S_m\le\frac m4R_m^2.
\]
Thus \(\mathbb E S_m^{-q/2}<\infty\) exactly when \(\mathbb E R_m^{-q}<\infty\).

**3. Small-range probability.** Write \(F\) for the beta CDF and \(f\) for the beta density. Choosing the unique minimum of the sample and requiring the other \(m-1\) observations to lie at most \(r\) above it gives the exact identity
\[
\Pr(R_m\le r)=m\int_0^1 f(x)\bigl[F(\min\{x+r,1\})-F(x)\bigr]^{m-1}\,dx.
\]
For \(0<r<1/8\), divide the integral into \((0,r)\), \((r,1/2)\), \((1/2,1-r)\), and \((1-r,1)\), with a harmless fixed interior subdivision if needed. Beta-density endpoint comparisons provide two-sided bounds, with constants independent of \(r\): the first piece is of order \(r^{m\alpha}\); the last is of order \(r^{m\beta}\); the near-left interior piece is of order
\[
r^{m-1}\int_r^{1/2}x^{m(\alpha-1)}\,dx,
\]
and the analogous near-right piece is of order
\[
r^{m-1}\int_r^{1/2}x^{m(\beta-1)}\,dx.
\]
These assertions follow from \(f(x)\asymp x^{\alpha-1}\) near zero, \(f(x)\asymp(1-x)^{\beta-1}\) near one, and \(F(x+r)-F(x)\asymp r x^{\alpha-1}\) for \(r\le x\le1/2\), with the reflected comparison at the right endpoint. Integrating the displayed powers yields \(r^{m-1}\) for exponent above \(-1\), \(r^{m-1}\log(1/r)\) at exponent \(-1\), or the corresponding endpoint power \(r^{m\alpha}\) or \(r^{m\beta}\) below \(-1\). Since all four contributions are nonnegative, their sum has precisely the two-sided order stated in the finding. The logarithm occurs in the leading order exactly when \(\gamma_m=m-1\) and either \(m\alpha=m-1\) or \(m\beta=m-1\); if the other endpoint has a smaller power, that power dominates the logarithmic contribution.

For \(q>0\), the layer-cake identity near zero gives
\[
\mathbb E R_m^{-q}=1+q\int_0^1r^{-q-1}\Pr(R_m<r)\,dr.
\]
The above two-sided small-range comparison makes this integral finite exactly if \(q<\gamma_m\); at equality it diverges even when there is no logarithmic enhancement. Steps 1 and 2 finish the finite-moment theorem.

**4. Exact arcsine coefficient and four-versus-five contrast.** For \(\alpha=\beta=1/2\), \(f(x)=\bigl(\pi\sqrt{x(1-x)}\bigr)^{-1}\) and \(F(x)=2\arcsin\sqrt{x}/\pi\). At \(m=4\) the contribution from each fixed interior strip \([\epsilon,1-\epsilon]\) is \(O_\epsilon(r^3)=o(r^2)\). The full neighborhoods of the two endpoints, including the scales \(x\gg r\), contribute, after \(x=ru\),
\[
\frac{32}{\pi^4}r^2\int_0^\infty u^{-1/2}\bigl(\sqrt{u+1}-\sqrt u\bigr)^3\,du+o(r^2).
\]
The integral equals \(3/4\): substitute \(u=\sinh^2t\), so \(u^{-1/2}du=2\cosh t\,dt\) and \(\sqrt{u+1}-\sqrt u=e^{-t}\); therefore the integral is \(2\int_0^\infty e^{-3t}\cosh t\,dt=3/4\). Both endpoints contribute equally, giving \(48r^2/\pi^4+o(r^2)\). The asymptotic interchange follows by domination of the rescaled integrand, whose large-\(u\) decay is integrable; the central region contributes a lower order.

For uniform nodes \(F(x)=x\), the exact range integral equals \(4r^3-3r^4\). Consequently \(\gamma_4=3\) for uniform nodes, \(\gamma_4=2\) for arcsine nodes, and \(\gamma_5=5/2\) for arcsine nodes. Taking \(q=2\) proves the stated contrasting risk thresholds.

## Verification
The standalone pure-Python script `verify.py` rechecks the uniform range identity against numerical integration, computes the analytic exponent and strict moment threshold for a grid of beta parameters, and compares independent numerical quadrature of the four-arcsine range probability to \(48r^2/\pi^4\) at shrinking radii. Those finite numerical checks are only corroboration; all quantified assertions follow from the foregoing proof.

## Relationship to prior work
Chkifa and Dolbeault (2023, arXiv:2306.07435, Section 6 and its algorithmic setup) compare iid uniform, arcsine and Christoffel sampling with stabilized/conditioned pointwise approximation, emphasizing conditioning and sample budget. Cohen and Migliorati (2016, arXiv:1608.00512) analyze weighted and *conditioned* random least squares, including noisy evaluations; their rejection/truncation mechanisms are absent here. Azriel (2021, arXiv:2112.14178) studies *asymptotic minimax random-design* objectives and weighted estimation. The distinct three-observation beta sample-variance lower-tail classification recorded in published-finding corpus covers \(m=3\), including constants, but does not state the claimed all-\(m\ge4\) finite-noise-moment threshold or the four-versus-five arcsine/uniform contrast. Our result concerns unconditional, unweighted affine OLS with iid beta nodes and exact Gaussian response noise, not any of the referenced stabilized design algorithms.

## Limitations
No claim is made that uniform iid sampling is globally better than arcsine sampling in other polynomial degrees or risk regimes. The threshold is an *unconditional* moment statement, not a high-probability stability estimate. Conditioning or rejecting clustered designs, regularization, deterministic nodes, correlated nodes, or Christoffel weights can change it. The range probability and inverse sample-variance arguments do not identify an exact leading constant for the slope-error tail in general. The distinct three-sample beta lower-tail publication was available only through its indexed mathematical summary; its inaccessible full text leaves a residual overlap risk. Independent publication-priority and scientific audits have not been performed.

## References
1. A. Chkifa and M. Dolbeault, *Randomized least-squares with minimal oversampling and interpolation in general spaces*, first posted 2023-06-12, https://arxiv.org/abs/2306.07435; SIAM J. Numer. Anal. 62 (2024), 1515–1538, https://doi.org/10.1137/23M160178X.
2. A. Cohen and G. Migliorati, *Optimal weighted least-squares methods*, 2016 preprint, https://arxiv.org/abs/1608.00512; SMAI J. Comput. Math. 3 (2017), 181–203, https://doi.org/10.5802/smai-jcm.24.
3. D. Azriel, *Optimal minimax random designs for weighted least squares estimators*, first posted 2021-12-28, https://arxiv.org/abs/2112.14178.
4. *Exact lower-tail phase diagram for the three-sample Beta variance*, indexed mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-lower-tail-phase-diagram-for-the-three-sample-beta-varianc--f275509045a1. Full text not accessible during comparison.
