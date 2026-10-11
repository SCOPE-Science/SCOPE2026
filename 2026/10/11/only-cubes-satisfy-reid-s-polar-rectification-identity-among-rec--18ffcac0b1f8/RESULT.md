# Only cubes satisfy Reid’s polar-rectification identity among rectangular boxes
## Finding
Let
\[
P_{a,b,c}=[-a,a]\times[-b,b]\times[-c,c]\subset\mathbb R^3,
\qquad a,b,c>0.
\]
Let \(R_1[P_{a,b,c}]\) denote the first rectification, namely the convex hull of the edge midpoints. Polarity is Euclidean polarity about the origin.

Then
\[
\boxed{
R_1[P_{a,b,c}]=P_{a,b,c}\cap\lambda P_{a,b,c}^{\circ}
\text{ for some }\lambda>0
\quad\Longleftrightarrow\quad
a=b=c
}.
\tag{1}
\]
When
\[
a=b=c=s,
\]
the scalar is uniquely
\[
\lambda=2s^2.
\tag{2}
\]

Thus every noncubic centered rectangular box is a counterexample to the conjecture that every convex polyhedron admits such a scaled-polar intersection description of its rectification. A concrete example is
\[
[-1,1]\times[-2,2]\times[-3,3].
\]

## Assumptions and scope
For a convex polyhedron \(P\subset\mathbb R^3\), the first rectification is
\[
R_1[P]
=
\operatorname{conv}
\left\{
\frac{x_i+x_j}{2}:
(x_i,x_j)\text{ is an edge of }P
\right\}.
\]

For a convex body containing the origin in its interior, the polar is
\[
P^{\circ}
=
\{y:x\cdot y\le1\text{ for every }x\in P\}.
\]
For the rectangular box above,
\[
P_{a,b,c}^{\circ}
=
\{y:a|y_1|+b|y_2|+c|y_3|\le1\}.
\tag{3}
\]

The theorem classifies exactly the centered rectangular boxes. It does not classify all parallelotopes or all centrally symmetric polyhedra.

## Proof
Let
\[
C=[-1,1]^3
\]
and let
\[
D=\operatorname{diag}(a,b,c),
\]
so that
\[
P_{a,b,c}=DC.
\]
Rectification commutes with invertible linear maps because linear maps preserve edge midpoints and convex hulls. Hence
\[
R_1[P_{a,b,c}]=D R_1[C].
\tag{4}
\]

For the cube, the twelve edge midpoints are precisely the sign-permutations of
\[
(1,1,0).
\]
A direct vertex check gives
\[
R_1[C]
=
\{x:|x_i|\le1\text{ for }i=1,2,3,
\ |x_1|+|x_2|+|x_3|\le2\}.
\tag{5}
\]
Applying \(D\) to (5) yields
\[
R_1[P_{a,b,c}]
=
\left\{
 x:
 |x_1|\le a,
 |x_2|\le b,
 |x_3|\le c,
 \frac{|x_1|}{a}+\frac{|x_2|}{b}+\frac{|x_3|}{c}\le2
\right\}.
\tag{6}
\]

Now suppose that for some \(\lambda>0\),
\[
R_1[P_{a,b,c}]
=
P_{a,b,c}\cap\lambda P_{a,b,c}^{\circ}.
\tag{7}
\]
Consider
\[
q_1=
\left(
\frac{4a}{5},
\frac{3b}{5},
\frac{3c}{5}
\right),
\]
\[
q_2=
\left(
\frac{3a}{5},
\frac{4b}{5},
\frac{3c}{5}
\right),
\]
and
\[
q_3=
\left(
\frac{3a}{5},
\frac{3b}{5},
\frac{4c}{5}
\right).
\]
Every coordinate of each \(q_i\) is strictly inside its box bound, while
\[
\frac{|q_{i,1}|}{a}
+
\frac{|q_{i,2}|}{b}
+
\frac{|q_{i,3}|}{c}
=2.
\]
Thus
\[
q_i\in\operatorname{int}P_{a,b,c}
\cap
\partial R_1[P_{a,b,c}].
\tag{8}
\]

