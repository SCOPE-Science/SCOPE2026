# Intrinsic-distance histograms determine every flat two-torus

## Finding
Let \(\Lambda\subset\mathbb R^2\) be any full-rank Euclidean lattice. Equip \(T_\Lambda=\mathbb R^2/\Lambda\) with its quotient intrinsic distance \(d_\Lambda\) and normalized Haar area. If \(X,Y\) are independent Haar-uniform points, let
\[
F_\Lambda(r)=\Pr\{d_\Lambda(X,Y)\le r\},\qquad r\ge0.
\]
**Inverse rigidity theorem.** The single scalar function \(F_\Lambda\) determines \(\Lambda\) up to a Euclidean isometry (including reflection), and hence determines the entire flat torus up to isometry. This includes both rectangular and nonrectangular lattices, all scales, and coincident facet distances.

A constructive inversion uses only the quadratic germ of \(F_\Lambda\) at zero and its finitely many square-root derivative singularities. Put
\[
A=\lim_{r\downarrow0}\frac{\pi r^2}{F_\Lambda(r)}.
\]
Let \(\mathscr D\) be the finite set of positive radii \(d\) at which the locally continuous derivative \(F_\Lambda'\) has a nonzero one-sided square-root jump, as characterized by
\[
\mathfrak m(d)=-\frac{A}{4\sqrt{2d}}\lim_{\varepsilon\downarrow0}
\frac{F_\Lambda'(d+\varepsilon)-F_\Lambda'(d-\varepsilon)}{\sqrt\varepsilon}>0.
\]
Then every \(\mathfrak m(d)\) is a positive integer, and the multiset containing \(d\) exactly \(\mathfrak m(d)\) times has either two or three entries. It consists **exactly** of the distances from the origin to one representative of each opposite pair of edges of the lattice Voronoi polygon.

If it has two entries \(a\le b\), the lattice has an orthogonal basis of lengths \(2a,2b\). If it has three entries \(a\le b\le c\), it has a basis \(u,v\) with
\[
|u|=2a,\qquad |v|=2b,\qquad u\cdot v=2(a^2+b^2-c^2)>0.
\]
This Gram matrix determines the lattice up to an orthogonal transformation. Equal entries and the square/hexagonal limiting symmetry cases are included without special limiting arguments.

## Assumptions and scope
No normalization of area or diameter is imposed; \(\Lambda\) must be a rank-two discrete lattice. The law concerns **intrinsic torus geodesic distance**, not ambient Euclidean distance of any embedding and not Euclidean distances between lattice sites. Both samples have the unique normalized translation-invariant area measure. The theorem is dimension-specific; no corresponding rigidity is asserted in dimensions three and above. The derivative \(F_\Lambda'\) is interpreted as the continuous radial area-density function, which exists everywhere for \(r>0\), even at the thresholds.

## Proof
**1. From two random points to a radial Voronoi area.** Translation invariance makes \(X-Y\) Haar-uniform on \(T_\Lambda\). Let \(V\) be the Voronoi cell of the origin. Almost every torus point has a unique representative in \(V\), of Euclidean norm equal to its distance from the origin. Thus
\[
F_\Lambda(r)=\frac{\operatorname{area}(V\cap\overline B(0,r))}{A},
\quad A=\operatorname{area}(V)=|\det(u,v)|
\]
for any lattice basis \(u,v\). Since \(V\) contains a centered open disk, \(F_\Lambda(r)=\pi r^2/A\) for all sufficiently small positive \(r\). This recovers \(A\).

**2. Exact angular formula.** Write the distinct facet-defining inequalities of \(V\) as
\[
x\cdot n_j\le d_j,\qquad j=1,\ldots,2m,
\]
where each \(n_j\in S^1\) is an outward unit normal and \(d_j>0\) its support distance. For \(r>d_j\), define the forbidden closed angular arc centered at the argument of \(n_j\), of half-width \(\arccos(d_j/r)\). At \(r\le d_j\), the arc is empty. Let \(U(r)\) be the union of all forbidden arcs, and let \(L(r)\) be its angular length (between zero and \(2\pi\)). A polar-area calculation, valid for every \(r>0\), gives
\[
F_\Lambda'(r)=\frac rA\bigl(2\pi-L(r)\bigr).
\]
Indeed, a radial ray reaches length at least \(r\) within \(V\) precisely when its direction belongs to none of the forbidden arcs. Since each arc length tends continuously to zero at its birth, the displayed derivative is continuous everywhere.

**3. Births are precisely detectable.** The perpendicular foot \(d_jn_j\) lies in the *relative interior* of every genuine Voronoi edge. To check this without a generic-position assumption, write the edge as the bisector between \(0\) and its relevant lattice vector \(w=2d_jn_j\). The only lattice sites equidistant to \(w/2\) are then \(0,w\); equivalently, \(\pm w\) are the only shortest representatives of the parity class \(w+2\Lambda\). Otherwise the bisector touches the Voronoi cell only in lower dimension and is not a genuine edge (the standard strict Voronoi-vector criterion). Consequently \(d_jn_j\) strictly satisfies all the other facet inequalities. Its normal direction is therefore separated by a positive angular gap from every forbidden arc already present at radius \(d_j\).

Suppose exactly \(k\) *pairs of opposite* genuine edges have common support distance \(d\). For sufficiently small \(\varepsilon>0\), the newly born \(2k\) arcs at \(d+\varepsilon\) are disjoint from one another and from all old arcs, and together contribute
\[
4k\arccos\!\left(\frac d{d+\varepsilon}\right)
=4k\sqrt{\frac{2\varepsilon}{d}}+O(\varepsilon^{3/2})
\]
to \(L(d+\varepsilon)\). All remaining arc endpoints are smooth as functions of \(r\) near \(d\); lengths of unions of finitely many arcs with uniformly bounded endpoint velocities are locally Lipschitz, including at arc-merger radii. Hence the old-arc contribution to \(L(d+\varepsilon)-L(d-\varepsilon)\) is \(O(\varepsilon)\). Substitution into step 2 gives the exact one-sided signature
\[
F_\Lambda'(d+\varepsilon)-F_\Lambda'(d-\varepsilon)
=-\frac{4k\sqrt{2d}}A\sqrt\varepsilon+O(\varepsilon).
\]
At every radius not equal to a facet distance, all arc endpoints (where present) have bounded derivatives in a neighborhood. Therefore \(L\), and thus \(F'\), is locally Lipschitz there: no other radius has such a nonzero square-root signature. This proves the recovery and integral multiplicities, even if facet distances coincide with polygon-vertex radii.

**4. Classifying and reconstructing the lattice.** By planar Gauss reduction, every rank-two lattice admits a basis \(u,v\) with
\[
0<|u|\le |v|,\qquad 0\le s:=u\cdot v\le |u|^2/2.
\]
The strict Voronoi-vector criterion, applied to the three nonzero parity classes of \(\Lambda/2\Lambda\), says the following. The class of \(u\) has exactly \(\pm u\) as shortest vectors; the class of \(v\) has exactly \(\pm v\); the remaining class has exactly \(\pm(v-u)\) if \(s>0\), and ties \(\pm(v-u),\pm(v+u)\) if \(s=0\). For completeness, these minimality assertions follow by considering the quadratic form \(Q(j,k)=j^2|u|^2+2jk s+k^2|v|^2\), using \(0\le s\le|u|^2/2\le|v|^2/2\): when \(|k|\ge2\), minimizing the square-completed expression yields \(Q(j,k)\ge3k^2|v|^2/4\); the remaining cases \(k=0,\pm1\) reduce immediately to the nearest integer of the required parity. Thus for \(s>0\) the genuine edge normals correspond to \(\pm u,\pm v,\pm(v-u)\), while for \(s=0\) they correspond only to \(\pm u,\pm v\). This also proves that a planar lattice Voronoi cell has four or six edges.

In the nonrectangular case, \(|u|\le|v|\le|v-u|\), because \(|v-u|^2-|v|^2=|u|^2-2s\ge0\). The recovered three facet distances therefore satisfy \((a,b,c)=(|u|,|v|,|v-u|)/2\), with multiplicity. Polarization recovers \(s=(|u|^2+|v|^2-|v-u|^2)/2=2(a^2+b^2-c^2)\). In the rectangular case \(s=0\) and the two support distances give the two orthogonal basis lengths. A real positive-definite Gram matrix determines its basis up to orthogonal transformation, completing the inversion and the theorem. \(\square\)

## Verification
An independent finite numerical calculation constructs the four or six Voronoi halfplanes of each test lattice, takes angular unions of their forbidden arcs, and compares the predicted singular multiplicities with centered derivative differences at offsets \(10^{-5}\), \(10^{-7}\), and \(10^{-9}\). Generic oblique, equal-length hexagonal, rectangular, and nonrectangular coincident-distance test cases recover multiplicities \((1,1,1)\), \((3)\), \((1,1)\), and \((1,2)\), respectively. Separately, midpoint-angle integration of the radial area agrees with the expected small-radius quadratic formula and full-area saturation, up to reported numerical discretization error. An independently generated sample of 75,000 Haar-distributed torus point pairs at five radius thresholds agrees with the computed radial CDF within the stated sampling tolerances; reproduce with `python check_sampling.py` and inspect `sampling_checks.txt`. Reproduce with `python verify_geometry.py`; representative outputs are in `numerical_checks.txt`. These finite checks are corroboration, not a replacement for the preceding proof.

## Relationship to prior work
Mantegazza--Mascellani--Uraltsev (first public version 2013-03-06) characterize the distributional Hessian of Riemannian distance and its cut-locus singular measures. Their general distance-function framework does not derive the *one-dimensional radial probability law* or an inverse classification of flat tori. Kurlin (2022) gives the planar strict Voronoi-vector and obtuse-superbase classification and proves completeness of the **lattice-neighbor distance sequence**, which is distinct from the law of distances between two uniformly random torus points. The inverse step here is that the latter law exposes the Voronoi facet distances, with their multiplicities, through a precise \(\sqrt\varepsilon\) transition. Zhou (2026) obtains facet-dependent Fourier signatures of the full distance kernel, but the Fourier data of the full kernel contain directional information absent from the scalar distance histogram. A previous facet-gradient-jump integral on planar flat tori likewise gives a single scalar integral rather than reconstructing the full lattice from this histogram.

## Limitations
The theorem recovers only the lattice up to Euclidean isometry, not its placement or orientation in a coordinate plane. It assumes the *entire exact continuum* distribution; finite noisy histograms may not resolve very short facet edges or nearly coincident thresholds. No finite-sample stability bound, algorithmic sample complexity, or analogous higher-dimensional rigidity theorem is claimed. The literature comparison was extensive but cannot rule out an equivalent older theorem in every inaccessible specialist source; independent external review remains outstanding.

## References
1. C. Mantegazza, G. Mascellani, G. Uraltsev, *On the Distributional Hessian of the Distance Function*, arXiv:1303.1421 (v1 first public 2013-03-06), https://arxiv.org/html/1303.1421v3.
2. V. Kurlin, *Mathematics of 2-dimensional lattices*, arXiv:2201.05150 (first public 2022-01-13), particularly Sections 2, 3, 8 and Appendix A, https://arxiv.org/html/2201.05150v3.
3. Y. Zhou, *Distance Energies and Negative Type of Flat Tori*, arXiv:2609.05622 (first public 2026-09-04), particularly Sections 1–3, https://arxiv.org/html/2609.05622v1.
