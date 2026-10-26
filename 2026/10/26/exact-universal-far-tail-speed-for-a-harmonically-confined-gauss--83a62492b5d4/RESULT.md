# Exact universal far-tail speed for a harmonically confined Gaussian shot-noise bath

## Finding
Fix \(k>0\), \(r>0\), \(\sigma>0\) and \(D\ge0\). For the stationary one-dimensional harmonic particle driven by independent thermal Brownian motion and instantaneous centered Gaussian kicks of Poisson rate \(r\), its displacement \(X\) obeys the sharp logarithmic-tail law
\[
\boxed{\displaystyle\lim_{x\to\infty}\frac{-\log\Pr(X>x)}{x\sqrt{\log x}}=\frac{\sqrt2}{\sigma}.}
\]
The same constant holds for the left and two-sided tails. It does not depend on the fixed confinement rate \(k\), positive kick rate \(r\), or thermal diffusivity \(D\). In particular, these stationary tails decay faster than any exponential tail \(e^{-cx}\) but slower than every Gaussian tail \(e^{-cx^2}\) in the logarithmic-rate sense.

## Assumptions and scope
Let \(W\) be standard Brownian motion. Independently let \(J\) be a two-sided compound-Poisson process with rate \(r\), independent jump amplitudes \(Y_j\sim N(0,\sigma^2)\), and stationary Poisson jump times. We consider the unique stationary solution to
\[
dX_t=-k X_t\,dt+\sqrt{2D}\,dW_t+dJ_t.
\]
Here \(D=0\) is permitted but \(k,r,\sigma\) must each be strictly positive and fixed while \(x\to\infty\). The stationary variable is
\[
X\ \stackrel{d}{=}\ G+\sum_{j:T_j\le0}e^{kT_j}Y_j,
\qquad G\sim N(0,D/k),
\]
where \(G\) is independent of the marked Poisson process. The series is absolutely convergent almost surely because \(r\,\mathbb E|Y_1|\int_0^\infty e^{-ku}\,du<\infty\); contraction also gives uniqueness of the stationary law.

## Proof
**Step 1: Laplace transform.** Campbell's identity and the independent Gaussian term give, for every real \(t\),
\[
K(t):=\log\mathbb E e^{tX}
=\frac{Dt^2}{2k}+r\int_0^\infty\!\left(e^{\sigma^2t^2e^{-2ku}/2}-1\right)du
=\frac{Dt^2}{2k}+\frac{r}{2k}\int_0^z\frac{e^v-1}{v}\,dv,
\qquad z=\frac{\sigma^2t^2}{2}.
\]
All integrals are finite for fixed \(t\): the integrand is bounded near zero in transformed coordinates, and at large shot ages it is of order \(e^{-2ku}\).

**Step 2: upper probability bound.** Fix \(0<\varepsilon<1\), take \(x>e\), and choose
\[
t_x=\frac{\sqrt2}{\sigma}(1-\varepsilon)\sqrt{\log x},
\qquad z_x=(1-\varepsilon)^2\log x.
\]
For \(v\ge0\), \((e^v-1)/v\le e^v\), so the transform satisfies
\[
K(t_x)\le\frac{Dt_x^2}{2k}+\frac{r}{2k}z_xe^{z_x}
=O(\log x+x^{(1-\varepsilon)^2}\log x)
=o(x\sqrt{\log x}).
\]
The Chernoff inequality \(\Pr(X>x)\le\exp[-t_xx+K(t_x)]\) therefore implies
\[
\liminf_{x\to\infty}\frac{-\log\Pr(X>x)}{x\sqrt{\log x}}
\ge\frac{\sqrt2}{\sigma}(1-\varepsilon).
\]
Letting \(\varepsilon\downarrow0\) proves the lower bound for the desired limit.

