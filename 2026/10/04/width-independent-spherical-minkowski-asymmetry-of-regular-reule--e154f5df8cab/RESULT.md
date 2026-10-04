# Width-independent spherical Minkowski asymmetry of regular Reuleaux odd-gons

## Finding

Let
\[
n=2m+1\ge3
\]
be odd. Let
\[
v_0,\ldots,v_{n-1}\subset\mathbb S^2
\]
be the vertices of a regular spherical \(n\)-gon lying on a circle of spherical radius
\[
0<\rho<\frac{\pi}{2}.
\]
Let \(\omega\) be the maximum spherical distance between two vertices and assume
\[
0<\omega\le\frac{\pi}{2}.
\]
Following Lassak, define the spherical Reuleaux odd-gon
\[
W_{n,\omega}
=
\bigcap_{j=0}^{n-1}B_\omega(v_j).
\]
This is a spherical convex body of constant width \(\omega\).

Then
\[
\sin\rho
=
\frac{\sin(\omega/2)}
{\cos(\pi/(2n))}
\]
and the spherical circumradius of the Reuleaux body is exactly
\[
R(W_{n,\omega})=\rho.
\]

Hou and Jin define the spherical Minkowski measure of asymmetry of a constant-width body \(W\) by
\[
\operatorname{as}_s(W)
=
\frac{\sin R(W)}
{2\sin(\omega/2)-\sin R(W)}.
\]
For every regular spherical Reuleaux odd-gon this therefore becomes
\[
\boxed{
\operatorname{as}_s(W_{n,\omega})
=
\frac{1}
{2\cos(\pi/(2n))-1}
}.
\]

In particular, the value is exactly independent of the spherical width \(\omega\). It is also exactly the same formula as the classical Euclidean Minkowski asymmetry of a regular Reuleaux \(n\)-gon.

As odd \(n\) increases, these values decrease strictly. The first value is
\[
\operatorname{as}_s(W_{3,\omega})
=
\frac{1+\sqrt3}{2},
\]
which is the sharp planar-spherical upper endpoint proved by Hou and Jin, and
\[
\operatorname{as}_s(W_{n,\omega})
\longrightarrow1.
\]
More precisely,
\[
\operatorname{as}_s(W_{n,\omega})
=
1+\frac{\pi^2}{4n^2}
+\frac{11\pi^4}{192n^4}
+O(n^{-6}).
\]

## Assumptions and scope

The ambient sphere is the unit two-sphere with geodesic distance. The term “regular spherical \(n\)-gon” is used in Lassak's sense: the vertices are equally spaced on a spherical circle of radius below \(\pi/2\).

For odd \(n\), each vertex has two farthest vertices at cyclic separations
\[
\frac{n-1}{2}
\quad\text{and}\quad
\frac{n+1}{2}.
\]
Their common distance is denoted by \(\omega\). Lassak defines the spherical Reuleaux odd-gon as the intersection of the radius-\(\omega\) spherical disks centered at the vertices and proves that, when \(\omega\le\pi/2\), this intersection is a convex body of constant width.

The theorem concerns the Hou–Jin asymmetry, which is defined for spherical constant-width bodies through their width and circumradius. It does not claim a definition of Minkowski asymmetry for arbitrary spherical convex bodies.

## Proof

Put
\[
t=\frac{\pi}{n}.
\]
Choose the center \(o\) of the generating spherical circle as north pole. Consecutive vertices differ in azimuth by \(2t\). Since \(n\) is odd, two farthest vertices differ in azimuth by
\[
\pi-t.
\]

The spherical cosine law for the triangle formed by \(o\) and such a farthest pair gives
\[
\cos\omega
=
\cos^2\rho
+
\sin^2\rho\cos(\pi-t).
\]
Since
\[
\cos(\pi-t)=-\cos t,
\]
we obtain
\[
\cos\omega
=
1-(1+\cos t)\sin^2\rho.
\]
Using
\[
1-\cos\omega=2\sin^2(\omega/2)
\]
and
\[
1+\cos t=2\cos^2(t/2)
\]
yields
\[
\sin\rho
=
\frac{\sin(\omega/2)}{\cos(t/2)}
=
\frac{\sin(\omega/2)}{\cos(\pi/(2n))}.
\]

It remains to identify the circumradius of the full curved Reuleaux body, not merely of its generating vertices.

First, all generating vertices belong to \(W_{n,\omega}\), because every pairwise vertex distance is at most \(\omega\). The regular vertex set itself has circumradius exactly \(\rho\). Indeed, in \(\mathbb R^3\),
\[
\frac1n\sum_{j=0}^{n-1}v_j
=
(\cos\rho)o.
\]
If a spherical ball \(B_s(c)\) contains every vertex, then
\[
\langle c,v_j\rangle\ge\cos s
\]
for every \(j\). Averaging gives
\[
(\cos\rho)\langle c,o\rangle
\ge
\cos s.
\]
Since \(\langle c,o\rangle\le1\),
\[
\cos s\le\cos\rho.
\]
Here all relevant radii are at most \(\pi/2\), so \(s\ge\rho\). Thus
\[
R(W_{n,\omega})\ge\rho.
\]

