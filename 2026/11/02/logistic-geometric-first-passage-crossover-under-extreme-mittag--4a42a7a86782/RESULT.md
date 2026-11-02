# Logistic-geometric first-passage crossover under extreme Mittag-Leffler jump-rate fluctuations

## Finding
Consider a continuous-time simple symmetric nearest-neighbor random walk on the positive integers, absorbed at zero. Its total jump rate is independent of the jump directions and is redrawn independently every deterministic time interval. At each redraw the positive rate has Laplace transform \(\mathbb E e^{-s\lambda}=1/(1+s^\alpha)\), with \(0<\alpha<1\). This is the heavy-tailed, first-type Mittag-Leffler rate distribution.

Let the initial distance \(x_\alpha\) be any positive integer, let the redraw interval \(\tau_\alpha>0\), and let \(T_\alpha\) be the first hitting time of zero. Suppose that, as \(\alpha\downarrow0\),
\[
\alpha\log\left(\frac{x_\alpha^2}{\tau_\alpha}\right)\longrightarrow\kappa\in\mathbb R.
\]
Then the full first-passage law, normalized by the redraw period, converges:
\[
\boxed{\frac{T_\alpha}{\tau_\alpha}\ \Longrightarrow\ G_\kappa,\qquad
\Pr(G_\kappa=j)=p_\kappa(1-p_\kappa)^j,\quad j=0,1,2,\ldots,\quad
p_\kappa=\frac{1}{1+e^\kappa}.}
\]
Equivalently, for every integer \(m\ge0\) and \(0<u<1\),
\[
\Pr\left(T_\alpha>(m+u)\tau_\alpha\right)
\longrightarrow (1-p_\kappa)^{m+1},
\]
and for \(s\ge0\),
\[
\mathbb E\exp\left(-sT_\alpha/\tau_\alpha\right)
\longrightarrow\frac{p_\kappa}{1-(1-p_\kappa)e^{-s}}.
\]
For a fixed redraw interval and \(x_\alpha=\lfloor e^{c/\alpha}\rfloor\) with \(c>0\), the crossover parameter is \(\kappa=2c\). Thus the first-passage law changes continuously from a fair-coin geometric limit at fixed distance to an exponentially larger typical number of refresh intervals on the critical exponential distance scale. Allowing the refresh interval to vary yields the more general ratio formulation above.

## Assumptions and scope
The state space is \(\{0,1,2,\ldots\}\). At rate \(\lambda_{\alpha,j}\) during the interval \([j\tau_\alpha,(j+1)\tau_\alpha)\), a particle at a positive state attempts an independent jump by \(+1\) or \(-1\), each with probability \(1/2\); state zero is absorbing. The redraws \(\lambda_{\alpha,j}\) are independent and identically distributed for each fixed \(\alpha\), and independent of the jump and Poisson-clock randomness. Their Laplace transform is precisely \((1+s^\alpha)^{-1}\). Time starts at a redraw boundary. No stationarity in the rate environment is needed, and the initial distance is deterministic.

The claim ranges over **all sequences** \(\alpha\downarrow0\), positive integers \(x_\alpha\), and positive real durations \(\tau_\alpha\) for which the displayed finite real limit \(\kappa\) exists. It does not assume either duration or distance remains fixed. The limit law is supported on nonnegative integers; it counts the number of redraw intervals preceding the first sufficiently fast rate interval, with the residual first-passage duration inside that final interval vanishing after period normalization.