**Step 3: a matching recent-kick event.** Fix \(\varepsilon>0\), set
\[
\delta_x=1/\log x,\qquad a_x=\sigma\sqrt{2\log x},
\qquad n_x=\left\lceil\frac{(1+\varepsilon)x}{a_x}\right\rceil.
\]
Require exactly \(n_x\) Poisson events in \((-\delta_x,0]\), each with mark in \([a_x,a_x+1]\). Since every event has weight at least \(e^{-k\delta_x}\), this event supplies at least \(e^{-k\delta_x}n_xa_x>x\) for all sufficiently large \(x\). The shot contribution from times prior to \(-\delta_x\), together with all thermal noise, is independent of these recent kicks and has a symmetric distribution, hence is nonnegative with probability at least one-half. Consequently
\[
\Pr(X>x)\ge\frac12e^{-r\delta_x}\frac{(r\delta_x)^{n_x}}{n_x!}p_x^{n_x},
\qquad p_x=\Pr\{Y_1\in[a_x,a_x+1]\}.
\]
A Gaussian-density lower bound yields
\[
p_x\ge\frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{(a_x+1)^2}{2\sigma^2}\right),
\qquad -\log p_x\le\log x+O(\sqrt{\log x}).
\]
Moreover \(\log n_x-\log(r\delta_x)=\log x+O(\log\log x)\) and \(\log(n_x!)\le n_x\log n_x\). Hence
\[
-\log\Pr(X>x)
\le n_x\left(2\log x+O(\sqrt{\log x})\right)+O(1)
=\left(\frac{\sqrt2}{\sigma}(1+\varepsilon)+o(1)\right)x\sqrt{\log x}.
\]
Taking \(\limsup\) and then \(\varepsilon\downarrow0\) matches Step 2. This is an infinite-\(x\) proof rather than an extrapolation from a finite sample.

**Step 4: other tails.** The marked point process and the Brownian term are symmetric in law under simultaneous sign reversal, so \(\Pr(X<-x)=\Pr(X>x)\). Also \(\Pr(|X|>x)=2\Pr(X>x)\); the constant factor does not affect the logarithmic-rate limit.

## Verification
The accompanying `checker.py` performs 315 deterministic exact rational coefficient and asymptotic-scale consistency assertions. For four parameter choices, it reconstructs the stationary moment-generating series up to order 28 and independently verifies the stationary generator equation and exact second and fourth cumulants. Additional numerical scale inequalities check the two bounding constructions for several large logarithmic sizes. The tail limit itself is established by the analytic Chernoff and Poisson-burst bounds above; no finite computation certifies an infinite limit.

## Relationship to prior work
Di Bello, Majumdar, Marathe, Metzler and Roldán give the harmonic active-bath model, its stationary Fourier representation, and finite-order moments, and demonstrate a distribution broader than the corresponding Gaussian. Their 2023 preprint (in particular Sections 3–4, figures and appendices) does not present the stated \(x\sqrt{\log x}\) logarithmic-tail rate. The independent-kick construction is therefore *not* proposed here as new; what is assessed is the precise extreme-displacement scale and its constant for the Gaussian-mark specialization. Park and collaborators studied a related optical-trap active-bath model with finite-duration active forcing and its approximately exponential measured tails, rather than this exact instantaneous-Gaussian-jump asymptotic. Ganesh, Macci and Torrisi give a sample-path large-deviation principle for a different regime involving growth of the observation horizon and a nondecreasing cumulative shot-response kernel. Earlier work by Gilbert and Pollak studies general shot-noise amplitude distributions; its precise relevance to Gaussian marks and this logarithmic rate remains a priority risk.

## Limitations
The limit requires fixed strictly positive Poisson rate and Gaussian kick variance; neither a zero-kick model nor a simultaneous vanishing-rate limit is covered. The result concerns stationary fixed-time tails, not excursions over long time windows, density-level prefactors, finite-threshold error estimates, or finite-sample statistical recovery. It is a comparison with existing exact stationary characterizations, not a claim to have discovered that law. Priority could change if an older general shot-noise theorem directly contains the specified constant.

## References
1. C. Di Bello, R. Majumdar, R. Marathe, R. Metzler, and É. Roldán, *Brownian particle in a Poisson-shot-noise active bath: exact statistics, effective temperature, and inference*, arXiv:2309.13424 (first posted 2023-09-23), https://arxiv.org/abs/2309.13424 .
2. J. T. Park, G. Paneru, C. Kwon, S. Granick, and H. K. Pak, *Rapid-Prototyping a Brownian Particle in an Active Bath*, arXiv:2101.07977 (2021), https://arxiv.org/abs/2101.07977 .
3. A. Ganesh, C. Macci, and G. L. Torrisi, *Sample path large deviations principles for Poisson shot noise processes, and applications*, Electronic Journal of Probability 10 (2005), 1026–1043, doi:10.1214/EJP.v10-273 .
4. E. N. Gilbert and H. O. Pollak, *Amplitude Distribution of Shot Noise*, Bell System Technical Journal 39 (1960), 333–350, doi:10.1002/j.1538-7305.1960.tb01603.x .
