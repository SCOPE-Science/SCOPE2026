# Two-term diameter-tail expansion for uniform point pairs in convex polytopes

## Finding
Let \(P\subset\mathbb R^d\) be a full-dimensional convex polytope, \(d\ge2\), with volume \(V\) and Euclidean diameter \(D\). If \(X,Y\) are independent uniform points of \(P\), then, for \(\varepsilon\downarrow0\),
\[
\Pr\bigl(\|X-Y\|>D-\varepsilon\bigr)
=A_P\varepsilon^{2d}+B_P\varepsilon^{2d+1}
+O_P(\varepsilon^{2d+2}). \tag{1}
\]
Both strictly positive coefficients are explicit **finite sums over ordered diametral vertex pairs and their simplicial tangent-cone pieces**, given below. They apply without simplicity, symmetry, or uniqueness of a longest segment.

For a Euclidean orthotope \(P=\prod_{i=1}^d[0,a_i]\) with \(a_i>0\), put \(V=\prod_i a_i\) and \(D=(\sum_i a_i^2)^{1/2}\). Formula (1) specializes to
\[
\boxed{\quad
\Pr(\|X-Y\|>D-\varepsilon)=
\frac{2^dD^{2d}}{(2d)!V^4}\varepsilon^{2d}
\left[1+\left(\frac{3D}{2d+1}\sum_i a_i^{-2}-\frac dD\right)\varepsilon
+O_P(\varepsilon^2)\right].\quad} \tag{2}
\]
For fixed \(V\), its leading coefficient obeys the sharp inequality
\[
\boxed{\quad A_P\ge \frac{2^d d^d}{(2d)!V^2},\quad}
\tag{3}
\]
with equality **only for a cube** among orthotopes. The comparison concerns the tails measured from each body's **own** Euclidean diameter.

## Assumptions and scope
A vertex \(p\) of \(P\) has tangent cone \(C_p=\{t(x-p):t\ge0,\ x\in P\}\). Let \(\mathcal D\) be the **ordered** set of all distinct vertex pairs \((p,q)\) with \(\|q-p\|=D\). In particular, both \((p,q)\) and \((q,p)\) are counted.

For each \((p,q)\in\mathcal D\) write \(e=(q-p)/D\). Triangulate the full-dimensional cones \(C_p,C_q\) into finitely many full-dimensional simplicial cones with disjoint interiors; the triangulations may be chosen independently for each pair. Fix one piece at \(p\) with linearly independent inward rays \(u_1,\ldots,u_d\), and one at \(q\) with inward rays \(v_1,\ldots,v_d\). The numbers
\[
\alpha_i=e\cdot u_i>0,\qquad \beta_i=-e\cdot v_i>0 \tag{4}
\]
are strictly positive (proved below). Let \(\Pi z=z-(e\cdot z)e\), and define the \(2d\) transverse vectors
\[
 c_i=\Pi(-u_i/\alpha_i),\qquad
 c_{d+i}=\Pi(v_i/\beta_i)\quad(1\le i\le d). \tag{5}
\]
For these two pieces set
\[
J=\frac{|\det(u_1,\ldots,u_d)\det(v_1,\ldots,v_d)|}
{\prod_{i=1}^d\alpha_i\beta_i},\qquad
Q=\left\|\sum_{j=1}^{2d}c_j\right\|^2+
\sum_{j=1}^{2d}\|c_j\|^2. \tag{6}
\]
All values are independent of positive rescaling of the rays. If the inner summation is over all ordered pairs of simplicial pieces for \((p,q)\), then
\[
\boxed{\quad A_P=\frac{1}{V^2(2d)!}
\sum_{(p,q)\in\mathcal D}\sum_{\rm pieces}J,\qquad
B_P=\frac{1}{2DV^2(2d+1)!}
\sum_{(p,q)\in\mathcal D}\sum_{\rm pieces}JQ.\quad}\tag{7}
\]
Thus the formulas are finite and algorithmic for any vertex/facet representation allowing tangent-cone triangulation. Formula (7), not a claim of a triangulation-free symbolic radical formula, defines the coefficients.

## Proof
**1. Diameter pairs are isolated vertex pairs.** For a fixed \(q\in P\), a maximizer of \(p\mapsto\|q-p\|\) cannot be in a positive-dimensional face's relative interior: the squared norm is strictly convex on any nonconstant line segment. Applying this to both coordinates shows that every diameter pair consists of vertices. There are finitely many. The complement of small, pairwise disjoint neighborhoods of these ordered pairs in \(P\times P\) has distance strictly below \(D\), by compactness.

