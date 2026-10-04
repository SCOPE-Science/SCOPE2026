# Extreme-particle pinning thresholds for alpha-Wiener mean-field bridges

## Finding
Consider the equal-weight pinned interacting diffusion on one segment \([0,T)\), with no common noise, diffusion scale \(\sigma>0\), and interaction rate
\[
f(t)=\frac{\alpha}{T-t},\qquad \alpha>0.
\]
Let
\[
A_t=\frac1n\sum_{i=1}^n X_i(t),\qquad M_n(t)=\max_{1\le i\le n}|X_i(t)-A_t|.
\]
Define
\[
v_\alpha(t)=\int_0^t\left(\frac{T-t}{T-s}\right)^{2\alpha}\,ds.
\]
Then, for every \(t<T\),
\[
M_n(t)\stackrel{d}{=}\sigma\sqrt{v_\alpha(t)}\max_{1\le i\le n}|Z_i-\bar Z_n|,
\]
where \(Z_1,\ldots,Z_n\) are independent standard Gaussian variables and \(\bar Z_n=n^{-1}\sum_i Z_i\).

Hence, for every deterministic sequence \(t_n<T\),
\[
\frac{M_n(t_n)}{\sigma\sqrt{2v_\alpha(t_n)\log n}}\xrightarrow{P}1.
\]
With
\[
b_n=\sqrt{2\log n}-\frac{\log\log n+\log\pi}{2\sqrt{2\log n}},
\]
the sharper extreme-value limit is
\[
b_n\left(\frac{M_n(t_n)}{\sigma\sqrt{v_\alpha(t_n)}}-b_n\right)\Rightarrow G,
\qquad \Pr(G\le x)=\exp(-e^{-x}).
\]

Writing \(\delta_n=T-t_n\), simultaneous pinning of every particle, \(M_n(t_n)\to0\) in probability, is equivalent to
\[
v_\alpha(t_n)\log n\to0.
\]
The exact variance factor is
\[
v_\alpha(t)=
\begin{cases}
\displaystyle \frac{\delta^{2\alpha}\bigl(T^{1-2\alpha}-\delta^{1-2\alpha}\bigr)}{1-2\alpha},&\alpha\ne\tfrac12,\\[6pt]
\displaystyle \delta\log(T/\delta),&\alpha=\tfrac12,
\end{cases}
\qquad \delta=T-t.
\]
Therefore the critical terminal-window scale is \((\log n)^{-1/(2\alpha)}\) for \(0<\alpha<1/2\), \((\log n\log\log n)^{-1}\) for \(\alpha=1/2\), and \((\log n)^{-1}\) for \(\alpha>1/2\). More precisely, if \(v_\alpha(t_n)\log n\to\ell\in(0,\infty)\), then
\[
M_n(t_n)\xrightarrow{P}\sigma\sqrt{2\ell},
\]
whereas \(v_\alpha(t_n)\log n\to\infty\) forces \(M_n(t_n)\to\infty\) in probability.

## Assumptions and scope
The statement concerns a single segment starting at zero, a simple ensemble average, no common Brownian noise, equal idiosyncratic diffusion scale, and the specific singular interaction \(f(t)=\alpha/(T-t)\). Initial conditions may be common because they cancel from \(X_i-A\). The result is a joint particle-number/terminal-time statement; it does not claim a corresponding law for weighted averages, nonzero common-noise coefficients after unequal weighting, heterogeneous diffusion coefficients, or non-Gaussian drivers.

The source model proves pathwise pinning for every fixed finite particle system and identifies the \(\alpha\)-Wiener-bridge specialization. It explicitly states that the effect of the interaction function on convergence rate, and the rate of its pointwise spatial limit, are left for future study. The present statement addresses a distinct uniform-over-particles rate question in that specialization.

## Proof
Subtracting the ensemble-average equation from the particle equation gives
\[
d\bigl(X_i(t)-A_t\bigr)
=-\frac{\alpha}{T-t}\bigl(X_i(t)-A_t\bigr)\,dt
+\sigma\bigl(dW_i(t)-d\bar W_n(t)\bigr),
\]
where \(\bar W_n=n^{-1}\sum_i W_i\). Variation of constants therefore yields
\[
X_i(t)-A_t
=\sigma\left(Q_i(t)-\bar Q_n(t)\right),
\]
with
\[
Q_i(t)=\int_0^t\left(\frac{T-t}{T-s}\right)^\alpha dW_i(s),
\qquad
\bar Q_n(t)=\frac1n\sum_i Q_i(t).
\]
At fixed \(t<T\), the variables \(Q_i(t)\) are independent centered Gaussians with common variance \(v_\alpha(t)\). Thus \(Q_i(t)=_d\sqrt{v_\alpha(t)}Z_i\), proving the exact finite-\(n\) reduction.

