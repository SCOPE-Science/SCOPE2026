# Spherical antiprism packing–covering bifurcation and sharp polar-hole switch

## Finding
For every integer \(n\ge3\), consider the \(2n\)-site antiprism configuration \(\mathcal A_n(h)\) on the unit sphere, with \(n\) equally spaced sites on each of the two circles at heights \(\pm h\), with the lower circle rotated by \(\pi/n\), and \(0<h<1\). Define the spherical packing radius as half the minimum intersite angular distance and the spherical covering radius as the largest angular distance to the nearest site. Put \(c=\cos(\pi/n)\).

**Complete optimality theorem.** Within this one-parameter family, the packing radius is uniquely maximized at
\[
h_{\mathrm{pack}}^2=\frac{1+c-2c^2}{3+c-2c^2},
\]
where the antiprism has equal lateral and ring-edge lengths. The covering radius is uniquely minimized at
\[
h_{\mathrm{cover}}^2=\frac{c}{1+c},\qquad
\rho_{\mathrm{min}}=\arccos\sqrt{\frac{c}{1+c}}.
\]
The two optima coincide if and only if \(n=3\). For every \(n\ge4\), the packing-optimal antiprism is strictly shorter than the covering-optimal antiprism, with exact squared-height gap
\[
h_{\mathrm{cover}}^2-h_{\mathrm{pack}}^2
=\frac{2c-1}{3+c-2c^2}>0.
\]

**Polar-hole phase transition.** The farthest points of the sphere from \(\mathcal A_n(h)\) are exactly the north and south poles when \(0<h<h_{\mathrm{cover}}\), precisely \(2n+2\) distinct polar and triangular-facet normal directions when \(h=h_{\mathrm{cover}}\), and exactly the \(2n\) triangular-facet normal directions when \(h_{\mathrm{cover}}<h<1\). The full profile is
\[
\cos\rho_n(h)=
\min\left\{h,\frac{h\sqrt{1-h^2}(1+c)}
{\sqrt{4h^2+(1-h^2)(1-c)^2}}\right\}.
\]
The packing and covering optima become asymptotically different as \(n\to\infty\):
\[
h_{\mathrm{pack}}\sim \frac{\sqrt3\,\pi}{2n},\qquad
h_{\mathrm{cover}}\to\frac1{\sqrt2},\qquad
\rho_n(h_{\mathrm{pack}})\to\frac\pi2,\qquad
\rho_n(h_{\mathrm{cover}})\to\frac\pi4.
\]
The last two limits show an asymptotic covering-radius loss of \(\pi/4\) when a packing-optimal antiprism is used for covering.

## Assumptions and scope
Let \(s=\sqrt{1-h^2}\). The sites are, for \(j=0,\ldots,n-1\),
\[
\begin{aligned}
p_j^+&=(s\cos(2\pi j/n),s\sin(2\pi j/n),h),\\
p_j^-&=(s\cos((2j+1)\pi/n),s\sin((2j+1)\pi/n),-h).
\end{aligned}
\]
All distances are intrinsic spherical angular distances on \(S^2\), i.e. \(d(u,v)=\arccos(u\cdot v)\). The covering quantity is \(\rho_n(h)=\max_{u\in S^2}\min_{p\in\mathcal A_n(h)}d(u,p)\). The packing quantity is \(r_n(h)=\frac12\min_{p\ne q\in\mathcal A_n(h)}d(p,q)\). The claim concerns only the specified staggered, equal-radius, opposite-latitude one-parameter family, not all \(2n\)-point configurations or arbitrary twists.

## Proof
**1. Packing.** Set \(\alpha=\pi/n\). The shortest possible same-ring Euclidean chord has length \(2s\sin\alpha\). The shortest possible cross-ring chord has length
\[
2\sqrt{h^2+s^2\sin^2(\alpha/2)}.
\]
Every other pair in its respective type has a greater or equal angular separation, hence also a greater or equal chord. The same-ring minimum decreases strictly as \(h\) increases; the cross-ring minimum increases strictly. Their unique intersection maximizes their minimum. Solving equality yields
\[
h^2=\frac{q}{1+q},\qquad
q=\sin^2\alpha-\sin^2(\alpha/2)=\frac{1+c-2c^2}{2},
\]
which simplifies to the asserted packing height. Equality of the two shortest chord types is exactly the condition that ring edges and lateral edges have equal lengths. Because \(\arcsin\) is strictly increasing, maximizing shortest chord also maximizes the spherical packing radius.

**2. Facets and covering.** The convex hull \(P=\operatorname{conv}\mathcal A_n(h)\) contains the origin in its interior. Its facets are the two parallel regular \(n\)-gons in the planes \(z=\pm h\) and the \(2n\) alternating lateral triangles. Indeed the side triangles connect each consecutive same-ring pair to the one intermediate site of the opposite ring; they are exposed supporting triangles by the angular ordering and together with the caps give a closed convex polyhedral boundary. The two cap facet planes have distance \(h\) from the origin.

For a representative lateral triangular facet, rotate coordinates so that the two upper vertices have longitudes \(\pm\alpha\) and the lower vertex longitude \(0\). Its outward normal is proportional to \((1,0,t)\), where equality of the three plane evaluations forces
\[
t=\frac{s(1-c)}{2h}.
\]
The distance from the origin to the facet plane is therefore
\[
\beta_n(h)=\frac{s(1+c)}{2\sqrt{1+t^2}}
=\frac{sh(1+c)}{\sqrt{4h^2+s^2(1-c)^2}}.
\]
All \(2n\) side facets have this distance by symmetry. For any unit direction \(u\), the largest site dot product equals the support function \(h_P(u)\). Since \(P\) contains the origin, the radius of its largest origin-centered ball is \(\min_{u\in S^2}h_P(u)\), which is also the smallest facet-plane distance. The largest nearest-site angular distance is the arccosine of this support-function minimum. This proves the full covering profile \(\cos\rho_n(h)=\min\{h,\beta_n(h)\}\).

