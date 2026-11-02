# Rare co-outliers synchronize reset ages without sharing a reset event

## Finding

Consider the stationary one-dimensional Brownian gas subject to uniform batch resetting described in the reference [1]. Fix an integer \(N\ge 2\), a batch size \(1\le m\le N\), diffusivity \(D>0\), and total batch-event rate \(r>0\). At each event, a uniformly selected subset of exactly \(m\) labels is sent to the origin; between events the coordinates are independent Brownian motions with generator \(D\partial_x^2\). For two distinct labels write \(X_1,X_2\) for the stationary positions, and \(A_1,A_2\) for their backward elapsed times since their respective most recent resets.

Define
\[
\lambda=\frac{rm}{N},\qquad c=\frac{rm(m-1)}{N(N-1)},\qquad e=\lambda-c,\qquad a=2\lambda-c.
\]
The parameters \(\lambda,c,e\) are respectively the reset rate of one label, the shared-reset rate of the pair, and the rate of each of the two exclusive-reset event types.

**Theorem (joint high excursions and their reset ancestry).** Fix these parameters and let \(x\to+\infty\).

1. If \(m\ge2\), put \(z=x\sqrt{2a/D}\). Then
\[
\Pr\{X_1>x,\ X_2>x\}\sim
\frac{a}{c\sqrt{2\pi z}}e^{-z}.
\]
Conditional on this joint excursion, the two reset ages satisfy
\[
\frac{A_1}{x},\frac{A_2}{x}\ \xrightarrow{\Pr}\ \frac1{\sqrt{2Da}},
\]
and their **unscaled** absolute age gap has the limit
\[
|A_1-A_2|\ \Longrightarrow\
\frac{c^2}{a^2}\,\delta_0+
\left(1-\frac{c^2}{a^2}\right)\operatorname{Exp}(c/2).
\]
Here \(\operatorname{Exp}(c/2)\) means a probability distribution on positive times with density \((c/2)e^{-cu/2}\), and \(\delta_0\) is a unit point mass at zero. Equivalently, the limiting conditional probability that the labels' *last reset event was the same event* is exactly \((c/a)^2\). The two possible signs of a nonzero age difference have equal limiting probabilities.

2. If \(m=1\), the two stationary coordinates and their reset ages are independent. Writing \(\lambda=r/N\),
\[
\Pr\{X_1>x,X_2>x\}=\tfrac14 e^{-2x\sqrt{\lambda/D}},
\]
and the conditional age difference has the different scale
\[
\frac{A_1-A_2}{\sqrt{x}}\ \Longrightarrow\
\mathcal N\!\left(0,\frac1{2\sqrt D\,\lambda^{3/2}}\right).
\]
Thus one-at-a-time resetting has age differences of order \(\sqrt x\) during joint high excursions; **any** positive shared-reset rate makes the difference tight and gives the atom-plus-exponential law above. The two regimes are not claimed to be uniform as \(c\downarrow0\).

For every \(m\), the stationary ordinary covariance \(\operatorname{Cov}(X_1,X_2)\) is exactly zero. For \(m\ge2\), however, the joint extreme dependence index is
\[
\eta=\sqrt{\frac{\lambda}{2a}}
=\frac1{\sqrt{2\bigl(2-(m-1)/(N-1)\bigr)}}>\frac12,
\]
whereas \(\eta=1/2\) for \(m=1\). The upper-tail dependence coefficient itself is zero in both regimes. This index and the joint-excursion asymptotic are included to quantify the observations; the new structural focus is the conditional ancestry and age-gap law.

## Assumptions and scope

All parameters and the integer labels are fixed before the threshold \(x\to\infty\). The particles have independent Brownian driving noises and no direct interaction. Batch selections are independent across the rate-\(r\) Poisson events, and each selected coordinate is completely reset to zero. Time is continuous; there is no external drift or confinement. Reset ages are observed in the two-sided stationary realization. The theorem concerns two **distinct** particle labels. It does not take any large-particle-number limit or simultaneous small-common-reset-rate limit.

Each label resets at positive rate \(\lambda\), ensuring its stationary finite age; the pair stationary construction exists by marking the Poisson event stream and taking the most recent event affecting each label. Its positions are obtained using independent Brownian increments of those respective ages.

## Proof

### 1. Exact stationary reset-age measure

