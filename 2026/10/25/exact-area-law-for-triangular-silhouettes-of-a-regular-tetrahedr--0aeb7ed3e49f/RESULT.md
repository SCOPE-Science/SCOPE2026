# Exact area law for triangular silhouettes of a regular tetrahedron

## Finding
Let \(T\subset\mathbb R^3\) be the regular tetrahedron with vertices
\[
(1,1,1),\quad(1,-1,-1),\quad(-1,1,-1),\quad(-1,-1,1).
\]
For a Haar-uniform plane normal \(U\in S^2\), let \(B\) be the Euclidean area of the orthogonal shadow of \(T\) on \(U^\perp\), and let \(N\) be its number of vertices. Almost surely \(N\in\{3,4\}\). Define
\[
s_- =2\sqrt2,\qquad s_* =4\sqrt{2/3},\qquad s_+=2\sqrt3,
\quad p_3=\frac2\pi\left(\frac\pi2-3\arcsin(1/3)\right).
\]
For \(s_-<s<s_+\), put \(\beta(s)=\arccos(s/(2\sqrt3))\). Define the elementary spherical-segment function
\[
G(s)=\begin{cases}
2\left[\displaystyle\arccos\!\left(\frac1{3\sin\beta(s)}\right)
-\cos\beta(s)\arccos\!\left(\frac{\cos\beta(s)}{2\sqrt2\sin\beta(s)}\right)\right],&s<s_*,\\[6pt]
0,&s\ge s_*.
\end{cases}
\]
Then the **entire area distribution marked by triangular silhouette** is
\[
\boxed{\ \Pr(B>s,\ N=3)=4\left(1-\frac{s}{2\sqrt3}\right)-\frac6\pi G(s),\qquad s_-<s<s_+.\ }
\tag{1}
\]
For \(s\le s_-\), the probability equals \(p_3\); for \(s\ge s_+\), it is zero. In particular \(\Pr(B>s\mid N=3)\) is (1) divided by \(p_3\). The exactly linear upper branch starts at \(s_*\). At the branch transition, from below,
\[
\boxed{\ \Pr(B>s,N=3)=4\left(1-\frac{s}{2\sqrt3}\right)
-\frac6\pi\left(\frac23\right)^{1/4}(s_*-s)^{3/2}
+O\bigl((s_*-s)^{5/2}\bigr).\ }
\tag{2}
\]
The density of triangular-silhouette shadow area therefore has a square-root cusp at \(s_*\). The support of \(B\mid N=3\) is exactly \([2\sqrt2,2\sqrt3]\), whereas quadrilateral shadows can have area as large as \(4\).

The known unmarked distribution of \(B\), together with (1), also determines the complete marked \((B,N)\) law through \(\Pr(B>s,N=4)=\Pr(B>s)-\Pr(B>s,N=3)\). This latter subtraction is not a separate claim of novelty.

## Assumptions and scope
The vertices specify a tetrahedron of edge length \(2\sqrt2\); all area constants refer to this normalization. The plane normal has normalized spherical area measure, so opposite normals correspond to the same plane. Degenerate orientations have probability zero. The event \(N=3\) means precisely that the projected fourth vertex is strictly inside the projected triangle of the other three.

For \(u\in S^2\), let \(m(u)=\max_i |u_i|\) and \(l(u)=\sum_i|u_i|\). The exact brightness identity and silhouette condition are
\[
B(u)=\sum_{v\in\operatorname{vert}(T)}|v\cdot u|
=\max\{4m(u),\,2l(u)\},\qquad
N(u)=3\ \Longleftrightarrow\ l(u)>2m(u),
\tag{3}
\]
away from equality surfaces. Equation (3) fixes both the geometric classification and the normalization.

## Proof
**1. Shadow area and silhouette cones.** Each face of \(T\) has area \(2\sqrt3\) and an outward unit normal equal to the negative of the opposing vertex divided by \(\sqrt3\). Cauchy's projected-area formula gives the first expression in (3). Sign expansion, or sorting the three absolute coordinates, gives the maximum representation. A projected tetrahedron is triangular precisely when the plane-normal ray belongs to the positive or negative tangent cone of one vertex. Within the positive coordinate octant, the three supporting rays of such a cone are \((1,1,0)\), \((1,0,1)\), and \((0,1,1)\); hence its spherical triangle is
\[
\mathcal C=\{u\in S^2: u_i>0,\ u_i<u_j+u_k\ \text{for all distinct }i,j,k\}.
\]
The seven other relevant spherical triangles are its coordinate-sign reflections. Each triangle has spherical area \(\Omega=\pi/2-3\arcsin(1/3)\), giving the known \(p_3=8\Omega/(4\pi)\).

**2. Restriction to a cap.** On \(\mathcal C\) the brightness is \(B(u)=2(u_1+u_2+u_3)=2\sqrt3\,c\cdot u\), where \(c=(1,1,1)/\sqrt3\). Thus \(B>s\) cuts the spherical triangle by a cap of radius \(\beta(s)=\arccos(s/(2\sqrt3))\) centered at \(c\). Its spherical circumradius is \(\arccos\sqrt{2/3}\) (distance to each of the three vertices), and its inradius is \(r=\arcsin(1/3)\) (distance to each of the three great-circle sides). Consequently when \(s_-<s<s_+\), the cap is contained in the positive octant; when \(s\ge s_*\), it lies inside the whole triangle. The transition condition \(\beta(s_*)=r\) is exactly \(s_*=4\sqrt{2/3}\).

