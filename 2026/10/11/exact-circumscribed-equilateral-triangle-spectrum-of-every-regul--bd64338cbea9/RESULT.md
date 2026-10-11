# Exact circumscribed-equilateral-triangle spectrum of every regular polygon
## Finding
Let \(P_n\subset\mathbb R^2\) be the centered regular \(n\)-gon with circumradius \(R>0\), where \(n\ge3\). For each angle \(\theta\), take the three supporting lines whose outward unit normals are
\[
u(\theta),\qquad
u(\theta+2\pi/3),\qquad
u(\theta+4\pi/3).
\]
Their supporting halfplanes contain \(P_n\) and intersect in an equilateral triangle, denoted \(T_n(\theta)\). Write \(\rho_n(\theta)\) for its inradius and \(A_n(\theta)\) for its area.

If
\[
3\mid n,
\]
then the complete spectra are
\[
\boxed{\rho_n(\theta)\in[R\cos(\pi/n),R]}
\tag{1}
\]
and
\[
\boxed{A_n(\theta)\in[3\sqrt3R^2\cos^2(\pi/n),3\sqrt3R^2]}.
\tag{2}
\]
The upper endpoint occurs exactly when a support normal points toward a polygon vertex, and the lower endpoint exactly when that normal is perpendicular to a side, modulo the polygon symmetries.

If
\[
3\nmid n,
\]
put
\[
C_n=\frac R3\left(1+2\cos\frac{2\pi}{3n}\right).
\tag{3}
\]
Then
\[
\boxed{\rho_n(\theta)\in\left[C_n\cos\frac{\pi}{3n},C_n\right]}
\tag{4}
\]
and
\[
\boxed{A_n(\theta)\in\left[3\sqrt3C_n^2\cos^2\frac{\pi}{3n},3\sqrt3C_n^2\right]}.
\tag{5}
\]
Every value in each interval is attained.

The orientation spread is therefore
\[
A_{\max}-A_{\min}=
\begin{cases}
3\sqrt3R^2\sin^2(\pi/n),&3\mid n,\\[4pt]
3\sqrt3C_n^2\sin^2(\pi/(3n)),&3\nmid n.
\end{cases}
\tag{6}
\]
As \(n\to\infty\) inside the two arithmetic regimes,
\[
A_{\max}-A_{\min}\sim
\begin{cases}
3\sqrt3\pi^2R^2/n^2,&3\mid n,\\[4pt]
(\sqrt3\pi^2/3)R^2/n^2,&3\nmid n.
\end{cases}
\tag{7}
\]
Thus the leading orientation sensitivity has a factor-nine jump according to divisibility by \(3\).

## Assumptions and scope
For a compact convex set \(K\) containing the origin, its support function is
\[
h_K(\phi)=\max_{x\in K}\langle x,u(\phi)\rangle,
\qquad
u(\phi)=(\cos\phi,\sin\phi).
\]
For three normals separated by \(2\pi/3\), the corresponding supporting halfplanes always form an equilateral triangle containing \(K\). This is the nonsmooth support-line version of the circumscribed equilateral triangles \(T(t)\) used in the evolutoid literature.

The theorem concerns the whole one-parameter family of equilateral support triangles. It does not assert that, when \(3\nmid n\), an area-minimizing enclosing triangle among all triangles is equilateral.

## Proof
Let
\[
u_j=u(\theta+2j\pi/3),
\qquad
h_j=h_K(\theta+2j\pi/3),
\qquad j=0,1,2.
\]
The three outward normals satisfy
\[
u_0+u_1+u_2=0.
\tag{8}
\]
If \(m\) and \(\rho\) are the incenter and inradius of the equilateral support triangle, its three sides have equations
\[
\langle x,u_j\rangle=h_j
=\langle m,u_j\rangle+\rho.
\]
Summing and using (8) gives the general identity
\[
\rho=\frac{h_0+h_1+h_2}{3}.
\tag{9}
\]
An equilateral triangle of inradius \(\rho\) has area
\[
3\sqrt3\,\rho^2,
\tag{10}
\]
which proves the first displayed identities in the finding.

Now specialize to \(P_n\). Put
\[
\Delta=\frac{2\pi}{n}.
\]
With one vertex at angular position \(0\), its support function is
\[
h_n(\phi)=R\cos d_n(\phi),
\qquad
d_n(\phi)=\operatorname{dist}(\phi,\Delta\mathbb Z)
\in[0,\Delta/2].
\tag{11}
\]

Suppose first that \(3\mid n\). Rotation through \(2\pi/3\) preserves \(P_n\), hence
\[
h_n(\theta)=h_n(\theta+2\pi/3)=h_n(\theta+4\pi/3).
\]
Equations (9) and (11) give
\[
\rho_n(\theta)=h_n(\theta),
\]
whose range is exactly
\[
[R\cos(\Delta/2),R].
\]
This proves (1)--(2) and the endpoint orientations.

