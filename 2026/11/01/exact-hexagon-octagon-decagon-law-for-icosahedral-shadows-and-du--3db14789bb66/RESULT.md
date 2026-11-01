# Exact hexagon–octagon–decagon law for icosahedral shadows and dual dodecahedral sections

## Finding
Let \(\varphi=(1+\sqrt5)/2\) and let \(I\) be the regular icosahedron with vertices
\[
(0,\pm1,\pm\varphi),\quad(\pm1,\pm\varphi,0),\quad(\pm\varphi,0,\pm1).
\]
For a Haar-uniform \(U\in S^2\), let \(N(U)\) denote the number of sides of the orthogonal shadow \(\operatorname{proj}_{U^\perp}I\). Define the two angles
\[
\alpha=\arccos\left(\frac1{\varphi\sqrt3}\right),\qquad
\beta=\arccos\left(\frac1{\sqrt3}\right).
\]
Then, almost surely, \(N(U)\in\{6,8,10\}\), with the complete exact law
\[
\begin{aligned}
\mathbb P\{N=6\}&=\frac{30}{\pi}\left(\alpha+\beta-\frac{2\pi}{3}\right)=0.638408811559345\ldots,\\
\mathbb P\{N=8\}&=\frac{30}{\pi}\left(\pi-\alpha-2\beta\right)=0.238989468899764\ldots,\\
\mathbb P\{N=10\}&=\frac{30}{\pi}\left(\beta-\frac{3\pi}{10}\right)=0.122601719540890\ldots.
\end{aligned}
\]
In particular, the exact mean is
\[
\mathbb E N=\frac{30}{\pi}\arccos\left(\frac{\sqrt5}{3}\right)=6.96838581596309\ldots.
\]
The same polygon-side-count distribution holds for Haar-uniform central planar sections of any regular dodecahedron, by polarity. The theorem concerns a complete discrete law, not merely its expectation.

## Assumptions and scope
The projection is an ordinary orthogonal projection onto a plane through the origin, with normal distributed according to normalized spherical area. The body is a nondegenerate *regular* icosahedron; scaling and rotation do not affect the result. A direction is generic when it is not orthogonal to any facet normal; the excluded finite union of great circles has spherical measure zero. For such directions, the projected convex polygon has no degeneracies, so its number of vertices equals its number of sides. The dodecahedral counterpart concerns central sections, not orthogonal shadows of the dodecahedron.

## Proof
**1. A silhouette-edge sign rule.** Let \(\nu_f\) be the outward normal of a face \(f\) of a convex three-dimensional polyhedron. For a generic viewing direction \(u\), an original edge between adjacent faces \(f,g\) appears on the silhouette exactly when \((u\cdot\nu_f)(u\cdot\nu_g)<0\). Indeed the two neighboring face planes then lie on opposite sides of the viewing horizon; otherwise their common edge projects into the interior of the outline. Every edge of a generic convex-polygon outline comes from exactly one such original edge. Thus its side count is the number of sign-changing adjacencies in the dual face graph.

For the specified icosahedron, the twenty outward facet-normal directions are the twenty vectors, divided by \(\sqrt3\), in
\[
\{(\pm1,\pm1,\pm1)\}
\cup\{(0,\pm\varphi,\pm\varphi^{-1})\}
\cup\{(\pm\varphi^{-1},0,\pm\varphi)\}
\cup\{(\pm\varphi,\pm\varphi^{-1},0)\}.
\]
Each normal supports exactly one triangular face, and the dual face-adjacency graph has thirty edges. The supplied exact-field checker derives these incidences directly from the twelve vertices, without assuming them numerically.

