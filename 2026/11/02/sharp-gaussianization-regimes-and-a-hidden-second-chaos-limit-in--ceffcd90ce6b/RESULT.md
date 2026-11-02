# Sharp Gaussianization regimes and a hidden second-chaos limit in fractional diffusion with persistent diffusivity

## Finding

Let \(p=2H\in(0,2)\). For the Riemann–Liouville heterogeneous fractional-diffusion model
\[
 X_t=\sqrt{2p}\int_0^t (t-s)^{(p-1)/2}\sqrt{\mathcal D_s}\,dW_s,
\]
with a stationary nonnegative diffusivity independent of the Brownian motion, the non-Gaussian parameter \(\Gamma(t)=\mathbb E[X_t^4]/(3\mathbb E[X_t^2]^2)-1\) has **three sharp long-time regimes** whenever the diffusivity covariance is asymptotically \(c h^{-\eta}\) with \(0<\eta<1\). Write \(\mu=\mathbb E\mathcal D_0>0\), \(C(h)=\operatorname{Cov}(\mathcal D_0,\mathcal D_h)\), and \(B\) for Euler's beta function. Then:
\[
\Gamma(t)\sim\begin{cases}
\displaystyle\frac{2p^2 B(p,1-2p)}{\mu^2}\left(\int_0^\infty h^{2p-1}C(h)\,dh\right)t^{-2p}, & 0<p<\eta/2,\\[7pt]
\displaystyle\frac{2p^2 c B(p,1-\eta)}{\mu^2}\,t^{-\eta}\log t, & p=\eta/2,\\[7pt]
\displaystyle\frac{2p^2 c B(p,1-\eta)}{\mu^2(2p-\eta)}\,t^{-\eta}, & p>\eta/2.
\end{cases}
\]
The transition is at \(H=\eta/4\), and \(X_t/\sqrt{2\mu t^p}\) converges in distribution to a standard normal in all three regimes.

A second conclusion concerns the **remaining non-Gaussian environmental fluctuations**. Let \(G_s\) be a stationary centered unit-variance Gaussian process with covariance \(\mathbb E[G_0G_h]=(1+|h|)^{-\eta/2}\), let \(d_0,\delta>0\), and set \(\mathcal D_s=d_0+\delta G_s^2\). Denote the conditional variance by \(V_t=\operatorname{Var}(X_t\mid\mathcal D)\), and \(M_t=V_t/(2t^p)\). For \(0<p<\eta/2\),
\[
 t^p\bigl(M_t-(d_0+\delta)\bigr)\ \xrightarrow{\ d\ }\
 Z_{p,\eta}=\delta p\int_0^\infty u^{p-1}(G_u^2-1)\,du.
\]
The improper integral converges in \(L^2\), is nondegenerate, and belongs to the second Gaussian Wiener chaos; in particular it is **not Gaussian**. Its variance is exactly
\[
 \operatorname{Var}(Z_{p,\eta})=4\delta^2p^2B(p,1-2p)B(2p,\eta-2p)>0.
\]
This is consistent with Gaussianization of the **position**, because it is the appropriately magnified **conditional-variance fluctuation** that has this non-Gaussian limit.

## Assumptions and scope

The integrator \(W\) is one-dimensional standard Brownian motion. The process \(\mathcal D\) is measurable, stationary, nonnegative, independent of \(W\), with \(\mathbb E\mathcal D_0^2<\infty\), \(\mu>0\), and nonnegative covariance \(C(h)\ge0\) for every \(h\ge0\). Assume \(C(h)\sim c h^{-\eta}\) as \(h\to\infty\), with \(c>0\) and \(0<\eta<1\). Time is measured in fixed units, so the logarithm in the borderline asymptotic is dimensionless; changing the reference time does not affect its leading coefficient. The stochastic integral is well defined for each \(t>0\) since \(p>0\).

For the distributional limit, the Gaussian process is taken in a measurable separable version with even covariance \((1+|h|)^{-\eta/2}\). Such a stationary process exists: the covariance is a positive mixture of exponential covariances. Only the marginal law of \(Z_{p,\eta}\) is asserted, not process-level convergence or asymptotic independence.

## Proof

**Conditional Gaussian reduction.** Given \(\mathcal D\), the stochastic integral is centered Gaussian with variance
\[
 V_t=2p\int_0^t (t-s)^{p-1}\mathcal D_s\,ds.
\]
Consequently \(\mathbb EV_t=2\mu t^p\), \(\mathbb E[X_t^4]=3\mathbb E[V_t^2]\), and therefore
\[
 \Gamma(t)=\frac{p^2}{\mu^2t^{2p}} I_t,\qquad
 I_t=\int_0^t\int_0^t u^{p-1}v^{p-1}C(|u-v|)\,du\,dv.
\]
This double-covariance identity itself is a previously known method; the contribution below is its sharp long-memory asymptotic classification and the second-chaos limit.

**Regime \(p>\eta/2\).** Substitute \(u=tx\), \(v=ty\). Since \(C\) is bounded near zero and regularly varying at infinity, \(h^\eta C(h)\) is globally bounded. Hence \(t^\eta C(t|x-y|)\le K|x-y|^{-\eta}\). The dominating kernel \(x^{p-1}y^{p-1}|x-y|^{-\eta}\) is integrable on the unit square precisely when \(2p>\eta\). Dominated convergence gives
\[
 \lim_{t\to\infty}t^{\eta-2p}I_t
 =c\int_0^1\int_0^1x^{p-1}y^{p-1}|x-y|^{-\eta}\,dx\,dy
 =\frac{2cB(p,1-\eta)}{2p-\eta}.
\]
The last equality follows on the triangle \(0<y<x<1\) by \(y=xz\).

