# Two sharp occupation thresholds for position-dependent refractory partial resetting

## Finding

A diffusively exploring particle that contracts its position on a Poisson reset and then rests for a time whose *conditional mean* grows exponentially in the reset displacement has **two distinct sharp thresholds**. Let \(c=\sqrt{r/D}\), let \(0<a<1\) be the contraction factor, and let the expected resting time after resetting to \(y\) be \(\tau_0 e^{\lambda |y|}\), where \(\lambda\ge0\). Define
\[
\lambda_{\mathrm{tail}}=c(a^{-1}-1),\qquad
\lambda_{\mathrm{stat}}=c/a,
\]
so that \(0<\lambda_{\mathrm{tail}}<\lambda_{\mathrm{stat}}\).

There is a normalizable time-stationary phase-position law **if and only if** \(0\le\lambda<\lambda_{\mathrm{stat}}\). Inside this entire domain, the posterior probability that a distant observed particle is resting satisfies
\[
\lim_{|x|\to\infty}\Pr(R\mid X=x)=
\begin{cases}
0,&0\le\lambda<\lambda_{\mathrm{tail}},\\
\dfrac{r\tau_0}{a+r\tau_0},&\lambda=\lambda_{\mathrm{tail}},\\
1,&\lambda_{\mathrm{tail}}<\lambda<\lambda_{\mathrm{stat}}.
\end{cases}
\]
At the higher stationarity threshold, the active fraction vanishes linearly, with an exact coefficient.

## Assumptions and scope

In one spatial dimension, exploration is drift-free Brownian motion with generator \(D\partial_x^2\), \(D>0\). Independent active epochs end at exponential rate \(r>0\). At each event the position changes instantaneously from \(x\) to \(ax\), for fixed \(a\in(0,1)\), followed by an immobile refractory epoch of almost surely finite positive duration. Conditional on the reset position \(y\), this epoch has mean \(\tau_0e^{\lambda|y|}\), with \(\tau_0>0\) and \(\lambda\ge0\). Given the reset positions, the refractory durations are independently sampled and are independent of future exploration increments and clocks; their full conditional distributions need not be exponential or deterministic. The augmented process records the phase and residual refractory duration.

Set \(q=a^2\), \(P_a=\prod_{m=1}^{\infty}(1-a^{2m})>0\), and \(\eta=r\tau_0\). Let \(Z_0,Z_1,\ldots\) be independent centered two-sided exponential (Laplace) variables with density \(z\mapsto(c/2)e^{-c|z|}\), where \(c=\sqrt{r/D}\). Define the convergent perpetuity
\[
S_a=\sum_{j=0}^{\infty}a^jZ_j,\qquad f_a=\text{density of }S_a,\qquad g_a(x)=a^{-1}f_a(x/a),
\]
and \(M_a(\lambda)=\int_{\mathbb R}e^{\lambda|x|}g_a(x)\,dx\).

## Proof

**1. Embedded Markov chain and phase occupation.** An exploration increment stopped at independent exponential time has Fourier transform \(r/(r+Dk^2)=c^2/(c^2+k^2)\), hence law \(Z_0\). The reset-position recursion is \(Y_{n+1}=a(Y_n+Z_n)\), a strict affine contraction with a unique ergodic stationary law \(aS_a\). By the memorylessness of the active clock, the per-unit-active-time position density is \(f_a\), while the post-reset resting-position density at reset epochs is \(g_a\). Integrating the time spent at each position within a cycle (Markov-renewal reward) gives the unnormalized phase-position occupation measures
\[
\mu_E(dx)=r^{-1}f_a(x)\,dx,\qquad
\mu_R(dx)=\tau_0e^{\lambda|x|}g_a(x)\,dx.
\]
Thus, when \(M_a(\lambda)<\infty\), the *normalized* stationary joint densities are
\[
p_E(x)=\frac{f_a(x)}{1+\eta M_a(\lambda)},\qquad
p_R(x)=\frac{\eta e^{\lambda|x|}g_a(x)}{1+\eta M_a(\lambda)}.
\tag{1}
\]
These densities integrate to one in total. Conversely, the embedded chain is Harris recurrent and has only this invariant law, and the finite-duration suspension has no invariant probability unless its invariant mean cycle length \(r^{-1}+\tau_0M_a(\lambda)\) is finite: a stationary process must carry strictly positive reset intensity, whose Palm cycle occupation is proportional to the measures above. Hence finite \(M_a\) is also necessary. This argument concerns the process with the residual holding time included, not just an arbitrary formal spatial density.

