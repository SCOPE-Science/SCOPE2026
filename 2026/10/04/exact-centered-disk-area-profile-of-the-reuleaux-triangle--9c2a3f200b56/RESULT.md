# Exact centered-disk area profile of the Reuleaux triangle
## Finding
Let \(K\) be a Reuleaux triangle of width \(w>0\), realized as the intersection of the three closed disks of radius \(w\) centered at the vertices \(V_0,V_1,V_2\) of an equilateral triangle of side \(w\). Let \(O\) be the common center and define
\[
d=OV_j=\frac{w}{\sqrt3},\qquad r_{\mathrm{in}}=w-d.
\]
For \(r\ge0\), put
\[
A(r)=\operatorname{area}\bigl(K\cap B(O,r)\bigr).
\]
For \(r_{\mathrm{in}}<r<d\), define
\[
\alpha(r)=\arccos\!\left(\frac{w^2-d^2-r^2}{2dr}\right),\qquad
\beta(r)=\arccos\!\left(\frac{d^2+w^2-r^2}{2dw}\right)
\]
and
\[
L(r)=r^2\alpha(r)-w^2\beta(r)+dr\sin\alpha(r).
\]
Then the centered-disk area profile is exactly
\[
A(r)=
\begin{cases}
\pi r^2,&0\le r\le r_{\mathrm{in}},\\
\pi r^2-3L(r),&r_{\mathrm{in}}<r<d,\\
\dfrac{\pi-\sqrt3}{2}w^2,&r\ge d.
\end{cases}
\]
On the open intervals where the formula is nonconstant,
\[
A'(r)=
\begin{cases}
2\pi r,&0<r<r_{\mathrm{in}},\\
2r\bigl(\pi-3\alpha(r)\bigr),&r_{\mathrm{in}}<r<d,\\
0,&r>d.
\end{cases}
\]
The one-sided derivatives agree at both transition radii because \(\alpha(r_{\mathrm{in}})=0\) and \(\alpha(d)=\pi/3\). Therefore, if \(X\) is uniformly distributed in \(K\), the exact distribution function of \(OX\) is
\[
\mathbb P(OX\le r)=\frac{A(r)}{(\pi-\sqrt3)w^2/2},
\]
with density \(A'(r)/((\pi-\sqrt3)w^2/2)\) on \((0,d)\).

## Assumptions and scope
The geometry is Euclidean and planar. The width parameter satisfies \(w>0\). The centered disk is always centered at the common centroid, circumcenter, and incenter \(O\) of the generating equilateral triangle. The profile concerns ordinary planar area, not an inner parallel set of \(K\). The endpoint values include the entire range from the maximal centered inscribed disk through the smallest centered circumscribed disk.

## Proof
Place \(O\) at the origin and write \(V_0+V_1+V_2=0\), with \(|V_j|=d=w/\sqrt3\). Since
\[
K=\bigcap_{j=0}^2 B(V_j,w),
\]
the disk \(B(O,r)\) is contained in \(K\) for \(0\le r\le w-d=r_{\mathrm{in}}\), giving \(A(r)=\pi r^2\). Conversely, \(K\subset B(O,d)\), so for \(r\ge d\) the area is the classical Reuleaux value \((\pi-\sqrt3)w^2/2\).

It remains to compute the intermediate range \(r_{\mathrm{in}}<r<d\). For each generating center define the excluded lune
\[
E_j(r)=B(O,r)\setminus B(V_j,w).
\]
These three lunes are pairwise disjoint in area. Indeed, suppose a point \(x\) with \(|x|\le r<d\) were outside both \(B(V_0,w)\) and \(B(V_1,w)\). Using \(V_0+V_1=-V_2\),
\[
|x-V_0|^2+|x-V_1|^2
=2|x|^2+2d^2+2x\cdot V_2
\le 2r^2+2d^2+2rd
<6d^2=2w^2,
\]
contradicting \(|x-V_0|>w\) and \(|x-V_1|>w\). Boundary intersections have zero area, so
\[
A(r)=\pi r^2-3\operatorname{area}(E_0(r)).
\]

The circles \(\partial B(O,r)\) and \(\partial B(V_0,w)\) meet in two points symmetric about the line \(OV_0\). Let \(2\alpha\) be the angle subtended at \(O\) by the arc of \(\partial B(O,r)\) lying outside \(B(V_0,w)\), and let \(2\beta\) be the corresponding angle at \(V_0\). The cosine rule in the triangle formed by the two centers and either intersection point gives
\[
\cos\alpha=\frac{w^2-d^2-r^2}{2dr},\qquad
\cos\beta=\frac{d^2+w^2-r^2}{2dw}.
\]
The lune is the circular segment of the radius-\(r\) disk beyond the common chord minus the radius-\(w\) segment lying between that chord and the Reuleaux arc. If \(h\) is the half-chord length, then
\[
h=r\sin\alpha=w\sin\beta,
\]
and the distances from the two centers to the common chord give
\[
w\cos\beta=d+r\cos\alpha.
\]
Thus
\[
\begin{aligned}
\operatorname{area}(E_0(r))
&=r^2(\alpha-\sin\alpha\cos\alpha)
-w^2(\beta-\sin\beta\cos\beta)\\
&=r^2\alpha-w^2\beta+dh\\
&=r^2\alpha-w^2\beta+dr\sin\alpha=L(r).
\end{aligned}
\]
Substitution yields the middle formula.

For the derivative, inspect the circle \(\partial B(O,r)\). Each excluded lune removes from this circle one arc of angular measure \(2\alpha(r)\), and the three removed arcs are disjoint for \(r<d\). Hence the length of the portion of \(\partial B(O,r)\) lying in \(K\) is
\[
2\pi r-6r\alpha(r)=2r\bigl(\pi-3\alpha(r)\bigr).
\]
The polar coarea identity gives this as \(A'(r)\). At \(r=r_{\mathrm{in}}\), the two circles are internally tangent and \(\alpha=0\); at \(r=d\), \(\cos\alpha=1/2\), so \(\alpha=\pi/3\). The derivative therefore matches the adjoining pieces. Finally, division by the total Reuleaux area gives the probability distribution statement.

## Verification
The proof is exact and uses only Euclidean circle geometry, the equilateral-vector identity \(V_0+V_1+V_2=0\), and area additivity after proving the three excluded lunes are disjoint in the intermediate radial range. A deterministic checker independently computes the radial boundary of the Reuleaux triangle, integrates the polar area on a dense angular grid, and compares it with the closed formula at multiple scales and radii. It also checks the derivative formula by finite differences and the two endpoint identities. The checker passed; the numerical work is supplementary and is not used to establish the universal statement.

## Relationship to prior work
Classical Reuleaux-triangle literature records the construction as an intersection of three equal disks, its inradius and circumradius, and its total area. Bezdek studies disk-polygons and gives the Reuleaux triangle as the regular three-disk extremal object, with explicit global area and radius formulas. Later work on inner parallel sets of constant-width bodies computes a different family, obtained by eroding the boundary inward. The profile above instead intersects the fixed Reuleaux triangle with concentric disks centered at its symmetry center and therefore resolves how area accumulates with Euclidean distance from that center. Searches using centered-disk, concentric-circle, radial-area, distance-distribution, and disk-triangle formulations did not locate this exact piecewise profile or its radial density.

## Limitations
The literature search is not a proof of historical novelty. In particular, a 2000 paper specifically about the Reuleaux triangle and its center of mass was identifiable but its full text was not available in the inspected sources, so an equivalent radial integration formula there remains a residual risk. The result is specific to the three-disk Reuleaux triangle and to disks centered at its symmetry center; it does not give an analogous profile for arbitrary constant-width bodies or off-center intersections.

## References
1. W. Gleißner and H. Zeitler, “The Reuleaux Triangle and its Center of Mass,” *Results in Mathematics* 37 (2000), 335–344. DOI: 10.1007/BF03322004.
2. E. M. Harrell, “A Direct Proof of a Theorem of Blaschke and Lebesgue,” arXiv:math/0009137 (2000); later *Journal of Geometric Analysis* 12 (2002), 81–90. DOI: 10.1007/BF02930861.
3. M. Bezdek, “On a Generalization of the Blaschke–Lebesgue Theorem for Disk-Polygons,” arXiv:0903.5361 (2009); *Contributions to Discrete Mathematics* 6 (2011), 77–85. DOI: 10.55016/ojs/cdm.v6i1.61918.
4. B. Bogosel, “On the Blaschke–Lebesgue Theorem for the Cheeger Constant via Areas and Perimeters of Inner Parallel Sets,” arXiv:2303.15559 (2023).
