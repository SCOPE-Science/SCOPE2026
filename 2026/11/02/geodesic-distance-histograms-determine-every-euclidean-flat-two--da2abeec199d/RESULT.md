# Geodesic distance histograms determine every Euclidean flat two-torus

## Finding
Let \(T=\mathbb R^2/\Lambda\) be any Euclidean flat two-torus, with its induced intrinsic geodesic distance \(d_T\) and normalized area measure. Choose \(X,Y\) independently from this measure and put \(D=d_T(X,Y)\). **The distribution of the single unoriented, unlabeled distance \(D\) determines \(\Lambda\) up to an orthogonal transformation, hence determines \(T\) up to isometry, including its absolute scale.**

Here is an explicit distribution and reconstruction. Let \(V\) be the Dirichlet–Voronoi polygon of \(\Lambda\) centered at the origin, let \(A=\operatorname{area}(V)\), and let \(R=\max_{x\in V}\|x\|\). The polygon has either two or three pairs of opposite facets. Denote by \(d_1,\ldots,d_m\), where \(m\in\{2,3\}\), their distances from the origin, listing each opposite pair once and retaining repetitions. Define
\[
C(t;d)=\begin{cases}0,&0\le t\le d,\\ t^2\arccos(d/t)-d\sqrt{t^2-d^2},&t>d.\end{cases}
\]
Then the complete cumulative distribution function is
\[
F_D(t)=\begin{cases}0,&t<0,\\
\displaystyle\frac{\pi t^2-2\sum_{i=1}^{m}C(t;d_i)}{A},&0\le t<R,\\1,&t\ge R.\end{cases}
\]
In particular, for \(0<t<R\) different from the finitely many \(d_i\),
\[
\frac{A F_D'(t)}{t}=2\pi-4\sum_{i:\,d_i<t}\arccos(d_i/t).
\]
Every distinct \(d_i\) is a nonanalytic onset of order \(3/2\):
\[
C(d+h;d)=\frac43\sqrt{2d}\,h^{3/2}+O_d(h^{5/2})\quad(h\downarrow0).
\]
At a repeated distance the coefficient is multiplied by its multiplicity. Thus the full law determines \(A\) from \(\lim_{t\downarrow0}F_D(t)/t^2=\pi/A\), determines \(R\) as its support endpoint, and determines the entire multiset \(\{d_1,\ldots,d_m\}\) (including multiplicities) from the strictly positive cap-onset coefficients.

If \(m=2\), then \(\Lambda\) has an orthogonal basis of lengths \(2d_1,2d_2\). If \(m=3\), the three numbers \(2d_1,2d_2,2d_3\) are the side lengths of a Euclidean Delaunay triangle whose two edge vectors from any vertex form a basis of \(\Lambda\). Their unordered values fix that triangle up to a Euclidean isometry, hence fix the lattice. This is a constructive inverse, not just an existence statement. Square, rectangular, hexagonal, rhombic and unequal generic lattices are included, with no genericity restriction.

## Assumptions and scope
A lattice is a rank-two discrete subgroup of \(\mathbb R^2\). The torus carries the quotient *intrinsic* Euclidean metric, not any extrinsic torus-of-revolution metric. The points are independent and Haar-uniform; no labels, directions, coordinates, marked lattice basis, area or scale are supplied with the distance observations. The theorem concerns an exact population probability law. A simultaneous overall rescaling of the metric rescales the observed distances and is therefore detectable.

For a normalized proof, rotate and rescale so that a Gauss-reduced lattice basis is
\[
e_1=(1,0),\qquad e_2=(a,b),\qquad 0\le a\le\tfrac12,\quad a^2+b^2\ge1,\quad b>0.
\]
Restoring the scale multiplies every length and radius by \(\|e_1\|\), and area by its square. If \(a=0\) the Voronoi polygon is a rectangle; otherwise it is a genuine hexagon.

## Proof
**1. Quotient distances are Voronoi radii.** The difference \(Y-X\) is Haar-uniform on \(T\). Its unique representative in the interior of the centered Dirichlet–Voronoi cell \(V\) is area-uniform there, and the torus geodesic distance is exactly its Euclidean norm. Therefore
\[
F_D(t)=\frac{\operatorname{area}(V\cap B(0,t))}{A}.
\]
Cell boundaries have zero area and do not change the law.

**2. The planar lattice cell is cyclic.** For \(0<a\le1/2\), Gauss reduction gives the three Voronoi-relevant pairs \(\pm e_1\), \(\pm e_2\), \(\pm(e_2-e_1)\); the cell consists exactly of their six perpendicular-bisector halfplanes. Its six vertices, in opposite pairs, can be taken as
\[
(\tfrac12,\alpha),\quad(a-\tfrac12,\beta),\quad(-\tfrac12,\alpha),
\quad\text{and their negatives},
\]
where
\[
\alpha=\frac{b^2+a^2-a}{2b},\qquad
\beta=\frac{b^2-a^2+a}{2b}.
\]
Direct expansion gives \((1/2)^2+\alpha^2=(a-1/2)^2+\beta^2\). All six vertices therefore lie on the circle centered at the origin of radius \(R=\sqrt{1/4+\alpha^2}\). The three facet distances are
\[
d_1=\tfrac12,\quad d_2=\tfrac12\sqrt{a^2+b^2},\quad
 d_3=\tfrac12\sqrt{(a-1)^2+b^2}.
\]
They all lie strictly below \(R\), because every facet is a nondegenerate chord of that circle. For \(a=0\), the cell is the rectangle with side lengths \(1,b\); it has two facet-pair distances \(1/2,b/2\) and its four vertices share radius \(\sqrt{1+b^2}/2\). These facts also follow from the standard planar Dirichlet-cell calculation in Glorieux–Yarmola, Section 3; the equal-radius identity and its consequences are checked here directly.

**3. Exact circular-cap decomposition.** A convex polygon inscribed in a circle centered at an interior point partitions that disk into the polygon plus one exterior circular segment beyond each facet, with disjoint segment interiors. Every facet here is a chord of the same \(R\)-circle, and there are two facets at each \(d_i\). For each \(0\le t\le R\), intersect this disjoint decomposition with \(B(0,t)\). The intersection of an exterior segment with that smaller disk is the usual circular cap of area \(C(t;d_i)\). Consequently
\[
\operatorname{area}(V\cap B(0,t))=\pi t^2-2\sum_i C(t;d_i).
\]
For \(t\ge R\) the cell is already inside the disk. Differentiating the cap formula yields \(\partial_t C(t;d)=2t\arccos(d/t)\) for \(t>d\). A local segment-height integration, \(2\int_0^h\sqrt{2d(h-s)+O(h^2)}\,ds\), gives its displayed positive \(3/2\)-order onset.

**4. All singular radii and multiplicities are observable.** For \(0<t<\min_i d_i\), \(F_D(t)=\pi t^2/A\), so \(A\) is determined. For \(t<R\), \(H(t)=(\pi t^2-AF_D(t))/2=\sum_iC(t;d_i)\). Each summand is identically zero to the left of its threshold, real-analytic to its right, and has a nonzero \(3/2\)-term there. At a new threshold all earlier summands are analytic, and the new singular terms have the same positive sign; hence cancellation is impossible. This identifies every distinct threshold and its integer multiplicity. Since each facet has positive length, \(d_i<R\), so the separate support endpoint \(R\) cannot disguise a threshold.

**5. The inverse is a lattice, not merely a polygon.** If the cell has four sides, it is the Voronoi rectangle of an orthogonal lattice, generated by vectors of norms \(2d_1,2d_2\). If it has six sides, the three relevant lattice vectors \(e_1,e_2,e_2-e_1\) are the three edge directions of the nondegenerate Euclidean triangle with vertices \(0,e_1,e_2\). Knowing the unordered three side lengths uniquely determines that triangle up to congruence; choosing any vertex as origin, its two incident edge vectors generate the same lattice as \(e_1,e_2\). Thus in either case the recovered data uniquely determine the lattice modulo Euclidean isometry. Because the facet-pair count and repetitions were recovered, this also covers every symmetry and degeneracy regime. \(\square\)

## Verification
The accompanying standalone `verify_torus.py` rederives the circular-cap integral independently by angular quadrature of the halfplane radial function for seven planar lattice configurations. It checks the all-vertices-on-one-circle identity, normalization at the covering radius, rectangular area recovery, Heron-area reconstruction of hexagonal cells, exact rational Gram identities for three nonrectangular lattices, and the \(4\sqrt{2d}/3\) cap coefficient at high precision. It reports `ALL_CHECKS_PASSED` on execution. These tests supplement but do not replace the complete analytic proof above.

Reproduce with `python verify_torus.py`; it uses Python's standard library and `mpmath` for the separate high-precision onset cross-check. The main theorem does not depend on numerical or symbolic certification.

## Relationship to prior work
Glorieux and Yarmola, *Random triangles on flat tori* (arXiv:2003.08190, first public 2020-03-18), explicitly compute planar flat-torus Dirichlet-cell vertices and a different random-triangle homotopy probability. Their Section 3 supplies a useful known Voronoi normal form, but their result neither gives the intrinsic **pair-distance** law nor proves its complete unlabeled inverse rigidity.

Kwakkel, Martens and Peixoto, *Focal Rigidity of Flat Tori* (arXiv:1104.5541), prove rigidity from much richer focal-decomposition information and discuss radial Brillouin/focal spectra. Focal equivalence and the infinite spectral data discussed there are not the scalar two-point distance distribution used here, and their theorem does not entail its injectivity.

Pure, Durrani, Tong and Pan, *Distance Distribution Between Two Random Nodes in Arbitrary Polygons* (arXiv:1903.07757; later titled *Distance distribution between two random points in arbitrary polygons*), give a general **Euclidean** distance law between two independent points in planar polygons. This is a different probability observable from the geodesic difference on a quotient torus (which is one uniform point in a Voronoi cell). Their full accessible preprint does not state this lattice-reconstruction theorem. General computational ability to calculate a forward law is not an inverse-rigidity implication.

The 2026 study *Distance Energies and Negative Type of Flat Tori* (arXiv:2609.05622) gives an independent general Voronoi/Haar integration normalization and studies Fourier signatures of cut loci and energy optimizers; it does not claim reconstruction from the scalar Haar two-point distance distribution.

The special facts that planar lattice Voronoi cells have four or six sides and that a triangle is determined by its three edge lengths are classical; novelty is not claimed for either component alone.

## Limitations
Only Euclidean flat **two-dimensional** tori are covered; there is no claim for higher-dimensional lattices, nonflat metrics or extrinsic distances. The result is exact population identifiability and supplies no finite-sample statistical estimator, noise robustness theorem, or uniform conditioning near colliding facet radii. A distinct older distance-law or inverse-rigidity formulation might exist despite the described searches; absolute historical priority has not been established.

## References
1. O. Glorieux and A. Yarmola, *Random triangles on flat tori*, arXiv:2003.08190 (first submitted 2020-03-18), published in *Rocky Mountain J. Math.* 52 (2022), 1345–1354. https://arxiv.org/abs/2003.08190
2. F. Kwakkel, M. Martens and M. Peixoto, *Focal Rigidity of Flat Tori*, arXiv:1104.5541, https://arxiv.org/html/1104.5541v2
3. R. Pure, S. Durrani, F. Tong and J. Pan, *Distance Distribution Between Two Random Nodes in Arbitrary Polygons*, arXiv:1903.07757, https://arxiv.org/html/1903.07757v1; journal version *Math. Methods Appl. Sci.* 45 (2022), 2760–2775.

4. *Distance Energies and Negative Type of Flat Tori*, arXiv:2609.05622 (2026), https://arxiv.org/abs/2609.05622.