Now assume \(3\nmid n\). Write \(n=3m+1\) or \(n=3m+2\). Modulo the period \(\Delta\), the three phases
\[
\theta,
\qquad
\theta+2\pi/3,
\qquad
\theta+4\pi/3
\]
are exactly
\[
t,
\qquad
t+\Delta/3,
\qquad
t-\Delta/3
\]
in some order. The sum in (9) has period \(\Delta/3\), so choose
\[
|t|\le\Delta/6.
\]
All three arguments then lie in one nearest-vertex cosine chamber, and (11) yields
\[
\begin{aligned}
3\rho_n(t)
&=R\left(\cos t+\cos(t+\Delta/3)+\cos(t-\Delta/3)\right)\\
&=R\left(1+2\cos(\Delta/3)\right)\cos t.
\end{aligned}
\tag{12}
\]
Therefore
\[
\rho_n(t)=C_n\cos t,
\qquad
|t|\le\frac{\pi}{3n}.
\tag{13}
\]
This proves (4). The cosine is continuous and strictly decreases with \(|t|\) on this chamber, so the maximum occurs at \(t=0\), the minima at the two endpoints, and every intermediate value occurs. Equation (10) gives (5).

Subtracting the squared endpoint radii gives (6). Finally,
\[
C_n\to R,
\qquad
\sin(\pi/n)\sim\frac\pi n,
\qquad
\sin(\pi/(3n))\sim\frac\pi{3n},
\]
which proves (7).

## Verification
The bundled `verify.py` reconstructs the support triangle directly from polygon vertices rather than assuming formula (9). For sampled \(n\) and \(\theta\), it computes the three support numbers by maximization over all vertices, intersects the three supporting lines, checks containment of every polygon vertex, verifies equality of the three triangle side lengths, and compares the shoelace area with
\[
3\sqrt3\left(\frac{h_0+h_1+h_2}{3}\right)^2.
\]

A second sweep checks the complete endpoint formulas for every \(3\le n\le150\), including both residue classes modulo \(3\). The finite computation is diagnostic only; the quantified theorem follows from the support-function phase reduction (11)--(13).

## Relationship to prior work
The support-line and support-function notation used here is standard in the evolutoid literature. Jerónimo-Castro's 2013 online paper writes the support line with outward normal \(u(t)\) and its support value \(p(t)\) explicitly.

The 2015 sequel by Aguilar-Arteaga, Ayala-Figueroa, González-García and Jerónimo-Castro introduces, for every orientation, an equilateral triangle \(T(t)\) circumscribed to a convex curve and denotes its incenter and inradius by \(m(t)\) and \(r(t)\). Their purpose is a circle characterization: constancy forced by midpoint conditions implies the curve is a circle. The inspected full text does not compute the orientation spectrum for regular polygons.

Minimum-enclosing-triangle literature already records that for regular convex \(n\)-gons with \(n=3k\), a minimum-area enclosing triangle is equilateral. Accordingly, no novelty is claimed for the bare fact that the lower endpoint in (2) is a global minimum when \(3\mid n\). The new content is the full orientation-resolved equilateral spectrum, the exact formulas in the two nonzero residue classes modulo \(3\), and the factor-nine asymptotic sensitivity split.

A later paper on circumscribed equiangular polygons proves circle characterizations in a broader setting. Its published abstract was checked, but its full text was not used for a noncoverage conclusion; it remains part of the residual historical risk.

Targeted searches under circumscribed equilateral triangles, enclosing equilateral triangles, regular polygons, support functions, orientation spectra, and the exact trigonometric fingerprints in (3)--(5) did not locate an implication-equivalent published formula.

## Limitations
The theorem is restricted to equilateral support triangles and regular polygons. It does not determine the globally minimum enclosing triangle for \(3\nmid n\).

The global minimum statement for regular \(3k\)-gons is prior work and is not part of the originality claim.

Because the final calculation is elementary after the support phases are aligned, an equivalent formula may exist in older rotor or circumscribed-polygon literature that is not well indexed. The later circumscribed-equiangular-polygon paper was available only at abstract level for the relevant comparison.

## References
1. J. Jerónimo-Castro, *On evolutoids of planar convex curves*, *Aequationes Mathematicae* 88 (2014), 97--103. DOI: 10.1007/s00010-013-0213-y. Published online 18 June 2013.
2. V. A. Aguilar-Arteaga, R. Ayala-Figueroa, I. González-García, J. Jerónimo-Castro, *On evolutoids of planar convex curves II*, *Aequationes Mathematicae* 89 (2015), 1433--1447. DOI: 10.1007/s00010-015-0352-4.
3. A. R. Cardoso and colleagues, *Implementation of linear minimum area enclosing triangle algorithm*, *Computational and Applied Mathematics*. DOI: 10.1007/s40314-014-0198-8.
4. J. Jerónimo-Castro, F. G. Jimenez-Lopez, U. Velasco-García, *Some characterizations of the circle related to circumscribed equiangular polygons*, *Boletín de la Sociedad Matemática Mexicana* 27 (2021). DOI: 10.1007/s40590-021-00372-w.
