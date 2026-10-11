# Erdős's circle conjecture is exact on all parallelograms
## Finding
For a planar convex body \(K\), define \(N(K)\) to be the least integer \(N\) for which there exists a point
\[
P\in\partial K
\]
such that every Euclidean circle centered at \(P\) intersects \(\partial K\) in at most \(N\) points.

For every nondegenerate Euclidean parallelogram \(Q\),
\[
\boxed{N(Q)=2}.
\tag{1}
\]

More strongly, every nonobtuse vertex of \(Q\) is a witnessing center: every circle centered at that vertex meets the boundary of \(Q\) in at most two points.

Thus Erdős's original proposed constant \(2\), false for general convex curves, is nevertheless exact on the complete class of Euclidean parallelograms.

## Assumptions and scope
A nondegenerate parallelogram is the convex hull
\[
Q=\operatorname{conv}\{P,P+a,P+b,P+a+b\},
\]
where \(a,b\in\mathbb R^2\) are linearly independent.

The invariant is Euclidean rather than affine: circles are not preserved by general affine maps. Therefore the assertion for all parallelograms is not reduced to the square by affine equivalence.

A parallelogram has two acute and two obtuse vertices unless it is a rectangle, in which case all four vertices are right. Hence it always has at least one nonobtuse vertex.

## Proof
Choose a nonobtuse vertex \(P\) and translate so that
\[
P=0.
\]
Let \(a\) and \(b\) be the adjacent side vectors. Since the angle between them is at most \(\pi/2\),
\[
a\cdot b\ge0.
\tag{2}
\]

The boundary of \(Q\) is the union of the two polygonal chains
\[
C_a:
0\longrightarrow a\longrightarrow a+b
\]
and
\[
C_b:
0\longrightarrow b\longrightarrow a+b.
\]

On the first edge of \(C_a\), points have the form
\[
ta,\qquad 0\le t\le1,
\]
and their distance from the origin is
\[
t\lVert a\rVert,
\]
which is strictly increasing.

On the second edge of \(C_a\), points have the form
\[
a+tb,\qquad 0\le t\le1.
\]
Their squared distance from the origin is
\[
f(t)=\lVert a+tb\rVert^2,
\]
and
\[
f'(t)
=
2a\cdot b+2t\lVert b\rVert^2.
\tag{3}
\]
By (2), equation (3) is nonnegative on \([0,1]\), and it is strictly positive for every \(t>0\). Thus the distance from \(0\) is strictly increasing along all of \(C_a\).

Exactly the same argument on \(C_b\) gives
\[
\frac{d}{dt}\lVert b+ta\rVert^2
=
2a\cdot b+2t\lVert a\rVert^2\ge0,
\]
so distance from \(0\) is strictly increasing along \(C_b\) as well.

Fix a radius \(r\ge0\). Since distance from \(0\) is strictly increasing along each chain, the circle
\[
S_r(0)=\{x:\lVert x\rVert=r\}
\]
meets \(C_a\) in at most one point and \(C_b\) in at most one point. Consequently
\[
\#\bigl(S_r(0)\cap\partial Q\bigr)\le2
\]
for every \(r\). Therefore
\[
N(Q)\le2.
\tag{4}
\]

For the reverse inequality, let \(P\in\partial Q\) be arbitrary. If \(P\) lies in the relative interior of a side, then every sufficiently small circle centered at \(P\) intersects that side once on each side of \(P\), giving two boundary intersections. If \(P\) is a vertex, then every sufficiently small centered circle meets each of the two incident sides once. Hence every boundary point \(P\) admits some centered circle meeting \(\partial Q\) in at least two points. Therefore
\[
N(Q)\ge2.
\tag{5}
\]

Combining (4) and (5) proves (1).

## Verification
The argument is exact and uses only the monotonicity of squared distance along two line segments.

The supplied `verify.py` checks the derivative identities symbolically and independently sweeps deterministic parallelograms with acute, right, and highly sheared geometries. For each chosen nonobtuse vertex it enumerates all critical radii determined by vertices and perpendicular projections to edges, samples every interval between consecutive critical radii, and verifies that no circle has more than two boundary intersections.

Those finite checks are regression tests only. The quantified theorem follows from equations (2)--(5).

## Relationship to prior work
Bárány and Roldán-Pensado formalized this circle-intersection invariant after revisiting Erdős's 1946 conjecture. Erdős had proposed the universal bound
\[
N(K)\le2,
\]
which fails in general. Their paper exhibits bodies with value \(6\), proves finiteness for every planar convex body, and notes that acute triangles and regular odd polygons already force four intersections at every boundary center.

The same authors' thesis-era treatment and journal article do not state a parallelogram theorem; targeted full-text checks found no occurrence of “parallelogram” or “centrally symmetric.” A later polygon-complexity bound gives only
\[
N(Q)\le4
\]
for arbitrary convex quadrilaterals. The result here is therefore a strict strengthening on the natural centrally symmetric quadrilateral class.

Targeted searches under “parallelogram,” “centrally symmetric quadrilateral,” the notation \(N(K)\), “circle centered at a vertex,” and the Erdős circle-intersection problem did not locate a published implication-equivalent statement.

## Limitations
The proof uses the parallelism of opposite sides. It does not show that every centrally symmetric convex body, every centrally symmetric polygon, or every convex quadrilateral has \(N=2\).

The conclusion is Euclidean and is not an affine invariant of a general convex body, because affine maps send circles to ellipses.

The proof is short enough that the result may have circulated as an unindexed observation or exercise. That is the principal residual originality risk.

The source problem has earlier thesis material dated only by month; the exact source date recorded with this result is the earliest exact public date verified for the journal version, rather than an invented day for the month-only thesis evidence.

## References
1. I. Bárány and E. Roldán-Pensado, *A Question from a Famous Paper of Erdős*, *Discrete & Computational Geometry* 50 (2013), 253--261. DOI: 10.1007/s00454-013-9507-z.
2. E. Roldán Pensado, *Problems in Convex Geometry*, doctoral thesis, University College London, 2013, Chapter 3.
3. P. Erdős, *On sets of distances of \(n\) points*, *American Mathematical Monthly* 53 (1946), 248--250.
