# A squared-distance plateau and exact intrinsic distance laws on tetrahedral face medians

## Finding
Let \(S_a\) be the boundary of a regular tetrahedron of edge length \(a>0\), with its intrinsic shortest-path metric and normalized surface-area measure. In any face, let \(p_s\) travel from the midpoint of one edge to that face's centroid: in unit-edge planar coordinates with face vertices \((0,0),(1,0),(1/2,\sqrt3/2)\), its position is \(q_s=(1/2,\sqrt3s)\), where \(0\le s\le1/6\); multiply all coordinates by \(a\) for general edge length. Let \(X\) be surface-area uniform and \(D_s=d_{S_a}(p_s,X)\).

For \(0\le s\le1/6\), put
\[
R_s=\sqrt{1+12s^2},\qquad d_-(s)=\sqrt3(1/2-s),\qquad d_+(s)=\sqrt3(1/2+s).
\]
Define the circular-cap area
\[
C(r,d)=\begin{cases}0,&0\le r\le d,\\ r^2\arccos(d/r)-d\sqrt{r^2-d^2},&r>d.\end{cases}
\]
The *complete intrinsic distance distribution* at every point on these 12 face-median half-segments is
\[
\Pr(D_s/a\le r)=\begin{cases}
0,&r<0,\\
\dfrac{\pi r^2-2C(r,R_s/2)-C(r,d_-(s))-C(r,d_+(s))}{\sqrt3},&0\le r<R_s,\\
1,&r\ge R_s.
\end{cases}
\]
In particular, an entire continuum of inequivalent source points has the same mean squared intrinsic distance,
\[
\boxed{\mathbb E[D_s^2]=a^2/3},
\]
while its fourth distance moment changes strictly along each open half-segment:
\[
\boxed{\mathbb E[D_s^4]=\frac{a^4}{30}(1+12s^2)(5-36s^2)}.
\]
The fourth moment rises from \(a^4/6\) at the edge midpoint to \(8a^4/45\) at the centroid. Simultaneously the source eccentricity is \(aR_s\), increasing strictly from \(a\) to \(2a/\sqrt3\). Thus equal average squared geodesic dispersion does not imply equal full intrinsic distance distribution, higher moments, or farthest-point distance.

## Assumptions and scope
Distances are intrinsic, not straight-line chords through the ambient three-space. The source traverses a specified face median only from edge midpoint to face centroid, including both endpoints. All 12 such half-segments follow by tetrahedral symmetry. The target \(X\) is uniform for the surface-area measure. The theorem does not claim that these points globally minimize the squared-distance average, nor that these segments are its entire level set. Scaling by \(a\) is explicit in all formulas.

## Proof
**1. Flat quotient and distance formula.** Develop the tetrahedral equilateral faces into the triangular tiling. Set \(\Lambda=\langle(2,0),(1,\sqrt3)\rangle\subset\mathbb R^2\). The two-dimensional flat torus \(\mathbb R^2/\Lambda\) has area \(2\sqrt3\). Quotienting this torus by central inversion \(z\mapsto-z\) yields four cone points of total angle \(\pi\), and a cell decomposition by four unit equilateral triangles; matching face edges realizes precisely the intrinsic regular tetrahedron. Inversion has order two away from the four cone points, so normalized Haar area on the torus pushes forward to normalized tetrahedral area. Lifting a source to \(q_s\) gives, for target lift \(z\),
\[
d_{S_1}(p_s,[z])=\min_{\lambda\in\Lambda,\,\epsilon\in\{\pm1\}}|z-(\lambda+\epsilon q_s)|.
\]
This holds also at the branch points by continuity.

**2. The entire nearest-source cell.** Translate the source \(q_s\) to the origin in the plane. Among other lifts are the four displacement vectors
\[
(1,-2\sqrt3s),\quad(-1,-2\sqrt3s),\quad(0,\sqrt3(1-2s)),\quad(0,-\sqrt3(1+2s)).
\]
Their four perpendicular-bisector halfplanes intersect in the isosceles trapezoid
\[
V_s=\operatorname{conv}\left\{\left(\pm(1/2+3s),\sqrt3(1/2-s)\right),\ \left(\pm(1/2-3s),-\sqrt3(1/2+s)\right)\right\}.
\]
The last lower pair coalesces when \(s=1/6\), giving a triangle. This candidate has vertical height \(\sqrt3\), widths \(1+6s\) and \(1-6s\), hence area \(\sqrt3\). The actual Voronoi cell of the entire periodic set \((\Lambda+q_s)\cup(\Lambda-q_s)\) at \(q_s\) is contained in \(V_s\). For \(0\le s\le1/6\), the two point orbits are distinct, and inversion exchanges them. Thus its two cells in a fundamental torus have equal area \((2\sqrt3)/2=\sqrt3\). Containment and equal area force the candidate \(V_s\) to be the actual Voronoi cell, up to null boundaries. This argument verifies that *all* remaining periodic images are irrelevant, rather than relying on a finite image search.