Second, the closed ball
\[
B_{\omega-\rho}(o)
\]
lies inside every defining ball \(B_\omega(v_j)\). For any point \(x\) of this ball,
\[
d(x,v_j)
\le
d(x,o)+d(o,v_j)
\le
(\omega-\rho)+\rho
=
\omega.
\]
Hence
\[
B_{\omega-\rho}(o)\subset W_{n,\omega},
\]
so the inradius satisfies
\[
r(W_{n,\omega})\ge\omega-\rho.
\]

Hou and Jin prove for every spherical constant-width body that the insphere and circumsphere are concentric and their radii satisfy
\[
r(W)+R(W)=\omega.
\]
Therefore
\[
R(W_{n,\omega})
=
\omega-r(W_{n,\omega})
\le
\rho.
\]
Together with the opposite inequality already proved,
\[
R(W_{n,\omega})=\rho.
\]

Finally, Hou and Jin's definition gives
\[
\operatorname{as}_s(W_{n,\omega})
=
\frac{\sin\rho}
{2\sin(\omega/2)-\sin\rho}.
\]
Substituting
\[
\sin\rho
=
\frac{\sin(\omega/2)}{\cos(\pi/(2n))}
\]
cancels the width completely:
\[
\operatorname{as}_s(W_{n,\omega})
=
\frac{1}{2\cos(\pi/(2n))-1}.
\]

Strict decrease in odd \(n\) follows because
\[
\cos(\pi/(2n))
\]
strictly increases with \(n\). The stated asymptotic expansion follows by expanding
\[
\frac{1}{2\cos x-1}
\]
at \(x=0\) and then setting
\[
x=\frac{\pi}{2n}.
\]

## Verification

The accompanying `verify.py` reconstructs the generating vertices in \(\mathbb R^3\) for every odd
\[
3\le n\le63
\]
and for several widths up to \(\pi/2\). It checks that the maximum vertex distance is the prescribed width, verifies the exact regular-vertex average used in the circumradius proof, and evaluates the Hou–Jin formula against the closed expression.

It also samples the boundary of the inner ball
\[
B_{\omega-\rho}(o)
\]
and verifies membership in every defining radius-\(\omega\) disk, checks the Reuleaux-triangle endpoint and strict monotonicity, and tests the displayed asymptotic coefficients.

The script was replayed from its packaged path and returned:

`VERIFY_OK spherical Reuleaux asymmetry profile`

The finite numerical replay is a consistency check only. The all-\(n\), all-\(\omega\) result follows from spherical trigonometry, the exact ball inclusions, and the cited constant-width inradius/circumradius theorem.

## Relationship to prior work

Lassak introduced the spherical Reuleaux odd-gon explicitly as the intersection of equal spherical disks centered at the vertices of a regular odd-gon and proved that it is a body of constant width when the defining diameter is at most \(\pi/2\). Lassak and Musielak later developed the constant-width theory further and again identify spherical Reuleaux odd-gons as examples.

Hou and Jin introduced the spherical Minkowski measure of asymmetry for constant-width bodies. Their planar-spherical corollary identifies spherical disks as the unique minimizers and spherical Reuleaux triangles as the unique maximizers. Their article does not give a regular Reuleaux odd-\(n\) profile.

In Euclidean geometry, Guo and Jin had already proved
\[
\operatorname{as}_\infty(R_n)
=
\frac{1}{2\cos(\pi/(2n))-1}
\]
for regular Reuleaux polygons. Thus the Euclidean formula itself is prior work. The new statement here is that the spherical Hou–Jin measure on the entire regular spherical Reuleaux odd-gon family has exactly the same expression, with complete cancellation of spherical width.

Targeted searches for spherical Reuleaux odd-gons together with Minkowski asymmetry, the exact secant-type denominator, circumradius, and regular odd-\(n\) profiles found no equivalent spherical formula. The closest indexed results concern Euclidean constant-width stability, reduced polygons, or unrelated regular-polygon invariants.

## Limitations

The proof uses the regular generating odd-gon and the constant-width regime
\[
0<\omega\le\frac{\pi}{2}
\]
appearing in Lassak's construction. It does not classify the asymmetry of irregular spherical Reuleaux polygons, nor does it claim a formula for widths above \(\pi/2\).

The Euclidean equality of formulas is a comparison, not an originality claim for the Euclidean expression. The spherical result is a short exact consequence of combining the regular spherical circumradius geometry with the later Hou–Jin definition; it does not establish a new extremality theorem among all spherical Reuleaux polygons.

The literature search was targeted rather than exhaustive. Older non-Euclidean constant-width sources may contain related radius formulas under different terminology, but the spherical Minkowski asymmetry used here was introduced only in the later Hou–Jin work.

## References

M. Lassak, “Width of spherical convex bodies,” Aequationes Mathematicae 89 (2015), 555–567, DOI 10.1007/s00010-013-0237-3.

M. Lassak and M. Musielak, “Spherical bodies of constant width,” Aequationes Mathematicae 92 (2018), 627–640, DOI 10.1007/s00010-018-0558-3; arXiv:1801.01161.

P. Hou and H. Jin, “The Minkowski Measure of Asymmetry for Spherical Bodies of Constant Width,” Wuhan University Journal of Natural Sciences 27 (2022), 367–371, DOI 10.1051/wujns/2022275367.

Q. Guo and H. Jin, “On a measure of asymmetry for Reuleaux polygons,” Journal of Geometry 102 (2011), 73–79, DOI 10.1007/s00022-011-0096-9.
