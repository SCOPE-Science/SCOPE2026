# Exact pure-pulse vaccination threshold for two-season transmission

## Finding
Consider a disease-free susceptible population with waning immunity, periodically dosed with a fixed quantity of vaccination effort. When transmission is higher during one consecutive season than another, the unique globally optimal vaccination measure is a pure pulse at the start of the high-transmission season **if and only if** the per-period vaccine mass is below an explicit positive threshold. At that threshold there is a sharp loss of pure-pulse optimality; either the high-season side or the preceding low-season side can cause the loss, depending on an explicit inequality.

Let \(0<h<T\), \(\delta>0\), and \(\beta_H>\beta_L>0\). On the circle of length \(T\), let \(\beta(t)=\beta_H\) for \(0<t<h\), and \(\beta(t)=\beta_L\) for \(h<t<T\). Write
\[
r=e^{-\delta T},\quad s=e^{-\delta h},\quad B=\beta_H(1-s)+\beta_L(s-r).
\]
For any fixed mass \(q\geq0\), minimize the disease-free invasion functional \(J(\mu)=\int_0^T\beta(t)S_\mu(t)\,dt\) over all nonnegative \(T\)-periodic Borel vaccination measures \(\mu\) of mass \(q\) per period. Then the unique minimizer is \(\mu=q\delta_0\) precisely when
\[
0\leq q\leq q_*:=\min\!\left\{\log\!\frac{\beta_H(1-r)}{B},\ \log\!\frac{B}{\beta_L(1-r)}\right\}.
\]
Both entries in the minimum are strictly positive. If \(q>q_*\), the pure pulse is not a minimizer. When \(B^2>\beta_H\beta_L(1-r)^2\), the first threshold is smaller and the advantageous infinitesimal reallocation is *after* the upward seasonal jump. When \(B^2<\beta_H\beta_L(1-r)^2\), the second is smaller and the advantageous reallocation is *before* that jump. At equality both directions become marginal simultaneously.

For the square-wave example \(T=\delta=1\), \(h=1/2\), \(\beta_H=7/4\), \(\beta_L=1/4\), the exact threshold is
\[
q_* =\log\!\frac{7(1-e^{-1})}{7-6e^{-1/2}-e^{-1}}
=0.390979957597\ldots.
\]
Thus, the pure-pulse transition numerically observed near effort \(0.4\) is exactly located without optimizing a discretized control grid.