The directions realizing this minimum are exactly the outward normals of facets at the smallest plane distance. To see the exhaustiveness, the origin-centered inball is tangent to precisely those facets, and any supporting plane tangent to this ball and to \(P\) must be one of their facet planes: an edge or vertex cannot be an additional contact because its Euclidean norm is strictly larger than the inradius. The cap normals are the two poles; the side normals are distinct and number \(2n\).

**3. Unique covering optimum and phase.** Put \(z=h^2\), \(d=1-c\), and write \(\beta_n(h)^2=F(z)\). Directly,
\[
F(z)=\frac{(1+c)^2z(1-z)}{d^2+(4-d^2)z}.
\]
The ratio \(F(z)/z\) is strictly decreasing in \(z\in(0,1)\), and is equal to one exactly when
\[
z=z_c=\frac{c}{1+c}.
\]
Thus \(\min\{h,\beta_n(h)\}=h\) strictly increases for \(z<z_c\). The derivative of \(F\) changes sign from positive to negative at the unique point
\[
z_0=\frac{1-c}{3-c}.
\]
Since \(c\ge1/2\), one has \(z_0<z_c\), so \(\beta_n(h)\) strictly decreases for \(z>z_c\). Therefore \(\min\{h,\beta_n(h)\}\) has its unique global maximum at \(h^2=z_c\), proving the covering minimum. The facet-contact classification in Step 2 yields the asserted exact \(2\), \(2n+2\), and \(2n\) farthest-point counts.

**4. Comparison and limits.** Substitution gives
\[
\frac{c}{1+c}-\frac{1+c-2c^2}{3+c-2c^2}
=\frac{2c-1}{3+c-2c^2}.
\]
As \(c=\cos(\pi/n)\ge1/2\), this is zero only for \(n=3\) and strictly positive for \(n>3\). Finally \(1-c\sim\pi^2/(2n^2)\) gives \(h_{\mathrm{pack}}\sim\sqrt3\,\pi/(2n)\), while \(h_{\mathrm{cover}}\to1/\sqrt2\). For \(n>3\) one has \(h_{\mathrm{pack}}<h_{\mathrm{cover}}\), hence \(\cos\rho_n(h_{\mathrm{pack}})=h_{\mathrm{pack}}\) by Step 3. This proves both limiting angular radii.

## Verification
A standalone Python 3 standard-library checker in `verify.py` independently enumerates all supporting planes from vertex triples for six values \(n\in\{3,4,5,6,9,13\}\), four characteristic heights each, and compares the smallest plane distance and multiplicity with the exact formulas. It also enumerates all intersite pairs and checks the two-distance packing formula and sampled global optimality inequalities. All 2412 numerical checks passed. The program tests finite instances only; the universal theorem is established by the analytic proof above.

## Relationship to prior work
Fowler, Tarnai, and Gáspár (2002) studied the transition from spherical circle packing to covering under an antipodal constraint, including an elongated pentagonal antiprism in the ten-site case. Their main optimization ranges over broader arrangements and reports finite cases and structural transitions; the new theorem instead gives the complete exact formula, uniqueness, and farthest-point phase transition for the fixed staggered two-latitude family for **every** integer \(n\ge3\). The classic octahedron coincidence at \(n=3\) is already known and is included as a boundary case, not a separate originality claim. Brauchart and collaborators (2015) develop the spherical covering-radius/hole-radius formalism for random point sets, rather than this deterministic constrained family. Wimmer (2017) analyzes the unconstrained global eight-cap problem, not a general \(n\)-parametric antiprism formula. The exact equilateral-edge packing height itself is classical geometry; the contribution is its strict and asymptotically large separation from the uniquely covering-optimal height and the complete covering-hole transition.

## Limitations
The theorem does not assert global optimality among all \(2n\) sites on the sphere, nor even among all two-ring constellations with arbitrary relative rotation or unequal latitudes. Published numerical best-covering configurations may have smaller radii. The full Wimmer (2017) article could not be accessed through the available lawful routes; a general earlier antiprism formula in other specialist literature cannot be entirely excluded. The numerical checker is not an infinite proof and the result has not undergone independent scientific validation.

## References
1. P. W. Fowler, T. Tarnai, and Zs. Gáspár, *From circle packing to covering on a sphere with antipodal constraints*, Proceedings of the Royal Society A 458 (2002), 2275–2287; published online 24 July 2002. DOI: https://doi.org/10.1098/rspa.2002.0990.
2. J. S. Brauchart et al., *Random Point Sets on the Sphere—Hole Radii, Covering, and Separation*, arXiv:1512.07470, first submitted 23 December 2015. https://arxiv.org/abs/1512.07470.
3. L. Wimmer, *Covering the Sphere with Equal Circles*, Discrete & Computational Geometry 57 (2017), 763–781. DOI: https://doi.org/10.1007/s00454-017-9891-x (only a publisher preview was available for comparison).
4. P. W. Fowler and T. Tarnai, *Transition from spherical circle packing to covering: geometrical analogues of chemical isomerization*, Proceedings of the Royal Society A 452 (1996), 2043–2064. DOI: https://doi.org/10.1098/rspa.1996.0108 (abstract-level comparison).
