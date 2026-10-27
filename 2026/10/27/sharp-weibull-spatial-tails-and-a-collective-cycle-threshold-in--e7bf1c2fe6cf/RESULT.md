# Sharp Weibull spatial tails and a collective-cycle threshold in intermittently confined Brownian diffusion

## Finding

In an alternating diffusive/free and harmonic/confining Brownian process, Weibull-distributed free residence times generate **sharp stationary stretched-exponential spatial tails**. The tail exponent is \(2p/(p+1)\); the leading coefficient changes mechanism at the Weibull shape \(p=1\). Below and at this threshold one unusually long free interval already achieves the sharp leading rate, which is insensitive to the strength or duration of the confining episode. Above the threshold, rare excursions cooperate across multiple earlier free intervals; the complete geometric history enters the sharp coefficient.

Write \(c=e^{-2\kappa\tau}\), and define
\[
 a_p=\frac1{\theta^p}\begin{cases}1,&0<p\le1,\\ (1-c^{p/(p-1)})^{p-1},&p>1.\end{cases}
 \qquad
 K_p=\frac{(p+1)a_p^{1/(p+1)}}{(4Dp)^{p/(p+1)}}.
\]
Then the stationary position \(X\) satisfies
\[
\boxed{\lim_{x\to\infty}\frac{\log\Pr(X>x)}{x^{2p/(p+1)}}=
\lim_{x\to\infty}\frac{\log\Pr(X<-x)}{x^{2p/(p+1)}}=-K_p.}
\]
The underlying conditional stationary variance \(V\) has a separate sharp asymptotic,
\[
\boxed{\lim_{w\to\infty}w^{-p}\log\Pr\{(V-D/\kappa)/(2D)>w\}=-a_p.}
\]
In particular, for the Rayleigh case \(p=2\),
\[
\boxed{K_2=\frac34\left(\frac{1-e^{-4\kappa\tau}}{D^2\theta^2}\right)^{1/3}},
\qquad\log\Pr(X>x)\sim-K_2x^{4/3}.
\]

## Assumptions and scope

Fix \(D,\kappa,\tau,\theta,p>0\). The real-valued position follows the Itô dynamics
\[
 dX_t=-\kappa\,\mathbf1_{\{\mathrm{on}\}}(t)X_t\,dt+\sqrt{2D}\,dB_t.
\]
The alternating environment has mutually independent off intervals \(T_n\) with continuous survival function \(\Pr(T_n>t)=e^{-(t/\theta)^p}\), each followed by an on interval of deterministic length \(\tau\); the Brownian noise is independent of the environment. No position jump is imposed at a switch. The environment is observed under its stationary alternating-renewal law. Since \(\mathbb ET=\theta\Gamma(1+1/p)<\infty\), the on-phase probability is \(\tau/(\mathbb ET+\tau)\) and the off-phase probability is \(\mathbb ET/(\mathbb ET+\tau)\). The positive on-phase duration produces a contraction each cycle, yielding a unique stationary position law. All limits keep the five physical parameters fixed and positive.

## Proof

**1. Stationary variance representation.** Given the entire switching path, the stationary solution is centered Gaussian. Let \(v_0=D/\kappa\) and \(W=(V-v_0)/(2D)\). In a free episode of length \(t\), \(W\) increases by \(t\). In a confined episode of length \(t\), \(W\) is multiplied by \(e^{-2\kappa t}\). Thus, at a free-episode entrance, successive cycles satisfy \(W_{n+1}=c(W_n+T_n)\). Iterating backward produces the almost surely finite perpetuity \(W_{\rm entrance}=\sum_{j\ge1}c^jT_j\). Finiteness follows from \(c<1\) and \(\mathbb ET<\infty\).

At a stationary time conditioned on being free, the age \(A\) is independent of preceding cycles and has density
\[
 f_A(a)=\frac{\Pr(T>a)}{\mathbb ET}=\frac{e^{-(a/\theta)^p}}{\theta\Gamma(1+1/p)},\quad a\ge0.
\]
Consequently,
\[
 W_{\rm off}\stackrel d=A+\sum_{j\ge1}c^jT_j.
\]
Conditioned on being confined, the current on-age \(U\) is uniform on \([0,\tau]\) and independent of previous intervals, so
\[
 W_{\rm on}\stackrel d=e^{-2\kappa U}\sum_{j\ge0}c^jT_j.
\]
In these displays, all \(T_j,A,U\) are mutually independent as appropriate. The unconditional \(W\) is the two-phase mixture with the stationary phase probabilities stated above.

