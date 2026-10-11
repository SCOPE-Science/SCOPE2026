# Edge-orbit matching-complex homotopy of the truncated tetrahedron

## Finding
Let \(G\) be the edge graph of the truncated tetrahedron, defined explicitly below. Its ordinary matching complex has the integral homotopy type
\[
\mathcal M(G)\simeq\bigvee^{22}S^3.
\]
Moreover its graph edges have two orbits. For each *triangular edge* \(e=\{u,v\}\),
\[
\mathcal M(G-e)\simeq\bigvee^{14}S^3,\qquad
\mathcal M(G-\{u,v\})\simeq\bigvee^{8}S^2;
\]
for each *reversal edge* \(e=\{u,v\}\),
\[
\mathcal M(G-e)\simeq\bigvee^{20}S^3,\qquad
\mathcal M(G-\{u,v\})\simeq\bigvee^{2}S^2.
\]
For every edge, the natural matching-complex deletion/link cofibration therefore splits as
\[
\mathcal M(G)\simeq\mathcal M(G-e)\vee\Sigma\mathcal M(G-\{u,v\}).
\]
The assertions are homotopy equivalences over the integers, not solely homology identities.

## Assumptions and scope
Use the finite simple graph with vertex set
\[
V(G)=\{(a,b):a,b\in\{0,1,2,3\},\ a\ne b\}.
\]
Distinct vertices \((a,b)\) and \((c,d)\) are adjacent exactly when \(a=c\), or when \((c,d)=(b,a)\). Thus there are twelve vertices, eighteen edges, twelve edges inside the four disjoint triangles sharing a first coordinate, and six edges joining opposite ordered pairs. This graph is also the line graph of the graph obtained by subdividing every edge of \(K_4\) once, and is the standard truncated-tetrahedral graph. Under permutation of four symbols the triangle edges form one orbit and the reversal edges a second orbit.

A matching is any subset of graph edges with no two sharing a graph vertex. The ordinary matching complex \(\mathcal M(H)\) is the abstract simplicial complex of all matchings in \(H\); its geometric realization is intended. In \(H-e\) only the one graph edge is removed; in \(H-\{u,v\}\) its two endpoint vertices and incident graph edges are removed. No assumptions on orientability, coefficients or field are made.

## Proof
**Finite reconstruction.** Order the twelve graph vertices lexicographically as ordered pairs, and order its eighteen unordered edges lexicographically by their endpoint indices. Identify each face of \(\mathcal M(G)\) with the bit mask recording its graph edges. Starting with the empty mask, for each graph edge add it to precisely those existing matchings whose graph vertices are not incident to it. This exhaustive recursion yields \(1009\) nonempty simplices with face vector, by simplex dimension,
\[
(18,117,332,390,144,8).
\]
The two orbit representatives are chosen as the first respective graph edge in that deterministic lexicographic edge order. Face deletion excludes masks containing this edge. The simplicial link consists of those masks containing the edge with its bit erased, exactly \(\mathcal M(G-\{u,v\})\).

**Acyclic matching certificate.** For each of these five simplicial complexes (full; triangular-edge deletion and link; reversal-edge deletion and link), process edge-bit indices in ascending order. At each index pair every currently unmatched face not containing the bit with its one-bit augmentation, if both faces remain unmatched. The augmented empty face is initially paired with a singleton, but, on returning to the ordinary nonaugmented face poset, that singleton is retained as the single critical vertex. All other matching pairs are nonempty-face covering relations. Reverse their arrows in the ordinary Hasse diagram, directing every other covering relation from coface to face. A complete topological-sort calculation of this finite directed graph finds all vertices, certifying that no closed gradient path exists.

The exhaustive certificate counts are:

| Complex | Nonempty faces | Matching pairs | Critical cells | Directed Hasse incidences |
| --- | ---: | ---: | --- | ---: |
| \(\mathcal M(G)\) | 1009 | 493 | one \(0\)-cell; 22 \(3\)-cells | 3558 |
| Triangular \(\mathcal M(G-e)\) | 819 | 402 | one \(0\)-cell; 14 \(3\)-cells | 2844 |
| Triangular \(\mathcal M(G-\{u,v\})\) | 189 | 90 | one \(0\)-cell; 8 \(2\)-cells | 512 |
| Reversal \(\mathcal M(G-e)\) | 793 | 386 | one \(0\)-cell; 20 \(3\)-cells | 2722 |
| Reversal \(\mathcal M(G-\{u,v\})\) | 215 | 106 | one \(0\)-cell; 2 \(2\)-cells | 608 |