## Proof
**1. Logarithmic rate scale.** Put \(W_\alpha=\alpha\log\lambda_\alpha\). The first-type Mittag-Leffler survival function has the integral representation (Levit and Reuveni, supplementary Eq. S50)
\[
\Pr(\lambda_\alpha>x)=
\frac{\sin(\pi\alpha)}{\pi\alpha}x^\alpha
\int_0^\infty\frac{\exp(-r^{1/\alpha})}{r^2+2rx^\alpha\cos(\pi\alpha)+x^{2\alpha}}\,dr.
\]
Set \(x=\exp(z/\alpha)\) for fixed real \(z\). The exponential factor in the integrand tends to the indicator of \(0<r<1\), the cosine tends to one, and the prefactor tends to \(e^z\). For all sufficiently small \(\alpha\), the integrand is dominated by a constant multiple of \((r^2+e^{2z})^{-1}\), an integrable function. Dominated convergence therefore gives
\[
\Pr(W_\alpha>z)\longrightarrow
\int_0^1\frac{e^z}{(r+e^z)^2}\,dr
=\frac{1}{1+e^z}.
\]
Thus \(W_\alpha\Rightarrow W\), where \(W\) has standard logistic distribution \(\Pr(W\le z)=1/(1+e^{-z})\). Independent draws give joint convergence for every fixed number of refresh intervals.

**2. Uniform bounds for an ordinary killed walk.** Let \(H_x\) be the zero-hitting time of a continuous-time unit-rate simple symmetric walk started at integer \(x\ge1\). For \(t>0\), reflection and the unit-rate free-walk heat-kernel bound imply
\[
\Pr(H_x>t)\le\min\left\{1,\frac{C x}{\sqrt t}\right\}
\]
for an absolute constant \(C\). For clarity, if \(p_t(k)\) denotes the free-walk transition probability from zero to \(k\), the reflection identity gives
\[
\Pr(H_x>t)=\sum_{k=1-x}^{x}p_t(k),\qquad
\sup_{k\in\mathbb Z}p_t(k)\le\frac{C}{\sqrt t}.
\]
The latter follows, for example, by Fourier inversion of \(\exp[-t(1-\cos\theta)]\). For a unit-rate free walk observed up to cumulative clock time \(v\), the centered position is a square-integrable martingale with variance \(v\), so Doob's maximal inequality yields
\[
\Pr\left(\sup_{0\le t\le v}|Z_t|\ge b\right)\le\frac{4v}{b^2}.
\]
Both bounds remain valid conditionally on any deterministic, finite piecewise-constant rate profile after changing to the cumulative jump-rate clock.

**3. Slow and fast blocks.** Write \(\kappa_\alpha=\alpha\log(x_\alpha^2/\tau_\alpha)\). Fix a tolerance \(\eta>0\) and a separation \(\delta>0\). Call the \(j\)-th redraw **slow** when \(W_{\alpha,j}\le\kappa-\delta\), and **fast** when \(W_{\alpha,j}\ge\kappa+\delta\). For sufficiently small \(\alpha\), uniformly on these events,
\[
\frac{\lambda_{\alpha,j}\tau_\alpha}{x_\alpha^2}
\le e^{-\delta/(2\alpha)}\quad\text{(slow)},\qquad
\frac{\lambda_{\alpha,j}\tau_\alpha}{x_\alpha^2}
\ge e^{\delta/(2\alpha)}\quad\text{(fast)}.
\]
For any fixed number \(N\) of initially slow blocks, their cumulative operational time is at most \(N x_\alpha^2 e^{-\delta/(2\alpha)}\). The martingale maximal inequality implies that with probability tending to one the spatial displacement throughout these blocks is smaller than \(x_\alpha/2\); in particular the particle has not hit zero and its position remains at most \(3x_\alpha/2\).

If the next block is fast, then its rate clock accumulated by physical time \(\eta\tau_\alpha\) is at least \(\eta x_\alpha^2e^{\delta/(2\alpha)}\). The preceding survival bound, conditional on the position at the redraw, gives probability at most \(C_\eta e^{-\delta/(4\alpha)}\) of not hitting zero by \(\eta\tau_\alpha\) after this redraw. Hence for any fixed number of observed redraws, slow blocks preserve the starting distance on its own scale, while the first fast block produces absorption in a negligible fraction of one period.

