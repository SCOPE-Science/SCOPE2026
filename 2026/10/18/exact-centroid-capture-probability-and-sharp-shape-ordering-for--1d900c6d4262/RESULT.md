# Exact centroid-capture probability and sharp shape ordering for uniformly sampled triangle perimeters

## Finding

**Theorem.** Let \(T=ABC\) be an arbitrary nondegenerate Euclidean triangle, with side lengths \(a=|BC|\), \(b=|CA|\), \(c=|AB|\), perimeter \(L=a+b+c\), and normalized side lengths \(p=a/L\), \(q=b/L\), and \(r=c/L\). Choose three independent points \(X_1,X_2,X_3\) from the full boundary \(\partial T\), each distributed according to Euclidean arclength divided by \(L\). Put \(G=(A+B+C)/3\).

Then the exact centroid-capture probability is
\[
\boxed{\Pr\bigl(G\in\operatorname{conv}(X_1,X_2,X_3)\bigr)
=\kappa(pq+pr+qr)+\eta pqr,\qquad
\kappa=\frac{3+4\ln2}{9},\quad\eta=\frac83\ln2-1.}
\]
Equivalently, it is the symmetric homogeneous cubic
\[
\frac{\kappa\sum_{i\ne j}a_i^2a_j+4(\ln2)abc}{(a+b+c)^3},
\qquad(a_1,a_2,a_3)=(a,b,c).
\]
The probability is **strictly Schur-concave** in \((p,q,r)\). Thus among all nondegenerate Euclidean triangles,
\[
\boxed{\frac{3+4\ln2}{36}<\Pr\bigl(G\in\operatorname{conv}(X_1,X_2,X_3)\bigr)
\le\frac{2(3+10\ln2)}{81}.}
\]
The upper equality holds exactly for equilateral triangles, for which the probability is approximately \(0.245221526064184\). The lower constant, approximately \(0.160349686728883\), is a sharp **unattained infimum** reached when normalized side lengths converge, up to permutation, to \((1/2,1/2,0)\). There are no other limiting minimizing configurations.

The exact edge-multiplicity subprobabilities underlying the theorem are
\[
\Pr(G\in\operatorname{conv}(X_1,X_2,X_3)\mid \text{one sampled point on each edge})=\frac23\ln2,
\]
\[
\Pr(G\in\operatorname{conv}(X_1,X_2,X_3)\mid \text{two points on one specified edge, one on another})
=\frac{3+4\ln2}{27}.
\]
These are independent of the triangle's shape, because conditional fractional locations along specified edges are independent uniform variables; the shape dependence enters only through the edge-selection weights \((p,q,r)\).

## Assumptions and scope

Triangles are nondegenerate and embedded in the Euclidean plane. The original three points are *not* conditioned to occupy distinct edges; repeated-edge samples are included. An endpoint has probability zero. The centroid is the affine vertex barycenter, not in general the perimeter centroid or incenter. Boundaries of sampled convex hulls contain the centroid with probability zero, so either open or closed containment gives the stated value. Neither coordinates nor orientation affect the probability.

A permissible side-length vector satisfies the strict triangle inequalities, equivalently \(p,q,r\in(0,1/2)\) and \(p+q+r=1\).

## Proof

**1. Angular semicircle identity.** Fix any interior point \(G\) of a convex polygon, parameterize its boundary counterclockwise, and let \(\ell(x)\) be the counterclockwise arclength from \(x\) to the second intersection of the line \(xG\) with the boundary. The angular directions of three sampled boundary points fail to capture \(G\) exactly when they fit inside some open angular semicircle. Except on a null set, a non-capturing triple has exactly one angular gap exceeding \(\pi\); the boundary point immediately after that gap is its unique starting point for which the other two samples are in the ensuing counterclockwise half-turn arc of length \(\ell(x)\). Conditioning on the unique starting sample and using independence, the three disjoint choices of its label give
\[
\Pr\bigl(G\notin\operatorname{conv}(X_1,X_2,X_3)\bigr)
=\frac{3}{L^3}\int_{\partial T}\ell(x)^2\,ds(x).
\tag{1}
\]
This identity needs no central symmetry. Its angular counting principle is related to standard formulas for random-triangle containment; the work below is the exact Euclidean perimeter evaluation.

**2. Exact opposite-ray arclength.** Affinely normalize the labeled triangle to \(A=(0,0),\ B=(1,0),\ C=(0,1)\). This affine normalization is used only to locate the opposite ray intersections: a fractional parameter along an edge is preserved, while its physical arclength remains the corresponding Euclidean edge length. For the point \(x=(t,0)\) on the oriented side \(AB\), \(0\le t\le1\), and centroid \(G=(1/3,1/3)\), an elementary line intersection gives
\[
\ell_{AB}(t)=
\begin{cases}
 c(1-t)+a\dfrac{1-t}{2-3t},&0\le t\le\frac12,\\[3pt]
 c(1-t)+a+b\dfrac{2t-1}{3t-1},&\frac12\le t\le1.
\end{cases}
\tag{2}
\]
In the first range the antipode lies on \(BC\); in the second it lies on \(CA\). The denominators in their respective ranges are at least \(1/2\), so no boundary singularity occurs. The formulas agree at \(t=1/2\). Cyclic permutations give the other two sides.