For the selected pair, independently thin the Poisson events into three disjoint types: both selected, only label 1 selected, and only label 2 selected. Their rates are \(c,e,e\), respectively. Events affecting neither label are irrelevant. In the backward stationary construction, let the elapsed times to the latest events of those three types be independent exponentials \(E_c,E_1,E_2\) with rates \(c,e,e\), omitting zero-rate types. Then
\[
A_1=\min(E_c,E_1),\qquad A_2=\min(E_c,E_2).
\]
When \(c,e>0\), the joint age law has an atom on the diagonal with one-dimensional density
\[
\Pr\{A_1=A_2\in dt\}=c e^{-at}\,dt,
\]
and off-diagonal two-dimensional density
\[
 f(s,t)=e\lambda\,
 \exp\{-e\min(s,t)-\lambda\max(s,t)\},\qquad s\ne t,\quad s,t>0.
\]
For example, for \(s<t\) the joint age survival function is
\[
\Pr(A_1>s,A_2>t)=e^{-es-\lambda t},
\]
whose mixed derivative gives the displayed density. For \(e=0\), only the diagonal component remains; for \(c=0\), the two exponential ages are independent. This is the Marshall–Olkin shared-shock construction [2], here obtained directly from batch marks. The diagonal mass without conditioning is \(c/a\).

Conditional on these two ages, the particle positions are independent centered Gaussians of variances \(2DA_1\) and \(2DA_2\). Define the positive Gaussian tail
\[
 Q_t(x)=\overline\Phi\left(\frac{x}{\sqrt{2Dt}}\right).
\]
Consequently, with \(J_x=\int_0^\infty e^{-at}Q_t(x)^2dt\), the diagonal contribution to the joint exceedance probability is \(cJ_x\). For \(e>0\), the total off-diagonal contribution is
\[
O_x=2e\lambda\int_0^\infty e^{-\lambda t}Q_t(x)
  \left[\int_0^t e^{-es}Q_s(x)\,ds\right]dt.
\]
These are **exact** stationary integral identities, not asymptotic guesses.

### 2. The common saddle and its exact prefactor

For \(x/\sqrt t\to\infty\), the Gaussian Mills estimate gives
\[
 Q_t(x)=\frac{\sqrt{Dt}}{\sqrt\pi x}
 \exp\left(-\frac{x^2}{4Dt}\right)
 \left(1+O\left(\frac{Dt}{x^2}\right)\right).
\]
The diagonal Laplace phase is
\[
F_x(t)=at+\frac{x^2}{2Dt}.
\]
It has a unique minimum at \(t_*=x/\sqrt{2Da}\), with \(F_x(t_*)=z=x\sqrt{2a/D}\). Ordinary one-variable Laplace asymptotics, or the integral representation of \(K_2\), now yield
\[
 J_x\sim\frac{e^{-z}}{a\sqrt{2\pi z}}.
\]
For the off-diagonal integral set \(s=t-u\) with \(u>0\). The two-variable phase
\[
 e(t-u)+\lambda t+\frac{x^2}{4D}
 \left(\frac1{t-u}+\frac1t\right)
\]
has its unique constrained minimum at \(u=0,t=t_*\) whenever \(c=\lambda-e>0\). Its unconstrained stationary point has the first age greater than the second, outside the domain \(s<t\). In the saddle window, for every fixed \(u\ge0\),
\[
 e^{eu}\frac{Q_{t-u}(x)}{Q_t(x)}\longrightarrow e^{-cu/2}.
\]
The boundary-layer direction is integrable precisely because \(c>0\). To justify exchanging limit and integration, choose a sufficiently small relative window about \(t_*\). The standard Gaussian tail derivative obeys
\[
\partial_t\log Q_t(x)\ge \frac{x^2}{4Dt^2},
\]
so inside this window the last display is bounded by \(e^{-cu/4}\), uniformly in \(x\) large. Outside the window the strictly convex two-variable phase has a positive large-deviation gap. Gaussian tail upper bounds control both tails of the age integral. Dominated convergence and Laplace concentration therefore give
\[
\frac{O_x}{J_x}\longrightarrow
2e\lambda\int_0^\infty e^{-cu/2}du
=\frac{4e\lambda}{c}.
\]
Since \(c^2+4e\lambda=(2\lambda-c)^2=a^2\), the joint probability is
\[
 cJ_x+O_x\sim\left(c+\frac{4e\lambda}{c}\right)J_x
=\frac{a^2}{c}J_x
\sim\frac{a}{c\sqrt{2\pi z}}e^{-z}.
\]
For \(e=0\), the same result follows with \(O_x=0\) and \(a=c=\lambda\).

### 3. Conditional ancestry and age-gap limit

The diagonal contribution divided by the total gives
\[
 \Pr\{A_1=A_2\mid X_1>x,X_2>x\}
 \longrightarrow\frac{c}{c+4e\lambda/c}=\frac{c^2}{a^2}.
\]
On the off-diagonal component the limiting distribution of \(u=|A_1-A_2|\), by the same uniform saddle argument, has density proportional to \(e^{-cu/2}\), hence is \(\operatorname{Exp}(c/2)\). The two off-diagonal orientations have the same density. The strict minimum at \(t_*\) simultaneously proves both \(A_i/x\to1/\sqrt{2Da}\) in conditional probability. Combining the diagonal and off-diagonal pieces proves the stated weak limit of the absolute age gap.

