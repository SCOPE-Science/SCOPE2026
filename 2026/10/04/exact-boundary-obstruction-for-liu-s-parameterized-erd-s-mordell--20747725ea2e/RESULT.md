# Exact boundary obstruction for Liu’s parameterized Erdős–Mordell conjecture
## Finding
Jian Liu’s Conjecture 6.3 asks whether, for \(0.48\le k\le1.36\), every interior point \(P\) of a nondegenerate triangle satisfies
\[
\sum_i R_i\;\ge\;M_k\;\ge\;2\sum_i r_i,
\]
where
\[
M_k=\frac{2\sum_i(kr_i+r_j+r_\ell)(R_i+r_i)}{(k+2)\sum_i r_i}
\]
and \(\{i,j,\ell\}=\{1,2,3\}\). Define
\[
s=\sum_i r_i,\qquad T=\sum_iR_i,\qquad
D=\sum_i r_iR_i-2\sum_{i<j}r_ir_j,\qquad
E=s(T-2s).
\]
For every interior configuration except the equilateral triangle with \(P\) at its center, \(D>0\). The two halves of Liu’s conjectured inequality are exactly
\[
E+(k-1)D\ge0,
\qquad
kE+2(1-k)D\ge0.
\]
Thus, with \(\alpha=E/D\), the parameter dependence is one-dimensional. In particular, if \(\alpha<2\), the two halves require
\[
k\ge1-\alpha,
\qquad
k\le\frac{2}{2-\alpha}.
\]

A natural isosceles boundary family gives an exact algebraic obstruction. Take equal sides \(1,1\), base \(t\in(0,2)\), and let \(P\) tend from the interior to the midpoint of the base. Write
\[
t=\frac{4u}{1+u^2},\qquad 0<u<1.
\]
Then the limiting defect ratio is
\[
\alpha(u)=-\frac{u^4-12u^3+4u-1}{4u^3}.
\]
It has a unique minimum at the unique \(u_*\in(0,1)\) satisfying
\[
u_*^4-8u_*+3=0.
\]
Numerically,
\[
u_*=0.377539568391233\ldots,
\qquad
\alpha_*=0.535565054837061\ldots.
\]
Eliminating \(u_*\) also shows that \(\alpha_*\) is the relevant real root of
\[
27\alpha^4-260\alpha^3+876\alpha^2-1140\alpha+397=0.
\]
Consequently, any nonnegative parameter \(k\) for which Liu’s double inequality holds for all triangles and all interior points must lie in
\[
1-\alpha_*\le k\le\frac{2}{2-\alpha_*},
\]
that is,
\[
0.464434945162939\ldots\le k\le1.365714473426112\ldots.
\]
For every parameter outside this interval, the corresponding strict failure already occurs at the boundary midpoint and therefore persists for interior points sufficiently close to it. Liu’s proposed interval \([0.48,1.36]\) lies strictly inside this exact outer obstruction.

## Assumptions and scope
The triangle is Euclidean and nondegenerate. The point \(P\) is interior for the asserted counterexamples; the side midpoint is used only as a limiting configuration. The distances \(R_i\) and \(r_i\) follow Liu’s notation: \(R_i\) is the distance from \(P\) to vertex \(i\), and \(r_i\) is the distance to the opposite side.

The result does not assert that every \(k\) in the outer interval is universally valid. In particular, it does not prove Conjecture 6.3 on Liu’s interval \([0.48,1.36]\). Its content is the exact two-defect reduction and an algebraic family that sharply determines this boundary-family obstruction.

## Proof
Expanding the coefficient in \(M_k\) gives
\[
kr_i+r_j+r_\ell=s+(k-1)r_i.
\]
Therefore, with \(B=\sum_i r_i(R_i+r_i)\),
\[
M_k=\frac{2[s(T+s)+(k-1)B]}{(k+2)s}.
\]
Since
\[
B-s^2=\sum_i r_iR_i-2\sum_{i<j}r_ir_j=D,
\]
a direct rearrangement yields
\[
\frac{(k+2)s}{2}(M_k-2s)=E+(k-1)D
\]
and
\[
(k+2)s(T-M_k)=kE+2(1-k)D.
\]
Liu’s Lemma 2.2 gives \(D\ge0\), with equality for an interior point only at the equilateral-center case. The classical Erdős–Mordell inequality gives \(E\ge0\). Hence, away from the equality case, division by \(D\) is legitimate and the two inequalities reduce to the stated conditions in \(\alpha=E/D\). At the equilateral center, both original inequalities are equalities for every \(k\ne-2\).

