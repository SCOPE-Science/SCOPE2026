# Pareto renewal resetting of an expanding Thomas–Fermi condensate: algebraic tails and two aging limits

## Finding

Consider the Thomas–Fermi free expansion and complete resetting-to-initial-cloud protocol of Mesquita, Kulkarni, Majumdar and Sabhapandit (2026), but replace their exponentially distributed waiting times by independent Pareto renewal gaps with survival \(\mathbb P(W>a)=(1+a)^{-\delta}\), \(\delta>0\). Within that explicit hydrodynamic model the one-body density has a sharp three-regime phase diagram. The statements below concern the random reset environment and the hydrodynamic density, not a microscopic quantum trajectory theorem.

Let \(X_t\) be a random position sampled from the normalized one-body Thomas–Fermi density at observation time \(t\). Let \(E_t\) be the full cloud's expanding half-width at that time. Let \(c=\sqrt2\,\omega\) and \(x_0>0\), as defined below.

**Finite renewal mean, \(\delta>1\).** A unique stationary augmented renewal/expansion law exists. Its normalized one-body spatial density \(x_0^{-1}G_\delta(x/x_0)\) has the sharp algebraic tail
\[
G_\delta(z)\sim \frac{3(\delta-1)c^{\delta-1}}{2\delta(\delta+2)}|z|^{-\delta},\qquad |z|\to\infty.
\]
Consequently,
\[
\mathbb P(|X_\infty|>x_0 z)\sim\frac{3c^{\delta-1}}{\delta(\delta+2)}z^{1-\delta},\qquad
\mathbb P(E_\infty>x_0z)\sim c^{\delta-1}z^{1-\delta},
\]
and, for each real \(p>0\), \(\mathbb E|X_\infty|^p<\infty\) if and only if \(p<\delta-1\), including divergence at equality.

**Infinite renewal mean, \(0<\delta<1\).** There is no stationary probability law for the expanding cloud's one-body position or edge. If \(U\sim\operatorname{Beta}(1-\delta,\delta)\) is independent of \(V\) having density \(R(v)=\frac34(1-v^2)\mathbf1_{|v|<1}\), then
\[
\left(\frac{X_t}{x_0ct},\frac{E_t}{x_0ct}\right)\ \Longrightarrow\ (UV,U).
\]
The limiting signed-position density is supported on \((-1,1)\) and equals
\[
g_\delta(z)=\frac{3\sin(\pi\delta)}{4\pi}
\int_{|z|}^1 u^{-\delta-1}(1-u)^{\delta-1}
\left(1-\frac{z^2}{u^2}\right)du,\quad 0<|z|<1.
\]
It has **two different singularity/edge exponents**:
\[
g_\delta(z)\sim\frac{3\sin(\pi\delta)}{2\pi\delta(\delta+2)}|z|^{-\delta}
\quad(z\to0),\qquad
 g_\delta(1-\varepsilon)\sim
\frac{3\sin(\pi\delta)}{2\pi\delta(\delta+1)}\varepsilon^{\delta+1}
\quad(\varepsilon\downarrow0).
\]
Both asymptotics also hold by reflection at the negative edge. For \(p>0\), the rescaled moment has the explicit limit
\[
\lim_{t\to\infty}\mathbb E\left|\frac{X_t}{x_0ct}\right|^p=
\frac{\Gamma(p+1-\delta)}{\Gamma(1-\delta)\Gamma(p+1)}
\frac3{(p+1)(p+3)}.
\]

**Marginal infinite mean, \(\delta=1\).** Neither position nor edge has a stationary probability law; instead the *logarithmic* spatial scales are uniformly spread across the observation-time exponent:
\[
\left(\frac{\log(1+|X_t|/x_0)}{\log t},
\frac{\log(1+E_t/x_0)}{\log t}\right)
\ \Longrightarrow\ (H,H),\qquad H\sim\operatorname{Uniform}(0,1).
\]
The marginal conclusion is a joint limit (both coordinates have the same limiting exponent), not a claim that the physical position and edge are equal.

## Assumptions and scope

Fix \(x_0>0\), \(\omega>0\), and \(\delta>0\). Independently sample successive reset intervals \(W_1,W_2,\dots\) from the absolutely continuous law \(\mathbb P(W>a)=(1+a)^{-\delta}\), \(a\ge0\). The entire cloud is instantaneously restored at every reset to its deterministic initial inverted-parabolic Thomas–Fermi hydrodynamic profile. The intervals and the conditional spatial sampling variables are independent. The renewal clock starts at time zero.

