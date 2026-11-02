# Multivariate Pareto excursions and a Gamma reset-age law in a first-passage-resetting Brownian gas

## Finding

Fix an integer \(N\geq3\), a diffusion constant \(D>0\), and a reset threshold \(L>0\). Consider \(N\) independent Brownian coordinates with generator \(D\partial_{xx}\) between resets. All positions are jointly returned to zero whenever *any* coordinate first reaches \(L\). Let \((X_1,\ldots,X_N)\) have the unique stationary position law, and let \(A\) be the backward recurrence time from the most recent joint reset. Define
\[
S(t)=\operatorname{erf}\!\left(\frac{L}{\sqrt{4Dt}}\right),\qquad
Z_N=\int_0^\infty S(t)^N\,dt\in(0,\infty),
\]
\[
K_N=\frac{2^{N-2}\Gamma(N/2-1)L^N}{\pi^{N/2}D Z_N}.
\]
For every integer \(1\leq k\leq N\) and every fixed vector \(\mathbf a=(a_1,\ldots,a_k)\) with \(a_i>0\), the following *fixed-population, large-negative-excursion* limit holds:
\[
\boxed{\lim_{R\to\infty}R^{N-2}\Pr\{X_1<-a_1R,\ldots,X_k<-a_kR\}
=K_N\left(\sum_{i=1}^k a_i^2\right)^{1-N/2}.}
\]
In particular the joint tail is not asymptotically independent:
\[
\boxed{\lim_{R\to\infty}\Pr\{X_2<-R,\ldots,X_k<-R\mid X_1<-R\}
=k^{1-N/2},\quad 2\leq k\leq N.}
\]
The conditional elapsed-time law identifies the mechanism. With \(U_R=R^2/(4DA)\), under the stationary event \(\{X_1<-R\}\),
\[
\boxed{U_R\ \Longrightarrow\ \operatorname{Gamma}\!\left(\frac N2-1,\text{rate }1\right).}
\]
All positive integer moments of \(U_R\) conditioned on this event converge to those of the displayed Gamma distribution; the same is true for any real nonnegative moment order.

Consequently, for every \(q>0\),
\[
\boxed{\mathbb E|X_1|^q<\infty\quad\Longleftrightarrow\quad q<N-2.}
\]
Thus a stationary distribution exists already at \(N=3\), but \(\mathbb E|X_1|\) is infinite there. The mean first becomes finite at \(N=4\), and the variance first becomes finite at \(N=5\). For each \(N\geq5\), the stationary cross-covariance of distinct labels is finite and strictly positive:
\[
\operatorname{Cov}(X_i,X_j)=\operatorname{Var}_{q_N}(m(A))>0,
\qquad
m(t)=-L\frac{\operatorname{erfc}(L/\sqrt{4Dt})}
{\operatorname{erf}(L/\sqrt{4Dt})},\quad
q_N(t)=\frac{S(t)^N}{Z_N}.
\]
The covariance statement is about finite \(N\); a previously published leading large-\(N\) approximation is symmetric and gives a different leading-order correlation structure.

## Assumptions and scope

The stochastic resetting trigger is the *first hitting* of a single positive level by any of the \(N\) diffusions, not a Poisson clock or independent particle resets. The diffusion coefficient convention is \(\operatorname{Var}(X_i(t))=2Dt\) before killing. Resets are instantaneous, complete, simultaneous, and restart each Brownian trajectory with fresh increments. The stationary assertions are for fixed finite integer \(N\geq3\), with \(D,L\) fixed and strictly positive; the limit \(R\to\infty\) is taken *before* any particle-number limit. No uniformity in \(N\), in levels approaching zero, or in the order of the large-\(N\) and far-tail limits is asserted. The Gamma variable uses shape/rate parametrization.

## Proof

