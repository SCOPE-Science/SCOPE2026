# Sharp side-count isoperimetric profile of planar tropical geodesic polygons

## Finding

Let \(K\subset\mathbb R^2\) be a full-dimensional compact convex set that is tropically geodesic for the norm
\[
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]
If its boundary has exactly \(m\) positive-length straight edges, then \(3\le m\le6\). For tropical perimeter \(P=P_N(\partial K)\) and Euclidean area \(A=A(K)\), the **sharp complete side-count profile** is
\[
P^2\ge c_m A,\qquad (c_3,c_4,c_5,c_6)=(18,16,14,12).
\]
Equality is as follows, up to translation, positive scaling and linear isometries of \(N\):

* \(m=3\): every tropically geodesic triangle; a representative is the triangle with vertices \((0,0),(1,0),(1,1)\).
* \(m=4\): either a parallelogram whose two edge families have the same tropical length (represented by the unit square), or the nonparallelogram trapezoid with vertices \((0,0),(1/2,0),(3/2,1),(0,1)\). The two types are genuinely distinct.
* \(m=5\): precisely the pentagon with vertices \((0,0),(1/2,0),(1,1/2),(1,1),(0,1)\).
* \(m=6\): precisely the tropical balls, the known equality class for the sharp tropical isoperimetric inequality.

The five-sided result has the stronger exact **two-square stability identity**
\[
P^2-14A=\frac72(a-b)^2+8\left(u-\frac{a+b}{4}\right)^2,
\]
where \(a,b>0\) are the side lengths of the enclosing coordinate rectangle and \(0<u<\min(a,b)\) is the equal-leg corner truncation. The three-, four- and five-sided sharp refinements and the pentagonal identity comprise the new claim; the hexagonal case is included to complete the profile and is explicitly credited to earlier work.

## Assumptions and scope

The metric is the planar tropical/projective Hilbert metric in the coordinates \((x,y)\), with length of a segment with displacement \((s,t)\) equal to \(N(s,t)\). A set is **tropically geodesic** if it contains every tropical length-minimizing curve between any two of its points. The needed structural characterization (Rosenmann, arXiv:2601.14447, Proposition 4.14 and Theorem 4.15) says that its compact full-dimensional instances are precisely bounded intersections of strips normal to the three linear forms \(x\), \(y\), and \(x-y\). Consequently all boundary edge directions are horizontal, vertical, or along \((1,1)\). Nonzero edges alone are counted, so an intersection at which an edge shrinks to a point is not counted as an extra edge.

The linear isometry group of \(N\) permutes, in absolute value, the three linear forms \(x,y,x-y\); the swaps are generated, for example, by \((x,y)\mapsto(y,x)\) and \((x,y)\mapsto(x,x-y)\). These coordinate maps have determinant of absolute value one, hence preserve both area and tropical perimeter. Only positive-area compact polygons and exact integer side counts \(3\le m\le6\) are claimed. The result does not give the optimal constant for arbitrary nongodesic convex polygons with the same edge count.

## Proof

**Normal-form classification.** The supporting lines use at most the six oriented normals from the three coordinate forms. A nondegenerate compact polygon must have at least three edges. For \(m=5\), the positive-edge counts in the three direction classes must be \((2,2,1)\). After the above isometry and translation, the two doubly represented classes bound a rectangle \([0,a]\times[0,b]\), and the single remaining supporting line cuts off just one of its corners. Because the third family has slope \(1\), the removed triangle has equal horizontal and vertical legs \(u\), with \(0<u<\min(a,b)\). Its vertices may be taken as
\[
(0,0),\quad(a-u,0),\quad(a,u),\quad(a,b),\quad(0,b).
\]
For \(m=4\) either \((2,2,0)\) occurs, giving a parallelogram, or \((2,1,1)\) occurs, giving the same corner-truncated rectangle when an edge vanishes: \(u=\min(a,b)\). By permuting directions, take \(a>b=u>0\) in the latter case. For \(m=3\), only \((1,1,1)\) is possible, giving the triangular endpoint \(a=b=u>0\). This classification uses no assumption that the polygons are symmetric.

