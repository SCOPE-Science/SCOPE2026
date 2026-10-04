# A polygon-complexity bound for the Erdős circle-intersection invariant
## Finding
For a planar convex body \(K\), define \(N(K)\) to be the least integer \(N\) for which there is a point \(P\in\partial K\) such that every circle centered at \(P\) meets \(\partial K\) in at most \(N\) distinct points.

If \(K\) is a convex \(n\)-gon with \(n\ge4\), then
\[
N(K)\le 2n-4.
\]
In particular, every convex quadrilateral satisfies \(N(K)\le4\), and every convex pentagon satisfies \(N(K)\le6\).

For triangles there is an exact classification. If \(T\) is a nondegenerate triangle, then
\[
N(T)=\begin{cases}
4,&\text{if }T\text{ is acute},\\
2,&\text{if }T\text{ is right or obtuse}.
\end{cases}
\]
Thus the right-angle threshold is the exact phase boundary for triangles.

## Assumptions and scope
All polygons are Euclidean, compact, convex, and nondegenerate. Intersections are counted as distinct boundary points, so a polygon vertex shared by two edges is counted once. Circles have positive radius. The result is a complexity-dependent bound; it does not establish a universal bound for arbitrary convex bodies or for polygons with an unbounded number of sides.

## Proof
Let \(K=V_0V_1\dots V_{n-1}\) be a convex \(n\)-gon with \(n\ge4\), with indices in cyclic order. Its interior angles sum to \((n-2)\pi\), so some interior angle is at least \(\pi/2\). Relabel so that
\[
\angle V_0V_1V_2\ge \frac{\pi}{2}.
\]
Use \(P=V_0\) as the circle center. Parameterize the edge \(V_1V_2\) by
\[
X(t)=V_1+t(V_2-V_1),\qquad 0\le t\le1.
\]
Then
\[
\frac{d}{dt}|X(t)-V_0|^2
=2(V_1-V_0)\cdot(V_2-V_1)+2t|V_2-V_1|^2.
\]
Because the angle at \(V_1\) is at least \(\pi/2\),
\[
(V_1-V_0)\cdot(V_2-V_1)
=-(V_0-V_1)\cdot(V_2-V_1)\ge0.
\]
Hence the distance from \(V_0\) is nondecreasing along \(V_1V_2\), beginning at \(|V_0V_1|\). Therefore, for every radius \(r>0\), the two-edge chain \(V_0V_1\cup V_1V_2\) contributes at most one distinct intersection with the circle centered at \(V_0\): the first edge can contribute only for \(r\le |V_0V_1|\), the second only for \(r\ge |V_0V_1|\), and at equality they share the single vertex \(V_1\).

The other edge incident to \(V_0\), namely \(V_{n-1}V_0\), contributes at most one point. Each of the remaining \(n-3\) line segments contributes at most two points because a line meets a circle in at most two points. Consequently every circle centered at \(V_0\) has at most
\[
1+1+2(n-3)=2n-4
\]
intersections with \(\partial K\), proving the polygon bound.

Now let \(T=ABC\) be a triangle.

If \(T\) is right or obtuse, relabel so that \(\angle ABC\ge\pi/2\), and center circles at \(A\). As above, distance from \(A\) is nondecreasing along \(BC\), starting at \(|AB|\). Since \(AC\) is the side opposite the nonacute angle, \(|AC|>|AB|\). Thus for \(0<r<|AB|\), the circle meets \(AB\) and \(AC\) once each; for \(|AB|<r<|AC|\), it meets \(BC\) and \(AC\) once each; at the endpoint radii shared vertices are counted once. Hence no circle centered at \(A\) has more than two boundary intersections, while every sufficiently small circle centered at \(A\) has exactly two. Therefore \(N(T)=2\).

Suppose instead that \(T\) is acute. Centering at any vertex shows \(N(T)\le4\): the two incident edges contribute at most one intersection each and the opposite edge at most two. For the reverse inequality, take any \(P\in\partial T\), say \(P\in AB\). The distance function \(X\mapsto |X-P|\) on \(\partial T\) has every triangle vertex distinct from \(P\) as a strict local maximum. At \(A\) and \(B\) this follows from the acuteness of the corresponding angle; at \(C\), writing \(P=(1-s)A+sB\) gives, for motion from \(C\) toward \(A\),
\[
(C-P)\cdot(A-C)=-(1-s)|C-A|^2-s(C-B)\cdot(C-A)<0,
\]
and similarly toward \(B\), because \(\angle C<\pi/2\). Choose a level just below the second largest of these strict vertex maxima. Continuity on the three sides gives two crossings near each of two vertex maxima; if those vertices are adjacent, the strict dip on their common side separates the two crossings. Thus some circle centered at \(P\) meets \(\partial T\) in at least four distinct points. Since this holds for every \(P\in\partial T\), \(N(T)\ge4\), and therefore \(N(T)=4\).

## Verification
The proof is exact and analytic. The only quantitative step is the derivative of the squared distance along one edge; its sign follows directly from the nonacute-angle dot-product inequality. The intersection count then uses only the fact that a segment lies on a line and hence contributes at most two points to a circle.

For the acute-triangle lower bound, the local-maxima argument was checked independently of the literature statement: all relevant one-sided derivatives have the required signs under the three acute-angle hypotheses, and the common level is chosen below the second-largest vertex value so that two strict maxima each force two distinct crossings.

No finite experiment, enumeration, or numerical certificate is used to infer an infinite statement.

## Relationship to prior work
Bárány and Roldán-Pensado introduced the invariant \(N(K)\) in their study of an Erdős conjecture. They state that every boundary point of an acute triangle admits a centered circle with four boundary intersections, construct a convex \(15\)-gon with \(N(K)=6\), and prove that \(N(K)\) is finite for every planar convex body. They also report that no universal finite upper bound was known there.

The present result is different in implication. General finiteness does not give an explicit bound in terms of polygon complexity. The published acute-triangle observation supplies a lower phenomenon but does not give the nonacute classification, the \(2n-4\) polygon bound, or its quadrilateral and pentagon consequences. Targeted searches for the invariant together with triangle type, quadrilateral, pentagon, and the exact expression \(2n-4\) did not locate a covering statement.

## Limitations
The bound \(2n-4\) is not claimed to be sharp for every \(n\), nor is a complete classification of quadrilaterals or pentagons claimed. In particular, the result does not settle the conjectured universal bound for all convex bodies. An equivalent elementary observation could exist in unindexed notes or follow-up discussions despite not appearing in the materially inspected primary article and thesis chapter.

The UCL thesis is dated March 2013, but an exact public-deposit day was not verified. The exact public date used for the source anchor is therefore the journal article's documented online publication date, 2013-05-08.

## References
I. Bárány and E. Roldán-Pensado, *A Question from a Famous Paper of Erdős*, Discrete & Computational Geometry 50 (2013), 253–261, DOI 10.1007/s00454-013-9507-z. Online publication: 2013-05-08.

E. Roldán Pensado, *Problems in Convex Geometry*, University College London doctoral thesis, March 2013, Chapter 3.
