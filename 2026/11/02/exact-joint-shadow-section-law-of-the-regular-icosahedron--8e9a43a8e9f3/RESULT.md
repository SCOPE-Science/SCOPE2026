# Exact joint shadow–section law of the regular icosahedron

## Finding

Let \(\varphi=(1+\sqrt5)/2\), and let \(I\subset\mathbb R^3\) be the convex hull of the twelve points
\[
(0,\pm1,\pm\varphi),\quad (\pm1,\pm\varphi,0),\quad (\pm\varphi,0,\pm1).
\]
Choose a normal \(U\) uniformly on the unit sphere. Let \(S(U)\) be the number of polygon vertices in the **orthogonal projection** of \(I\) onto \(U^\perp\) (its shadow), and let \(T(U)\) be the number of vertices of the **central planar intersection** \(I\cap U^\perp\) (its section). This is a joint law for the *same* random normal, not two independently selected normals.

Set
\[
a=\arccos(1/3),\qquad b=\arccos(\sqrt5/3),\qquad c=\arccos(1/\sqrt5).
\]
Then the complete joint distribution, up to the probability-zero nongeneric orientations, is
\[
\begin{array}{c|c}
(S,T)&\mathbb P\{(S,T)\}\\\hline
(6,12)&15c/\pi-5\approx0.286245735244\\
(6,10)&15-15(a+b+c)/\pi\approx0.352163076316\\
(8,10)&15(2a+b-\pi)/\pi\approx0.238989468900\\
(10,10)&6-15a/\pi\approx0.122601719541
\end{array}
\]
and all other pairs have probability zero. Each of the four listed probabilities is strictly positive. In particular, **a twelve-sided central section forces a six-sided shadow**:
\[
\boxed{T(U)=12\Longrightarrow S(U)=6\quad\text{for every generic }U.}
\]
The conditional shadow law when \(T=12\) is thus deterministic, whereas the converse does not hold. The covariance is strictly negative and equals
\[
\operatorname{Cov}(S,T)
=\left(\frac{15c}{\pi}-5\right)\left(12-\frac{60b}{\pi}\right)
\approx-0.554392619780.
\]
The separate marginal laws are not asserted to be new; the finding is the exact **cooriented coupling**, especially the pointwise cone-containment implication.

## Assumptions and scope

The solid is the regular icosahedron with the stated coordinates and its center at the origin. The normal \(U\) has Haar (rotation-invariant) distribution on \(S^2\). A generic normal avoids all great circles orthogonal to a primal vertex and all great circles orthogonal to an outward facet normal. Such nongeneric sets have zero spherical area. Both the shadow and section use the same plane \(U^\perp\). The shadow is the full orthogonal projection, not merely the visible part of the front surface. Vertices refer to the noncollinear polygon corners; the direction of \(U\) and \(-U\) give the same pair.

## Proof

**1. Two sign arrangements.** Write \(V\) for one vector on each of the six antipodal vertex axes:
\[
\begin{split}
V={}&\{(0,1,\pm\varphi),(1,\pm\varphi,0),(\varphi,0,\pm1)\}.
\end{split}
\]
Write \(A\) for one outward normal on each of the ten antipodal pairs of triangular facets:
\[
\begin{split}
A={}&\{(1,\pm1,\pm1),\\
& (0,\varphi,\pm\varphi^{-1}),\ (\varphi,\pm\varphi^{-1},0),\ (\varphi^{-1},0,\pm\varphi)\}.
\end{split}
\]
All vectors of \(V\) have common square norm \(\varphi+2\); all vectors of \(A\) have square norm three. The twenty oriented facet normals are \(A\cup(-A)\), and the twelve primal vertices are \(V\cup(-V)\). In each arrangement, no three distinct representative axes are coplanar with the origin: their determinants lie in \(\mathbb Q(\sqrt5)\) and are nonzero, as certified exhaustively by `verify.py`.

For a generic \(u\), the central section crosses precisely those thirty *primal* edges whose endpoint inner products with \(u\) have opposite signs. Thus \(T(u)\) is an edge-cut statistic determined by the six signs of \(u\cdot v\), \(v\in V\). Similarly, an edge of the projected silhouette is the shared primal edge between a front-facing and back-facing *facet*; equivalently, two adjacent outward facet normals have opposite signs of their inner products with \(u\). Thus \(S(u)\) is the edge-cut statistic of the thirty-edge dual dodecahedral graph, determined by the ten signs \(u\cdot a\), \(a\in A\). These are different great-circle arrangements on the same normal sphere.

