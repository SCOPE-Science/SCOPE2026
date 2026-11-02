# Equilibrium-age inflation of threshold occupation fluctuations under Poisson resetting

## Finding
For geometric Brownian motion with independent Poisson resets to \(x_0>0\), the stationary preparation has **strictly larger variance of the finite-window fraction spent above \(x_0\)** than preparation by a fresh reset, at **every** positive observation duration. There is an exact initial-factor-two enhancement, a strictly positive all-duration difference, and a sharp \((rT)^{-2}\) long-window variance gap, even when positive wealth moments are infinite.

Precisely, for \(r,\sigma,x_0>0\), let the process between resets obey
\[
dX_t=\frac{\sigma^2}{2}X_t\,dt+\sigma X_t\,dW_t,
\]
with independent rate-\(r\) resets \(X\mapsto x_0\). For the bounded threshold fraction \(U_T=T^{-1}\int_0^T\mathbf1_{\{X_t>x_0\}}\,dt\), write \(V_{\rm eq}(T)\) for its variance under the strictly stationary law and \(V_{\rm fresh}(T)\) for its variance starting at \(X_0=x_0\) at time zero. Put \(z=rT\). Then
\[
V_{\rm fresh}(T)=\frac{z-1+e^{-z}}{4z^2},
\]
and
\[
V_{\rm eq}(T)=\frac{(4z^2-4z+3)\operatorname{erfc}(\sqrt z)+4z-3+2\sqrt z(3-2z)e^{-z}/\sqrt\pi}{16z^2}.
\]
For every \(T>0\),
\[
0<V_{\rm fresh}(T)<V_{\rm eq}(T)<\frac14.
\]
Moreover,
\[
\lim_{T\downarrow0}\frac{V_{\rm eq}(T)}{V_{\rm fresh}(T)}=2,
\qquad\lim_{T\to\infty}(rT)^2\big(V_{\rm eq}(T)-V_{\rm fresh}(T)\big)=\frac1{16}.
\]

## Assumptions and scope
The Brownian increments are independent across reset excursions and independent of the two-sided stationary Poisson reset clock. The drift choice makes the log-relative position \(Y_t=\log(X_t/x_0)\) a driftless Brownian motion with volatility \(\sigma>0\) between resets to zero. In the equilibrium version the backward age at time zero is exponential of rate \(r\). In the fresh version time zero is a reset epoch. All signs are understood modulo a null set of zero-level times. Each variance concerns the temporal occupation fraction on the same deterministic interval \([0,T]\), not wealth's random-time stationary distribution. The theorem holds for all positive \(r,\sigma,T\) with no moment assumptions on wealth.

## Proof
At age \(a>0\), conditional on no reset during the subsequent lag \(t>0\), the ordered log coordinates are jointly Gaussian with covariance correlation \(\sqrt{a/(a+t)}\). The standard centered Gaussian quadrant identity therefore yields
\[
h(a,t):=\mathbb E[\operatorname{sgn}(Y_0)\operatorname{sgn}(Y_t)\mid a,\text{no reset}]
=\frac2\pi\arcsin\sqrt{\frac a{a+t}}=\frac2\pi\arctan\sqrt{\frac at}.
\]
The function \(h(a,t)\) is strictly increasing in \(a>0\). If a reset occurs between the two observations, the later sign is independent of the earlier and has conditional mean zero, so it contributes zero to sign covariance.

For the stationary process the backward age \(A\) is \(\operatorname{Exp}(r)\), independent of future resets. Its sign correlation is consequently
\[
C_{\rm eq}(t)=e^{-rt}\int_0^\infty re^{-ra}h(a,t)\,da
=\operatorname{erfc}(\sqrt{rt}).
\]
The last equality follows by integration by parts: differentiating \(\arctan\sqrt{a/t}\) gives \(\sqrt t/[2\sqrt a(a+t)]\), and the remaining elementary Laplace integral yields \(e^{rt}\operatorname{erfc}(\sqrt{rt})\) after cancellation of constants. The threshold indicator is \((1+\operatorname{sgn}Y)/2\), so its centered covariance is \(C/4\). Stationarity and double integration give
\[
V_{\rm eq}(T)=\frac1{2T^2}\int_0^T(T-t)C_{\rm eq}(t)\,dt.
\]
Elementary integrations of \(\operatorname{erfc}\) after substituting \(u=rt\) give the closed expression in the Finding.

