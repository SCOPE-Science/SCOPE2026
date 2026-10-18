# Opposite-sign survival correlations from a common reset clock

## Finding

For two independent Brownian searchers subject to the *same* independent Poisson reset clock, the covariance of their binary nonarrival indicators at a fixed observation time is always strictly positive when their target distances agree, yet is strictly **negative** for an explicit nonempty region of unequal starting distances and sufficiently weak positive reset rates. In particular the shared reset clock alone does not force positive association across heterogeneous searchers.

For any \(D,t>0\), distances \(d_1,d_2>0\) and rate \(r\ge0\), let \(S_i(t)=\mathbf{1}_{\{T_i>t\}}\). With
\[
Q_d(s)=\operatorname{erf}\!\left(\frac{d}{\sqrt{4Ds}}\right),\qquad
\Delta_d(u)=Q_d(u)Q_d(t-u)-Q_d(t),
\]
we prove the exact derivative
\[
\operatorname{Cov}(S_1(t),S_2(t))
=r\int_0^t\Delta_{d_1}(u)\Delta_{d_2}(u)\,du+O(r^2t^2)
\quad (r\downarrow0).
\]
For equal starting distances, covariance is strictly positive for every \(r>0\). Conversely, put
\[
c(d_2)=\operatorname{erfc}\!\left(\frac{\sqrt3\,d_2}{2\sqrt{Dt}}\right).
\]
If \(d_2^2\ge6Dt\) and
\[
0<d_1<\frac{\sqrt{Dt}}{3e\sqrt\pi}c(d_2)^2,
\]
then the displayed first-order coefficient is strictly negative. Consequently the covariance is strictly negative for every sufficiently small \(r>0\). The strict small-distance inequality is only a sufficient condition, not an asserted sharp threshold.

## Assumptions and scope

Two labeled independent real Brownian motions evolve on \((0,\infty)\), each with variance rate \(2D\), and are absorbed upon their first encounter with zero. They start at prescribed positive positions \(d_1,d_2\). A *single* rate-\(r\) Poisson clock independent of both Brownian noises simultaneously returns each still-searching particle to its own initial position. Arrivals are permanently recorded; later resets do not cancel a recorded first arrival. The clock continues exogenously after either arrival. We examine indicators of not having arrived by one fixed time \(t>0\). All claims hold for every \(D,t>0\) with the stated distance and rate qualifications. No assertion about covariance of the unbounded first-passage times is made.

## Proof

**1. Conditional survival and expansion.** Let \({\cal C}\) be the common Poisson event times up to \(t\), with successive gap lengths \(\ell_1,\ldots,\ell_{m+1}\) summing to \(t\). Brownian independence, the strong Markov property and independent fresh increments give
\[
q_d({\cal C})=\Pr(T_d>t\mid{\cal C})=\prod_{j=1}^{m+1}Q_d(\ell_j).
\]
Given \({\cal C}\), the two survival indicators are independent, so their covariance is \(\operatorname{Cov}_{\cal C}(q_{d_1}({\cal C}),q_{d_2}({\cal C}))\). Zero Poisson events have probability \(e^{-rt}\); exactly one in \((u,u+du)\) has probability \(r e^{-rt}du\); at least two events have probability at most \((rt)^2/2\). Since all conditional survival probabilities lie in \([0,1]\), expanding their first and second moments and subtracting their product proves the stated coefficient, with an \(O(r^2t^2)\) remainder for fixed \(D,t,d_1,d_2\).

