# Sharp two-edge concentration laws for a high-dimensional run-and-rest swimmer

## Finding

In the stationary isotropic run-and-tumble model with a genuine exponentially distributed motionless tumble phase, the squared radius of a harmonically trapped swimmer has a nondegenerate limit as spatial dimension tends to infinity. This limiting law has *two sharp and different boundary exponents*: its near-zero exponent is determined by the escape rate from the resting phase, whereas its near-one exponent is determined by the departure rate from the running phase.

Let \(b,v,\lambda,\mu>0\). Set \(a=\mu/b\), \(p=\lambda/(2b)\), \(\pi_{\mathrm R}=\lambda/(\lambda+\mu)\), and \(\pi_{\mathrm T}=\mu/(\lambda+\mu)\). The normalized stationary squared radius is \(R_d^2=b^2\|X_d\|^2/v^2\). There is a random variable \(S\in(0,1)\), not depending on the dimension, for which

\[
\mathbb E[(R_d^2-S)^2]\le \frac2d,\qquad d\ge2.
\]

The limit has a completely specified perpetuity law: independently draw \(E\sim\operatorname{Beta}(a,1)\), \(Z\sim\operatorname{Beta}(p,1)\), and an independent copy \(S_{\mathrm R}'\) of \(S_{\mathrm R}\). Then

\[
S_{\mathrm R}\stackrel{\mathrm d}= (1-E)^2+E^2ZS_{\mathrm R}',\qquad
S_{\mathrm T}\stackrel{\mathrm d}=ZS_{\mathrm R}',
\]

and \(S\) is the mixture \(\pi_{\mathrm R}\mathcal L(S_{\mathrm R})+\pi_{\mathrm T}\mathcal L(S_{\mathrm T})\). These recursions determine unique probability laws on \([0,1]\). Their sharp tails are

\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{-a}\Pr(S>1-\varepsilon)
=\pi_{\mathrm R}2^{-a}},
\]

\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{-p}\Pr(S<\varepsilon)
=\pi_{\mathrm T}\,\mathbb E[S_{\mathrm R}^{-p}]\in(0,\infty)}.
\]

The negative moment above is finite for **every** positive triple of rates; it is defined unambiguously by the given perpetuity, rather than claimed to have an elementary closed form. One further exact normalization check is

\[
\mathbb E S=\frac{\lambda}{\lambda+\mu}\frac{b}{b+\mu}.
\]

## Assumptions and scope

For each integer \(d\ge2\), consider the athermal piecewise deterministic Markov process \((X_d(t),\sigma(t),N_d(t))\) on \(\mathbb R^d\), with equation \(\dot X_d=-bX_d+v\sigma N_d\). The state \(\sigma\in\{0,1\}\) jumps from 0 to 1 at rate \(\lambda\) and from 1 to 0 at rate \(\mu\). At every beginning of a run (state 1), the unit direction \(N_d\) is independently sampled uniformly on \(S^{d-1}\) and remains fixed during that run. During a tumble (state 0), propulsion vanishes and confinement continues. All waiting times and orientation draws are mutually independent. The continuous-time invariant solution is constructed from the infinite past; the restoring drift makes it unique in position law. No translational Brownian noise or inter-particle interactions are present. The limits \(d\to\infty\) and \(\varepsilon\downarrow0\) are separate in the stated order; no simultaneous-limit uniformity is claimed.

## Proof

**1. Stationary random-direction series.** Solving the stable linear equation backward gives

\[
Y_d:=bX_d/v=\sum_{j\ge0}w_jU_j^{(d)},\qquad
w_j=e^{-b t_j}(1-e^{-b u_j}),
\]

where \((t_j,t_j+u_j)\) are the disjoint run intervals measured backward from the observation time, and \(U_j^{(d)}\) are iid uniform unit vectors independent of these intervals. Each \(w_j\ge0\), the intervals do not overlap, and \(\sum_jw_j\le\int_0^\infty b e^{-bt}\,dt=1\). Define \(S=\sum_jw_j^2\). Since sphere directions satisfy \(\mathbb E U_i=0\) and \(\mathbb E[(U_i\cdot U_j)^2]=1/d\) for distinct indices, the cross terms in

