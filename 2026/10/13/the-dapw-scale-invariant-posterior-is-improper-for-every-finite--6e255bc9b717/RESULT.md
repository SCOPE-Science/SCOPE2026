# The DAPW scale-invariant posterior is improper for every finite Type-II or upper-record dataset
## Finding
Consider the common-shape discrete alpha-power Weibull (DAPW) stress–strength model with parameter vector
\[
(\alpha,\theta_1,\beta_1,\theta_2,\beta_2),
\qquad \alpha>0,\ \alpha\ne1,\ 0<\theta_j<1,\ \beta_j>0.
\]
The source specifies, for its Type-II and upper-record Bayesian procedures, the joint improper prior
\[
\pi(\alpha,\theta_1,\beta_1,\theta_2,\beta_2)
\propto\frac1{\alpha\theta_1\beta_1\theta_2\beta_2}.
\]
**The posterior is improper for every finite valid dataset under either sampling procedure.** This holds regardless of the number of observed values or how many distinct integers they contain.

The obstruction comes from a nondegenerate distributional boundary rather than a zero-count anomaly. There exists an escaping parameter family with \(\alpha\to\infty\), \(\theta_j\to0\), \(\beta_j\to0\), on which both DAPW laws converge to positive-atom discrete Fréchet distributions and on which the prior carries infinite mass.

## Assumptions and scope
For each margin, the source's CDF on the nonnegative integers is
\[
F_{\alpha,\theta,\beta}(x)
=1-\frac\alpha{\alpha-1}
\left(1-\alpha^{-\theta^{(x+1)^\beta}}\right),
\qquad x=0,1,\ldots,
\]
with \(F(-1)=0\). The PMF is
\[
p_{\alpha,\theta,\beta}(x)=F(x)-F(x-1).
\]
The two margins share \(\alpha\) but have their own \((\theta_j,\beta_j)\).

The Type-II data comprise finite ordered failure times and finite sample sizes. The upper-record data comprise finite strictly increasing nonnegative-integer sequences. Their likelihoods are the finite products of PMFs, survivors, and conditional record factors displayed in the source. The result assumes those displayed likelihoods, although the same escaping-boundary mechanism persists for the exact probability of any finite positive-probability discrete observation event.

The mixed upper–lower record procedure fixes \(\alpha\) and uses a different four-parameter prior. It is **not** included in this theorem.

## Proof
Work in the admissible region \(\alpha>1\) and put
\[
A=\log\alpha,\qquad \ell=\log A.
\]
The CDF can be rewritten exactly as
\[
F_{\alpha,\theta,\beta}(x)
=\frac{\exp[-A\theta^{(x+1)^\beta}]-\exp(-A)}{1-\exp(-A)}.
\]
For each margin choose
\[
\theta_j=\frac{e^{-s_j}}A,
\qquad \beta_j=\frac{c_j}{\ell},
\]
where \(s_j\) lies in a fixed compact interval and \(c_j\) in a compact positive interval. These parameters are admissible for every sufficiently large \(A\).

For fixed integer \(x\ge0\), uniformly on those compact intervals,
\[
(x+1)^{\beta_j}
=\exp\left[\frac{c_j\log(x+1)}\ell\right]
=1+\frac{c_j\log(x+1)}\ell+O(\ell^{-2}).
\]
Therefore
\[
\begin{aligned}
\log\!\left(A\theta_j^{(x+1)^{\beta_j}}\right)
&=\ell-(\ell+s_j)(x+1)^{c_j/\ell}\\
&=-s_j-c_j\log(x+1)+O(\ell^{-1}),
\end{aligned}
\]
and hence
\[
A\theta_j^{(x+1)^{\beta_j}}
\longrightarrow e^{-s_j}(x+1)^{-c_j}.
\]
The DAPW CDF converges to
\[
H_{s_j,c_j}(x)
=\exp[-e^{-s_j}(x+1)^{-c_j}],
\qquad x\ge0,
\]
with \(H(-1)=0\). This is a proper nondegenerate CDF. Its probability at zero is positive and, for every integer \(x\ge1\),
\[
H_{s,c}(x)-H_{s,c}(x-1)>0.
\]
Furthermore, \(0<H_{s,c}(x)<1\) at every finite \(x\). All limiting PMF, survivor, and strict-record factors in finite valid observations are therefore positive. Because only finitely many evaluations occur and all denominators remain bounded away from zero on compact \((s_1,c_1,s_2,c_2)\) rectangles, the likelihood converges uniformly to a continuous function with a strictly positive minimum there.