**1. Stationary renewal representation.** Let
\[
g(x,t)=\frac{1}{\sqrt{4\pi Dt}}
\left(e^{-x^2/(4Dt)}-e^{-(x-2L)^2/(4Dt)}\right)\mathbf1_{\{x<L\}}
\]
be the absorbing half-line transition density of one Brownian coordinate started at zero. The reflection principle yields \(\int_{-\infty}^L g(x,t)\,dx=S(t)\). The survival probability of the full inter-reset cycle is \(S(t)^N\). Since \(S(t)\sim L/\sqrt{\pi Dt}\) as \(t\to\infty\), the mean cycle length \(Z_N\) is finite precisely for \(N>2\). The stationary renewal reward identity therefore yields
\[
P_{\rm st}(x_1,\dots,x_N)=\frac1{Z_N}\int_0^\infty
\prod_{i=1}^N g(x_i,t)\,dt,
\qquad
q_N(t)=\frac{S(t)^N}{Z_N}.
\]
Given \(A=t\), the positions are independent with density \(g(x,t)/S(t)\). This exact representation was established in the originating literature; it is the starting point, not the new claim.

**2. Exact negative-event integral.** For \(b>0\), define the killed negative-tail event probability:
\[
F_b(t):=\int_{-\infty}^{-b}g(x,t)\,dx
=\frac12\left[\operatorname{erfc}\!\left(\frac b{\sqrt{4Dt}}\right)
-\operatorname{erfc}\!\left(\frac{b+2L}{\sqrt{4Dt}}\right)\right].
\]
Then for \(B_R=\bigcap_{i=1}^k\{X_i<-a_iR\}\),
\[
\Pr(B_R)=\frac1{Z_N}\int_0^\infty
S(t)^{N-k}\prod_{i=1}^k F_{a_iR}(t)\,dt.
\]
The conditional negative-event probability is \(H_b(t)=F_b(t)/S(t)\).

**3. Uniform domination and asymptotic integration.** Substitute \(t=R^2s/(4D)\). For each fixed \(s>0\), the error-function expansion and the mean-value theorem for a short interval of Gaussian density show
\[
RS\!\left(\frac{R^2s}{4D}\right)\to\frac{2L}{\sqrt{\pi s}},
\qquad H_{aR}\!\left(\frac{R^2s}{4D}\right)\to e^{-a^2/s}.
\]
For every \(t>0\), writing \(\sigma=\sqrt{2Dt}\), the standard-normal density \(\varphi\) gives the bounds
\[
S(t)\leq\frac{2L}{\sigma}\varphi(0),\quad
F_{aR}(t)\leq\frac{2L}{\sigma}\varphi(aR/\sigma),\quad
S(t)\geq\frac{2L}{\sigma}\varphi(L/\sigma).
\]
Hence, for \(R\geq\sqrt2 L/\min_i a_i\),
\[
0\leq H_{a_iR}\!\left(\frac{R^2s}{4D}\right)
\leq e^{-a_i^2/(2s)}.
\]
After extracting the factor \(R^{2-N}\), the rescaled integrand is dominated by a positive constant times
\[
s^{-N/2}\exp\!\left[-\frac{1}{2s}\sum_{i=1}^k a_i^2\right],
\]
which is integrable on \((0,\infty)\) exactly because \(N>2\). Dominated convergence therefore yields
\[
\lim_{R\to\infty}R^{N-2}\Pr(B_R)=
\frac{(2L)^N}{4D\,\pi^{N/2}Z_N}
\int_0^\infty s^{-N/2}e^{-\sum a_i^2/s}\,ds.
\]
The substitution \(u=(\sum a_i^2)/s\) evaluates the integral to
\(\Gamma(N/2-1)(\sum a_i^2)^{1-N/2}\), proving the multivariate limit and its exact normalization.

**4. Extreme-event reset age.** Under \(\{X_1<-R\}\), the unnormalized stationary age density is \(Z_N^{-1}S(t)^N H_R(t)\,dt\). The same change of variables gives the limiting \(s\)-density proportional to \(s^{-N/2}e^{-1/s}\). Transforming \(u=1/s=R^2/(4Dt)\) gives the density
\[
\frac{u^{N/2-2}e^{-u}}{\Gamma(N/2-1)}\,\mathbf1_{\{u>0\}}.
\]
The domination in Step 3 also applies with every nonnegative power of \(u\), giving convergence of those moments, not merely weak convergence. Taking ratios of the \(k\)- and one-coordinate limits proves \(k^{1-N/2}\).

