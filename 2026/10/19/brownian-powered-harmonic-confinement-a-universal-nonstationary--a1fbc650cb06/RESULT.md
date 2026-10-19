# Brownian-powered harmonic confinement: a universal nonstationary heavy-tail law

## Finding

A thermal particle subject to a harmonic stiffness proportional to a positive power of an *independent* Brownian environment has an explicit, non-Gaussian long-time scaling limit. For any power \(p>0\), the limiting distribution is a Gaussian variable divided by a power of another independent Gaussian variable. Its two-sided tail index is \(2/p\). In the Brownian-squared case \(p=2\), the limit is exactly Cauchy, although every finite-time position has moments of all positive orders. The limit remains unchanged on adding any fixed nonnegative baseline stiffness.

More precisely, put \(a_p=\sqrt{D/(\kappa\sigma^p)}\). As \(t\to\infty\), jointly with the Brownian environment,

\[
\left(\frac{B_t}{\sigma\sqrt t},\;t^{p/4}X_t\right)
\;\Longrightarrow\;
\left(G,\;a_p\frac{Z}{|G|^{p/2}}\right),
\]

where \(G,Z\) are independent standard normal variables. The companion self-normalized law is

\[
\left(\frac{B_t}{\sigma\sqrt t},\;|B_t|^{p/2}X_t\right)
\;\Longrightarrow\;
\left(G,\;\sqrt{\frac D\kappa}Z\right).
\]

In particular, the two limiting coordinates in the second display are independent. The absolute-tail law is

\[
\mathbb P\!\left(\left|a_p Z/|G|^{p/2}\right|>R\right)
\sim C_p R^{-2/p},\qquad
C_p=\sqrt{\frac2\pi}\,a_p^{2/p}\,\mathbb E|Z|^{2/p}
=\frac{2^{1/2+1/p}}\pi
\Gamma\!\left(\frac12+\frac1p\right)a_p^{2/p}.
\]

The limiting absolute moment of order \(q>0\) is finite precisely when \(q<2/p\). For \(q\ge2/p\), the finite-time renormalized moments diverge:

\[
\lim_{t\to\infty}t^{pq/4}\mathbb E|X_t|^q=+\infty.
\]

For \(p=2\), \(a_2 Z/|G|\) has the centered Cauchy density \(a_2/[\pi(a_2^2+y^2)]\). These are distributional and moment-divergence conclusions, not assertions of stationary position distributions.

## Assumptions and scope

Let \(W^{(1)}\) and \(W^{(2)}\) be independent standard real Brownian motions, on a common filtered probability space. Fix real numbers \(\sigma,\kappa,D>0\), \(p>0\), \(k_0\ge0\), and \(x_0\in\mathbb R\). Set \(B_t=\sigma W^{(1)}_t\), initially \(B_0=0\), and let \(X_t\) be the unique continuous adapted solution to

\[
 dX_t=-\left(k_0+\kappa|B_t|^p\right)X_t\,dt
       +\sqrt{2D}\,dW^{(2)}_t,\qquad X_0=x_0.
\]

This is a time-dependent, nonnegative-stiffness overdamped Langevin model; the driving thermal Brownian motion is independent of the stiffness Brownian motion. All parameters are fixed as \(t\to\infty\). Convergence is weak convergence of laws in \(\mathbb R^2\). An actual finite-time stationary distribution is not assumed or claimed. The reference \(p=2\) case has stochastic Brownian-squared harmonic stiffness. No result here requires \(k_0=0\).

## Proof

**1. Exact conditional Gaussian representation.** Define \(A_t=k_0t+\kappa\int_0^t|B_u|^p\,du\). Variation of constants gives

\[
 X_t=x_0e^{-A_t}+\sqrt{2D}\int_0^t e^{-(A_t-A_s)}\,dW^{(2)}_s.
\]

Conditional on the complete stiffness path up to time \(t\), the position is Gaussian with mean \(m_t=x_0e^{-A_t}\) and variance

\[
 V_t=2D\int_0^t\exp\left[-2k_0(t-s)-2\kappa\int_s^t|B_u|^p\,du\right]ds.
\]

Consequently, at the level of joint distributions with the stiffness path, \(X_t\) can be replaced by \(m_t+\sqrt{V_t}Z\), for a fresh independent standard normal \(Z\). Notice that \(0\le V_t\le2Dt\), and \(|m_t|\le|x_0|\).

