# Polar moment and isotropic constant of regular Reuleaux odd-gons
## Finding
Let \(K_n(w)\subset\mathbb R^2\) be the regular Reuleaux \(n\)-gon of odd order
\[
n\ge5
\]
and constant width \(w>0\), centered at its dihedral center. Put
\[
t=\frac{\pi}{2n},
\qquad
u=\tan t.
\]
Then its polar second moment about the center is
\[
\boxed{
J_n(w)=
\int_{K_n(w)}\|x\|_2^2\,dx
=
\frac{w^4}{16}
\left[
2\pi(3+u^2)-nu(11+u^2)
\right].
}
\tag{1}
\]

The known area formula simplifies to
\[
A_n(w)=\frac{w^2}{2}(\pi-nu).
\tag{2}
\]
Because \(K_n(w)\) has rotational symmetry of order at least five, its centroid is the dihedral center and its covariance is scalar:
\[
\operatorname{Cov}(K_n(w))
=
\frac{J_n(w)}{2A_n(w)}I_2.
\tag{3}
\]
Consequently, with the planar normalization
\[
L_K^4=
\frac{\det\operatorname{Cov}(K)}
{\operatorname{area}(K)^2},
\]
the isotropic constant is
\[
\boxed{
L_{K_n}^2
=
\frac{
2\pi(3+u^2)-nu(11+u^2)
}{
8(\pi-nu)^2
}.
}
\tag{4}
\]

For width \(1\),
\[
J_n(1)
=
\frac{\pi}{32}
-\frac{\pi^3}{192n^2}
+\frac{\pi^5}{2560n^4}
+O(n^{-6}),
\tag{5}
\]
whereas
\[
L_{K_n}^2
=
\frac1{4\pi}
+
\frac{\pi^3}{180n^4}
+
O(n^{-6}).
\tag{6}
\]
Thus the second-order defect in the raw polar moment disappears completely after affine normalization: the isotropic-constant defect from the width-one disk is quartic.

The same closed expression in (1) is algebraically valid when \(n=3\), but the Reuleaux-triangle polar moment was already treated in engineering literature. The new family statement is therefore restricted to odd \(n\ge5\).

## Assumptions and scope
A regular Reuleaux \(n\)-gon is the constant-width curve obtained from a regular odd \(n\)-gon by replacing each side by the radius-\(w\) circular arc centered at the opposite vertex.

It is enough to prove (1) for
\[
w=1,
\]
because area scales quadratically and polar second moment scales quartically.

For width \(1\), the generating regular \(n\)-gon has circumradius
\[
R=\frac1{2\cos t}.
\tag{7}
\]
Indeed, the distance from any generating vertex to either of the two opposite vertices is \(1\).

The Reuleaux region is the disjoint union, up to boundaries, of the generating regular polygon and \(n\) congruent circular segments. This decomposition is used only for exact integration; no approximation is involved.

## Proof
Normalize to \(w=1\). Choose one side of the generating regular polygon so that its midpoint lies on the positive horizontal ray. Its endpoints, viewed from the opposite vertex that centers the corresponding Reuleaux arc, are
\[
(\cos t,\sin t),
\qquad
(\cos t,-\sin t).
\]
Thus the circular segment is the difference between a unit circular sector of half-angle \(t\) and the triangle spanned by those two unit vectors.

Let local coordinates \(y\) be centered at the arc center. For the sector \(S\),
\[
\operatorname{area}(S)=t,
\]
\[
\int_S\|y\|_2^2\,dy=\frac t2,
\]
and
\[
\int_S y_1\,dy=\frac{2\sin t}{3}.
\tag{8}
\]

For the isosceles triangle \(Q\) removed from the sector,
\[
\operatorname{area}(Q)=\sin t\cos t,
\]
\[
\int_Q\|y\|_2^2\,dy
=
\operatorname{area}(Q)\frac{2+\cos(2t)}6,
\]
and
\[
\int_Q y_1\,dy
=
\operatorname{area}(Q)\frac{2\cos t}{3}.
\tag{9}
\]

The arc center is at
\[
c=(-R,0)
\]
relative to the dihedral center. Therefore the contribution of one circular segment to the polar moment about the dihedral center is exactly
\[
J_{\mathrm{seg}}
=
R^2\bigl(\operatorname{area}(S)-\operatorname{area}(Q)\bigr)
+
\left(
\int_S\|y\|_2^2\,dy-\int_Q\|y\|_2^2\,dy
\right)
-
2R
\left(
\int_S y_1\,dy-\int_Q y_1\,dy
\right).
\tag{10}
\]