**4. Remove the transition band.** The event that any of the first \(N\) sampled logarithmic rates lies in \((\kappa-\delta,\kappa+\delta)\) has limiting probability bounded by \(N\Pr(|W-\kappa|\le\delta)\). The latter tends to zero with \(\delta\downarrow0\), since the logistic law is continuous. Therefore, for every fixed \(m\ge0\) and \(0<u<1\), survival beyond \((m+u)\tau_\alpha\) becomes equivalent in probability to having no fast rate in the first \(m+1\) independent blocks. Its limiting probability is
\[
\Pr(W<\kappa)^{m+1}
=\left(\frac{e^\kappa}{1+e^\kappa}\right)^{m+1}.
\]
These convergence statements at all noninteger continuity points establish weak convergence to the claimed geometric law. Convergence of bounded Laplace transforms follows from weak convergence. \(\square\)

## Verification
The accompanying `CHECK.py` is standalone Python 3 code using only the standard library. It numerically evaluates the first-type Mittag-Leffler log-rate survival integral and the **exact** half-line spectral survival formula at integer redraw times:
\[
\Pr(T_\alpha>m\tau_\alpha)
=\int_0^1\sin(\pi u x_\alpha)
\cot(\pi u/2)\left[1+\big(\tau_\alpha(1-\cos(\pi u))\big)^\alpha\right]^{-m}\,du.
\]
This is the spectral formula from Levit and Reuveni applied at the redraw boundaries. The checker tests the normalization, monotonicity, logarithmic-rate limit, and convergence toward the geometric survival probabilities on both sides of the crossover. The output file records 40 passing assertions. Numerical quadrature verifies finite examples, **not** the infinite-parametric theorem; the analytic proof above is the evidence for the limiting claim.

## Relationship to prior work
Levit and Reuveni (2026) introduced the half-line Mittag-Leffler-rate first-passage analysis, obtained its spectral survival representation, proved the mean first-passage threshold at \(\alpha=1/2\), and identified the fixed-distance mean limit \(\mathbb E T_\alpha\to\tau\) as \(\alpha\downarrow0\). Their supplementary analysis establishes the limiting half-mass at zero and infinity for **fixed** rate thresholds. It does not give a distributional first-passage theorem on the exponentially changing joint distance/refresh-time scale. The present result establishes that singular two-parameter limit and its full logistic-geometric law; it does not claim the previously established spectral representation or fixed-distance mean as new results.

Arutkin and Reuveni (2023 preprint; 2024 publication) introduced the doubly stochastic random-walk framework and solved interval first-exit problems for exponentially distributed rates. Their formulas do not include the present Mittag-Leffler small-parameter log-distance scaling. Haubold, Mathai and Saxena (2011) give the classical structural and Mellin representations for Mittag-Leffler variables; the rate-law identity is prior mathematics, not claimed as new.

## Limitations
The theorem concerns weak convergence only. It neither asserts convergence of first-passage expectations or higher moments nor a uniform approximation over diverging numbers of redraw intervals or unbounded crossover parameters. In particular, the limiting geometric mean \((1-p_\kappa)/p_\kappa=e^\kappa\) is **not** by itself a proof that \(\mathbb E T_\alpha/\tau_\alpha\to e^\kappa\). Other rate distributions require a separate logarithmic-rate limit, and other spatial walks require analogous uniform slow-displacement and fast-absorption bounds. There has been no independent mathematical audit or external reproduction.

## References
1. B. Levit and S. Reuveni, *First Passage in the Presence of Jump Rate Fluctuations: A Transition from Infinite to Finite Mean*, arXiv:2609.26925v1, publicly posted September 22, 2026. https://arxiv.org/abs/2609.26925 (main text and supplementary sections S3.2–S3.3).
2. M. Arutkin and S. Reuveni, *Doubly stochastic continuous time random walk*, arXiv:2302.07041v1, publicly posted February 14, 2023; *Physical Review Research* 6, L012033 (2024). https://arxiv.org/abs/2302.07041 .
3. H. J. Haubold, A. M. Mathai and R. K. Saxena, *Mittag-Leffler Functions and Their Applications*, *Journal of Applied Mathematics* (2011), Article 298628. https://doi.org/10.1155/2011/298628 .
