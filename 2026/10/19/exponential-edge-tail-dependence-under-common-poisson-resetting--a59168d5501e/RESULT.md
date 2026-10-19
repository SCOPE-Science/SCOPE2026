# Exponential edge-tail dependence under common Poisson resetting

## Finding
Consider a stationary gas of \(N\ge3\) independent one-dimensional Brownian particles with diffusivity \(D>0\), simultaneously reset to the origin whenever a common rate-\(r>0\) Poisson clock rings. Let \(M_N(t)=\max_{1\le i\le N}X_i(t)\), \(V_N(t)=N^{-1}\sum_{i=1}^N X_i(t)^2\), and let \(b_N=\Phi^{-1}(1-1/N)\), where \(\Phi\) is the standard normal distribution function. Almost surely \(V_N(t)>0\). Define the empirically standardized edge
\[
Y_N(t)=b_N\left(\frac{M_N(t)}{\sqrt{V_N(t)}}-b_N\right).
\]
For every fixed \(s>0\) and \(x,y\in\mathbb R\), with \(t_N=s/(r\log N)\),
\[
\lim_{N\to\infty}\Pr\{Y_N(0)\le x,\;Y_N(t_N)\le y\}=F_s(x,y),
\]
where
\[
F_s(x,y)=\int_0^\infty e^{-a}\exp\!\left[-e^{-x}\Phi\!\left(\lambda_a+\frac{y-x}{2\lambda_a}\right)-e^{-y}\Phi\!\left(\lambda_a+\frac{x-y}{2\lambda_a}\right)\right]da,
\quad \lambda_a=\sqrt{\frac{s}{2a}}.
\]
Each marginal is standard Gumbel, \(G(x)=\exp(-e^{-x})\). For all finite \(s>0\), the bivariate law \(F_s\) is not max-stable. Its *ordered-limit* upper-tail dependence coefficient obeys the exact universal identity
\[
\chi(s):=\lim_{h\to\infty}\frac{\Pr\{Y_0>h,\;Y_s>h\}}{\Pr\{Y_0>h\}}=e^{-\sqrt{s}},
\]
where \((Y_0,Y_s)\) is distributed according to \(F_s\). Neither \(D\) nor \(r\) enters this scaling law. The order of limits is first \(N\to\infty\) at fixed \(s,x,y\), then \(h\to\infty\).

## Assumptions and scope
Particle driving Brownian motions are independent; the Poisson clock is independent of them and is common to all particles; every clock event resets every particle to zero. The process is observed in its stationary two-sided construction. For each \(N\), both observations use the same \(N\) particles and common clock. The observation lag vanishes as \(s/(r\log N)\), with \(s\) fixed and positive. The empirical second moment is calculated independently at each observation time. No thermodynamic limit at fixed nonvanishing physical lag is asserted.

## Proof
**1. Stationary backward age and conditional Gaussian structure.** At time zero, the elapsed time since the last common reset, \(A\), is exponentially distributed with rate \(r\). Put \(a=rA\); then \(a\) has density \(e^{-a}\) on \((0,\infty)\). The probability of no reset during \([0,t_N]\) equals \(e^{-rt_N}=e^{-s/\log N}\to1\). Hence replacing the full two-time experiment by its no-intervening-reset restriction changes the joint event probability by at most \(1-e^{-s/\log N}\to0\).

Fix \(a>0\). Conditional on this age and no subsequent reset, the \(N\) particle pairs are independent and identically distributed centered Gaussian pairs. Their variances are \(\sigma_0^2=2Da/r\) and \(\sigma_1^2=2D(a/r+t_N)\). After division by the respective standard deviations, each pair has unit marginal variances and correlation
\[
\rho_N(a)=\sqrt{\frac{a}{a+s/\log N}},\qquad
(1-\rho_N(a))\log N\longrightarrow\frac{s}{2a}=\lambda_a^2.
\]
The sample second moments obey \(V_N(jt_N)/\sigma_j^2=1+O_{\Pr}(N^{-1/2})\) for \(j=0,1\), conditional on \(a\). Meanwhile the maximum of \(N\) standard Gaussian samples is \(O_{\Pr}(b_N)\), with \(b_N^2\sim2\log N\). Thus replacing each empirical normalization \(\sqrt{V_N}\) by its conditional deterministic \(\sigma_j\) changes the corresponding edge \(Y_N\) by \(O_{\Pr}(b_N^2/\sqrt N)=o_{\Pr}(1)\).

