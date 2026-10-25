# The exact short Euclidean surface-pair law and its dihedral bending coefficient

## Finding

Let \(P\subset\mathbb R^3\) be any nondegenerate compact convex polyhedron, with surface area \(A>0\), edge set \(E\), edge lengths \(L_e\), and interior dihedral angles \(0<\alpha_e<\pi\). If \(X,Y\) are independent uniformly surface-area-sampled points, and \(D=\|X-Y\|_2\) is their **ambient Euclidean distance**, there exist \(r_0(P)>0\) and a finite real constant \(C_4(P)\) such that **exactly**, for every \(0\le r<r_0(P)\),

\[
\Pr(D\le r)=\frac{\pi}{A}r^2+\frac{4}{3A^2}\sum_{e\in E}L_e\left(\frac{\pi-\alpha_e}{\sin\alpha_e}-1\right)r^3+C_4(P)r^4.
\]

The coefficient of \(r^3\) is strictly positive. Writing the exterior bend as \(\delta_e=\pi-\alpha_e\in(0,\pi)\), this coefficient satisfies the **sharp universal hinge stability bound**

\[
\frac{4}{3A^2}\sum_e L_e\left(\frac{\delta_e}{\sin\delta_e}-1\right)\ >\ \frac{2}{9A^2}\sum_e L_e\delta_e^2,
\]

where the lower multiplicative constant \(2/9\) is optimal in the small-bend limit. The first correction to the flat-surface \(r^2\) law therefore detects total edge-weighted bending; unlike asymptotic statements, all terms beyond degree four vanish on a sufficiently small interval.

## Assumptions and scope

The word *facet* means a maximal planar face, so distinct facets cannot lie in the same supporting plane. Surface sampling uses normalized two-dimensional Hausdorff measure \(d\sigma/A\). Each edge is incident to exactly two facets; the interior dihedral angle is measured between the inward transverse tangent rays, not between outward normals. The result concerns the extrinsic straight-line distance \(\|X-Y\|_2\), **not** shortest-path distance on the surface. Constants depend on the fixed polyhedron; no uniform lower bound for \(r_0\) over varying shapes is asserted.

## Proof

**1. Exact finite-degree locality.** Put
\[
I(r)=\int_{\partial P}\int_{\partial P}\mathbf1_{\{\|x-y\|_2\le r\}}\,d\sigma_y\,d\sigma_x.
\]
Split the ordered integral into pairs of facets \(F,G\). If \(F=G\), translating the planar polygon gives
\[
I_{F,F}(r)=\int_{\|z\|\le r}|F\cap(F+z)|\,dz.
\]
The intersection of two polygons defined by finitely many linear inequalities has vertices that are affine functions of \(z\) on each cell of a finite polyhedral subdivision of translation space. Consequently its area is polynomial of degree at most two on each cell. For \(\|z\|\) sufficiently small, the cells meeting zero are conical angular sectors (no nonzero affine breakpoint meets the disk). Integration over the disk therefore makes \(I_{F,F}\) an **exact polynomial in \(r\) of degree at most four**, beginning at degree two.

For \(F\ne G\), their supporting planes are distinct. If they are parallel, the two faces are positively separated and contribute zero for small \(r\). Otherwise use the linear map \(T:(x,y)\mapsto x-y\) from the four-dimensional product of the facet planes onto \(\mathbb R^3\); its rank is three and its fibers are affine lines. The linear coarea formula expresses \(I_{F,G}(r)\) as a constant multiple of \(\int_{\|z\|\le r}\ell_{F,G}(z)\,dz\), where \(\ell_{F,G}(z)\) is the length of a line segment defined by finitely many affine inequalities. Its two endpoints are maxima/minima of finitely many affine functions of \(z\) in a polyhedral feasibility region, and \(\ell_{F,G}\) is thus continuous piecewise affine there. In a sufficiently small neighborhood of zero the polyhedral cells form cones with apex zero, so the disk integral is an exact polynomial consisting only of degrees three and four. If \(F\cap G=\varnothing\), positive distance eliminates it for small \(r\). Finitely many facet pairs allow a single common \(r_0>0\). Hence \(I(r)=b_2r^2+b_3r^3+b_4r^4\) exactly.

**2. Same-facet coefficient.** For a planar convex polygon \(F\), the linear directional loss of its covariogram is \(\sum_{e\subset\partial F}L_e(z\cdot n_e)_+\), with \(n_e\) a unit outward edge normal. Integrating this first-order term over \(\|z\|\le r\) gives \(\frac{2}{3}\operatorname{perim}(F)r^3\), since \(\int_0^{2\pi}(\cos\theta)_+d\theta=2\). Thus
\[
I_{F,F}(r)=\pi|F|r^2-\frac23\operatorname{perim}(F)r^3+O(r^4).
\]
Summing over facets gives \(b_2=\pi A\) and a same-facet contribution \(-\frac43\sum_e L_e\) to \(b_3\), because each edge belongs to two facet perimeters.

