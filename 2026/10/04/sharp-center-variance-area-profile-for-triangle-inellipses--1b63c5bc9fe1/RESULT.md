# Sharp center-variance area profile for triangle inellipses

## Finding

Let \(T\) be a nondegenerate Euclidean triangle of area \(\Delta\), and let \(E\) be a nondegenerate ellipse tangent to its three sides. If the center of \(E\) has barycentric coordinates \(t,u,v\) with respect to \(T\), set
\[
D=(t-u)^2+(u-v)^2+(v-t)^2,\qquad r=\sqrt{2D}.
\]
Then \(0\le r<1\). Writing \(A_S=\pi\Delta/(3\sqrt3)\) for the area of the Steiner inellipse and \(\eta=\operatorname{area}(E)/A_S\), the complete sharp fixed-\(D\) area profile is
\[
(1+r)\sqrt{1-2r}\le \eta\le (1-r)\sqrt{1+2r}\qquad (0\le r<1/2),
\]
while
\[
0<\eta\le (1-r)\sqrt{1+2r}\qquad (1/2\le r<1),
\]
with infimum \(0\) in the second range. The upper equality centers are exactly the permutations of \(((1-r)/3,(2+r)/6,(2+r)/6)\); for \(r<1/2\), the lower equality centers are exactly the permutations of \(((1+r)/3,(2-r)/6,(2-r)/6)\). Consequently
\[
1-\eta\ge 2D,
\]
and the coefficient \(2\) is globally sharp.

## Assumptions and scope

The triangle is nondegenerate and the ellipse is nondegenerate, lies in the triangle, and is tangent to all three side lines. Barycentric coordinates are normalized by \(t+u+v=1\). For a triangle inellipse its center lies in the open medial triangle, so \(0<t,u,v<1/2\). The quantity \(D\) is affine-invariant because barycentric coordinates are affine-invariant. No Euclidean distance from the center to the centroid is being asserted to be invariant.

The lower endpoint for \(r\ge 1/2\) is an infimum only: at fixed \(r\) it is approached when the center tends to the boundary of the medial triangle and the ellipse degenerates. The upper endpoint is attained for every \(0\le r<1\). At \(r=0\) both endpoints coincide at the Steiner inellipse.

## Proof

We first reconstruct the area formula rather than use it as a black box. Affine maps preserve barycentric coordinates, tangency, ellipse centers, and ratios of areas, so it is enough to work in an equilateral triangle of altitude \(H\). Choose inward unit normals
\[
n_1=(1,0),\qquad n_2=(-1/2,\sqrt3/2),\qquad n_3=(-1/2,-\sqrt3/2).
\]
If the center has barycentric coordinates \(t,u,v\), its perpendicular distances to the three opposite sides are \(d_1=Ht\), \(d_2=Hu\), and \(d_3=Hv\).

Write the centered ellipse as
\[
\{w}: {w}^{\mathsf T}Q^{-1}{w}\le 1\},
\]
where \(Q\) is symmetric positive definite. Its support distance in unit direction \(n\) is \(\sqrt{n^{\mathsf T}Qn}\). Tangency to the three sides therefore gives \(n_i^{\mathsf T}Qn_i=d_i^2\). For
\[
Q=\begin{pmatrix}a&b\\b&c\end{pmatrix},
\]
these three equations uniquely give
\[
a=d_1^2,\qquad b=\frac{d_3^2-d_2^2}{\sqrt3},\qquad c=\frac23(d_2^2+d_3^2)-\frac13d_1^2.
\]
A direct determinant calculation yields
\[
\det Q=-\frac13(d_1-d_2-d_3)(d_1-d_2+d_3)(d_1+d_2-d_3)(d_1+d_2+d_3).
\]
Since \(t+u+v=1\), this becomes
\[
\det Q=\frac{H^4}3(1-2t)(1-2u)(1-2v).
\]
The equilateral triangle has area \(H^2/\sqrt3\), while the ellipse has area \(\pi\sqrt{\det Q}\). Thus in every triangle
\[
\operatorname{area}(E)=\pi\Delta\sqrt{(1-2t)(1-2u)(1-2v)}. \tag{1}
\]
This also shows directly that positive definiteness is equivalent to the center lying in the open medial triangle.

