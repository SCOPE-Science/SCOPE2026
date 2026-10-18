# A persistent integral two-sphere in the Euclidean Rips filtration of the icosidodecahedral root orbit

## Finding
Let \(\phi=(1+\sqrt5)/2\), and let \(P\) be the set of thirty unit vertices of the regular icosidodecahedron, as explicitly defined below. For the inclusive Euclidean Vietoris–Rips complex \(X_r=\operatorname{VR}_{\le r}(P)\),
\[
X_r\simeq\begin{cases}
\bigsqcup^{30}\mathrm{pt},&0\le r<\sqrt{2-\phi},\\
\bigvee^{11}S^1,&\sqrt{2-\phi}\le r<1,\\
S^2,&1\le r<\sqrt3.
\end{cases}
\]
More strongly, for all \(1\le r<\sqrt3\), the inclusion \(X_1\hookrightarrow X_r\) is a simple-homotopy equivalence. At every new distance level in this interval, the larger complex simplicially collapses onto the *entire included subcomplex* \(X_1\). Consequently, its nonzero integral second-homology generator persists unchanged across the squared-distance levels \(3-\phi\), \(2\), and \(1+\phi\). For every orthogonal symmetry \(g\) of \(P\), the action on this rank-one integral homology is multiplication by \(\det(g)\); these assertions concern the induced homology action, not equivariance of the chosen collapses.

## Assumptions and scope
The metric is the ordinary chordal Euclidean metric, **not** the graph shortest-path metric or circular arc metric. The threshold is *inclusive*. Put \(\phi=(1+\sqrt5)/2\). The vertex set consists of \(\pm e_1,\pm e_2,\pm e_3\) and the twenty-four cyclic coordinate permutations of \((\pm1,\pm\phi,\pm(\phi-1))/2\), with independent choices of the three signs; cyclic means the three even coordinate permutations only. These are thirty distinct points with norm one. A simplex is exactly a nonempty vertex subset of pairwise distance at most \(r\). Homotopy statements are ordinary, integral, and unbased; the first disconnected stage is not a wedge.

## Proof
**Exact distance ring and filtration.** Encode an element \(a+b\phi\in\mathbb Z[\phi]\) by the integer pair \((a,b)\). Use \(\phi^2=\phi+1\) to calculate the squared Euclidean distance between every unordered pair of the thirty vertices exactly. The resulting levels in increasing order are
\[
2-\phi,\ 1,\ 3-\phi,\ 2,\ 1+\phi,\ 3,\ 2+\phi,\ 4,
\]
with multiplicities \(60,60,60,60,60,60,60,15\). These are the *only* points where the simplicial filtration changes.

**Before scale one.** Below the first distance the complex consists of thirty isolated points. At squared-distance \(2-\phi\), it has exactly thirty vertices, sixty edges, and twenty triangles, and no higher faces. Each of its sixty edges belongs to exactly one of the twenty triangles. Delete one chosen edge along with its unique coface triangle for each of the twenty triangles, choosing the least bitmask edge in each triangle. The resulting graph contains all thirty vertices, exactly forty edges, and is connected, as established by a direct exact finite adjacency test. It therefore has first Betti number \(40-30+1=11\) and is homotopy equivalent to a wedge of eleven circles.

**A two-sphere at scale one.** At squared-distance one, maximal simplices are precisely twenty triangles and twelve five-vertex simplices. The sixty edges of the first scale form the usual edge graph of the icosidodecahedron: twenty triangular faces and twelve pentagonal faces. For each five-vertex simplex, retain the three fan triangles triangulating its associated pentagonal face, including all their subfaces. Retain all twenty original triangles. The resulting two-dimensional subcomplex has face vector \((30,84,56)\). Each edge belongs to exactly two triangles, and every vertex link is a single cycle; connectivity is checked on the original thirty-vertex graph. Its Euler characteristic is \(30-84+56=2\), hence it is a connected closed triangulated surface homeomorphic to \(S^2\). An exact certificate of ninety-six elementary free-face pairs collapses the entire scale-one Rips complex onto this surface. Both the surface and its embedding are explicitly reconstructed by the accompanying verifier.