Now transform the prior measure. As \(\alpha=e^A\), \(d\alpha/\alpha=dA\). Moreover,
\[
-\log\theta_j=\ell+s_j,
\qquad \log\beta_j=\log c_j-\log\ell.
\]
The Jacobian of \((A,-\log\theta_1,\log\beta_1,-\log\theta_2,\log\beta_2)\) with respect to \((A,s_1,c_1,s_2,c_2)\) equals \((c_1c_2)^{-1}\). Therefore, exactly,
\[
\frac{d\alpha}{\alpha}
\prod_{j=1}^2\frac{d\theta_j}{\theta_j}\frac{d\beta_j}{\beta_j}
=dA\,ds_1\,ds_2\,\frac{dc_1}{c_1}\frac{dc_2}{c_2}.
\]
Fix a rectangle such as \(0\le s_j\le1\) and \(1\le c_j\le2\). For all sufficiently large \(A\), the data likelihood is bounded below by a positive constant on this rectangle. The unnormalized posterior integral is therefore bounded below by a positive multiple of
\[
\int_{A_0}^{\infty}dA
\prod_{j=1}^2\int_0^1 ds_j\int_1^2\frac{dc_j}{c_j}
=\infty.
\]
This proves posterior impropriety for every finite dataset in both schemes, without a large-sample or asymptotic-normality approximation.

## Verification
Run the self-contained accompanying Python file:

`python verify_dapw_ridge.py`

It numerically evaluates the exact DAPW CDF along the escaping path, the discrete Fréchet limit, and finite Type-II and upper-record likelihoods for two sets of distinct integer observations. It checks that both likelihoods approach strictly positive limits while the CDF error tends to zero. Symbolic differentiation independently checks the exact five-dimensional Jacobian \((c_1c_2)^{-1}\). Its output ends with `VERIFY_OK`.

These finite checks do not establish the infinite-volume conclusion; that conclusion is the analytical uniform-limit and measure-change argument above.

## Relationship to prior work
The target article gives the DAPW formulas and explicitly adopts \(1/\alpha\), \(1/\theta_j\), and \(1/\beta_j\) as independent priors in its Type-II and upper-record Bayesian sections. It acknowledges that these priors are improper but suggests sufficiently informative data generally produce proper posteriors, and then computes formal posterior means and intervals. The derived nondegenerate boundary proves that those particular posteriors remain improper irrespective of finite data.

The original DAPW paper of Mohamed, Hassan, and Abdelrahman (2022) defines the discrete family and studies its probabilistic properties and maximum-likelihood and moment estimation. It does not analyze this five-parameter prior-normalization problem.

Ramos and Ramos (2020) establish necessary and sufficient posterior-propriety criteria for the **continuous two-parameter Weibull** law, with examples where the prior proportional to \(1/(\eta\beta)\) yields a proper posterior. That result concerns a different likelihood family and parameter geometry; it does not cover the coordinated DAPW boundary \(\alpha\to\infty,\theta_j\to0,\beta_j\to0\) or the present divergent five-dimensional prior volume.

Targeted searches of the DAPW DOI, exact prior, posterior-normalization terminology, discrete Fréchet limits, and equivalent joint-parameter escape routes did not locate this result.

## Limitations
This result concerns the **unbounded joint parameter domain and exact improper prior stated for the Type-II and upper-record Bayesian methods**. A properly truncated or otherwise regularized prior would have to be analyzed separately and may avoid the obstruction. Neither pointwise numerical integration over a finite box nor a finite collection of apparently stable posterior draws proves posterior propriety.

No conclusion is drawn about the separate mixed-record Bayesian procedure, which fixes \(\alpha\), or about the paper's classical estimation results. We do not infer which finite numerical integration bounds or other unstated implementation choices may have been used to produce its tables.

A recent unindexed study may also have noticed this particular boundary.

## References
1. B. Elkalzah, M. O. Mohamed, K. Elsharkawy, E. S. Osman, A. Aldukeel, and G. A. Marei, “Classical and Bayesian estimation of stress–strength reliability under the discrete Alpha-power Weibull distribution with incomplete and record data: Application to high-voltage capacitors,” *AIMS Mathematics* **11** (2026), 6374–6399. DOI: 10.3934/math.2026263.
2. M. O. Mohamed, N. A. Hassan, and N. Abdelrahman, “Discrete alpha-power Weibull distribution: Properties and application,” *International Journal of Nonlinear Analysis and Applications* **13** (2022), 1305–1317. DOI: 10.22075/ijnaa.2022.6301.
3. E. Ramos and P. L. Ramos, “Posterior properties of the Weibull distribution for censored data,” arXiv:2005.08195 (2020); *Statistics & Probability Letters* **166** (2020), 108872.