**2. Exhaustive exact chamber procedure.** For an arrangement of \(m\) great circles with no triple concurrence, every chamber vertex is one of the \(m(m-1)\) oriented pairwise crosses \(\pm(a_i\times a_j)\). The four local sectors at each crossing generate precisely the nonempty sign masks, and every closed chamber is the spherical convex hull of its eligible cross products. The `verify.py` certificate computes all dot-product signs exactly in \(\mathbb Q(\sqrt5)\), using integer/rational comparison of coefficients against \(\sqrt5\), rather than floating tolerances. It reconstructs all twenty triangular facets, thirty primal edges and thirty dual edges from the coordinate model. For the six vertex-normal circles it exhaustively obtains 32 chambers: twenty spherical triangles with \(T=12\), and twelve spherical pentagons with \(T=10\). For the ten facet-normal circles it exhaustively obtains 92 chambers: twenty spherical hexagons with \(S=6\), sixty spherical triangles with \(S=8\), and twelve spherical pentagons with \(S=10\). The observed counts also equal \(m(m-1)+2\), the exact Euler count for simple great-circle arrangements, completing the exhaustive enumeration argument.

**3. Pointwise coupling by exact cone containment.** For each of the twenty vertex-normal triangular chambers having \(T=12\), take its three oriented cross-product extreme rays. The exact certificate finds one facet-normal sign mask that is nonnegative on *all three* rays. Every vector in the chamber's positive convex cone is a positive combination of these rays. Because the sign conditions are homogeneous linear inequalities, the entire triangular chamber lies in that one facet-normal shadow chamber. The containing shadow chamber is among the twenty with \(S=6\). This proves the pointwise implication \(T=12\Rightarrow S=6\). It is a certificate of cone inclusion for *all* orientations in twenty open regions; it is not inferred from finite random samples or the two marginal laws.

**4. Exact spherical areas.** The same exact dot products determine every interior angle at every enumerated chamber vertex. For the shadow arrangement, the three chamber types have respectively:

- a hexagon with three angles \(\pi-a\) and three angles \(\pi-b\);
- a triangle with two angles \(a\) and one angle \(b\);
- a pentagon with five angles \(\pi-a\).

By the spherical excess formula, their areas are \(2\pi-3a-3b\), \(2a+b-\pi\), and \(2\pi-5a\). In the section arrangement, each of the twenty \(T=12\) triangles has three angles \(c\), hence area \(3c-\pi\); each of the twelve \(T=10\) pentagons has five angles \(\pi-c\), hence area \(2\pi-5c\). Multiplying by the chamber multiplicities and dividing by the full area \(4\pi\) gives
\[
\begin{split}
\mathbb P(S=6)&=10-15(a+b)/\pi,\\
\mathbb P(S=8)&=15(2a+b-\pi)/\pi,\\
\mathbb P(S=10)&=6-15a/\pi,\\
\mathbb P(T=12)&=15c/\pi-5.
\end{split}
\]
The implication proved in step 3 gives \(\mathbb P(S=6,T=12)=\mathbb P(T=12)\), and it forces the other two \(T=12\) cells to have zero probability. Subtraction gives the displayed four joint cells. Four explicit generic rational normal vectors, respectively \((-3,-2,0)\), \((-3,-3,-3)\), \((-3,-3,-1)\), and \((-3,0,-2)\), give the pairs \((6,10)\), \((6,12)\), \((8,10)\), and \((10,10)\). Their exactly nonzero inner products with every vertex and facet normal prove that each outcome holds on an open patch of the sphere, and hence has positive probability. The four probabilities sum to one.

