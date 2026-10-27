# Universal multivariate extreme tails in a first-passage-reset Brownian gas

## Finding
For every integer \(N\ge3\), the stationary joint lower tail of a Brownian gas reset simultaneously when any particle reaches a fixed positive barrier obeys an exact multivariate power law. Define
\[
J_N=\int_0^\infty\operatorname{erf}\!\left(\frac1{2\sqrt s}\right)^N\,ds,
\qquad
C_N=\frac{4^{N/2-1}\Gamma(N/2-1)}{\pi^{N/2}J_N}.
\]
For every integer \(1\le k\le N\), distinct labels \(i_1,\ldots,i_k\), and fixed positive multipliers \(a_1,\ldots,a_k\), the stationary positions satisfy
\[
\boxed{\lim_{R\to\infty}\left(\frac RL\right)^{N-2}\Pr(X_{i_j}<-a_j R\ \text{for all }1\le j\le k)
=C_N\left(\sum_{j=1}^k a_j^2\right)^{1-N/2}.}
\]
In particular, the conditional probability of a joint extreme among any \(k\) specified particles, given that the first is extreme, has the positive universal limit
\[
\boxed{\lim_{R\to\infty}\Pr(X_{i_2}<-R,\ldots,X_{i_k}<-R\mid X_{i_1}<-R)=k^{1-N/2}.}
\]
For each \(q>0\), the stationary absolute moment is finite **if and only if** \(q<N-2\). At the boundary, with \(Y=(-X_i)_+\),
\[
\mathbb E[(Y\wedge R)^{N-2}]\sim(N-2)C_N L^{N-2}\log R.
\]
The physical diffusion coefficient cancels from these stationary laws. This claim concerns fixed \(N\) and large negative displacements; the limits do not interchange with an unrestricted \(N\to\infty\) limit.

## Assumptions and scope
Take \(L,D>0\) and an integer \(N\ge3\). Between resets, \(N\) labeled, independent one-dimensional Brownian motions have generator \(D\partial_{xx}\), all begin at \(0\), and the first hitting of \(+L\) by **any** walker instantaneously resets **every** position to \(0\). All cycles use fresh independent Brownian increments. Let \((X_1,\ldots,X_N)\) have the unique stationary law of this regenerative system. The stated joint limits hold for every fixed set of distinct indices and every fixed \(a_j>0\), with no requirement that multipliers be equal.

## Proof
**1. Established renewal representation.** Put
\[
S(t)=\operatorname{erf}\!\left(\frac{L}{\sqrt{4Dt}}\right),\quad
G(x,t)=\frac{e^{-x^2/(4Dt)}-e^{-(x-2L)^2/(4Dt)}}{\sqrt{4\pi Dt}}\ \ (x<L).
\]
The reset-free survival probability for all \(N\) walkers is \(S(t)^N\). The mean regenerative cycle length is
\[
M_N=\int_0^\infty S(t)^N\,dt=\frac{L^2}{D}J_N\in(0,\infty),
\]
where finiteness follows from \(S(t)\sim L/(\sqrt{\pi Dt})\) at large \(t\), since \(N>2\). The exact stationary density previously derived by Biroli, Majumdar and Schehr is \(M_N^{-1}\int_0^\infty\prod_iG(x_i,t)\,dt\). Thus the present proof begins from, and does not claim, that published stationary formula.

**2. An exact multi-exceedance integral.** For \(b>0\), integrate the absorbed heat kernel to obtain
\[
H_b(t):=\int_{-\infty}^{-b}G(x,t)\,dx
=\int_b^{b+2L}\frac{e^{-z^2/(4Dt)}}{\sqrt{4\pi Dt}}\,dz.
\]
Integrating out the \(N-k\) unobserved positions in the stationary density gives the exact identity
\[
\Pr(X_{i_j}<-a_jR,\ 1\le j\le k)
=\frac1{M_N}\int_0^\infty S(t)^{N-k}\prod_{j=1}^kH_{a_jR}(t)\,dt.
\]
No factorization of the **unconditional** stationary positions is assumed.

