# Exact six-, eight-, and ten-sided central-section law for the regular dodecahedron

## Finding

Let \(P\subset\mathbb R^3\) be a regular dodecahedron centered at the origin, \(U\) a uniformly distributed unit vector, and \(N(U)\) the number of sides of the convex polygon \(P\cap U^\perp\). Let \(\alpha=\arccos(1/3)\) and \(\beta=\arccos(\sqrt5/3)\). Then, almost surely, \(N\in\{6,8,10\}\), with the **complete exact law**
\[
\begin{aligned}
\Pr(N=6)&=10-\frac{15(\alpha+\beta)}{\pi}=0.638408811559\ldots,\\
\Pr(N=8)&=\frac{15(2\alpha+\beta-\pi)}{\pi}=0.238989468900\ldots,\\
\Pr(N=10)&=6-\frac{15\alpha}{\pi}=0.122601719541\ldots.
\end{aligned}
\]
The orientation sphere splits into precisely \(92\) open cells bounded by ten great circles: \(20\) congruent spherical hexagons give six-sided sections, \(60\) congruent spherical triangles give eight-sided sections, and \(12\) congruent spherical pentagons give ten-sided sections. The exceptional great circles have measure zero.

## Assumptions and scope

Use the standard Cartesian vertex model with \(\varphi=(1+\sqrt5)/2\): the eight vertices \((\pm1,\pm1,\pm1)\), together with the twelve even-cyclic permutations of \((0,\pm\varphi^{-1},\pm\varphi)\), where the latter two signs vary independently. Any scaled and rotated regular dodecahedron has the same law. The plane is **central** (passes through the symmetry center), and its normal is Haar-uniform on the sphere; these probabilities are not those of independently translated random section planes.

## Proof

**1. Chamber decomposition.** A face of the regular dodecahedron is a pentagon. For any normal \(u\) for which no vertex lies in \(u^\perp\), this plane meets the relative interior of a facet exactly when the five signed vertex heights on that facet include both signs. Each intersected facet contributes exactly one polygon edge. The face-crossing status therefore depends only on the signs of \(u\cdot v\) for the twenty vertices, or equivalently on which component of the complement of the ten distinct great circles \(u\cdot v=0\), with antipodal \(v\) identified, contains \(u\). This excludes a Haar-null set.

**2. Exact chamber certificate.** Double every vertex coordinate, so that each belongs to the quadratic integer ring \(\mathbb Z[\sqrt5]\), and all vertex squared norms equal \(12\). Choose one from each antipodal vertex pair as one of ten circle normals. The standalone code `dodeca_exact.py` performs all sign calculations **exactly** in \(\mathbb Z[\sqrt5]\), including the signs of all 120 determinants of triples of normals. Every determinant is nonzero; hence the ten great circles have no triple intersections. A great-circle arrangement in general position with ten circles has \(10(10-1)+2=92\) cells. The code generates all 92 chambers by exact perturbations at pairwise intersections, identifies every chamber's bounding rays by all pairwise normal cross products, and checks the signs of the twenty vertex heights on a strictly interior sum of these rays. The twelve dodecahedral pentagonal facets are independently generated as supporting faces normal to the twelve vertices of its dual regular icosahedron; each contains exactly five vertices. Thus the certificate independently counts the crossed facets in each chamber.

The exhaustive **exact** chamber classification, tabulated by number of section edges, chamber-edge count, and chamber count, is
\[
\begin{array}{c|c|c}
N&\text{edges of spherical chamber}&\text{chambers}\\\hline
6&6&20\\8&3&60\\10&5&12.
\end{array}
\]
The certificate also computes the exact cosine of every spherical polygon interior angle: for the 20 hexagonal cells there are three angles with cosine \(-1/3\) and three with cosine \(-\sqrt5/3\); for the 60 triangular cells there are two with cosine \(1/3\) and one with cosine \(\sqrt5/3\); for the 12 pentagonal cells all five angles have cosine \(-1/3\). Each cosine follows directly from the dot product of the two inward signed unit great-circle normals meeting at the vertex. These are algebraic identities, not floating-point inferences.

**3. Solid angles and normalization.** Spherical Girard excess for a \(k\)-sided spherical polygon is the sum of its interior angles minus \((k-2)\pi\). Using \(\alpha=\arccos(1/3)\) and \(\beta=\arccos(\sqrt5/3)\), the respective single-cell areas are
\[
\begin{aligned}
A_6&=2\pi-3\alpha-3\beta,\\
A_8&=2\alpha+\beta-\pi,\\
A_{10}&=2\pi-5\alpha.
\end{aligned}
\]
They are positive, and the exact consistency identity \(20A_6+60A_8+12A_{10}=4\pi\) holds. Division of \(20A_6,60A_8,12A_{10}\) by the sphere area \(4\pi\) produces the displayed probabilities. No numerical integration or finite sampling is used to prove the infinite-sphere assertion.

## Verification

Run `python3 dodeca_exact.py`. It uses only the Python standard library and exact integer-pair arithmetic for \(\mathbb Z[\sqrt5]\). The recorded successful run is in `dodeca_exact_output.txt`; the output certifies all chamber sign patterns, exact facet counts, spherical chamber side counts, and algebraic interior-angle cosine multisets. Independently, `dodeca_law.py` numerically reconstructs the spherical chambers and evaluates their angles and normalized areas; it yields the displayed decimals to the printed precision. The exact certificate supplies the nonnumerical proof of the finite enumeration; the analytic spherical-excess argument supplies the probability normalization.

## Relationship to prior work

The classical general question of frequencies of polygon types in planar polyhedral sections is studied by K. Voss, *Frequencies of n-polygons in planar sections of polyhedrons*, Journal of Microscopy (1982), DOI below. Its publicly available abstract describes integral-geometric methods for classes of polyhedra; the full paper could not be inspected, and an unrecognized earlier specialized dodecahedral calculation remains a historical-priority risk. Dirksen studies volumes of regular-simplex sections, not polygon-count probabilities for dodecahedra. Akama and Yan study spherical dodecahedral tilings, not central plane section frequencies. Preexisting formulas for central sections of the regular icosahedron and of rectangular boxes concern different bodies and do not imply the three probabilities here by elementary duality: polar duality exchanges sections with **projections of the polar**, not sections of the polar itself. General-purpose enumeration methods can derive this answer but are not the same as a pre-existing table of these exact probabilities. The novelty claimed is the particular complete dodecahedral law, its three chamber orbits, and the explicit closed formulas, not the general chamber-arrangement method.

## Limitations

Only central planes and Haar-uniform orientations are considered. The measure-zero degeneracy set is excluded; tangential or vertex-passing sections may have other side counts. No statement is made for translated planes, irregular dodecahedra, or arbitrary stereological sampling of solids. This is a self-review, not independent verification. The full text of the 1982 Voss article was unavailable; its potentially relevant prior coverage has not been conclusively excluded.

## References

- K. Voss, *Frequencies of n-polygons in planar sections of polyhedrons*, Journal of Microscopy 128 (1982), 111–120, DOI: 10.1111/j.1365-2818.1982.tb00443.x (abstract inspected; complete article inaccessible).
- Y. Akama and M. Yan, *On Deformed Dodecahedron Tiling*, arXiv:1403.6907, publicly posted 2014-03-27; https://arxiv.org/abs/1403.6907.
- H. Dirksen, *Sections of the regular simplex—Volume formulas and estimates*, arXiv:1509.06408, publicly posted 2015-09-21; https://arxiv.org/abs/1509.06408.
