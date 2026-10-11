# One-section criterion for Herburt's dual-volume problem on Euclidean balls
## Finding
Let
\[
B_R^d=\{x\in\mathbb R^d:\lVert x\rVert\le R\},
\qquad d\ge3.
\]
For
\[
a,b\in\operatorname{int}B_R^d
\]
and any affine hyperplane \(H\) containing both \(a\) and \(b\), define
\[
M_H(x)
=
\int_{S^{d-1}\cap(H-x)}
\rho_{(B_R^d\cap H)-x}(u)\,d\sigma_H(u).
\]
Also define
\[
M(x)
=
\int_{S^{d-1}}
\rho_{B_R^d-x}(u)\,d\sigma(u).
\]

Then, for every common hyperplane \(H\),
\[
M_H(a)\le M_H(b)
\quad\Longleftrightarrow\quad
\lVert a\rVert\ge\lVert b\rVert
\quad\Longleftrightarrow\quad
M(a)\le M(b).
\]

Thus the affine-section implication posed in Problem 7 of the 2009 Banach Center open-problem session holds for every Euclidean ball. More strongly, on a ball it is enough to compare the two section integrals on one affine hyperplane through the two points; requiring the comparison for every common hyperplane is redundant.

## Assumptions and scope
The radial function of a convex body \(K\) containing the origin in its interior is
\[
\rho_K(u)
=
\max\{t\ge0:tu\in K\}.
\]
For a translated section \((B_R^d\cap H)-x\), the integration sphere is the unit sphere in the linear space \(H-x\).

The measure \(d\sigma_H\) is ordinary spherical surface measure in the \((d-1)\)-dimensional direction space of \(H\), and \(d\sigma\) is ordinary surface measure on \(S^{d-1}\). Their normalizations do not matter for comparisons.

The condition \(d\ge3\) is essential for the one-section equivalence proved here. A hyperplane section then has dimension at least \(2\). In dimension \(2\), a common hyperplane is a line and the sum of the two radial distances to the endpoints of a chord is its length, independent of the chosen interior point on that chord.

The theorem is specific to Euclidean balls. No affine invariance is claimed, because the radial integral in the problem is Euclidean and is not preserved by arbitrary affine maps.

## Proof
First consider an \(m\)-dimensional Euclidean ball
\[
D=c+rB_2^m,
\qquad m\ge2,
\]
and a point \(x\in\operatorname{int}D\). Put
\[
s=\lVert x-c\rVert.
\]
Choose a unit vector \(e\) with
\[
x-c=se.
\]
For \(u\in S^{m-1}\), the positive radial distance from \(x\) to the boundary of \(D\) is obtained from
\[
\lVert x+\rho u-c\rVert^2=r^2.
\]
The positive root is
\[
\rho_{D-x}(u)
=
-s(e\cdot u)
+
\sqrt{r^2-s^2+s^2(e\cdot u)^2}.
\tag{1}
\]

The linear term in (1) integrates to zero over the sphere. Hence
\[
J_m(r,s)
:=
\int_{S^{m-1}}\rho_{D-x}(u)\,d\sigma(u)
=
\int_{S^{m-1}}
\sqrt{r^2-s^2\bigl(1-(e\cdot u)^2\bigr)}
\,d\sigma(u).
\tag{2}
\]
Rotational invariance shows that \(J_m(r,s)\) depends only on \(r\) and \(s\).

For
\[
0\le s_1<s_2<r,
\]
the integrand in (2) at \(s_2\) is no larger than the integrand at \(s_1\), and it is strictly smaller whenever
\[
|e\cdot u|<1.
\]
Because \(m\ge2\), this strict inequality holds on a set of positive spherical measure. Therefore
\[
J_m(r,s_2)<J_m(r,s_1).
\tag{3}
\]
So the mean radial distance in a Euclidean ball is strictly decreasing with the distance from the center.

Applying (3) directly to the ambient ball gives
\[
M(a)\le M(b)
\quad\Longleftrightarrow\quad
\lVert a\rVert\ge\lVert b\rVert.
\tag{4}
\]