For a nonzero tangent-cone direction \(u\in C_p\), the point \(p+tu\) lies in \(P\) for sufficiently small \(t>0\). Since \((p,q)\) is diametral,
\[
\|q-p-tu\|^2=D^2-2Dt(e\cdot u)+t^2\|u\|^2\le D^2.
\]
The inequality forces \(e\cdot u>0\), even if \(u\) is on the cone boundary; otherwise its positive quadratic term gives a contradiction. Similarly \(-e\cdot v>0\) for every nonzero \(v\in C_q\). Compactness on the unit-sphere cross sections supplies uniform positive angular margins. This proves (4).

**2. Local simplex coordinates.** A polytope agrees, sufficiently close to any vertex \(p\), with \(p+C_p\). For the chosen cone pieces use nonnegative parameters \(t_1,\dots,t_{2d}\) and the representation
\[
 X=p+\sum_{i=1}^d t_i u_i/\alpha_i,
\qquad Y=q+\sum_{i=1}^d t_{d+i}v_i/\beta_i.
\]
Its \(2d\)-dimensional Jacobian is exactly \(J\). Put \(m=2d\), \(s=\sum_{j=1}^{m}t_j\) and \(w=\sum_{j=1}^{m}t_jc_j\). Then the **exact**, not linearized, distance identity is
\[
 \|Y-X\|=\sqrt{(D-s)^2+\|w\|^2}.\tag{8}
\]
For small \(t\), the distance deficit is \(s+O(s^2)\), uniformly over the simplex of parameter ratios. Therefore \(\|Y-X\|>D-\varepsilon\) entails \(s=O(\varepsilon)\). Consequently, for all sufficiently small \(\varepsilon\), only the specified local cone neighborhoods contribute; no global portions of the polytope are omitted.

**3. Uniform radial expansion.** Write \(t_j=sz_j\) with \(z_j\ge0\), \(\sum_jz_j=1\), and \(c(z)=\sum_jz_jc_j\). On the fixed compact standard simplex \(\Delta_{m-1}\), the positive boundary of the near-diameter region is the unique small solution of
\[
 (D-s)^2+s^2\|c(z)\|^2=(D-\varepsilon)^2.
\]
The implicit-function theorem (uniformly in the compact \(z\)-simplex) gives
\[
 s_\varepsilon(z)=\varepsilon+
 \frac{\varepsilon^2}{2D}\|c(z)\|^2+O_P(\varepsilon^3).\tag{9}
\]
The map \((s,z)\mapsto(t_1,\ldots,t_m)\) has Jacobian \(s^{m-1}\). Hence, by integrating (9), the parameter volume is
\[
\int_{\Delta_{m-1}}\frac{s_\varepsilon(z)^m}{m}\,dz
=\frac{\varepsilon^m}{m!}
+\frac{\varepsilon^{m+1}}{2D}
\int_{\Delta_{m-1}}\|c(z)\|^2\,dz
+O_P(\varepsilon^{m+2}).\tag{10}
\]
Dirichlet-simplex moments \(\int_\Delta z_i^2\,dz=2/(m+1)!\) and \(\int_\Delta z_iz_j\,dz=1/(m+1)!\) for \(i\ne j\) yield
\[
 \int_{\Delta_{m-1}}\|c(z)\|^2\,dz
=\frac{\|\sum_jc_j\|^2+\sum_j\|c_j\|^2}{(m+1)!}
=\frac Q{(m+1)!}.\tag{11}
\]
Multiply (10) by \(J/V^2\) and sum over the finitely many ordered diametral vertex pairs and cone pieces to obtain (1) and (7), with the claimed \(O_P(\varepsilon^{m+2})\) remainder. The coefficients do not depend on triangulations because they integrate intrinsic volume contributions over a partition of each tangent cone. The coefficient \(A_P\) is positive. Since \(d\ge2\), a full-dimensional cone has at least one nonzero transverse \(c_j\), making each \(Q>0\) and hence \(B_P>0\).

