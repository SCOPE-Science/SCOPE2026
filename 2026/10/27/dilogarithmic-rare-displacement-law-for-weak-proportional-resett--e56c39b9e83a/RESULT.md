# Dilogarithmic rare-displacement law for weak proportional resetting

## Finding

For the one-dimensional Brownian motion with proportional Poisson resetting, the stationary state is approximately Gaussian on its central-fluctuation scale when the reset contraction approaches one. Its *rare-displacement* scale nevertheless has a different, exact large-deviation law.

Fix Brownian diffusivity \(D>0\) and reset rate \(r>0\). At each reset, replace the current position \(X\) by \(cX\), where \(-1<c<1\). Put \(\alpha=\sqrt{r/D}\), \(\varepsilon=-\log(c^2)\), and consider \(|c|=e^{-\varepsilon/2}\uparrow1\). Let \(X_\varepsilon\) have the unique stationary position law and set \(Y_\varepsilon=\varepsilon\alpha X_\varepsilon\). This applies on approach to either endpoint, \(c\uparrow1\) or \(c\downarrow-1\).

**Theorem.** The variables \(Y_\varepsilon\) obey a full large-deviation principle on \(\mathbb R\), with speed \(1/\varepsilon\) and the good, even, strictly convex rate function

\[
I(y)=\sup_{-1<\theta<1}\{\theta y-\operatorname{Li}_2(\theta^2)\},
\qquad
\operatorname{Li}_2(z)=\sum_{m=1}^{\infty}\frac{z^m}{m^2}.
\]

Precisely, for every open \(G\subset\mathbb R\) and closed \(F\subset\mathbb R\),

\[
\liminf_{\varepsilon\downarrow0}\varepsilon\log\Pr(Y_\varepsilon\in G)\ge-\inf_{y\in G}I(y),
\qquad
\limsup_{\varepsilon\downarrow0}\varepsilon\log\Pr(Y_\varepsilon\in F)\le-\inf_{y\in F}I(y).
\] In particular, for each fixed \(y>0\),

\[
\lim_{\varepsilon\downarrow0}\varepsilon\log\Pr(Y_\varepsilon\ge y)=-I(y).
\]

For every \(y>0\), its maximizing parameter \(\theta_y\in(0,1)\) is the unique solution of

\[
y=-\frac{2\log(1-\theta_y^2)}{\theta_y},
\qquad I(y)=y\theta_y-\operatorname{Li}_2(\theta_y^2).
\]

The exact crossover between Gaussian-core and exponential-tail rates is

\[
I(y)=\frac{y^2}{4}-\frac{y^4}{64}+O(y^6)\quad(y\to0),
\qquad
I(y)=|y|-\frac{\pi^2}{6}+e^{-|y|/2}+O(|y|e^{-|y|})\quad(|y|\to\infty).
\]

Moreover \(0<I(y)<y^2/4\) whenever \(y\ne0\), so the weak-resetting Gaussian approximation understates every fixed nonzero rare-displacement probability at the leading exponential scale.

The theorem includes the finite-parameter bound, valid for all \(\varepsilon>0\) and \(|\theta|<1\),

\[
0\le\varepsilon\log\mathbb E\exp\!\left(\frac{\theta Y_\varepsilon}{\varepsilon}\right)-\operatorname{Li}_2(\theta^2)
\le\varepsilon\log\frac1{1-\theta^2}.
\]

## Assumptions and scope

The process is the continuous-time Markov jump diffusion with generator

\[
(\mathcal L f)(x)=D f''(x)+r\bigl(f(cx)-f(x)\bigr).
\]

Between jumps, \(dX_t=\sqrt{2D}\,dW_t\); the jump clock is independent and Poisson with rate \(r\); a jump multiplies the *current* state by the deterministic factor \(c\). The process lives on the full real line. Negative \(c\) additionally reflects the state at each reset. The stationary law is centered and symmetric for either sign. The boundary cases \(|c|=1\) have no finite-variance stationary law and are excluded before taking the limit.

The statement is about one-time *stationary* position statistics and a weak-contraction parameter limit, not time averages or first-passage times. The whole real-line LDP uses open and closed sets at fixed macroscopic \(y\); no uniform estimate at simultaneously varying or diverging \(y\) is claimed.

## Proof

**1. Existence, uniqueness, and exact stationary transform.** Couple two solutions with the same Brownian path and jump times. Their difference at time \(t\) is exactly \(c^{N_t}\) times its initial value, and tends to zero almost surely when \(|c|<1\). A stationary construction uses a two-sided Brownian motion and jump clock:

