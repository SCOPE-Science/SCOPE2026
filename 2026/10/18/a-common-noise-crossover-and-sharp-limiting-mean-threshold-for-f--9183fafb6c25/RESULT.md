# A common-noise crossover and sharp limiting mean threshold for fastest Brownian first passage

## Finding
For \(N\ge2\) Brownian searchers subjected to a shared Gaussian environment, write \(q_N=(1-\rho_N)\log N\), with \(\rho_N\) the pairwise increment correlation. The limiting law of the earliest arrival is controlled by this single parameter. If \(q_N\to a<\infty\), the first-arrival time converges in probability under a common Brownian coupling to
\[
T_a=\inf\{t>0:\ell+\sqrt{2D}B(t)-2\sqrt{Da t}\le0\}.
\]
If \(q_N\to\infty\), then \(4Dq_N T_N/\ell^2\to1\) in probability. For every finite \(a\ge0\), the mean **of the limiting variable** has a sharp transition:
\[
\mathbb E T_a<\infty\quad\Longleftrightarrow\quad a>\tfrac12.
\]
More precisely, the survival exponent is the ground-state Dirichlet eigenvalue \(\lambda(\sqrt{2a})\) of an Ornstein–Uhlenbeck generator on a half-line:
\[
\lim_{t\to\infty}\frac{\log\mathbb P(T_a>t)}{\log t}=-\lambda(\sqrt{2a}),
\qquad\lambda(1)=1.
\]
The mean criterion concerns this limiting law; convergence of finite-system means is neither asserted nor inferred.

## Assumptions and scope
Fix a starting distance \(\ell>0\) and diffusivity \(D>0\). For each \(N\ge2\), let \(\rho_N\in[0,1]\) and \(\eta_N=1-\rho_N\). On one probability space take independent standard one-dimensional Brownian motions \(B_0,B_1,\ldots\). The \(i\)-th particle follows
\[
X_i^{(N)}(t)=\ell+\sqrt{2D}\left(\sqrt{\rho_N}\,B_0(t)+\sqrt{\eta_N}\,B_i(t)\right),\qquad t\ge0,
\]
and \(T_N=\inf\{t>0:\min_{1\le i\le N}X_i^{(N)}(t)\le0\}\). The target is the origin, and there is no drift, resetting, killing before target arrival, or interaction other than the common noise. The pairwise correlation of distinct particle increments is exactly \(\rho_N\), while each marginal diffusivity is \(D\). The underlying Brownian coupling is common for all \(N\).

For the Brownian scaling statement when \(q_N\to\infty\), the convergence is in probability for this coupling as well; for the proof it suffices to establish convergence in distribution to a constant.

## Proof
**Lemma 1 (uniform Gaussian-path extreme).** For \(N\ge2\) put
\[
Y_N(t)=\frac{\max_{1\le i\le N}[-B_i(t)]}{\sqrt{2\log N}},\quad t\ge0.
\]
Then for each fixed \(R<\infty\), \(\sup_{0\le t\le R}|Y_N(t)-\sqrt t|\to0\) in probability. At each fixed \(t>0\), normal tail bounds give convergence to \(\sqrt t\). To upgrade it, fix a mesh of spacing \(\delta\). Reflection and Gaussian tail bounds show
\[
\mathbb P\left(\max_i\sup_{0\le u\le\delta}|B_i(u)|>\varepsilon\sqrt{2\log N}\right)
\le 4N\exp\left[-\frac{\varepsilon^2\log N}{\delta}\right]
\]
(up to an inessential constant determined by the Gaussian tail convention). For \(\delta<\varepsilon^2\), the right side tends to zero. A union bound across finitely many mesh intervals controls uniform continuity of \(Y_N\) at the needed normalized scale. Pointwise convergence at mesh points and uniform continuity of \(\sqrt t\) finish the proof, including the interval near zero. More concretely, the displayed reflection bound follows from \(\mathbb P(\sup_{u\le\delta}|B(u)|>z)\le4e^{-z^2/(2\delta)}\).

