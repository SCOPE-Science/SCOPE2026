# Exact Ulam floating body of the square

## Finding

Let
\[
Q=[-1,1]^2,
\]
and let \(M_\delta(Q)\) denote the Ulam floating body at absolute area level \(0<\delta<4\). Equivalently, in every unit normal direction \(u\), the unique support point of \(M_\delta(Q)\) with normal \(u\) is the barycenter of the cap of \(Q\) cut off by a line orthogonal to \(u\) and having area \(\delta\).

For \(0<\delta\le2\), one eighth of the boundary, in the sector \(0\le y\le x\), is exactly the union of a parabolic arc
\[
x=1-\frac{\delta}{4}-\frac{3\delta}{4}y^2,
\qquad
0\le y\le\frac13,
\]
and a rectangular-hyperbolic arc
\[
(1-x)(1-y)=\frac{2\delta}{9},
\qquad
\frac13\le y\le 1-\frac{\sqrt{2\delta}}3.
\]
The full boundary is obtained by the eight dihedral symmetries of the square. At \(\delta=2\), the hyperbolic arc degenerates to the diagonal endpoint \((1/3,1/3)\).

The area is
\[
|M_\delta(Q)|
=
4-\frac{44}{27}\delta
+\frac{8}{9}\delta\log\!\left(\frac{\delta}{2}\right),
\qquad 0<\delta\le2.
\]
For \(2\le\delta<4\), central symmetry gives
\[
M_\delta(Q)
=
\frac{4-\delta}{\delta}\,M_{4-\delta}(Q),
\]
so the preceding formulas determine the Ulam floating body for every admissible level. In particular,
\[
4-|M_\delta(Q)|
=
\frac89\delta\log\!\left(\frac2\delta\right)
+\frac{44}{27}\delta,
\qquad 0<\delta\le2.
\]

## Assumptions and scope

The parameter \(\delta\) is absolute cap area, not a fraction of \(|Q|=4\). The construction is the uniform-density Ulam floating body introduced for convex bodies. The result is specific to the square, although affine equivariance immediately converts it into the corresponding formula for every parallelogram after applying the same affine map and the appropriate determinant scaling of the cap-area parameter.

## Proof

The general Ulam-body support characterization says that for a direction \(u\), the support point is the barycenter of the unique \(\delta\)-area cap cut off orthogonally to \(u\). By the dihedral symmetry of \(Q\), it is enough to take a normal proportional to
\[
(1,m),\qquad 0\le m\le1.
\]

Assume first that \(0<\delta\le2\).

When \(m\le\delta/2\), the cap is a trapezoid meeting both horizontal sides of the square. Its cutting line can be written
\[
x=1-\frac\delta2-my.
\]
The vertical fiber at height \(y\) therefore has width
\[
w(y)=\frac\delta2+my.
\]
Direct integration over \(-1\le y\le1\) gives cap area \(\delta\) and barycenter
\[
\bar x
=1-\frac\delta4-\frac{m^2}{3\delta},
\qquad
\bar y
=\frac{2m}{3\delta}.
\]
Eliminating \(m\) yields
\[
\bar x
=1-\frac\delta4-\frac{3\delta}{4}\bar y^2.
\]
At the transition \(m=\delta/2\), one gets
\[
(\bar x,\bar y)=\left(1-\frac\delta3,\frac13\right).
\]

When \(m\ge\delta/2\), the cap is a right triangle at the vertex \((1,1)\). If
\[
d=\sqrt{2\delta m},
\]
its legs on the top and right sides have lengths \(d\) and \(d/m\), respectively, and their product divided by two is \(\delta\). The centroid is
\[
\bar x=1-\frac{d}{3},
\qquad
\bar y=1-\frac{d}{3m}.
\]
Consequently,
\[
(1-\bar x)(1-\bar y)=\frac{d^2}{9m}=\frac{2\delta}{9}.
\]
At \(m=1\), the normal is diagonal and the endpoint is
\[
\left(1-\frac{\sqrt{2\delta}}3,1-\frac{\sqrt{2\delta}}3\right).
\]
Thus the two conic arcs give exactly one octant of the boundary.