The generating regular polygon splits into \(n\) triangles with vertex at the origin and endpoint angle \(4t\). The polar moment of one such triangle is
\[
J_{\mathrm{poly},1}
=
\frac{R^4\sin(4t)(2+\cos(4t))}{12}.
\tag{11}
\]
Hence
\[
J_n(1)
=
n\left(
J_{\mathrm{poly},1}+J_{\mathrm{seg}}
\right).
\tag{12}
\]
Substituting (7)--(11), using
\[
nt=\frac\pi2,
\]
and reducing the trigonometric terms gives
\[
J_n(1)
=
\frac1{16}
\left[
2\pi(3+\tan^2t)
-
n\tan t(11+\tan^2t)
\right].
\]
Restoring the scale \(w^4\) proves (1).

For completeness, the same polygon-plus-segments decomposition gives
\[
A_n(1)
=
\frac{\pi}{2}
-\frac n2\tan t,
\]
which is (2) and agrees with the published regular-Reuleaux area formula.

Rotational symmetry makes both the centroid and every off-diagonal covariance entry vanish, while the two diagonal second moments agree. Their sum is
\[
\frac{J_n(w)}{A_n(w)},
\]
so each diagonal entry is
\[
\frac{J_n(w)}{2A_n(w)}.
\]
This proves (3), and substitution into the definition of \(L_K\) gives (4).

Finally, the Taylor expansion
\[
\tan\frac{\pi}{2n}
=
\frac{\pi}{2n}
+
\frac{\pi^3}{24n^3}
+
\frac{\pi^5}{240n^5}
+
O(n^{-7})
\]
inserted into (1)--(4) yields (5)--(6).

## Verification
The supplied `verify.py` symbolically reconstructs the sector and triangle moments in (8)--(11), sums them, and proves exact equality with (1).

It independently checks the area decomposition, the covariance/isotropic identity, and the series coefficients through the displayed orders.

As a numerical regression test, it also integrates the polar radial function
\[
\rho(\theta)
=
-R\cos\theta+
\sqrt{1-R^2\sin^2\theta}
\]
over one fundamental angular sector and compares the result with (1) for several odd values of \(n\).

The numerical integrations are supplementary. The quantified theorem follows from the exact decomposition and symbolic simplification.

## Relationship to prior work
The classical literature on Reuleaux polygons is rich in area, perimeter, width, circumradius, and symmetry inequalities. A full author-provided treatment of regular Reuleaux polygons gives an explicit all-\(n\) area formula and uses it in an asymmetry theorem. It does not contain the words “moment” or “inertia” in the searchable full text and does not state a covariance or isotropic-constant formula.

A 2014 engineering paper gives a detailed polar-moment calculation for the Reuleaux triangle. That special case is therefore treated as prior work. Formula (1) extends the same mechanically meaningful invariant to every regular Reuleaux odd-gon with \(n\ge5\).

The exact area in (2) is also prior work and is included only because it is needed to state the affine-invariant consequence (4).

Searches using “polar moment”, “second moment of area”, “covariance”, “isotropic constant”, regular Reuleaux pentagon/heptagon, and the distinctive \(\tan(\pi/(2n))\) parameter did not locate an implication-equivalent published family formula.

## Limitations
The result concerns the regular member of each odd-order Reuleaux class. It does not optimize the polar moment or isotropic constant over all irregular Reuleaux \(n\)-gons.

The Reuleaux-triangle moment is prior-covered and is not part of the novelty claim.

No monotonicity theorem for \(L_{K_n}\) over odd \(n\) is claimed, although the exact formula makes such questions directly accessible.

An older unindexed mechanics or constant-width source could contain an equivalent regular-family inertia computation; this remains the principal historical originality risk.

## References
1. H. Jin and Q. Guo, *On the Asymmetry for Convex Domains of Constant Width*, Communications in Mathematical Research 26 (2010), 176--182. DOI: 10.4208/cmr.v26.n2.p176.
2. H. Jin, *Asymmetry of Reuleaux polygons*, Beiträge zur Algebra und Geometrie 58 (2017), 311--317. DOI: 10.1007/s13366-016-0318-2.
3. M. S. Razumov, A. O. Gladyshkin, V. N. Kassikhin, A. I. Pykhtin, Y. V. Skripkina, *Stress calculation of moment transmitting roll with profile on the base of Reuleaux triangle*, Metallurgical and Mining Industry (2014).
4. Y. S. Kupitz and H. Martini, *On the isoperimetric inequalities for Reuleaux polygons*, Journal of Geometry 68 (2000), 171--191. DOI: 10.1007/BF01221070.