**No change through three further thresholds.** The verifier reconstructs all simplices as subsets of maximal cliques, without floating-point comparisons. In increasing squared-distance order \(3-\phi\), \(2\), and \(1+\phi\), the complexes contain respectively \(1022\), \(3742\), and \(15966\) nonempty simplices; the included \(X_1\) contains \(362\) nonempty simplices. The companion certificate records respectively \(330\), \(1690\), and \(7802\) elementary free-face pairs, removing every simplex outside exactly \(X_1\) and no simplex within it. Each recorded deletion is checked against the *current* complex: the deleted codimension-one face has exactly one immediate coface, its partner; both are outside the protected target. No undecided or extrapolated case remains below squared-distance \(3\). Each relative collapse is a deformation retraction up to simplicial simple homotopy, proving the inclusion-induced isomorphisms throughout \(1\le r<\sqrt3\).

**Symmetry character.** The oriented convex boundary of the icosidodecahedron defines a canonical generator on the explicitly triangulated surface; a pentagonal face may be triangulated in any fan, and changing that fan changes the associated two-cycle by a boundary *inside its five-vertex simplex*. Thus the generator defines a canonical class in \(H_2(X_1;\mathbb Z)\), independent of fan choices. Every orthogonal symmetry of \(P\) maps the oriented polytope boundary to itself with degree \(\det(g)\). The inclusion-induced isomorphisms transport this equality to \(H_2(X_r;\mathbb Z)\) for \(1\le r<\sqrt3\). There are no other positive-degree reduced homology groups in this interval.

## Verification
Run `python verify_h3.py verify collapse_sequences.json` using Python's standard library, from the directory containing the two supplied files. It reconstructs vertices and pairwise squared distances in \(\mathbb Z[\phi]\), enumerates all faces of the four relevant stages, checks the closed surface including all vertex links, and replays every recorded elementary simplicial collapse. Expected output ends in `VERIFY_OK`. The stored sequences are required data, not unverified assertions. All finite checks are exhaustive for this precisely defined thirty-vertex configuration, and the proof explains why the checked collapses entail the asserted integral homotopy statements.

## Relationship to prior work
Adamaszek's *Clique complexes and graph powers* (2011) classifies clique complexes of graph powers and circular configurations, including circle-power sphere phenomena; those objects do not contain the Euclidean thirty-point icosidodecahedral chordal metric as a special case. Adamaszek and collaborators' *Nerve complexes of circular arcs* (2014) and Adamaszek–Adams' *The Vietoris–Rips complexes of a circle* (2015) concern points on a common circle and thus cannot directly determine this noncoplanar point configuration. Baez's *The Icosidodecahedron* describes the geometric thirty-vertex polyhedron and its symmetries but does not compute its Euclidean Rips filtration. The new content here is the exact **relative simplicial-collapse and persistence statement through the three later distance levels**, plus the geometric symmetry character. All cited background results retain their original provenance.

## Limitations
This does **not** classify the complexes at or beyond squared-distance \(3\), nor does it identify the eventual death parameter of the integral two-dimensional persistence class. The supplied collapse sequence is not claimed to be equivariant. The statement does not concern the graph metric, other normalizations of roots, or full persistent homology across subsequent scales. A semantically equivalent computation may exist in literature indexed under different polytope names; originality assessment is subject to that bibliographic uncertainty. No independent scientific audit has been performed.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first public 2011-04-03. https://arxiv.org/abs/1104.0433
2. M. Adamaszek, H. Adams, F. Frick, C. Peterson, C. Previte-Johnson, *Nerve complexes of circular arcs*, arXiv:1410.4336, first public 2014-10-16. https://arxiv.org/abs/1410.4336
3. M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669, first public 2015-03-12. https://arxiv.org/abs/1503.03669
4. J. C. Baez, *The Icosidodecahedron*, arXiv:2309.15774, first public 2023-09-26; supplementary geometric reference, not an archive-qualifying first-source anchor. https://arxiv.org/abs/2309.15774
