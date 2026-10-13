# A sharp infinite-wave threshold for an exponentially forced SIR model

## Finding

The standard closed SIR model with an **exponentially increasing** transmission rate can produce infinitely many strict local maxima in both infectious prevalence and incidence, even though the transmission law requires only **one log-linear segment (two endpoint values)** on every prescribed finite horizon. There is an exact sharp criterion for recurrent prevalence maxima.

**Theorem.** Let \(N,\gamma,\beta_0>0\), \(a\in\mathbb R\), and let \(S(0)>0\), \(I(0)>0\), \(R(0)\ge 0\) with \(S(0)+I(0)+R(0)=N\). For \(t\ge0\) take \(\beta(t)=\beta_0e^{at}\). Then:

1. If \(a\le0\) or \(a\ge\gamma\), infectious prevalence \(I(t)\) has at most one strict local maximum on \((0,\infty)\).
2. If \(0<a<\gamma\), set
   \[
   Q(t)=\frac{\beta(t)S(t)}{\gamma N},\qquad P(t)=\frac{\beta(t)I(t)}{aN},\qquad
   H(Q,P)=\gamma Q-(\gamma-a)\log Q+aP-a\log P.
   \]
   The quantity \(E=H(Q(0),P(0))\) is conserved. If \(E>\gamma+a\), \(I(t)\) has **exactly one strict local maximum and one strict local minimum during each period** of the transformed orbit; there are infinitely many of each. The incidence \(C(t)=\beta(t)S(t)I(t)/N\) has at least one strict local maximum in each period. If \(E\le\gamma+a\), \(I(t)\) is nonincreasing and has no strict interior local maximum.
3. For every nonstationary transformed orbit in the range \(0<a<\gamma\), there exists \(T>0\) such that
   \[
   S(t+T)=e^{-aT}S(t),\quad I(t+T)=e^{-aT}I(t),\quad C(t+T)=e^{-aT}C(t)
   \]
   for all \(t\ge0\). Hence wave heights decay geometrically even as \(\beta(t)\) increases without bound.

In particular, for \(N=\gamma=1\), \(a=1/2\), \(\beta_0=5\), and \((S(0),I(0),R(0))=(2/5,1/10,1/2)\), both prevalence and incidence have infinitely many strict local maxima, with no changes in the sign of \(d\log\beta(t)/dt\). For any prescribed finite number of waves, truncate this single log-linear transmission law after the requisite periods. Its two endpoint values of \(\log\beta\) suffice to specify the entire forcing on that finite interval. Constant transmission, by contrast, cannot produce two prevalence maxima in this closed model.

## Assumptions and scope

The equations are
\[
\dot S=-\frac{\beta(t)SI}{N},\qquad
\dot I=\frac{\beta(t)SI}{N}-\gamma I,\qquad
\dot R=\gamma I.
\]
The compartments are real-valued, with no births, reinfection, or replenishment; \(C\) denotes **infection incidence** and \(I\) denotes **prevalence**, not interchangeable observables. Solutions are considered on \([0,\infty)\). The infinite-wave construction uses unbounded \(\beta(t)\) over an infinite horizon; on each finite interval, its transmission rate is positive and bounded. A 'wave' here is a mathematically strict interior local maximum, with no fixed observational amplitude cutoff.

## Proof

**Global physical solution.** The equations for \(S\) and \(I\) are multiplicative, so positive initial values remain positive at all finite times. Since \(\dot R=\gamma I\ge0\) and total population is constant, \(0<S(t)+I(t)\le N\); thus the smooth nonautonomous solution exists globally and remains physical.

**Exact change of variables.** For \(a>0\), differentiate the definitions of \(Q,P\). Using \(\dot\beta=a\beta\) gives exactly
\[
\dot Q=aQ(1-P),\qquad
\dot P=\gamma P\left(Q-1+\frac a\gamma\right).
\tag{1}
\]
Conversely \(S=\gamma NQ/\beta\) and \(I=aNP/\beta\) recover the original system, with \(R=N-S-I\). In particular, the transformation is an exact nonautonomous conjugacy, not a numerical approximation.