The unreset cloud at age \(a\) has position-density \((x_0\lambda(a))^{-1}R(x/(x_0\lambda(a)))\), where \(R(v)=\frac34(1-v^2)\mathbf1_{|v|<1}\) and the monotonically increasing hydrodynamic scale \(\lambda(a)\) satisfies \(\lambda(0)=1\),
\[
\frac{d\lambda}{da}=\sqrt2\,\omega\sqrt{1-\lambda^{-1}},
\qquad
 a=\frac{\sqrt{\lambda(\lambda-1)}+\operatorname{arsinh}\sqrt{\lambda-1}}{\sqrt2\,\omega}.
\]
Set \(c=\sqrt2\,\omega\). Therefore \(1\le\lambda(a)\le1+ca\) and \(\lambda(a)/(ca)\to1\) as \(a\to\infty\). Writing \(S_n=\sum_{k=1}^nW_k\), \(N_t=\max\{n:S_n\le t\}\), and \(A_t=t-S_{N_t}\), the exact one-body density representation is
\[
X_t=x_0\lambda(A_t)V,\qquad E_t=x_0\lambda(A_t),
\]
with \(V\) independent of the clock and distributed by \(R\). Quantifiers cover all strictly positive \(x_0,\omega,\delta\) and all real \(p>0\) where a moment assertion is given. No microscopic particle-number limit, first-passage law or Bose-field fluctuation claim is asserted.

## Proof

**1. Expansion and exact renewal mixture.** Equations (39)–(42) of Mesquita et al. give the displayed hydrodynamic scale. Differentiating its implicit inverse yields \(d a/d\lambda=c^{-1}\sqrt{\lambda/(\lambda-1)}\), so \(\lambda\) grows from one, its velocity is bounded above by \(c\), and its speed tends to \(c\); hence the stated linear large-age asymptotic. The density at any physical observation time is exactly the mixture of scaled copies of \(R\) indexed by \(A_t\); this uses no independence assertion about different atoms of the cloud.

Let \(S(a)=(1+a)^{-\delta}\), \(f(a)=\delta(1+a)^{-\delta-1}\), and \(u_\delta(s)=\sum_{n\ge1}f^{*n}(s)\) be the renewal density for the strictly positive reset epochs. A direct last-reset decomposition gives a point mass \(\mathbb P(A_t=t)=S(t)\) and, for \(0<a<t\),
\[
\mathbb P(A_t\in da)=S(a)u_\delta(t-a)\,da.
\]
For \(\delta>1\), the mean renewal gap is \(\mu=\int_0^\infty S(a)da=(\delta-1)^{-1}\). The equilibrium age distribution therefore has pdf \(S(a)/\mu=(\delta-1)(1+a)^{-\delta}\), and the stationary cloud law is the pushforward by \(a\mapsto x_0\lambda(a)V\). In an augmented model retaining elapsed renewal age, the equilibrium renewal law is unique; convergence from the initial renewal law follows from nonlattice renewal theory. The spatial density is
\[
G_\delta(z)=\frac{3(\delta-1)}4\int_0^\infty(1+a)^{-\delta}
\frac{\bigl(1-z^2/\lambda(a)^2\bigr)_+}{\lambda(a)}\,da.
\]
For large \(|z|\), substitute \(a=|z|y/c\), use \(\lambda(a)/(ca)\to1\) uniformly on compact positive \(y\)-intervals and the global bound \(\lambda(a)\le1+ca\). Standard positive-integrand tail bounds (split \(y\in(0,1-\eta),[1-\eta,M],(M,\infty)\), then let \(\eta\downarrow0,M\uparrow\infty\)) justify dominated convergence. Its coefficient reduces to
\[
\frac{3(\delta-1)c^{\delta-1}}4
\int_1^\infty y^{-\delta-1}(1-y^{-2})dy
=\frac{3(\delta-1)c^{\delta-1}}{2\delta(\delta+2)}.
\]
Integration over both spatial tails yields the asserted exceedance constant; the edge tail follows directly from \(\mathbb P(A_\infty>a)=(1+a)^{1-\delta}\) and \(\lambda(a)\sim ca\). Finally \(\mathbb E|X_\infty|^p=x_0^p\mathbb E|V|^p\mathbb E\lambda(A_\infty)^p\), with \(\mathbb E|V|^p=3/[(p+1)(p+3)]\) and \(\mathbb E\lambda(A_\infty)^p<\infty\) exactly for \(p<\delta-1\). The equality case diverges logarithmically.

