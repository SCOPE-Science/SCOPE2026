# A dilogarithmic stationary large-deviation law and a strict diffusion-approximation tail gap

## Finding

For one-dimensional Brownian diffusion interrupted by very frequent weak proportional resets, the exact stationary law and its customary effective-diffusion surrogate agree at ordinary spatial scales, but have **different large-deviation rate functions** at the natural rare-displacement scale. The discrepancy is global, strictly positive away from the origin, and first appears at sixth order near that origin.

Fix \(D>0\), \(\lambda>0\), and \(0<s<1\). Let \(X_s\) be stationary for the Brownian jump process with generator
\[
\mathcal L_s f(x)=D f''(x)+\frac{\lambda}{s}\left[f((1-s)x)-f(x)\right].
\]
Define \(W_s=\sqrt{\lambda s/D}\,X_s\). Then \(\{W_s\}_{s\downarrow0}\) satisfies a full large-deviation principle on \(\mathbb R\) with speed \(1/s\) and good even rate
\[
I(w)=\sup_{|\theta|<1}\left\{\theta w-\tfrac12\operatorname{Li}_2(\theta^2)\right\},
\qquad \operatorname{Li}_2(z)=\sum_{k\ge1}\frac{z^k}{k^2}.
\]
Here a full large-deviation principle means that for every closed \(F\subset\mathbb R\) and every open \(G\subset\mathbb R\),
\[
\limsup_{s\downarrow0}s\log\mathbb P(W_s\in F)\le-\inf_F I,
\qquad
\liminf_{s\downarrow0}s\log\mathbb P(W_s\in G)\ge-\inf_G I.
\]
For \(w>0\), the unique maximizer \(\theta(w)\in(0,1)\) obeys
\[
w=\frac{-\log(1-\theta(w)^2)}{\theta(w)},
\qquad I(w)=w\theta(w)-\tfrac12\operatorname{Li}_2(\theta(w)^2).
\]
Its even extension specifies negative \(w\); \(I(0)=0\).

The Gaussian-noise diffusion approximation in [1], specialized to the same Brownian resetting model, is
\[
d\widehat X_s=-\lambda\widehat X_s\,dt+
\sqrt{2D+\lambda s\widehat X_s^2}\,dB_t.
\]
Its rescaled stationary variable \(\widehat W_s=\sqrt{\lambda s/D}\,\widehat X_s\) has a full large-deviation principle with the same speed and rate
\[
J(w)=\log(1+w^2/2).
\]
**The principal comparison is strict:**
\[
I(w)>J(w)\quad\text{for all }w\ne0.
\]
More precisely, near zero,
\[
I(w)=\frac{w^2}{2}-\frac{w^4}{8}+\frac{5w^6}{72}+O(w^8),
\quad J(w)=\frac{w^2}{2}-\frac{w^4}{8}+\frac{w^6}{24}+O(w^8),
\]
so \(I(w)-J(w)=w^6/36+O(w^8)\). At large displacement,
\[
I(w)=|w|-\frac{\pi^2}{12}+o(1),
\qquad J(w)=2\log|w|-\log2+o(1).
\]
In particular, two models with the same limiting Gaussian stationary distribution and identical first two local rate-function corrections assign exponentially different probabilities at every fixed nonzero rare-position scale.

## Assumptions and scope

Brownian motion is on the full real line, with generator \(D\partial_{xx}\). Independent rate-\(\lambda/s\) Poisson epochs instantaneously replace the current position by \((1-s)\) times that position. The reset factor is deterministic and the Brownian noise is independent of the resets. All limits hold with \(D,\lambda\) fixed and \(s\downarrow0\). The effective diffusion uses the Itô interpretation and **retains** its multiplicative Gaussian noise; it is not the simpler additive Ornstein–Uhlenbeck limit. Statements are only about *stationary one-time positions*; no path-space, first-passage or finite-\(s\) relative-error theorem is claimed.

## Proof

