# Exact translative convex-hull profile of every regular polygon
## Finding
Let \(P_m\subset\mathbb R^2\) be a regular Euclidean \(m\)-gon with \(m\ge3\). Define
\[
c^{\mathrm{tr}}(P_m)
=
\max_{t:\,P_m\cap(P_m+t)\ne\varnothing}
\frac{\operatorname{area}\operatorname{conv}(P_m\cup(P_m+t))}
{\operatorname{area}(P_m)}.
\]
Then
\[
\boxed{
c^{\mathrm{tr}}(P_m)=
\begin{cases}
\displaystyle
1+\frac{8\cos^3(\pi/(2m))}{m\sin(2\pi/m)},
& m\ \text{odd},\\[8pt]
\displaystyle
1+\frac{4}{m\sin(\pi/m)},
& m\equiv2\pmod4,\\[8pt]
\displaystyle
1+\frac{8}{m\sin(2\pi/m)},
& m\equiv0\pmod4.
\end{cases}}
\tag{1}
\]

There is also an exact directional phase. Put
\[
J_m(u)
=
d_{P_m}(u)\,w_{P_m}(u^\perp),
\tag{2}
\]
where \(d_{P_m}(u)\) is the longest chord length parallel to \(u\), and \(w_{P_m}(u^\perp)\) is the width in the perpendicular direction. If \(4\nmid m\), then \(J_m(u)\) is independent of \(u\). If \(m\equiv0\pmod4\), then
\[
4\cos^2\!\left(\frac{\pi}{m}\right)
\le
J_m(u)
\le
4,
\tag{3}
\]
and the maximum is attained in the vertex directions.

In particular, all three residue classes have the common limit
\[
c^{\mathrm{tr}}(P_m)\longrightarrow1+\frac4\pi
\qquad(m\to\infty).
\]

## Assumptions and scope
The quantity \(c^{\mathrm{tr}}\) is scale and affine invariant, but the proof is most transparent after scaling \(P_m\) to circumradius \(1\).

For a convex body \(K\), let
\[
D_K=\frac12(K-K)
\]
be its central symmetral. Then
\[
w_{D_K}(v)=w_K(v)
\]
for every direction \(v\). Also
\[
d_K(u)=2\rho_{D_K}(u),
\tag{4}
\]
where \(\rho_{D_K}\) is the radial function. Indeed, \(tu\in K-K\) exactly when two points of \(K\) differ by \(tu\); maximizing \(t\) gives the longest chord parallel to \(u\).

Thus
\[
J_K(u)=4\rho_{D_K}(u)h_{D_K}(u^\perp).
\tag{5}
\]
Formula (5) is also a direct explanation of why central symmetrization preserves the numerator in the standard planar formula for \(c^{\mathrm{tr}}\).

No claim is made here that regular \(m\)-gons minimize \(c^{\mathrm{tr}}\) among all convex \(m\)-gons when \(m\ge6\). That extremal problem is separate.

## Proof
We first solve the directional problem for a centrally symmetric regular \(N\)-gon \(Q_N\) of circumradius \(R\), where \(N\) is even. Put
\[
a=\frac{\pi}{N}.
\]
Orient \(Q_N\) so that one edge has outward unit normal of angle \(0\). In the edge-normal chamber
\[
-a\le\theta\le a,
\]
the radial function is
\[
\rho(\theta)
=
\frac{R\cos a}{\cos\theta}.
\tag{6}
\]

By reflection symmetry it is enough to take
\[
0\le\theta\le a.
\]

Suppose first that
\[
N\equiv2\pmod4.
\]
Then the direction \(\pi/2\) is a vertex direction. Hence the vertex nearest to the direction \(\theta+\pi/2\) is at angular distance \(\theta\), and
\[
h(\theta+\pi/2)=R\cos\theta.
\]
Combining with (6),
\[
4\rho(\theta)h(\theta+\pi/2)
=
4R^2\cos a.
\tag{7}
\]
Thus the product is constant in every direction.

Now suppose
\[
N\equiv0\pmod4.
\]
Then \(\pi/2\) is an edge-normal direction. For \(0\le\theta\le a\), the closest vertex to \(\theta+\pi/2\) is at angular distance \(a-\theta\), so
\[
h(\theta+\pi/2)=R\cos(a-\theta).
\]
Therefore
\[
4\rho(\theta)h(\theta+\pi/2)
=
4R^2\cos a\,
\frac{\cos(a-\theta)}{\cos\theta}.
\tag{8}
\]
Since
\[
\frac{\cos(a-\theta)}{\cos\theta}
=
\cos a+\sin a\tan\theta,
\]
the expression in (8) is strictly increasing on \([0,a]\). Its endpoints are
\[
4R^2\cos^2a
\quad\text{and}\quad
4R^2.
\tag{9}
\]