\[
R_d^2=S+2\sum_{i<j}w_iw_j(U_i^{(d)}\cdot U_j^{(d)})
\]

have zero conditional covariances between distinct unordered index pairs. Consequently

\[
\mathbb E[(R_d^2-S)^2\mid(w_j)]=\frac4d\sum_{i<j}w_i^2w_j^2
\le\frac2d S^2\le\frac2d.
\]

This justifies the infinite sum by bounded \(L^2\) convergence and proves the asserted \(L^2\) radial limit.

**2. Perpetuity and normalization.** The stationary run fraction is \(\pi_{\mathrm R}\). Given that a run is in progress, its backward age \(A\) is \(\operatorname{Exp}(\mu)\). The backward age \(B\) of an intervening tumble is independently \(\operatorname{Exp}(\lambda)\). Thus \(E=e^{-bA}\) has beta parameter \(a=\mu/b\) and \(Z=e^{-2bB}\) has beta parameter \(p=\lambda/(2b)\), both with second beta parameter 1. The current run contributes square weight \((1-E)^2\); all earlier runs are discounted by \(E^2Z\). In a currently resting phase, all contributions are discounted by \(Z\). This proves both distributional recursions and the mixture. Repeated substitution is contractive because the independent multiplicative factors lie in \((0,1)\) and their products tend to zero almost surely, hence gives uniqueness. The recursions give

\[
\mathbb E S_{\mathrm R}=\frac{2(p+1)}{(a+1)(a+2p+2)},\qquad
\mathbb E S_{\mathrm T}=\frac{2p}{(a+1)(a+2p+2)},
\]

which combine to yield \(\mathbb E S=\pi_{\mathrm R}/(a+1)\) as stated. The infinite past contains runs almost surely, so \(S>0\), while finite present/past runs and nonzero resting times preclude \(S=1\) almost surely.