### 4. One-at-a-time boundary and extreme-dependence index

For \(m=1\), the individual reset streams are independent Poisson processes, each of rate \(\lambda=r/N\). Mixing \(N(0,2Dt)\) against an \(\operatorname{Exp}(\lambda)\) age gives the exact one-sided Laplace tail \(\Pr(X_i>x)=\tfrac12e^{-x\sqrt{\lambda/D}}\). Thus the joint exceedance probability factors exactly. The conditional single-coordinate age has Laplace phase \(\lambda t+x^2/(4Dt)\), uniquely minimized at \(x/(2\sqrt{D\lambda})\), with second derivative \(4\sqrt D\lambda^{3/2}/x\). Its centered fluctuations divided by \(\sqrt x\) converge to a zero-mean Gaussian of variance \(1/(4\sqrt D\lambda^{3/2})\); subtracting two independent copies proves the displayed boundary-case age-difference limit.

Finally, for every \(m\), each marginal positive tail is \(\tfrac12e^{-x\sqrt{\lambda/D}}\). Comparing this with the joint exponent \(\sqrt{2a/D}\) establishes \(\eta=\sqrt{\lambda/(2a)}\) for positive \(c\), and with the independent exact product when \(c=0\). Since the joint exponent exceeds the marginal exponent, asymptotic upper-tail dependence is zero. Conditional Gaussian centering gives \(\mathbb E[X_1X_2]=0\), despite positive dependence in even observables.

## Verification

The standalone program `verify_pair_extremes.py` checks rational identities for every \(2\le N\le30\) and \(1\le m\le N\), including the stationary two-point transform of [1, Eq. (5)] and its published squared-position covariance. It also evaluates independent integral expressions for the diagonal and off-diagonal high-excursion probabilities and the conditional age-gap Laplace transform, using log-Gaussian-tail quadrature to avoid underflow. Its actual execution passed **4,633 deterministic assertions**.

These finite checks are diagnostics. The infinite-threshold prefactor, conditional weak convergence and special-case Gaussian scaling are proved by the preceding analytical arguments, not inferred from numerical convergence.

## Relationship to prior work

De Mauro, Majumdar and Schehr [1] introduced the batch-resetting model and derived its exact one- and two-coordinate stationary characteristic functions and densities, as well as correlations of squared positions. Their supplementary two-coordinate density [1, Eq. (S36)] already determines the **unconditional spatial joint law**. Consequently, neither the model nor that density is claimed as new. The present result instead conditions on exceptionally large *simultaneous* excursions and resolves their previously uncharacterized **last-event identity and reset-age separation**, which are not specified by the two-position stationary density. The sharp tail prefactor makes the conditioning quantitative and is not asserted to be a fundamentally new stochastic representation.

The Marshall–Olkin common-shock construction [2] supplies the classical joint waiting-time structure, but by itself has no Brownian high-excursion conditioning. Opitz [3] establishes residual joint-tail indices for elliptical Laplace mixtures. In particular, its zero-linear-correlation bivariate Laplace case already yields \(\eta=1/\sqrt2\), matching the all-at-once-resetting boundary \(m=N\); it does not provide the interior batch-marked conditional ancestry distribution. Engelke, Opitz and Wadsworth [4] give broader general tail-dependence methods for random-scale constructions, but no corresponding model-specific mixed reset-age posterior was identified in the inspected material. These literatures are methodological prerequisites and priority risks, rather than evidence of a certified independent discovery.

## Limitations

The conditional limit holds for fixed positive \(c\), so it is **not uniform** as the batch size approaches one or the common-reset intensity tends to zero. The Brownian drivers must be independent and each selected coordinate fully reset. The theorem does not cover non-Poisson clocks, heterogeneous reset-selection weights, interacting particles, general drifts, or simultaneous limits involving \(N\) and the extreme threshold. No claim is made about experimental verification or an independent mathematical audit.

## References

[1] G. de Mauro, S. N. Majumdar and G. Schehr, *Tuning the strength of emergent correlations in a Brownian gas via batch resetting*, arXiv:2601.20077v1, first public version 27 January 2026; see the stationary transform and supplemental Eqs. (S29)–(S39). https://arxiv.org/html/2601.20077v1

[2] A. W. Marshall and I. Olkin, *A generalized bivariate exponential distribution*, Journal of Applied Probability (1967), common-shock construction. https://doi.org/10.2307/3212024

[3] T. Opitz, *Modeling asymptotically independent spatial extremes based on Laplace random fields*, arXiv:1507.02537 (2015), Proposition 1. https://arxiv.org/abs/1507.02537

[4] S. Engelke, T. Opitz and J. Wadsworth, *Extremal dependence of random scale constructions*, arXiv:1803.04221 (2018). https://arxiv.org/abs/1803.04221