**Periodic level sets when \(0<a<\gamma\).** Put \(Q_*=1-a/\gamma\in(0,1)\). Equation (1) is the classical positive predator–prey Lotka–Volterra flow. Direct differentiation gives
\[
\dot H=\bigl(\gamma Q-(\gamma-a)\bigr)a(1-P)
      +a(P-1)\bigl(\gamma Q-(\gamma-a)\bigr)=0.
\]
In logarithmic coordinates \((u,v)=(\log Q,\log P)\), the energy is
\[
H(e^u,e^v)=\gamma e^u-(\gamma-a)u+ae^v-av.
\]
It is strictly convex and coercive on the plane, with the unique minimum at \((Q_*,1)\). Each larger level is the smooth, compact, simple closed boundary of a strictly convex sublevel set. As the vector field (1) is nowhere zero on such a level, every such level is one periodic trajectory of some period \(T>0\); its minimum-energy level is the stationary equilibrium.

**Sharp prevalence criterion.** Along a nonstationary cycle, \(Q\) has one minimum \(Q_{\min}<Q_*\) and one maximum \(Q_{\max}>Q_*\). Both occur when \(P=1\), since \(\dot Q=aQ(1-P)\). The function \(Q\mapsto H(Q,1)\) is strictly increasing for \(Q>Q_*\), and \(H(1,1)=\gamma+a\). Therefore
\[
Q_{\max}>1\quad\Longleftrightarrow\quad E>\gamma+a.
\]
Moreover \(\dot I=\gamma I(Q-1)\). If \(E\le\gamma+a\), this derivative is everywhere nonpositive. If \(E>\gamma+a\), the level intersects \(Q=1\) twice per period, once with \(\dot Q>0\) and once with \(\dot Q<0\), since the energy exceeds its constrained minimum at \((Q,P)=(1,1)\). The first crossing yields a strict minimum and the second a strict maximum of \(I\); there are no other extrema in that period. Every period repeats these sign changes.

**Incidence and geometric damping.** The incidence has the exact representation
\[
C(t)=\frac{a\gamma N}{\beta(t)}Q(t)P(t),\qquad
\frac{d}{dt}\log C=\frac{\dot Q}{Q}+\frac{\dot P}{P}-a.
\]
At either extremum of \(Q\), \(P=1\), so this logarithmic derivative equals \(\gamma(Q-1)\). When \(E>\gamma+a\) it is positive at \(Q_{\max}>1\) and negative at \(Q_{\min}<1\). Its periodic sign pattern therefore forces at least one strict incidence maximum in every transformed period (the functions are analytic and the derivative is not identically zero). The definitions of \(S,I,C\), periodicity of \(Q,P\), and \(\beta(t+T)=e^{aT}\beta(t)\) give all three attenuation identities. The positive physical compartments decay towards zero, with \(R(t)\to N\).

**Other growth rates.** If \(a\le0\), \(d(\log Q)/dt=a-\beta I/N<0\), where \(Q=\beta S/(\gamma N)\). Thus \(Q\) decreases and \(I\) has at most one strict maximum. If \(a\ge\gamma\), the transformed system still applies, with \(\dot P=\gamma P(Q-1)+aP\ge\gamma PQ>0\). Therefore \(P\) increases strictly and \(\dot Q=aQ(1-P)\) can switch sign only once, from positive to negative. So \(Q\) increases and then decreases at most once, and \(\dot I=\gamma I(Q-1)\) has at most one transition from positive to negative. These arguments prove the stated exhaustive trichotomy.

**Exact example.** For the stated parameters the initial transformed state is \((Q(0),P(0))=(2,1)\), and
\[
E=\frac52-\frac12\log2>\frac32=\gamma+a,
\]
using \(\log2<1\). The sharp criterion supplies infinitely many prevalence and incidence waves. On any finite window containing arbitrarily many successive transformed periods, \(\log\beta(t)=\log5+t/2\) is the affine interpolation of its values at just the two endpoints, without interior knots.