For the area, use Green's formula on the first-octant sector. Radial segments from the origin contribute zero to \(x\,dy-y\,dx\), so the full area is four times the integral of \(x\,dy-y\,dx\) along the boundary arc from the positive \(x\)-axis to the diagonal.

On the parabola this integral is
\[
I_1=\frac13-\frac{2\delta}{27}.
\]
On the hyperbola, writing \(k=2\delta/9\) and \(x=1-k/(1-y)\), direct integration gives
\[
I_2
=\frac23-\frac\delta3+\frac{2\delta}{9}\log\!\left(\frac\delta2\right).
\]
Hence
\[
|M_\delta(Q)|=4(I_1+I_2)
=4-\frac{44}{27}\delta+\frac89\delta\log\!\left(\frac\delta2\right).
\]

Finally, let \(2\le\delta<4\), set \(\eta=4-\delta\), and fix a direction \(u\). The \(\delta\)-cap in direction \(u\) and its complement, which is the \(\eta\)-cap in direction \(-u\), partition a body of centroid zero. Therefore their barycenters \(b_\delta(u)\) and \(b_\eta(-u)\) satisfy
\[
\delta b_\delta(u)+\eta b_\eta(-u)=0.
\]
Central symmetry gives \(b_\eta(-u)=-b_\eta(u)\), and so
\[
b_\delta(u)=\frac\eta\delta b_\eta(u).
\]
Equality of support points in every direction proves the complement law.

## Verification

The accompanying `verify.py` independently integrates cap fibers for multiple levels and normal directions, compares those numerical barycenters with the two closed forms, checks the conic equations, reconstructs the full boundary by square symmetries, and compares its polygonal area with the exact area formula. It also checks the complement scaling for levels above half the square's area.

The replay output is:

`VERIFY_OK square Ulam body boundary and area`

The finite numerical checks are consistency tests only. The all-level statement follows from the exact cap integrations, Green's formula, and the centroid complement identity.

## Relationship to prior work

Huang, Slomka, and Werner introduced the Ulam floating body and proved that the barycenter of each prescribed-volume cap is the unique boundary point with the corresponding normal. Their paper also proves general smoothness and affine-surface-area properties. Its full text contains no occurrence of “square,” “rectangle,” or “polygon,” and it does not state the conic boundary or area profile above.

Huang and Slomka's earlier metronoid paper introduced the underlying measure-generated convex sets and noted the special importance of bodies generated by uniform measures on convex bodies. Its full text likewise contains no square or rectangle example of this transform.

Molchanov and Turin later recast Ulam floating bodies as average-quantile convex sets within a broad sublinear-expectation framework. Their accessible full text contains no square, rectangle, cube, or polygon specialization.

Targeted searches for exact square Ulam bodies, metronoids of the uniform square, average-quantile sets of the square, and the distinctive parabola–hyperbola boundary did not locate an equivalent formula.

## Limitations

The explicit conic decomposition uses the two-dimensional square and uniform density. Affine equivariance gives parallelograms, but not arbitrary quadrilaterals. No claim is made here for cubes in dimensions above two, nonuniform weights, convex floating bodies, or Dupin floating bodies. The literature search was targeted rather than exhaustive, so an older equivalent computation under zonoid-trimming or robust-statistics terminology remains a residual risk.

## References

H. Huang, B. A. Slomka, and E. M. Werner, “Ulam Floating Body,” arXiv:1803.08224, first submitted 2018-03-22; Journal of the London Mathematical Society 100 (2019), 425–446.

H. Huang and B. A. Slomka, “Approximations of convex bodies by measure-generated sets,” arXiv:1706.07112, first submitted 2017-06-21; Geometriae Dedicata 192 (2018), 173–196.

I. Molchanov and R. Turin, “Convex bodies generated by sublinear expectations of random vectors,” arXiv:2006.02186, first submitted 2020-06-03; Advances in Applied Mathematics 131 (2021), 102251.
