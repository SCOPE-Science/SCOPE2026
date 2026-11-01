# Exact Haar law of the centered outer radius of tetrahedral plane sections

## Finding
Consider the regular tetrahedron
\[
T=\operatorname{conv}\{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\}\subset\mathbb R^3.
\]
Let \(U\) be uniform on the unit sphere \(S^2\), put \(E=U^\perp\), and define the **centered outer radius**
\[
R(U)=\max\{\|x\|_2:x\in T\cap E\}.
\]
In particular, this is a radius measured from the tetrahedron's centroid, **not** the minimum-enclosing-circle radius or the Euclidean diameter of the section. Almost every section is either triangular or quadrilateral.

For \(1\le r\le\sqrt3\), set
\[
s=\sqrt{\frac{r^2-1}{2}},\quad a=\frac{\sqrt2s}{1+s},\quad b=\frac{s}{\sqrt2},\quad
M=\sqrt{1+a^2},\quad N=\sqrt{1+2b^2},
\]
\[
\Phi(s)=\arctan\!\left(\frac{ab}{MN+M+N+1+ab}\right),\qquad
\Psi(s)=3\arccos\!\left(\frac{s(2-s)}{1+2s^2}\right)-\pi\quad (s\ge\tfrac12).
\]
The complete **joint cumulative distribution with the polygon type** is
\[
\boxed{\mathbb P\bigl(R\le r,\ T\cap E\text{ is quadrilateral}\bigr)=\frac{24}{\pi}\Phi(s)}
\]
and
\[
\boxed{\mathbb P\bigl(R\le r,\ T\cap E\text{ is triangular}\bigr)=
\begin{cases}0,&1\le r\le\sqrt{3/2},\\[2pt]
\frac2\pi\Psi(s),&\sqrt{3/2}<r\le\sqrt3.
\end{cases}}
\]
Their sum is \(\mathbb P(R\le r)\). This unconditional CDF equals zero for \(r<1\) and one for \(r>\sqrt3\). The endpoint conventions give the same values at \(1\) and \(\sqrt3\), with no atoms. In particular, triangular sections have the sharp minimum possible centered outer radius \(\sqrt{3/2}\), whereas quadrilateral sections have possible radii arbitrarily close to \(1\). The total triangular-section probability is
\[
\mathbb P(\text{triangle})=\frac6\pi\arccos(1/3)-2,
\]
with complementary quadrilateral probability. At the triangle-onset threshold, its joint CDF has the exact quadratic contact
\[
\mathbb P(R\le r,\text{ triangle})
=\frac{8\sqrt3}{\pi}\bigl(r-\sqrt{3/2}\bigr)^2+
O\!\left(\bigl(r-\sqrt{3/2}\bigr)^3\right)
\quad(r\downarrow\sqrt{3/2}).
\]

## Assumptions and scope
The normal is Haar-uniform under the usual rotation-invariant spherical probability. The origin is the tetrahedron's centroid, and the chosen tetrahedron has edge length \(2\sqrt2\) and vertex norm \(\sqrt3\). Plane orientations \(U\) and \(-U\) are equivalent; using the uniform normal gives the correct unoriented Grassmannian measure. Degenerate normals with a vertex or an edge contained in the plane have spherical probability zero, and their values follow by continuity. No assertion is made about uncentered planes, other tetrahedra, minimum-enclosing-circle radii, or Euclidean diameters.

## Proof
**1. Spherical height coordinates and an exact edge formula.** Write the four vertices as \(v_1,\ldots,v_4\) and their signed heights as \(h_i=\langle U,v_i\rangle\). Since \(\sum_i v_i=0\) and \(\sum_i v_iv_i^{\mathsf T}=4I_3\), the vector \(h/2\) is Haar-uniform on the unit sphere in the three-dimensional subspace \(H=\{h\in\mathbb R^4:\sum_i h_i=0\}\). For a generic normal, a section vertex occurs exactly at an edge \(v_iv_j\) with \(h_i=p>0\) and \(h_j=-q<0\). Its position is
\[
x_{ij}=\frac{qv_i+pv_j}{p+q}.
\]
Because \(\|v_i\|^2=3\) and \(v_i\cdot v_j=-1\) when \(i\ne j\),
\[
\|x_{ij}\|^2=3-\frac{8pq}{(p+q)^2}.
\]
The maximum of this expression over all opposite-sign edge pairs is \(R^2\). Since \(pq/(p+q)^2\le1/4\), every section vertex has squared norm at least \(1\), while the displayed formula gives an upper bound of \(3\); this proves the support interval. Put \(s=\sqrt{(r^2-1)/2}\) and \(k=(1-s)/(1+s)\), with \(0\le s\le1\). Solving the quadratic inequality exactly shows
\[
\|x_{ij}\|\le r\quad\Longleftrightarrow\quad k\le p/q\le1/k.
\]
At \(k=0\), interpret this as no further restriction; at \(k=1\), it means \(p=q\). The event \(R\le r\) is the intersection of these inequalities for **all** opposite-sign pairs. Thus it depends only on a spherically homogeneous cone in \(H\).