**2. Conditional extremal law, with its critical correlation normalization.** Set \(u_N(z)=b_N+z/b_N\). The standard Gaussian tail asymptotics give
\[
N\Pr\{Z>u_N(z)\}\to e^{-z},\qquad
\frac N{b_N}\varphi(b_N+v/b_N)\to e^{-v},
\]
where \(Z\) is standard normal and \(\varphi\) its density. For a Gaussian pair \((Z_0,Z_1)\) with correlation \(\rho_N(a)\), condition on \(Z_0=b_N+v/b_N\). Then the conditional law of \(b_N(Z_1-Z_0)\) converges to a Gaussian law with mean \(-2\lambda_a^2\) and variance \(4\lambda_a^2\). Consequently the limiting intensity of *joint* upper exceedances is
\[
\begin{aligned}
I_a(x,y)&=\lim_{N\to\infty}N\Pr\{Z_0>u_N(x),\;Z_1>u_N(y)\}\\
&=\int_x^\infty e^{-v}\Phi\!\left(\frac{v-y-2\lambda_a^2}{2\lambda_a}\right)dv\\
&=e^{-x}\Phi\!\left(-\lambda_a+\frac{x-y}{2\lambda_a}\right)
+e^{-y}\Phi\!\left(-\lambda_a+\frac{y-x}{2\lambda_a}\right).
\end{aligned}
\]
The final equality follows by integration by parts and a Gaussian change of variables. Inclusion-exclusion therefore gives the limiting *union* upper-exceedance intensity
\[
H_a(x,y)=e^{-x}\Phi\!\left(\lambda_a+\frac{y-x}{2\lambda_a}\right)
+e^{-y}\Phi\!\left(\lambda_a+\frac{x-y}{2\lambda_a}\right).
\]
Independence across particle pairs shows
\[
\Pr\{\max_i Z_{i,0}\le u_N(x),\;\max_i Z_{i,1}\le u_N(y)\mid a,\text{no reset}\}\longrightarrow e^{-H_a(x,y)}.
\]
The conditional empirical-normalization error does not alter this continuous limiting law. Bounded convergence over the exponential backward-age density yields precisely the stated \(F_s\), and the disappearing probability of an intervening reset completes the argument. This establishes convergence for every real \(x,y\) and every finite \(s>0\).

**3. Strict non-max-stability.** On the diagonal,
\[
F_s(x,x)=\mathbb E\left[\exp\{-V_s e^{-x}\}\right],\qquad
V_s=2\Phi\left(\sqrt{s/(2A_*)}\right),\quad A_*\sim\operatorname{Exp}(1).
\]
For fixed finite \(s>0\), the random variable \(V_s\) is nonconstant and lies strictly between \(1\) and \(2\). Strict Cauchy–Schwarz therefore implies
\[
F_s(x+\log2,x+\log2)^2
=\big(\mathbb E[e^{-V_s e^{-x}/2}]\big)^2
<\mathbb E[e^{-V_s e^{-x}}]=F_s(x,x).
\]
A max-stable bivariate distribution with standard Gumbel margins would satisfy equality for this same shift and square, contradicting max-stability.