**2. Identical distances.** When \(d_1=d_2=d\), the clock covariance equals \(\operatorname{Var}_{\cal C}(q_d({\cal C}))\). This variance is strictly positive for every \(r>0\): the no-event history has value \(Q_d(t)\), while a one-event history near \(u=0\) has value \(Q_d(u)Q_d(t-u)>Q_d(t)\). The last inequality for small \(u>0\) follows from \(Q_d'(t)<0\) and \(1-Q_d(u)=\operatorname{erfc}(d/\sqrt{4Du})=o(u)\). Both histories have positive Poisson probabilities.

**3. The far target gains survival under one reset.** Write \(F_d(s)=1-Q_d(s)=\operatorname{erfc}(d/\sqrt{4Ds})\), extended by \(F_d(0)=0\). Direct differentiation gives
\[
F_d''(s)=\frac{d e^{-d^2/(4Ds)}}{2\sqrt{\pi D}\,s^{5/2}}
\left(\frac{d^2}{4Ds}-\frac32\right).
\]
If \(d_2^2\ge6Dt\), this is nonnegative for every \(0<s\le t\); hence convexity and \(F_{d_2}(0)=0\) imply \(F_{d_2}(u)+F_{d_2}(t-u)\le F_{d_2}(t)\). Therefore
\[
\Delta_{d_2}(u)=F_{d_2}(t)-F_{d_2}(u)-F_{d_2}(t-u)+F_{d_2}(u)F_{d_2}(t-u)>0
\]
for \(0<u<t\). Set \(I_2=\int_0^t\Delta_{d_2}(u)\,du\). Since \(F_{d_2}\) increases, restricting to \(t/3\le u\le2t/3\) yields
\[
I_2\ge \frac t3 F_{d_2}(t/3)^2=\frac t3 c(d_2)^2>0.
\]

**4. The near target loses survival and dominates the covariance coefficient.** The elementary error-function bound \(Q_{d_1}(s)\le d_1/\sqrt{\pi Ds}\) gives
\[
\int_0^tQ_{d_1}(u)Q_{d_1}(t-u)\,du
\le\frac{d_1^2}{\pi D}\int_0^t\frac{du}{\sqrt{u(t-u)}}=\frac{d_1^2}{D}.
\]
The assumed bound on \(d_1\) implies \(d_1<2\sqrt{Dt}\), so \(z=d_1/(2\sqrt{Dt})<1\). Thus \(Q_{d_1}(t)=\operatorname{erf}(z)\ge(2ze^{-1})/\sqrt\pi=d_1/(e\sqrt{\pi Dt})\). Also \(0<\Delta_{d_2}(u)\le1\). Hence the weak-rate covariance coefficient \(J\) satisfies
\[
\begin{aligned}
J&=\int_0^tQ_{d_1}(u)Q_{d_1}(t-u)\Delta_{d_2}(u)\,du-Q_{d_1}(t)I_2\\
&\le \frac{d_1^2}{D}-\frac{d_1}{e\sqrt{\pi Dt}}\,\frac t3 c(d_2)^2<0.
\end{aligned}
\]
Because \(J<0\), the exact first-order expansion implies strictly negative covariance for all sufficiently small strictly positive \(r\). This completes both sign statements.

## Verification

The proof is analytical: it uses the absorbing Brownian reflection formula, Poisson conditioning, a second derivative/convexity identity and elementary integral bounds. Run `python CHECK.py` (Python standard library only) to independently calculate the integrand and its weak-rate coefficient for a representative heterogeneous pair, and to check the derivative signs and the stated integral bound. Its numerical outputs are illustrations, not a certificate of all continuous parameter values. The proof establishes the latter.

## Relationship to prior work

Vatash, Goldfarb, Rudyak and Roichman (arXiv:2609.23542v1, first posted 2026-09-20) derive rank-dependent optimum reset rates and note that a global Poisson clock creates correlations, while discussing heterogeneous starting distances. They do not identify the negative fixed-time survival-indicator covariance established here. Biroli, Majumdar and Schehr (arXiv:2303.18012, 2023) analyze an identical-distance global-reset first-arrival observable, not the sign of fixed-time cross-survival dependence with unequal distances. Their earlier Brownian-gas work concerns reset-induced spatial correlations. An earlier exact same-distance first-passage-time covariance result does not imply the current sign statement, since hitting-time covariance and fixed-time indicator covariance are different observables. This note does not claim novelty for the conditional-independence observation itself, the reflection principle, or known reset renewal formulas.

## Limitations

The explicit unequal-distance inequality is sufficient and potentially very conservative. The claim guarantees negative covariance only for all sufficiently small common reset rates and does not determine the sharp distance/rate sign boundary. The proof applies to ideal instantaneous simultaneous Poisson resetting and independent Brownian noises with a common absorbing target. It does not show a negative covariance of the full hitting times, and it makes no statement about interactions, global resetting stopped after first arrival, non-Poisson clocks or higher dimensions. Potential implicit coverage by general shared-environment dependence results remains an originality risk.

## References

- R. Vatash, E. Goldfarb, V. Yu. Rudyak, and Y. Roichman, *Rank-dependent optimal resetting in multiparticle search*, arXiv:2609.23542v1 (first public 2026-09-20), https://arxiv.org/abs/2609.23542.
- M. Biroli, S. N. Majumdar, and G. Schehr, *Critical number of walkers for diffusive search processes with resetting*, arXiv:2303.18012, https://arxiv.org/abs/2303.18012.
- M. Biroli, H. Larralde, S. N. Majumdar, and G. Schehr, *Extreme Statistics and Spacing Distribution in a Brownian Gas Correlated by Resetting*, Phys. Rev. Lett. 130, 207101 (2023), DOI:10.1103/PhysRevLett.130.207101.