**3. Integration and cubic reduction.** Set \(I(a,b,c)=\int_0^1\ell_{AB}(t)^2dt\). Integrating the two rational expressions in (2), by polynomial division and logarithms, yields
\[
\begin{aligned}
I(a,b,c)={}&\left(\frac{11}{18}+\frac{4\ln2}{27}\right)(a^2+ac)
+\left(\frac23-\frac{4\ln2}{9}\right)ab\\
&+\left(\frac5{18}-\frac{8\ln2}{27}\right)(b^2+bc)+\frac{c^2}{3}.
\end{aligned}
\tag{3}
\]
Since \(ds=c\,dt\) on \(AB\), the integral in (1) is
\[
 cI(a,b,c)+aI(b,c,a)+bI(c,a,b).
\tag{4}
\]
Substituting (3) into (4) and simplifying (1) gives
\[
\Pr(G\in\operatorname{conv}(X_1,X_2,X_3))
=\frac{\kappa\sum_{i\ne j}a_i^2a_j+4\ln2\,abc}{L^3}.
\tag{5}
\]
The elementary identity \(\sum_{i\ne j}p_i^2p_j=(pq+pr+qr)-3pqr\), valid when \(p+q+r=1\), changes (5) into the claimed symmetric polynomial with \(\eta=4\ln2-3\kappa>0\). Grouping (5) by the multinomial edge labels yields the displayed conditional probabilities, where the all-on-one-edge pattern contributes zero.

**4. Strict shape ordering and sharp endpoints.** Write
\[
\Phi(p,q,r)=\kappa(pq+pr+qr)+\eta pqr.
\]
Because \(\kappa>0\) and \(\eta>0\), for any distinct indices \(i,j,k\),
\[
(p_i-p_j)\left(\frac{\partial\Phi}{\partial p_i}-\frac{\partial\Phi}{\partial p_j}\right)
=-(p_i-p_j)^2(\kappa+\eta p_k),
\tag{6}
\]
strictly negative when \(p_i\ne p_j\). Thus \(\Phi\) is strictly Schur-concave (strict on unequal vectors related by a nontrivial majorization step). Every normalized triangle side vector is majorized by \((1/2,1/2,0)\), since its largest component is less than \(1/2\), and it majorizes \((1/3,1/3,1/3)\). Equality conditions for strict Schur concavity give the unique equilateral maximizer and show that the only limiting minimizing vectors are permutations of \((1/2,1/2,0)\).

Finally, evaluate \(\Phi(1/3,1/3,1/3)=2(3+10\ln2)/81\) and \(\Phi(1/2,1/2,0)=(3+4\ln2)/36\). The latter vector is not realized by a nondegenerate triangle but is approached by the admissible isosceles side ratios \((1/2-\varepsilon,1/2-\varepsilon,2\varepsilon)\) for \(0<\varepsilon<1/6\). This completes the proof.

## Verification

The accompanying standalone `CHECK.py` uses SymPy to recompute the two rational integrals in (2), compare with the complete expression (3), establish the symmetric cubic identity (5), verify the differentiation identity (6), recover the sharp endpoint values, and check the multinomial edge-pattern coefficients. Run `python CHECK.py` with SymPy installed. These are algebraic checks of the proof rather than statistical simulations or external certification. The angular semicircle principle and the majorization conclusion are separately proved above.

As optional numerical sanity checks, three independent simulations with 500,000 triples each compared observed probabilities against the exact expression for an equilateral triangle, a \(3\)-\(4\)-\(5\) right triangle, and a thin triangle; all deviations were within the sampling errors. The result itself is not inferred from Monte Carlo data.

## Relationship to prior work

Ionaşcu's *Random triangles in planar regions containing a fixed point* (arXiv:1612.08619) develops general angular integration formulas for points sampled uniformly from a **planar region by area** and gives the known equilateral-centroid constant \(2(3+10\ln2)/81\). Its generic radial-boundary setup motivates the half-circle counting identity; its specified sampling distribution is not uniform perimeter arclength on an arbitrary scalene triangle. The equilateral constant is **not claimed as new**; it dates at least to Prékopa's 1972 work.

Maesumi's *Triangle Inscribed-Triangle Picking* (arXiv:1804.11007) studies the area distribution when **one point is forced onto each of the three sides**. It does not give centroid-containment probability, repeated-side patterns, or perimeter-dependent side weights. Reitzner, Schütt, and Werner's *The convex hull of random points on the boundary of a simple polytope* (arXiv:1911.05917) treats the large-sample random boundary-hull setting and asymptotics, not the present three-point centroid event. The new statement is the all-shape Euclidean arclength cubic and its strict Schur and sharp extremal classification, not the well-known constant in the equilateral special case.

## Limitations

The theorem concerns exactly three independent points, normalized uniform Euclidean arclength on a triangular boundary, and capture of the vertex centroid. It does not assert analogous formulas for general polygons, arbitrary interior target points, other sampling laws, or more points. The case of zero-area degenerate triangles is excluded; the lower bound is only a limit through nondegenerate triangles. The displayed finite symbolic checks corroborate algebraic steps but do not replace the geometric arguments.

## References

1. E. J. Ionaşcu, *Random triangles in planar regions containing a fixed point*, arXiv:1612.08619 (first public preprint 15 December 2016), https://arxiv.org/abs/1612.08619. Section 1 and its area-sampling angular integral; Section 5 gives the already-known equilateral constant.
2. A. Maesumi, *Triangle Inscribed-Triangle Picking*, arXiv:1804.11007 (first public preprint 30 April 2018), https://arxiv.org/html/1804.11007v1. Conditional side-forced triangle area distribution.
3. M. Reitzner, C. Schütt, and E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (first public preprint 14 November 2019), https://arxiv.org/abs/1911.05917.
4. A. Prékopa, *On the number of vertices of random convex polyhedra*, Periodica Mathematica Hungarica 2 (1972), 259–282, equation (5.24). The classical area-uniform equilateral special value; bibliographic indication also appears in https://oeis.org/A393427.