**2. Exact spatial tails and the stationarity boundary.** Write \(S_a=Z_0+W\), with \(W=\sum_{j\ge1}a^jZ_j\). The moment-generating product yields
\[
\mathbb E[e^{cW}]=\prod_{j=1}^{\infty}(1-a^{2j})^{-1}=P_a^{-1}.
\]
Since \(W\) has some exponential moment strictly beyond rate \(c\), convolution with the two-sided exponential kernel, splitting at \(W=x\) and applying dominated convergence, proves
\[
f_a(x)\sim\frac{c}{2P_a}e^{-c|x|},\qquad
g_a(x)\sim\frac{c}{2aP_a}e^{-(c/a)|x|}\quad(|x|\to\infty).
\tag{2}
\]
Both tails have strictly positive leading coefficients. It follows immediately that \(M_a(\lambda)<\infty\) exactly when \(\lambda<c/a\), including divergence at equality; this proves the stationarity criterion.

**3. Rare-position phase inversion.** Dividing the two densities in (1) removes the common normalization and gives the exact conditional odds
\[
\frac{\Pr(R\mid X=x)}{\Pr(E\mid X=x)}
=\eta e^{\lambda|x|}\frac{f_a(x/a)}{a f_a(x)}
\sim\frac{\eta}{a}e^{(\lambda-\lambda_{\mathrm{tail}})|x|}.
\tag{3}
\]
The three limiting posterior values follow. In particular at the critical exponent the resting fraction approaches \(\eta/(a+\eta)\), and is not generally one half. The stationary spatial density \(p_E+p_R\) has the strictly positive leading exponential decay rate \(\min\{c,c/a-\lambda\}\), with both contributions present on the equality line.

**4. Sharp collapse of active occupancy.** Equation (2) gives the one-sided Laplace-transform pole and therefore
\[
M_a(\lambda)\sim\frac{c}{aP_a}\frac1{c/a-\lambda},
\qquad
\Pr(E)=\frac1{1+\eta M_a(\lambda)}
\sim\frac{aP_a}{\eta c}(c/a-\lambda)
\quad(\lambda\uparrow c/a).
\tag{4}
\]
The pole follows by splitting the defining integral at a fixed large distance and applying the positive-tail equivalents with uniform relative-error bounds; both spatial half-lines contribute. This proves the coefficient without an unverified interchange of infinite series.

## Verification

The accompanying standalone program `verify_extreme_phase.py` evaluates the exact partial-fraction series
\[
f_a(x)=\frac{c}{2P_a}\sum_{j=0}^{\infty}
\frac{(-1)^j a^{j^2}}{\prod_{m=1}^{j}(1-a^{2m})}
\exp(-c|x|/a^j),
\]
whose coefficients follow by residues from \(\prod_{j\ge0}(1+a^{2j}k^2/c^2)^{-1}\). It cross-checks the refractory normalizer independently by numerical quadrature, tests the three posterior regimes, and measures the pole and active-fraction slopes approaching the upper threshold. It finishes with `ALL_CHECKS_PASS`. The infinite-dimensional and stationarity claims are analytical; finite numerical checks are supporting evidence only.

## Relationship to prior work

Olsen and Löwen (2024), arXiv:2406.10039, derive the mixture of exploring and resting particles for partial resetting with an independently drawn refractory period; its mean is independent of reset position (notably their equations (30)–(33)). The perpetuity for free proportional resetting is established in the earlier literature (e.g., arXiv:2205.03363 and arXiv:2204.07215). We use those objects but change the physical recovery law: the mean refractory time is exponentially weighted by the attained reset distance, making occupation-time bias nonconstant. This produces a new normalizability obstruction and the distinct rare-position phase-inversion boundary. Conventional resetting with finite return or refractory duration (arXiv:1809.01551) does not establish these partial-reset conditional phase thresholds.

## Limitations

The theorem concerns one-dimensional drift-free Brownian exploration, exact proportional contraction, independent exponential exploration clocks, and a specified exponential conditional *mean* of refractory durations. It does not prove analogous thresholds for nonlinear contractions, drift, or regularly varying state-dependent holding times. At and above \(\lambda_{\mathrm{stat}}\) no normalizable physical-time invariant probability is claimed; infinite invariant occupation measures may still be defined. The stationary phase-conditional tail law presumes the unique normalizable equilibrium below that boundary. It is not a theorem about arbitrary transient initial distributions or finite-time large deviations. An equivalent treatment in not-yet-inspected literature remains possible.

## References

- K. Stølevik Olsen and H. Löwen, “Partial stochastic resetting with refractory periods,” arXiv:2406.10039 (first public 2024-06-14), https://arxiv.org/abs/2406.10039.
- Tal-Friedman, Roichman and Reuveni, proportional partial resetting study, arXiv:2205.03363, https://arxiv.org/abs/2205.03363.
- J. K. Pierce, partial-resetting steady-state analysis, arXiv:2204.07215, https://arxiv.org/abs/2204.07215.
- M. R. Evans and S. N. Majumdar, stochastic resetting with finite return/refractory times, arXiv:1809.01551, https://arxiv.org/abs/1809.01551.