\[
X_0=\sqrt{2D}\int_{-\infty}^{0}c^{N(s,0]}\,dW_s.
\]

The integral is well-defined in \(L^2\), since its expected quadratic variation is \(2D/[r(1-c^2)]\). This also proves existence and, with coupling, uniqueness.

Writing the stationary characteristic function as \(\phi(k)=\mathbb E e^{ikX_0}\), the generator identity gives

\[
(r+Dk^2)\phi(k)=r\phi(ck).
\]

Iteration, \(\phi(0)=1\), and continuity at zero yield

\[
\phi(k)=\prod_{j=0}^{\infty}\frac1{1+(D/r)c^{2j}k^2}.
\]

Equivalently, \(X_\varepsilon\) is a convergent sum of independent centered Laplace variables having scales \(\alpha^{-1}e^{-j\varepsilon/2}\). This exact representation is **previously established** in the positive-contraction model; its one-point transform is also unchanged when \(c\) is replaced by \(-c\). In particular, for \(|\theta|<1\),

\[
\mathbb E e^{\theta\alpha X_\varepsilon}
=\prod_{j=0}^{\infty}(1-\theta^2e^{-j\varepsilon})^{-1}.
\]

For \(|\theta|\ge1\) this exponential moment diverges, already because of the first Laplace summand.

**2. The limiting pressure and a quantitative error bound.** Set

\[
\Lambda_\varepsilon(\theta)=\varepsilon\log\mathbb E\exp\left(\frac{\theta Y_\varepsilon}{\varepsilon}\right)
=\varepsilon\sum_{j=0}^{\infty}-\log(1-\theta^2e^{-j\varepsilon}).
\]

For \(|\theta|<1\), the summand \(f_\theta(s)=-\log(1-\theta^2e^{-s})\) is nonnegative, integrable and decreasing on \([0,\infty)\). Its integral lies below the left Riemann sum by at most \(\varepsilon f_\theta(0)\). Expansion into an absolutely summable exponential series gives

\[
\int_0^\infty f_\theta(s)\,ds
=\sum_{m=1}^{\infty}\frac{\theta^{2m}}{m^2}
=\operatorname{Li}_2(\theta^2).
\]

Thus \(\Lambda_\varepsilon\to\Lambda=\operatorname{Li}_2(\theta^2)\), with the stated explicit error bound. Differentiating the same sums on compact subintervals of \((-1,1)\) shows convergence of the first two derivatives. In particular, \(\sup_{0<\varepsilon\le1}\Lambda_\varepsilon''(\theta)<\infty\) for each fixed interior \(\theta\).

**3. Full large deviations without an endpoint regularity shortcut.** The limiting pressure on \((-1,1)\) has

\[
\Lambda'(\theta)=-\frac{2\log(1-\theta^2)}{\theta}
\]

(with continuous value zero at zero), and \(\Lambda''(\theta)>0\). Its derivative maps \((-1,1)\) bijectively onto \(\mathbb R\). For any target \(y\), take the unique \(\theta_y\) with \(\Lambda'(\theta_y)=y\). The tilted probability law with density proportional to \(\exp(\theta_yY_\varepsilon/\varepsilon)\) has expectation \(\Lambda_\varepsilon'(\theta_y)\to y\) and variance \(\varepsilon\Lambda_\varepsilon''(\theta_y)=O(\varepsilon)\). Under the tilt, \(Y_\varepsilon\) therefore concentrates at \(y\). Undoing the tilt inside an arbitrarily small neighborhood gives the LDP lower bound with exponent \(-I(y)\), hence the lower bound for every open set.

For the upper bound on a compact set, apply exponential Markov inequalities with finitely many interior parameters \(\theta\in(-1,1)\) chosen to approximate the Legendre supremum on a finite covering. Exponential tightness follows from the same Markov bounds for one fixed positive and one fixed negative interior parameter: for any \(0<\theta<1\),

\[
\limsup_{\varepsilon\downarrow0}\varepsilon\log\Pr(|Y_\varepsilon|\ge R)
\le-\theta R+\operatorname{Li}_2(\theta^2).
\]

Letting \(R\to\infty\) proves exponential tightness and promotes the compact upper bound to all closed sets. This argument avoids assuming lower semicontinuity of the *raw* limiting moment-generating function at \(\theta=\pm1\), where each finite-parameter moment diverges but the interior limiting pressure remains finite.

