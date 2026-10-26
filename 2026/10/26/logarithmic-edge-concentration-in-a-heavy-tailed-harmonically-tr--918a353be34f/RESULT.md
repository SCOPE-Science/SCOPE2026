# Logarithmic edge concentration in a heavy-tailed harmonically trapped run-and-tumble particle

## Finding
Consider the stationary one-dimensional overdamped run-and-tumble dynamics
\[
\dot Y_t=-Y_t+\sigma_t,\qquad\sigma_t\in\{-1,+1\},
\]
where the sign alternates at successive renewal epochs and the independent strictly positive run durations have the common law of \(S\). Write \(\overline F(t)=\Pr(S>t)\) and \(m=\mathbb E S\). Assume that \(S\) has a continuous distribution, that \(0<m<\infty\), and that, for constants \(c>0\), \(\beta>1\), \(C<\infty\), and \(\eta>0\),
\[
\overline F(t)\sim c\,t^{-\beta}\quad(t\to\infty),
\qquad \Pr(S\le t)\le C t^\eta\quad(0<t<1).
\]
There is a unique stationary position law, supported on \((-1,1)\), and both endpoint probabilities have the exact asymptotic
\[
\boxed{\lim_{\varepsilon\downarrow0}
\bigl[\log(1/\varepsilon)\bigr]^{\beta-1}
\Pr(Y>1-\varepsilon)
=\frac{c}{2m(\beta-1)}}.
\]
The same limit holds with \(Y<-1+\varepsilon\) in place of \(Y>1-\varepsilon\). In particular, for every \(q>0\),
\[
\boxed{\mathbb E\bigl[(1-|Y|)^{-q}\bigr]=\infty.}
\]
The edge mass therefore decays as an inverse *power of the logarithm*, rather than the power of distance arising in the standard exponentially timed model.

The conclusion admits a finite-threshold renewal identity. Let \(D=1-Y_{\mathrm{start},+}\in(0,2)\) denote the distance to the right edge **at the beginning of a stationary positive run**, and define
\[
H(u)=\int_u^\infty\overline F(s)\,ds,\qquad
J(u)=\int_0^u\overline F(s)\,ds\quad(u\ge0).
\]
Then, for every \(0<\varepsilon<1\),
\[
\boxed{\Pr(Y>1-\varepsilon)
=\frac1{2m}\,\mathbb E\!\left[
H\!\left(\bigl[\log(D/\varepsilon)\bigr]_+\right)
+J\!\left(\bigl[\log(D/(2-\varepsilon))\bigr]_+\right)
\right],}
\]
with \([a]_+=\max(a,0)\). This exact identity also provides a non-rare-event route for evaluating the limiting law.

For Lomax waiting times \(\overline F(s)=(1+s)^{-\beta}\), the leading right-edge coefficient is exactly \(1/2\) for **every** \(\beta>1\). For the half-\(t\) law \(g(s)=(1+s^2)^{-3/2}\) considered as a waiting-time family in prior non-Markovian trapping work, the coefficient in this **harmonic** model is \(1/4\) and \(\beta=2\).

## Assumptions and scope
The sign switches deterministically at each renewal, rather than being independently redrawn; durations of successive positive and negative runs are iid. The process has no additional Brownian noise and the trap has linear force. The physical model \(\dot X=-kX+v\sigma\), with \(k,v>0\), reduces to the displayed dynamics under \(Y=kX/v\) and dimensionless durations \(S=kT\). If \(\Pr(T>t)\sim a t^{-\beta}\) and \(\mathbb ET=M\), the right-edge coefficient in physical units is \(a k^{\beta-1}/[2M(\beta-1)]\).

The finite-mean condition is essential for the stationary renewal construction. The small-time assumption rules out an exceptionally heavy concentration of arbitrarily short runs that could compete with the integrated long-run tail. No finite-time transient statement, added translational diffusion, general confining force, or infinite-mean switching law is covered.

## Proof
**1. Stationarity and switching-time contraction.** A two-sided equilibrium alternating-renewal sign process exists because \(0<m<\infty\); positive and negative signs each occupy stationary fraction \(1/2\). Define
\[
Y_t=\int_{-\infty}^{t}e^{-(t-u)}\sigma_u\,du.
\]
This is the unique stationary solution for the given stationary sign process: differences of solutions driven by the same sign decay as \(e^{-t}\). The representation gives \(|Y_t|\le1\), with strict inequality almost surely because both signs have occupied positive-length intervals in the past. Equivalently, the positions at successive switching times follow the affine contraction \(y\mapsto\sigma+(y-\sigma)e^{-S}\), whose products of contraction coefficients vanish almost surely; this determines the unique stationary switch-position distribution.

**2. A lower-tail bound for the starting gap.** At a positive-run entrance the previous negative run has duration \(U\) distributed as \(S\), and its starting position \(Z\le1\) yields
\[
Y_{\mathrm{start},+}=-1+(Z+1)e^{-U},\qquad
D=2-(Z+1)e^{-U}\ge2(1-e^{-U}).
\]
Therefore \(0<D\le2\) almost surely, and for sufficiently small \(\delta>0\),
\[
\Pr(D<\delta)\le
\Pr\!\left(U<-\log(1-\delta/2)\right)
=O(\delta^\eta).
\]
The position at an entrance is independent of the *next* run duration, by iid renewal sampling. Consequently the entrance gap \(D\) is also independent of the age of the current interval in an equilibrium time sample, conditional on the sign.