**2. Renewal-age asymptotics for \(0<\delta\le1\).** For clarity we justify the requisite renewal-density asymptotics, rather than assuming that ordinary finite-mean stationary renewal theory applies. The survival function is completely monotone,
\[
S(a)=\frac1{\Gamma(\delta)}\int_0^\infty\theta^{\delta-1}e^{-\theta}e^{-\theta a}d\theta.
\]
Consequently its Laplace transform \(\widehat S(s)\) is a Stieltjes function, \(s\widehat S(s)\) is complete Bernstein, and the reciprocal is Stieltjes. Since \(s\widehat S(s)\to1\) as \(s\to\infty\), the renewal-transform identity
\[
\widehat u_\delta(s)=\frac1{s\widehat S(s)}-1
\]
is a Stieltjes transform of a nonnegative measure, and \(u_\delta\) is completely monotone (in particular nonincreasing). These standard Stieltjes/Bernstein closure facts are documented by Schilling, Song and Vondraček. The scalar Laplace asymptotics are
\[
\widehat S(s)\sim\Gamma(1-\delta)s^{\delta-1}\quad(0<\delta<1),
\qquad\widehat S(s)\sim\log(1/s)\quad(\delta=1).
\]
The monotone-density form of Karamata's theorem yields
\[u_\delta(t)\sim\frac{\sin(\pi\delta)}\pi t^{\delta-1}\quad(0<\delta<1),
\qquad u_1(t)\sim\frac1{\log t}.
\]
For \(0<\delta<1\), apply the exact age-density identity to \(a=tv\) with fixed \(0<v<1\):
\[
tS(tv)u_\delta(t(1-v))\to
\frac{\sin(\pi\delta)}\pi v^{-\delta}(1-v)^{\delta-1}.
\]
The endpoints are controlled by positive renewal mass bounds and regular variation (equivalently the classical Dynkin–Lamperti age theorem); the no-reset atom \(S(t)\) vanishes. The limiting density integrates to one by Euler's reflection formula, so \(A_t/t\Rightarrow U\sim\mathrm{Beta}(1-\delta,\delta)\). In particular \(A_t\to\infty\) in probability.

At \(\delta=1\), for any fixed \(0<v<1\), the exact identity plus \(u_1(t-a)\sim1/\log t\) uniformly for \(0\le a\le t^v\) gives
\[
\mathbb P(A_t\le t^v)
=\int_0^{t^v}\frac{u_1(t-a)}{1+a}da
\sim\frac{\log(1+t^v)}{\log t}\to v.
\]
The no-reset atom is at \(a=t\), not in the event \(a\le t^v\). Hence \(\log(1+A_t)/\log t\Rightarrow\mathrm{Uniform}(0,1)\), and again \(A_t\to\infty\) in probability. Because \(\lambda(a)\to\infty\), both infinite-mean cases escape every compact set in position and edge: for the position, use \(\mathbb P(|V|\le \varepsilon)\to0\) as \(\varepsilon\downarrow0\). Tightness and any stationary limiting one-body law are therefore impossible.

**3. The aging condensate, \(0<\delta<1\).** Since \(\lambda(a)/ca\to1\) and \(\lambda(a)\le1+ca\), the continuous mapping theorem, independent \(V\), and boundedness give the joint convergence
\[
(X_t/(x_0ct),E_t/(x_0ct))\Rightarrow(UV,U).
\]
Conditioned on \(U=u\), the signed variable \(UV\) has density \(\frac3{4u}(1-z^2/u^2)_+\). Mixing against the exact beta density \(\frac{\sin(\pi\delta)}\pi u^{-\delta}(1-u)^{\delta-1}\) gives the displayed \(g_\delta\), which is nonnegative and integrates to one. For \(z\to0\), substitute \(u=|z|y\). Dominated convergence on \(y\ge1\) (the integrable singular at \(u=1\) is negligible after multiplication by \(|z|^\delta\)) leaves
\[
\int_1^\infty y^{-\delta-1}(1-y^{-2})dy=\frac2{\delta(\delta+2)},
\]
proving the central cusp. For \(z=1-\varepsilon\), put \(u=1-w\) and expand \(1-z^2/u^2=2(\varepsilon-w)+o(\varepsilon)\) uniformly at first order; then
\[
\int_0^\varepsilon 2(\varepsilon-w)w^{\delta-1}dw
=\frac{2\varepsilon^{\delta+1}}{\delta(\delta+1)},
\]
proving the edge law. The moment formula follows by multiplying \(\mathbb EU^p=\Gamma(p+1-\delta)/[\Gamma(1-\delta)\Gamma(p+1)]\) and \(\mathbb E|V|^p=3/[(p+1)(p+3)]\). Uniform boundedness of \(|X_t|/(x_0ct)\) for large \(t\) justifies convergence of every such positive moment.

**4. Marginal logarithmic spreading.** At \(\delta=1\), write
\[
\log(1+\lambda(A_t)|V|)=\log(1+A_t)+O_{\mathbb P}(1).
\]
Indeed for \(A_t\to\infty\), \(\lambda(A_t)/A_t\to c\), and \(\log|V|\) is a fixed almost-surely finite random variable; the addition of one only controls the origin. The same estimate holds without \(V\) for the edge. Divide by \(\log t\), apply the renewal-age limit, and obtain the joint diagonal uniform law.