**4. Rate geometry and tails.** The derivative map establishes that \(I\) is even, nonnegative, strictly convex, and smooth, with \(I(0)=0\); the interior linear test \(\theta y-\Lambda(\theta)\) makes its level sets compact. The power series

\[
\Lambda(\theta)=\theta^2+\frac{\theta^4}{4}+O(\theta^6)
\]

and inversion of \(y=\Lambda'(\theta)\) give \(\theta_y=y/2-y^3/16+O(y^5)\) and the stated small-\(y\) expansion. For \(y>0\), the positive series implies \(\Lambda(\theta_y)>\theta_y^2\); hence

\[
0<I(y)=y\theta_y-\Lambda(\theta_y)<y\theta_y-\theta_y^2\le y^2/4.
\]

For large \(y>0\), set \(\delta=1-\theta_y^2\). The defining equation becomes \(\log\delta=-y\sqrt{1-\delta}/2\), so \(\delta=e^{-y/2}+O(ye^{-y})\). Using

\[
\operatorname{Li}_2(1-\delta)=\frac{\pi^2}{6}+\delta\log\delta-\delta+O(\delta^2|\log\delta|)
\]

in \(I(y)=y\sqrt{1-\delta}-\operatorname{Li}_2(1-\delta)\) gives \(I(y)=y-\pi^2/6+e^{-y/2}+O(ye^{-y})\). Symmetry gives the negative-tail formula. Strict monotonicity on the positive half-line turns the LDP for half-lines into the stated exact logarithmic tail probability.

## Verification

`verification_check.py` is a standalone Python-standard-library check. It evaluates the limiting dilogarithm both by a convergent series and by an independent quadrature; tests the finite-parameter Riemann-sum bounds for twelve parameter pairs; reconstructs saddle points by bisection; tests strict Gaussian comparisons; and checks the local and far-tail expansions. The archived run passed 79 deterministic comparisons. The script and its exact output are embedded alongside this document. These finite computations are secondary checks; the argument above proves the infinite-dimensional stationarity construction and the limiting probability theorem.

## Relationship to prior work

Pierce's April 14, 2022 preprint introduces proportional resetting and solves stationary moments and densities, with the Gaussian limit under weak resetting. Tal-Friedman, Roichman and Reuveni (May 6, 2022) derive the independent-Laplace representation and infinite-product transform used as the starting point in step 1. Biroli, Feld, Hartmann, Majumdar and Schehr (June 12, 2024) study the rescaling model for both signs, give exact stationary distributions and fixed-parameter Gaussian-center/exponential-tail behavior, and analyze first-passage times. The present result concerns a *different, joint* weak-contraction/rare-position limit: the full logarithmic probability rate, its dilogarithmic pressure, finite-parameter pressure enclosure and precise interpolation between quadratic and linear rate regimes. Fixed-parameter exponential tails and ordinary central Gaussian convergence do not supply this quantified crossover by themselves.

The large-deviation lower/upper-bound methods and the dilogarithm identity are established mathematical tools, not claimed as new. Meylahn, Sabhapandit and Touchette's resetting large deviations concern long-time additive functionals, rather than the stationary one-point distribution in a vanishing-contraction regime. Novelty of this particular application and its sharp crossover has been assessed against these closest sources, but priority in the broader geometric-perpetuity literature remains a genuine risk.

## Limitations

This theorem treats Brownian motion with deterministic multiplicative partial resets, constant independent Poisson rate, stationary initialization, and fixed positive \(D,r\). It does not give prefactors for large-deviation probabilities, uniform estimates for thresholds growing with \(\varepsilon^{-1}\), a path-space large-deviation principle, or results for stochastic contraction factors and non-Poisson clocks. The weak-contraction limit and the long-time limit used to construct stationarity must not be interchanged without separate justification. Independent scholarly priority assessment has not been performed.

## References

1. J. Kevin Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215, first posted April 14, 2022. https://arxiv.org/abs/2204.07215
2. O. Tal-Friedman, Y. Roichman and S. Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363, first posted May 6, 2022. https://arxiv.org/abs/2205.03363
3. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387, first posted June 12, 2024. https://arxiv.org/html/2406.08387v1
4. J. M. Meylahn, S. Sabhapandit and H. Touchette, *Large deviations for Markov processes with resetting*, Phys. Rev. E 92, 062148 (2015). https://doi.org/10.1103/PhysRevE.92.062148