**1. Stationarity and the existing exact transform.** Let \(q=1-s\) and let \(N_t\) count reset epochs in a time interval of length \(t\), so \(N_t\) is Poisson with rate \(\lambda t/s\). The unique stationary law is the convergent stochastic convolution of Brownian noise damped by intervening reset multipliers. Conditional on reset epochs its variance is
\[
V=2D\int_0^\infty q^{2N_t}\,dt.
\]
The successive independent interarrival times are exponential with mean \(s/\lambda\). Consequently \(V\) has the distribution of \(2D\sum_{j\ge0}q^{2j}E_j\), with \(E_j\) independent \(\mathrm{Exp}(\lambda/s)\). The sum is almost surely finite since its expectation is finite; uniqueness follows by coupling two initial states using common reset epochs, whose difference contracts as \(q^{N_t}\). Integrating the conditional Gaussian moment-generating function gives the exact product already supplied in [2]:
\[
\mathbb E e^{tX_s}=\prod_{j\ge0}\left(1-\frac{Ds}{\lambda}\,t^2q^{2j}\right)^{-1},
\qquad |t|<\sqrt{\lambda/(Ds)}.
\]
This step is background, not the asserted novelty.

**2. Scaled cumulants and steepness.** At \(t=\theta\sqrt{\lambda/(Ds)}\), the scaled log-moment-generating function is
\[
\Lambda_s(\theta):=s\log\mathbb E e^{\theta W_s/s}
=-s\sum_{j\ge0}\log(1-\theta^2q^{2j}),\qquad |\theta|<1.
\]
Write \(h_s=-\log q\), so \(s/h_s\to1\). The Riemann sum \(h_s\sum_{j\ge0}-\log(1-\theta^2e^{-2jh_s})\) converges to
\[
\int_0^\infty-\log(1-\theta^2e^{-2u})\,du
=\frac12\sum_{k\ge1}\frac{\theta^{2k}}{k^2}
=\Lambda(\theta).
\]
The same argument after differentiation, uniformly on compact subsets of \((-1,1)\), proves convergence of the first two derivatives. In particular,
\[
\Lambda'(\theta)=\frac{-\log(1-\theta^2)}{\theta}
\]
(with its continuous value zero at \(\theta=0\)) is strictly increasing and ranges over all \(\mathbb R\). Strict increase follows from the positive Taylor series \(\Lambda(\theta)=\tfrac12\theta^2+\tfrac18\theta^4+\cdots\); its derivative diverges at each endpoint.

**3. Full large-deviation principle.** Finite exponential moments at each \(|\theta|<1\), together with the convergence just proved, give exponential tightness by two-sided Chernoff inequalities. The exponential upper bound on compact closed sets follows from finite coverings by affine exponential bounds and minimax separation; exponential tightness extends it to all closed sets. For every finite \(w\), choose its unique \(\theta\) satisfying \(\Lambda'(\theta)=w\), and tilt the law by \(\exp(\theta W_s/s-\Lambda_s(\theta)/s)\). Under this tilted law, \(\mathbb E W_s=\Lambda'_s(\theta)\to w\) and \(\operatorname{Var}(W_s)=s\Lambda''_s(\theta)\to0\). Undoing the tilt on an arbitrarily small neighborhood proves the local lower bound \(-I(w)\); taking the supremum over points in an open set gives the asserted open-set bound. Thus the full LDP is established without assuming that convergence of a finite histogram proves the limit. The rate is good because \(\theta w-\Lambda(\theta)\to\infty\) as \(|w|\to\infty\) for any fixed \(0<|\theta|<1\) of matching sign.

**4. Diffusion comparator.** The stationary zero-flux Fokker–Planck equation for the effective Itô diffusion has density
\[
\widehat p_s(x)=C_s(2D+\lambda sx^2)^{-1-1/s}
\]
as in [1], specialized to zero baseline drift. The density of \(\widehat W_s\) is proportional to \((1+w^2/2)^{-1-1/s}\). Its normalizing factor has logarithm \(o(1/s)\), for example by Laplace's method around its unique mode at zero. Applying upper and lower Laplace bounds, with exponential tightness from polynomial-density tails raised to power \(1/s\), gives the full LDP with \(J(w)=\log(1+w^2/2)\).

