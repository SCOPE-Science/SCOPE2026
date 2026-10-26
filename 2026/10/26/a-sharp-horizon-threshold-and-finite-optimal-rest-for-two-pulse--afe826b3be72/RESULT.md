# A sharp horizon threshold and finite optimal rest for two-pulse Horton infiltration

## Finding

Consider a soil whose infiltrability declines exponentially during an excess-rain interval and recovers exponentially while dry. When at most two rain-on intervals can be separated by one rain-off interval within a fixed horizon, **the optimum is governed by a sharp horizon threshold**. For any prescribed positive dry interval, the two wet intervals must have equal length. Below the threshold, uninterrupted wetting is optimal; above it, a uniquely optimal positive rest occurs, increases with the horizon, and converges to a finite, explicitly determined duration.

Let \(f_c,A,k,h,T>0\). Write \(f_{\max}=f_c+A\), \(r=h/k\), and \(\eta=f_c/A\). For any wet–dry–wet schedule \((t_1,\delta,t_2)\) with nonnegative durations and \(t_1+\delta+t_2=T\), let \(U\) denote total infiltration under the dynamics described below.

**Theorem.** If \(\delta>0\) and \(\delta<T\), the unique maximizing allocation at that fixed gap is \(t_1=t_2=(T-\delta)/2\). The corresponding total infiltration equals
\[
G_T(\delta)=f_c(T-\delta)+\frac{A}{k}\left[2(1-z)-b(1-z)^2\right],\qquad z=e^{-k(T-\delta)/2},\quad b=e^{-h\delta}.
\]
For every \(T>0\), \(G_T\) is strictly concave on \([0,T]\). If \(r\leq\eta\), uninterrupted wetting is globally optimal for all horizons. If \(r>\eta\), define
\[
z_c=\frac{r-\eta}{r+\sqrt{r+(r-1)\eta}},\qquad T_c=\frac{2}{k}\log\frac{1}{z_c}.
\]
For \(0<T\leq T_c\), the unique time allocation is uninterrupted wetting, up to a zero-duration rest. For \(T>T_c\), the unique optimizer has a positive dry interval \(\delta_*(T)\in(0,T)\) and equal positive wet intervals. Its dry interval is the unique solution of
\[
\eta+z=e^{-h\delta}\left[z(1-z)+r(1-z)^2\right],\qquad z=e^{-k(T-\delta)/2}.
\]
In the second regime, \(\delta_*(T)\) increases strictly with \(T\), satisfies
\[
0<\delta_*(T)<\delta_\infty:=\frac{1}{h}\log\frac{r}{\eta},
\qquad \lim_{T\to\infty}\delta_*(T)=\delta_\infty,
\]
and emerges linearly at the critical horizon:
\[
\delta_*(T)=C(T-T_c)+o(T-T_c)\quad\text{as }T\downarrow T_c,
\]
where, with \(B_c=z_c(1-z_c)+r(1-z_c)^2\),
\[
C=\frac{z_c[z_c+r(1-z_c)]}{z_c[z_c+r(1-z_c)]+rB_c}\in(0,1).
\]
The restricted two-pulse model is essential: this is not an optimality theorem over arbitrarily many on/off cycles.

## Assumptions and scope

Initially, infiltration capacity \(f\) is fully recovered at \(f(0)=f_{\max}\). During each wet interval, an available rainfall supply of at least \(f_{\max}\) keeps actual infiltration equal to capacity and obeys \(\dot f=-k(f-f_c)\). During the single dry interval, zero rainfall and zero infiltration are assumed, and capacity obeys \(\dot f=h(f_{\max}-f)\). All capacity trajectories are continuous at switching times. Excess incident water during wetting runs off and is removed before the dry interval; no ponded storage is carried across the gap. The horizon is fixed, and schedules are restricted to a single consecutive wet–dry–wet sequence (degenerate zero-length periods are permitted). There is no upper cap on total soil infiltration, no additional evaporation or water-budget restriction, and no dependence of \(k\) or \(h\) on state.

The outcome \(U\) is cumulative infiltrated depth by time \(T\), not agronomic water-use efficiency, crop response, runoff minimization for a fixed delivered dose, or a claim about all physical soils. In particular, fixed supplied-water constraints are absent: the wet supply remains capacity-saturating.

## Proof