Let \(H_n=\max_i|Z_i-\bar Z_n|\) and \(R_n=\max_i|Z_i|\). The deterministic inequality
\[
|H_n-R_n|\le |\bar Z_n|
\]
shows that centering by the sample mean is negligible on the extreme scale because
\[
\sqrt{\log n}\,|\bar Z_n|\xrightarrow{P}0.
\]
Standard Gaussian tail bounds give
\[
\frac{R_n}{\sqrt{2\log n}}\xrightarrow{P}1,
\]
so the same holds for \(H_n\), which proves the first-order formula uniformly along every deterministic sequence \(t_n<T\) because the time dependence is only the deterministic factor \(\sigma\sqrt{v_\alpha(t_n)}\).

For the second-order law, Gaussian Mills asymptotics give, for every fixed \(x\in\mathbb R\),
\[
n\Pr\left(|Z_1|>b_n+\frac{x}{b_n}\right)\longrightarrow e^{-x}.
\]
Independence implies
\[
\Pr\left(b_n(R_n-b_n)\le x\right)\longrightarrow\exp(-e^{-x}).
\]
Since \(b_n|H_n-R_n|\le b_n|\bar Z_n|\xrightarrow{P}0\), Slutsky's theorem transfers the Gumbel limit to \(H_n\), and hence to the normalized particle maximum.

Finally, direct integration gives the displayed closed form for \(v_\alpha\). As \(\delta=T-t\downarrow0\),
\[
v_\alpha(t)\sim
\begin{cases}
\displaystyle \frac{T^{1-2\alpha}}{1-2\alpha}\,\delta^{2\alpha},&0<\alpha<\tfrac12,\\[6pt]
\delta\log(T/\delta),&\alpha=\tfrac12,\\[4pt]
\displaystyle \frac{\delta}{2\alpha-1},&\alpha>\tfrac12.
\end{cases}
\]
Combining these equivalents with \(H_n/\sqrt{2\log n}\to1\) gives the three critical windows and all three product regimes.

## Verification
The proof uses only the exact Gaussian representation, elementary integration, Gaussian tail asymptotics, and the sample-mean estimate. The accompanying deterministic checker recomputes \(v_\alpha(t)\) against numerical quadrature at representative parameters and checks the Gaussian extreme-value tail normalization for increasing \(n\). These computations are sanity checks rather than substitutes for the analytic proof.

## Relationship to prior work
Mengütürk and Mengütürk, *Mean-field interacting systems with sequential coalescence at future ensemble averages*, DOI:10.1017/jpr.2025.10032, provide the model, prove pinning at every segment terminus, derive the residual representation, and in Example 2.1 choose \(f(t)=\alpha/(T-t)\), identifying the resulting limiting process as an \(\alpha\)-Wiener bridge. Their Remark 2.1 states that the interaction function controls convergence speed and leaves a detailed rate study for future research; their spatial-limit discussion separately states that its convergence is pointwise and leaves the rate for future work.

Barczy and Pap, arXiv:0810.3070 and the subsequent journal article, study the sample-path endpoint behavior of one \(\alpha\)-Wiener bridge. That single-process endpoint theory supplies important background but does not compare the endpoint distance with a growing particle count or derive the maximum-over-particles transition and its Gumbel profile.

Mengütürk, DOI:10.1088/1751-8121/ac2715, treats the earlier one-segment interacting system and its mean-field \(\alpha\)-Wiener limit. Del Moral and Rio, DOI:10.1214/10-AAP716, develop general concentration inequalities for broad mean-field particle models. Neither inspected source states the exact centered-Gaussian maximum reduction or the three terminal-window thresholds above.

## Limitations
The result is exact only for the equal-weight Gaussian specialization with no common noise and the singular interaction \(f(t)=\alpha/(T-t)\). It does not prove a universal extreme-particle rate for the full sequential model, for arbitrary admissible interaction functions, or for heterogeneous weights. It also does not address maxima over continuous time, only maxima over particles at a chosen time \(t_n\). The Gumbel refinement concerns the Gaussian specialization and should not be extrapolated to non-Gaussian drivers without additional tail assumptions.

## References
1. L. A. Mengütürk and M. C. Mengütürk, *Mean-field interacting systems with sequential coalescence at future ensemble averages*, Journal of Applied Probability, DOI:10.1017/jpr.2025.10032. First published online 2025-10-13.
2. M. Barczy and G. Pap, *alpha-Wiener bridges: singularity of induced measures and sample path properties*, arXiv:0810.3070; Stochastic Analysis and Applications 28 (2010), 447–466.
3. L. A. Mengütürk, *A family of interacting particle systems pinned to their ensemble average*, Journal of Physics A 54 (2021), 435001, DOI:10.1088/1751-8121/ac2715.
4. P. Del Moral and E. Rio, *Concentration inequalities for mean field particle models*, Annals of Applied Probability 21 (2011), DOI:10.1214/10-AAP716.
