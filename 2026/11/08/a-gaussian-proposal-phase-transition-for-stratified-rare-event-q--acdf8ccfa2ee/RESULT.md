# A Gaussian-proposal phase transition for stratified rare-event quadrature

## Finding
Fix a threshold \(z>0\), a proposal variance \(s>0\), and the standard normal density \(\phi\) and cumulative distribution \(\Phi\). Estimate \(p_z=\Pr\{Z\ge z\}=1-\Phi(z)\) for \(Z\sim N(0,1)\), using the proposal \(N(0,s)\) and one independent inverse-proposal sample in each of \(n\) equal probability strata. Write \(U_j\overset{\mathrm{iid}}\sim\operatorname{Uniform}(0,1)\), \(u_j=(j-1+U_j)/n\), and
\[
Q_{n,s}=\frac1n\sum_{j=1}^n h_s(u_j),\quad h_s(u)=\sqrt{s}\exp\!\left(\frac{1-s}{2}[\Phi^{-1}(u)]^2\right)\mathbf1\{u\ge u_*\},\quad u_*=\Phi(z/\sqrt{s}).
\]
The estimator is unbiased for every \(n\ge1\).

**Underdispersed proposals.** For \(0<s<1\), let \(\beta=1-s\) and \(A_s=\sqrt{s}(4\pi)^{-\beta/2}\). On a probability space carrying independent uniform \(V_k\), set
\[
T_s=A_s\sum_{k=1}^{\infty}\left[(k-1+V_k)^{-\beta}-\int_{k-1}^k t^{-\beta}\,dt\right].
\]
The series converges in \(L^1\) and almost surely. With \(p_z=1-\Phi(z)\),
\[
 n^s(\log n)^{(1-s)/2}(Q_{n,s}-p_z)\ \Longrightarrow\ T_s.
\]
The limit is non-Gaussian, bounded below, and has the exact right-tail constant
\[
\lim_{x\to\infty}x^{1/(1-s)}\Pr\{T_s>x\}=A_s^{1/(1-s)}.
\]
For every \(p>0\), \(\mathbb E|Q_{n,s}|^p<\infty\) if and only if \(p(1-s)<1\). In particular, \(\operatorname{Var}(Q_{n,s})=\infty\) for every \(n\) when \(s\le1/2\). When \(1/2<s<1\), there is the *sharp positive variance asymptotic*
\[
\lim_{n\to\infty}n^{2s}(\log n)^{1-s}\operatorname{Var}(Q_{n,s})
=s(4\pi)^{-(1-s)}\sum_{k=1}^{\infty}\left[\int_{k-1}^k t^{-2(1-s)}\,dt-\left(\int_{k-1}^k t^{-(1-s)}\,dt\right)^2\right].
\]
Its leading constant and limiting distribution do not depend on the fixed event threshold \(z\).

**Matched or overdispersed proposals.** For \(s\ge1\), let \(\theta_n=\{nu_*\}\) be the fractional part and \(w_s(z)=\sqrt{s}\exp((1-s)z^2/(2s))\). Then
\[
 n^2\operatorname{Var}(Q_{n,s})=w_s(z)^2\theta_n(1-\theta_n)+o(1).
\]
Along any subsequence with \(\theta_n\to\theta\in[0,1]\),
\[
 n(Q_{n,s}-p_z)\Longrightarrow w_s(z)\bigl(B_{1-\theta}-(1-\theta)\bigr),
\]
where \(B_{1-\theta}\) is Bernoulli with success probability \(1-\theta\). For \(s=1\), the variance formula without its \(o(1)\) term and the Bernoulli identity hold for every \(n\) (with the phase \(\theta_n\)). If \(u_*\) is irrational, the cluster set of \(n^2\operatorname{Var}(Q_{n,s})\) is exactly \([0,w_s(z)^2/4]\).

## Assumptions and scope
The proposal variance \(s\) is the *variance*, not its standard deviation. The threshold \(z\) is any fixed strictly positive real number, and \(n\) tends through positive integers. Sampling is independent across equal-proposal-probability strata; the only random variables used in the rule are the independent uniforms \(U_j\). All equalities concern exact arithmetic and a fixed \(s,z\); the result does not address adaptively chosen proposals, multivariate events, dependence between strata, or thresholds drifting with \(n\).

