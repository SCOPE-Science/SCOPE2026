# Sharp distributional optimization of renewal-reset Brownian search in one and three dimensions

## Finding

Consider a Brownian searcher with independent renewal resetting to newly sampled positions. The resetting-location law is a design variable, constrained to a bounded interval of distances from an absorbing target and to a fixed mean distance. In both (i) one-dimensional Brownian search for an absorbing point and (ii) three-dimensional Brownian search for an absorbing sphere, **a maximally dispersed two-point resetting law is the unique optimum for the entire first-passage-time distribution, for every independent strictly positive renewal clock**. Resetting always to the mean distance is the unique worst law. More generally, mean-preserving spreads of the resetting radius improve the full first-passage-time distribution in the usual stochastic order.

Specifically, fix \(0<\ell<m<u\) in the point-target case, or \(a<\ell<m<u\) for an absorbing three-dimensional sphere of radius \(a>0\). Define
\[
 Q_{\mathrm{end}}=\frac{u-m}{u-\ell}\delta_\ell+\frac{m-\ell}{u-\ell}\delta_u,
 \qquad Q_{\mathrm{point}}=\delta_m.
\]
For every resetting-radius law \(Q\) on \([\ell,u]\) with \(\mathbb E_QR=m\), there is a coupling of the three full first-passage times satisfying
\[
 \tau_{Q_{\mathrm{end}}}\le \tau_Q\le \tau_{Q_{\mathrm{point}}}\qquad\text{almost surely}.
\]
Thus, simultaneously for every \(t\ge0\),
\[
 \Pr(\tau_{Q_{\mathrm{end}}}>t)\le \Pr(\tau_Q>t)\le \Pr(\tau_{Q_{\mathrm{point}}}>t).
\]
The two extreme laws are the unique respective extrema of the first-passage-time laws: if \(Q\ne Q_{\mathrm{end}}\) the left inequality is strict at some finite \(t\), and if \(Q\ne\delta_m\) the right inequality is strict at some finite \(t\). The inequalities can be equal at early times, so strictness is **not** asserted at every time. More generally, whenever \(Q_1\) is a mean-preserving spread of \(Q_2\), then \(\tau_{Q_1}\le_{\mathrm{st}}\tau_{Q_2}\), and the two laws are different unless \(Q_1=Q_2\).

## Assumptions and scope

The searcher has diffusivity \(D>0\), corresponding to free generator \(D\Delta\). In case (i), it moves on the positive half-line and is absorbed on first contact with \(0\); its initial position is a fixed \(x_0>0\). In case (ii), it moves in the exterior of the closed sphere of radius \(a>0\) in \(\mathbb R^3\), and is absorbed on first contact with the sphere; its initial radius is fixed and exceeds \(a\). Radial symmetry makes the resetting direction irrelevant to the hitting-time law.

The reset intervals \(\sigma_0,\sigma_1,\ldots\) are iid, independent of all Brownian paths and reset positions, with \(0<\sigma_n<\infty\) almost surely. They need **not** be exponential or have finite mean for the stochastic ordering. After each reset, the radius is independently sampled from \(Q\), supported on \([\ell,u]\), while the initial starting point is kept fixed across the comparisons. Each inter-reset Brownian path is newly sampled, independent of preceding paths. All resets are instantaneous, and clocks restart after each relocation. There is no state-dependent reset triggering.

Convex order \(Q_1\succeq_{\mathrm{cx}}Q_2\) means the laws have the same finite mean and satisfy \(\int\phi\,dQ_1\ge\int\phi\,dQ_2\) for every convex \(\phi\). The usual stochastic order \(\tau_1\le_{\mathrm{st}}\tau_2\) means \(\Pr(\tau_1>t)\le\Pr(\tau_2>t)\) for all \(t\). No convex-order comparability is claimed between arbitrary laws sharing only their mean.

## Proof