## Verification

The analytical derivation is self-contained given the standard renewal monotone-density Tauberian theorem and elementary Stieltjes/Bernstein closure theorems stated above. The attached standalone `verify.py` (Python with SciPy; see `requirements.txt`) tests the exact derivative of the expansion inverse, the normalized beta clock, the spatial cusp and edge constants, and convergence toward the stationary algebraic-tail coefficient for multiple \(\delta\). Running it produced 43 finite checks passing. These tests are illustrative: the limits, existence, uniqueness and uniform laws are established by the preceding proof, not inferred from finite sample computations.

## Relationship to prior work

Mesquita, Kulkarni, Majumdar and Sabhapandit (arXiv:2609.37110v1, first public 29 September 2026) derive the Thomas–Fermi expanding profile and the Poisson-reset mixture; their Poisson fixed-rate stationary density has exponential tails and their conclusions explicitly motivate considering non-Poisson resets. The scale equation and initial Thomas–Fermi profile used here are theirs, not new. De Mauro, Biroli, Majumdar and Schehr (arXiv:2509.06658v2, 2026, Eqs. (36)–(42)) already prove the finite-mean renewal mixture for arbitrary unreset propagators and obtain power-law stationary tails for independent **Brownian** gas particles. Accordingly, neither the abstract renewal-mixture principle nor the mere existence of algebraic tails under finite-mean power-law resetting is claimed as new; their Gaussian diffusive propagator is distinct from the ballistically expanding compactly supported Thomas–Fermi profile, and their paper does not state the displayed exact Thomas–Fermi coefficients or the infinite-mean moving-profile central/edge asymptotics and marginal uniform log law. Meerson and Vilk (arXiv:2512.14345) study age-structured hydrodynamics for anomalous diffusive populations with Poisson resetting and do not present the Pareto-clock Thomas–Fermi trichotomy considered here. Classical renewal-reward, Dynkin–Lamperti arcsine laws, Karamata theory and Bernstein/Stieltjes facts are prior mathematical tools; the renewal-age limits themselves are not claimed as new general probability theorems.

The contribution assessed here is the explicitly calculated **interacting Thomas–Fermi spatial phase diagram**, including finite-mean stationary algebraic-tail amplitudes and moment cutoff, infinite-mean nonstationary beta-mixture density with *both* its divergent central cusp and vanishing moving-edge exponent, and the critical logarithmically uniform spatial spreading. Exact physical quantities and their compound singularities are not stated in the inspected primary work. Broader general renewal or expanding-profile theorems might encompass this specialization: no independence or exhaustive priority certification is asserted.

## Limitations

This is a hydrodynamic/Thomas–Fermi model calculation with complete resets to the same initial cloud. It assumes a fixed exact Pareto waiting-time family, one global renewal clock, linearly expanding scale at long ages, and independent spatial sampling from the normalized conditional one-body density. It does not address short-distance microscopic quantum correlations, finite-particle fluctuations, imperfect resetting, nonuniform reset selection, interactions outside the Thomas–Fermi regime, general slowly varying renewal tails, or convergence rates. The stationary law in the finite-mean case concerns the augmented renewal state; the position alone need not be Markov. Originality is evaluated to best knowledge, not independently certified.

## References

1. N. Mesquita, M. Kulkarni, S. N. Majumdar, S. Sabhapandit, *Weakly interacting Bose-Einstein condensate with stochastic resetting*, arXiv:2609.37110v1 (2026), https://arxiv.org/pdf/2609.37110 ; especially Eqs. (39)–(42), (45)–(53), and Conclusions/Outlook.
2. B. Meerson and O. Vilk, *Age-structured hydrodynamics of ensembles of anomalously diffusing particles with renewal resetting*, arXiv:2512.14345 (2025), https://arxiv.org/pdf/2512.14345 ; especially the introductory model definitions and Poisson-reset stationary analysis.
3. G. de Mauro, M. Biroli, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658v2 (2026), https://arxiv.org/pdf/2509.06658 ; especially Eqs. (36)–(42) and the Pareto-Brownian stationary-tail analysis.
4. R. Schilling, R. Song and Z. Vondraček, *Bernstein Functions: Theory and Applications*, 2nd ed., De Gruyter (2012), DOI:10.1515/9783110269338. Standard complete-Bernstein/Stieltjes closure results.
5. Classical renewal-reward and Dynkin–Lamperti age limit, and the monotone-density Karamata Tauberian theorem; used as established probabilistic results rather than claimed discoveries.