Set
\[
x=1-2t,\qquad y=1-2u,\qquad z=1-2v.
\]
Then \(x,y,z>0\), \(x+y+z=1\), and
\[
(x-y)^2+(y-z)^2+(z-x)^2=4D=2r^2.
\]
Hence
\[
xy+yz+zx=\frac{1-r^2}3,
\]
while by (1)
\[
\eta=\sqrt{27xyz}. \tag{2}
\]
At fixed \(r\), both the sum and the pairwise sum of \(x,y,z\) are fixed, so maximizing or minimizing \(xyz\) is the only remaining problem.

For an interior extremum with \(r>0\), Lagrange multipliers for fixed \(x+y+z\) and fixed \(x^2+y^2+z^2\) imply, after subtracting any two stationarity equations, that at least two of \(x,y,z\) are equal. The two possible two-equal triples, up to permutation, are
\[
\left(\frac{1+2r}3,\frac{1-r}3,\frac{1-r}3\right)
\quad\text{and}\quad
\left(\frac{1-2r}3,\frac{1+r}3,\frac{1+r}3\right). \tag{3}
\]
The second triple is positive exactly when \(r<1/2\). Their products satisfy
\[
27xyz=1-3r^2+2r^3=(1-r)^2(1+2r)
\]
and
\[
27xyz=1-3r^2-2r^3=(1+r)^2(1-2r),
\]
respectively. The first is the maximum and the second the minimum when both are feasible. When \(r\ge1/2\), the fixed-\(r\) level set meets the boundary of the nonnegative simplex, where \(xyz=0\); therefore the positive simplex has infimum \(0\) and no minimum. Substituting these products into (2) proves the stated profile.

Transforming (3) back by \(t=(1-x)/2\), and similarly for \(u,v\), gives exactly the stated equality centers.

Finally,
\[
\eta\le (1-r)\sqrt{1+2r}\le 1-r^2,
\]
because after squaring the second inequality its difference is \(r^2(1-r)^2\ge0\). Since \(r^2=2D\), this gives \(1-\eta\ge2D\). Along the upper branch as \(r\to1^-\), one has \(\eta\to0\) and \(D\to1/2\), so no larger universal coefficient than \(2\) is possible.

## Verification

The accompanying deterministic script `verify_inellipse_profile.py` independently checks the support-matrix determinant identity, both equality branches, the complete upper/lower envelopes on dense fixed-\(r\) grids, and the global inequality \(\eta\le1-r^2\). These numerical checks are supplementary; the universal result follows from the symbolic proof above.

## Relationship to prior work

Horwitz gives a general area formula for an ellipse with prescribed center tangent to the three side lines of a triangle and explicitly identifies it as a generalization of Chakerian's triangle result. Specializing Horwitz's Lemma 6 to a center inside the triangle yields equation (1). Minda and Phelps prove the classical global statement that the Steiner inellipse uniquely maximizes area among ellipses contained in a triangle, with ratio \(\pi/(3\sqrt3)\).

The present claim retains the full center information instead of optimizing it away: for every fixed affine barycentric spread \(D\), it determines the exact attainable area interval, identifies both extremizing center branches, locates the transition at \(r=1/2\), and yields the globally sharp quantitative stability inequality \(1-\eta\ge2D\). Searches using the phrases “triangle inellipse area fixed barycentric center spread variance complete sharp interval Steiner”, “inellipse center areal coordinates area product fixed sum of squared barycentric deviations”, “quantitative Steiner inellipse area stability barycentric distance centroid sharp”, and “triangle inscribed ellipse center variance product (1-2t)(1-2u)(1-2v)” did not locate an equivalent fixed-spread profile.

## Limitations

The classical area formula and the global maximality of the Steiner inellipse are not claimed as new. The historical book chapter by Chakerian from 1979 was not directly available for full-text inspection here; Horwitz explicitly attributes the underlying triangle area formula to it. Older literature may use different terminology for the same fixed-center optimization, so historical exhaustiveness is not claimed. The stability measure \(D\) is an affine barycentric displacement, not ordinary Euclidean center distance.

## References

1. A. Horwitz, “The locus of centers of ellipses inscribed in quadrilaterals,” arXiv:math/0312403, first publicly posted 2003-12-22. In particular, Lemma 6 gives the prescribed-center triangle area formula used for comparison.
2. D. Minda and S. Phelps, “Triangles, Ellipses, and Cubic Polynomials,” *American Mathematical Monthly* 115 (2008), 679–689, DOI 10.1080/00029890.2008.11920581. Corollary 4.2 proves global areal maximality of the Steiner inellipse.
3. G. D. Chakerian, “A Distorted View of Geometry,” in *Mathematical Plums*, Mathematical Association of America, 1979. This is cited by Horwitz as the source of the interior-center triangle area formula; it was not directly inspected here.