**2. Brownian scaling and pathwise endpoint Laplace concentration.** Put \(H=t^{1+p/2}\). By Brownian scaling, the pair \((B_t/(\sigma\sqrt t),t^{p/2}V_t)\) has the same law as

\[
\left(b(1),\;2D H\int_0^1
\exp\left[-2\kappa\sigma^p H\int_u^1|b(v)|^p\,dv
                   -2k_0t(1-u)\right]du\right),
\]

where \(b\) is standard Brownian motion on \([0,1]\). Changing variables \(z=H(1-u)\), the second coordinate becomes

\[
 J_H(b)=2D\int_0^H
\exp\left[-2\kappa\sigma^p\int_0^z|b(1-v/H)|^p\,dv
 -2k_0zt^{-p/2}\right]dz.
\]

We claim that for every continuous \(b\) with \(b(1)\ne0\),

\[
 J_H(b)\longrightarrow \frac{D}{\kappa\sigma^p|b(1)|^p}.
\]

For each fixed \(z\ge0\), continuity at \(1\) makes the inner integral tend to \(|b(1)|^p z\), while the baseline term tends to zero because \(p>0\). To justify taking the limit inside an integral whose upper endpoint grows, choose \(\delta\in(0,1)\) and \(c>0\) such that \(|b(v)|\ge c\) for \(1-\delta\le v\le1\). On \(0\le z\le\delta H\), the integrand is bounded by \(\exp(-2\kappa\sigma^pc^pz)\), an integrable majorant. Dominated convergence applies after extending that part of the integrand by zero beyond \(\delta H\). For \(\delta H<z\le H\), the first \(\delta H\) units of the inner integral contribute at least \(c^p\delta H\), so the tail integral is bounded above by

\[
 H\exp(-2\kappa\sigma^p c^p\delta H)\longrightarrow0.
\]

Thus \(J_H(b)\to2D\int_0^\infty e^{-2\kappa\sigma^p|b(1)|^pz}dz=D/(\kappa\sigma^p|b(1)|^p)\). Brownian motion satisfies \(b(1)\ne0\) almost surely.

**3. The initial condition vanishes in the same coupling.** Under scaling, the conditional mean is distributed as

\[
 \widetilde m_t=x_0\exp\left[-k_0t-\kappa\sigma^pH\int_0^1|b(u)|^pdu\right].
\]

Almost every Brownian path has \(\int_0^1|b(u)|^pdu>0\); consequently \(t^{p/4}\widetilde m_t\to0\). On the same probability space with an independent \(Z\), the pair

\[
 \left(b(1),\;t^{p/4}\widetilde m_t+\sqrt{J_H(b)}Z\right)
\]

converges almost surely to \((G,a_pZ/|G|^{p/2})\). This proves the first weak limit. Multiply the second coordinate by \(\sigma^{p/2}|b(1)|^{p/2}\) and apply the continuous mapping theorem away from \(G=0\) to obtain the self-normalized limit and its independence.

**4. Exact index and the Cauchy specialization.** Let \(Y_p=a_p Z/|G|^{p/2}\). Conditioning on \(Z\),

\[
\mathbb P(|Y_p|>R)
=\mathbb E\left[\mathbb P\left(|G|<(a_p|Z|/R)^{2/p}\,\middle|\,Z\right)\right].
\]

Because \(\mathbb P(|G|<h)=\sqrt{2/\pi}\,h+o(h)\) as \(h\downarrow0\) and \(\mathbb P(|G|<h)\le\sqrt{2/\pi}\,h\) for all \(h\ge0\), dominated convergence, using the finiteness of all positive Gaussian moments, yields the stated \(R^{-2/p}\) coefficient. Independence gives \(\mathbb E|Y_p|^q=a_p^q\mathbb E|Z|^q\mathbb E|G|^{-pq/2}\), finite exactly for \(pq/2<1\). At \(p=2\), the ratio of independent standard normals is standard Cauchy; replacing \(G\) by \(|G|\) does not change its distribution since \(G\)'s sign is independent of its magnitude and \(Z\) is symmetric.