## Verification

The standalone standard-library script `verify.py` performs exact polynomial-identity checks for the transformed equations and energy conservation, verifies the incidence derivative at the relevant turning points, and checks the rational initial data and strict threshold inequality. Run `python3 verify.py`; it prints `VERIFY_OK` on success. The periodic-orbit and sharp-crossing arguments are analytical and are not inferred from finite computation.

## Relationship to prior work

Rabajante (2026), arXiv:2610.05556v1, introduces peak-preserving dynamic complexity, the time-varying SIR framework, and log-linear interpolation of transmission through knot values. It shows representability of arbitrary epidemic wave shapes under generally flexible time-varying transmission, but it does not establish this **fixed two-endpoint exponential forcing**, its exact autonomous scaling, or the sharp energy criterion for infinitely repeated damped waves. Our theorem gives a structural existence boundary for noiseless peak counts; it **does not** claim that a data-dependent, amplitude-aware, posterior-predictive complexity estimate equals two.

Maheshwari, Shetty, Bannur and Merugu (2021), *CoSIR*, provide an earlier SIR-to-Lotka–Volterra connection under a **state-feedback transmission policy** tailored to hold the unscaled infective population in bounded LV cycles, with finite physical depletion time. This is an important predecessor, and the use of LV integrability alone is not asserted to be new. Their dynamically chosen control law and finite-time oscillatory infective trajectories do not imply the present exogenous exponential transmission, periodically rescaled infective variable, globally existing exponentially damped real epidemic waves, or the \(E>\gamma+a\) test.

Earn and Parsons (2025), arXiv:2511.01939, analyze conserved epidemic momentum and related phase-plane geometry, including distinctions between autonomous and nonautonomous transmission. The specific exponentially forced LV transformation and knot-count consequence are not their established result. Perakis et al. (2023) use piecewise-constant wave-specific SIR rates; their number of pieces grows with modeled waves, unlike the continuous single-affine-log forcing here. General LV periodicity is classical; originality is restricted to its exact coupling with this specified nonautonomous SIR law and the sharp observables/complexity consequences.

## Limitations

The construction assumes exponentially **unbounded** contact transmission as \(t\to\infty\), a potentially unrealistic policy over very long periods. The peaks become arbitrarily small and need not survive surveillance noise, detection thresholds, posterior predictive tolerances, or a finite sampling grid. It does not identify or estimate a real epidemic's minimal peak-preserving complexity and does not imply a sustained epidemic burden or recurring disease without replenishment. Only the closed homogeneous SIR equations, positive initial data, and constant removal rate are covered. Despite substantive literature searches, an undiscovered exact exponential-forcing equivalence remains a residual originality risk; no independent external validation is asserted.

## References

1. J. F. Rabajante, *How Simple Models Can Reproduce Multiple Epidemic Waves: Peak Topology, Minimal Dynamic Complexity, and Inference for Time-Varying Transmission*, arXiv:2610.05556v1 (first posted 2026-10-04), https://arxiv.org/abs/2610.05556.
2. H. Maheshwari, S. Shetty, N. Bannur, S. Merugu, *CoSIR: Optimal control of SIR epidemic dynamics by mapping to Lotka–Volterra System*, medRxiv:2020.11.10.20211995v3 (2021), https://doi.org/10.1101/2020.11.10.20211995.
3. D. J. D. Earn and T. L. Parsons, *Epidemic “momentum” and a conservation law for infectious disease dynamics*, arXiv:2511.01939 (2025), https://arxiv.org/abs/2511.01939.
4. G. Perakis and colleagues, *COVID-19: A multiwave SIR-based model for learning waves*, *Production and Operations Management* (2023), https://doi.org/10.1111/poms.13681.