**1. Exact free survival and its strict radial concavity.** Let \(H_z\) denote the first hitting time of the target from radial distance \(z\), interpreted as \(+\infty\) when the three-dimensional Brownian motion never hits. Reflection arguments and the exterior spherical harmonic hitting formula give, for \(t>0\),
\[
 S_1(t,z)=\Pr(H_z>t)=\operatorname{erf}\!\left(\frac{z}{\sqrt{4Dt}}\right),\qquad z>0,
\]
\[
 S_3(t,z)=1-\frac a z\operatorname{erfc}\!\left(\frac{z-a}{\sqrt{4Dt}}\right),\qquad z>a.
\]
For \(c=(4Dt)^{-1/2}\),
\[
 \frac{\partial^2 S_1}{\partial z^2}=-\frac{4c^3z}{\sqrt\pi}e^{-c^2z^2}<0.
\]
For the sphere, write \(E(z)=\operatorname{erfc}(c(z-a))\). On \(z>a\), \(E>0\), \(E'<0\), and \(E''>0\). Thus
\[
 \frac{\partial^2 S_3}{\partial z^2}
 =-a\left(\frac{E''}{z}-\frac{2E'}{z^2}+\frac{2E}{z^3}\right)<0.
\]
Both survival functions are therefore strictly concave in starting radius for every positive elapsed time. This property is the essential geometry-specific input.

**2. One-cycle convex-order and endpoint bounds.** If \(R\sim Q\), a fresh no-reset search cycle has survival
\[
 S_Q(t)=\int S_j(t,z)\,Q(dz),\qquad j\in\{1,3\}.
\]
Concavity implies \(S_{Q_1}(t)\le S_{Q_2}(t)\) whenever \(Q_1\succeq_{\mathrm{cx}}Q_2\). Strict concavity and a martingale coupling for convex order show that these inequalities are strict for all \(t>0\) when the distributions are different. For an arbitrary \(Q\) supported on \([\ell,u]\) with mean \(m\), the strict chord inequality and Jensen's inequality give
\[
 \frac{u-m}{u-\ell}S_j(t,\ell)
 +\frac{m-\ell}{u-\ell}S_j(t,u)
 \le S_Q(t)\le S_j(t,m).
\]
The left equality for one positive \(t\) requires support entirely at the two endpoints and hence \(Q=Q_{\mathrm{end}}\); the right equality requires \(Q=\delta_m\). Consequently, the **free cycle hitting times** obey
\[
 H_{Q_{\mathrm{end}}}\le_{\mathrm{st}}H_Q\le_{\mathrm{st}}H_{\delta_m}.
\]
This remains valid when \(H\) can equal infinity.

**3. Order-preserving renewal construction.** Independently sample a common sequence of positive reset intervals \((\sigma_n)_{n\ge0}\), and one common initial free first-hitting time \(H_0\). For each post-reset cycle \(n\ge1\), use one uniform random variable and the left-continuous quantiles of the three ordered one-cycle hitting-time distributions to construct
\[
 H_n^{\mathrm{end}}\le H_n^Q\le H_n^{\mathrm{point}}\qquad\text{almost surely}.
\]
All cycles and all reset intervals are otherwise independent. A protocol completes on its first cycle \(n\) with \(H_n\le\sigma_n\), at elapsed time \(\sum_{i<n}\sigma_i+H_n\). Whenever a slower protocol completes, the faster one has either already completed in an earlier cycle or finishes no later in the same cycle. This proves the claimed **pathwise order of completion times**.

All completion times are almost surely finite: for a fresh post-reset cycle the positive success probability is \(p_Q=\Pr(H_Q\le\sigma_1)>0\), because every positive deadline affords positive Brownian hitting probability from every radius in the bounded permitted interval. Success/failure cycles are iid, hence the first successful reset cycle occurs almost surely after finitely many trials. The initial cycle obeys the same finiteness convention.

For nonidentical convex-ordered laws, strict one-cycle order gives a positive probability of \(H_n^{(1)}<H_n^{(2)}\) and of finishing under the smaller time before a subsequent reset. Since the common initial cycle has a positive chance of resetting before absorption, the coupled full completion times differ with positive probability. Thus their distributions differ and some finite survival inequality is strict. This establishes uniqueness of both extremizers.

**4. Mean for any finite-mean renewal clock (auxiliary identity, not the novelty claim).** Suppose additionally \(\mathbb E\sigma<\infty\). Put
\[
 b_0=\mathbb E\min(H_0,\sigma),\quad
 q_0=\Pr(H_0>\sigma),\quad
 p_Q=\Pr(H_Q\le\sigma),\quad
 b_Q=\mathbb E\min(H_Q,\sigma).
\]
The ordinary renewal-reward identity gives the exact finite mean
\[
 \mathbb E\tau_Q=b_0+q_0\frac{b_Q}{p_Q}.
\]
The strict complete-law ordering implies corresponding inequalities between all finite increasing costs. For an exponential clock of rate \(r>0\), the single-cycle success probabilities are the already-known Laplace transforms
\[
 p_Q=\mathbb E_Q e^{-R\sqrt{r/D}}\quad\text{(point target)},
 \qquad
 p_Q=\mathbb E_Q\frac aR e^{-(R-a)\sqrt{r/D}}\quad\text{(sphere)},
\]
and \(\mathbb E\tau_Q=(1-p_{x_0})/(rp_Q)\). These Poisson mean formulas are recalled solely as comparisons and checks, not claimed as discoveries.

## Verification

The standalone, standard-library script `verification_check.py` evaluates both exact free-survival functions, numerical second derivatives over six positive times and eleven interior radii in each geometry, random fixed-mean two-site mixtures, the exact Poisson mean formulas, and independently integrated deterministic-renewal means. It passes 332 finite assertions and reports these illustrations for \(D=r=1\):

- Point target, \([\ell,u]=[1,3]\), \(m=2\), \(x_0=1\): the Poisson-clock mean is approximately \(4.67077427047\) for \(\delta_2\) and \(3.02691522730\) for the equal endpoint mixture. With deterministic resetting every \(1.35\) units, the corresponding checked means are approximately \(3.39837801428\) and \(2.54866173411\).
- Spherical target with \(a=1\), \([\ell,u]=[2,4]\), \(m=x_0=3\): the Poisson-clock means are approximately \(21.16716829679\) and \(9.72458187132\); the deterministic-clock means are approximately \(17.5634865109\) and \(9.21599294246\).

The proof of the all-time, all-clock and all-distribution claim is the strict-concavity and quantile-coupling argument above. Finite checker results alone would not establish it.

## Relationship to prior work

Julián-Salgado, Dagdug and Boyer (arXiv:2311.11897, first posted November 20, 2023) derive a two-site Poisson-reset mean first-passage formula and a discontinuous transition in optimal reset **rate**. Toledo-Marín and Boyer (arXiv:2206.14387) treat Poisson mean times, resetting events and information costs for distributions of reset points. Méndez, Flaquer-Galmés and Campos (arXiv:2401.01125) analyze Poisson-reset mean, variance, and an effective single-site interpretation for random reset locations. A later study by Julián-Salgado, Dagdug and Boyer (arXiv:2507.14483v2) optimizes Poisson rate for several compactly supported reset-site densities and obtains critical-rate transitions. None of the inspected relevant sections states a fixed-mean **complete first-passage-law** ordering for arbitrary positive renewal clocks, a unique endpoint optimizer for the entire law, or the exterior three-dimensional sphere extension.

The renewal decomposition itself is standard, and the Poisson mean effect of distributing reset sites follows readily from published formulas and Jensen's inequality. The assessed new theorem is specifically their non-Poisson **full-law, all-increasing-cost, sharp convex-order optimization**, including the sphere case with defective no-reset hitting times. A general implicit stochastic-order/restart comparison theorem in broader literature could reduce priority; no proof of absolute novelty is claimed.

## Limitations

The geometric concavity proof is specific to the positive half-line with a point absorber and the exterior of a sphere in three dimensions. No generalization to two-dimensional disk hitting, arbitrary domains, inner-ball hitting, or non-Brownian search is established. Reset radii are confined to an interval strictly outside the target and sampled independently after each failure; clock intervals are strictly positive, finite and independent. Reset cost, noninstantaneous relocations, state-dependent resets and environment feedback are excluded. Full stochastic order needs no moment of the renewal clock, but the finite-mean identity requires \(\mathbb E\sigma<\infty\). The two extremizers need not dominate all other laws in a pointwise strict sense at every observation time. The physical optimality here assumes the mean radius and allowed spatial interval are the only design constraints; transportation or energetic constraints may reverse practical preferences.

## References

1. P. Julián-Salgado, L. Dagdug and D. Boyer, *Diffusion with two resetting points*, arXiv:2311.11897 (first public submission November 20, 2023). https://arxiv.org/abs/2311.11897
2. V. Méndez, R. Flaquer-Galmés and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125 (2024). https://arxiv.org/abs/2401.01125
3. J. Q. Toledo-Marín and D. Boyer, *First passage time and information of a one-dimensional Brownian particle with stochastic resetting to random positions*, arXiv:2206.14387 (2022). https://arxiv.org/abs/2206.14387
4. P. Julián-Salgado, L. Dagdug and D. Boyer, *Abrupt transitions in the optimization of diffusion with distributed resetting*, arXiv:2507.14483v2 (2025). https://arxiv.org/abs/2507.14483
5. A. Chechkin and I. M. Sokolov, *Random Search with Resetting: A Unified Renewal Approach*, Physical Review Letters 121, 050601 (2018), DOI:10.1103/PhysRevLett.121.050601. https://doi.org/10.1103/PhysRevLett.121.050601
6. M. R. Evans and S. N. Majumdar, *Diffusion with resetting in arbitrary spatial dimension*, Journal of Physics A 47, 285001 (2014). https://doi.org/10.1088/1751-8113/47/28/285001
