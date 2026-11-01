# Sharp four-window switching and a two-cycle fold in the Abel equation

## Finding

For the nonautonomous Abel equation
\[
\dot x=A(t)x^3+B(t)x^2,\qquad x>0,
\]
with period four and a cyclic sequence of four **pure** monomial windows, two positive isolated periodic solutions are possible, but never more than two. Four is the least possible number of such windows: with at most three windows, there is at most one positive isolated periodic solution. This statement allows arbitrary real pulse strengths and durations and counts distinct isolated solutions rather than their multiplicities.

The upper bound is attained by the four unit-length windows with successive nonzero coefficients
\[
(B,A,B,A)=(-1,-5,2,d),\qquad d\geq0.
\]
More explicitly, on successive windows \([0,1),[1,2),[2,3),[3,4)\), take respectively \((A,B)=(0,-1),(-5,0),(0,2),(d,0)\), extended four-periodically. Set
\[
 d_{\infty}=\frac{15-4\sqrt{11}}2,\qquad
 d_{\mathrm f}=\frac{13-2\sqrt{30}}2,
 \qquad 0<d_{\infty}<d_{\mathrm f}.
\]
The number of **finite, positive, isolated** four-periodic solutions is exactly one when \(0\le d\le d_{\infty}\), exactly two when \(d_{\infty}<d<d_{\mathrm f}\), one double (nonhyperbolic) solution when \(d=d_{\mathrm f}\), and zero when \(d>d_{\mathrm f}\). At \(d=d_{\infty}\), the additional branch reaches reciprocal coordinate zero, corresponding to infinite physical amplitude, not a finite periodic solution. At \(d=d_{\mathrm f}\) the two branches merge in a nondegenerate saddle-node.

For \(d_{\infty}<d<d_{\mathrm f}\), the smaller positive reciprocal initial value is repelling and the larger one is attracting. At \(d=1\), these reciprocal initial values are exactly \(1/2\) and \(7/6\), corresponding to original initial values \(2\) and \(6/7\), with respective Floquet multipliers \(9/7\) and \(143/161\). The two hyperbolic cycles persist under sufficiently small smooth time-periodic coefficient perturbations, although the universal two-cycle upper bound is asserted only for the exact pulse class.

## Assumptions and scope

A pure monomial window is an interval of finite positive duration on which precisely one coefficient in \(A(t)x^3+B(t)x^2\) may be nonzero and is constant; zero-strength windows may be removed. Endpoints are interpreted in the usual Carathéodory sense. The coefficient pair repeats periodically, and a periodic solution is a positive solution that stays finite over every period and returns to its initial value. Floquet multipliers are derivatives of the scalar Poincaré return, invariant under the smooth reciprocal change of coordinates on \(x>0\). Window count refers to the cyclically reduced number of consecutive pure-monomial intervals, not the number of equal subdivisions of a constant-coefficient interval.

## Proof

**One-window flows.** Put \(y=1/x\). A quadratic pulse of integrated strength \(b\) has the return \(Q_b(y)=y-b\); a cubic pulse of integrated strength \(a\) has \(C_a(y)=\sqrt{y^2-2a}\). These expressions are restricted to positive arguments and positive resulting states. The corresponding intermediate trajectories remain positive precisely on the physical domain of the full pulse. All such maps are strictly increasing diffeomorphisms between their positive-domain intervals.

**Universal four-window bound.** If a cyclic four-window word has two neighboring windows of the same type, including across the period boundary, merge them (integrated strengths add). Cyclic changes of the return section conjugate the return on neighborhoods of periodic solutions and preserve isolated-periodic-solution counts. It therefore suffices to consider the alternating word \(Q_b,C_a,Q_c,C_d\), with return
\[
 P(y)=\sqrt{\bigl(\sqrt{(y-b)^2-2a}-c\bigr)^2-2d}.
\]
Let \(s=\sqrt{(y-b)^2-2a}>0\). On any positive fixed point, comparison of the squared return with \(y^2\) gives
\[
 2cs=-2by+b^2-2a+c^2-2d. \tag{1}
\]
If \(c\ne0\), write \(k=(b^2-2a+c^2-2d)/(2c)\). Every positive fixed point solves
\[
 \left(k-\frac bc y\right)^2-\bigl((y-b)^2-2a\bigr)=0.\tag{2}
\]
This is a polynomial of degree at most two. If it is not identically zero, there are at most two candidate positive fixed points; squaring can add extraneous roots, never remove the upper bound. If it vanishes identically, then at any genuine fixed point the branch signs of all radicals are strict and remain unchanged on a neighborhood. Equation (1) therefore holds on that neighborhood, and the return equals the identity there; consequently such a fixed point is not isolated. If \(c=0\), the cubic pulses combine and the return becomes conjugate to a single quadratic and a single cubic pulse. Its fixed-point equation is linear in \(y\), unless the return is locally the identity, and hence it has at most one isolated positive fixed point. The same holds for a four-window word which can be merged.

**Sharp minimality.** Every cyclic word of at most three pure windows has neighboring equal-type windows or itself contains at most two windows. After merging, one obtains at most a single quadratic and a single cubic map. Their fixed-point equation after squaring is \((y-b)^2-2a=y^2\), linear in \(y\), unless every fixed point is nonisolated. Thus two isolated positive periodic solutions first become possible at four windows. Cyclic resection preserves the count by invertibility on positive trajectories.

