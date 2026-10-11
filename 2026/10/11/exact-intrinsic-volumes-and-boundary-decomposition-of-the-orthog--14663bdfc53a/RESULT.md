# Exact intrinsic volumes and boundary decomposition of the orthogonal three-disk hull

## Finding

Let \(R>0\). In Euclidean three-space let \(D_{xy}\), \(D_{xz}\), and \(D_{yz}\) be the three radius-\(R\) closed circular disks centered at the origin and lying in the three coordinate planes, and let
\[
K_R=\operatorname{conv}(D_{xy}\cup D_{xz}\cup D_{yz}).
\]
The boundary of \(K_R\) consists, up to common edges and endpoints, of exactly eight exposed equilateral triangular facets of side \(R\) and twenty-four congruent developable ruled surface patches. Its intrinsic volumes have the following exact forms:
\[
\boxed{\operatorname{Vol}_3(K_R)=\left(8-\frac{10\sqrt2}{3}\right)R^3},
\qquad
\boxed{\mathcal H^2(\partial K_R)=(12-4\sqrt3+2\pi)R^2}.
\]
Its largest centered inscribed Euclidean ball has radius \(R\sqrt{2/3}\), and its smallest centered containing Euclidean ball has radius \(R\). These are also its unrestricted inradius and circumradius.

## Assumptions and scope

The coordinate disks are
\[
D_{xy}=\{(x,y,0):x^2+y^2\le R^2\},\quad
D_{xz}=\{(x,0,z):x^2+z^2\le R^2\},\quad
D_{yz}=\{(0,y,z):y^2+z^2\le R^2\}.
\]
All three planes meet only at the center jointly: there is no common line contained in all three planes. The convex hull is the filled three-dimensional solid, not the union of the disks and not the intersection of cylinders. Surface area is the two-dimensional Hausdorff measure of the full boundary, including planar faces. The classification counts the relatively open two-dimensional strata; their common edges have zero surface measure.

## Proof

**1. Supporting faces.** A homothety reduces the calculation to \(R=1\). For a nonzero vector \(u=(u_1,u_2,u_3)\), maximizing the linear functional \(u\cdot x\) separately over the three disks gives
\[
h_K(u)=\max\{\sqrt{u_1^2+u_2^2},\sqrt{u_1^2+u_3^2},\sqrt{u_2^2+u_3^2}\}
=\sqrt{\|u\|_2^2-\min_i u_i^2}.
\]
When the least absolute coordinate is unique, precisely one disk attains this support value. Its exposed face is a single circle point (with the obvious coincident-point interpretation at zero coordinates). Such points contribute no two-dimensional surface stratum. When exactly two least absolute coordinates agree, with the remaining one strictly larger, two disks attain the support value, and the exposed face is their supporting segment. When all three absolute coordinates agree and are nonzero, all three disks attain it, and the exposed face is a triangle. These alternatives, including their limiting zero-coordinate cases, exhaust all supporting faces.

For \(u=(1,1,1)\), the three supporting vertices are
\[
(1/\sqrt2,1/\sqrt2,0),\quad(1/\sqrt2,0,1/\sqrt2),\quad(0,1/\sqrt2,1/\sqrt2).
\]
They form an equilateral triangle of side one and area \(\sqrt3/4\), lying in the supporting plane \(x+y+z=\sqrt2\). Its outward unit normal is \((1,1,1)/\sqrt3\), and the plane is at distance \(\sqrt{2/3}\) from the origin. Independent sign changes produce exactly eight distinct triangles, all of the same size.

**2. Ruled boundary patches.** By reflection and permutation, every remaining relatively open two-dimensional stratum is congruent to the following surface in the positive octant:
\[
F(\phi,t)=\bigl(\cos\phi,\,t\sin\phi,\,(1-t)\sin\phi\bigr),
\qquad 0<\phi<\pi/4,\quad 0<t<1.
\]
Indeed, this is the segment joining the support points of the \(xy\)- and \(xz\)-disks in direction \((\cos\phi,\sin\phi,\sin\phi)\). Three choices for the uniquely largest normal coordinate and eight sign octants yield twenty-four patches. Their interiors are disjoint, and supporting-face exhaustiveness shows that no additional two-dimensional pieces are missing. Because the tangent-plane normal along \(F\) is independent of \(t\), each patch is developable.

Direct differentiation gives
\[
F_\phi\times F_t=-\sin\phi\bigl(\cos\phi,\sin\phi,\sin\phi\bigr),
\quad
\mathrm dA=\sin\phi\sqrt{1+\sin^2\phi}\,\mathrm d\phi\,\mathrm dt.
\]
The outward unit normal is
\[
\nu(\phi)=\frac{(\cos\phi,\sin\phi,\sin\phi)}{\sqrt{1+\sin^2\phi}},
\quad
F(\phi,t)\cdot\nu(\phi)=\frac{1}{\sqrt{1+\sin^2\phi}}.
\]

**3. Surface area.** Each ruled patch has area
\[
\begin{aligned}
I&=\int_0^{\pi/4}\sin\phi\sqrt{1+\sin^2\phi}\,\mathrm d\phi
=\int_{1/\sqrt2}^{1}\sqrt{2-s^2}\,\mathrm ds\\
&=\frac12-\frac{\sqrt3}{4}+\frac\pi{12}.
\end{aligned}
\]
There are twenty-four such patches and eight triangles of area \(\sqrt3/4\), hence
\[
\mathcal H^2(\partial K_1)
=24I+8\frac{\sqrt3}{4}
=12-4\sqrt3+2\pi.
\]

