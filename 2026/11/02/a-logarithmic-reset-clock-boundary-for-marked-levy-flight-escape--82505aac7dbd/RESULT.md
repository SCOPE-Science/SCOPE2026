# A logarithmic reset-clock boundary for marked Levy-flight escape

## Finding

A symmetric strictly \(\alpha\)-stable flight escaping a growing interval has a reset-clock universality transition at the **unit tail exponent**. Finite-mean renewal clocks, and even the critical infinite-mean Lomax clock, give a rate-independent exponential exit time and independent exit-side mark. Subcritical Lomax clocks instead retain the full unreset first-exit distribution in an explicit marked Laplace transform. This supplies the entire scaled first-exit law, not just its mean.

Let \(0<\alpha<2\), \(\sigma>0\), and \(-1<\Lambda<1\). The unreset flight \(Y\), started at \(\Lambda L\), has stationary increments with
\[
\mathbb E[e^{i\xi(Y_t-Y_0)}]=e^{-t\sigma^\alpha|\xi|^\alpha}.
\]
Let \(T\) be the first exit time from \((-1,1)\) of the same flight started at \(\Lambda\), and let \(J\in\{+,-\}\) be its exit side. Put
\[
K=L^\alpha,\qquad \eta_\alpha=\frac{\Gamma(\alpha)\sin(\pi\alpha/2)}{\pi},\qquad
k_\pm=\eta_\alpha\sigma^\alpha(1\mp\Lambda)^{-\alpha},\quad k=k_++k_-.
\]
Here \(k_+\) is the jump intensity across the right boundary in the scaled rare-escape limit, and \(k_-\) is the analogous left intensity.

Reset the flight to \(\Lambda L\) at independent, identically distributed positive waiting times \(R\), restarting both the clock and the flight independently after each unsuccessful attempt. Denote the completed first-exit time by \(\mathcal T_L\), and its exit side by \(J_L\).

**Finite-mean clocks.** For *every* law of \(R\) with \(0<\mathbb ER<\infty\), without a variance, density, or memorylessness assumption, the marked weak limit is
\[
\left(\frac{\mathcal T_L}{K},J_L\right)\Longrightarrow(E,J_\infty),
\quad E\sim\operatorname{Exp}(k),\quad
\mathbb P(J_\infty=\pm)=\frac{k_\pm}{k},\quad E\perp J_\infty.
\]
Also \(\mathbb E\mathcal T_L/K\to1/k\). In particular, deterministic resets and power-law resets of finite mean have the **same** leading law as Poisson resets.

**The infinite-mean critical clock.** For \(\mathbb P(R>t)=(1+t)^{-1}\), \(t\ge0\), the same marked limit and same scaled-mean limit hold, even though \(\mathbb ER=\infty\). The successful-cycle probability and expected cycle duration obey
\[
\mathbb P(T_L<R)\sim\frac{k\log K}{K},\qquad
\mathbb E\min(T_L,R)\sim\log K,
\]
where \(T_L\stackrel d=KT\) is one unreset attempt. Their logarithms cancel in the exit clock.

**The infinite-mean subcritical clocks.** If \(\mathbb P(R>t)=(1+t)^{-\delta}\) for \(0<\delta<1\), define \(m_\delta=\mathbb E[T^{-\delta}]\in(0,\infty)\). The marked limiting law is characterized, for every \(s\ge0\), by
\[
\boxed{\lim_{L\to\infty}\mathbb E\left[e^{-s\mathcal T_L/K}\mathbf 1_{\{J_L=\pm\}}\right]
=\frac{\mathbb E[e^{-sT}T^{-\delta}\mathbf1_{\{J=\pm\}}]}{m_\delta+\delta\int_0^\infty(1-e^{-su})u^{-1-\delta}\mathbb P(T>u)\,du}.}
\]
Consequently, \(\mathbb P(J_L=\pm)\to\mathbb E[T^{-\delta}\mathbf1_{\{J=\pm\}}]/m_\delta\), and
\[
\boxed{\lim_{L\to\infty}\frac{\mathbb E\mathcal T_L}{K}
=\frac{\mathbb E[T^{1-\delta}]}{(1-\delta)\mathbb E[T^{-\delta}]}.}
\]
The subcritical limit depends on the entire unreset exit law, rather than only on \(k_\pm\). Its mean coefficient tends to \(\mathbb ET\) as \(\delta\downarrow0\) and to \(1/k\) as \(\delta\uparrow1\). For the centered Cauchy flight \((\alpha,\Lambda)=(1,0)\), these endpoint coefficients are, respectively, \(1/\sigma\) and \(\pi/(2\sigma)\), so the subcritical and critical clock regimes cannot be treated as one distribution-free exponential formula.