For the freshly prepared process, at observation time \(s\ge0\), the age of the current excursion is distributed as \(A_s=\min(E,s)\) for \(E\sim\operatorname{Exp}(r)\), independently of resets after \(s\). Consequently its sign covariance at \(s<s+t\) is \(e^{-rt}\mathbb E[h(A_s,t)]\). Couple this with equilibrium age \(A=E\) on the same probability space. Since \(A_s\le A\) almost surely and \(\mathbb P(A>s)>0\), strict monotonicity of \(h\) gives
\[
\operatorname{Cov}_{\rm fresh}(\mathbf1_{Y_s>0},\mathbf1_{Y_{s+t}>0})
<\operatorname{Cov}_{\rm eq}(\mathbf1_{Y_0>0},\mathbf1_{Y_t>0})
\]
for every \(s\ge0,t>0\); both indicator means equal \(1/2\) when observation times are positive. Integration over the positive-area triangular domain \(0<s<s+t<T\) proves \(V_{\rm fresh}(T)<V_{\rm eq}(T)\) **without** relying on numerical inequalities between closed forms. Positivity and the strict \(1/4\) upper bound follow because both fractions lie in \([0,1]\), have mean \(1/2\), and are nondegenerate with strictly positive probability of changing sign in finite windows.

For completeness the fresh variance can be computed independently by conditioning on the number \(N\sim\operatorname{Poisson}(z)\) of resets in \([0,T]\). Its \(N+1\) Brownian excursion lengths divided by \(T\) have the uniform-Dirichlet law. Conditional on these lengths, excursion occupation fractions are independent standard arcsine fractions of mean \(1/2\), variance \(1/8\). The Dirichlet second-moment identity then yields
\[
\operatorname{Var}(U_T\mid N=n)=\frac1{8}\mathbb E\sum_{j=1}^{n+1}(L_j/T)^2=\frac1{4(n+2)}.
\]
Poisson averaging gives \(\mathbb E[(N+2)^{-1}]=(z-1+e^{-z})/z^2\), hence the fresh closed form. Finally the equilibrium expression has limits \(V_{\rm eq}\to1/4\) at zero and \(V_{\rm eq}=1/(4z)-3/(16z^2)+o(z^{-2})\) at infinity, whereas \(V_{\rm fresh}\to1/8\) and \(V_{\rm fresh}=1/(4z)-1/(4z^2)+o(z^{-2})\). This gives the two sharp asymptotic comparisons.

## Verification
The included independent `verify.py` evaluates conditional Gaussian-sign integrals, direct numerical integrations of equilibrium occupation covariance, closed forms, independent Poisson-mixture fresh variances, and finite-age covariance comparisons at 47 parameter instances. These finite checks are supplementary to the all-duration stochastic-dominance proof and do not certify any untested model.

## Relationship to prior work
Stojkoski, Sandev, Kocarev and Pal (2021) introduce resetting geometric Brownian motion and establish its stationary and nonergodic regimes. The Brownian-log reduction here deliberately uses the zero-log-drift parameter surface. den Hollander, Majumdar, Meylahn and Touchette (2018) treat additive occupation functionals starting from reset initial conditions; Taźbierski and Magdziarz (2025) give the fresh-reset Brownian arcsine occupation laws, so neither their fresh occupation distributions nor their established moments are claimed novel. Taźbierski, Metzler and Magdziarz (2025) derive general two-time resetting densities, and Dębicki, Hashorva and Michna (2026) give stationary two-dimensional distributions, from which individual sign correlations can in principle be computed. The targeted new statement is the **strict equilibrium-age versus fresh-age variance ordering for every finite window**, including its explicit exact and sharp asymptotic comparison, proved directly by an age-monotone Gaussian coupling, not a claimed new general two-point law.

## Limitations
This is a model-specific strict ordering for drift-neutral log Brownian motion with memory-erasing Poisson resets. Nonzero log drift, non-Poisson reset times, or sign indicators at other thresholds need not follow. The two-point sign formula itself is obtainable from previously published joint densities and is not asserted as an independent general distributional discovery. The proof supplies no entropy-production formula, no finite-sample estimation theorem and no independent external validation. The distinction between nonergodicity of wealth and stable bounded threshold-time averages is descriptive, not a claim that all observables are ergodic.

## References
- V. Stojkoski, T. Sandev, L. Kocarev, A. Pal, *Geometric Brownian Motion under Stochastic Resetting: A Stationary yet Non-ergodic Process* (2021), arXiv:2104.01571, https://arxiv.org/abs/2104.01571.
- F. den Hollander, S. N. Majumdar, J. M. Meylahn, H. Touchette, *Properties of additive functionals of Brownian motion with resetting* (2018), arXiv:1801.09909, https://arxiv.org/abs/1801.09909.
- K. Taźbierski, M. Magdziarz, *Arcsine laws for Brownian motion with Poissonian resetting* (2025), arXiv:2502.03889, https://arxiv.org/abs/2502.03889.
- K. Taźbierski, R. Metzler, M. Magdziarz, *Series representation approach to stochastic processes with complete and incomplete renewal resetting* (2025), New Journal of Physics 27, 074603, https://doi.org/10.1088/1367-2630/adee40.
- K. Dębicki, E. Hashorva, Z. Michna, *Distributional and Extremal Behaviour of Brownian Motion with Exponential Resetting* (2026), arXiv:2603.03050, https://arxiv.org/abs/2603.03050.
