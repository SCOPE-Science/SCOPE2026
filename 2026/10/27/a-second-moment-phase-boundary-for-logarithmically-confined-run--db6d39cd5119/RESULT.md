# A second-moment phase boundary for logarithmically confined run-and-tumble searches

## Finding
Consider the absorbing-origin first-passage time \(T\) of a one-dimensional persistent particle
\[
\dot X_t=-\frac{1}{1+X_t}+v\sigma_t,\qquad \sigma_t\in\{-1,+1\},
\]
where \(0<v<1\), the sign flips at independent rate \(\gamma>0\), and \(X_0=x>0\). Put \(D_{\mathrm{eff}}=v^2/(2\gamma)\) and \(x_*=v^{-1}-1\). Either deterministic initial sign, or any independent mixture of the two signs, is allowed.

**Theorem.** If \(0<x<x_*\), all moments of \(T\) are finite. The same conclusion holds at \(x=x_*\). If \(x>x_*\), then
\[
\mathbb E T<\infty\quad\Longleftrightarrow\quad D_{\mathrm{eff}}<1,
\qquad
\mathbb E T^2<\infty\quad\Longleftrightarrow\quad D_{\mathrm{eff}}<\frac13.
\]
In particular, the nonempty interval \(\frac13\le D_{\mathrm{eff}}<1\), equivalently \(v^2/2<\gamma\le3v^2/2\), has finite mean but infinite variance for every \(x>x_*\).

When \(D_{\mathrm{eff}}<1/3\), and the initial sign is equally likely, the large-starting-distance asymptotic is
\[
\lim_{x\to\infty}\frac{\mathbb E_x T^2}{x^4}
=\frac{1}{4(1-D_{\mathrm{eff}})(1-3D_{\mathrm{eff}})}.
\]
The same coefficient holds for either deterministic initial sign. The leading \(x^2\) coefficient of \(\mathbb E_xT\), previously known, is \(1/[2(1-D_{\mathrm{eff}})]\).

## Assumptions and scope
The velocity state is a symmetric two-state continuous-time Markov chain, independent of position, with generator \(\gamma[g(-\sigma)-g(\sigma)]\). There is no translational Brownian noise or resetting. The trajectory solves the ordinary differential equation between tumbles and is killed on first hitting zero. The potential is exactly \(V(x)=\log(1+x)\) on the positive half-line, with unit amplitude and length scale. The only free parameters are \(v\in(0,1)\) and \(\gamma>0\). The asserted moment equivalences apply to every fixed starting point strictly beyond the repelling positive-velocity turning point \(x_*\).

## Proof
**The protected interval.** For \(x<x_*\), both possible velocities are negative, and the maximal velocity along the subsequent decreasing trajectory is at most \(v-(1+x)^{-1}<0\). Thus \(T\le x/[(1+x)^{-1}-v]\). At \(x=x_*\), a positive-sign particle waits an exponential time to flip; after an initial negative-sign stretch it enters \((0,x_*)\), which it can never leave. On the compact state space \([0,x_*]\times\{\pm1\}\), each block of length \(1+x_*/v\) has a uniformly positive probability of hitting zero (force a sign change within the first unit if needed, then maintain negative sign for \(x_*/v\)); hence \(T\) has an exponential tail from the turning point.

**The first-moment input.** Guéneau, Majumdar and Schehr derive the exact mean for this log-potential model. On \((x_*,\infty)\), their integral solution gives \(\mathbb E_xT<\infty\) exactly for \(D_{\mathrm{eff}}<1\), and for the average \(u=(u_++u_-)/2\) of sign-conditioned means,
\[
u(x)=\frac{x^2}{2(1-D_{\mathrm{eff}})}+O(x),\qquad
u'(x)=\frac{x}{1-D_{\mathrm{eff}}}+O(1).
\]
The derivative estimate also follows directly from their first-order integrating-factor equation. The backward equations give \(u_\pm(x)=u(x)+O(x)\), so for \(D_{\mathrm{eff}}<1\) there is a finite constant \(C\) with \(u_\pm(x)\le C(1+x)^2\) for every \(x\ge x_*\). The established first-moment divergence already implies second-moment divergence for \(D_{\mathrm{eff}}\ge1\).

**Finite second moment below the new boundary.** Let \(y=1+x\), \(\mathcal L=(v\sigma-y^{-1})\partial_y+\gamma(\mathrm{flip}-I)\), and define
\[
H_2(y,\sigma)=y^2+\frac v\gamma\sigma y,\qquad
H_4(y,\sigma)=y^4+\frac{2v}{\gamma}\sigma y^3.
\]
Exact generator calculations yield
\[
\mathcal LH_2=-2(1-D_{\mathrm{eff}})-\frac{v\sigma}{\gamma y},\qquad
\mathcal LH_4=-4(1-3D_{\mathrm{eff}})y^2-\frac{6v}{\gamma}\sigma y.
\]
On \(x\ge x_*\) we have \(y\ge1/v\), hence \(\mathcal LH_2\le-2+4D_{\mathrm{eff}}<0\) whenever \(D_{\mathrm{eff}}<1/3\). The negative quadratic term of \(\mathcal LH_4\) dominates for large \(y\); a sufficiently large positive multiple of \(H_2\) makes a positive combination \(U=A H_4+B H_2+C_0\) nonnegative and ensures \(\mathcal LU\le-2u_\sigma(x)\) for all \(x\ge x_*\). Moreover \(U=O(y^4)\). For the exit time \(\tau_L\) from \((x_*,L)\), the backward potential identity and Dynkin's formula imply
\[
\mathbb E_{x,\sigma}\tau_L^2=2\mathbb E_{x,\sigma}
\int_0^{\tau_L}\mathbb E_{X_s,\sigma_s}\tau_L\,ds
\le2\mathbb E\int_0^{\tau_L}u_{\sigma_s}(X_s)\,ds\le U(x,\sigma).
\]
The finite mean of \(T\) implies \(\tau_L\uparrow\tau_{x_*}\) almost surely as \(L\uparrow\infty\). Monotone convergence gives \(\mathbb E\tau_{x_*}^2\le U(x,\sigma)\). At \(x_*\) the remaining passage time has uniformly bounded second moment for either sign, as shown above. Strong Markov and Cauchy--Schwarz therefore yield \(\mathbb E_{x,\sigma}T^2<\infty\), bounded by a constant times \((1+x)^4\).

