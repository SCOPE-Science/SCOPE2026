# Unique optimal local-ratchet resetting rate and a refractory crossover in near-perfect asymmetry

## Finding

For the free-excursion, instantaneous-asymmetric-capture Brownian ratchet defined below, with any strictly asymmetric but nondegenerate catchment geometry, **the magnitude of the long-run velocity has precisely one global maximum as a function of the Poisson capture rate**. This optimum strictly decreases with a fixed post-capture refractory delay and strictly increases with the degree of geometric asymmetry. Two distinct near-perfect-asymmetry scaling laws are rigorously established, with or without delay.

Take \(0<\delta<1\), \(D,L>0\), \(\tau\geq0\), and define
\[
 y=\frac L2\sqrt{\frac rD},\qquad
 \eta=\frac{4D\tau}{L^2},\qquad
 F_{\delta,\eta}(y)=\frac{y^2\sinh(\delta y)}{(1+\eta y^2)\sinh y}.
\]
The long-run drift has magnitude \(2D F_{\delta,\eta}(y)/L\). Its unique maximizer \(y_*(\delta,\eta)\) is the unique positive root of
\[
 \frac{2}{y(1+\eta y^2)}+\delta\coth(\delta y)-\coth y=0,
\]
so the unique optimal resetting rate is \(r_*=4D y_*^2/L^2\). For fixed \(0<\delta<1\), as \(\tau\to\infty\),
\[
 y_*\sim\left[\frac{6}{\eta(1-\delta^2)}\right]^{1/4},\qquad
 r_*\sim\frac{2\sqrt{6D}}{L\sqrt{\tau(1-\delta^2)}}.
\]
For \(\varepsilon=1-\delta\downarrow0\) at fixed \(\eta\),
\[
 y_*\sim\begin{cases}2/\varepsilon,&\eta=0,\\ [2/(\eta\varepsilon)]^{1/3},&\eta>0.\end{cases}
\]
Thus the optimal rate diverges respectively with exponents \(2\) and \(2/3\) in \(\varepsilon^{-1}\). The speed supremum in the long-refractory limit obeys \(\max_r |v(r,\tau)|\sim \delta L/(2\tau)\).

## Assumptions and scope

Fix \(L>0,D>0,r>0,\tau\geq0\), and the left-basin distance \(a\in(0,L)\) with \(a\ne L/2\). A particle starts at a lattice site \(kL\), runs a free Brownian excursion \(\sqrt{2D}\,W_t\) for an independent exponential time of rate \(r\), then jumps instantaneously to the unique lattice site \(jL\) whose catchment interval is \((jL-a,(j+1)L-a)\). A deterministic refractory period \(\tau\) follows, during which the particle is immobilized at that site. The Brownian motion and exponential clock are then restarted independently. Boundary ties have probability zero. The Poisson rate operates during excursions only, and \(\tau\) is an actual fixed delay, not a random return time. Set \(\delta=|2a/L-1|\) and \(s=\operatorname{sgn}(2a/L-1)\). The long-run velocity is \(\lim_{t\to\infty}X_t/t\), almost surely and in mean, when starting at any lattice site. No finite potential height or noisy return dynamics are claimed.

The symmetric geometry \(a=L/2\) has identically zero drift; the perfectly asymmetric endpoint \(a\in\{0,L\}\) is excluded from uniqueness, and is addressed only as a singular limit. A deterministic delay is imposed after the instantaneous relocation and is absent when \(\tau=0\).

## Proof

**1. One-cycle distribution and renewal drift.** Set \(q=\sqrt{r/D}\) and let \(T\sim\operatorname{Exp}(r)\) be independent of Brownian motion. The endpoint \(Z=\sqrt{2D}W_T\) has density \(f_Z(z)=q e^{-q|z|}/2\), directly from the Laplace transform of the Gaussian heat kernel. Let \(J\in\mathbb Z\) satisfy \(Z\in(JL-a,(J+1)L-a)\). For every integer \(n\geq1\),
\[
 \Pr(J\geq n)=\tfrac12e^{-q(nL-a)},\qquad
 \Pr(J\leq-n)=\tfrac12e^{-q((n-1)L+a)}.
\]
The tail-sum formula, two geometric series, and hyperbolic-function algebra therefore give
\[
 \mathbb EJ=\frac{e^{-q(L-a)}-e^{-qa}}{2(1-e^{-qL})}
 =\frac{\sinh(q(a-L/2))}{2\sinh(qL/2)}
 =s\frac{\sinh(\delta y)}{2\sinh y}.
\]
Each cycle advances by \(LJ\) and has duration \(T+\tau\), independently of other cycles. Both have finite moments. The renewal-reward strong law gives
\[
 v(r,\tau)=\lim_{t\to\infty}\frac{X_t}{t}
 =\frac{L\mathbb EJ}{r^{-1}+\tau}
 =s\frac{2D}{L}\frac{y^2\sinh(\delta y)}{(1+\eta y^2)\sinh y}.
\]
The unfinished Brownian excursion is negligible divided by time, by integrability of its within-cycle supremum. Its contribution to mean velocity is negligible as well.