Forman's discrete Morse theorem converts each matching into a CW homotopy model with precisely these cells. In a CW complex having only one zero-cell and cells in a single dimension at least two, the attaching spheres map to a point (there are no positive-dimensional lower cells), so the CW space is a wedge of spheres in that dimension. This proves all five displayed integral homotopy classifications for the chosen representatives. Every permutation of the four symbols is a graph automorphism, and its action is transitive separately on the twelve triangular edges and six reversal edges. Thus they hold for every edge in the corresponding orbit.

**Splitting.** Let \(e=\{u,v\}\). In the matching complex, the deletion of the vertex corresponding to \(e\) is \(\mathcal M(G-e)\), and its link is \(\mathcal M(G-\{u,v\})\). The simplicial decomposition into deletion and star yields the homotopy cofibration of the link inclusion into the deletion. For both orbits, the link is a wedge of \(2\)-spheres whereas the deletion is a wedge of \(3\)-spheres. Because a wedge of \(3\)-spheres is \(2\)-connected, **every** map from the link to the deletion is nullhomotopic. Its homotopy cofiber is the displayed wedge with the suspended link. In the two cases this gives \(14+8=22\) and \(20+2=22\) three-spheres, respectively, consistently with the direct Morse model.

## Verification
Run `python3 verify_truncated_tetra.py` using only the Python standard library. It constructs the graph, enumerates every matching, certifies pair disjointness and acyclicity on every covering relation, and checks critical-cell dimensions and counts for all five complexes. Its success marker is `VERIFY_OK`; the complete simplex/critical-cell counts and deterministically computed matching digests are printed.

Run `python3 verify_alternate.py` independently. It builds the graph as the line graph of once-subdivided \(K_4\), enumerates matchings by a different recursion, calculates all mod-two boundary ranks and reduces homology for each of the five complexes. Its success marker is `INDEPENDENT_VERIFY_OK` and its reduced Betti numbers are respectively \(22\) in dimension \(3\); \(14\) in dimension \(3\); \(8\) in dimension \(2\); \(20\) in dimension \(3\); and \(2\) in dimension \(2\). The first program, not these mod-two checks, establishes the integral homotopy equivalences.

## Relationship to prior work
Engström's *Independence complexes of claw-free graphs* (arXiv:math/0512420) establishes connectivity methods for this class but does not compute this exact polyhedral matching complex. Barmak's *Star clusters in independence complexes of graphs* (arXiv:1007.0418) develops general homotopy tools, not the five explicit decompositions above. Bayer, Jelić Milutinović, and Vega's *General polygonal line tilings and their matching complexes* (arXiv:2211.12559) concerns strings of edge-sharing cycles, unlike the four vertex-disjoint triangles in \(G\). Their *Matching Complexes of Outerplanar Graphs* (arXiv:2411.04601) proves a sphere-wedge theorem for outerplanar graphs, not this graph. Indeed contracting each of the four disjoint triangles of \(G\) to one vertex gives a \(K_4\) minor; therefore \(G\) is not outerplanar. Their paper proposes the broader planar wedge-of-spheres question, for which this is one specific positive example. Indexed comparisons under the truncated-tetrahedron, edge-orbit, once-subdivided complete-graph, and line-graph descriptions revealed no stronger covering calculation; such searches cannot establish absolute priority.

## Limitations
This is an exact finite computation with an exhaustive, replayable combinatorial certificate. It applies to the stated twelve-vertex graph only. It does not establish the planar matching-complex conjecture, an infinite-family theorem, or publication priority. Possible equivalent unpublished or unindexed calculations remain a bibliographic risk. No independent external mathematical audit has been performed.

## References
1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420 (first public version 2005-12-17), https://arxiv.org/abs/math/0512420.
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418, https://arxiv.org/abs/1007.0418.
3. M. Bayer, M. Jelić Milutinović, and J. Vega, *General polygonal line tilings and their matching complexes*, arXiv:2211.12559, https://arxiv.org/abs/2211.12559.
4. M. Bayer, M. Jelić Milutinović, and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, https://arxiv.org/abs/2411.04601.
