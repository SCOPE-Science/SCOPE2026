# Shadow-count complementarity under complete parallel truncation of a tetrahedron

## Finding
Let \(\Delta=\operatorname{conv}\{v_0,v_1,v_2,v_3\}\subset\mathbb R^3\) be any nondegenerate tetrahedron. For every choice of four real numbers \(t_i>0\) satisfying \(t_i+t_j<1\) whenever \(i\ne j\), truncate all four vertices by planes parallel to their opposite faces, obtaining
\[
P_{\mathbf t}=\operatorname{conv}\{(1-t_i)v_i+t_i v_j:0\le i,j\le3,\ i\ne j\}.
\]
For every direction \(u\in S^2\) outside the four great circles orthogonal to the outward normals of the original faces, let \(N_\Delta(u)\) and \(N_{\mathbf t}(u)\) be the numbers of vertices of the respective orthogonal projections to \(u^\perp\). Then the **pointwise, shape-independent and depth-independent complementarity law** is
\[
\boxed{N_{\mathbf t}(u)+N_\Delta(u)=12.}
\]
In particular \(N_{\mathbf t}(u)\) is always \(8\) or \(9\): a truncated tetrahedron has an octagonal shadow exactly when the original tetrahedron has a quadrilateral shadow, and a nonagonal shadow exactly when the original tetrahedron has a triangular shadow. No other generic counts occur.

Write \(\Omega_i\) for the ordinary solid angle, in steradians, of \(\Delta\) at \(v_i\). If \(U\) is uniformly distributed on the sphere, the **entire** generic shadow-type distribution is
\[
\boxed{\mathbb P(N_{\mathbf t}(U)=9)=\frac1{2\pi}\sum_{i=0}^3\Omega_i,\qquad
\mathbb P(N_{\mathbf t}(U)=8)=1-\frac1{2\pi}\sum_{i=0}^3\Omega_i.}
\]
Consequently \(\mathbb E N_{\mathbf t}(U)=8+(2\pi)^{-1}\sum_i\Omega_i\), independently of all four truncation depths. When \(\Delta\) is regular, including its Archimedean truncation at \(t_i=1/3\),
\[
\mathbb P(N_{\mathbf t}=9)=\frac6\pi\arccos\frac13-2\approx0.350959312184,
\qquad
\mathbb P(N_{\mathbf t}=8)=3-\frac6\pi\arccos\frac13\approx0.649040687816.
\]
The sharp range \(0<\mathbb P(N_{\mathbf t}=9)<1\) as the tetrahedron varies, with both endpoint limits approachable by degenerating tetrahedra, follows from the previously established tetrahedral shadow-angle theorem. The new assertion here is **the exact coupling with the fully truncated tetrahedron for each direction and every admissible set of unequal cuts**; the tetrahedral solid-angle probability itself is prior work.

## Assumptions and scope
The tetrahedron is an arbitrary four-vertex full-dimensional simplex in Euclidean three-space; it need not be regular. The parameter inequalities ensure that the four vertex cuts are proper and pairwise disjoint on every original edge. The orthogonal projection uses the Euclidean metric and the same direction for both solids. A direction is called generic when its scalar product with each of the four original outward face normals is nonzero; the excluded finite union of great circles has spherical measure zero. The probability measure is spherical Haar measure, equivalently uniform unoriented viewing planes. The assertion does not extend the numerical probabilities to arbitrary, nonuniform laws of directions.

## Proof
**1. Exact facets and incidences for arbitrary cuts.** Write each point of the tetrahedron in barycentric coordinates \(x=\sum_{i=0}^3\lambda_i v_i\) with \(\lambda_i\ge0\) and \(\sum_i\lambda_i=1\). The truncation is equivalently the intersection of \(\Delta\) with the four inequalities \(\lambda_i\le1-t_i\). Since \(t_i+t_j<1\), no two distinct new cutting planes intersect inside \(\Delta\). The twelve vertices are exactly the intersections \(\lambda_i=1-t_i\), \(\lambda_j=t_i\), other coordinates zero, with \(i\ne j\), giving the formula in the finding. There are four surviving old faces \(H_i\) (hexagons) and four new cutting faces \(T_i\) (triangles). Every unordered pair \(H_i,H_j\) shares one edge, every ordered pair \(T_i,H_j\) with \(i\ne j\) shares one edge, and no two cutting triangles share an edge. This accounts for the full \(6+12=18\) edges.

**2. Facet-normal pairing.** Let \(n_i\) be the outward unit normal of the old face opposite \(v_i\). Then \(H_i\) has outward normal \(n_i\), while \(T_i\) has outward normal \(-n_i\), since its plane is parallel and faces in the opposite direction. The area-weighted normal equilibrium relation \(\sum_i A_i n_i=0\), with all \(A_i>0\), implies that, for a generic direction \(u\), the number
\[
k(u)=\#\{i:n_i\cdot u>0\}
\]
is one of \(1,2,3\).