**2. Strict uniqueness.** For \(0<\delta<1\), logarithmic differentiation gives \(F'/F=G\), where
\[
 G(y)=\frac2{y(1+\eta y^2)}+\delta\coth(\delta y)-\coth y.
\]
The critical global inequality is
\[
 G'(y)=-\frac{2(1+3\eta y^2)}{y^2(1+\eta y^2)^2}
 -\frac{\delta^2}{\sinh^2(\delta y)}+\frac1{\sinh^2 y}<0.
\]
Indeed, strict convexity of \(\sinh\) with value zero at zero implies \(\sinh(\delta y)<\delta\sinh y\); hence the last two terms have negative sum. Also \(G(y)=2/y+O(y)\) for \(\eta=0\), while for fixed \(\eta\), the same \(2/y\) leading behavior holds as \(y\downarrow0\), and \(G(y)\to\delta-1<0\) as \(y\to\infty\). Exactly one positive zero exists, \(F\) increases strictly before it and decreases strictly after it. Its endpoint limits are \(F(y)\to0\) at both ends, proving uniqueness of the global maximum.

**3. Parameter ordering.** At every \(y>0\),
\[
 \partial_\eta G=-\frac{2y}{(1+\eta y^2)^2}<0,
 \qquad
 \partial_\delta G=\coth(\delta y)-\frac{\delta y}{\sinh^2(\delta y)}>0.
\]
The second inequality follows from \(\sinh z\cosh z>z\) for \(z>0\). Because \(G_y<0\), implicit differentiation yields \(\partial_\eta y_*<0\) and \(\partial_\delta y_*>0\). The optimal \(r_*\) has the same strict signs.

**4. Large deterministic delay.** At fixed \(\delta\), as \(\eta\to\infty\), the strict root moves to zero: for each fixed positive \(y\), the positive first term of \(G\) tends to zero, while \(\delta\coth(\delta y)-\coth y<0\). Expand at the shrinking root:
\[
 \coth y-\delta\coth(\delta y)
 =\frac{1-\delta^2}{3}y+O_\delta(y^3).
\]
The root equation forces \(\eta y_*^2\to\infty\), since otherwise its first term would be of order \(1/y_*\) rather than order \(y_*\). Consequently \(\eta y_*^4\to6/(1-\delta^2)\). Conversion to \(r_*\) gives the stated dimensionful law. Substitution into the exact speed, using \(\sinh(\delta y)/\sinh y\sim\delta\) and \(\eta y_*^2\to\infty\), yields \(\max_r|v|\sim\delta L/(2\tau)\).

**5. Nearly perfect asymmetry: two genuinely different exponents.** Write \(\delta=1-\varepsilon\) and fix \(\eta\geq0\). At any fixed \(y>0\), \(G(y)\to2/[y(1+\eta y^2)]>0\) as \(\varepsilon\downarrow0\); hence its unique root diverges. Uniformly along these diverging roots,
\[
 \coth y-\delta\coth(\delta y)=\varepsilon+O(e^{-2\delta y}),
\]
where the error is smaller than any power of \(\varepsilon\) once the root's scale is established by elementary upper/lower barriers around \(y\asymp\varepsilon^{-1}\) for \(\eta=0\), or \(y\asymp\varepsilon^{-1/3}\) for fixed \(\eta>0\). Equating the leading terms \(2/y=\varepsilon\) for zero delay or \(2/(\eta y^3)=\varepsilon\) for positive delay proves the two stated scalings. At the degenerate endpoint \(\delta=1\), the speed becomes monotone in \(y\), so the excluded endpoint is genuinely singular.

## Verification

Run `python3 verify.py` using the Python standard library. It implements the exact tail-sum for the integer displacement independently of the closed hyperbolic expression, brackets the unique root without symbolic root assumptions, tests rate and parameter monotonicity, and checks both limiting exponents against multiple parameter values. The supplied program passed 116 reproducibility assertions. These finite numerical checks do not prove the all-parameter theorem: the convexity inequality and asymptotic root equations above provide that proof.

## Relationship to prior work

Ghosh, Nayak, Liu, Li, and Marchesoni (2023) proposed local resets to the bottoms of asymmetric potential wells and observed an optimal resetting timescale numerically. Roberts, Sezik, and Lardet (2024), Section IV, Eq. (24), already give the **instantaneous-ratchet current formula** on a periodic domain; this is the exact \(\tau=0\) input and is **not** claimed as original. Their Section IV also plots nonmonotone mean velocities, and Appendix C studies a different stop-and-start static-ratchet model. Alston and Bertrand (2024) study local resetting to symmetric nearest sites and diffusion enhancement, not the asymmetric-capture velocity-rate design here.

The new theorem concerns the strict global uniqueness and monotone comparative statics with a deterministic refractory period, together with two sharply different, proved rate-divergence exponents at nearly perfect asymmetry and the long-latency scale. Prior exact-current identities are essential antecedents, not gaps to obscure. A general renewal optimization result may encompass part of this extension and should be checked independently before claiming publication-level priority.

## Limitations

The theorem is a free-Brownian-excursion, instantaneous-relocation idealization with a fixed zero-motion refractory delay. A finite sloping ratchet has return times, noise, and substrate forces not treated here. It does not justify replacing a weak but finite potential by this ideal model without an additional approximation theorem. It makes no claim about optimal efficiency, energy costs, fluctuations of empirical velocity, stochastic delays, or generic non-exponential excursion times. Uniqueness excludes symmetric basins, where the velocity is identically zero. Scientific correctness is supported analytically and computationally but has not received independent audit; a close 2024 exact-current antecedent creates a material originality/priority risk.

## References

1. P. K. Ghosh, S. Nayak, J. Liu, Y. Li, F. Marchesoni, *Autonomous Ratcheting by Stochastic Resetting* (first arXiv public version 2023-07-12), arXiv:2307.06202. https://arxiv.org/abs/2307.06202
2. C. Roberts, E. Sezik, E. Lardet, *Ratchet-mediated resetting: Current, efficiency, and exact solution* (first arXiv public version 2024-05-17), arXiv:2405.10698, especially Section IV, Eq. (24), and Appendix C. https://arxiv.org/abs/2405.10698
3. H. Alston and T. Bertrand, *Boosting macroscopic diffusion with local resetting* (first arXiv public version 2024-01), arXiv:2401.12772. https://arxiv.org/abs/2401.12772