**2. Free-variance tail for \(0<p\le1\).** The variables \(T^p\) and \(A^p\) have exponential moments \(\mathbb E e^{\lambda T^p}\) and \(\mathbb E e^{\lambda A^p}\) finite for every \(\lambda<\theta^{-p}\). For nonnegative inputs, \((u+v)^p\le u^p+v^p\). Hence, for such \(\lambda\), independence, the contraction \(c<1\), and convergence of \(\sum_{j\ge1}c^{jp}\) give \(\mathbb E e^{\lambda W_{\rm off}^p}<\infty\) and \(\mathbb E e^{\lambda W_{\rm on}^p}<\infty\). More explicitly, the infinite product of moment-generating functions converges because each logarithm is \(O(c^{jp})\) for large \(j\). Markov's inequality yields \(\limsup_{w\to\infty}w^{-p}\log\Pr(W>w)\le-\theta^{-p}\). For the matching lower bound, the off phase occurs with strictly positive probability and \(W_{\rm off}\ge A\). Integrating the displayed density shows \(\lim_{w\to\infty}w^{-p}\log\Pr(A>w)=-\theta^{-p}\). Thus the proposed limit holds.

**3. Free-variance tail for \(p>1\).** Set \(q=p/(p-1)\) and \(b_p=(p-1)p^{-q}\theta^q\). Laplace's method applied directly to the positive Weibull densities gives
\[
 \lim_{s\to\infty}s^{-q}\log\mathbb E e^{sT}=
 \lim_{s\to\infty}s^{-q}\log\mathbb E e^{sA}=b_p.
\]
The polynomial density factors do not affect the leading saddle exponent. Since \(\log\mathbb E e^{sT}\le(b_p+\varepsilon)s^q+C_\varepsilon s\) and likewise for \(A\), summing over the geometrically weighted independent intervals gives
\[
 \lim_{s\to\infty}s^{-q}\log\mathbb E e^{sW_{\rm off}}=
 \frac{b_p}{1-c^q}.
\]
For the on state, \(W_{\rm on}\le\sum_{j\ge0}c^jT_j\); its moment-growth upper bound has the same coefficient, so the unconditional mixture obeys the corresponding upper bound. Optimizing Chernoff's inequality in \(s\) establishes
\[
 \limsup_{w\to\infty}\frac{\log\Pr(W>w)}{w^p}
 \le-\frac{(1-c^q)^{p-1}}{\theta^p}.
\]
For the lower bound, fix a positive integer \(N\) and put \(S_N=\sum_{j=0}^Nc^{jq}\). In the off state require \(A\ge w/S_N\) and \(T_j\ge wc^{j/(p-1)}/S_N\) for every \(1\le j\le N\). Their weighted contributions then sum to at least \(w\). Independence and the Weibull logarithmic tails yield
\[
 \liminf_{w\to\infty}w^{-p}\log\Pr(W>w)
 \ge -\frac1{\theta^pS_N^{p-1}}.
\]
Let \(N\to\infty\) to obtain the matching coefficient \(a_p=\theta^{-p}(1-c^q)^{p-1}\). This proof also shows why for \(p>1\) no finite number of past free intervals fully saturates the sharp coefficient.