**3. Cross-facet hinge coefficient.** Two distinct facets can give order \(r^3\) only if they share a full edge; if they meet just at a vertex, their ordered surface-pair measure is \(O(r^4)\), by homogeneity of the two local planar cones. Near an interior point of an edge of length \(L\), choose longitudinal coordinates \(u,v\) and inward transverse coordinates \(s,t\ge0\) on the two faces. Their squared ambient distance is
\[
(u-v)^2+s^2+t^2-2st\cos\alpha,
\]
where \(\alpha\) is the interior dihedral angle. After rescaling and ignoring an endpoint set contributing only \(O(r^4)\), one ordered pair contributes \(Lr^3K(\alpha)\), with
\[
K(\alpha)=\int_{s,t\ge0}\int_{w\in\mathbb R}\mathbf1_{\{w^2+s^2+t^2-2st\cos\alpha\le1\}}\,dw\,ds\,dt.
\]
The linear map \((s,t)\mapsto s\mathbf e_1-t\mathbf e_2\) has absolute Jacobian \(\sin\alpha\) and carries the nonnegative quadrant onto a wedge of aperture \(\pi-\alpha\). Polar integration yields
\[
K(\alpha)=\frac{\pi-\alpha}{\sin\alpha}\int_0^1 2\sqrt{1-\rho^2}\,\rho\,d\rho
=\frac{2(\pi-\alpha)}{3\sin\alpha}.
\]
The two ordered facet pairs across the edge therefore contribute \(\frac{4}{3}L(\pi-\alpha)/\sin\alpha\) to \(b_3\). Combining with step 2 and dividing by \(A^2\) proves the exact polynomial and stated cubic coefficient.

**4. Strict positivity and optimal quadratic bend bound.** For \(0<\delta<\pi\), \(\sin\delta<\delta\), so every edge term is positive. For the sharp lower bound, let \(h(\delta)=(1+\delta^2/6)\sin\delta-\delta\). Direct differentiation gives
\[
h''(\delta)=\frac23(\delta\cos\delta-\sin\delta)-\frac{\delta^2}{6}\sin\delta<0
\quad(0<\delta<\pi),
\]
because \(\delta\cos\delta-\sin\delta<0\) follows by differentiating it from zero. Since \(h(0)=h'(0)=0\), \(h(\delta)<0\), equivalently \(\delta/\sin\delta>1+\delta^2/6\). Multiplication by \(4/3\) gives the claimed coefficient \(2/9\). Finally \(\delta/\sin\delta-1=\delta^2/6+O(\delta^4)\), making \(2/9\) sharp.

## Verification

The standalone file `check_polyhedral_surface_euclidean.py` reproduces the independent numeric cross-facet integral in original transverse coordinates, compares same-face and cross-face pair integrals against exact unit-cube formulas, and directly samples pairs of points on cube faces. It checks four dihedral angles, three cube radii and the sharp small-bend coefficient. All checks passed. These finite calculations **corroborate but do not prove** the arbitrary-polyhedron theorem; the finite-face and coarea argument above supplies that proof.

As a known benchmark, for the unit cube \(P=[0,1]^3\) with \(A=6\), the formula specializes, on \(0\le r<1\), to
\[
\Pr(D\le r)=\frac{\pi}{6}r^2+\frac{2\pi-4}{9}r^3+\frac{1-\pi}{12}r^4.
\]
This benchmark is not claimed as original.

## Relationship to prior work

Mathai, Moschopoulos and Pederzoli (1999) discuss cube distances including adjacent-face pairs; this **covers the cube special case** and is credited, not newly asserted. Tong, Ahmadi and Pan (2013), and Tong and Pan (2016), study distances between random points in **planar** triangles and polygons, including adjacent coplanar triangles. Their setup does not yield the three-dimensional dihedral hinge factor. Ma and Torquato (2018) derive the leading small-separation divergence of surface correlation functions for **everywhere-differentiable** interfaces and state that higher-order terms are beyond their analysis; their result does not imply an edge-angle cubic correction for a nonsmooth polyhedral surface. The present claim is the exact short-radius general convex-polyhedron law, not novelty for the leading term or any previously tabulated single polyhedron.

A separate intrinsic-geodesic metric on polyhedral surfaces has a short-distance law determined by cone angles; that metric is different and does not imply the ambient Euclidean formula. Searches of public mathematical-record claims and the accessible related geometrical literature did not reveal this complete general statement. Historical priority is not definitively certified; unexamined specialized stereology literature remains a risk.

## Limitations

The formula holds for each fixed nondegenerate convex polyhedron in three-dimensional Euclidean space, at a positive but shape-dependent radius threshold. It does not provide a general closed form for \(C_4(P)\), nor an all-radius distance distribution. The stability inequality is strict for an actual nonflat polyhedron, but its universal coefficient is only **asymptotically** sharp as bends tend to zero. The computational tests address only finitely many cases. No independent mathematical audit has been performed.

## References

- Mathai, A. M., Moschopoulos, P. G., and Pederzoli, G. (1999), *Distance between random points in a cube*, Statistica **59**, 61–81, DOI: 10.6092/issn.1973-2201/1104. Journal record and abstract inspected; full article was unavailable.
- Tong, F., Ahmadi, M., and Pan, J. (2013), *Random Distances Associated with Arbitrary Triangles*, arXiv:1312.2498, first submitted 29 November 2013. Primary abstract and introduction inspected.
- Tong, F., and Pan, J. (2016), *Random Distances Associated with Arbitrary Polygons: An Algorithmic Approach between Two Random Points*, arXiv:1602.03407, first submitted 21 January 2016. Accessible primary full text, especially planar decomposition sections, inspected.
- Ma, Z., and Torquato, S. (2018), *Precise algorithms to compute surface correlation functions of two-phase heterogeneous media and their applications*, Physical Review E **98**, 013307, DOI: 10.1103/PhysRevE.98.013307. Accessible complete author manuscript inspected, especially Sec. III and Appendix A.