**5. Moment and covariance check.** All thirty primal icosahedron edges subtend angle \(c\) at the center, because adjacent vertices have normalized inner product \(1/\sqrt5\). A Haar-uniform plane separates the two endpoints of a given edge with probability \(c/\pi\). Hence linearity gives \(\mathbb ET=30c/\pi\). Likewise, all thirty adjacent pairs of dual facet normals subtend angle \(b\), since their normalized inner product is \(\sqrt5/3\), and the same crossing argument yields \(\mathbb ES=30b/\pi\). In either case, these Crofton identities agree with the area computations. Since \(T=10+2\mathbf1_{\{T=12\}}\) and \(S=6\) on that event, elementary covariance calculation yields \(\operatorname{Cov}(S,T)=2\mathbb P(T=12)(6-\mathbb ES)\), the claimed negative expression.

## Verification

Run `python3 verify.py` using only the Python standard library. Its exact arithmetic reconstructs the icosahedron graph and the dual dodecahedron graph, checks all pairwise great-circle intersections have no triple concurrence, enumerates the 92 shadow chambers and 32 section chambers, determines each chamber's silhouette or section vertex count from independently reconstructed edge cuts, verifies all angle signatures, and tests every extreme ray of each of the 20 \(T=12\) cones against its containing \(S=6\) sign mask. It verifies generic integer-coordinate witnesses for all four joint outcomes, then evaluates the closed-form spherical-excess probabilities and the independent Crofton mean check. The final output line is `ALL_CHECKS_PASSED`. Every combinatorial, containment, and sign assertion is exact in \(\mathbb Q(\sqrt5)\). Floating point is used only for the displayed inverse-trigonometric numerical probabilities, not for the exhaustive certificate.

## Relationship to prior work

Black and Criado (arXiv:2406.06936, first public June 11, 2024) study general quantitative bounds for random shadows of fixed polytopes, including their normal-fan interpretation, but do not calculate the cooriented shadow–section joint law of this regular icosahedron. Böröczky and Henk's *Random Projections of Regular Polytopes* (1997 preprint) studies regular simplex/cube/crosspolytope projection families, not this icosahedral coupled statistic. Kabluchko and Seidel (arXiv:2006.09492) develop conic methods for regular simplex, cube and crosspolytope sections and projections, not the present joint polygon-count problem. De Loera, Lopez-Campos, and Torres (arXiv:2412.12419, first posted December 17, 2024) study possible section vertex counts rather than a cooriented joint Haar law.

Most importantly, the **separate** regular-icosahedron central-section law is already available as *Exact Haar polygon-type law for central icosahedron sections* (2026), and the **separate** regular-icosahedron shadow law is equivalent by polarity to the previously computed regular-dodecahedron central-section law. The previously known six-circle and ten-circle tessellations and their separate spherical-area distributions therefore do **not** establish originality for the individual marginals. The proposed distinguishing result is the exact containment of twenty triangular section normal cones in shadow hexagon cones, which determines the four joint probabilities, the two forbidden couplings, and the covariance. Neither marginal by itself nor their combination logically determines that containment. Historical priority for the joint theorem remains provisional.

## Limitations

The theorem is for the regular icosahedron and *the same* Haar-uniform central plane in both operations. Nongeneric normals meeting an original vertex or having a facet parallel to the cutting plane are excluded from the pointwise classification; they form a set of probability zero. Noncentral cuts, scaled or deformed icosahedra, independent shadow and section normals, and distributions of areas, edge lengths and angles are outside the theorem. The known marginal results and the basic spherical arrangements are not claimed as new; an equivalent earlier joint cone-refinement calculation may exist in less accessible stereological literature.

## References

1. Alexander E. Black and Francisco Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936, first public June 11, 2024, https://arxiv.org/abs/2406.06936.
2. Károly Böröczky Jr. and Martin Henk, *Random Projections of Regular Polytopes*, preprint SC 97-21 (May 1997), https://page.math.tu-berlin.de/~henk/preprints/boeroeczky%20henk%26random%20projections%20of%20regular%20polytopes.pdf.
3. Zakhar Kabluchko and Hauke Seidel, *Convex cones spanned by regular polytopes*, arXiv:2006.09492, first public June 16, 2020, https://arxiv.org/abs/2006.09492.
4. Jesús A. De Loera, Gyivan Lopez-Campos and Antonio J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419, first public December 17, 2024, https://arxiv.org/abs/2412.12419.
5. *Exact Haar polygon-type law for central icosahedron sections* (2026), published research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-haar-polygon-type-law-for-central-icosahedron-sections--65970a533c4f.