## Assumptions and scope

The interval is open and is left upon the *first* entry into its complement, including an overshoot. The Lévy process is symmetric with characteristic exponent exactly \(\sigma^\alpha|\xi|^\alpha\); the Brownian endpoint \(\alpha=2\) is excluded. The start and reset location scale proportionally as \(\Lambda L\), with fixed \(\Lambda\) strictly between the endpoints. Reset times are positive and finite almost surely, i.i.d. across cycles, independent of all flight paths; the first cycle uses the same law. A reset after absorption is immaterial. The law of \(R\) does not depend on \(L\). The two Lomax regimes use the stated unit scale; the critical and subcritical coefficients explicitly reflect this convention. The finite-mean statement permits atomic or heavy-tailed reset times. The result concerns \(L\to\infty\) for fixed \(\alpha,\sigma,\Lambda\) and a fixed clock law; no uniform parameter limit is claimed.

## Proof

**1. Small-time marked exit.** Self-similarity gives \((T_L,J)\stackrel d=(KT,J)\). The Lévy measure corresponding to the characteristic exponent is
\[
\nu(dz)=\alpha\eta_\alpha\sigma^\alpha|z|^{-1-\alpha}\,dz.
\]
Its mass above \(1-\Lambda\) equals \(k_+\), and its mass below \(-1-\Lambda\) equals \(k_-\). The standard one-large-jump short-time exit estimate for a Lévy process, with the exit overshoot marked by the boundary side, therefore yields
\[
F_\pm(u):=\mathbb P(T\le u,J=\pm)=k_\pm u+o(u),\qquad u\downarrow0.
\]
This fact follows from the Lévy–Itô large-jump decomposition; a precise first-exit/overshoot small-time theorem is provided by Figueroa-López and Tankov (2014), and the unmarked version is used explicitly by Żbik and Palmowski (2026). Because \(F_\pm\) are distribution functions, there is a finite \(C\) such that \(F_\pm(u)\le Cu\) for *all* \(u>0\): use the asymptotic near zero and \(F_\pm(u)\le1\) away from zero. Thus \(\mathbb ET^{-\delta}<\infty\) for \(0<\delta<1\). Killed stable motion on a bounded interval has finite positive exit-time moments of all orders: jumps larger than two in absolute magnitude occur at a positive finite Poisson rate and force exit regardless of the pre-jump position. Thus the exit time is stochastically bounded by a positive-rate exponential clock, so every positive moment displayed below is finite.

**2. Exact cycle identity.** In each independent attempt, let \(T_i\stackrel d=KT\) be its unreset exit time, \(J_i\stackrel d=J\) its side, and \(R_i\stackrel d=R\) its reset time. The attempt succeeds if \(T_i<R_i\). For \(s\ge0\), define
\[
a_{\pm,K}(s)=\mathbb E[e^{-sT}\mathbf1_{\{KT<R,J=\pm\}}],\qquad
b_K(s)=\mathbb E[e^{-sR/K}\mathbf1_{\{R<KT\}}].
\]
Summing the geometric sequence of failed independent cycles gives the *exact* marked transform
\[
\mathbb E[e^{-s\mathcal T_L/K}\mathbf1_{\{J_L=\pm\}}]
=\frac{a_{\pm,K}(s)}{1-b_K(s)}.
\]
The exact renewal-reward mean identity is
\[
\mathbb E\mathcal T_L=\frac{\mathbb E\min(KT,R)}{\mathbb P(KT<R)}.
\]
Since both \(KT\) and \(R\) are a.s. finite and the per-cycle success probability is positive, these expressions are well defined and absorption occurs almost surely. All subsequent limits are obtained from these identities, not from a Gaussian approximation or finite simulations.