## Assumptions and scope
The disease-free susceptible state is the unique attracting \(T\)-periodic solution in the impulsive sense of
\[
dS=\delta(1-S)\,dt-S\,d\mu,
\]
where an atom of mass \(a\) multiplies \(S\) by \(e^{-a}\). This is a multiplicative *log-dose* convention: the fraction immediately removed at such a pulse is \(1-e^{-a}\). For smooth vaccination density, the equation is \(S'=\delta(1-S)-\eta(t)S\). The constraint is total measure mass \(\mu([0,T))=q\), not the fraction immunized at the pulse. Reproduction number differs from \(J\) by the positive factor \(1/[T(\gamma+\mu_d)]\) for constant infectious removal rate \(\gamma+\mu_d>0\); minimizing either is equivalent. The symbol \(\mu\) always means the vaccination measure, not demographic mortality.

The result applies to **all** admissible Borel measures, including singular-continuous and atomic policies, with fixed total mass. The unique optimizer for \(q=0\) is the zero measure. The pulse \(\delta_0\) is the periodic point at which transmission jumps from \(\beta_L\) to \(\beta_H\). Translating the time origin translates the optimal pulse.

## Proof
**1. Convex optimization and its marginal criterion.** For a fixed total mass \(q\), the periodic variation-of-constants formula writes the susceptible state at almost every phase as
\[
S_\mu(t)=\frac{\delta}{1-e^{-\delta T-q}}
\int_{t-T}^t e^{-\delta(t-u)-\mu((u,t])}\,du.
\]
The denominator is independent of the location of vaccination mass. Consequently \(J\) is convex in \(\mu\) on the fixed-mass set. It is strictly convex: for distinct measures, the intervening arc masses differ on a set of phase pairs of positive Lebesgue measure, and exponential is strictly convex. Thus a first-order optimality condition is both necessary and sufficient, with a unique minimizer.

For a reference measure with an atom at phase zero, define the forward marginal value \(G(t)=S(t)v(t)\) away from that atom, where \(v(t)\) is the positive periodic solution of the *backward adjoint* \(v'=\delta v-\beta(t)\) on the open seasons, with the adjoint jump \(v(T-)=e^{-q}v(0+)\). The product has the same limiting value on the two sides of the vaccination atom. Differentiation of the periodic integral formula, or equivalently sensitivity of the controlled linear equation, gives for a competitor \(\nu\) of the same mass
\[
DJ[q\delta_0](\nu-q\delta_0)=qG(0)-\int_{[0,T)}G(t)\,\nu(dt).
\]
Hence \(q\delta_0\) is optimal for \(q>0\) exactly when \(G(t)\leq G(0)\) at every phase. This condition explicitly considers every possible relocation of dose, not merely nearby smooth perturbations.

**2. Values for the pure pulse.** Write \(z=e^{-q}\). Immediately after the pulse, and over both open seasons,
\[
S(t)=1-Ce^{-\delta t},\qquad C=\frac{1-z}{1-zr},
\quad S(0+)=\frac{z(1-r)}{1-zr},\quad S(T-)=\frac{1-r}{1-zr}.
\]
Integrating the adjoint over a full period gives
\[
v(0+)=\frac{B}{\delta(1-zr)},\qquad v(T-)=zv(0+),
\quad G(0)=\frac{z(1-r)B}{\delta(1-zr)^2}.
\]
Inside either open season, differentiation and the state equations yield
\[
G'=\delta v-\beta S.
\]
Therefore the right derivative at the upward jump and the left derivative at the preceding low-season endpoint are
\[
G'(0+)=\frac{B-\beta_H z(1-r)}{1-zr},\qquad
G'(T-)=\frac{zB-\beta_L(1-r)}{1-zr}.
\]
If \(G(0)\) is the global maximum, necessarily \(G'(0+)\leq0\) and \(G'(T-)\geq0\). These are respectively
\[
z\geq\frac{B}{\beta_H(1-r)},\qquad
z\geq\frac{\beta_L(1-r)}{B}.
\]

**3. Endpoint conditions suffice globally.** During the high season the future-weighted adjoint is strictly smaller than \(\beta_H/\delta\) (because transmission is strictly lower for part of each future period), while \(0<S\leq1\). Hence
\[
G''=\delta^2v-2\delta\beta_H+\delta\beta_HS<0
\qquad(0<t<h).
\]
If \(G'(0+)\leq0\), the marginal value is strictly decreasing throughout the high season. During the low season,
\[
v(t)=\frac{\beta_L}{\delta}+D e^{\delta(t-T)},
\quad D=v(T-)-\frac{\beta_L}{\delta},
\]
and therefore
\[
G'(t)=\beta_L C e^{-\delta t}+\delta D e^{\delta(t-T)}.
\]
If \(D\geq0\), this derivative is nonnegative (and strictly positive for \(q>0\)). If \(D<0\), the derivative is strictly decreasing in time. Thus \(G'(T-)\geq0\) implies \(G'\geq0\) throughout the low season. Together the endpoint inequalities imply that \(G\) decreases through the high season and increases through the low season, attaining its global maximum only at phase zero. Convex first-order optimality yields the unique minimizer.

If either endpoint inequality fails, \(G\) exceeds \(G(0)\) just after or just before phase zero. Moving a sufficiently small quantity of vaccine mass to that phase strictly decreases \(J\). This proves necessity, sufficiency and sharpness. Taking logarithms proves the stated \(q_*\). Finally, comparing the two candidate thresholds gives the phase-selection criterion based on the sign of \(B^2-\beta_H\beta_L(1-r)^2\).

## Verification
The accompanying `verify.py` uses only the Python standard library. It recomputes the exact seasonal constants, integrates the susceptible equation exactly on every interval for two-pulse perturbations, checks that the finite-difference directional derivative agrees with \(G(0)-G(t)\), and exercises parameters on both sides of the high-side/low-side threshold classification. For the published square-wave example it returns \(q_*=0.390979957597\ldots\), \(q_H=0.390979957597\ldots\) and \(q_L=1.554930191458\ldots\). These finite computational checks are supplementary; the above convexity and strict derivative-sign arguments, not numerical sampling, prove the assertion for all admissible measures.

## Relationship to prior work
Gavish and Katriel (2026, *Optimal Vaccination for Contagious Diseases with Seasonal Transmission*, Sect. 7 and Eq. (29)) introduced the precise seasonal control problem, treated discontinuous transmission, and numerically observed that the optimizer for their square-wave example is a pure pulse when the annual mass is below approximately \(0.4\). They explicitly distinguish the numerical observation from their analytically derived conditions. The earlier Gavish–Katriel (*Optimal Regulation in a Time-Periodic Environment*, 2026, Sect. 2 and Sect. 4.1) proves existence, uniqueness and convex first-order criteria for a more general positive-measure optimization problem; those principles are used here rather than claimed as new. The novelty asserted here is the *exact necessary-and-sufficient scalar threshold for arbitrary two-season square waves*, including both directions of loss and the parameter inequality choosing between them. General theory by itself does not specify this closed-form cutoff. Related vaccination-timing results for vaccines targeting only susceptible individuals concern different control dynamics.

## Limitations
The theorem only characterizes whether the **entire** vaccination budget concentrated at the high-season onset is optimal. For budgets above the threshold it does not determine the full optimal measure, the surviving pulse mass, or any interior continuous-vaccination region. It concerns invasion linearization around a disease-free orbit, not nonlinear endemic prevalence, stochastic vaccine efficacy, limited administration rates or host heterogeneity. A Dirac dose is an idealization. A general convex optimality criterion was already known, so the contribution is a sharp square-wave resolution, not a new convexity theorem. Publication priority outside the inspected literature has not been independently certified.

## References
1. N. Gavish and G. Katriel, *Optimal Vaccination for Contagious Diseases with Seasonal Transmission*, Bulletin of Mathematical Biology **88**, article 170 (published 2026-09-02), DOI: 10.1007/s11538-026-01741-0, open full text: https://link.springer.com/article/10.1007/s11538-026-01741-0 . See Sections 2, 3, 7 (notably Eq. 29 and Fig. 9) and 9.
2. N. Gavish and G. Katriel, *Optimal Regulation in a Time-Periodic Environment: Insights from a Simple Model*, Applied Mathematics & Optimization **93**, article 22 (published 2026-01-10), DOI: 10.1007/s00245-025-10374-z, open full text: https://link.springer.com/article/10.1007/s00245-025-10374-z . See Sections 2, 3, 4.1 and 4.8.