**Finite-window crossover.** The minimum position is the exact continuous process
\[
M_N(t)=\min_i X_i^{(N)}(t)
=\ell+\sqrt{2D\rho_N}\,B_0(t)-2\sqrt{Dq_N}\,Y_N(t).
\]
If \(q_N\to a<\infty\), then \(\rho_N=1-q_N/\log N\to1\). Lemma 1 and local boundedness of Brownian paths imply uniform convergence in probability on each compact time interval to \(m_a(t)=\ell+\sqrt{2D}B_0(t)-2\sqrt{Da t}\). The limit starts strictly positive and hits zero almost surely since \(T_a\) is no larger than the ordinary Brownian hitting time of the origin. At the first hit, which lies strictly after zero, Brownian motion makes arbitrarily small downward excursions relative to any locally differentiable deterministic boundary; therefore \(m_a\) becomes strictly negative immediately after its first zero. This is the standard regularity of Brownian motion at a continuous differentiable barrier at positive time, obtainable from the strong Markov property and the local law of the iterated logarithm. Consequently the first-zero functional is almost surely continuous at \(m_a\) under uniform-on-compact perturbations, proving \(T_N\to T_a\) in probability.

**Logarithmic acceleration regime.** Assume \(q_N\to\infty\) and let \(h_N=\ell^2/(4Dq_N)\). Brownian scaling applied to every \(B_i\) gives, on any fixed compact \(u\)-interval, equality in distribution between
\[
\frac{M_N(h_Nu)}\ell
\quad\text{and}\quad
1+\sqrt{\frac{2D\rho_Nh_N}{\ell^2}}\,\widetilde B_0(u)
-Y_N^{*}(u),
\]
where \(Y_N^{*}\) is built from independent Brownian motions as in Lemma 1; the last term is simply \(-Y_N^{*}(u)\), with its continuous value zero at \(u=0\). Indeed, the coefficient of \(Y_N^*(u)\) after scaling is exactly one since \(2\sqrt{Dq_Nh_N}/\ell=1\). The common-noise coefficient is \(O(q_N^{-1/2})\), because \(\rho_N\le1\). Lemma 1 shows that the right-hand side converges uniformly in probability to \(1-\sqrt u\). This deterministic curve crosses zero once, strictly, at \(u=1\). The first-crossing map therefore gives \(T_N/h_N\to1\) in distribution, hence in probability.

**Sharp first-moment threshold for the limiting law.** Fix finite \(a\ge0\), and set \(b=\sqrt{2a}\) and \(c=\ell/\sqrt{2D}\). The survival event \(\{T_a>t\}\) is equivalent to
\[
B_0(r)> b\sqrt r-c\qquad\text{for every }0<r\le t.
\]
Under logarithmic time \(r=e^s\), the normalized process \(Z_s=e^{-s/2}B_0(e^s)\) is a two-sided stationary Ornstein–Uhlenbeck process with generator
\[
Lf=\tfrac12 f''-\tfrac x2 f',
\]
whose invariant law is standard Gaussian. Survival through \(t=e^S\) corresponds to staying above the moving boundary \(b-ce^{-s/2}\) for \(s\le S\). Let \(\lambda(v)\) be the principal eigenvalue of \(-L\) on \((v,\infty)\), with an absorbing Dirichlet boundary at \(v\). This operator has discrete spectrum in Gaussian \(L^2\), a strictly positive ground state, and \(\lambda(v)\) is continuous and strictly increasing in \(v\) by one-dimensional Dirichlet domain monotonicity and the variational principle.

For every \(\varepsilon>0\), at all sufficiently large \(s\) the moving boundary lies between \(b-\varepsilon\) and \(b\). Consequently the survival probability is bounded above by the stationary killed-OU survival above \(b-\varepsilon\), which is at most a constant times \(e^{-\lambda(b-\varepsilon)S}\) by the spectral theorem. For a lower bound, fix a finite \(s_0\) and a compact interval strictly inside \((b,\infty)\) that the OU process can enter with positive probability without violating the moving barrier before \(s_0\). Thereafter remaining above the fixed barrier \(b\) implies survival of the moving barrier. Positivity of the killed semigroup and its ground-state spectral projection supply \(\mathbb P(T_a>e^S)\ge C e^{-\lambda(b)(S-s_0)}\) for all large \(S\). The bounds, followed by \(\varepsilon\downarrow0\), prove the claimed logarithmic tail exponent.

