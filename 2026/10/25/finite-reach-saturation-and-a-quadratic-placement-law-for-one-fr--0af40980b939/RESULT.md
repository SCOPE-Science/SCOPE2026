# Finite-reach saturation and a quadratic placement law for one fractional river aerator

## Finding

For the classical linear Streeter–Phelps oxygen-deficit model with zero initial deficit, consider exactly one instantaneous aerator that removes a fixed fraction of the local deficit. Among all installation positions along a reach of travel time \(T>0\), there is exactly one that minimizes the largest deficit over the reach. A critical reach length \(T_c\) determines whether the downstream endpoint or a genuine downstream oxygen-sag minimum is the active constraint. The optimal location is strictly increasing with \(T\) below \(T_c\) and becomes exactly independent of \(T\) at and above \(T_c\). As \(T\uparrow T_c\), its remaining displacement from that stable location vanishes quadratically, not linearly.

More precisely, write \(a,b\) for positive deoxygenation and reaeration rates with \(0<a<b\), \(L_0>0\) for initial biochemical oxygen demand, and \(q\in(0,1)\) for the fraction of oxygen deficit remaining immediately after aeration. Put
\[
C=\frac{aL_0}{b-a},\quad
g(t)=C(e^{-at}-e^{-bt}),\quad
t_0=\frac{\log(b/a)}{b-a},\quad
A(s)=q+(1-q)e^{(b-a)s}.
\]
Let \(M_0=g(t_0)\), \(m(s)=M_0 A(s)^{-a/(b-a)}\), and
\[
h(s)=t_0+\frac{\log A(s)}{b-a}.
\]
There exists exactly one \(s_\infty\in(0,t_0)\) such that \(g(s_\infty)=m(s_\infty)\). Define \(T_c=h(s_\infty)>t_0\) and \(J=g'(s_\infty)-m'(s_\infty)>0\).

For every \(T>0\), the unique optimal site \(s_T\) belongs to \((0,\min\{T,t_0\})\). If \(0<T<T_c\), it is the unique solution in that interval to
\[
 g(s_T)\left[1+(1-q)e^{-b(T-s_T)}\right]=g(T),
\]
and it satisfies \(T<h(s_T)\). If \(T\ge T_c\), then \(s_T=s_\infty\). Its optimal worst-case deficit is always \(g(s_T)\), and \(s_T\) is strictly increasing in \(T\) on \((0,T_c)\). Moreover,
\[
\lim_{T\downarrow0}\frac{s_T}{T}=\frac1{2-q},\qquad
\lim_{T\downarrow0}\frac{g(s_T)}{aL_0T}=\frac1{2-q},
\]
while the approach to the placement plateau is
\[
\boxed{\ s_\infty-s_T=
\frac{ab\,g(s_\infty)}{2J}(T_c-T)^2
+o\big((T_c-T)^2\big)\quad(T\uparrow T_c).\ }
\]
All minimizers are unique as positions in the closed interval \([0,T]\). No assertion is made for more than one aerator or for a placement-dependent aerator efficiency.

## Assumptions and scope