**2. Reduce the entire sphere to one fundamental spherical triangle.** Take the following unnormalized positive rays:
\[
A_0=(0,-1,-\varphi),\quad B_0=(-1,-1,-1),\quad
C_0=(-\varphi^{-1},-\varphi,-1).
\]
Their unit normalizations are \(A,B,C\). These are, respectively, an incident vertex axis, face axis, and edge-midpoint axis. The icosahedral spherical face triangulation, subdivided into vertex–edge–face flags, consists of \(120\) congruent spherical triangles \(ABC\). Its angles at \(A,B,C\) are \(\pi/5,\pi/3,\pi/2\), so by spherical excess its area is \(\pi/30\). The tiles cover the sphere with overlaps only on null boundaries.

Choose from each antipodal normal pair the representative with positive dot product with \(B_0\). Exact substitution gives the following *complete* table of signs at \((A_0,B_0,C_0)\):

| Signs at the three rays | Number of representative normals |
| --- | ---: |
| \((+,+,+)\) | 7 |
| \((+,+,0)\) | 1 |
| \((-,+,0)\) | 1 |
| \((-,+,+)\) | 1 |

All other normals are negatives of these ten. The two normals whose equators genuinely cut the triangle are
\[
n_1=(-\varphi,\varphi^{-1},0),\qquad n_2=(-1,-1,1).
\]
The first equator runs from \(C\) to \(P\), and the second from \(D\) to \(P\), where unit vectors \(P,D\) lie on the arcs \(AB,AC\), respectively, and are represented by the positive rays
\[
P_0=A_0+\varphi^{-1}B_0=(-\varphi^{-1},-\varphi,-\sqrt5),
\qquad D_0=2A_0+C_0.
\]
The equalities \(n_1\cdot C_0=n_1\cdot P_0=n_2\cdot P_0=n_2\cdot D_0=0\) are exact identities in \(\mathbb Q(\sqrt5)\). Moreover \(\|P_0\|=2\sqrt2\), \(\|D_0\|=2\sqrt3\varphi\); their positive-ray expressions locate them on the claimed arcs. The remaining normal with a zero at \(C\) touches the triangle only at that endpoint. Therefore these two cuts partition the entire fundamental triangle into precisely three spherical triangles \(ADP\), \(DCP\), and \(CBP\). There is no unexamined open region.

**3. Identify the shadow counts, exactly.** Evaluate the twenty signs of \(u\cdot\nu_f\) at any interior ray of each of those three regions. Since signs do not change inside a region, the number of sign-changing edges is constant there. Exhaustive exact comparisons in \(\mathbb Q(\sqrt5)\), counting the thirty adjacent face pairs, give
\[
\begin{array}{c|ccc}
\text{region}&ADP&DCP&CBP\\\hline
\text{silhouette edges}&10&8&6.
\end{array}
\]
For example, positive sums of the three respective unnormalized corner rays are interior test directions. The executable certificate verifies all twenty face supports, all thirty dual adjacencies, the endpoint-sign table and the three stated counts using rational arithmetic in \(\mathbb Q(\sqrt5)\).

**4. Integrate the three region areas.** Direct spherical-angle calculations using the displayed vectors give
\[
\begin{array}{c|ccc}
\text{triangle}&\text{first angle}&\text{second angle}&\text{third angle}\\\hline
ADP&\pi/5&\pi/2&\beta\\
CBP&\alpha&\pi/3&\beta.
\end{array}
\]
These identities can be checked *exactly* by squaring the tangent-plane cosine formula: the resulting squared cosines lie in \(\mathbb Q(\sqrt5)\), and their signs are positive (except for the right angle). The checker verifies all these algebraic identities. Girard's spherical excess formula now gives
\[
\operatorname{area}(ADP)=\beta-3\pi/10,\qquad
\operatorname{area}(CBP)=\alpha+\beta-2\pi/3.
\]
Subtract from \(\operatorname{area}(ABC)=\pi/30\) to obtain \(\operatorname{area}(DCP)=\pi-\alpha-2\beta\). Since all \(120\) fundamental triangles are congruent and the distribution is rotation invariant, each global event probability is precisely its region area divided by \(\pi/30\). This proves the law.

