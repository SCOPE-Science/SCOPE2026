# Exact Busemann–Petty section-width profile of three-dimensional parallelotopes

## Finding

For a centered convex body \(K\subset\mathbb R^3\) and a unit vector \(u\in S^2\), define the normalized central-section/width functional
\[
F_K(u)=
\frac{\lambda_2(K\cap u^\perp)\,\lambda_1(K\mid l_u)}{\lambda_3(K)}.
\]

If \(P\) is any three-dimensional parallelotope, then
\[
\boxed{
\min_{u\in S^2}F_P(u)=1,
\qquad
\max_{u\in S^2}F_P(u)=\frac94.
}
\]

More precisely, write
\[
P=A[-1,1]^3,
\qquad A\in\operatorname{GL}(3).
\]
The minimum occurs exactly at directions \(u\) for which \(A^Tu\) is parallel to one of the coordinate vectors. The maximum occurs exactly at directions for which the three absolute coordinates of \(A^Tu\) are equal.

The argument also gives a structural statement valid in every dimension: for every invertible linear map \(A\),
\[
F_{AK}(u)=F_K\!\left(\frac{A^Tu}{\lVert A^Tu\rVert}\right).
\]
Thus the directional profile is reparameterized, and its minimum and maximum are affine invariants.

## Assumptions and scope

A parallelotope here means an invertible linear image of the centered cube. Lebesgue measures are Euclidean measures in the indicated dimensions, \(K\mid l_u\) is the orthogonal projection of \(K\) onto the line spanned by \(u\), and \(K\cap u^\perp\) is the central hyperplane section.

The result solves this directional optimization for the complete affine class of three-dimensional parallelotopes. It does not solve Busemann–Petty Problem 6 over all centered convex bodies.

## Proof

First prove affine covariance. Let \(A\in\operatorname{GL}(d)\), \(u\in S^{d-1}\), and set
\[
v=\frac{A^Tu}{\lVert A^Tu\rVert}.
\]
Then
\[
A(v^\perp)=u^\perp.
\]
The \((d-1)\)-dimensional Jacobian of \(A\) restricted to \(v^\perp\) is
\[
\frac{|\det A|}{\lVert A^Tu\rVert}.
\]
Consequently
\[
\lambda_{d-1}(AK\cap u^\perp)
=
\frac{|\det A|}{\lVert A^Tu\rVert}
\lambda_{d-1}(K\cap v^\perp).
\]
On the other hand, support functions give
\[
\lambda_1(AK\mid l_u)
=
\lVert A^Tu\rVert\lambda_1(K\mid l_v),
\]
and
\[
\lambda_d(AK)=|\det A|\lambda_d(K).
\]
The factors cancel, proving
\[
F_{AK}(u)=F_K(v).
\]
Since the map \(u\mapsto A^Tu/\lVert A^Tu\rVert\) is a bijection of the sphere, the directional extrema are affine invariants. It therefore suffices to analyze
\[
C=[-1,1]^3.
\]

By the symmetries of the cube, take a unit normal with ordered absolute coordinates
\[
a\ge b\ge c\ge0.
\]
The width is
\[
\lambda_1(C\mid l_u)=2(a+b+c).
\]

Parameterize the central plane by
\[
(y,z)\longmapsto\left(-\frac{by+cz}{a},y,z\right).
\]
Its area scale factor is \(1/a\), because \(a^2+b^2+c^2=1\).

If \(a\ge b+c\), every \((y,z)\in[-1,1]^2\) is admissible. Hence
\[
\lambda_2(C\cap u^\perp)=\frac4a
\]
and
\[
F_C(u)=\frac{a+b+c}{a}.
\]
Therefore
\[
1\le F_C(u)\le2
\]
in this chamber. Equality \(F_C=1\) forces \(b=c=0\), while \(F_C=2\) occurs on the chamber boundary \(a=b+c\).

Now suppose \(a<b+c\). The admissible region in the \((y,z)\)-square is
\[
|by+cz|\le a.
\]
It is obtained from the square by deleting two congruent corner triangles. With
\[
\delta=b+c-a,
\]
each deleted triangle has legs \(\delta/b\) and \(\delta/c\). Thus
\[
\lambda_2(C\cap u^\perp)
=
\frac1a\left(4-\frac{\delta^2}{bc}\right)
=
\frac{2(ab+ac+bc)-(a^2+b^2+c^2)}{abc}.
\]
Writing
\[
s=a+b+c,
\qquad
P=ab+ac+bc,
\qquad
Q=a^2+b^2+c^2,
\]
we obtain
\[
F_C(u)=\frac{s(2P-Q)}{4abc}.
\]

