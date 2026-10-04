# Exact two-disk covering radius of every regular even polygon

## Finding

Let \(P_n\) be a regular even \(n\)-gon with \(n\ge 4\) and circumradius \(R\). Define \(\rho_2(P_n)\) to be the least \(r\) for which two closed Euclidean disks of radius \(r\) have union containing all of \(P_n\). Then
\[
\rho_2(P_n)=R\sqrt{1-\frac34\sin^2\!\left(\frac{\pi}{n}\right)}.
\]

The optimizer is completely classified. Up to a dihedral symmetry of \(P_n\) and exchange of the two disks, cut the boundary at the midpoints of a pair of opposite sides and cover the two resulting half-polygons. Put
\[
a=R\cos\!\left(\frac{\pi}{n}\right),\qquad
b=R\sin\!\left(\frac{\pi}{n}\right).
\]
After rotating coordinates so the cut midpoints are \((0,a)\) and \((0,-a)\), the optimal centers are
\[
\left(-\frac b2,0\right)\quad\text{and}\quad
\left(\frac b2,0\right),
\]
and the common radius is
\[
\sqrt{a^2+\frac{b^2}{4}}
=R\sqrt{1-\frac34\sin^2\!\left(\frac{\pi}{n}\right)}.
\]

For example, a unit square has optimal radius \(\sqrt5/4\). For a regular hexagon of circumradius \(R\), the optimal radius is \(\sqrt{13}\,R/4\).

## Assumptions and scope

The problem is the continuous planar two-center problem for the whole polygon, not merely for its vertices. The polygon is regular and has an even number of sides. The disks may overlap and their centers are unrestricted.

Choi, Jeong, and Ahn study exactly the continuous convex-polygon two-center problem and give an \(O(n\log n)\)-time algorithm. A key structural observation in their paper is that whenever two congruent disks cover a convex polygon, one disk can be assigned a connected subchain of the polygon boundary and the other disk the complementary connected subchain. The present result uses that structural reduction and solves the regular even family in closed form.

## Proof

Write
\[
\alpha=\frac{\pi}{n},\qquad
a=R\cos\alpha,\qquad
b=R\sin\alpha.
\]
Orient \(P_n\) so one side is the horizontal segment from
\[
A=(-b,a)\quad\text{to}\quad V=(b,a).
\]

Consider any cover of \(P_n\) by two congruent disks of radius \(r\). By the connected-subchain reduction for convex-polygon two-center covers, the boundary can be split into two complementary connected subchains, one covered by each disk. Their boundary lengths add to the perimeter, so at least one of them has length at least one half of the perimeter. That chain contains a boundary subchain of exactly half the perimeter.

Central symmetry of a regular even polygon sends every boundary point to the point half a perimeter away. Let the initial point of such a half-perimeter subchain be
\[
x=(t,a),\qquad -b\le t\le b.
\]
Its other endpoint is \(-x=(-t,-a)\). Choose the half-chain that runs along the left side of the polygon. It contains
\[
A=(-b,a)\quad\text{and}\quad B=(-b,-a).
\]
Therefore its diameter is at least
\[
\max\!\left\{
\sqrt{4a^2+(b+t)^2},
\sqrt{4a^2+(b-t)^2}
\right\}.
\]
The larger of \(b+t\) and \(b-t\) is \(b+|t|\), so this diameter is at least
\[
\sqrt{4a^2+(b+|t|)^2}
\ge
\sqrt{4a^2+b^2}.
\]
Any disk containing the chain has radius at least half its diameter. Hence every two-disk cover satisfies
\[
r\ge \sqrt{a^2+\frac{b^2}{4}}.
\]