**3. Finite-mean resetting.** Conditional on \(R\),
\[
K\,\mathbb P(KT<R,J=\pm)=\mathbb E[K F_\pm(R/K)]\longrightarrow k_\pm\mathbb ER,
\]
by dominated convergence using \(K F_\pm(R/K)\le CR\). The same limit holds with \(e^{-sT}\) inside, because, conditional on success, \(T<R/K\) and its exponential factor lies between \(e^{-sR/K}\) and one. Also
\[
K(1-b_K(s))=K\mathbb P(KT<R)
+\mathbb E[K(1-e^{-sR/K})\mathbf1_{\{R<KT\}}]
\longrightarrow(k+s)\mathbb ER.
\]
Here \(K(1-e^{-sR/K})\le sR\), so dominated convergence applies. Taking the ratio gives \(k_\pm/(k+s)\), exactly the transform of an independent \(\operatorname{Exp}(k)\) clock and Bernoulli exit mark. In the mean identity, \(\mathbb E\min(KT,R)\to\mathbb ER\), yielding \(\mathbb E\mathcal T_L/K\to1/k\).

**4. Subcritical Lomax resetting.** Put \(\mathbb P(R>t)=(1+t)^{-\delta}\), \(0<\delta<1\). Since \(m_\delta\) is finite, dominated convergence gives
\[
K^\delta a_{\pm,K}(s)
=\mathbb E[e^{-sT}K^\delta(1+KT)^{-\delta}\mathbf1_{\{J=\pm\}}]
\longrightarrow\mathbb E[e^{-sT}T^{-\delta}\mathbf1_{\{J=\pm\}}].
\]
Decomposing the failed-cycle denominator, changing variables \(R=Ku\) in its reset-time integral, and applying dominated convergence yields
\[
K^\delta[1-b_K(s)]\longrightarrow
m_\delta+\delta\int_0^\infty(1-e^{-su})u^{-1-\delta}\mathbb P(T>u)\,du.
\]
A dominating integrand is a constant multiple of \(\min(su,1)u^{-1-\delta}\), integrable at zero precisely because \(\delta<1\), and integrable at infinity because \(\delta>0\). The ratio proves the marked transform. Further,
\[
\mathbb E\min(KT,R)
=\mathbb E\frac{(1+KT)^{1-\delta}-1}{1-\delta}
\sim\frac{K^{1-\delta}}{1-\delta}\mathbb ET^{1-\delta},
\]
whereas \(\mathbb P(KT<R)\sim K^{-\delta}m_\delta\), proving the mean formula. The two \(\delta\)-endpoint limits follow from dominated convergence at zero and the marked small-time asymptotic at one. In particular \((1-\delta)\mathbb ET^{-\delta}\to k\) as \(\delta\uparrow1\).

**5. The logarithmic critical clock.** For \(\mathbb P(R>t)=(1+t)^{-1}\), the small-time expansion \(F_\pm(u)=k_\pm u+o(u)\), integrated against \((1+Ku)^{-1}\), implies
\[
\mathbb P(KT<R,J=\pm)\sim\frac{k_\pm\log K}{K}.
\]
Indeed, the logarithm comes solely from the range \(1/K\ll u\ll1\); the contributions from either endpoint are only \(O(K^{-1})\) after fixing a small upper cutoff, and the \(o(u)\) term is \(o(\log K/K)\). Inserting \(e^{-sT}\) changes no leading coefficient, since the successful-event logarithm also comes from \(u\downarrow0\). For the failed-cycle time term,
\[
\frac{K}{\log K}\mathbb E[(1-e^{-sR/K})\mathbf1_{\{R<KT\}}]\longrightarrow s.
\]
To see this, integrate the density \((1+R)^{-2}\) and split at \(R=1\), \(R=K\varepsilon\), and \(R=K\). On \(1\ll R\ll K\), \(1-e^{-sR/K}\sim sR/K\) and \(\mathbb P(T>R/K)\to1\), producing \(s\log K/K\); the remaining ranges contribute at most \(o(\log K/K)\) by first fixing \(\varepsilon\) and then letting it decrease. Hence the marked transform tends again to \(k_\pm/(k+s)\). Finally
\[
\mathbb E\min(KT,R)=\mathbb E\log(1+KT)\sim\log K,
\]
where \(\mathbb E|\log T|<\infty\) follows from the small-time estimate and the finite positive moments. The mean limit is \(1/k\). This proves the critical boundary, including its logarithmic cancellation.

