# Four barriers determine the exact Euclidean inradius of consecutive-layer S-hypersimplices
## Finding
Let
\[
d\ge2,
\qquad
0\le a<b\le d
\]
be integers, and let
\[
P_{d;a,b}
=
\Delta(d,\{a,a+1,\ldots,b\})
\]
be the consecutive-layer \(S\)-hypersimplex.

Then
\[
\boxed{
P_{d;a,b}
=
[0,1]^d
\cap
\left\{
x\in\mathbb R^d:
a\le\sum_{i=1}^d x_i\le b
\right\}.
}
\tag{1}
\]

Its standard Euclidean inradius is
\[
\boxed{
r_{\mathrm{in}}(P_{d;a,b})
=
r_*
=
\min\left\{
\frac12,\,
\frac{b}{d+\sqrt d},\,
\frac{d-a}{d+\sqrt d},\,
\frac{b-a}{2\sqrt d}
\right\}.
}
\tag{2}
\]

The complete set of centers of largest inscribed balls is
\[
\boxed{
\mathcal I_{d;a,b}
=
\left\{
c\in\mathbb R^d:
r_*\le c_i\le1-r_*\ \text{for all }i,\quad
a+r_*\sqrt d
\le
\sum_i c_i
\le
b-r_*\sqrt d
\right\}.
}
\tag{3}
\]

The incenter is unique if and only if the minimum in (2) is attained by at least one of the first three barriers
\[
\frac12,\qquad
\frac{b}{d+\sqrt d},\qquad
\frac{d-a}{d+\sqrt d}.
\tag{4}
\]
Equivalently, nonuniqueness occurs exactly when
\[
\frac{b-a}{2\sqrt d}
<
\min\left\{
\frac12,\,
\frac{b}{d+\sqrt d},\,
\frac{d-a}{d+\sqrt d}
\right\}.
\tag{5}
\]
In that strict slab-width regime,
\[
\dim\mathcal I_{d;a,b}=d-1.
\tag{6}
\]

The four terms in (2) have distinct geometric meanings:
- \(\frac12\) is the cube-width barrier;
- \(\frac{b}{d+\sqrt d}\) is the competition between the lower coordinate walls and the upper sum wall;
- \(\frac{d-a}{d+\sqrt d}\) is the reflected competition between the upper coordinate walls and the lower sum wall;
- \(\frac{b-a}{2\sqrt d}\) is half the Euclidean distance between the two parallel sum walls.

Thus a family introduced by selecting consecutive Hamming layers of the cube has an exact four-phase Chebyshev geometry.

## Assumptions and scope
The result is for the full-dimensional consecutive-layer case
\[
0\le a<b\le d.
\]
The metric is the standard Euclidean metric in \(\mathbb R^d\).

The \(S\)-hypersimplex is used in the coordinate realization of Manecke--Sanyal--So: it is the convex hull of all \(0/1\)-vectors whose coordinate sum belongs to the chosen set \(S\).

The theorem does not claim the same formula for a nonconsecutive set \(S\), where additional gaps between Hamming layers change the convex hull.

## Proof
By definition,
\[
P_{d;a,b}
=
\operatorname{conv}
\left\{
x\in\{0,1\}^d:
a\le\sum_i x_i\le b
\right\}.
\tag{7}
\]
Every point in (7) lies in the right-hand side of (1), so only the reverse containment needs proof.

Consider
\[
Q=
[0,1]^d
\cap
\left\{
a\le\sum_i x_i\le b
\right\}.
\]
Every vertex of \(Q\) is a \(0/1\)-vector. Indeed, if a point of \(Q\) has two fractional coordinates, one can perturb those two coordinates by opposite sufficiently small amounts while preserving their sum and all inequalities, so the point is not a vertex. If it has exactly one fractional coordinate and neither sum wall is active, that coordinate itself can be perturbed. If exactly one fractional coordinate remains and a sum wall is active, then its value is an integer minus a sum of \(0/1\) coordinates, hence is integral, a contradiction. Thus all vertices of \(Q\) belong to the set in (7), proving (1).

Let a Euclidean ball of radius \(r\), centered at \(c\), be contained in \(P_{d;a,b}\). The coordinate halfspaces give
\[
c_i\ge r,
\qquad
1-c_i\ge r
\qquad
(1\le i\le d).
\tag{8}
\]
The normal of either sum wall is \(\mathbf1\), of norm \(\sqrt d\), so the two slab constraints give
\[
\sum_i c_i-a\ge r\sqrt d,
\qquad
b-\sum_i c_i\ge r\sqrt d.
\tag{9}
\]

Conversely, (8)--(9) are sufficient, because they are exactly the Euclidean distance conditions for the ball to lie in every halfspace of the description (1). Therefore a radius \(r\) is feasible exactly when there exists \(c\) satisfying
\[
r\le c_i\le1-r
\]
and
\[
a+r\sqrt d
\le
\sum_i c_i
\le
b-r\sqrt d.
\tag{10}
\]