We now return to \(P_m\), scaled to circumradius \(1\).

If \(m\) is even, then
\[
D_{P_m}=P_m.
\]
For
\[
m\equiv2\pmod4,
\]
equation (7) with \(R=1\) gives
\[
\max_u J_m(u)
=
4\cos\frac{\pi}{m}.
\tag{10}
\]
For
\[
m\equiv0\pmod4,
\]
equations (8)--(9) give
\[
\max_u J_m(u)=4
\tag{11}
\]
and also the full range (3).

If \(m\) is odd, then
\[
D_{P_m}
\]
is a regular \(2m\)-gon. Its circumradius is half the largest distance between two vertices of \(P_m\), namely
\[
R
=
\cos\frac{\pi}{2m}.
\tag{12}
\]
Since
\[
2m\equiv2\pmod4,
\]
equation (7), now with
\[
a=\frac{\pi}{2m},
\]
gives the constant value
\[
J_m(u)
=
4R^2\cos a
=
4\cos^3\!\left(\frac{\pi}{2m}\right).
\tag{13}
\]

The planar translative convex-hull identity is
\[
c^{\mathrm{tr}}(K)
=
1+
\frac{\max_u d_K(u)w_K(u^\perp)}
{\operatorname{area}(K)}.
\tag{14}
\]
Finally,
\[
\operatorname{area}(P_m)
=
\frac m2\sin\frac{2\pi}{m}.
\tag{15}
\]
Substitution of (10), (11), and (13) into (14)--(15) yields exactly (1).

## Verification
The bundled `verify.py` independently constructs regular polygons, their central symmetrals, and their support and radial functions from polygon half-planes. It samples directions for every
\[
3\le m\le40
\]
and compares the numerically maximized product in (2) against the three closed forms.

It also checks the published small values
\[
c^{\mathrm{tr}}(P_3)=3,
\qquad
c^{\mathrm{tr}}(P_4)=3,
\qquad
c^{\mathrm{tr}}(P_5)=\frac{10+\sqrt5}{5},
\]
and verifies the constant-direction behavior in the two residue classes with \(4\nmid m\).

The sampling is only a regression test. The proof for every \(m\) is the exact chamber computation (6)--(13).

## Relationship to prior work
Horváth and Lángi give the general identity (14) and show that central symmetrization preserves its numerator. They determine the polygonal extremal constants only for three, four, and five sides, obtaining
\[
3,\qquad3,\qquad\frac{10+\sqrt5}{5},
\]
and then explicitly ask whether regular \(m\)-gons attain the corresponding extremal constants for every \(m\ge3\).

The formulas above evaluate the regular-polygon benchmark appearing on the right-hand side of that problem for every \(m\). They agree with all three published small cases. They do not solve the minimization problem for \(m\ge6\).

The constant-direction cases are consistent with the classical Radon-curve characterization of translative constant volume. In particular, regular polygons with \(4k+2\) sides are standard polygonal Radon examples. The new calculation needed for (1) is the exact value and the complete \(m\bmod4\) directional profile, including the nonconstant \(4k\)-gon branch.

A later full-text treatment of translative constant volume revisits the projection-body characterization but does not supply the all-\(m\) regular-polygon formula (1). Targeted searches using the invariant notation, touching-translate formulation, regular-polygon aliases, and numerical/trigonometric fingerprints did not locate an implication-equivalent published formula.

## Limitations
The result evaluates
\[
c^{\mathrm{tr}}(P_m)
\]
for the regular polygon. It does not prove that this value equals the infimum over all convex \(m\)-gons for \(m\ge6\), nor does it address the reflected-copy quantities from the same source problem.

The constant-direction phenomenon for residue classes with \(4\nmid m\) is compatible with previously known Radon-curve theory and is not asserted as a new classification by itself.

Because the proof begins from a published general reduction (14), an unindexed later computation of the same regular-polygon benchmark remains the main originality risk.

## References
1. Á. G. Horváth and Z. Lángi, *On the volume of the convex hull of two convex bodies*, arXiv:1302.6164v1, 25 February 2013; *Monatshefte für Mathematik* 174 (2014), 219--229. DOI: 10.1007/s00605-013-0526-x.
2. Á. G. Horváth and Z. Lángi, *On the convex hull and homothetic convex hull functions of a convex body*, *Geometriae Dedicata* 216 (2022), article 20. DOI: 10.1007/s10711-022-00673-y.
3. H. Martini and K. J. Swanepoel, *Antinorms and Radon curves*, arXiv:math/0409200v1, 13 September 2004; *Aequationes Mathematicae* 72 (2006), 110--138.