**3. Silhouette-edge criterion.** For a convex three-dimensional polyhedron and a generic viewing direction, an edge belongs to the contour of its orthogonal projection precisely when the two incident outward face normals have scalar products with the viewing direction of opposite signs. Its projection produces one vertex of the planar shadow; hence the number of shadow vertices is the number of such incident-face edges. One way to see the criterion is to intersect each two-dimensional edge normal cone, spanned by its adjacent face normals, with the great circle of supporting normals in \(u^\perp\). The great circle meets the relative interior of the cone if and only if the two endpoint normals have opposite signed \(u\)-components. The intersection is transverse under the genericity hypothesis, and each such intersection is a distinct shadow edge of the planar normal fan.

For the original tetrahedron, every two old facets are adjacent. Of its six edges, precisely \(k(4-k)\) have opposite-sign incident normals. Hence
\[
N_\Delta(u)=k(4-k)=\begin{cases}3,&k=1\text{ or }3,\\4,&k=2.\end{cases}
\]
For the truncated tetrahedron, the six \(H_iH_j\) edges still contribute \(k(4-k)\). An edge \(T_iH_j\) is in the contour if and only if \(n_i\cdot u\) and \(n_j\cdot u\) have the **same** sign. Its twelve ordered pairs contribute
\[
2\left[\binom{k}{2}+\binom{4-k}{2}\right]=12-2k(4-k).
\]
Their sum is \(12-k(4-k)=12-N_\Delta(u)\). The asserted two-point classification and truncation-depth independence are proved for **every** generic direction, not merely almost surely.

**4. Probabilities and sharpness.** By step 3 the nine-vertex event is exactly the three-vertex event of the original tetrahedron. The classical tetrahedral solid-angle probability theorem (Feldman--Klain, 2008) gives the latter event probability as \(\sum_i\Omega_i/(2\pi)\). For a regular tetrahedron each vertex solid angle is \(3\arccos(1/3)-\pi\), giving the displayed exact constants. Positivity, strict upper bound, and sharp endpoint limits for the tetrahedral triangular-shadow probability were established in that earlier source, and transfer immediately under the event equality. The probability formula and sharp range are credited consequences, not separately novel angle theorems.

## Verification
Run `python verify.py` with Python 3, NumPy and SciPy available. The program independently reconstructs the two planar convex hulls from projected vertex coordinates for four geometric tetrahedra and three choices of truncation depths, over \(2300\) deterministic spherical directions per tetrahedron. It verifies both the individual sign-count formulas and the pointwise sum, and compares the empirical nine-vertex frequency to solid-angle formulas. A second, **exact-rational** projected-hull implementation uses integer viewing vectors and rational geometry on two tetrahedra and two depth choices, carrying out \(1016\) nondegenerate exact checks. It also evaluates the regular-tetrahedron closed formula against its independent spherical solid-angle computation. Output ends in `VERIFY_OK`.

The floating-point and rational checks are finite diagnostics, not an infinite proof. The all-tetrahedra, all-admissible-depth assertion follows from the barycentric incidence classification and the exact contour sign count. The solid-angle probability itself uses the cited established theorem.

## Relationship to prior work
Feldman and Klain, *Angles as probabilities* (2008), already proved \(\mathbb P(N_\Delta=3)=\sum_i\Omega_i/(2\pi)\) for every tetrahedron and observed the sharp probability range. Neither statement is claimed as new. Prior work on area-weighted tetrahedral shadows likewise already used this unweighted probability. Al-Ajmi, Koca and Bu Salasel studied particular Coxeter-plane projections of the uniform truncated tetrahedron, including an eightfold-symmetric projection. That is a prior example, not the asserted universal two-type law. Black and Criado derived general estimates for expected shadow complexity of fixed polytopes; their estimates do not give a pointwise coupling across independent vertex truncations. The distinction in this theorem is the exact **twelve-vertex complementarity and full four-parameter truncation invariance for every tetrahedron**, from which the already-known tetrahedral probability law is transferred without new spherical integration.

## Limitations
Cuts must be parallel to each vertex's opposite original face, positive and pairwise disjoint as stated; arbitrary bevel directions, missing cuts, and limiting merged cuts need not obey the law. The theorem concerns vertex counts, not the areas, perimeters or internal angles of the shadows. Non-generic directions are excluded from the count classification, although they have probability zero. The normal-incidence identity is exact; the tests do not by themselves certify infinitely many tetrahedra or directions. Literature searches and full-text comparisons are not a proof of absolute historical novelty; a less-indexed classical discussion of truncated-polyhedron silhouettes could contain an equivalent statement. No independent mathematical audit has been performed.

## References
1. D. V. Feldman and D. A. Klain, *Angles as probabilities*, arXiv:0809.3459v1, 19 September 2008, Theorem 1 and the discussion after it. https://arxiv.org/abs/0809.3459
2. M. Al-Ajmi, M. Koca and H. Bait Bu Salasel, *Projection of Polyhedra onto Coxeter Planes Described with Quaternions*, Sultan Qaboos University Journal for Science **19** (2014/2015), 77--90, especially the truncated-tetrahedron example and Table 2. DOI:10.24200/squjs.vol19iss2pp77-90.
3. A. E. Black and F. Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936v1, 11 June 2024, especially Theorems 1.1 and 1.5. https://arxiv.org/abs/2406.06936
4. *Area-weighted silhouette probabilities of arbitrary tetrahedra*, publicly accessible research record, 11 October 2026. The unweighted tetrahedral triangular-shadow probability is acknowledged there as earlier work.