The box constraint implies
\[
dr\le\sum_i c_i\le d(1-r).
\tag{11}
\]
Hence a feasible center exists exactly when the intervals
\[
[dr,d(1-r)]
\]
and
\[
[a+r\sqrt d,b-r\sqrt d]
\]
intersect.

Two closed intervals intersect exactly when each left endpoint is no larger than each right endpoint. The four resulting inequalities are
\[
dr\le d(1-r),
\tag{12}
\]
\[
dr\le b-r\sqrt d,
\tag{13}
\]
\[
a+r\sqrt d\le d(1-r),
\tag{14}
\]
and
\[
a+r\sqrt d\le b-r\sqrt d.
\tag{15}
\]
They are respectively equivalent to the four upper bounds in (2). This proves the upper bound.

Conversely, if \(r\) satisfies all four bounds, choose any
\[
s
\in
[dr,d(1-r)]
\cap
[a+r\sqrt d,b-r\sqrt d]
\]
and put
\[
c=\frac{s}{d}\mathbf1.
\]
Then (8)--(9) hold, so a radius-\(r\) ball is contained in the polytope. This proves (2).

At the optimal radius, conditions (8)--(9) themselves give exactly the set (3).

If \(r_*=\frac12\), the box is already the singleton \(\{\frac12\mathbf1\}\). If
\[
r_*=\frac{b}{d+\sqrt d},
\]
then
\[
b-r_*\sqrt d=dr_*,
\]
and the upper sum condition plus \(c_i\ge r_*\) forces \(c=r_*\mathbf1\). If
\[
r_*=\frac{d-a}{d+\sqrt d},
\]
then
\[
a+r_*\sqrt d=d(1-r_*),
\]
and the lower sum condition plus \(c_i\le1-r_*\) forces \(c=(1-r_*)\mathbf1\). These conclusions remain valid in tie cases.

Conversely, if the slab-width term is the strict minimum, then
\[
a+r_*\sqrt d=b-r_*\sqrt d=\frac{a+b}{2},
\]
while strictness against the other three barriers gives
\[
dr_*<\frac{a+b}{2}<d(1-r_*),
\qquad
r_*<\frac12.
\]
Thus (3) is a nondegenerate hyperplane slice of the box, of dimension \(d-1\). This proves the uniqueness classification.

## Verification
The proof is exact and arbitrary-dimensional. It uses only the defining vertex set of the \(S\)-hypersimplex and elementary Euclidean distances to the cube and slab halfspaces.

The source-dependent premise was checked directly in the primary full text: Manecke--Sanyal--So define an \(S\)-hypersimplex as the convex hull of the \(0/1\)-vectors whose coordinate sum lies in \(S\), and develop its vertices, edges, facets, and canonical decompositions.

The accompanying `verify.py` checks every integer pair
\[
0\le a<b\le d
\]
for \(2\le d\le100\). It verifies all four barrier inequalities, constructs a symmetric optimal center, checks every halfspace-distance condition, and verifies the uniqueness/nonuniqueness criterion by endpoint identities. The finite computation is corroborative only.

## Relationship to prior work
Manecke, Sanyal, and So introduce and study \(S\)-hypersimplices, including their vertices, edges, facets, dissections, pulling triangulations, and monotone path polytopes. Their inspected full text contains no occurrence of “inradius”, “Chebyshev”, or “Euclidean”.

A published-result record on the same consecutive-layer subfamily determines its one-skeleton shortest-path metric and graph diameter. That is a distinct invariant: graph distance between vertices does not imply the radius of a largest ambient Euclidean ball, nor the complete set of Chebyshev centers.

Targeted published-result and literature searches used the object names “\(S\)-hypersimplex” and “consecutive-layer \(S\)-hypersimplex” together with “inradius”, “Chebyshev center”, and “largest inscribed Euclidean ball”. No statement was located that gives (2)--(6).

## Limitations
The theorem relies essentially on \(S\) being an interval of integers. For nonconsecutive \(S\), the convex hull is generally not just the cube intersected with one slab.

The formula concerns Euclidean balls in the standard coordinate realization. It is not invariant under arbitrary affine equivalence.

The metric optimization becomes elementary once the slab representation (1) is recognized, so an unindexed folklore observation remains a realistic originality risk. Search nonappearance is not treated as a formal novelty certificate.

## References
1. Sebastian Manecke, Raman Sanyal, and Jeonghoon So, *S-hypersimplices, pulling triangulations, and monotone paths*, arXiv:1812.07491, first public version 2018-12-18; Electronic Journal of Combinatorics 27(3) (2020), P3.16, DOI 10.37236/8457.