At \(b=1\), the polynomial \(f(x)=x^2-1\) is positive on \((1,\infty)\), zero at \(1\), belongs to Gaussian \(L^2\), and satisfies \(Lf=-f\). It is therefore the positive ground state, so \(\lambda(1)=1\). Since \(\lambda\) increases strictly, \(b>1\) yields a survival upper bound \(Ct^{-1-\delta}\) for some \(\delta>0\), implying \(\mathbb ET_a<\infty\). For \(b\le1\), the lower bound with \(\lambda(b)\le1\) implies \(\int^\infty\mathbb P(T_a>t)\,dt=\infty\). The exact boundary is \(a=b^2/2=1/2\). At \(a=0\), the limiting law is ordinary Brownian first passage, with
\[
\mathbb P(T_0\le t)=\operatorname{erfc}\left(\frac\ell{\sqrt{4Dt}}\right).
\]
This completes the proof.

## Verification
The included `verify.py` provides direct finite-system Gaussian-mixture quadrature for fixed-time positivity, independent Gaussian-extrema tail checks, simulated Brownian path envelopes at several sizes, the ordinary Brownian first-passage identity at \(a=0\), and an independent finite-difference calculation of killed Ornstein–Uhlenbeck eigenvalues. These checks are finite and numerical; they do not establish either functional convergence or the spectral tail theorem. The proof above supplies the infinite statements. To reproduce: `python verify.py` (requires NumPy and SciPy).

## Relationship to prior work
Ruicheng Bao's 2026 study develops extreme first-passage theory for interacting overdamped particles driven by *independent* Brownian motions, and emphasizes the familiar \(1/\log N\) search speed under bounded forces. The present model introduces a *shared* Brownian environmental component, lets its relative variance depend on \(N\), and identifies a nondegenerate limiting first-passage law when independent variance is \(O(1/\log N)\). Hass, Corwin and Corwin study correlated first passage in space-time random environments with KPZ fluctuations, a different source and scaling of correlations. Classical Brownian square-root barriers, Gaussian extremes and killed Ornstein–Uhlenbeck theory are used, not claimed as new. The distinctive conclusion is the joint correlation crossover and its exact critical limiting mean threshold.

## Limitations
All particles are driftless one-dimensional Brownian motions with an equicorrelated global Gaussian environment and a common starting distance. The asymptotics do not cover general pairwise interactions, spatially varying noise correlations, heterogeneous diffusivities, or non-Brownian searchers. The limiting mean threshold says nothing by itself about convergence or finiteness of finite-\(N\) mean hitting times. The logarithmic survival exponent is a tail statement, not a full density expansion. Novelty against all unlocated literature is not certified, and the scientific review is not independent.

## References
1. R. Bao, *Extreme First-Passage Time of Many Interacting Particles*, arXiv:2607.22528v1 (first public 2026-07-24), https://arxiv.org/html/2607.22528v1.
2. J. Hass, I. Corwin, and E. Corwin, *First Passage Time for Many Particle Diffusion in Space-Time Random Environments*, arXiv:2308.01267 (2023), https://arxiv.org/abs/2308.01267.
3. A. Metzler, *On the first passage problem for correlated Brownian motion*, Statistics & Probability Letters (2010), https://doi.org/10.1016/j.spl.2009.11.001. (Related finite-dimensional treatment; full text not verified in this investigation.)
4. T. Guillaume, *Survival Probabilities for Correlated Drifted Brownian Motions via Exit from Simplicial Cones* (2026). (Related finite-dimensional cone-survival setting; direct coverage of the present many-body limit not established.)