## Proof
**1. Exact change of measure.** With \(x=\sqrt{s}\Phi^{-1}(u)\) and Gaussian proposal density \(q_s(x)=s^{-1/2}\phi(x/\sqrt{s})\), the importance weight is
\[
\frac{\phi(x)}{q_s(x)}=\sqrt{s}\exp\!\left(\frac{1-s}{2s}x^2\right).
\]
Thus \(\int_0^1h_s(u)\,du=p_z\). The expectation of the contribution of the \(j\)-th stratum is precisely \(\int_{(j-1)/n}^{j/n}h_s(u)\,du\), proving unbiasedness.

**2. The endpoint law.** Write \(v=1-u\), and \(g_s(v)=h_s(1-v)\). The normal Mills asymptotic
\[
1-\Phi(t)\sim\frac{e^{-t^2/2}}{t\sqrt{2\pi}},\qquad t\to\infty,
\]
combined with \(t\sim\sqrt{2\log(1/v)}\), gives, for \(0<s<1\),
\[
g_s(v)\sim A_s v^{-\beta}\bigl(\log(1/v)\bigr)^{-\beta/2},\quad v\downarrow0.
\]
The same calculation after logarithmic differentiation gives \(|g_s'(v)|\le C v^{-\beta-1}(\log(1/v))^{-\beta/2}\) for sufficiently small \(v\). For every fixed right-endpoint stratum \(k\), with \(v=(k-1+V_k)/n\), the centered, scaled stratum contribution tends to
\[
A_s\left[(k-1+V_k)^{-\beta}-\int_{k-1}^k t^{-\beta}\,dt\right].
\]
For \(k\ge2\), the absolute size of this limiting centered summand is bounded by \((k-1)^{-\beta}-k^{-\beta}\); these bounds telescope, establishing absolute convergence of the tail of the series. The \(k=1\) term is integrable because \(\beta<1\); hence the series converges in \(L^1\) and almost surely.

For completeness, the remainder can be controlled uniformly, rather than assuming pointwise convergence suffices. The scaled oscillation of a cell indexed \(k\ge2\) with \(k\le n^{1/2}\) is at most \(C(k-1)^{-\beta-1}\). For \(n^{1/2}<k\le n v_0\), the sum of scaled oscillations is \(O(n^{-\beta/2}(\log n)^{\beta/2})\) after possibly reducing the fixed small \(v_0\). On the remaining compact interval away from \(v=0\), \(g_s\) has finite total variation, including its single jump at \(v=1-u_*\), so the total centered contribution after scaling is \(O(n^{-\beta}(\log n)^{\beta/2})\) in \(L^1\). The first cell converges in \(L^1\) by a Potter bound with exponent strictly between \(\beta\) and \(1\). Truncate at fixed \(K\), take \(n\to\infty\), then \(K\to\infty\). This proves the announced \(L^1\) convergence under a natural coupling, hence convergence in law. For \(\beta<1/2\), use Potter exponents below \(1/2\) and square the tail oscillation bounds; the same argument proves \(L^2\) convergence.

**3. Moments, sharp variance and tail.** Because \(g_s(v)\) is nonnegative and behaves as above, its \(p\)-th power is locally integrable at zero exactly when \(p\beta<1\). At equality the divergent local integral is proportional to \(\int_0 v^{-1}(\log(1/v))^{-1/2}\,dv\). A sampled endpoint cell exists for every \(n\), so all moments of the full nonnegative estimator have the same threshold. When \(\beta<1/2\), \(L^2\) convergence and independence give the claimed sum of within-unit-interval variances and its strictly positive finite value. For the upper tail, the first series term is \(A_s(V_1^{-\beta}-(1-\beta)^{-1})\); all remaining terms form a *uniformly bounded* random variable because their maximal deviations telescope. Hence the probability tail is asymptotic to that of \(A_s V_1^{-\beta}\), proving the exact coefficient and showing the limit cannot be Gaussian.

**4. The jump-phase law.** For \(s>1\), the function \(h_s\) is bounded, continuous and of bounded variation separately on \([0,u_*)\) and \([u_*,1]\), with a jump of height \(w_s(z)\) at \(u_*\). Indeed \(h_s(u)\to0\) at \(u\uparrow1\). The sum of cell oscillations away from the single jump cell is bounded by the total variation on those intervals; its largest cell oscillation tends to zero by uniform continuity. Therefore the sum of their centered cell variances tends to zero. In the jump cell, after scaling by \(n\), the centered fluctuation converges in \(L^2\) to \(w_s(z)[\mathbf1\{U>\theta_n\}-(1-\theta_n)]\), uniformly in the phase. Independence gives both the uniform variance expansion and the Bernoulli subsequential limit. For \(s=1\), the weight equals one, so only the jump cell contributes and these formulas are exact. Finally, for irrational \(u_*\), the fractional parts \(\{nu_*\}\) are dense in \([0,1]\); continuity of \(\theta(1-\theta)\) gives the full cluster interval.

## Verification
A standalone standard-library checker, `verify_rare_event.py`, computes finite-\(n\) variances from Gaussian integral identities, checks the matched-proposal Bernoulli identity for every tested grid, and compares normalized variance against the sharp constants in the underdispersed and overdispersed regimes. For \(s>1/2\), writing \(\kappa=2-1/s\) and \(a_j=\sqrt{s}\Phi^{-1}((j-1)/n)\), \(b_j=\sqrt{s}\Phi^{-1}(j/n)\), the exact cell raw moments are
\[
 m_{1,j}=n[\Phi(b_j)-\Phi(\max\{a_j,z\})]_+,\quad m_{2,j}=n\sqrt{s/\kappa}[\Phi(\sqrt{\kappa}b_j)-\Phi(\sqrt{\kappa}\max\{a_j,z\})]_+,
\]
where a bracket is set to zero if \(b_j\le z\). Then \(\operatorname{Var}(Q_{n,s})=n^{-2}\sum_j(m_{2,j}-m_{1,j}^2)\). These identities provide exact-arithmetic specifications even when evaluated numerically. Computational checks are supporting evidence, not the infinite-\(n\) proof.

## Relationship to prior work
He, Zheng, and Wang (2022) study how Gaussian importance proposals affect randomized QMC convergence under boundary growth conditions. He (2017/2018) treats discontinuities combined with boundary singularities and establishes general error bounds. Liu (2024 preprint, 2025 journal) develops spectral variance-rate bounds for singular and discontinuous randomized QMC integrands. Owen (1997) supplies classical variance decompositions for scrambled nets. The present theorem concerns the exact one-dimensional *independently stratified* Gaussian tail-indicator problem: its distributional endpoint limit and Pareto constant, exact moment threshold, exact leading variance series, and arithmetic jump-phase limit. Those specific formulas were not found in the inspected sources. Broader specialized stratified-sampling literature may contain equivalent conclusions, so independent precedence review is still warranted.

## Limitations
These are exact results only for one fixed scalar Gaussian tail event and centered Gaussian proposals; neither variance-optimal proposal selection nor a guarantee for high-dimensional rare-event simulation follows. A finite \(n\) can be far from the limiting regime when \(s\) is close to the critical values. For \(s\le1/2\), classical variance and RMSE are undefined even though convergence in law remains valid. The arithmetic phase means there need not be an unconditional limiting law under \(s\ge1\). No independent external validation has been performed.

## References
1. Z. He, Z. Zheng and X. Wang, *On the error rate of importance sampling with randomized quasi-Monte Carlo*, arXiv:2203.03220 (first posted March 7, 2022), https://arxiv.org/abs/2203.03220.
2. Z. He, *Quasi-Monte Carlo for discontinuous integrands with singularities along the boundary of the unit cube*, arXiv:1702.03361 (first posted February 11, 2017), https://arxiv.org/abs/1702.03361.
3. Y. Liu, *Randomized quasi-Monte Carlo and Owen's boundary growth condition: A spectral analysis*, arXiv:2405.05181 (first posted May 8, 2024), https://arxiv.org/abs/2405.05181.
4. A. B. Owen, *Monte Carlo Variance of Scrambled Net Quadrature*, SIAM J. Numer. Anal. 34 (1997), 1884–1910, https://doi.org/10.1137/S0036142994277468.