**4. Exact upper-tail dependence.** Since each marginal is standard Gumbel and \(0<V_s<2\), bounded Taylor expansion on the diagonal gives
\[
\Pr\{Y_0>h,Y_s>h\}=
\left(2-\mathbb E V_s\right)e^{-h}+O(e^{-2h}),
\qquad \Pr\{Y_0>h\}=e^{-h}+O(e^{-2h}).
\]
Writing \(a\) for the exponential age, the coefficient is
\[
\chi(s)=\int_0^\infty e^{-a}\operatorname{erfc}\left(\sqrt{\frac{s}{4a}}\right)da.
\]
For \(c\ge0\), set \(J(c)=\int_0^\infty e^{-a}\operatorname{erfc}(c/\sqrt a)\,da\). Differentiation under the integral for \(c>0\) and the elementary Gaussian integral
\[
\int_0^\infty a^{-1/2}e^{-a-c^2/a}\,da=\sqrt\pi e^{-2c}
\]
give \(J'(c)=-2e^{-2c}\). As \(J(0)=1\), \(J(c)=e^{-2c}\). Substitution \(c=\sqrt{s}/2\) proves \(\chi(s)=e^{-\sqrt{s}}\). Limits \(s\downarrow0\) and \(s\uparrow\infty\) in the mixed bivariate CDF give, respectively, complete edge dependence and independent Gumbel extremes by dominated convergence.

## Verification
Run `python check.py` with NumPy and SciPy installed. The bundled checker performs 82 numerical assertions, including two different age-integral quadratures, the exact complementary-error-function integral identity, explicit finite-\(N\) Gaussian upper-union probabilities, non-max-stability, limiting extreme-dependence endpoints, and a Monte Carlo check with self-normalization. All 82 assertions passed when executed against the bundled file. Numerical calculations test finite formulas and asymptotic tendencies; the proof above establishes the infinite-population claims. In particular, finite-particle simulation is not used as a replacement for the conditional Gaussian-extremes argument.

## Relationship to prior work
Biroli, Larralde, Majumdar, and Schehr (2022) derived the common-reset Brownian gas, the exponential stationary resetting-age mixture, and *single-time* extreme-particle statistics. These model ingredients and the age-mixture construction are prior results. Le Doussal (2023) developed two-time Hüsler–Reiss-type extremal laws for freely diffusing independent Brownian particles: the fixed-age conditional extreme law used here is likewise prior mathematical machinery. The present finding concerns the **common-reset stationary gas with empirical-width self-normalization** and its resulting non-max-stable *mixture* at lag \(s/(r\log N)\), including the evaluated universal exponential-square-root tail-dependence coefficient. De Mauro, Biroli, Majumdar, and Schehr (2025) analyze simultaneous non-Poissonian resetting, including single-time positional observables; their work was considered for related coverage. An equivalent unlocated specialization of general bivariate-extreme or resetting formulas remains possible.

## Limitations
The theorem requires a single shared Poisson clock and complete resetting to a common point; it does not cover independent clocks, heterogeneous diffusivities, interacting particles, non-Brownian dynamics, or general renewal resetting. The lag depends on population size through \(1/\log N\). The tail coefficient \(\chi\) is defined only for the limiting bivariate law and cannot be read as an ordinary fixed-\(N\) asymptotic upper-tail coefficient; interchange of the population and upper-threshold limits is not asserted. The result is established mathematically and by internal numerical checks but has not undergone independent audit or definitive mathematical priority review.

## References
1. M. Biroli, H. Larralde, S. N. Majumdar, G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, arXiv:2211.00563v1 (first public version 2022-11-01), https://arxiv.org/abs/2211.00563.
2. P. Le Doussal, *Dynamics at the edge for independent diffusing particles*, arXiv:2308.16709v1 (first public version 2023-08-31), https://arxiv.org/abs/2308.16709.
3. L. de Mauro, M. Biroli, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658 (2025), https://arxiv.org/abs/2509.06658.
4. J. Hüsler and R.-D. Reiss, *Maxima of normal random vectors: between independence and complete dependence*, Statistics & Probability Letters 7 (1989), 283–286.