It remains to attain the bound. Cut at the midpoints
\[
p=(0,a),\qquad q=(0,-a)
\]
of the chosen opposite sides. Consider the left half of \(P_n\), and set
\[
c=\left(-\frac b2,0\right),\qquad
\rho=\sqrt{a^2+\frac{b^2}{4}}.
\]
The four boundary points \(p,A,B,q\) lie on the circle centered at \(c\) of radius \(\rho\). Every other original vertex \((u,v)\) on the left boundary satisfies
\[
u^2+v^2=R^2,\qquad u\le -b.
\]
Thus
\[
\left\|(u,v)-c\right\|^2
=\left(u+\frac b2\right)^2+v^2
=R^2+bu+\frac{b^2}{4}
\le
R^2-\frac{3b^2}{4}
=\rho^2.
\]
The disk is convex, so it contains the entire left half-polygon. Its centrally symmetric mate contains the right half-polygon. Hence two disks of radius \(\rho\) cover \(P_n\), proving equality.

For uniqueness, equality in the lower-bound estimate requires \(t=0\). If one assigned boundary chain were longer than half the perimeter, it would contain a nontrivial interval of half-perimeter subchains; at most isolated starts are side midpoints, so one of those subchains would have \(t\ne0\) and would force a radius strictly larger than \(\rho\). Thus, in an optimal cover both assigned chains have exactly half the perimeter, and their cut points are midpoints of opposite sides.

For the left optimal half-chain, the pairs
\[
\{p,B\}\quad\text{and}\quad\{A,q\}
\]
both have distance \(2\rho\) and have the same midpoint \(c\). Any disk of radius \(\rho\) containing either diameter pair must be centered at that midpoint. The right center is forced by the symmetric argument. This proves the optimizer classification.

## Verification

The lower bound uses only three ingredients: the connected-boundary-subchain reduction for convex-polygon two-center covers, central symmetry of a regular even polygon, and the elementary fact that a disk containing two points at distance \(d\) has radius at least \(d/2\).

The upper bound was checked algebraically at every vertex. For a left-boundary vertex, \(u\le-b\) makes
\[
R^2+bu+\frac{b^2}{4}
\le
R^2-\frac{3b^2}{4}.
\]
The cut-side endpoints are equality cases. Convexity then upgrades vertex containment to containment of the full half-polygon.

The formula also passes two direct checks:
\[
\rho_2(P_4)=\frac{\sqrt5}{4}
\]
for a unit square, and
\[
\rho_2(P_6)=\frac{\sqrt{13}}{4}R
\]
for a regular hexagon of circumradius \(R\).

## Relationship to prior work

The directly relevant convex-polygon literature is algorithmic. Choi, Jeong, and Ahn give an \(O(n\log n)\)-time exact algorithm for arbitrary convex polygons and explicitly reduce a feasible cover to two complementary connected boundary subchains. Their full text does not state a special closed formula for regular polygons.

Earlier algorithms of Shin and collaborators and of Kim and Shin also solve the general convex-polygon two-center problem algorithmically. A later planar two-center algorithm likewise treats arbitrary convex polygons and sets of points in convex position. Targeted searches of these sources and of indexed research records did not locate the formula or the optimizer classification above.

The distinction between covering the vertices and covering the whole polygon is substantive. In the polygon problem, points in the relative interiors of the two cut sides force the offset centers and the radius above; the proof therefore does not reduce to a finite vertex two-center computation.

## Limitations

The theorem covers regular even polygons only. It does not classify regular odd polygons, arbitrary centrally symmetric polygons, unequal-radius two-disk covers, or covers by more than two disks. The originality check was targeted rather than exhaustive: because the derivation is elementary once the connected-subchain structure is known, an equivalent special-case formula could exist in older or differently indexed geometry literature.

## References

J. Choi, D. Jeong, and H.-K. Ahn, “Covering Convex Polygons by Two Congruent Disks,” arXiv:2105.02483, first submitted 2021-05-06.

S. W. Kim and C.-S. Shin, “Efficient algorithms for two-center problems for a convex polygon,” Proceedings of the 11th International Symposium on Algorithms and Computation, 2000.

“An Optimal and Practical Algorithm for the Planar 2-center Problem,” Theory of Computing Systems, DOI 10.1007/s00224-025-10228-9.
