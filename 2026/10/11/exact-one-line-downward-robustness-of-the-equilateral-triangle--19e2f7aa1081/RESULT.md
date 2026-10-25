# Exact one-line downward robustness of the equilateral triangle
## Finding
Let \(T\) be an equilateral triangle. Following the reduced robustness model suggested by Domokos and Lángi, define
\[
\rho_{\mathrm{line}}(T)
=
\inf_H\frac{\operatorname{area}(T\setminus(T\cap H))}{\operatorname{area}(T)},
\]
where \(H\) ranges over closed half-planes for which \(T\cap H\) is two-dimensional, has only nondegenerate equilibria with respect to its own centroid, and has fewer stable equilibria than \(T\). Then
\[
\rho_{\mathrm{line}}(T)=\frac{3-\sqrt5}{2}.
\]
More precisely, a symmetric cut parallel to one side gives the sharp transition. If its two intersection points lie at the same fraction \(s\) of the adjacent sides, measured from the opposite vertex, then the retained trapezoid has four nondegenerate stable side equilibria for
\[
0<s<\frac{\sqrt5-1}{2},
\]
has two degenerate side equilibria at
\[
s=\frac{\sqrt5-1}{2},
\]
and has exactly two nondegenerate stable equilibria for every slightly larger \(s\). Its removed area fraction is \(s^2\), so the limiting threshold is \((3-\sqrt5)/2\).

## Assumptions and scope
A stable equilibrium of a convex polygon with respect to an interior point is the perpendicular foot on a side when that foot lies in the relative interior of the side. Vertex equilibria are unstable in the polygonal convention used by Domokos and Lángi. A side projection landing at a vertex is degenerate, and the source works throughout with bodies having only nondegenerate equilibria.

Normalize
\[
A=(0,\sqrt3),\qquad B=(-1,0),\qquad C=(1,0).
\]
Every proper line cut of \(T\), after relabeling the vertices, intersects \(AB\) and \(AC\) at
\[
P=A+t(B-A),\qquad Q=A+u(C-A),\qquad 0<t,u<1.
\]
The cut has two possible retained pieces: the quadrilateral \(BCQP\), which removes the cap \(APQ\), or the triangle \(APQ\), which removes the complementary region. The cap has area fraction \(p=tu\).

The theorem concerns this one-line restricted robustness only. It does not prove the unrestricted full-robustness conjecture for regular polygons.

## Proof
Let \(G\) be the centroid of the retained quadrilateral \(K=BCQP\). Since the removed cap has area fraction \(p=tu\), centroid subtraction gives
\[
G=\frac{G_T-pG_{APQ}}{1-p}.
\]
The base \(BC\) always carries a stable equilibrium because \(G\) lies in the interior of \(K\), so its horizontal coordinate lies strictly between the endpoints of \(BC\).

For the side \(CQ\), the perpendicular projection parameter from \(C\) toward \(Q\) is
\[
\lambda_{CQ}
=
\frac{t^2u+2tu^2-6tu+3}{6(u-1)(tu-1)}.
\]
Its numerator is positive, while its denominator is positive. Moreover
\[
1-\lambda_{CQ}
=
-\frac{L(t,u)}{6(u-1)(tu-1)},
\qquad
L(t,u)=t^2u-4tu^2+6u-3.
\]
Hence \(CQ\) fails to carry a nondegenerate stable equilibrium exactly when \(L(t,u)\ge0\). By reflection, the side \(PB\) fails exactly when
\[
R(t,u)=-4t^2u+tu^2+6t-3\ge0.
\]

The new cut side \(QP\) is stable whenever either old slanted side fails. Indeed its projection parameter has denominator
\[
D=6(tu-1)(t^2-tu+u^2)<0
\]
and numerator
\[
N=2t^3u-3t^2u^2+4tu^3+3tu-3t-6u^2+3u.
\]
Also the numerator of \(1-\lambda_{QP}\) is
\[
M=4t^3u-3t^2u^2-6t^2+2tu^3+3tu+3t-3u.
\]
Assume first that \(L(t,u)\ge0\). If \(u<1/2\), then as a convex quadratic in \(t\), \(L(t,u)\) is negative at both \(t=0\) and \(t=1\), hence negative on \([0,1]\), a contradiction. Thus \(u\ge1/2\). The exact identity
\[
N=\left(\frac t2-u\right)L(t,u)+\frac{3t}{2}(t^2u-1)
\]
then gives \(N<0\). Furthermore
\[
\frac{\partial^2 M}{\partial u^2}=6t(2u-t)>0
\]
on \(1/2\le u\le1\), so convexity gives
\[
M(t,u)\le\max\{M(t,1/2),M(t,1)\}.
\]
The endpoints factor as
\[
M(t,1)=(t-1)(4t^2-5t+3)<0,
\]
and
\[
4M(t,1/2)=t(1-t)(19-8t)-6<0,
\]
because \(t(1-t)\le1/4\). Thus \(M<0\), and since \(D<0\), both \(\lambda_{QP}>0\) and \(1-\lambda_{QP}>0\). The case \(R(t,u)\ge0\) follows by reflection. Therefore the retained quadrilateral has fewer than three stable equilibria if and only if both
\[
L(t,u)\ge0,\qquad R(t,u)\ge0,
\]
with strict inequalities in the nondegenerate class.

