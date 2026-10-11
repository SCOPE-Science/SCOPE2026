# Exact Erdős circle-intersection invariant of regular odd polygons
## Finding
For a planar convex body \(K\), define \(N(K)\) to be the least integer \(N\) for which there exists a boundary point \(P\in\partial K\) such that every Euclidean circle centered at \(P\) intersects \(\partial K\) in at most \(N\) points.

Let \(P_n\) be a regular \(n\)-gon with odd \(n=2k+1\ge3\). Then
\[
N(P_n)=4.
\]
In fact, every vertex is a witnessing point for the upper bound. If \(V\) is a vertex, \(M\) is the midpoint of the side opposite \(V\), and \(W\) is either of the two farthest vertices from \(V\), then every radius \(r\) satisfying
\[
VM<r<VW
\]
gives exactly four intersections of the circle centered at \(V\) with \(\partial P_n\).

## Assumptions and scope
The polygon is Euclidean, regular, and has an odd number \(n=2k+1\ge3\) of sides. Intersections are counted as distinct boundary points. No statement is made here about even regular polygons or arbitrary convex polygons.

The lower bound \(N(P_n)\ge4\) uses a published fact of Bárány and Roldán-Pensado: for every point on the boundary of a regular odd polygon there exists a centered circle meeting the boundary in four points. The upper bound below is independent and elementary.

## Proof
Scale the circumradius to \(1\). Put
\[
\alpha=\frac{2\pi}{n},\qquad
V_j=(\cos(j\alpha),\sin(j\alpha)),\qquad V=V_0=(1,0),
\]
with indices increasing counterclockwise. Let \(M=(V_k+V_{k+1})/2\), the midpoint of the side opposite \(V_0\). The boundary is the union of two reflected polygonal arcs from \(V_0\) to \(M\). It suffices to control the distance to \(V_0\) on one arc
\[
V_0V_1\cdots V_kM.
\]

For \(0\le j\le k-1\), parameterize the edge \([V_j,V_{j+1}]\) by
\[
X_j(s)=V_j+s(V_{j+1}-V_j),\qquad 0\le s\le1,
\]
and set \(q_j(s)=\lVert X_j(s)-V_0\rVert^2\). Then \(q_j''(s)=2\lVert V_{j+1}-V_j\rVert^2>0\), while
\[
q_j'(0)=4\sin\!\left(\frac\alpha2\right)
\left[
\sin\!\left(\left(j+\frac12\right)\alpha\right)-\sin\!\left(\frac\alpha2\right)
\right].
\]
For \(j=0\) this is \(0\), and for \(1\le j\le k-1\) it is positive because
\[
\frac{3\alpha}{2}\le \left(j+\frac12\right)\alpha\le \pi-\alpha
\]
and the sine on this interval is strictly larger than \(\sin(\alpha/2)\). Hence the distance from \(V_0\) is strictly increasing along every edge from \(V_0\) through \(V_k\).

On the opposite side \([V_k,V_{k+1}]\), the squared distance from \(V_0\) is a strictly convex quadratic symmetric about the midpoint \(M\). Therefore it is strictly decreasing from \(V_k\) to \(M\). Thus, along the arc \(V_0V_1\cdots V_kM\), the distance from \(V_0\) rises strictly from \(0\) to \(V_0V_k\) and then falls strictly to \(V_0M\). Any radius therefore occurs at most twice on this arc. Reflection gives the same conclusion on the other arc, so any circle centered at \(V_0\) meets the whole boundary in at most four points.

Moreover, if \(V_0M<r<V_0V_k\), the increasing portion of each arc contributes exactly one point and the final half of the opposite side contributes exactly one point. Hence such a circle has exactly four intersections. Consequently the maximum intersection count at a vertex is exactly four, and in particular \(N(P_n)\le4\).

Bárány and Roldán-Pensado state that every boundary point of a regular \(2k+1\)-gon is the center of a circle intersecting the boundary in four points. Therefore no boundary point can witness an upper bound below four, so \(N(P_n)\ge4\). Combining the two bounds proves \(N(P_n)=4\).

## Verification
The edge derivative identity above was rederived directly from dot products of the regular-polygon vertices. A standalone checker included with this result samples odd orders from \(3\) through \(31\), verifies the derivative signs and the opposite-edge symmetry numerically, and directly counts four intersections for representative radii in the open interval \(V_0M<r<V_0V_k\). These computations are consistency checks only; the proof is the analytic argument above.

The primary source was inspected in full-text form. Its introduction defines \(N(K)\), states the four-intersection property for every boundary point of a regular odd polygon, proves only general finiteness globally, and later constructs a body with \(N(K)=6\). It does not state the exact value \(N(P_n)=4\) for the regular odd family.

## Relationship to prior work
Bárány and Roldán-Pensado introduced the invariant in this form and explicitly observed the lower-bound phenomenon for regular odd polygons: every boundary point supports a four-intersection centered circle. Their paper also proves \(N(K)<\infty\) for every planar convex body and exhibits an example with \(N(K)=6\). The present result closes the regular odd-polygon case exactly by adding a uniform four-intersection upper bound at every vertex.

A published published-finding corpus record gives the broader but weaker polygonal estimate \(N(K)\le2n-4\) for an arbitrary convex \(n\)-gon and exact values for triangles. For regular odd \(n\ge5\), that bound is strictly weaker and does not imply the present theorem.

## Limitations
The proof exploits the one-peak distance profile from a vertex of a regular odd polygon. It does not classify which nonvertex boundary points have maximum intersection count exactly four, and it does not determine \(N\) for even regular polygons or general polygon classes. The originality search cannot exclude an unindexed elementary observation under different terminology.

## References
1. I. Bárány and E. Roldán-Pensado, “A Question from a Famous Paper of Erdős,” *Discrete & Computational Geometry* 50 (2013), 253–261. DOI: `10.1007/s00454-013-9507-z`. Published online 2013-05-08. Primary MSC listed by the paper: `52C10`.