**5. Moment and covariance boundaries.** Since \(X_i\leq L\) almost surely, only its negative tail can generate divergent absolute moments. The \(k=1\) equivalent has a strictly positive coefficient and exponent \(N-2\); integrating \(qR^{q-1}\Pr(X_i<-R)\) from any positive lower cutoff proves the exact criterion, including divergence at equality. Direct integration of \(xg(x,t)\) gives the conditional mean \(m(t)\) displayed in the finding. Conditional independence implies \(\mathbb E[X_iX_j\mid A]=m(A)^2\) for distinct labels. When \(N\geq5\), the second moments exist, so total covariance gives \(\operatorname{Cov}(X_i,X_j)=\operatorname{Var}_{q_N}(m(A))\). It is strictly positive because \(q_N\) has a positive density on \((0,\infty)\) and \(m(t)\) is not constant.

## Verification

A standalone numerical diagnostic, `verify.py`, evaluates \(Z_N\) by two independent quadrature parametrizations and the *exact finite-threshold* joint probabilities via a stable Gaussian short-interval integral. It compares the scaled joint exceedances with the sharp constants, the predicted \(k\)-fold conditional ratios, and the first two rare-event Gamma-age moments for all integers \(3\leq N\leq8\). In the stated computational environment it passed 60 checks. Numerical integration illustrates finite-\(R\) approach; the bound and dominated-convergence proof above establish the universal limit.

## Relationship to prior work

Biroli, Majumdar and Schehr, *First Passage Resetting Gas* (arXiv:2512.00440; EPL 153, 31002), establishes the complete stationary renewal/conditional-independence representation, the \(N>2\) existence threshold, and typical \(N\to\infty\) density, order, gap and counting statistics. Those are explicitly prior results. The present result performs a different **fixed-\(N\), far-left multivariate tail** limit, including the angular \(\ell_2\) dependence, the conditional Gamma clock law, and sharp moment thresholds; these formulas are not presented in the inspected text. In particular, the source's Gaussian large-\(N\) typical-coordinate scaling cannot be interchanged with the fixed-\(N\) remote-tail limit.

Biroli, Larralde, Majumdar and Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting* (arXiv:2211.00563; PRL 130, 207101), gives the corresponding exact stationary density for a globally **Poisson-reset** gas: its clock has exponential, rather than event-survival, age density, and its one-particle tails are exponential. De Mauro and collaborators' *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols* (arXiv:2509.06658; PRE 113, 014120) covers externally drawn shared reset intervals and generic stationary mixtures; this is not the same trigger-dependent killed-diffusion model. Standard renewal theory and Gaussian asymptotics supply proof techniques, not the stated constants by themselves. Fixed-\(N\) multivariate tail equivalences might potentially be latent in wider stationary-mixture literature, which is a publication-priority limitation.

## Limitations

No claim is made of new discovery of the exact stationary JPDF, the renewal mixture, the \(N>2\) stationarity threshold, or the large-population typical-coordinate statistics. The theorem requires integer \(N\geq3\), independent Brownian increments between complete common resets, one common upper threshold, zero drift, and fixed positive diffusivity. The extreme-event limit is only for fixed positive directional levels; it is not uniform as levels approach zero or as population size diverges. Stationary cross-covariances require \(N\geq5\); it would be incorrect to assign finite Pearson correlations for \(N=3\) or \(N=4\). Numerical diagnostics do not establish infinite-domain claims. No independent mathematical or publication-priority validation has been performed.

## References

1. M. Biroli, S. N. Majumdar, and G. Schehr, *First Passage Resetting Gas*, arXiv:2512.00440 (preprint dated 29 November 2025, publicly announced December 2025), *Europhysics Letters* **153**, 31002 (2026). https://arxiv.org/abs/2512.00440 ; https://doi.org/10.1209/0295-5075/ae3f4f .
2. M. Biroli, H. Larralde, S. N. Majumdar, and G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, arXiv:2211.00563, *Physical Review Letters* **130**, 207101 (2023). https://arxiv.org/html/2211.00563v3 .
3. G. de Mauro, M. Biroli, S. N. Majumdar, and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658, *Physical Review E* **113**, 014120 (2026). https://arxiv.org/abs/2509.06658 .
