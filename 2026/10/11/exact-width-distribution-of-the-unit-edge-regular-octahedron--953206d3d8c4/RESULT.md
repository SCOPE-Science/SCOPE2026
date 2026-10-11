# Exact width distribution of the unit-edge regular octahedron
## Finding
Let
\[
O=\operatorname{conv}\{\pm e_1/\sqrt2,\pm e_2/\sqrt2,\pm e_3/\sqrt2\}
\subset\mathbb R^3.
\]
Adjacent vertices have distance \(1\), so \(O\) is the unit-edge regular octahedron. If \(U\) is uniformly distributed on \(S^2\) and
\[
W=w_O(U)
\]
is the directional width, then
\[
\operatorname{supp}(W)=\left[\sqrt{\frac23},\sqrt2\right]
\]
and its cumulative distribution function is
\[
F_W(w)=0
\qquad
\left(w<\sqrt{\frac23}\right),
\]
\[
F_W(w)=
\frac{3w}{\sqrt2}-2
+\frac6\pi\arccos\!\left(\frac{w^2}{2-w^2}\right)
-\frac{6\sqrt2\,w}{\pi}
\arccos\!\left(\frac{w}{\sqrt{2-w^2}}\right)
\tag{1}
\]
for
\[
\sqrt{\frac23}\le w\le1,
\]
\[
F_W(w)=\frac{3w}{\sqrt2}-2
\tag{2}
\]
for
\[
1\le w\le\sqrt2,
\]
and
\[
F_W(w)=1
\qquad
(w>\sqrt2).
\]

Thus the entire random-direction width law of the regular octahedron is elementary and has exactly one interior transition, at width \(1\).

## Assumptions and scope
For a convex body \(K\), the width in direction \(u\in S^2\) is
\[
w_K(u)=h_K(u)+h_K(-u),
\]
where
\[
h_K(u)=\max_{x\in K}x\cdot u.
\]
The probability law uses normalized spherical area measure on \(S^2\).

The formula is specific to the three-dimensional regular crosspolytope with edge length \(1\). Scaling the octahedron by a positive factor scales the width variable by the same factor.

No statement is made here about random chord length. A random chord and a random orthogonal projection length are distinct geometric distributions.

## Proof
For
\[
u=(u_1,u_2,u_3)\in S^2,
\]
the support function of \(O\) is
\[
h_O(u)
=
\frac1{\sqrt2}
\max\{|u_1|,|u_2|,|u_3|\}.
\]
Because \(O\) is centrally symmetric,
\[
w_O(u)=2h_O(u)
=
\sqrt2\,M(u),
\qquad
M(u):=\max_i|u_i|.
\tag{3}
\]

The sphere identity
\[
u_1^2+u_2^2+u_3^2=1
\]
shows
\[
\frac1{\sqrt3}\le M(u)\le1.
\]
Equation (3) therefore gives the stated support of \(W\).

Fix
\[
m\in\left[\frac1{\sqrt3},1\right].
\]
For each coordinate axis and each sign, let
\[
C_i^\pm(m)=\{u\in S^2:\pm u_i>m\}.
\]
These are six congruent spherical caps, each of area
\[
A_1(m)=2\pi(1-m).
\tag{4}
\]
The event
\[
M\le m
\]
is exactly the complement of their union.

First suppose
\[
\frac1{\sqrt2}\le m\le1.
\]
Two caps belonging to distinct coordinate axes have disjoint interiors, because
\[
u_i^2+u_j^2>2m^2\ge1
\]
would be impossible. Opposite caps on the same axis are also disjoint. Hence
\[
\mathbb P(M\le m)
=
1-\frac{6A_1(m)}{4\pi}
=
3m-2.
\tag{5}
\]
With \(m=w/\sqrt2\), equation (5) becomes (2).

Now suppose
\[
\frac1{\sqrt3}\le m\le\frac1{\sqrt2}.
\]
Triple cap intersections have zero spherical area, since a positive-area triple intersection would require
\[
u_1^2+u_2^2+u_3^2>3m^2\ge1.
\]
There are exactly twelve unordered pairs of distinct-axis signed caps, and all pair intersections are congruent. Let
\[
A_2(m)
=
\operatorname{area}\{u\in S^2:u_1>m,\ u_2>m\}.
\]
Inclusion-exclusion gives
\[
\mathbb P(M\le m)
=
1-\frac{6A_1(m)-12A_2(m)}{4\pi}
=
3m-2+\frac{3A_2(m)}{\pi}.
\tag{6}
\]

