# Exact shared-strut intervals and sharp two-mode perimeter stability for parallelograms

## Finding

Let \(Q\) be any nondegenerate Euclidean parallelogram with adjacent nonzero vectors \(u,v\). Relabel so \(a=|u|\ge b=|v|>0\), and put \(c=|u\cdot v|/(ab)\in[0,1)\). A side with endpoints \(A,B\) has an \(\ell\)-strut if some **nonvertex** \(C\in Q\) satisfies \(|C-A|=|C-B|=\ell\). Write \(\Delta(\ell)\) if all four sides have such a strut, for the same \(\ell>0\). This is the strut convention of Nikonorov--Nikonorova [1].

For \(d=|u\cdot v|=abc\) define \(T_u=\min\{1,a^2/(2d)\}\) and \(T_v=\min\{1,b^2/(2d)\}\); if \(d=0\) both are defined to equal \(1\). Define
\[
R_u^2=\frac{a^2}{4}+b^2(1-c^2)T_u^2,\qquad
R_v^2=\frac{b^2}{4}+a^2(1-c^2)T_v^2.
\]
Then the complete set of common positive strut radii is
\[
\mathcal S(Q)=\left[\frac a2,\min(R_u,R_v)\right]
\]
**with the following and only the following endpoint convention**: exclude its right endpoint if that endpoint equals \(R_u\) and \(2d=a^2\), or equals \(R_v\) and \(2d=b^2\). An interval with upper endpoint below its lower endpoint is empty. In particular, \(\mathcal S(Q)\ne\varnothing\) if and only if
\[
\boxed{|u\cdot v|\le b^2,\quad\text{equivalently}\quad c\le b/a.}
\]
(The equality case in this feasibility criterion has an actual nonvertex strut.) Thus sufficiently sheared unequal-side parallelograms fail the common-strut property, and the threshold is exact.

For every \(\ell\in\mathcal S(Q)\), writing \(L=2(a+b)\) for perimeter, one has the **sharp two-mode stability inequality**
\[
\boxed{L^2-\frac{64}{5}\ell^2\ge
\frac45(a-b)(a+11b)+\frac{64}{5}b^2c^2.}\tag{1}
\]
In particular \(L\ge8\ell/\sqrt5\), with equality **if and only if** \(Q\) is a square of side \(2\ell/\sqrt5\). The two coefficients on the right side of (1) cannot individually be increased: rectangles at their maximal common radii saturate the side-disparity part, and rhombi of nonzero \(c<1/2\) at their maximal common radii saturate the shear part. More precisely, the entire inequality (1) is an equality for these two families.

For fixed \(\ell\), the square is quantitatively rigid: if \(L^2-64\ell^2/5\le\varepsilon\ell^2\) with \(\varepsilon\to0+\), then \((a-b)/\ell=O(\varepsilon)\) and \(c=O(\sqrt\varepsilon)\). Neither exponent improves uniformly, as witnessed respectively by nearly square rectangles and nearly square rhombi.

## Assumptions and scope

All distances are Euclidean. The parallelogram is closed and nondegenerate, allowing obtuse angles and arbitrary aspect ratios; the absolute cosine \(c\) removes the orientation choice. A witness may lie on a side and may coincide with the midpoint of the tested side, but may not be a vertex. The radius \(\ell\) is fixed simultaneously for all four sides. The theorem concerns exact geometry, not noisy geometric measurements. The first-public inspiration [1] dates to 2022-09-13 and is classed in MSC 52A10; the present theorem's primary classification is 52A10.

## Proof

**1. Bisector intersections.** Parametrize \(Q\) by \(x u+y v\) with \(0\le x,y\le1\). For the side from \(0\) to \(u\), equality of endpoint distances means
\[
a^2x+(u\cdot v)y=a^2/2,
\quad\text{so}\quad x=1/2-(u\cdot v)y/a^2.
\]
As \(y\) increases from zero, the last point on this segment of the perpendicular bisector has \(y=T_u\); the opposite side gives the reflected same radius range. At the point with parameter \(y\), its common squared distance from the two endpoints is
\[
\ell^2=\frac{a^2}{4}+b^2(1-c^2)y^2.
\]
Since \(Q\) is nondegenerate, this varies continuously and strictly with \(y\) from \(a^2/4\) to \(R_u^2\). The starting point is the tested side midpoint, not a vertex. The terminal point is a polygon vertex precisely when simultaneously \(y=1\) and \(x\in\{0,1\}\), or equivalently \(2d=a^2\). Otherwise it is a nonvertex, even when the bisector meets an adjacent edge. Thus both sides parallel to \(u\) admit radii \([a/2,R_u]\), except for the specified terminal exclusion. Interchanging the vectors gives the analogous \([b/2,R_v]\) for the other two sides. Their intersection gives the stated complete interval and exclusions. No other obstruction exists because each perpendicular-bisector intersection is a closed segment with strictly monotone radius, apart from removal of possible terminal vertices.

**2. Feasibility threshold.** Because \(a\ge b\), the common lower endpoint is \(a/2\) and \(R_u>a/2\). Therefore only \(R_v\ge a/2\) matters. If \(d\le b^2/2\), then \(T_v=1\) and
\[
R_v^2=b^2/4+a^2(1-c^2)\ge a^2/4,
\]
indeed \(c\le b/(2a)\le1/2\) makes the inequality immediate. If \(d>b^2/2\), then \(T_v=b^2/(2d)\) and direct cancellation gives
\[
R_v^2=\frac{b^2}{4c^2}.
\]
Hence \(R_v\ge a/2\) exactly when \(c\le b/a\). This includes the first case. At threshold equality \(c=b/a\), the terminal v-bisector point has edge parameter strictly between zero and one (the excluded vertex condition would require \(2d=b^2\), whereas here \(d=b^2\)); therefore feasibility holds with equality.