**3. Sharp upper tail.** Put \(u(\varepsilon)=\Pr(S_{\mathrm R}>1-\varepsilon)\). Since \(0\le ZS_{\mathrm R}'\le1\), the deficit is bounded by

\[
2E(1-E)\le1-S_{\mathrm R}\le2E.
\]

On \(E\le1/2\), the event of deficit below \(\varepsilon\) therefore sandwiches \(\{E<\varepsilon/2\}\) and \(\{2E(1-E)<\varepsilon\}\) (intersected with \(E\le1/2\)). Both have probability \((\varepsilon/2)^a(1+o(1))\). On \(E>1/2\), use the exact nonnegative decomposition

\[
1-S_{\mathrm R}=2E(1-E)+E^2(1-Z)+E^2Z(1-S_{\mathrm R}').
\]

A deficit below \(\varepsilon<1/16\) then requires simultaneously \(1-E<\varepsilon\), \(1-Z<4\varepsilon\), and \(1-S_{\mathrm R}'<8\varepsilon\). Independence gives the bound \(C\varepsilon^2u(8\varepsilon)\). The elementary inequality \(u(\varepsilon)\le\varepsilon^a+C\varepsilon^2u(8\varepsilon)\), iterated a fixed integer number of times greater than \(a/2\), implies \(u(\varepsilon)=O(\varepsilon^a)\). Consequently the \(E>1/2\) contribution is negligible and \(u(\varepsilon)\sim2^{-a}\varepsilon^a\). In the resting state, \(S_{\mathrm T}=ZS_{\mathrm R}'\); a near-one event additionally requires \(Z>1-\varepsilon\), which has probability \(O(\varepsilon)\) independent of the run variable. Hence its upper tail is \(O(\varepsilon^{a+1})\). Mixing proves the first boxed law.

**4. Negative moments and sharp lower tail.** Let \(f(\varepsilon)=\Pr(S_{\mathrm R}<\varepsilon)\) and \(g(\varepsilon)=\Pr(ZS_{\mathrm R}<\varepsilon)\). The perpetuity implies \(S_{\mathrm R}\ge(1-E)^2\), so a small value requires \(1-E<\sqrt\varepsilon\). On this event, for \(\varepsilon<1/16\), \(E>1/2\) and the remaining term requires \(ZS_{\mathrm R}'<4\varepsilon\). Independence and boundedness of the beta density near \(E=1\) give

\[
f(\varepsilon)\le C\sqrt\varepsilon\,g(4\varepsilon).
\]

Starting from \(g\le1\), this yields \(f(\varepsilon)=O(\varepsilon^{1/2})\). If \(f(\varepsilon)=O(\varepsilon^t)\), integration of the distribution function implies \(\mathbb E[S_{\mathrm R}^{-s}]<\infty\) for every \(0<s<t\). Since \(\mathbb E[Z^{-s}]=p/(p-s)<\infty\) for \(s<p\), Markov's inequality gives \(g(\varepsilon)=O(\varepsilon^s)\) for every \(s<\min(t,p)\). The preceding inequality upgrades the exponent to \(1/2+s\). Iterating this finite bootstrap raises \(t\) beyond any fixed \(p\), so \(\mathbb E[S_{\mathrm R}^{-p}]<\infty\) and \(f(\varepsilon)=o(\varepsilon^p)\). The exact beta CDF yields

\[
g(\varepsilon)=\varepsilon^p\mathbb E[S_{\mathrm R}^{-p};\ S_{\mathrm R}\ge\varepsilon]+f(\varepsilon).
\]

Dominated convergence now gives \(g(\varepsilon)\sim\varepsilon^p\mathbb E[S_{\mathrm R}^{-p}]\). As \(f=o(\varepsilon^p)\), mixing with \(\pi_{\mathrm T}>0\) proves the second boxed law. Positivity of the constant follows from \(0<S_{\mathrm R}\le1\).

## Verification

The accompanying `verify.py` uses only the Python standard library and a fixed random seed. It checks the exact first-moment identities against four independent stationary perpetuity simulations, samples the conditional finite-dimensional spherical variance, and compares the two predicted edge scalings against stationary mixed-state draws. Run `python3 verify.py` from the extracted package. These finite-sample diagnostics are supplementary; the probability limits and all-parameter inequalities follow from the analytical proof above, not from simulation. The negative-moment constant may be approximated by the same perpetuity recursion, with explicit Monte Carlo sampling error not asserted by the theorem.

## Relationship to prior work

Sun, Ye and Podgornik (2024), arXiv:2409.00578v1, formulate exactly this finite-tumble harmonic-trap model and derive every fixed-dimensional coordinate moment by a Volterra recursion, including a high-moment *coordinate* boundary exponent. They explicitly relate coordinate and radial moments but do not state the dimension-to-infinity random-squared-radius perpetuity, its mean-square convergence bound, or either sharp tail of that limit. Their full fixed-dimensional moment family does, in principle, determine the compactly supported law; the new contribution is the nontrivial limiting random geometry and two sharp boundary asymptotics, rather than a claim that the underlying stationary state was previously unknown.

Guéneau, Majumdar and Schehr (2026), arXiv:2602.08436v1, derive radial distributions via stick-breaking for the different *instantaneous-tumble* model, in which the particle always propels. Its weights sum to one and it has no independent rest-duration beta factor. Their general method supplies context for perpetuities but does not establish the finite-rest lower-edge power or the present two-rate classification. Basu et al. (2019), arXiv:1910.10083, study a one-dimensional three-state run-and-tumble special case, rather than the isotropic \(d\to\infty\) radius limit. General perpetuity theorems may be relevant background and priority risk; the specific two-sided sharp constants are proved here rather than inferred from a failed search.

## Limitations

The result concerns athermal harmonic confinement, exponential run and rest times, iid uniform reorientation at each run start, and a fixed positive rest exit rate. It proves high-dimensional convergence before taking small-radius limits, not uniform estimates when dimension and radius thresholds vary together. It does not characterize the full density of \(S\), and the near-zero constant is a finite negative moment defined through a perpetuity rather than an elementary explicit number. General Kesten/perpetuity boundary laws or subsequent unpublished work may independently imply the two-edge exponents; no claim of independent external certification or exhaustive priority search is made.

## References

1. A. Sun, F. Ye, R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578v1 (first public version, 2024-09-01). https://arxiv.org/html/2409.00578v1
2. M. Guéneau, S. N. Majumdar, G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436v1 (2026-02-09). https://arxiv.org/html/2602.08436v1
3. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit, G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083 (2019). https://arxiv.org/abs/1910.10083
