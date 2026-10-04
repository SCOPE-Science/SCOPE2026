# Rigidity of orthogonal seams for weighted geometric-mean antinorms

## Finding

Let \(d\ge2\), let
\[
p_i>0,\qquad \sum_{i=1}^d p_i=1,
\]
and consider the smooth self-dual antinorm
\[
f_p(x)=\prod_{i=1}^d\left(\frac{x_i}{\sqrt{p_i}}\right)^{p_i},
\qquad x\in\mathbb R_{>0}^d.
\]
Write
\[
S_p=\{x\in\mathbb R_{>0}^d:f_p(x)=1\}
\]
for its antisphere.

Let
\[
V=\{x\in\mathbb R^d:a\cdot x=0\}
\]
be a linear hyperplane whose relative interior meets the positive orthant. Suppose that for every
\[
x\in V\cap S_p
\]
the tangent hyperplane \(T_xS_p\) is orthogonal to \(V\).

Then there is a unique unordered pair \(\{i,j\}\) such that
\[
\boxed{
V=
\left\{
 x:\frac{x_i}{\sqrt{p_i}}=rac{x_j}{\sqrt{p_j}}
\right\}.
}
\]
Conversely, every one of these \(\binom d2\) hyperplanes has the stated orthogonality property.

Thus, for this canonical smooth family, the weighted coordinate-pair hyperplanes used in the lifting construction are exhaustive among all linear hyperplanes through the origin with everywhere orthogonal intersection. In the terminology of Makarov and Protasov, every such seam is admissible; no non-admissible linear hyperplane can have this global orthogonality property for the weighted geometric-mean antisphere.

## Assumptions and scope

All weights are strictly positive. This excludes the lower-dimensional degeneracies that occur when a weight vanishes.

The hyperplane \(V\) is required to meet \(\mathbb R_{>0}^d\). Equivalently, after choosing a nonzero normal \(a\), that normal has at least one positive and at least one negative coordinate.

The phrase “the tangent hyperplane is orthogonal to \(V\)” is used in the ordinary Euclidean sense: the normal to \(T_xS_p\) is orthogonal to the normal of \(V\).

The theorem classifies only linear seams through the origin for the explicit smooth weighted geometric-mean family. It does not classify arbitrary autopolar conic bodies, and it does not resolve the open polyhedral splitting problem for non-admissible hyperplanes.

## Proof

The gradient is
\[
\nabla f_p(x)
=
f_p(x)
\left(
\frac{p_1}{x_1},\ldots,\frac{p_d}{x_d}
\right).
\]
Since \(\nabla f_p(x)\) is normal to the tangent hyperplane, the tangent hyperplane at \(x\) is orthogonal to \(V\) exactly when
\[
a\cdot\nabla f_p(x)=0.
\]
Equivalently,
\[
\sum_{i=1}^d\frac{a_ip_i}{x_i}=0.
\tag{1}
\]

Because \(f_p\) is positively homogeneous, every positive point of \(V\) can be rescaled to a point of \(V\cap S_p\). The gradient is homogeneous of degree zero. Hence (1) holds for every
\[
x\in V\cap\mathbb R_{>0}^d.
\]

Let
\[
P=\{i:a_i>0\},
\qquad
N=\{j:a_j<0\}.
\]
Both sets are nonempty. For \(i\in P\) and \(j\in N\), define positive variables
\[
y_i=a_ix_i,
\qquad
z_j=-a_jx_j.
\]
The equation \(a\cdot x=0\) becomes
\[
\sum_{i\in P}y_i
=
\sum_{j\in N}z_j.
\tag{2}
\]
Meanwhile (1) becomes
\[
\sum_{i\in P}\frac{a_i^2p_i}{y_i}
=
\sum_{j\in N}\frac{a_j^2p_j}{z_j}.
\tag{3}
\]

Fix a common positive value for the two sums in (2), and fix all the \(z_j\). Then the right side of (3) is constant while the positive \(y_i\) vary over an open simplex.

If \(|P|\ge2\), choose two indices \(r,s\in P\), hold all remaining \(y_i\) fixed, and write
\[
y_r=t,
\qquad
y_s=C-t
\]
for \(0<t<C\). The varying part of the left side of (3) is
\[
\frac{a_r^2p_r}{t}
+
\frac{a_s^2p_s}{C-t}.
\]
Its derivative is
\[
-\frac{a_r^2p_r}{t^2}
+
\frac{a_s^2p_s}{(C-t)^2},
\]
which cannot vanish identically on \((0,C)\). Thus (3) cannot hold for all such \(y\), a contradiction. Therefore
\[
|P|=1.
\]
The same argument with the two sides interchanged gives
\[
|N|=1.
\]