It remains to evaluate one spherical lens. Let \(X=e_1\) and \(Y=e_2\) be the centers of the two caps. Their angular radius is
\[
r=\arccos m,
\]
and
\[
d(X,Y)=\frac\pi2.
\]
Let \(P\) be one of the two intersection points of the cap boundaries. In the spherical triangle \(XYP\), the side lengths are
\[
XP=YP=r,
\qquad
XY=\frac\pi2.
\]
Write the angles at \(X,Y,P\) as
\[
\alpha,\alpha,\gamma.
\]
The spherical cosine rule gives
\[
\cos\alpha
=
\frac{m}{\sqrt{1-m^2}},
\tag{7}
\]
and
\[
\cos\gamma
=
-\frac{m^2}{1-m^2}.
\tag{8}
\]
Put
\[
\beta=\pi-\gamma.
\]
Then
\[
\beta
=
\arccos\!\left(\frac{m^2}{1-m^2}\right).
\tag{9}
\]

Each cap sector spanning the two boundary-intersection points has azimuth \(2\alpha\), so its area is
\[
2\alpha(1-m).
\]
The two congruent spherical triangles \(XYP\) and \(XYQ\) each have spherical excess
\[
2\alpha+\gamma-\pi.
\]
Therefore the lens area is
\[
A_2(m)
=
4\alpha(1-m)
-
2(2\alpha+\gamma-\pi)
=
2\beta-4m\alpha.
\tag{10}
\]
Using (7) and (9),
\[
A_2(m)
=
2\arccos\!\left(\frac{m^2}{1-m^2}\right)
-
4m\arccos\!\left(\frac{m}{\sqrt{1-m^2}}\right).
\tag{11}
\]

Substituting (11) into (6), then setting
\[
m=\frac{w}{\sqrt2},
\]
gives exactly (1).

At the lower endpoint,
\[
m=\frac1{\sqrt3},
\qquad
\alpha=\frac\pi4,
\qquad
\beta=\frac\pi3,
\]
and (6) gives \(0\). At
\[
m=\frac1{\sqrt2},
\]
both \(\alpha\) and \(\beta\) vanish, so the two interior formulas agree. At \(m=1\), equation (5) gives \(1\). Hence the displayed piecewise formula is a continuous cumulative distribution function on the complete support.

## Verification
The standalone `verify.py` checks four independent layers.

First, it confirms the unit-edge normalization of the six octahedral vertices and verifies directly that
\[
w_O(u)=\sqrt2\max_i|u_i|
\]
for deterministic test directions.

Second, symbolic endpoint substitutions verify
\[
F_W\!\left(\sqrt{\frac23}\right)=0,
\qquad
F_W(1^-)=F_W(1^+)=\frac3{\sqrt2}-2,
\qquad
F_W(\sqrt2)=1.
\]

Third, deterministic numerical quadrature computes the spherical area of
\[
\{|u_1|\le m,\ |u_2|\le m,\ |u_3|\le m\}
\]
directly in latitude-longitude coordinates at several values of \(m\) spanning both branches and checks agreement with the closed form.

Fourth, the script evaluates the lens area independently by one-dimensional quadrature of the two-cap intersection and compares it with (11).

The quadratures are consistency checks only. Exactness follows from inclusion-exclusion, the spherical cosine rule, and spherical sector-minus-triangle area calculation above.

## Relationship to prior work
Kabluchko, Litvak, and Zaporozhets give a higher-moment Sudakov formula for every regular crosspolytope. In their notation
\[
C_n=\operatorname{conv}(\pm e_1,\ldots,\pm e_n),
\]
and all integer moments of its random projection length are represented through
\[
\max_{1\le i\le n}|\eta_i|
\]
for independent standard Gaussian variables. They also prove a high-dimensional Gumbel limit. Their full text does not give a finite-dimensional closed cumulative distribution for \(n=3\).

Finch's earlier paper develops width distributions and mean-square widths for regular polyhedra, treating the regular tetrahedron and cube and explicitly encouraging analogous computations for other convex bodies. Its full text contains no octahedral calculation.

A later general theory of random width for three-dimensional polytopes gives a spherical co-area density formula valid for every polytope. Its explicitly evaluated examples are the regular tetrahedron, the regular truncated octahedron, and the corresponding rhombic-dodecahedral law. Full-text search finds no crosspolytope occurrence. Thus that framework applies in principle to the regular octahedron, but it does not state the elementary closed CDF (1)--(2).

The regular octahedron also has a published exact random-chord-length density, but random chord length is a different invariant and does not imply the random-direction width distribution.

## Limitations
The result is a three-dimensional exact evaluation, not a closed distribution formula for crosspolytopes in arbitrary dimension.

The higher-moment representation of Kabluchko, Litvak, and Zaporozhets characterizes the compactly supported width law implicitly, so the novelty here is the explicit finite-dimensional CDF and its spherical-lens derivation, not the abstract existence or moment determination of the law.

A differently phrased classical stereological source could contain the same formula under terms such as caliper diameter or Feret diameter. Targeted searches under those aliases and under the equivalent maximum-coordinate formulation did not locate one.

## References
1. Z. Kabluchko, A. E. Litvak, and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479v1, 26 November 2015.
2. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671v1, 4 October 2011.
3. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202v1, 10 August 2026.
4. S. Ciccariello, *The chord-length probability density of the regular octahedron*, arXiv:1401.7950v1, 30 January 2014.