The river is represented by a one-dimensional steady advective reach with travel time \(t\), constant rate coefficients, no sediment oxygen demand or photosynthesis term, and initial oxygen deficit \(D(0)=0\). The biochemical oxygen demand is \(L(t)=L_0e^{-at}\) and the deficit satisfies \(D'(t)=aL(t)-bD(t)\) between interventions. The aerator at \(s\in[0,T]\) changes \(D(s^-)\) instantaneously to \(D(s^+)=qD(s^-)\), without changing \(L\). The objective is \(R_T(s)=\sup_{0\le t\le T}D_s(t)\), taking the one-sided upstream limit at the discontinuity. Units of \(T,s,a^{-1},b^{-1}\) are travel time; position in physical distance is obtained with the river's advection relation. The positivity and ordering \(0<a<b\), \(L_0>0\), \(0<q<1\) are essential to the stated formulas and uniqueness proof.

## Proof

**1. Response on either side of the site.** Direct integration gives \(D_s(t)=g(t)\) for \(0\le t<s\) and
\[
D_s(t)=g(t)-(1-q)g(s)e^{-b(t-s)}
=C\left(e^{-at}-A(s)e^{-bt}\right),\qquad t\ge s.
\]
The unmodified curve \(g\) increases strictly until \(t_0\) and then decreases, with maximum \(M_0\). Differentiation of the post-aeration branch shows its formal unconstrained maximum occurs at \(h(s)\), with value \(m(s)\). Here \(A(s)>1\) for \(s>0\), so \(h(s)>t_0\), and \(m(s)\) is strictly decreasing on \((0,\infty)\).

**2. Monotone balance gives the unique global minimizer.** Fix \(T\). For \(0<s<\min\{T,t_0\}\), the largest pre-aeration deficit is exactly \(g(s)\), which strictly increases in \(s\). The largest post-aeration deficit is \(Q_T(s)=D_s(\min\{T,h(s)\})\). This quantity strictly decreases with \(s\): if \(0<s_1<s_2<\min\{T,t_0\}\), then for every \(t\ge s_2\),
\[
D_{s_2}(t)-D_{s_1}(t)
=-(1-q)C\left(e^{(b-a)s_2}-e^{(b-a)s_1}\right)e^{-bt}<0.
\]
Furthermore \(D_{s_1}(t)\) increases on \([s_1,s_2]\), because \(h(s_1)>t_0>s_2\). Hence its post-aeration maximum is attained at \(t\ge s_2\); strict decrease follows also for the maxima. The crossing \(g(s)=Q_T(s)\) exists and is unique: near \(s=0\), \(g(s)\to0<Q_T(0)\); at \(s=\min\{T,t_0\}\), either the post-aeration interval is empty (\(T\le t_0\)) or the pre-aeration maximum \(M_0\) strictly exceeds its downstream counterpart (\(T>t_0\)). Positions \(s\ge t_0\), when available, have upstream risk at least \(M_0\), whereas an interior aerator gives strictly less than \(M_0\). Consequently the crossing is the unique global optimum of \(\max\{g(s),Q_T(s)\}\).

**3. Saturation threshold.** Since \(g\) strictly increases on \((0,t_0)\) and \(m\) strictly decreases, the equation \(g(s)=m(s)\) has exactly one solution \(s_\infty\in(0,t_0)\). Because the post-aeration peak is later than \(t_0\), \(T_c=h(s_\infty)>t_0\). If \(T\ge T_c\), the downstream maximum at \(s_\infty\) is \(m(s_\infty)=g(s_\infty)\). Every site to its left has full post-aeration peak at least as high (its own peak occurs before \(T_c\)), and every site to its right has larger upstream maximum. Thus \(s_T=s_\infty\). For \(T<T_c\), the site \(s_\infty\) has risk \(g(s_\infty)\), with its downstream maximum strictly lower. A sufficiently small upstream shift decreases the risk, so \(s_T<s_\infty\). At the unique balancing site \(g(s_T)<m(s_T)\). Therefore its downstream constrained maximum must occur at \(T<h(s_T)\); substituting the exact post-aeration branch gives the stated scalar equation. Differentiation of \(g(s)-D_s(T)=0\) shows \(s_T\) strictly increases with \(T\): its derivative with respect to \(s\) is positive, while the derivative with respect to \(T\) is \(-D_s'(T)<0\) because \(T<h(s_T)\).

**4. Short and near-critical reaches.** Uniform Taylor expansions for \(0\le s\le T\to0\) give \(g(s)=aL_0s+O(T^2)\) and \(D_s(T)=aL_0[T-(1-q)s]+O(T^2)\). Equating yields both short-reach limits. At the unconstrained downstream maximum, direct differentiation of the exponential curve gives the exact curvature identity \(D_s''(h(s))=-ab\,m(s)\). Let \(\varepsilon=T_c-T\downarrow0\). Monotonicity and the balance established above imply \(s_T\to s_\infty\). As \(g(s_T)=D_{s_T}(T)\) and \(g(s)-m(s)=J(s-s_\infty)+O((s-s_\infty)^2)\), Taylor expansion around the moving maximum yields
\[
 J(s_T-s_\infty)+O((s_T-s_\infty)^2)
=-\frac{ab\,m(s_T)}2\left[T-h(s_T)\right]^2
+O\left(|T-h(s_T)|^3\right).
\]
Since \(h\) is continuously differentiable near \(s_\infty\), the displayed equality first gives \(s_T-s_\infty=O(\varepsilon^2)\) (use a local bound and absorb the mixed and quadratic terms); hence \(T-h(s_T)=-\varepsilon+O(\varepsilon^2)\). Division by \(\varepsilon^2\) proves the claimed sharp coefficient.

## Verification

For \(a=1\), \(b=2\), \(L_0=1\), and \(q=1/2\), the balancing equation has the exact solution
\[
s_\infty=\log\sqrt2,\qquad
T_c=\log(1+\sqrt2),\qquad
g(s_\infty)=\frac{\sqrt2-1}{2}.
\]
The quadratic coefficient is exactly \(1/2\); for \(T=0.5\) the numerical root is \(s_T\approx0.27156565\) and the optimal deficit is approximately \(0.18125890\). Run `python3 CHECK.py` using Python 3's standard library. It checks this exact example, the small-reach and quadratic limits, and 200 randomized instances against 101 equally spaced alternative placements. The finite computations are numerical cross-checks, not a proof of global optimality; the above monotonic balance is the proof.

## Relationship to prior work

The differential equations and the classic sag curve originate with Streeter and Phelps, *A Study of the Pollution and Natural Purification of the Ohio River*, U.S. Public Health Bulletin 146 (1925). Rinaldi and Soncini-Sessa, *Optimal Allocation of Artificial In-Stream Aeration*, RR-77-007 (1977), analyze aerator costs and continuous oxygen-standard constraints using general in-stream impulses, prove a cost-optimal device-position condition (Property A) and outline dynamic programming for discrete sites. Their qualitative insight that optimal aeration can be governed by limiting upstream/downstream oxygen levels is relevant to the balancing argument here. They do **not** formulate this fixed-fraction, exactly one-device, finite-horizon minimax objective, nor state the explicit reach-length cutoff or quadratic approach-to-plateau coefficient in their inspected analysis. These claims should not be interpreted as a new principle of equalizing extrema in general optimal control. The inaccessible Koivo–Phillips 1975 paper on optimization of dissolved oxygen with in-stream aeration is a residual originality risk, as are general minimax impulse-placement results with different terminology.

## Limitations

The claim concerns the idealized two-rate model only: the deficit reset proportion \(q\) is independent of position, a fully mixed water parcel is assumed, no oxygen saturation upper-bound violation is modeled, flow is constant and no biological feedback or cost optimization is included. The result does not identify the best number, size or cost of aerators, and is not a field-calibrated engineering recommendation. The original 1925 Bulletin is labelled February 1925 but does not verify a particular day of first release; the cited public federal catalog entry dated 1925-04-01 supplies a conservative day-specific public-source record, not a claim that the Bulletin itself was first published on April 1. The paper by Koivo and Phillips (1975) could not be fully read; its title is very close, and equivalent special-case coverage remains possible. Independent validation has not been performed.

## References

1. H. W. Streeter and E. B. Phelps (1925), *A Study of the Pollution and Natural Purification of the Ohio River*, U.S. Public Health Bulletin No. 146 (marked February 1925). Original scan: https://udspace.udel.edu/server/api/core/bitstreams/6f57c427-5f4f-4435-9d8c-87e3c8c02a66/content . Public dated catalog record: https://mocat.library.unt.edu/catalog/364-ch798 (April 1, 1925).
2. S. Rinaldi and R. Soncini-Sessa (1977), *Optimal Allocation of Artificial In-Stream Aeration*, IIASA RR-77-007, https://pure.iiasa.ac.at/708/1/RR-77-007.pdf . Especially pp. 7–19, Property A and the dynamic-programming section.
3. A. J. Koivo and G. Phillips (1975), *Optimization of Dissolved Oxygen Concentration in Polluted Streams Using Instream Aeration*, IFAC Sixth Triennial World Congress, https://www.sciencedirect.com/science/article/pii/S1474667017675906 . Relevant plausible prior paper; only bibliographic/secondary descriptions could be checked.
4. V. Gourishankar and R. L. Lawson (1975), *Optimal control of water pollution in a river stream*, *International Journal of Systems Science* 6(3), 201–216, https://doi.org/10.1080/00207727508941809 . Abstract on multiobjective pollutant load and artificial aeration control.