**Exact two-cycle diagram.** For the stated numerical pulses,
\[
 s(y)=\sqrt{(y+1)^2+10},\quad
 P_d(y)=\sqrt{(s(y)-2)^2-2d},\quad
 k(d)=\frac{15-2d}{4}.
\]
On the return's admissible positive domain,
\[
 P_d(y)^2-y^2=4g_d(y),\qquad
 g_d(y)=k(d)+\frac y2-s(y).\tag{3}
\]
Conversely, any positive root of \(g_d\) is admissible: \(y+1>0\), \(s(y)>\sqrt{11}>2\), and (3) gives the last squared-radical argument \(y^2>0\). Thus the positive roots of \(g_d\) correspond bijectively to finite positive four-periodic solutions. Direct differentiation yields
\[
 g_d'(y)=\frac12-\frac{y+1}{s(y)},\qquad
 g_d''(y)=-\frac{10}{s(y)^3}<0.
\]
The unique maximum on \((0,\infty)\) occurs at \(y_* = \sqrt{10/3}-1>0\), and
\[
 g_d(0)=\frac{15-2d}{4}-\sqrt{11},\qquad
 g_d(y_*)=\frac{15-2d}{4}-\frac{1+\sqrt{30}}2.
\]
Also \(g_d(y)\to-\infty\) as \(y\to\infty\). These signs and strict concavity yield exactly the claimed four regimes. In the two-cycle regime the roots are
\[
 y_\pm=\frac23\left[k(d)-2\pm\sqrt{4k(d)^2-4k(d)-29}\right],
 \qquad 0<y_-<y_+.
\]
Differentiating (3) at a fixed point gives
\[
 P_d'(y)-1=\frac{2g_d'(y)}{y}.
\]
Each pulse has positive derivative on its positive domain, so \(P_d'(y)>0\); strict concavity then implies \(P_d'(y_-)>1\), \(0<P_d'(y_+)<1\). At the maximum, \(P_d'=1\), \(P_d''=2g_d''(y_*)/y_*\ne0\), and \(\partial P_d/\partial d=-1/y_*\ne0\), proving a nondegenerate saddle-node. At \(d=d_\infty\), the lower root is \(y=0\), which is excluded from \(y>0\).

**Exact witnesses.** For \(d=1\), the two complete reciprocal state sequences at integer times are
\[
 \left(\tfrac12,\tfrac32,\tfrac72,\tfrac32,\tfrac12\right),\qquad
 \left(\tfrac76,\tfrac{13}6,\tfrac{23}6,\tfrac{11}6,\tfrac76\right).
\]
The derivative product is \((y+1)(s-2)/(sy)\) on either orbit. Substitution gives \(9/7\) and \(143/161\) respectively. Since both fixed points are hyperbolic, continuous dependence of the coefficient-to-return map in \(C^1\) near these compact, bounded trajectories and the implicit-function theorem give persistence under sufficiently small smooth periodic coefficient approximations. The latter assertion is an existence result for at least two cycles, not an upper bound for all smooth coefficients.

## Verification

Run `python3 verify.py` using Python 3 and its standard library. It checks both exact rational orbits and Floquet multipliers, an exact rational polynomial factorization, and finite consistency tests of the general radical-composition algebra. The supplied run printed `PASS; assertions: 553`, `positive period-four-time initial x-values: 2 6/7`, and `Floquet multipliers: 9/7 143/161`. These are finite corroborations; the global upper bound, exact thresholds, and bifurcation assertions follow from the analytic arguments above, not enumeration.

## Relationship to prior work

Bravo Trinidad, Tian, and Zhao (arXiv:2610.19340v1, 2026) prove a one-positive-cycle theorem under continuity, specific half-period symmetry, a two-zero pattern, and a convexity or concavity condition. The alternating pure-pulse coefficients here are discontinuous and violate those hypotheses; the present two-cycle example therefore does not contradict that theorem and is not covered by it. The general sign-definite linear-combination criterion of Álvarez, Gasull, and Giacomini does not apply: both pulse coefficient functions change sign on disjoint windows, so no nonzero constant linear combination has a definite sign. The Huang–Tian–Zhao extended-Chebyshev two-cycle bound applies to smooth coefficients in a three-dimensional ET-system and does not supply the four-window minimality or sharp pulse bifurcation diagram. Work on rational Abel cycles and piecewise Abel systems considers distinct coefficient restrictions and is acknowledged as a priority-check risk; an inaccessible specialized prior theorem could still supersede the present novelty assessment.

## Limitations

The universal two-cycle upper bound and minimal-window result apply to pure monomial, piecewise-constant coefficients with at most four cyclic windows. Coefficient magnitudes may be positive or negative, and a periodic solution must remain positive and finite for the full cycle. No global claim for arbitrary smooth coefficients, more than four windows, or negative solutions is made. The two-cycle smooth-persistence statement is local in coefficients and initial data. No independent audit has been conducted; historical priority remains provisional against unindexed specialized pulse-switching literature.

## References

1. J. L. Bravo Trinidad, R. Tian, Y. Zhao, *Uniqueness of Limit Cycles for Abel Equations and Planar Systems*, arXiv:2610.19340v1 (first posted 2026-10-14), https://arxiv.org/html/2610.19340v1.
2. J. Huang, R. Tian, Y. Zhao, *A Chebyshev criterion for at most two non-zero limit cycles in Abel equations*, arXiv:2506.14091v1 (2025), https://arxiv.org/html/2506.14091v1.
3. M. Álvarez, A. Gasull, J. Giacomini, *A new uniqueness criterion for the number of periodic orbits of Abel equations*, arXiv:math/0602468 (2006).
4. J. Llibre, C. Valls, *Rational limit cycles of Abel equations*, Communications on Pure and Applied Analysis 20 (2021), 1077–1089, DOI:10.3934/cpaa.2021007.
5. J. Huang, R. Tian, Y. Zhao, *On the Number of Limit Cycles in Generalized Abel Equations with Coefficients Having the Chebyshev Property*, arXiv:2608.15618 (2026).