**5. Exact global rate-function ordering.** By evenness it suffices to take \(w>0\). With \(\theta=\theta(w)\) and \(z=-\log(1-\theta^2)>0\), Legendre differentiation gives \(I'(w)=\theta\), while \(J'(w)=w/(1+w^2/2)\) and \(w=z/\theta\). The inequality \(I'(w)>J'(w)\) is equivalent to
\[
G(z):=z^2-2z+2(1-e^{-z})>0.
\]
Indeed, \(G(0)=0\) and \(G'(z)=2(z-1+e^{-z})>0\) for \(z>0\), since \(z-1+e^{-z}\) starts at zero and has derivative \(1-e^{-z}>0\). Integrating from zero yields \(I(w)>J(w)\) for each \(w>0\).

**6. Local and distant asymptotics.** Taylor inversion of \(w=\theta+\theta^3/2+\theta^5/3+\cdots\) yields \(\theta=w-w^3/2+5w^5/12+O(w^7)\). Substitution into the Legendre transform gives the displayed sixth-order gap. Finally, \(\theta(w)\uparrow1\), \((1-\theta(w))w\to0\), and \(\operatorname{Li}_2(1)=\pi^2/6\); hence \(I(w)=w-\pi^2/12+o(1)\). The expansion of \(J\) follows directly from its logarithm.

## Verification

The companion `verify.py` requires `mpmath >= 1.3` and can be executed with `python verify.py`. It checks the finite scaled cumulant-product approximation at four tilt values and four shrinking reset strengths, differentiates the limiting cumulant function, numerically solves the variational critical-point equation, compares the two rates at seven positive points, checks symmetry and the analytic positive-gap expression, tests the sixth-order coefficient, and tests the distant asymptotic. A successful run reports 41 finite diagnostics. These tests diagnose arithmetic and normalization only; the LDP and strict global inequality are analytic results proved above.

## Relationship to prior work

[1] introduced the fast-weak-reset approximation, including the Itô diffusion and its exact stationary density for linear examples. Section S1.1 examines its Gaussian small-reset limit but does not give the stationary large-deviation rate of the underlying jump process or the strict comparison between the two rate functions.

[2] derived the exact product for the stationary transform of Brownian motion with proportional partial resetting; that product is fully acknowledged here. At fixed resetting rate it also shows a Gaussian weak-reset regime. The new analysis requires the joint rate-and-amplitude scaling and, crucially, the full strict comparison with the diffusion surrogate. Merely knowing the transform is not, by itself, a statement of the rate comparison.

[3] studies stationary far tails and time-dependent large deviations for fixed-parameter partial resetting and Lévy flights. Fixed-parameter spatial tails and long-time rate functions do not state the present joint weak-reset stationary LDP, and its diffusion-surrogate inequality is not supplied there.

## Limitations

This is a best-knowledge priority assessment, not a proof of absence from all literature: general transform-based large-deviation theorems might imply the first LDP statement, although the exact strict comparison and sixth-order onset were not found in the inspected sources. The statement makes no uniform relative-error estimate on actual pointwise densities and no assertion about nonlinear drift, heterogeneous reset multipliers, non-Poisson clocks, or finite-time paths. The two models' central stationary variances agree, so strict large-deviation separation must not be misinterpreted as a mismatch of ordinary variances.

## References

[1] Tobias Galla, *A diffusion approximation for systems with frequent weak resetting*, arXiv:2602.21635v1 (first public 2026-02-25), https://arxiv.org/html/2602.21635, especially Eq. (4), Eq. (5), and Supplement S1.1.

[2] Tal-Friedman, Roichman and Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363 (first public 2022-05-06), https://arxiv.org/html/2205.03363v2, especially Sec. II and Eq. (5).

[3] Di Bello et al., *Partial versus total resetting for Lévy flights in d dimensions*, arXiv:2501.01139 (first public 2025-01-02), https://arxiv.org/abs/2501.01139, especially stationary tails and dynamical large deviations.