For the mean, each of the thirty icosahedral edges has adjacent outward normals meeting at angle \(\arccos(\sqrt5/3)\). A uniformly random direction separates any two fixed normal directions meeting at angle \(\theta\) with probability \(\theta/\pi\). Summing the thirty silhouette-edge indicators proves the independent mean formula above.

**5. Dual central-section formulation.** For a full-dimensional centrally symmetric body \(K\) containing the origin and any plane \(L\), the polar *within \(L\)* of its orthogonal projection is \((K^\circ)\cap L\). Applied to \(K=I\), its polar is a regular dodecahedron (up to similarity). In dimension two, polarity interchanges edges and vertices but preserves their total count. Thus the derived three-point law also describes central planar sections of the regular dodecahedron.

## Verification
Run `python3 verify_icosahedron_shadows.py` from the directory containing this file. It uses only the Python standard library. Its exact certificate checks all twenty face supports, the thirty face adjacencies, the ten antipodal normal representatives, all four endpoint sign patterns, the two active great circles, the three combinatorial region counts, and nine spherical-angle squared-cosine identities by exact arithmetic in \(\mathbb Q(\sqrt5)\). Its numerical diagnostics independently check spherical excess and the mean, and compare projected planar convex-hull counts with dual sign counts for 2,000 reproducible random directions. A successful run prints `EXACT_Q5_CHAMBERS_AND_SHADOW_COUNTS_OK`. Numerical random checks do not replace the exhaustive exact sign calculation or the analytic spherical-area proof.

## Relationship to prior work
Donoho and Tanner, *Counting faces of randomly-projected polytopes when the projection radically lowers dimension* (first public July 15, 2006; arXiv:math/0607364), treat random projection face counts in broad and mainly high-dimensional regimes rather than this exact regular-icosahedron law. Black and Criado, *Random Shadows of Fixed Polytopes* (arXiv:2406.06936, first public June 11, 2024), give general expected-complexity bounds for shadows of fixed polytopes; their inspected article does not specialize to the complete icosahedral silhouette law. A geometric account of regular icosahedron projections at representative axes (Eusebeia, last updated March 21, 2019) displays hexagonal, octagonal, and decagonal examples, but not their Haar probabilities.

A separately published exact law for **central sections of the icosahedron** concerns ten- and twelve-gons, not orthogonal shadows of the icosahedron. Polarity converts the present shadows into **central sections of the dodecahedron**, not the icosahedron. Likewise, published Platonic shadow-area variances concern continuous area rather than discrete silhouette side counts. These are genuine adjacent results, not alternate statements of the present three-point law. General polyhedral algorithms can in principle enumerate and integrate the appropriate normal-fan cells; an equivalent older explicit calculation of this particular distribution remains possible.

## Limitations
This is an almost-sure law; directions on finitely many normal equators are not classified, and the corresponding nongeneric projections may have merging edges. The result is restricted to *regular* icosahedra and normalized uniform orientations. No assertion is made about perturbed solids, affine icosahedra, or noncentral dodecahedral sections. Novelty relative to unindexed older stereological and polyhedral-visibility literature is not independently certified. All probability equalities follow analytically, not from simulation.

## References
1. D. L. Donoho and J. Tanner, *Counting faces of randomly-projected polytopes when the projection radically lowers dimension*, arXiv:math/0607364, first posted July 15, 2006, https://arxiv.org/abs/math/0607364.
2. A. E. Black and F. Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936, first posted June 11, 2024, https://arxiv.org/html/2406.06936v1.
3. *The Icosahedron*, Eusebeia, projections and coordinates, last updated March 21, 2019, https://eusebeia.qfbox.info/4d/icosahedron.
4. *Exact Haar polygon-type law for central icosahedron sections*, published geometric research note, October 11, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-haar-polygon-type-law-for-central-icosahedron-sections--65970a533c4f.
5. *Exact orientation-variance spectrum of Platonic shadow areas*, published geometric research note, October 11, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-orientation-variance-spectrum-of-platonic-shadow-areas--76ed33fc3859.