By (7), a point in (8) must lie on the boundary of \(\lambda P_{a,b,c}^{\circ}\); otherwise it would be interior to both factors in the intersection. Using (3), we obtain
\[
\lambda
=a(q_1)_1+b(q_1)_2+c(q_1)_3
=
\frac{4a^2+3b^2+3c^2}{5},
\tag{9}
\]
\[
\lambda
=
\frac{3a^2+4b^2+3c^2}{5},
\tag{10}
\]
and
\[
\lambda
=
\frac{3a^2+3b^2+4c^2}{5}.
\tag{11}
\]
Subtracting (10) from (9) gives
\[
a^2=b^2,
\]
and subtracting (11) from (10) gives
\[
b^2=c^2.
\]
Since \(a,b,c>0\),
\[
a=b=c.
\tag{12}
\]

Conversely, let
\[
a=b=c=s.
\]
Then (6) becomes
\[
R_1[P_{s,s,s}]
=
P_{s,s,s}
\cap
\{x:|x_1|+|x_2|+|x_3|\le2s\}.
\tag{13}
\]
By (3),
\[
\lambda P_{s,s,s}^{\circ}
=
\{x:s(|x_1|+|x_2|+|x_3|)\le\lambda\}.
\]
Taking
\[
\lambda=2s^2
\]
makes this set exactly the second factor in (13), proving the converse. The scalar is unique because the triangular facets in (13) are genuine boundary facets.

This proves (1)--(2).

## Verification
The supplied `verify.py` enumerates all twelve cube edge midpoints and checks the cuboctahedral inequalities in (5). It verifies symbolically that the three scaled-polar boundary values in (9)--(11) differ by
\[
\frac{a^2-b^2}{5}
\quad\text{and}\quad
\frac{b^2-c^2}{5},
\]
and checks the concrete box
\[
[-1,1]\times[-2,2]\times[-3,3]
\]
where the three forced values are
\[
\frac{43}{5},\qquad
\frac{46}{5},\qquad
\frac{51}{5}.
\]

These finite checks are regression checks only. The theorem follows from the exact facet-boundary argument (8)--(12).

## Relationship to prior work
Reid defines the first rectification of a convex polyhedron as the convex hull of its edge midpoints. In the same paper, Conjecture 3 asserts that every convex polyhedron \(P\subset\mathbb R^3\) satisfies
\[
R_1[P]=P\cap\lambda P^{\circ}
\]
for some positive scalar \(\lambda\).

The regular cube is consistent with that conjecture: its rectification is the cuboctahedron
\[
[-1,1]^3\cap\{x:\lVert x\rVert_1\le2\}.
\]
The theorem above shows that this regular identity is rigid even inside the simplest three-parameter deformation family: among centered rectangular boxes, only cubes retain it.

Targeted searches under rectification, scaled polarity, rectangular boxes, cuboids, orthotopes, edge-midpoint hulls, and dual intersections did not locate a published rectangular-box classification or an explicit noncubic-box counterexample. General descriptions of dual-polyhedron intersections note that midpoint coincidence is special to regular settings, but they do not supply the statement-and-proof classification (1).

## Limitations
The result treats centered rectangular boxes. It does not determine which nonorthogonal parallelotopes, prisms, or arbitrary convex polyhedra may satisfy a scaled-polar intersection identity.

The obstruction depends on Euclidean polarity with respect to the box center. A translated formulation requires specifying the polarity center and is not addressed here.

Because the counterexample is elementary once the conjecture is written in coordinates, an equivalent observation may exist in unindexed notes or informal discussions. Targeted literature searches did not locate one; this remains the main historical originality risk.

## References
1. S. Reid, *Rectifications of Convex Polyhedra*, arXiv:1604.00580v1, 3 April 2016.