Now fix an affine hyperplane \(H\) through \(a\) and \(b\). Let \(L\) be its direction space and let \(c_H\) be the orthogonal projection of the origin onto \(H\). Then
\[
c_H\perp L.
\]
Write
\[
\delta=\lVert c_H\rVert.
\]
The section of the ambient ball is the \((d-1)\)-dimensional ball
\[
B_R^d\cap H
=
c_H+\sqrt{R^2-\delta^2}\,B_L,
\tag{5}
\]
where \(B_L\) is the unit ball in \(L\).

For every \(x\in H\), write
\[
x=c_H+v,
\qquad v\in L.
\]
Orthogonality gives
\[
\lVert x-c_H\rVert^2
=
\lVert x\rVert^2-\delta^2.
\tag{6}
\]
The radius in (5) is the same for \(a\) and \(b\), so strict monotonicity (3), now with
\[
m=d-1\ge2,
\]
and identity (6) imply
\[
M_H(a)\le M_H(b)
\quad\Longleftrightarrow\quad
\lVert a-c_H\rVert\ge\lVert b-c_H\rVert
\quad\Longleftrightarrow\quad
\lVert a\rVert\ge\lVert b\rVert.
\tag{7}
\]

Combining (4) and (7) proves the three-way equivalence. Since (7) holds for every common hyperplane, comparison on any one such hyperplane already implies the global comparison.

## Verification
The supplied `verify.py` reconstructs the radial quadratic equation symbolically, checks the positive-root formula, verifies the projection identity
\[
\lVert x-c_H\rVert^2=\lVert x\rVert^2-\lVert c_H\rVert^2
\]
under the orthogonality relation, and numerically integrates the radial formula in dimensions \(2\) through \(6\) for several radii and eccentricities as regression checks.

The universal theorem does not rely on the numerical integrations. Its strict monotonicity is pointwise: for increasing \(s\), the square-root integrand in (2) decreases strictly away from the two polar directions, a set of full spherical measure when \(m\ge2\).

The checker also verifies the dimension-\(1\) boundary phenomenon:
\[
(r-s)+(r+s)=2r,
\]
which explains why the one-section equivalence is stated only for \(d\ge3\).

## Relationship to prior work
The Banach Center open-problem session asks whether comparison of the first radial integrals for every affine hyperplane section through two points \(a,b\) forces the analogous comparison for the full body. The problem is stated for a general convex body and cites the theory of radial centers and generalized dual volumes.

Herburt's work on radial centers identifies the radial center of order \(1\) as the point maximizing the mean distance from the boundary over all directions and proves an interior-location theorem for smooth convex bodies. The earlier radial-center paper develops the associated generalized dual-volume selectors. These results provide the surrounding framework but do not state the one-hyperplane criterion above.

The present proof exploits a feature special to Euclidean balls: after the odd linear term cancels in the spherical average, the remaining radial integrand is pointwise monotone in eccentricity. Orthogonal projection then shows that every affine hyperplane section preserves the ordering of the ambient center distances.

Targeted searches for the problem together with Euclidean balls, affine sections, mean radial distance, radial centers, and monotonicity in eccentricity did not locate this equivalence or the strengthening from all common hyperplanes to one.

## Limitations
The result does not settle the open problem for arbitrary convex bodies.

It does not extend automatically from balls to ellipsoids, because the radial integral and spherical surface measure are not affine invariant.

The section argument requires \(d\ge3\). In dimension \(2\), the unique line through two distinct points has a one-dimensional ball section, and its two radial distances always sum to the chord length.

No quantitative stability estimate is claimed beyond the exact ordering equivalence.

## References
1. *Open Problem Session*, Banach Center Publications 84 (2009), 217--222, Problem 7.
2. I. Herburt, *Location of radial centres of convex bodies*, Advances in Geometry 8 (2008), 309--313. DOI: 10.1515/ADVGEOM.2008.019.
3. I. Herburt, M. Moszyńska, and Z. Peradzyński, *Remarks on radial centres of convex bodies*, Mathematical Physics, Analysis and Geometry 8 (2005), 157--172. DOI: 10.1007/s11040-005-2968-4.