For \(s<s_*\), the cap protrudes across three congruent triangle sides. The three external spherical pieces are disjoint: within the octant no point can simultaneously satisfy two strict inequalities \(u_i>u_j+u_k\). The cap area \(2\pi(1-\cos\beta)\) therefore loses precisely three equal side segments of area \(G(s)\).

**3. Exact spherical segment.** For the side \(u_1=u_2+u_3\), take the outward hemisphere centered at \(n=(1,-1,-1)/\sqrt3\); its center satisfies \(c\cdot n=-1/3\). The excluded segment is the intersection of the cap \(\{c\cdot u>\cos\beta\}\) with the hemisphere \(\{n\cdot u>0\}\). The spherical triangle with vertices the cap center \(c\), the hemisphere center \(n\), and one boundary-intersection point has angle \(A\) at \(c\) and angle \(C\) at the boundary intersection, satisfying
\[
\cos A=\frac{\cos\beta}{2\sqrt2\sin\beta},
\qquad \cos C=-\frac1{3\sin\beta}.
\]
The lens consists of two equal spherical sectors, and Gauss--Bonnet (equivalently sector minus two spherical triangles) gives its area
\[
2(\pi-C-\cos\beta\,A)
=2\left(\arccos\!\frac1{3\sin\beta}
-\cos\beta\arccos\!\frac{\cos\beta}{2\sqrt2\sin\beta}\right)=G(s).
\]
This derivation establishes the specified arccosine branches because \(r<\beta<\arccos\sqrt{2/3}<\pi/2\). The eight disjoint silhouette cones contribute
\[
\Pr(B>s,N=3)=\frac8{4\pi}\left[2\pi(1-\cos\beta)-3G(s)\right],
\]
proving (1) with no probabilistic independence assumption.

**4. Sharp tangency onset.** As \(s\uparrow s_*\), let \(\delta=\beta(s)-r\). The outward great-circle boundary has geodesic curvature zero and the small-circle boundary has geodesic curvature \(\cot r=2\sqrt2\). Tangential coordinates at their contact give the cap's excess normal displacement \(\delta-\sqrt2 x^2+O(\delta^2+|x|^3)\). Integrating over \(|x|<\sqrt{\delta/\sqrt2}\) yields
\[
G(s)=\frac43 2^{-1/4}\delta^{3/2}+O(\delta^{5/2}).
\]
Since \(\delta=(\sqrt3/2)(s_*-s)+O((s_*-s)^2)\), the coefficient simplifies to \((2/3)^{1/4}\), proving (2). Smoothness and reflection symmetry of the two curves remove an order-\(\delta^2\) correction: in geodesic tangent coordinates the two boundary graphs and their separation are even functions of the tangential coordinate. This also establishes the stated remainder. The final support statements follow from the cap inradius and circumradius and from (3): all triangular orientations have brightness at most \(2\sqrt3\), while axial normals yield quadrilateral brightness \(4\).

## Verification
The standalone `verify.py` reconstructs the area directly from projected tetrahedron vertices, independently classifies triangular versus quadrilateral convex hulls, evaluates the spherical segment by both its elementary expression and direct one-dimensional spherical quadrature, and compares the marked tail formula with \(1{,}900{,}000\) Haar-uniform sample directions. It additionally checks that integrating the marked tail recovers the previously published first and second area moments conditional on a triangular silhouette. These finite checks support but do not replace the geometric derivation.

To rerun: install Python with NumPy and SciPy, and execute `python verify.py`. A successful execution ends with `ALL_MARKED_TETRAHEDRAL_SHADOW_CHECKS_OK`.

## Relationship to prior work
Finch's 2012 analysis states the unconditional tetrahedral shadow-area moments, silhouette frequencies, and a **directional piecewise formula** for area in a dodecant (especially §2.1 and §5); these are acknowledged rather than claimed as new. An exact tetrahedral brightness marginal density was subsequently obtained by Abas in 2026, which determines the unmarked distribution \(B\) but not by itself how its mass splits between triangular and quadrilateral silhouettes. Published area-weighted silhouette identities for arbitrary tetrahedra determine the first two **conditional moments**, rather than the present complete conditional law.

The additional step here is an exact evaluation of the cap cut out of each **triangle of silhouette-normal directions**, including the sharp cap-to-side transition, yielding all conditional quantiles and tail probabilities, not only one or two moments. In particular an unmarked CDF and two conditional moments together do not algebraically determine the marked CDF. The older unweighted silhouette law and this new marked distribution are distinct statements.

## Limitations
The formula applies to the fixed, regular three-dimensional tetrahedron with Haar-uniform orthogonal projections and its exact edge-length normalization. It is not a conditional distribution formula for arbitrary irregular tetrahedra, arbitrary viewing laws, or projections into different dimensions. The 2026 brightness-density study was bibliographically confirmed but its full text could not be inspected through the available lawful access routes; this is a material residual originality risk, especially for appendices that might contain a joint area/silhouette law. Definitive historical priority and external independent review are not claimed.

## References
1. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1 (first public 12 March 2012), §§2.1, 5. https://arxiv.org/abs/1203.2464
2. D. V. Feldman and D. A. Klain, *Angles as Probabilities*, arXiv:0809.3459v1 (19 September 2008). https://arxiv.org/abs/0809.3459
3. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202v1 (first public 10 August 2026), especially the advertised tetrahedral brightness marginal. https://arxiv.org/abs/2609.26202