**3. Sharp scaling and justified limit.** Substitute \(t=R^2u/D\) with \(u>0\). For each fixed \(u\), the mean value theorem and the small-argument error-function limit yield
\[
\lim_{R\to\infty}\frac RL H_{aR}(R^2u/D)
=\frac{e^{-a^2/(4u)}}{\sqrt{\pi u}},
\qquad
\lim_{R\to\infty}\frac RL S(R^2u/D)=\frac1{\sqrt{\pi u}}.
\]
For **all** \(R,u>0\), positivity and monotonicity of the Gaussian kernel give
\[
0\le\frac RL H_{aR}(R^2u/D)
\le\frac{e^{-a^2/(4u)}}{\sqrt{\pi u}},
\qquad
0\le\frac RL S(R^2u/D)\le\frac1{\sqrt{\pi u}}.
\]
Hence the scaled integrand is dominated by
\(\pi^{-N/2}u^{-N/2}\exp[-(\sum_j a_j^2)/(4u)]\), integrable on \((0,\infty)\) precisely for \(N>2\) (the positive multipliers control the origin). Dominated convergence therefore gives the proposed limit with coefficient
\[
\frac{1}{\pi^{N/2}J_N}\int_0^\infty u^{-N/2}
\exp\!\left[-\frac{\sum_j a_j^2}{4u}\right]du.
\]
The elementary substitution \(v=(\sum_j a_j^2)/(4u)\) evaluates this as
\[\frac{4^{N/2-1}\Gamma(N/2-1)}{\pi^{N/2}J_N}
\left(\sum_j a_j^2\right)^{1-N/2}.\]
This also proves the stated equal-threshold conditional limit by dividing the \(k\)-particle asymptotic by the \(k=1\) asymptotic.

**4. Exact moment boundary.** For one particle, the preceding theorem gives
\(\Pr(X_i<-R)\sim C_N(L/R)^{N-2}\). The positive part is bounded by \(L\). For any \(q>0\), the layer-cake identity
\[
\mathbb E[Y^q]=q\int_0^\infty r^{q-1}\Pr(Y>r)\,dr
\]
therefore converges if and only if \(q<N-2\). Applying the truncated version of the same identity for \(q=N-2\) gives the asserted sharp logarithmic coefficient. Every part of this conclusion follows analytically, not from finite enumeration or numerical extrapolation.

## Verification
The standalone standard-library script `verify_first_passage_tail.py` evaluates the *exact finite-threshold renewal integrals* after nondimensionalization, compares them against the independently evaluated gamma-limit coefficients, and tests unequal thresholds, the equal-threshold conditional ratios, and gamma-function consistency. It completed **52 deterministic numerical/algebra checks**, using \(N=3,4,5,7\) and finite ratios \(R/L=60,250\). For example \(J_3\approx0.757602154835\), \(C_3\approx0.840308819484\), and the two-particle limiting conditional probability is \(1/\sqrt2\). These finite checks corroborate but do not replace the dominated-convergence proof.

## Relationship to prior work
Biroli, Majumdar and Schehr (arXiv:2512.00440v1, equations (1), (2), (10), (11)–(13)) established the regenerative stationary density and its conditional-independence representation, plus large-particle-number density and order-statistics results. This finding applies an additional fixed-\(N\), far-negative-tail analysis to that exact density and obtains a multivariate tail dependence law and moment classification not stated there. De Mauro, Biroli, Majumdar and Schehr (arXiv:2509.06658, section IV.B) established power-law density tails for **externally imposed** Pareto-reset intervals and free Gaussian excursions. That model has neither event-triggered resets nor the survival-conditioned absorbed propagator used here; its one-point power-law mechanism is closely related, but does not give the stated multivariate fixed-\(N\) coefficient without additional analysis. Biswas, Majumdar and Pal (arXiv:2504.13501) study threshold-reset search times rather than these stationary joint extreme tails.

## Limitations
The asymptotics hold at fixed \(N\) and fixed positive relative threshold multipliers. They do not provide a uniform simultaneous limit in \(N,R\), the long-time approach to stationarity, or distributions for non-Brownian dynamics and nonidentical thresholds or diffusion constants. The general formula for the stationary joint density is prior work; no claim of independent validation or exhaustive literature priority is made.

## References
Biroli, M., Majumdar, S. N., and Schehr, G., *First Passage Resetting Gas*, arXiv:2512.00440v1 (first publicly dated November 29, 2025), https://arxiv.org/html/2512.00440v1.

De Mauro, G., Biroli, M., Majumdar, S. N., and Schehr, G., *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658, https://arxiv.org/pdf/2509.06658.

Biswas, A., Majumdar, S. N., and Pal, A., *Target Search Optimization by Threshold Resetting*, arXiv:2504.13501, https://arxiv.org/abs/2504.13501.
