# Sharp affine least-squares stability on regular polygons and its disk-limit defect

## Finding
Let \(P_n\subset\mathbb R^2\), \(n\ge3\), be the convex hull of the \(n\) vertices \(v_j=(\cos(2\pi j/n),\sin(2\pi j/n))\). Equip \(P_n\) with normalized area measure and let \(\mathcal P_n\) be the orthogonal projection in \(L^2(P_n)\) onto the affine functions \(\operatorname{span}\{1,x_1,x_2\}\). The sharp \(L^1\) and \(L^\infty\) operator norms agree and have the following finite, exact trigonometric prescription, requiring only one clipping line and polygon area/first-moment sums.

Set \(\vartheta=2\pi/n\), \(c=12/(2+\cos\vartheta)\), \(h=-1/c\), \(k=\lfloor\arccos(h)/\vartheta\rfloor\), and
\[
q=\frac{h-\cos(k\vartheta)}{\cos((k+1)\vartheta)-\cos(k\vartheta)},\qquad y_*=(1-q)\sin(k\vartheta)+q\sin((k+1)\vartheta).
\]
Form the counterclockwise polygon \(W\) with ordered vertices
\[
(h,y_*),\ v_{k+1},v_{k+2},\ldots,v_{n-k-1},\ (h,-y_*).
\]
For its cyclic vertices \(w_i=(a_i,b_i)\), set
\[
S_i=a_i b_{i+1}-a_{i+1}b_i,\qquad C=\frac12\sum_i S_i,\qquad J=\frac16\sum_i(a_i+a_{i+1})S_i.
\]
With \(A=n\sin(\vartheta)/2\), the exact sharp norm is
\[
\boxed{\ \|\mathcal P_n\|_{L^1\to L^1}=\|\mathcal P_n\|_{L^\infty\to L^\infty}=1+\frac{2(-C-cJ)}{A}.\ }
\]
The formula applies also if the clipping line passes through a vertex (zero-length boundary pieces are interpreted normally). It gives \(19/8\) for the triangle, \(233/108\) for the square, and \(361/180\) for the regular hexagon. The earlier triangle and square cases are background benchmarks, not claimed as original discoveries.

Define
\[
\Lambda_\circ=1-\frac2\pi\arccos\!\left(\frac14\right)+\frac{11\sqrt{15}}{8\pi}.
\]
Then the sharp norms obey the precise polygon-to-disk law
\[
\boxed{\ \|\mathcal P_n\|_{L^\infty\to L^\infty}=\Lambda_\circ+\frac{5\pi\sqrt{15}}{12n^2}+o(n^{-2}),\qquad n\to\infty.\ }
\]
In particular the first nonzero correction is positive, explicitly quantifying the extra worst-case amplification due to polygonal approximation of the disk.

## Assumptions and scope
All polygons are planar, filled, regular, inscribed in the unit circle, and equipped with normalized two-dimensional Lebesgue area. The projection is the **linear** orthogonal least-squares projection onto the full affine polynomial space, not a nonlinear metric projection onto a convex set, nor a projection on boundary arclength. Operator norms use the usual measure-induced \(L^1\) and \(L^\infty\) norms. The exact prescription holds for every integer \(n\ge3\); the novel all-polygon statement is of particular interest for \(n\ge5\), beyond previously known simplex and parallelogram special cases. The asymptotic is along all integers, without a subsequence condition.

## Proof
**Step 1 (normalization).** The regular polygon has zero centroid. Triangulating it from the origin into the \(n\) equal-area sectors with vertices \(0,v_j,v_{j+1}\) gives
\[
\mathbb E|X|^2=\frac{2+\cos\vartheta}{6},\qquad
\mathbb E X_1^2=\mathbb E X_2^2=\frac{2+\cos\vartheta}{12},\quad
\mathbb E X_1X_2=0.
\]
The last two identities follow from rotational symmetry by angle \(2\pi/n\), which is nontrivial for every \(n\ge3\). Thus the reproducing kernel of the affine space, for normalized area, is exactly
\[
K(x,y)=1+c\,x\mathbin\cdot y,\qquad c=\frac{12}{2+\cos\vartheta}.
\]

**Step 2 (locating the sharp row).** For fixed \(x\in P_n\), define \(F(x)=\int_{P_n}|K(x,y)|\,d\mu(y)\). It is convex as an integral of absolute values of affine functions of \(x\). Since every \(x\in P_n\) is a convex combination of polygon vertices, \(F(x)\le\max_j F(v_j)\). Rotational symmetry makes all vertex values equal. The sign-valued input \(f(y)=\operatorname{sgn}(K(v_0,y))\) attains this upper bound at \(v_0=(1,0)\). Kernel symmetry and duality give the identical sharp \(L^1\) norm.

**Step 3 (exact clipping prescription).** The row at \(v_0\) is \(K(v_0,y)=1+cy_1\). Its negative region is exactly the polygonal cap \(W=P_n\cap\{y_1<h\}\), \(h=-1/c\). On the upper half of the boundary, \(\cos(j\vartheta)\) decreases until angle \(\pi\), so its crossing with \(y_1=h\) is uniquely located on the edge \(v_kv_{k+1}\) with the displayed \(k,q,y_*\). Reflection across the horizontal axis gives the second crossing. The standard shoelace area and polygon first-moment identities show that \(\operatorname{area}(W)=C\) and \(\int_W y_1\,dy=J\). Since \(\int_{P_n}K(v_0,y)\,d\mu(y)=1\), the absolute kernel row integral is precisely \(1+2(-C-cJ)/A\). This proves the finite formula without numerical quadrature.