**3. Sharp perimeter inequality.** For any common strut radius,
\[
\ell^2\le R_u^2\le\frac{a^2}{4}+b^2(1-c^2).
\]
Substituting into \(L^2=4(a+b)^2\) gives the **exact algebraic lower bound**
\[
L^2-\frac{64}{5}\ell^2
\ge 4(a+b)^2-\frac{64}{5}\Bigl(\frac{a^2}{4}+b^2(1-c^2)\Bigr)
=\frac45(a-b)(a+11b)+\frac{64}{5}b^2c^2.
\]
Both terms on the right are nonnegative. Their simultaneous vanishing forces \(a=b\) and \(c=0\), hence a square. Conversely, for a square of side \(s\), each tested side has the opposite-side midpoint as a nonvertex strut of radius \(\ell=\sqrt5\,s/2\), giving equality.

**4. Two independent sharpness families.** For a rectangle with side lengths \(a\ge b\) and \(c=0\), the largest common strut radius is \(\ell=R_u=\sqrt{a^2/4+b^2}\); it is realized by the opposite-side midpoint on each longer side and corresponding nonvertex points for shorter sides. This realizes equality in (1), so its coefficient \(4/5\) for the unequal-side term is best possible. For a rhombus with side \(a=b=s\) and \(0<c<1/2\), the largest common radius is \(\ell=s\sqrt{5/4-c^2}\), realized on each opposite side away from its vertices. Equality holds in (1), showing the coefficient \(64/5\) on the shear term is individually optimal.

**5. Optimal near-square stability rates.** Put \(W=a+b\) and \(X=a-b\). As \(a+11b=6W-5X\ge W\), inequality (1) and \(W=L/2\ge4\ell/\sqrt5\) imply
\[
X/\ell\le(5\sqrt5/16)\varepsilon.
\]
Meanwhile \(W=4\ell/\sqrt5+O(\varepsilon\ell)\), so \(b=(W-X)/2\) is bounded below by a fixed multiple of \(\ell\) for sufficiently small \(\varepsilon\); the second term of (1) therefore gives \(c=O(\sqrt\varepsilon)\). For the rectangle family \(a=b(1+t)\) with \(t\downarrow0\), the normalized perimeter deficit is of first order in \(t\), proving optimality of exponent one for side disparity. For the rhombus family with \(c\downarrow0\), the deficit is of second order in \(c\), proving optimality of exponent one-half for angular deviation. These families satisfy the nonvertex convention.

## Verification

The standalone `CHECK.py` uses exact rational coordinates and independently intersects the perpendicular bisectors with all four polygon edges. It checks the claimed maximal strut radii and shear threshold for 1,530 rational configurations, tests two vertex-only terminal exclusions, then verifies exact rational equalities on rectangles and rhombi and their near-square orders. Run with `python3 CHECK.py`; no nonstandard Python dependencies are required. This finite test suite cross-checks calculations but is not used as a universal proof; the preceding arguments supply that proof.

## Relationship to prior work

Nikonorov and Nikonorova [1] introduce the \(\Delta(\ell)\) property, prove the universal perimeter bound \(L\ge3\ell\) for arbitrary polygons, and investigate partial-side strut hypotheses and a distinct centrally symmetric difference-body property. Their results do not give the common-radius phase boundary \(|u\cdot v|\le b^2\), the exact four-side radius interval, or the two-mode sharpened perimeter bound of (1). The precise radius and midpoint geometry specializes their natural strut problem to the centrally symmetric four-sided class, where a substantially sharper statement is possible.

Nikitenko and Nikonorov [2] solve the minimum-perimeter quadrilateral problem for **self-Chebyshev boundary radius**, a different invariant involving minimax distances from a boundary center. They explicitly note the same numerical factor \(8/\sqrt5\) for the square in that invariant. This shared square ratio is **not claimed as a newly discovered number**: [2] does not imply the all-strut existence threshold, endpoint structure, or equality and stability assertions for \(\Delta(\ell)\) parallelograms. The square constant alone is not the contribution.

Searches for aliases involving equidistant-side witnesses, unit struts, centrally symmetric quadrilaterals, and parallelogram shear found no stronger theorem that implies the full assertion. Absence of a retrieved match is not a proof of historical priority; unindexed earlier classifications remain possible.

## Limitations

The result assumes a Euclidean **parallelogram** rather than a general quadrilateral, and permits boundary strut witnesses so long as they are not vertices. Its interval description is exact only for this closed-body convention. The stability statement is asymptotic and concerns exact normalized length deficits; it is not a noisy-estimation guarantee. Historical originality has been checked against the specified primary sources and available indexed results but independently audited priority has not been established.

## References

[1] Yu. G. Nikonorov and O. Yu. Nikonorova, *Some extremal problems for polygons in the Euclidean plane*, arXiv:2209.05940, originally submitted 2022-09-13; especially Introduction and Theorems 1--3. https://arxiv.org/abs/2209.05940

[2] E. V. Nikitenko and Yu. G. Nikonorov, *The extreme polygons for the self Chebyshev radius of the boundary*, arXiv:2301.03218, originally submitted 2023-01-09; Introduction, Theorem 1, and Sections 3--8. https://arxiv.org/abs/2301.03218