**Regimes \(p\le\eta/2\).** Here \(p<1/2\). Write \(u=v+h\) on the upper triangle, so
\[
 I_t=2\int_0^t h^{2p-1} C(h) F_p((t-h)/h)\,dh,\qquad
 F_p(w)=\int_0^w z^{p-1}(1+z)^{p-1}\,dz.
\]
Since \(p<1/2\), \(F_p(w)\uparrow F_p(\infty)=B(p,1-2p)\). If \(2p<\eta\), the integrable majorant \(2B(p,1-2p)h^{2p-1}C(h)\) applies, so monotone convergence gives the finite limiting value of \(I_t\) in the first case. If \(2p=\eta\), the tail satisfies \(h^{2p-1}C(h)\sim c/h\). For any fixed \(a\in(0,1)\), the integral over \(h\in[1,t^a]\) contributes asymptotically \(2acB(p,1-2p)\log t\). An upper bound using \(F_p\le B(p,1-2p)\) gives at most \(2cB(p,1-2p)\log t\) to leading order. Letting \(a\uparrow1\), \(I_t\sim2cB(p,1-2p)\log t\). Because \(\eta=2p\), this equals the displayed critical constant.

**Gaussianization of the position.** In each case \(\Gamma(t)\to0\), hence \(V_t/(2\mu t^p)\to1\) in \(L^2\). Conditional Gaussian characteristic functions converge to \(\exp(-q^2/2)\) after deterministic standardization; bounded convergence establishes the weak limit.

**Second-chaos limit.** For the specified diffusivity, \(\mu=d_0+\delta\) and \(C(h)=2\delta^2(1+h)^{-\eta}\). By stationarity and Gaussian time reversibility,
\[
 t^p(M_t-\mu)\ \stackrel d=\ \delta p\int_0^t u^{p-1}(G_u^2-1)\,du.
\]
For \(0<p<\eta/2\), the right-hand integrals are Cauchy in \(L^2\): their covariance kernel is \(2(1+|u-v|)^{-\eta}\) and the weighted double integral over \((0,\infty)^2\) is finite. The triangle substitution above yields
\[
 \int_0^\infty\!\int_0^\infty u^{p-1}v^{p-1}(1+|u-v|)^{-\eta}\,du\,dv
 =2B(p,1-2p)B(2p,\eta-2p).
\]
This proves the limit and stated variance. Each centered square \(G_u^2-1\) lies in the second Wiener chaos, a closed subspace of \(L^2\); so does the limit. Its positive variance rules out zero. Any nonzero second-chaos random variable admits an expansion \(\sum_j\lambda_j(N_j^2-1)\) with \(\sum_j\lambda_j^2>0\), whose fourth cumulant is \(48\sum_j\lambda_j^4>0\). Thus the limit is not Gaussian.

## Verification

The accompanying standalone program `verify.py` implements two mathematically independent covariance-integral quadratures and the asymptotic beta-function coefficients. The six-parameter quadratures agree within the stated relative tolerance; the numerical asymptotic ratios at large time approach the predicted subcritical, critical and supercritical constants. An additional check confirms that the second-chaos variance matches the subcritical covariance coefficient. The program prints `PASS 13` on a successful run. These finite checks support, but do not replace, the preceding general proof.

## Relationship to prior work

Pacheco-Pozo and Krapf (2024) introduced the fluctuating-diffusivity fractional stochastic integral and developed second-order displacement and time-average theory. Balcerek and collaborators (2025) derived exact fourth-moment/kurtosis identities for switching fractional Brownian motion, including Markovian exponential correlations and heavy-tailed renewal switching; the double-covariance formula above is therefore **not** asserted to be new. Their heavy-tailed switching processes may be nonstationary and need not have the stationary covariance hypotheses used here. The contribution here is the evaluated **three-regime long-memory decay theorem** for stationary algebraically correlated diffusivity, together with the **non-Gaussian magnified mixing-variable limit** in a concrete positive Gaussian-square environment. Broader general theories of random diffusivity and second Wiener chaos may imply special portions of these results; priority outside the inspected sources is not certified.

## Limitations

The theorem does not cover sign-changing covariance without further cancellation analysis, multifractional kernels with time-varying \(H\), the full trajectory-level distribution, or nonstationary heavy-tailed renewal models. The Gaussian position limit is in distribution, not a quantitative total-variation bound. The second-chaos limit is for environmental conditional variance under a specific Gaussian-square diffusivity, not the normalized particle position. Independent verification and exhaustive publication-priority certification have not been performed.

## References

1. A. Pacheco-Pozo and D. Krapf, *Fractional Brownian motion with fluctuating diffusivities*, arXiv:2405.03836 (first publicly posted 2024-05-06), Physical Review E 110, 014105 (2024).
2. M. Balcerek, A. Pacheco-Pozo, A. Wyłomańska, and D. Krapf, *Evaluating Gaussianity of heterogeneous fractional Brownian motion*, arXiv:2501.10472 (first posted 2025-01-16).
3. A. Lanoiselée, D. Grebenkov, and G. Pagnini, *A unifying approach to diffusive transport in annealed heterogeneous media*, arXiv:2603.12775 (2026), for broader heterogeneous-transport context.
