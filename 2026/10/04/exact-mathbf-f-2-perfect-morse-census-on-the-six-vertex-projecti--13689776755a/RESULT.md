# Exact \(\mathbf F_2\)-perfect Morse census on the six-vertex projective plane
## Finding
Let \(K\) be the standard six-vertex triangulation of \(\mathbb{RP}^2\) with facets `012`, `014`, `023`, `035`, `045`, `125`, `134`, `135`, `234`, and `245`. Exactly \(428{,}400\) acyclic Hasse matchings on \(K\) have discrete Morse vector \((1,1,1)\); equivalently, exactly \(428{,}400\) discrete gradient vector fields on this triangulation are \(\mathbf F_2\)-perfect.

After forgetting the critical vertex and critical triangle, these fields are in bijection with \(7{,}140\) tree-cotree decompositions. Among the \(1{,}296\) spanning trees of the complete one-skeleton, the complementary dual graph is always connected and unicyclic. Its unique cycle has length \(5\), \(6\), or \(9\), for exactly \(726\), \(540\), or \(30\) spanning trees respectively. Consequently the number of compatible dual spanning trees is
\[
726\cdot 5+540\cdot 6+30\cdot 9=7{,}140.
\]
Each tree-cotree decomposition has \(6\) choices of critical vertex and \(10\) choices of critical triangle, giving
\[
7{,}140\cdot 6\cdot 10=428{,}400.
\]
Each of the \(15\) edges is the critical edge in exactly \(28{,}560\) of these fields.
## Assumptions and scope
A discrete gradient vector field is understood as an acyclic matching on the face-poset Hasse diagram. A field is called \(\mathbf F_2\)-perfect when its critical-cell counts equal the mod-two Betti numbers. The claim concerns the displayed standard six-vertex triangulation only, although that triangulation is combinatorially unique among six-vertex triangulations of \(\mathbb{RP}^2\).

The facet list is the standard one used in the boundary-matrix example of Joswig, Lofano, Lutz, and Tsuruga. The one-skeleton is \(K_6\), there are \(15\) edges and \(10\) triangles, and every edge belongs to exactly two triangles.
## Proof
Because \(K\) is a connected closed triangulated surface and \(\chi(K)=6-15+10=1\), mod-two Poincaré duality gives \(b_0=b_2=1\), and then \(b_1=b_0+b_2-\chi=1\). Thus an \(\mathbf F_2\)-perfect field has exactly one critical vertex, one critical edge, and one critical triangle.

Consider first its vertex-edge pairs. There are exactly five such pairs. The five matched edges cannot contain an undirected cycle. Indeed, a cycle avoiding the critical vertex would force every cycle vertex to be paired to a cycle edge, producing a closed gradient path; a cycle containing the critical vertex would have more cycle edges than matchable noncritical cycle vertices. Hence the five matched edges form a spanning tree \(T\) of the six-vertex one-skeleton. Conversely, once \(T\) and the critical vertex are fixed, orienting \(T\) toward that vertex gives a unique acyclic vertex-edge matching.

The same argument in the dual graph applies to edge-triangle pairs. There are nine such pairs, and their dual edges form a spanning tree \(C^*\) on the ten triangles, rooted at the critical triangle. No primal edge can occur both in \(T\) and in the edge-triangle matching. Hence every perfect field determines a tree-cotree decomposition
\[
E(K)=T\sqcup L\sqcup C,
\]
where \(|T|=5\), \(|C|=9\), and the single leftover edge \(L\) is the critical edge. Conversely, any such decomposition, together with a root vertex and a root triangle, determines an acyclic matching with critical vector \((1,1,1)\). This establishes a bijection.

It remains to count the tree-cotree decompositions. The complete graph \(K_6\) has \(6^{4}=1{,}296\) spanning trees. For each spanning tree \(T\), deleting the five corresponding edges from the dual graph leaves ten dual edges on ten dual vertices. Exhaustive Prüfer enumeration verifies that this graph is always connected, hence unicyclic. A connected unicyclic graph has exactly as many spanning trees as the length of its unique cycle. The exact cycle-length distribution is \(726\) cases of length \(5\), \(540\) cases of length \(6\), and \(30\) cases of length \(9\). The displayed sum therefore gives \(7{,}140\) tree-cotree decompositions and \(428{,}400\) rooted fields.

Finally, direct tallying gives \(476\) tree-cotree decompositions for each possible leftover edge. Independently, the simplicial automorphism group has order \(60\) and is transitive on the \(15\) edges, so uniformity is forced. Multiplying \(476\) by the \(60\) root choices gives \(28{,}560\) perfect fields per critical edge.
## Verification
The standalone script `verify.py` reconstructs the facet list, dual incidences, all \(1{,}296\) Prüfer spanning trees, the complementary dual graphs, their unique cycle lengths, all compatible dual spanning trees, the leftover-edge tally, and the full simplicial automorphism group. It checks the exact histogram
\[
(\ell,N_\ell)=(5,726),(6,540),(9,30),
\]
the totals \(7{,}140\) and \(428{,}400\), the uniform leftover-edge count \(476\), and the automorphism-group order \(60\).

The computation is finite and exhaustive for this triangulation. The mathematical bijection between perfect gradient fields and rooted tree-cotree decompositions is proved above; the computation is used only for the exact finite census.
## Relationship to prior work
Forman's discrete Morse theory identifies acyclic Hasse matchings with discrete gradient data and explicitly exhibits a projective-plane vector field with one critical cell in each dimension. Joswig, Lofano, Lutz, and Tsuruga use the standard six-vertex triangulation \(\mathbb{RP}^2_6\), state that the vector \((1,1,1)\) is \(\mathbf F_2\)-perfect, and display one such matching together with the boundary matrices. Lutz records the combinatorial uniqueness of the six-vertex triangulation. Eppstein's tree-cotree framework supplies the general primal/dual spanning-tree viewpoint for graphs embedded on surfaces.

The inspected sources establish existence and the general decomposition mechanism, but they do not give an exact census of all \(\mathbf F_2\)-perfect acyclic matchings on \(\mathbb{RP}^2_6\), the \(5/6/9\) complementary-cycle distribution, or the count per critical edge.
## Limitations
The exact numbers are specific to the standard six-vertex triangulation. No claim is made about larger triangulations of \(\mathbb{RP}^2\), about counts of real-valued discrete Morse functions inducing a given field, or about coefficient fields other than \(\mathbf F_2\). A later source could contain an unindexed exact census not found in the searches reported in the review.
## References
1. R. Forman, *A User's Guide to Discrete Morse Theory*, Séminaire Lotharingien de Combinatoire B48c (2002).
2. D. Eppstein, *Dynamic Generators of Topologically Embedded Graphs*, arXiv:cs/0207082 (2002).
3. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Combinatorial Manifolds*, arXiv:math/0506372v1 (2005).
4. M. Joswig, D. Lofano, F. H. Lutz, and M. Tsuruga, *Frontiers of Sphere Recognition in Practice*, arXiv:1405.3848v1 (2014).