**1. Compose the wet and dry flows.** Set \(a=e^{-kt_1}\), \(c=e^{-kt_2}\), and \(b=e^{-h\delta}\). The first wet interval starts with excess capacity \(A\), ends with excess \(Aa\), and contributes excess infiltrated depth \(A(1-a)/k\). During the rest, excess capacity recovers to \(A[1-b(1-a)]\). The second wet interval contributes excess depth \(A[1-b(1-a)](1-c)/k\). Therefore
\[
\frac{k}{A}\bigl[U-f_c(t_1+t_2)\bigr]
=(1-a)+[1-b(1-a)](1-c)
=2-b-bac-(1-b)(a+c).
\]
At fixed \(\delta\), the product \(ac=e^{-k(T-\delta)}\) is fixed. For \(0<\delta<T\), \(1-b>0\), and the strict arithmetic-geometric mean inequality \(a+c\geq2\sqrt{ac}\) proves unique maximization at \(a=c\), equivalently \(t_1=t_2\). When \(\delta=0\), the wet intervals concatenate and every split is the same physical uninterrupted wetting schedule. When \(\delta=T\), uptake is zero. Substitution at the optimal split gives the displayed \(G_T\).

**2. Prove strict gap concavity.** Put \(z=e^{-k(T-\delta)/2}\), \(b=e^{-h\delta}\), and \(B(z)=z(1-z)+r(1-z)^2\). Direct differentiation, with \(z'=kz/2\) and \(b'=-hb\), gives
\[
G_T'(\delta)=A[-\eta-z+bB(z)],
\]
\[
G_T''(\delta)=-A\left[\frac{kz}{2}(1-bB_z(z))+hbB(z)\right],
\qquad B_z(z)=1-2z-2r(1-z).
\]
For \(0<z\leq1\) and \(0<b\leq1\), \(B_z(z)<1\), so \(1-bB_z(z)>0\). Also \(B(z)\geq0\), with equality only at \(z=1\). Hence \(G_T''<0\) throughout the closed feasible interval, including the endpoints interpreted one-sidedly. At \(\delta=T\), one has \(z=1\), so \(G_T'(T)=-f_c-A<0\). Consequently the unique maximizing gap is \(0\) if \(G_T'(0)\leq0\), and otherwise the unique interior zero of \(G_T'\).

**3. Identify the horizon threshold.** At \(\delta=0\), set \(z_0=e^{-kT/2}\). The derivative simplifies to
\[
\frac{G_T'(0)}{A}=r(1-z_0)^2-z_0^2-\eta.
\]
The right side is strictly decreasing as a function of \(z_0\in(0,1)\) because its derivative is \(-2r(1-z_0)-2z_0<0\). As the horizon increases, it rises continuously from \(-1-\eta\) to \(r-\eta\). Thus it never becomes positive when \(r\leq\eta\), and crosses zero exactly once when \(r>\eta\). Solving the quadratic and rationalizing its physically admissible root yields the stated \(z_c\in(0,1)\), and hence \(T_c\). Strict concavity supplies the claimed global decisions, including equality at \(T=T_c\).

**4. Monotonicity, bounded saturation, and onset.** At fixed \(\delta\), differentiating with respect to the horizon gives
\[
\partial_T G_T'(\delta)=\frac{Akz}{2}[1-bB_z(z)]>0.
\]
Since \(G_T'\) is strictly decreasing in \(\delta\), its unique zero shifts strictly to the right as \(T\) grows above \(T_c\). At that zero, \(\eta+z=bB(z)\); moreover \(B(z)-z=r(1-z)^2-z^2<r\). Therefore \(\eta=bB(z)-z\leq b(B(z)-z)<b r\), proving \(\delta_*<h^{-1}\log(r/\eta)\). The increasing, bounded optimal gap has a limit \(L\). Taking the limit of its derivative-zero equation as \(T\to\infty\) gives \(\eta=r e^{-hL}\), whence \(L=\delta_\infty\).

At \((T_c,0)\), the derivative-zero equation is nondegenerate because \(G_{T_c}''(0)<0\). Implicit differentiation provides the positive one-sided branch and
\[
\left.\frac{d\delta_*}{dT}\right|_{T_c+}
=\frac{\partial_TG_T'}{-\partial_\delta G_T'}\bigg|_{(T_c,0)}
=\frac{z_c[z_c+r(1-z_c)]}{z_c[z_c+r(1-z_c)]+rB_c}.
\]
Both numerator and the additional denominator term are positive, so the coefficient lies strictly between zero and one. This proves the onset law and completes the theorem.

**Exact benchmark.** For \(k=h=f_c=1\), \(A=8\), and \(T=\log32\), one has \(r=1\), \(\eta=1/8\), \(z_c=7/16\), and \(T_c=2\log(16/7)\). The unique optimal rest solves the derivative equation at \(b=1/2\), \(z=1/4\), yielding \(\delta_*=\log2\) and \(t_1=t_2=\log4\). Exact depths are
\[
U_{\max}=\log16+\frac{39}{4},\qquad
U_{\mathrm{continuous}}=\log32+\frac{31}{4},\qquad
U_{\max}-U_{\mathrm{continuous}}=2-\log2>0.
\]
Here \(\delta_\infty=\log8\).

## Verification

The standalone `verify.py` requires Python 3 and its standard library only. Run `python3 verify.py` alongside this document. In one reproducible run it passed 3,000 independent fixed-gap allocation checks, 3,000 concavity evaluations, 3,000 comparisons with 52 trial gaps apiece, 120 independent Simpson quadratures of the two wet integrals, 800 centered finite-difference comparisons of the derived gap derivative, and exact logarithmic benchmark checks. It also checked the horizon threshold, increasing optimal gap, finite limiting gap and one-sided onset coefficient. The checks use a fixed pseudorandom seed and are supporting numerical diagnostics, not proofs for the continuous parameter domain; the universal claims are established by the preceding algebra and inequalities.

## Relationship to prior work

The exponential wet infiltration law originates in Horton's infiltration-capacity research. The corresponding drying/rest recovery prescription is also described in the SWMM infiltration manual; both modeling ingredients are established, not discoveries of this theorem. Gencoglan and collaborators (2005) analyze ponding times and cycle counts for sprinkler irrigation under Horton and Kostiakov responses; their openly available full manuscript treats a fixed water dose and runoff avoidance, not maximum cumulative infiltration by a fixed clock horizon when a single recovery rest has freely chosen length. Karmeli and Peri (1974) present pulse irrigation principles and cycle-design procedures. Dadhich, Singh and Mahar (2012) compare variable versus constant sprinkler application rates and report time savings for a prescribed dose; the accessible abstract does not settle the present theorem, but the full manuscript was not available for exclusion of all possible overlap. Assouline (2019) studies irrigation rate and duration design based on infiltration capacity for water-use efficiency; its accessible full text does not derive the joint two-pulse optimality threshold. James and Larson (1976) model intermittent infiltration and soil-water redistribution, a more physical model with a different state description; accessible abstract-level evidence is insufficient to rule out every related result.

The contribution claimed here is specifically the simultaneous *equal-pulse allocation, strict one-gap concavity, if-and-only-if horizon cutoff, monotone unique recovery rest, finite saturation and critical onset* for the explicit switched exponential-capacity model. Generic optimal-control or rearrangement methods may provide related machinery; no discovery of the Horton law, dry recovery formula or general pulse-irrigation concept is asserted.

## Limitations

This theorem optimizes **at most two wet intervals and exactly one possible internal dry interval**. Introducing three or more wet intervals changes the feasible class and may improve uptake. The continuous-time empirical capacity model assumes exponential recovery independent of moisture history; real soil infiltration also depends on unsaturated profiles, heterogeneity, runoff storage, and water availability. The formulation allows excess rainfall to run off, while other irrigation designs minimize runoff and constrain the delivered water volume. The exact cutoff cannot be transferred to those different objectives or richer infiltration models without new analysis. Originality remains subject to specialized historical literature and inaccessible potentially relevant full texts; a negative search result is not proof of priority.

## References

1. Horton, R. E. (1941). "An Approach Toward a Physical Interpretation of Infiltration-Capacity." *Soil Science Society of America Journal*. DOI: 10.2136/sssaj1941.036159950005000C0075x. Publisher records first public date 1941-01-01.
2. *OpenSWMM Engine: Chapter 4 — Infiltration*, §§4.2.1–4.2.2 (Horton wet decline and dry recovery). https://www.hydrocouple.org/openswmm.engine/d9/de6/hydrology_ref_ch4_infiltration.html
3. Gençoğlan, C., Gençoğlan, S., Merdun, H., and Uçan, K. (2005). "Determination of ponding time and number of on–off cycles for sprinkler irrigation applications." *Agricultural Water Management* 72, 47–58. DOI: 10.1016/j.agwat.2004.08.001.
4. Karmeli, D., and Peri, G. (1974). "Basic Principles of Pulse Irrigation." *Journal of the Irrigation and Drainage Division* 100, 309–319. DOI: 10.1061/JRCEA4.0000988.
5. James, L. G., and Larson, C. L. (1976). "Modeling Infiltration and Redistribution of Soil Water During Intermittent Application." *Transactions of the ASAE* 19, 482–488. DOI: 10.13031/2013.36054.
6. Dadhich, S. M., Singh, R. P., and Mahar, P. S. (2012). "Saving Time in Sprinkler Irrigation Application through Cyclic Operation: A Theoretical Approach." *Irrigation and Drainage* 61, 631–635. DOI: 10.1002/ird.1674.
7. Assouline, S. (2019). "A Simple Method to Design Irrigation Rate and Duration and Improve Water Use Efficiency." *Water Resources Research*. DOI: 10.1029/2019WR025221.