For the boundary family, place
\[
A=(-t/2,0),\qquad C=(t/2,0),\qquad B=(0,h),
\]
where \(h=\sqrt{1-t^2/4}\), and first take the limiting point \(P=(0,0)\). Then
\[
R_A=R_C=t/2,\qquad R_B=h,
\]
and, because the equal sides have length \(1\),
\[
r_A=r_C=th/2,\qquad r_B=0.
\]
Thus
\[
D=\frac{t^2h(1-h)}{2},
\qquad
E=th(t+h-2th),
\]
so
\[
\alpha(t)=\frac{2(t+h-2th)}{t(1-h)}.
\]
With \(t=4u/(1+u^2)\) and \(h=(1-u^2)/(1+u^2)\), this becomes
\[
\alpha(u)=-\frac{u^4-12u^3+4u-1}{4u^3}.
\]
Differentiation gives
\[
\alpha'(u)=-\frac{u^4-8u+3}{4u^4}.
\]
The polynomial \(u^4-8u+3\) is strictly decreasing on \((0,1)\), because its derivative \(4u^3-8\) is negative there; it changes sign from positive to negative, so it has exactly one root \(u_*\) in that interval. Since \(\alpha'(u)\) changes from negative to positive at \(u_*\), this root is the unique global minimum of the boundary-family ratio. The displayed quartic for \(\alpha_*\) follows by eliminating \(u\) from the two exact polynomial equations.

At \(u=u_*\), the lower-half defect has sign equal to that of \(k-(1-\alpha_*)\), while the upper-half defect has sign equal to that of \(2-k(2-\alpha_*)\). If \(k<1-\alpha_*\) or \(k>2/(2-\alpha_*)\), one of these defects is strictly negative at the limiting midpoint. Distances, and hence both defects, vary continuously with \(P\). Moving \(P\) a sufficiently small positive distance into the triangle preserves that strict sign, producing genuine interior counterexamples.

## Verification
The accompanying checker independently evaluates the algebraic reduction on randomized triangles and interior points, verifies the rational boundary parameterization on exact rational samples, isolates the unique root \(u_*\), checks the quartic relation for \(\alpha_*\), and constructs interior points close to the boundary midpoint that violate the appropriate half of the double inequality for parameters just outside the derived interval.

These computations are consistency checks. The universal algebraic reduction, uniqueness of the boundary-family minimizer, and continuity argument are proved symbolically above; finite sampling is not used as a proof of an infinite assertion.

## Relationship to prior work
Liu’s 2016 paper states the double inequality above as Conjecture 6.3 specifically for \(0.48\le k\le1.36\), after establishing the inequality \(\sum_i r_iR_i\ge2\sum_{i<j}r_ir_j\) used here. The present result does not claim Liu’s conjectured interval itself: it rewrites both halves through the two classical defects \(D\) and \(E\), then derives an exact algebraic outer obstruction from a natural isosceles boundary family.

Tran’s 2021 weighted Erdős–Mordell paper develops a different family of weighted inequalities. Its inspected full text does not state the defect-ratio reduction or the algebraic endpoint constants above. Later weighted/refinement papers were also searched by the source formula, parameter interval, endpoint decimals, and eliminating quartic. No covering statement was located in the inspected material.

## Limitations
The result supplies a necessary outer interval for any universal nonnegative parameter and an exact reduction of the parameter dependence; it does not establish sufficiency anywhere beyond what was already known. The exact endpoints are sharp for the displayed isosceles boundary family, not claimed to be the globally optimal obstruction among all possible triangle-point families.

Literature searches cannot prove novelty. Full text of Jian Liu’s 2018 Discrete & Computational Geometry paper and Quang Hung Tran’s 2026 Mathematics Magazine paper was not available through the accessible sources in this check; both remain explicit overlap risks because they concern weighted or strengthened Erdős–Mordell inequalities. Their accessible abstracts and previews did not expose the same defect-ratio reduction or endpoint constants.

## References
1. J. Liu, “Refinements of the Erdös-Mordell inequality, Barrow’s inequality, and Oppenheim’s inequality,” Journal of Inequalities and Applications 2016, article 9. DOI 10.1186/s13660-015-0947-2. Published 2016-01-04.
2. Q. H. Tran, “A family of weighted Erdös–Mordell inequality and applications,” Journal of Geometry 112 (2021), article 33; arXiv:2105.07885.
3. J. Liu, “Two New Weighted Erdős–Mordell Type Inequalities,” Discrete & Computational Geometry 59 (2018), 707–724. DOI 10.1007/s00454-017-9917-4.
4. J. Liu, “New Refinements of the Erdös–Mordell Inequality and Barrow’s Inequality,” Mathematics 7 (2019), 726. DOI 10.3390/math7080726.
5. Q. H. Tran, “Some new improvements of the Erdős–Mordell Inequality,” Mathematics Magazine (2026). DOI 10.1080/0025570X.2026.2653460.