**3. Exact finite-threshold identity.** In a stationary positive run, the (joint, sign-unconditional) age measure is \(\overline F(a)\,da/(2m)\). At age \(a\), the distance to the right edge is \(De^{-a}\). The condition \(De^{-a}<\varepsilon\) is \(a>\bigl[\log(D/\varepsilon)\bigr]_+\), apart from an endpoint event of probability zero. Integrating the age measure produces the first \(H\)-term. In a negative run, the position is \(-1+D_-e^{-a}\), where \(D_-=1+Y_{\mathrm{start},-}\) has the same law as \(D\) by reflection. It exceeds \(1-\varepsilon\) exactly when \(D_->2-\varepsilon\) and \(a<\log(D_-/(2-\varepsilon))\). Integrating yields the \(J\)-term. Adding the disjoint sign events gives the claimed exact identity.

**4. Sharp boundary coefficient.** Since \(D\le2\), the negative-run contribution obeys
\[
0\le\frac1{2m}\mathbb EJ\!\left(
\bigl[\log(D/(2-\varepsilon))\bigr]_+\right)
\le\frac1{2m}\log\frac2{2-\varepsilon}=O(\varepsilon).
\]
Integrating the power-law survival tail gives
\[
H(L)\sim\frac{c}{\beta-1}L^{1-\beta}
\quad(L\to\infty).
\]
Set \(L=\log(1/\varepsilon)\). On \(D\ge e^{-L/2}\), the ratio \(H(L+\log D)/H(L)\) tends to one almost surely, and for large \(L\) it is bounded by the finite ratio \(H(L/2)/H(L)\). Dominated convergence applies. On the exceptional event \(D<e^{-L/2}\), the expected contribution is at most \(m\Pr(D<e^{-L/2})=O(e^{-\eta L/2})=o(H(L))\). Hence
\[
\mathbb E\,H\!\left([L+\log D]_+\right)\sim H(L).
\]
Combining the two sign contributions proves the displayed coefficient. Reflection gives the left-edge law. For Lomax waiting times \(m=1/(\beta-1)\) and \(c=1\), giving coefficient \(1/2\). For the half-\(t\) density, \(m=1\) and \(\overline F(t)=1-t/\sqrt{1+t^2}\sim(2t^2)^{-1}\), giving \(1/4\).

**5. Divergent reciprocal-gap moments.** Symmetry and disjointness of the two sufficiently narrow edge events yield
\[
\Pr(1-|Y|<\varepsilon)
\sim\frac{c}{m(\beta-1)}[\log(1/\varepsilon)]^{1-\beta}.
\]
For any \(q>0\), substituting \(\varepsilon=z^{-1/q}\) shows that the survival probability of \((1-|Y|)^{-q}\) decreases only as a positive multiple of \((\log z)^{1-\beta}\). Its integral over \(z\ge1\) diverges, proving the final assertion.

## Verification
The standalone `verify.py` implements the exact switching-time affine recurrence and samples the equilibrium interval age independently of the switching-time state, without numerically integrating a stochastic differential equation. It compares the exact renewal identity with independent age-and-sign stationary sampling for multiple nonzero thresholds. Four Lomax exponents and the half-\(t\) law are checked; the limiting constants are also checked using conditional expectation rather than rare-event counting. Run `python3 verify.py` with NumPy installed. The recorded run completed 24 comparisons successfully. These finite tests are consistency checks, not proofs of the \(\varepsilon\downarrow0\) limits or of infinite moments.

## Relationship to prior work
Farago and Smith (2024; arXiv:2401.01576) provide general stationary integral equations and a numerical method for one-dimensional **non-Markovian** trapped run-and-tumble dynamics; they examine half-\(t\) waiting times numerically under the nonlinear force \(-\sin(\pi x/2)\), observing vanishing effective edge switching rates. Their framework determines the distribution implicitly, but the inspected analysis does not provide the explicit integrated log-edge mass coefficient above for a harmonic force or the reciprocal-gap moment classification. The present theorem shares the underlying model class and does not claim the general stationary equations as new.

Guéneau, Majumdar, and Schehr (2023; arXiv:2306.09453, Appendix B) and their 2026 follow-up (arXiv:2602.08436) treat exponentially timed trapped run-and-tumble models, for which the near-edge scaling is algebraic in distance rather than logarithmic. Datta, Beta, and Großmann (2024; arXiv:2406.15277) analyze arbitrary waiting-time transport in homogeneous media, not the stationary endpoint geometry created by harmonic confinement. Xu, Zhou, Metzler, and Deng (2020; arXiv:2004.09775) study a different inertial Lévy-walk model that evolves through a second-order harmonic oscillator between renewal events. None of these inspected results states the exact boundary constant for the present overdamped heavy-tailed model.

## Limitations
The theorem is stationary and one-dimensional, with exact deterministic orientation reversal and no translational thermal noise. It does not describe finite observation-time convergence, inference of unknown heavy-tail exponents, or the behavior when the mean run time is infinite. The exact finite-threshold formula involves the endogenous entrance-gap distribution, which is not evaluated in closed form for an arbitrary renewal law. Independent validation and exhaustive publication-priority assessment have not been performed.

## References
1. O. Farago and N. R. Smith, *Confined run and tumble particles with non-Markovian tumbling statistics*, arXiv:2401.01576, publicly available 2024-01-03; *Physical Review E* 109, 044121 (2024).
2. M. Guéneau, S. N. Majumdar, and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453 (2023), Appendix B.
3. A. Datta, C. Beta, and R. Großmann, *The random walk of intermittently self-propelled particles*, arXiv:2406.15277, publicly available 2024-06-21.
4. P. Xu, T. Zhou, R. Metzler, and W. Deng, *Lévy walk dynamics in an external harmonic potential*, arXiv:2004.09775 (2020).
5. M. Guéneau, S. N. Majumdar, and G. Schehr, *Exact Stationary State of a \(d\)-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436 (2026).