The strict triangle inequalities permit the substitution
\[
a=y+z,
\qquad
b=z+x,
\qquad
c=x+y,
\qquad
x,y,z>0.
\]
A direct expansion gives
\[
s(2P-Q)-8abc=8xyz,
\]
so throughout the hexagonal-section chamber
\[
F_C(u)-2=\frac{2xyz}{abc}>0.
\]
Thus no minimum is hidden in this chamber.

For the upper bound,
\[
9abc-s(2P-Q)
=
(x+y+z)(xy+xz+yz)-9xyz.
\]
The arithmetic-geometric mean inequality gives
\[
x+y+z\ge3(xyz)^{1/3}
\]
and
\[
xy+xz+yz\ge3(xyz)^{2/3}.
\]
Hence
\[
(x+y+z)(xy+xz+yz)\ge9xyz,
\]
and therefore
\[
F_C(u)\le\frac94.
\]
Equality holds if and only if
\[
x=y=z,
\]
which is equivalent to
\[
a=b=c=\frac1{\sqrt3}.
\]

Combining both chambers gives
\[
\min F_C=1,
\qquad
\max F_C=\frac94,
\]
with the stated equality directions. Affine covariance transfers the complete result to every three-dimensional parallelotope.

## Verification

The accompanying `verify.py` performs two independent consistency checks.

First, exact rational arithmetic verifies the two polynomial identities governing the hexagonal-section chamber on a large integer grid, including both the strict lower separation from \(2\) and the factor controlling the \(9/4\) upper bound.

Second, the checker reconstructs central section polygons directly from intersections of a plane with the twelve edges of a cube. It computes their Euclidean polygonal areas without using the closed section formula and compares them with the analytic expression for hundreds of random directions. It then applies random invertible linear maps to the cube, reconstructs sections of the resulting parallelotopes geometrically, and checks the affine reparameterization identity against the cube profile.

The replay output is:

`VERIFY_OK parallelotope Busemann-Petty profile`

These finite tests are consistency checks only. The all-direction bounds and equality cases are proved analytically above.

## Relationship to prior work

Martini, Mustafaev, and Zarbaliev formulate Busemann–Petty Problem 6 through the normalized functional \(F_K\): minimize its directional maximum over centered convex bodies. They also emphasize the complementary maximin problem and record only dilation invariance of the normalized quantities in their introductory discussion. Their open-access full text develops general minimax inequalities using intersection and projection bodies, but does not discuss cubes, parallelepipeds, or parallelotopes.

Mustafaev's earlier article revisits Lutwak's minimax inequality for inscribed cones and relates maximal inscribed double cones to circumscribed cylinders of the polar body. Its publicly accessible abstract does not state an exact cube or parallelotope directional profile.

The central-section formula for a cube is elementary and is not claimed as new by itself. The finding is the exact optimization of the Busemann–Petty section-width product over all directions, together with the full affine reparameterization and hence the complete three-dimensional parallelotope class.

Focused searches for the exact value \(9/4\), for cube or parallelotope instances of Busemann–Petty Problem 6, for section-width products, and for equivalent inscribed-cone formulations did not locate a covering statement.

## Limitations

The exact \(9/4\) upper value is proved only in dimension three. Affine covariance is dimension-independent, but an exact higher-dimensional cube profile requires a separate optimization of central cube sections.

The result gives a benchmark inside the parallelotope affine class. It neither proves nor disproves the conjecture that ellipsoids minimize the global directional maximum in Busemann–Petty Problem 6.

The 2023 related article was accessible only through its detailed abstract and bibliographic page during the literature comparison; this is recorded as a residual access risk. Differently phrased or unindexed prior computations of the same cube product remain a residual originality risk.

## References

H. Martini, Z. Mustafaev, and S. M. Zarbaliev, “Some new minimax inequalities for centered convex bodies,” Aequationes Mathematicae 99 (2025), 1143–1152, published online 31 July 2024, DOI 10.1007/s00010-024-01109-6.

Z. Mustafaev, “A minimax inequality for inscribed cones revisited,” Canadian Mathematical Bulletin 67 (2024), 160–165, published online 31 August 2023, DOI 10.4153/S000843952300067X.

H. Busemann and C. M. Petty, “Problems on convex bodies,” Mathematica Scandinavica 4 (1956), 88–94.