**3. Circular caps and the distribution.** All trapezoid vertices have squared distance \(1+12s^2\) from the origin, so \(V_s\) is cyclic with circumradius \(R_s\). Its two sloping sides lie at distance \(R_s/2\) from the origin; the two horizontal sides lie at distances \(d_-(s)\) and \(d_+(s)\). At radius \(r\le R_s\), the four portions of a centered radius-\(r\) disk cut off by these four side halfplanes have disjoint interiors: their exterior arcs end at successive circumcircle vertices. Their areas are the indicated circular caps \(C(r,d)\). Subtracting these four areas from \(\pi r^2\), then dividing by cell area \(\sqrt3\), proves the exact formula up to \(R_s\). There is no mass beyond \(R_s\). The formulas agree at every cap-onset threshold and at both endpoint values of \(s\).

**4. Exact moments.** Put \(y=\sqrt3(v-s)\). The horizontal cross-section of \(V_s\) at \(-1/2\le v\le1/2\) has half-width \(w(v)=1/2+6sv\). Its area element is \(\sqrt3\,dx\,dv\), exactly canceled by area normalization. For every nonnegative integer \(k\),
\[
\mathbb E[D_s^{2k}]/a^{2k}=\int_{-1/2}^{1/2}\int_{-w(v)}^{w(v)}\bigl(x^2+3(v-s)^2\bigr)^k\,dx\,dv.
\]
For \(k=0,1,2\), elementary polynomial integration gives respectively \(1\), \(1/3\), and \((1+12s^2)(5-36s^2)/30\). The derivative of the fourth-moment factor is \(\frac85s(1-36s^2)>0\) for \(0<s<1/6\). Since a convex polygon's farthest point from the origin is a vertex, its maximum distance is exactly \(R_s\). This completes the proof.

## Verification
The independent-of-data symbolic integration in the accompanying `CHECK.py` uses exact rational SymPy polynomial arithmetic and confirms mass normalization and both moment identities **for all real parameters algebraically**, not just at sampled parameters. It also checks the complete competing-image Voronoi vertices at 61 parameter values, the CDF's support and monotonicity at 53 configurations, and direct distances to 550,000 total Haar-uniform torus target samples at five source positions. The 55 Monte Carlo CDF comparisons have maximum observed absolute discrepancy 0.003290. These finite numerical tests corroborate the analytical Voronoi and distribution proofs and are not substitutes for the all-parameter area argument.

Reproduce with `python3 CHECK.py` after installing Python packages `numpy` and `sympy`; no downloaded datasets or external services are required.

## Relationship to prior work
Davis, Dods, Traub and Yang (2015) describe vertex-to-point geodesics on the regular tetrahedron using its equilateral tiling. Fuchs (2016) studies regular-polyhedron geodesics with vertex endpoints. Davis (2023), particularly the expanded cut loci in Section 2 and Figure 2.8, studies **the same source-segment geometry** used here; no originality is claimed for its basic cut-locus picture. Those works address geodesic trajectories, cut loci, or geodesic complexity, rather than the exact uniform-area distance law and the continuous constant-second-moment / strictly varying fourth-moment phenomenon established here. General power-diagram quantization literature covers broad Voronoi methods, not this specific intrinsic tetrahedral distribution. A relevant existing vertex-source distance distribution is also distinct, because its source is a tetrahedral cone vertex rather than an edge-midpoint-to-face-centroid position. Historical priority beyond inspected sources is not certified.

## Limitations
Only the twelve specified half-face medians are classified, not arbitrary source positions or the full extremizer set for global mean squared distance. Voronoi-cell geometry is related to previously published tetrahedral cut-locus diagrams. The mathematical proof is self-contained for the stated family; numerical tests are finite and an independent scholarly audit has not been carried out. Exact novelty against every potentially unindexed historical publication cannot be guaranteed.

## References
1. D. Davis, V. Dods, C. Traub, J. Yang, *Geodesic trajectories on regular polyhedra*, arXiv:1508.03546v1, first posted 2015-08-12, https://arxiv.org/abs/1508.03546 .
2. D. Fuchs, *Geodesics on Regular Polyhedra with Endpoints at the Vertices*, first online 2016-03-23, doi:10.1007/s40598-016-0040-z .
3. D. M. Davis, *Geodesic complexity of a tetrahedron*, arXiv:2306.11059v1, first posted 2023-06-19, https://arxiv.org/abs/2306.11059 .
4. D. P. Bourne, S. M. Roper, *Centroidal power diagrams, Lloyd's algorithm and applications to optimal location problems*, 2015. (Generic Voronoi quantization context.)