Hence the normal \(a\) has exactly two nonzero coordinates. Say
\[
a_i>0,
\qquad
a_j<0.
\]
Equation (2) forces
\[
y_i=z_j,
\]
and then (3) yields
\[
a_i^2p_i=a_j^2p_j.
\]
Consequently
\[
\frac{-a_j}{a_i}
=
\sqrt{\frac{p_i}{p_j}}.
\]
The equation of \(V\) is therefore equivalent to
\[
\frac{x_i}{\sqrt{p_i}}
=
\frac{x_j}{\sqrt{p_j}}.
\]
This proves necessity.

For the converse, fix \(i\ne j\) and take the normal
\[
a_i=\sqrt{p_j},
\qquad
a_j=-\sqrt{p_i},
\qquad
a_k=0\ \text{for }k\notin\{i,j\}.
\]
On the hyperplane
\[
\frac{x_i}{\sqrt{p_i}}
=
\frac{x_j}{\sqrt{p_j}},
\]
one has
\[
\sqrt{p_j}\frac{p_i}{x_i}
=
\sqrt{p_i}\frac{p_j}{x_j}.
\]
Hence
\[
a\cdot\nabla f_p(x)=0.
\]
So the tangent hyperplane is orthogonal to \(V\) at every positive intersection point.

All weights are positive, so distinct unordered pairs give distinct hyperplanes. There are therefore exactly
\[
\binom d2
\]
such seams.

## Verification

The standalone checker independently evaluates the antinorm and its gradient for many positive weight vectors in dimensions \(2\) through \(9\). For every coordinate pair it constructs points on the claimed seam, rescales them to the antisphere, and checks both the hyperplane equation and the vanishing Euclidean inner product between the seam normal and the antisphere normal.

It also stress-tests mixed-sign normals with more than one coefficient on one side, using two different positive points with the same hyperplane balance to expose the nonconstant reciprocal-sum obstruction used in the analytic proof.

The replay output is:

`VERIFY_OK weighted geometric-mean seam rigidity`

These finite tests are consistency checks only. Exhaustiveness for every dimension and every positive weight vector follows from the reciprocal-simplex argument in the proof.

## Relationship to prior work

Protasov introduced this weighted geometric-mean family as an explicit family of self-dual antinorms. Makarov and Protasov later revisited the family in their lifting theory for autopolar conic bodies.

For positive weights, their Proposition 3 chooses the hyperplane
\[
\frac{x_{d-1}}{\sqrt{p_{d-1}}}
=
\frac{x_d}{\sqrt{p_d}},
\]
observes that the gradient remains in that hyperplane along the intersection, and uses this to realize the antinorm by their lifting construction. By coordinate permutation, the same construction applies to every coordinate pair.

That argument proves existence of the \(\binom d2\) pairwise seams. It does not classify arbitrary linear hyperplanes intersecting the positive orthant. The present theorem supplies the converse: global orthogonality forces the normal to have exactly one positive and one negative coordinate, with the precise weighted ratio above.

This distinction is aligned with the authors’ broader discussion. Their lifting theorem is formulated for admissible pairwise-coordinate hyperplanes, while they explicitly ask whether non-admissible hyperplanes can play an analogous role for more general autopolar objects. The result here does not answer that general problem; instead, it shows rigidity of the canonical smooth monomial family at exactly the point where the lifting construction uses an orthogonal seam.

Targeted searches for an exhaustive hyperplane classification for this antinorm, for a uniqueness theorem for its orthogonal seams, and for a non-admissible seam of the weighted geometric-mean antisphere did not locate an equivalent statement.

## Limitations

The weights must be positive. If some weight is zero, the antinorm reduces to a lower-dimensional one and additional ambient directions become irrelevant.

The result concerns linear hyperplanes through the origin and everywhere orthogonality along their positive intersection with the antisphere. It does not exclude non-admissible hyperplanes satisfying weaker local or polyhedral conditions.

It does not solve the higher-dimensional classification of self-dual antinorms or the authors’ open non-admissible splitting problem for autopolar conic polyhedra.

Because the proof is short once the explicit gradient is written down, an unindexed equivalent observation remains a residual originality risk.

## References

M. Makarov and V. Yu. Protasov, “Autopolar conic bodies and polyhedra,” arXiv:2407.04137, first submitted 2024-07-04; Sbornik: Mathematics 216 (2025), 412–430, DOI 10.4213/sm10202.

V. Yu. Protasov, “Antinorms on cones: duality and applications,” arXiv:2109.11882, first submitted 2021-09-24; Linear and Multilinear Algebra 70 (2022), 7387–7413, DOI 10.1080/03081087.2021.1988885.