**Necessity, including the critical point.** Assume \(1/3\le D_{\mathrm{eff}}<1\) and that a second moment is finite for one starting point \(x>x_*\). Positive-probability communication before absorption along uninterrupted runs and flips propagates finiteness to both signs and all finite \(x>x_*\). Define \(m(x)=(\mathbb E_{x,+}T^2+\mathbb E_{x,-}T^2)/2\) and \(f(x)=-(1+x)^{-1}\). Eliminating the sign difference from the two second-moment backward equations gives
\[
(v^2-f^2)m''+2f(\gamma-f')m'
=2(f'-2\gamma)u+4fu'+4.
\]
The right-hand side is \(-4\gamma c x^2+O(x)\), with \(c=[2(1-D_{\mathrm{eff}})]^{-1}>0\). Set \(w=m'\). Dividing by \(v^2-f^2\) yields \(w'+P(x)w=Q(x)\), where
\[
P(x)=-\frac{1}{D_{\mathrm{eff}}x}+O(x^{-2}),\qquad
Q(x)=-\frac{2c}{D_{\mathrm{eff}}}x^2+O(x).
\]
The integrating factor is \(\mu(x)=C x^{-1/D_{\mathrm{eff}}}(1+O(x^{-1}))\), \(C>0\). If \(D_{\mathrm{eff}}>1/3\), integration gives \(w(x)\sim-2c x^3/(3D_{\mathrm{eff}}-1)\). At equality, \(w(x)\sim-6c x^3\log x\). In either case \(m\) eventually becomes negative, contradicting nonnegativity of an expected square. Thus the second moment is infinite.

**Sharp fourth-power coefficient.** For \(D_{\mathrm{eff}}<1/3\) the established \(m(x)=O(x^4)\) bound eliminates the growing homogeneous solution of the equation for \(w\), which would behave as \(x^{1/D_{\mathrm{eff}}}\) and yield a moment of order \(x^{1+1/D_{\mathrm{eff}}}\), strictly larger than quartic. Integrating from infinity now gives \(w(x)\sim2c x^3/(1-3D_{\mathrm{eff}})\), hence
\[
m(x)\sim\frac{x^4}{4(1-D_{\mathrm{eff}})(1-3D_{\mathrm{eff}})}.
\]
The difference of the two sign-conditioned second moments is one power smaller, by the backward first-order system and its polynomial-growth constraint, so the same leading term holds for either initial sign.

## Verification
The accompanying `verify.py` builds a finite-interval, two-orientation upwind Markov generator and independently solves its first- and second-hitting-time Poisson equations. The finite-domain results exhibit stable first moments and increasing second moments in the two regimes \(D_{\mathrm{eff}}=1/2\) and \(D_{\mathrm{eff}}=1/3\), but convergent-looking second moments for \(D_{\mathrm{eff}}=1/4\). Exact symbolic expansions in the script check both Lyapunov-generator identities and the coefficient matching in the asymptotic differential equation. These computations test, but do not prove, an infinite-domain moment statement; the proof above supplies that step.

## Relationship to prior work
Guéneau, Majumdar and Schehr (arXiv:2409.16951v1, Section IV and Appendix B) proved the mean first-passage threshold at \(D_{\mathrm{eff}}=1\), the quadratic large-distance mean asymptotic, and the formal higher-moment differential recurrence. They did **not** state the second-moment threshold, the mean-finite/variance-infinite phase, or its exact fourth-power coefficient. The present result uses their first-moment formula and derives the new finiteness boundary and coefficient with a separate Lyapunov construction and a critical integrating-factor contradiction. Radice (arXiv:2208.10220) studied return-time moments for a different, discrete Gillis random walk with stochastic resetting. General Lamperti/Bessel-process moment theory supplies strong analogy, but does not by itself identify the asserted coefficients or the protected-turning-point distinction for this continuous velocity-jump system.

## Limitations
No full first-passage distribution, survival-tail prefactor, higher-order moment threshold, or time-dependent resetting extension is proved. The exact potential, two symmetric velocity states, and initially prescribed sign assumptions are essential. The finite numerical cutoffs are not infinity certificates. A general Markov-modulated Lamperti theorem may subsume the finiteness criterion; publication priority remains uncertain.

## References
1. M. Guéneau, S. N. Majumdar and G. Schehr, *Run-and-tumble particle in one-dimensional potentials: mean first-passage time and applications*, arXiv:2409.16951v1 (public 2024-09-25), especially Section IV, Eq. (44), and Appendix B, Eq. (B9). https://arxiv.org/abs/2409.16951
2. M. Radice, *Non-homogeneous random walks with stochastic resetting: an application to the Gillis model*, arXiv:2208.10220 (public 2022-08-22). https://arxiv.org/abs/2208.10220
3. C. H. Lo, M. V. Menshikov and A. R. Wade, *Strong transience for one-dimensional Markov chains with asymptotically zero drifts*, arXiv:2208.12955 (2022). https://arxiv.org/abs/2208.12955