**Step 4 (disk limit and the sharp correction).** Put \(\delta=\pi/n\). The regular polygon's radial boundary, on each angular cell centered at an outward edge normal, is \(r_n(\phi)=\cos\delta/\cos s\) for \(|s|\le\delta\), hence uniformly
\[
r_n(\phi)=1+\frac{s^2-\delta^2}{2}+O(\delta^4),\quad
A_n=\pi\left(1-\frac{2\delta^2}{3}+O(\delta^4)\right),\quad
c_n=4+\frac{8\delta^2}{3}+O(\delta^4).
\]
For any fixed Lipschitz periodic \(g\), averaging \(s^2\) on each angular cell and using a Riemann sum proves
\[
\int_0^{2\pi}(r_n(\phi)-1)g(\phi)\,d\phi
=-\frac{\delta^2}{3}\int_0^{2\pi}g(\phi)\,d\phi+o(\delta^2).
\]
The expansion of the absolute-value integral with respect to \(c\) is differentiable at \(c=4\), because its vanishing set has zero planar measure; the difference quotient is dominated by \(|y_1|\). The radial perturbation contributes the boundary integrand \(g(\phi)=|1+4\cos\phi|\), which is Lipschitz. Denote by \(\Lambda_{\rm disk}(c)\) the normalized disk integral \(\pi^{-1}\int_{|y|\le1}|1+cy_1|\,dy\). A direct integration of the circular segment \(y_1<-1/4\) yields
\[
\Lambda_{\rm disk}(4)=1-\frac2\pi\arccos\!\left(\frac14\right)+\frac{11\sqrt{15}}{8\pi},\qquad
\Lambda'_{\rm disk}(4)=\frac{5\sqrt{15}}{16\pi},
\]
and
\[
\int_0^{2\pi}|1+4\cos\phi|\,d\phi
=2\pi-4\arccos\!\left(\frac14\right)+4\sqrt{15}.
\]
Consequently the coefficient of \(\delta^2\) in the polygon norm is
\[
\frac23\Lambda_{\rm disk}(4)
+\frac83\Lambda'_{\rm disk}(4)
-\frac1{3\pi}\int_0^{2\pi}|1+4\cos\phi|\,d\phi
=\frac{5\sqrt{15}}{12\pi}.
\]
Substitution of \(\delta^2=\pi^2/n^2\) gives \(5\pi\sqrt{15}/12\) as claimed, with a rigorously controlled remainder \(o(n^{-2})\). No finite experiment is used to infer this limit.

## Verification
The standalone, standard-library-only `verify_polygon.py` independently clips convex polygons and computes their areas and first moments. It verifies by exact rational arithmetic the triangular, square, and hexagonal benchmarks \(19/8,233/108,361/180\) (after a harmless vertical rescaling to rational coordinates). It also compares the exact clipping expression against a separate triangle-based numerical quadrature for \(n=5,7,9,12\), and checks the predicted rescaled asymptotic coefficient for \(n=80,120,200,320,500\). All 15 groups of checks passed on the packaged source. The infinite-dimensional-index statement and its \(o(n^{-2})\) limit are analytical results, not certified by those finite tests.

## Relationship to prior work
Hangelbroek, Narcowich, Sun and Ward (arXiv:1005.2424, first public May 13, 2010), studied \(L^\infty\)-stability of \(L^2\) least-squares projectors generated by localized kernels on smooth manifolds; their Section 5 bounds a different class of approximation spaces and does not give the exact regular-polygon constants or the polygon-to-disk coefficient here. The general reproducing-kernel and convexity reductions are standard and are not claimed as new. Independent earlier exact calculations for affine least-squares projection on simplices, parallelepipeds, and balls also supply, respectively, the triangle, square, and limiting disk benchmarks. The contribution here is the full filled-polygon family and its explicitly evaluated sharp second-order geometric discrepancy. Defant and collaborators (2026, DOI 10.1112/jlms.70429) investigate polynomial projection constants on spheres rather than filled regular polygons; their scope is related but does not imply the present cap-moment formula.

## Limitations
The exact finite expression is an elementary **algorithmic** trigonometric formula involving one integer cutoff and polygon moments; it is not asserted to be a single rational-in-\(n\) expression. The expansion controls the first nonzero correction only; no monotonicity across successive \(n\), uniqueness of maximizing spatial positions, or optimality among arbitrary polygons is claimed. Numerical tables are supporting checks rather than infinite proofs. Bibliographic priority remains provisional, especially for older sources not found through available indexing. No independent audit is claimed.

## References
1. T. Hangelbroek, F. J. Narcowich, X. Sun and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L^\infty\)-norm of the \(L^2\)-projector*, arXiv:1005.2424 (first public 2010-05-13), Sections 1, 3, and 5. https://arxiv.org/abs/1005.2424
2. A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Minimal projections onto spaces of polynomials on real Euclidean spheres*, J. London Math. Soc. (2026), DOI:10.1112/jlms.70429; related spherical setting, not filled polygons. https://doi.org/10.1112/jlms.70429