**2. Quadrilateral sign cells.** There are six cells with exactly two positive and two negative heights; each corresponds to a quadrilateral. Scaling by a common positive factor (which does not change direction), one representative takes the form
\[
h=(\tfrac12+A,\tfrac12-A,-\tfrac12-B,-\tfrac12+B).
\]
The all-pairs inequalities above become
\[
|A|+k|B|\le(1-k)/2,\qquad k|A|+|B|\le(1-k)/2.
\]
This is an octagon with axial vertices \((\pm c,0),(0,\pm c)\), \(c=s/(1+s)\), and four diagonal vertices \((\pm d,\pm d)\), \(d=s/2\). In the orthonormal coordinates of \(H\), its cone directions are \((\sqrt2A,\sqrt2B,1)\). Decompose the spherical octagon into eight congruent triangles, each spanned by the rays
\[
(0,0,1),\qquad(a,0,1),\qquad(b,b,1).
\]
For unit vectors \(w_0,w_1,w_2\) on \(S^2\), the spherical area of the triangle equals
\[
2\arctan\frac{|\det(w_0,w_1,w_2)|}{1+w_0\cdot w_1+w_1\cdot w_2+w_2\cdot w_0}.
\]
Applying it to these three rays gives area \(2\Phi(s)\) per small triangle, hence area \(16\Phi(s)\) per sign cell. The six cells have disjoint interiors. Dividing their total spherical area by \(4\pi\) yields \(24\Phi(s)/\pi\).

**3. Triangular sign cells.** Four cells have one positive height and three negative heights, and four have the opposite signs. In a representative one-positive cell, scale the heights to \(h=(1,-q_1,-q_2,-q_3)\), where \(q_i\ge0\) and \(\sum_iq_i=1\). Since \(q_i\le1\), the edge condition is precisely \(q_i\ge k\) for each \(i\). The cell is nonempty exactly when \(3k\le1\), equivalently \(s\ge1/2\). When it is nonempty its spherical triangle has the three rays
\[
(1,-(1-2k),-k,-k),\quad(1,-k,-(1-2k),-k),\quad(1,-k,-k,-(1-2k)).
\]
Their normalized pairwise dot product is
\[
\gamma=\frac{1+2k-3k^2}{2-4k+6k^2}
=\frac{s(2-s)}{1-2s+3s^2}.
\]
Each interior spherical angle of this equilateral spherical triangle therefore has cosine \(\gamma/(1+\gamma)=s(2-s)/(1+2s^2)\). By the spherical-excess formula the triangle has area \(\Psi(s)\). Eight such sign cells contribute \(8\Psi(s)/(4\pi)=2\Psi(s)/\pi\). This proves both joint laws and the threshold.

**4. Endpoints and sharp onset.** When \(s=1\), the sign cones partition the sphere, so the CDF is one; the triangular area expression gives \(\Psi(1)=3\arccos(1/3)-\pi\), proving the stated polygon-type marginal. At \(s=0\), both sectors have area zero. At \(s=1/2\), the three rays for a triangular sign cell coincide and its area vanishes; differentiating \(\Psi\) shows
\[
\Psi(s)=\frac8{\sqrt3}\bigl(s-\tfrac12\bigr)^2+O\bigl((s-\tfrac12)^3\bigr).
\]
Differentiating \(s=\sqrt{(r^2-1)/2}\) gives \(ds/dr=r/(2s)\), hence \(ds/dr=\sqrt{3/2}\) at the threshold. The displayed quadratic onset follows. The minimum radius \(\sqrt{3/2}\) is realized by the facet-parallel central sections, and radius \(1\) by coordinate-plane central squares; planes containing a tetrahedral vertex reach the upper endpoint \(\sqrt3\).

## Verification
The standalone standard-library program `verify_tetra.py` reconstructs edge-intersection points with exact rational arithmetic and checks the height-ratio condition at seven rational parameters for more than a thousand generic integer normal vectors. It also independently computes spherical-triangle areas using unit-ray determinants, verifies the Gram-based spherical-excess formula, checks the exact endpoint normalization and the quadratic transition, and compares the joint laws with a seeded sample of 150,000 independent Haar-distributed plane normals. The actual program prints `PASS 7236 exact and structural assertions plus 150000 Haar-random plane samples`, followed by observed and analytic probabilities for seven thresholds. Sampling is not an infinite proof and has deliberately finite tolerance; the analytic cone partition proves the theorem.

Run `python verify_tetra.py` with Python 3.10 or later; no nonstandard packages are needed.

## Relationship to prior work
Guedon–Litvak–Tatarko–Vritsiou (2026) introduce probabilistic bounds for radii/diameters of random sections of general convex bodies, with applications to \(p\)-ellipsoids. Their inspected results do not give a finite-dimensional exact distribution for a regular tetrahedron. Dirksen (2015) analyzes volumes and extremal orientations of regular-simplex sections, rather than this radius distribution. The mathematically related published geometric results on regular-octahedron central-section diameters and simplex-section face counts concern different bodies or different observables; neither gives the radius law here by a direct equivalence. The present computation adds the entire joint radius–polygon-type law, notably the sharp triangular-section onset. Historical priority cannot be guaranteed from targeted searches, especially for older stereological studies.

## Limitations
The invariant is measured relative to the fixed tetrahedron centroid and is not the minimal enclosing radius of the section. The theorem is specific to uniform central planes in a regular tetrahedron of the displayed normalization; extension to off-center planes or arbitrary tetrahedra is unproved. Full historical priority review and independent mathematical validation remain outstanding. The probabilistic numerical tests are corroborating rather than exhaustive, and the numerical threshold comparisons use sampling error tolerances.

## References
1. O. Guedon, A. E. Litvak, K. Tatarko, B.-H. Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131, first publicly posted September 21, 2026. https://arxiv.org/abs/2609.24131
2. H. Dirksen, *Sections of the regular simplex – Volume formulas and estimates*, arXiv:1509.06408, first publicly posted September 21, 2015; *Mathematische Nachrichten* **290** (2017), 2567–2584. https://arxiv.org/abs/1509.06408
3. S. Webb, *Central slices of the regular simplex*, *Geometriae Dedicata* **61** (1996), 19–28 (as referenced in Dirksen).
4. S. Ciccariello, *The intersect distribution of the regular tetrahedron* (2005), stereological chord/intersect distribution; full-text comparison remains a residual priority risk. 