**4. Transfer from variance to position.** Let \(Z\) be an independent standard normal. The Gaussian-mixture representation is \(X\stackrel d=\sqrt{v_0+2DW}\,Z\), with \(v_0=D/\kappa\). Set \(\beta=2p/(p+1)\) and \(h=x^{2/(p+1)}\). For fixed \(z>0\), the event \(W\ge zh\) gives the lower bound
\[
 \Pr(X>x)\ge\Pr(W\ge zh)\,
 \overline\Phi\!\left(\frac{x}{\sqrt{v_0+2Dzh}}\right).
\]
Gaussian tail asymptotics and the established \(W\)-tail limit give an exponent at least \(-[a_pz^p+(4Dz)^{-1}]x^\beta\). For the upper bound, partition \(\varepsilon h\le W\le Mh\) into a finite grid: on each cell, bound the environmental probability by the left endpoint's tail and the Gaussian survival by its right endpoint's variance. Handle \(W<\varepsilon h\) by a Gaussian bound and \(W>Mh\) by the \(W\)-tail bound. Take successively a fine grid, \(\varepsilon\downarrow0\), and \(M\uparrow\infty\); this yields the same variational minimum as an upper exponent. Minimizing
\[
 \inf_{z>0}\left(a_pz^p+\frac1{4Dz}\right)
 =\frac{(p+1)a_p^{1/(p+1)}}{(4Dp)^{p/(p+1)}}
\]
proves the positive-tail formula. Symmetry of the centered conditional Gaussian law gives the identical negative-tail result.

## Verification

The standalone `check_tail.py` is executable with Python, NumPy, and SciPy. It reproduces 86 deterministic algebraic, saddlepoint and finite-sample comparison assertions. Among them: a second numerical saddlepoint implementation is compared with the analytic coefficient; Rayleigh-distributed waiting times permit direct moment-generating-function asymptotics; and simulated stationary Gaussian mixtures are compared with an independently derived exact second-moment formula. The deterministic finite checks passed in the packaged version. Numerical tests corroborate, but do not certify, the asymptotic and uniqueness claims: the proof above supplies those conclusions.

## Relationship to prior work

D. Frydel, *Semi-Markovian switching in a fluctuating harmonic trap: An age-structured formulation* (arXiv:2607.05173v1; Phys. Rev. E 114, 024105, 2026) derives the general switching/age equations and exact Gaussian-mixture variance representation, with power-law waiting-time consequences. These foundational constructions are **not claimed as new**. The present result extracts the sharp Weibull-shape-dependent logarithmic **spatial** rate for strictly positive harmonic on-time; particularly, the \(p>1\) geometric-history factor is not supplied by the published algebraic-tail calculation.

Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap* (Phys. Rev. E 110, 024613, 2024), treats the fluctuating trap with Markovian switching, a different residence-time family. Eule and Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting* (2016; arXiv:1510.07876), treat generalized resetting, including the idealized instantaneous-return protocol; that does not encode finite harmonic contraction per on cycle. The mathematical theory of Weibull-like sums, including Asmussen and coauthors' work on light-tailed Weibull-like sums, already contains much of the underlying large-deviation calculus, which is accordingly **not proposed as a new abstract probabilistic theorem**. The contribution is the exact switching-physics coefficient and its sharp \(p=1\) history-dependence threshold, including the Gaussian spatial transfer.

## Limitations

The result concerns one position coordinate, constant diffusivity, a zero-stiffness off state, deterministic strictly positive harmonic on durations, and Weibull free durations. It determines the leading logarithmic tail exponent and coefficient, **not** multiplicative density prefactors, full stationary density, or a uniform limit as \(p\to1\), \(\tau\to0\), \(\kappa\to0\), or \(D\to0\). The source paper's broader arbitrary-residence family is not covered by the specialized sharp Weibull formula. Stronger abstract weighted-Weibull theorems could cover individual intermediate probability estimates, so priority for those estimates is not asserted independently.

## References

1. D. Frydel, *Semi-Markovian switching in a fluctuating harmonic trap: An age-structured formulation*, arXiv:2607.05173v1 (posted 2026-07-06); Phys. Rev. E **114**, 024105 (2026), doi:10.1103/7pxv-tg3b.
2. D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, Phys. Rev. E **110**, 024613 (2024), arXiv:2407.12213, doi:10.1103/PhysRevE.110.024613.
3. S. Eule and J. J. Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, arXiv:1510.07876 (2015); New J. Phys. **18**, 033006 (2016).
4. S. Asmussen et al., *Tail asymptotics of light-tailed Weibull-like sums* (2017), doi:10.19195/0208-4147.37.2.3. The use here is methodological context for known Weibull-sum large deviations, not attribution of the physical switching theorem.