**4. Volume.** The body contains the origin in its interior and has a piecewise smooth boundary, so the divergence theorem applied to the field \(x\mapsto x\) gives
\[
3\operatorname{Vol}_3(K_1)=\int_{\partial K_1} x\cdot\nu(x)\,\mathrm dA(x).
\]
On each ruled patch the integral is
\[
\int_0^1\!\int_0^{\pi/4}
\frac{\sin\phi\sqrt{1+\sin^2\phi}}{\sqrt{1+\sin^2\phi}}
\,\mathrm d\phi\,\mathrm dt
=1-\frac1{\sqrt2}.
\]
Each planar triangular facet contributes its area times its support distance, namely \((\sqrt3/4)\sqrt{2/3}=\sqrt2/4\). Therefore
\[
3\operatorname{Vol}_3(K_1)
=24\left(1-\frac1{\sqrt2}\right)
+8\frac{\sqrt2}{4}=24-10\sqrt2,
\]
which yields the stated volume formula.

**5. Radii and scaling.** On the Euclidean unit sphere, the support-function identity implies
\[
\min_{\|u\|_2=1}h_{K_1}(u)
=\sqrt{1-\max_{\|u\|_2=1}\min_i u_i^2}=\sqrt{2/3},
\quad \max_{\|u\|_2=1}h_{K_1}(u)=1.
\]
The centered balls of these radii are respectively inscribed in and circumscribed about \(K_1\). Because \(K_1=-K_1\), averaging any inscribed-ball center with its opposite puts a ball of at least the same radius at the origin. Likewise, the smallest enclosing ball of a centrally symmetric body is centered at the symmetry center. Finally a homothety by \(R\) multiplies volume by \(R^3\), area by \(R^2\), and radii by \(R\).

## Verification

The standalone script `verify.py` compares both closed formulas against independent three-dimensional convex hulls of increasingly fine polygonal samples from each disk boundary. It checks the support function against direct maximization, evaluates surface and divergence integrals numerically, verifies triangular geometry and tests homothety. The discretized polyhedral hulls are *inscribed approximations*, so their finite numerical agreement supports but does not replace the analytical supporting-face proof and integration above. Execute with `python verify.py` using NumPy and SciPy.

## Relationship to prior work

Finch, *Convex Hull of Two Orthogonal Disks* (first publicly posted 2012; arXiv:1211.4514), derives volume \(8/3\) and surface area \(2(2+\pi)\) for two centered orthogonal unit disks, as well as other two-disk configurations. The present set includes a third disk, with no common line shared by all three disk planes; its support-function tie pattern has eight triangular facets and twenty-four ruled patches instead of the two-disk boundary geometry. For unit radius the polar of this hull is the classical triple Steinmetz solid (tricylinder), since \(K_1^\circ=\{u:u_i^2+u_j^2\le1\text{ for all }i<j\}\). The tabulated tricylinder volume \(8(2-\sqrt2)\) belongs to this **polar** body, not to \(K_1\); it supplies no direct formula for the primal hull's volume or surface area.

Nash, Pir, Sottile and Ying, *Convex Hull of Two Circles in* \(\mathbb R^3\) (arXiv:1612.09382), classify two-circle hulls and their algebraic boundaries; it does not establish three-circle intrinsic volumes. Wu, Gupta, Kurzeja and Rossignac, *CHoCC: Convex Hull of Cospherical Circles and Applications to Lattices* (2020), study a class based on circles bounding disjoint spherical caps. The three great circles here do not bound pairwise disjoint hemispherical caps, and the cited abstract does not give the displayed volume or surface-area formula. This comparison is not a claim of exhaustive historical uniqueness.

## Limitations

The formulas apply to three *congruent*, *concentric*, *mutually perpendicular* circular disks. They do not assert corresponding formulas for unequal radii, displaced disks, arbitrary triples of planes, or more general collections of circles. The theorem concerns volume, surface area, boundary strata and radii, not mean width or full curvature measures. Earlier treatments under different terminology cannot be ruled out completely; the full article text for the 2020 cospherical-circle work was not available for detailed comparison.

## References

1. Steven R. Finch, *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514 (first version posted 19 November 2012), https://arxiv.org/abs/1211.4514 ; full text: https://arxiv.org/pdf/1211.4514 .
2. Evan D. Nash, Ata Firat Pir, Frank Sottile and Li Ying, *Convex Hull of Two Circles in* \(\mathbb R^3\), arXiv:1612.09382 (first version posted 30 December 2016), https://arxiv.org/html/1612.09382v2 .
3. Yaohong Wu, Ashish Gupta, Kelsey Kurzeja and Jarek Rossignac, *CHoCC: Convex Hull of Cospherical Circles and Applications to Lattices*, *Computer-Aided Design* **129** (2020), 102903, https://doi.org/10.1016/j.cad.2020.102903 ; 2019 poster abstract at https://igs2019.org/IGS2019-POSTER-PROCEEDINGS-LR.pdf .
4. Eric W. Weisstein, *Steinmetz Solid*, Wolfram MathWorld, https://mathworld.wolfram.com/SteinmetzSolid.html (standard tricylinder formulas; polar object, not the present hull).