It remains to minimize \(p=tu\) under these two conditions. Put \(a=6-4p\) and assume without loss of generality that \(t\ge u\). The inequalities become
\[
pt+au\ge3,
\qquad
pu+at\ge3.
\]
Since \(a>p\), the first left-hand side is the smaller one, so it is at least \(3\). Writing \(u=p/t\) gives
\[
3\le pt+\frac{ap}{t}.
\]
For fixed \(p\in(0,1)\) and \(t\in[\sqrt p,1)\), the right-hand side is strictly decreasing, because \(a>2>t^2\). Hence
\[
3\le 3\sqrt p(2-p).
\]
With \(s=\sqrt p\), this is
\[
2s-s^3\ge1,
\]
which factors to give
\[
s\ge\frac{\sqrt5-1}{2}.
\]
Consequently
\[
p\ge\left(\frac{\sqrt5-1}{2}\right)^2
=\frac{3-\sqrt5}{2}.
\]
Equality forces \(t=u=(\sqrt5-1)/2\). At this limiting cut, the base and cut-side projection parameters are \(1/2\), while the two slanted-side parameters are \(1\) and \(0\); hence those two equilibria are degenerate. For \(0<t=u<s\), where \(s=(\sqrt5-1)/2\), the base and cut-side projections stay at their midpoints and both slanted-side projections lie in their relative interiors; hence there are four nondegenerate stable equilibria. Taking \(t=u\) slightly larger than \(s\) produces exactly two nondegenerate stable side equilibria and removed fraction tending down to the displayed threshold.

For completeness, consider retaining the cap triangle \(APQ\). Its three side projection parameters are
\[
\lambda_{PQ}=
\frac{4t^2-3tu+2u^2}{6(t^2-tu+u^2)},
\qquad
\lambda_{QA}=\frac{4u-t}{6u},
\qquad
\lambda_{AP}=\frac{2t+u}{6t}.
\]
The first always lies in \((0,1)\). A second side fails only if \(t\ge4u\) or \(u\ge4t\). In either case \(tu<1/4\), so the discarded complementary area fraction \(1-tu\) exceeds \(3/4\), which is larger than \((3-\sqrt5)/2\). Thus no triangle-retaining cut improves the quadrilateral threshold, completing the proof.

## Verification
The bundled `verify.py` uses exact symbolic algebra to reconstruct the centroid and all seven projection formulas, verify the factorizations used in the proof, and confirm the golden-ratio equality parameters. It also samples rational proper cuts only as a stress test of the logical partition. The symbolic proof above, not the sampling, establishes the all-parameter result.

## Relationship to prior work
Domokos and Lángi define full downward robustness using area removed from a convex body while recomputing the center of gravity of the retained body. They prove sharp results for decoupled external and internal robustness in the plane and conjecture maximal full robustness for regular polygons. In their discussion they explicitly propose a reduced version obtained by admitting only truncations by straight lines in two dimensions and note that this model is especially suitable for numerical investigation.

The present theorem computes that reduced model exactly for the first regular polygon, the equilateral triangle. The primary paper does not give this value, the golden-ratio transition, or a classification of triangle line cuts. Targeted searches for the reduced model, the exact constant, and equivalent triangle-truncation formulations found no covering statement.

## Limitations
The theorem concerns one straight-line truncation of an equilateral triangle. It does not compute unrestricted full robustness, average robustness, or the corresponding value for regular polygons with more sides. The sharp constant is an infimum because the threshold cut has degenerate equilibria; admissible nondegenerate cuts approach it from above.

A residual originality risk remains that an unindexed note or computational study may have derived the same triangle threshold without using the terminology of robustness.

## References
1. G. Domokos and Z. Lángi, *The robustness of equilibria on convex solids*, arXiv:1301.4031v1, first posted 2013-01-17; Mathematika 60 (2014), 237--256, DOI:10.1112/S0025579313000181. See the equilibrium definitions, Definition 1, and the discussion on page 18 of the preprint proposing truncations by straight lines.