**4. Orthotopes.** Each of the \(2^d\) ordered diagonal vertex pairs has one simplicial cone piece at each endpoint. In coordinates pointing from the first corner to its opposite, both sets of inward ray generators have Euclidean unit coordinate directions with normalized axial slopes \(a_i/D\). Thus every ordered pair contributes
\[
 J=\frac{D^{2d}}{V^2},\qquad
 Q=6D^2\sum_{i=1}^{d}a_i^{-2}-4d^2-2d.\tag{12}
\]
Substitution into (7) gives (2). For fixed \(V\), arithmetic-geometric mean gives \(D^2=\sum_i a_i^2\ge dV^{2/d}\), with equality if and only if all lengths are equal. Applying it to \(2^dD^{2d}/((2d)!V^4)\) yields (3) and its strict equality characterization.

## Verification
The file `CHECKER.py` is a standalone reproducibility script (Python 3 with `mpmath`). It independently integrates the exact two-point difference-coordinate density of four rectangles by one-dimensional high-precision quadrature; it compares the numerically extracted second-order coefficient with (2) at three successively smaller deficits for each shape. It also checks the coefficient algebra and the strict fixed-volume inequality for sample boxes in dimensions two through four. It prints `DIAMETER_TAIL_CHECK_OK` upon success. Such numerical tests corroborate (2) but do not replace the all-polytopes analytical argument in Steps 1–3.

As additional hand checks, for the unit square formula (2) predicts \(A_P=2/3\) and \(B_P/A_P=\sqrt2/5\), while the unit cube has \(A_P=3/10\) and \(B_P/A_P=2\sqrt3/7\). Both are consistent with the independent difference-coordinate derivation. For the equilateral unit-edge triangle, (7) gives \(A_P=4\) and \(B_P/A_P=3/5\), a nonorthogonal-cone check.

## Relationship to prior work
Sinan Wang, *A Brunn–Minkowski Theory for the Distribution of Random Pairs of Points in Convex Bodies* (first arXiv posting 2026-10-01, arXiv:2610.01916), introduces the normalized pair-distance distribution and proves Brunn–Minkowski and rigidity theorems. Its saturation observation establishes that the cumulative distribution equals one beyond the diameter, but it does not supply the two coefficients at this upper endpoint.

Wei Lao, *Some Weak Limit Laws for the Diameter of Random Point Sets in Bounded Regions* (2010), Chapter 6, obtains maximum-sample diameter limit laws for cubes and certain polygons from projected extreme-point behavior. In particular, the **leading cube-order behavior is a known special-case phenomenon**, not claimed as new. Those theorems do not imply the correction in (7): the transverse quadratic deviation \(\|w\|^2\) omitted by the linearized projected-distance limit law is exactly what produces \(B_P\). Mayer and Molchanov, *A Limit Theorem for the Maximal Interpoint Distance of a Random Sample in the Unit Ball* (arXiv:math/0605289), derive endpoint tails and sampling limit laws for smooth balls rather than the present all-polytopal two-term vertex-cone expression.

The geometric content asserted here is the finite, triangulation-independent all-polytope coefficient formula for the **first two** upper-tail orders, together with the strict fixed-volume orthotope minimizer for the leading order. This does not assert historical priority over all unpublished or unindexed stereological calculations.

## Limitations
The limit takes \(\varepsilon\downarrow0\) for a fixed polytope. The constant in the remainder may deteriorate under degenerating families, so no uniform expansion over all polytopes is asserted. The theorem concerns interior-uniform samples, not boundary-uniform sampling, random chords, a sample maximum of three or more points, or smooth convex bodies. The orthotope inequality compares leading coefficients at **each body's own diameter**, not pointwise probabilities at a common radius. Numerical verification is finite; priority relative to older unindexed integral-geometric literature remains a risk. Independent external audit has not been conducted.

## References
1. S. Wang, *A Brunn–Minkowski Theory for the Distribution of Random Pairs of Points in Convex Bodies*, arXiv:2610.01916 (first posted 2026-10-01), https://arxiv.org/abs/2610.01916.
2. W. Lao, *Some Weak Limit Laws for the Diameter of Random Point Sets in Bounded Regions*, KIT Scientific Publishing, 2010, Chapter 6, https://publikationen.bibliothek.kit.edu/1000019800/105664897.
3. M. Mayer and I. Molchanov, *A Limit Theorem for the Maximal Interpoint Distance of a Random Sample in the Unit Ball*, arXiv:math/0605289, 2006, https://arxiv.org/abs/math/0605289.