For any \(q\ge2/p\), the limiting law has infinite \(q\)-moment. Since \(t^{p/4}X_t\Rightarrow Y_p\) and \(y\mapsto\min\{M,|y|^q\}\) is bounded continuous for each fixed \(M>0\),

\[
\liminf_{t\to\infty}\mathbb E|t^{p/4}X_t|^q
\ge \mathbb E\min\{M,|Y_p|^q\}.
\]

Letting \(M\to\infty\) yields divergence. Every finite-time \(q\)-moment nevertheless exists because the conditional Gaussian means are bounded by \(|x_0|\) and variances by \(2Dt\). This proves the precise finite-time/long-time distinction.

## Verification

`check.py` is a reproducible standalone supplemental checker requiring Python 3, NumPy and SciPy, executed as `python check.py`. It carried out 109 deterministic comparisons. They include analytic fixed-path integral identities, numerical endpoint Laplace tests on deterministic varying stiffness paths, the Gaussian-ratio Cauchy characteristic function and tail formula, general-power tail coefficients, and a numerical Brownian-path sample check for the scaled conditional variances. The sampled-path relative-error median was 0.0084 across 44 paths in the stated test regime. These finite computations corroborate identities and convergence mechanisms only; the pathwise dominance proof above establishes the limit.

The two relevant structural checks are explicit in the proof: the long initial-time integral is exponentially suppressed when the endpoint stiffness is nonzero; and the initial-position contribution vanishes exponentially in \(t^{1+p/2}\). There is no interchange of an unbounded expectation with a limit in the derivation of the distributional result.

## Relationship to prior work

Gupta and Klapp's 2026 study, *Non-stationary Statistics and Energetics of Brownian Motion under Stochastic Harmonic Confinement* (arXiv:2609.33751v1), motivates the Brownian-squared stiffness model and analyzes nonstationary statistics and energetics. Its model and foundational stochastic-convolution representation are prior material, not claimed here as novel. The contribution assessed here is the rigorous growing-time marginal limit, its self-normalized counterpart, the explicit Cauchy law for quadratic stiffness, and the power-dependent sharp tail index, for independent positive-temperature forcing and any fixed nonnegative baseline stiffness.

The related earlier Gupta–Klapp study, *Non-equilibrium fluctuations in a harmonic trap with annealed stochastic stiffness*, treats stochastic harmonic confinement with an Ornstein–Uhlenbeck stiffness rather than an unbounded Brownian-powered stiffness. General Gaussian variance mixtures, normal-ratio Cauchy laws and Student-type superstatistics are long-established and excluded from the novelty claim. The potentially novel part is proving that this *specific nonstationary stochastic-confinement model* converges to the indicated variance mixture and identifying the exact scale and tail-index transition.

## Limitations

The 2026 motivating arXiv paper's full text could not be obtained for a complete paragraph-by-paragraph comparison in this run; its accessible abstract was inspected. The 2025 related paper's accessible full text was consulted. Thus a hidden result or appendix in the 2026 paper remains a material originality risk; a broad theorem about fast stochastic confinement could also contain the conclusion as a corollary. Search nonmatches are not evidence of mathematical uniqueness. There is no claim of independent audit or external validation.

Independence of the two driving Brownian motions is essential to conditional Gaussianity. The theorem covers the specified Brownian-powered stiffness with fixed coefficients and deterministic initial position, not stationary, correlated or fractional environmental noise. The proved sharp moment threshold pertains to the weak limiting distribution and divergence of renormalized moments at and above threshold. Convergence of moments below the threshold and rates of convergence are not asserted. The Cauchy limit does not mean finite-time moments cease to exist.

## References

1. Gupta and Klapp, *Non-stationary Statistics and Energetics of Brownian Motion under Stochastic Harmonic Confinement*, arXiv:2609.33751v1 (first public date: 2026-09-27), https://arxiv.org/abs/2609.33751. Accessible abstract inspected; primary full text not available during this comparison.
2. Gupta and Klapp, *Non-equilibrium fluctuations in a harmonic trap with annealed stochastic stiffness*, Journal of Statistical Mechanics (2025), DOI:10.1088/1742-5468/ae09a5. Accessible full-text mathematical and model discussion inspected.
3. Standard facts used: Brownian scaling, linear stochastic variation of constants, dominated convergence, the normal-ratio Cauchy distribution, and Gaussian moments. These are classical tools, not new claims.