**The pentagon.** Its area and perimeter are exactly
\[
A=ab-\frac{u^2}{2},\qquad P=2(a+b)-u.
\]
The diagonal replacement removes tropical length \(2u\) from the sides of the rectangle and adds length \(u\). Direct expansion gives
\[
P^2-14A=\frac72(a-b)^2+8\left(u-\frac{a+b}{4}\right)^2\ge0.
\]
Equality forces \(a=b\) and \(u=a/2\), which is admissible and yields exactly the stated pentagon. Thus the sharp constant is \(14\), including a coercive two-parameter stability certificate modulo scale and isometry.

**The quadrilateral.** A parallelogram with lengths \(a,b>0\) along two of the primitive tropical directions has \(A=ab\), \(P=2(a+b)\), and
\[
P^2-16A=4(a-b)^2.
\]
For a trapezoid in the normalized cut-rectangle form with \(a>b=u>0\),
\[
A=ab-\frac{b^2}{2},\quad P=2a+b,\quad P^2-16A=(2a-3b)^2.
\]
Therefore the sharp quadrilateral constant is \(16\), with exactly the two equality families \(a=b\) (parallelogram) and \(a=3b/2\) (trapezoid).

**The triangle.** The final degeneration \(a=b=u>0\) is the triangle with vertices \((0,0),(0,a),(a,a)\); it has \(A=a^2/2\), \(P=3a\), hence \(P^2=18A\). The normal-form classification shows this holds for every tropically geodesic triangle.

**The hexagon.** Rosenmann's tropical isoperimetric theorem gives \(P^2\ge12A\) for all such convex sets and identifies equality only at tropical balls. Sharpness is confirmed by the tropical unit ball \(N(x,y)\le1\), which has area \(3\) and perimeter \(6\). This last inequality and equality characterization are quoted as known, not presented as novel.

The four exact cases exhaust all permitted edge counts, completing the proof.

## Verification

A standalone exact-arithmetic checker accompanies this text. Execute `python3 tropical_profile_checker.py` with Python 3 and SymPy installed. It symbolically verifies each new deficit identity and uses rational polygon coordinates to test \(2,000\) pentagons, \(1,000\) trapezoids, \(1,000\) parallelograms, \(100\) triangles, and the equality representatives for the pentagon, trapezoid and tropical unit hexagon. Expected terminal line: `VERIFY_OK: 4103 exact polygon cases and 3 symbolic identities`. Finite tests are supplementary; the proof relies on normal-form exhaustiveness and exact squares, not sampling.

## Relationship to prior work

Rosenmann's March 2026 paper proves \(P^2\ge12A\) generally, describes the \(18\) combinatorial tropical-geodesic polygon types, and obtains the unrestricted tropical honeycomb theorem (Lemma 7.2, Theorems 7.3 and 8.2). It does **not** state side-specific sharp constants, the two distinct equality morphologies at four sides, or the five-sided stability identity. The earlier January 2026 paper supplies the structural classification of tropically geodesic sets (Proposition 4.14 and Theorem 4.15), not their sharp perimeter-area ratios at fixed side count. Lángi and Wang (2024; version inspected from December 2025) analyze normed-plane honeycomb inequalities and minimum-area circumscribed polygons (Theorems 1.4, 1.5 and Lemma 3.7), but their minimization over circumscribed polygons or whole tilings is not the same statement as the present sharp deficit and equality classification for individual tropical geodesic polygons. The known six-sided endpoint is expressly excluded from novelty.

## Limitations

This theorem concerns the geodesic/alcoved subclass, not all convex triangles through hexagons under the tropical norm. In particular, the tropical isoperimetric constant \(12\) for general plane regions was already known. Earlier uncatalogued crystalline-isoperimetric calculations or an equivalent formulation via polygonal anisotropic duality remain a residual bibliographic priority risk. The named literature comparisons do not establish absolute historical uniqueness. No independent mathematical audit has been carried out.

## References

1. Amnon Rosenmann, *Tropical measures, anisotropic isoperimetric inequality and honeycomb* (first public 2026-03-03), arXiv:2603.03215, especially Sections 3, 7 and 8. https://arxiv.org/abs/2603.03215
2. Amnon Rosenmann, *Tropical balls, geodesics and honeycomb* (first public 2026-01-20), arXiv:2601.14447, especially Proposition 4.14 and Theorem 4.15. https://arxiv.org/abs/2601.14447
3. Zsolt Lángi and Shanshan Wang, *The Honeycomb Conjecture in normed planes and an alpha-convex variant of a theorem of Dowker* (first public 2024-06-15), arXiv:2406.10622, especially Sections 1 and 3. https://arxiv.org/abs/2406.10622
