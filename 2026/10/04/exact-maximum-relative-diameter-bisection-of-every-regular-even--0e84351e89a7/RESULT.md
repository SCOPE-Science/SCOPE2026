# Exact maximum-relative-diameter bisection of every regular even polygon

## Finding

Let \(P_n\) be a regular even \(n\)-gon, \(n\ge4\), of circumradius \(R\). A bisection is a decomposition of \(P_n\) into two connected subsets by a simple curve whose endpoints lie on \(\partial P_n\); the two parts need not have equal area. If
\[
d_M(\mathcal B)=\max\{D(C_1),D(C_2)\}
\]
is the maximum relative diameter of the bisection, then
\[
\min_{\mathcal B}d_M(\mathcal B)
=
R\sqrt{4-3\sin^2\!\left(\frac{\pi}{n}\right)}.
\]

A minimizing bisection is obtained by joining the midpoints of any pair of opposite sides. Among straight-line bisections through the center, these side-midpoint cuts are exactly the minimizers, up to the dihedral symmetries of \(P_n\).

For \(n=4\), this gives \(R\sqrt{5/2}\), equivalently \(\sqrt5/2\) times the side length of the square. For \(n=6\), it gives \(\sqrt{13}\,R/2\), agreeing with the previously computed standard two-partition of the regular hexagon.

## Assumptions and scope

The polygon is Euclidean, regular, and has an even number of sides. Bisections are allowed to be arbitrary simple curves with boundary endpoints, exactly as in the centrally symmetric convex-body bisection problem; equal-area parts are not assumed.

The argument uses the published reduction that every bisection of a centrally symmetric planar convex body can be replaced by a straight-line bisection through the center with no larger maximum relative diameter. The new work is the exact optimization of that reduced problem for the entire regular-even family.

## Proof

Put
\[
\alpha=\frac{\pi}{n},\qquad
a=R\cos\alpha,\qquad
b=R\sin\alpha.
\]
Choose coordinates so one side of \(P_n\) has endpoints
\[
A=(a,-b),\qquad B=(a,b).
\]

For centrally symmetric planar convex bodies, every bisection has a center-passing straight-line bisection with no larger maximum relative diameter. Therefore it is enough to minimize over center-passing lines.

Let \(x\) be one endpoint of such a line. By symmetry we may take
\[
x=(a,t),\qquad -b\le t\le b,
\]
on the side \(AB\); the other endpoint is \(-x\). For a center-passing bisection, the maximum relative diameter is the largest distance from \(x\) to the boundary. For a polygon, that farthest point can be taken at a vertex.

All vertices of \(P_n\) lie on the circle of radius \(R\). Maximizing the squared distance from \(x\) to a vertex is therefore equivalent to minimizing the scalar product with \(x\). Since the direction of \(-x\) lies between the directions of the two vertices opposite \(A\) and \(B\), a farthest vertex is one of
\[
-A=(-a,b),\qquad -B=(-a,-b).
\]
Consequently
\[
d_M^2
=
\max\!\left\{
4a^2+(t-b)^2,\,
4a^2+(t+b)^2
\right\}
=
4a^2+(b+|t|)^2.
\]
This expression is uniquely minimized on the side when \(t=0\). Hence the best center-passing cut meets the two opposite sides at their midpoints and has
\[
d_M^2=4a^2+b^2
=R^2\left(4-3\sin^2\alpha\right).
\]
Taking square roots gives
\[
d_M
=
R\sqrt{4-3\sin^2\!\left(\frac{\pi}{n}\right)}.
\]

Because every arbitrary bisection admits a center-passing straight-line replacement with no larger \(d_M\), this center-passing minimum is also the global bisection minimum. The strict dependence on \(|t|\) proves that, among center-passing straight lines, equality occurs exactly at side midpoints. Rotating or reflecting the polygon gives all equivalent midpoint cuts.

## Verification

The proof has three independently checked steps.

First, the reduction from arbitrary bisections to center-passing straight-line bisections is a published theorem for centrally symmetric planar convex bodies.

Second, for \(x=(a,t)\), the farthest-vertex calculation was checked directly from
\[
\|x-v\|^2=\|x\|^2+R^2-2x\cdot v.
\]
The minimizing vertex scalar product is attained by one of the two vertices bracketing the direction \(-x\), namely \(-A\) and \(-B\), giving the exact profile
\[
4a^2+(b+|t|)^2.
\]

Third, the special case \(n=6\) reduces to
\[
R\sqrt{4-\frac34}=\frac{\sqrt{13}}2R,
\]
which coincides with the published regular-hexagon value for the standard two-partition. The square case likewise gives the elementary half-square diameter.

No numerical experiment, asymptotic argument, or unproved classification is used.

## Relationship to prior work

Cañete and Segura Gomis prove that, for every centrally symmetric planar convex body, arbitrary bisections may be reduced to center-passing straight-line bisections without increasing the maximum relative diameter. They also give necessary and sufficient conditions for minimizing bisections and analyze standard bisections. Their examples include the square, rectangle, ellipse, circle, and several nonregular centrally symmetric bodies. Their paper does not state a formula for all regular even polygons.

An earlier paper of Cañete studies maximum relative diameter for multi-rotationally symmetric bodies. It records, for the regular hexagon, the value
\[
d_M(P_2)=\frac{\sqrt{13}}2R
\]
for the standard two-partition. The formula proved here recovers that special case and gives the uniform value for every regular even \(n\)-gon, while also proving optimality among all bisections through the later center-line reduction.

Targeted searches for regular even polygons, regular \(2m\)-gons, standard bisections, and the maximum-relative-diameter formula did not locate a prior all-\(n\) statement.

## Limitations

The theorem concerns even regular polygons only. It does not treat odd regular polygons, nonregular centrally symmetric polygons, more than two pieces, or other partition objectives. It classifies the minimizing center-passing straight lines, but it does not claim that every arbitrary curved minimizing bisection must itself be the midpoint segment; the general literature allows nonuniqueness of minimizing bisections.

The originality assessment is based on direct inspection of the most relevant papers and targeted database searches. Because the derivation is elementary after the center-line reduction, an equivalent special-family observation could exist under different terminology.

## References

A. Cañete and S. Segura Gomis, “Bisections of centrally symmetric planar convex bodies minimizing the maximum relative diameter,” arXiv:1803.00321, first submitted 2018-03-01.

A. Cañete, “The maximum relative diameter for multi-rotationally symmetric planar convex bodies,” arXiv:1511.08009; Mathematical Inequalities & Applications 19 (2016), 335–347, DOI 10.7153/mia-19-25.