**6. Nontriviality of the boundary.** For the centered Cauchy case the known unreset exit-time mean equals \(1/\sigma\); the marked jump intensity gives \(k=2\sigma/\pi\). Thus the subcritical mean coefficient approaches \(1/\sigma\) as \(\delta\downarrow0\), whereas the critical/exponential coefficient is \(\pi/(2\sigma)\). Continuity of the subcritical mean in \(\delta\) shows that, for sufficiently small positive \(\delta\), the limit cannot be the same \(\operatorname{Exp}(k)\) law. This establishes a genuine clock-tail transition, not merely an alternate expression for the same distribution.

## Verification

The key analytic checks are the Lévy-tail constant \(\eta_\alpha\), its centered relation \(1/(2\eta_\alpha)=\Gamma(1-\alpha)\cos(\pi\alpha/2)\) (continuous interpretation at \(\alpha=1\)), the exact geometric-cycle transform, and the logarithmic order of both critical-cycle terms. The last three proof steps establish the limits using dominated convergence and explicit Pareto integrals; they do not require an external simulation. The Cauchy check gives \(k=2\sigma/\pi\) and reconciles the finite-mean limit with the Poisson result's published coefficient \(\pi/(2\sigma)\). No numerical calculation is invoked as proof of a limit. Distinct atomic, Pareto and continuous reset laws are all covered by the stated assumptions where applicable.

## Relationship to prior work

Żbik and Palmowski (arXiv:2610.20410, first public 2026-10-14) give the Poisson-reset **mean** first-exit asymptotic for stable Lévy flights; the centered coefficient agrees with the present finite-mean result. Their paper does not assert the marked distributional limit or the critical and subcritical Pareto-clock classification. Żbik and Dybiec (arXiv:2311.16014) examine Lévy-flight/Levy-walk escape and optimization, but not this large-interval marked law over reset-clock tail classes. Figueroa-López and Tankov's small-time exit/overshoot theorem supplies the already known one-large-jump premise: that premise is not claimed as new. Classical renewal-restart identities and rare-event exponential-limit methods are likewise prior tools. Imkeller and Pavlyukevich establish exponential exit in a different small-noise confining-drift model; their potential-driven system neither gives the Lomax critical law nor the explicit marked formula here. The contribution evaluated is the specific clock-tail phase boundary and complete joint transform with the explicit stable-flight coefficients, not the generic restart or large-jump lemmas.

## Limitations

The subcritical law is expressed through unreset exit-time moments and a one-dimensional integral, not an elementary closed density. There is no claim of a rate of convergence, of uniformity as \(\Lambda\) approaches an endpoint or as \(\alpha\) approaches two, nor of universality under state-dependent, correlated, or resetting-position-changing clocks. The finite-mean conclusion requires a fixed clock law independent of interval size. Broader regenerative rare-event theory may yield parts of the exponential branch; the critical and subcritical comparisons are assessed only against the sources explicitly inspected, not independently priority-certified.

## References

1. B. Żbik and Z. Palmowski, *Asymptotic behaviour for escaping an interval by Lévy flights under stochastic resetting*, arXiv:2610.20410 (first public 2026-10-14), https://arxiv.org/abs/2610.20410.
2. B. Żbik and B. Dybiec, *Lévy flights and Lévy walks under stochastic resetting*, arXiv:2311.16014 (2023), https://arxiv.org/abs/2311.16014.
3. J. E. Figueroa-López and P. Tankov, *Small-time asymptotics of stopped Lévy bridges and simulation schemes with controlled bias*, Bernoulli 20 (2014), 1126–1164, arXiv:1203.2355, https://arxiv.org/abs/1203.2355.
4. M. R. Evans, S. N. Majumdar and G. Schehr, *Stochastic Resetting and Applications*, J. Phys. A 53 (2020), 193001, arXiv:1910.07993, https://arxiv.org/abs/1910.07993.
5. P. Imkeller and I. Pavlyukevich, *First exit times of solutions of non-linear stochastic differential equations driven by symmetric Lévy processes with alpha-stable components*, arXiv:math/0409246 (2004), https://arxiv.org/abs/math/0409246.
6. R. Zweimüller, *Hitting Times and Positions in Rare Events*, Annales Henri Lebesgue 5 (2022), 1361–1415, https://doi.org/10.5802/ahl.154.
