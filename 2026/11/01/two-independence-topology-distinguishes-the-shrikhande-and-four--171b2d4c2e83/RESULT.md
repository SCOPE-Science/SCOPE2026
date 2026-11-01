# Two-independence topology distinguishes the Shrikhande and four-by-four rook graphs

## Finding
For the Shrikhande graph \(S\) and the \(4\times4\) rook graph \(R=K_4\mathbin{\square}K_4\), their higher-independence complexes at cutoff two satisfy the integral homotopy equivalences
\[
\operatorname{Ind}_2(R)\simeq\bigvee^{105}S^3,
\qquad
\operatorname{Ind}_2(S)\simeq\bigvee^{57}S^3.
\]
Both graphs are nonisomorphic strongly regular graphs with the same parameters \((16,6,2,2)\), and both complexes have the same numbers of vertices, edges and two-dimensional faces, namely \((16,120,384)\). Nevertheless their reduced integral third Betti numbers differ by \(48\), and their integral homology is torsion-free and concentrated in degree three.

## Assumptions and scope
For any finite simple graph \(G\), the higher-independence complex \(\operatorname{Ind}_2(G)\) is the simplicial complex on \(V(G)\) whose faces are vertex sets \(U\) for which every connected component of the induced graph \(G[U]\) has at most two vertices. The empty set is included as a face for enumeration but not as an ordinary cell in the geometric realization. No other graph or cutoff is covered by the theorem.

Index each vertex by \(4a+b\), with \(a,b\in\{0,1,2,3\}\). In \(R\), two distinct vertices are adjacent when their first or second coordinates agree. In \(S\), distinct vertices \((a,b)\) and \((c,d)\) are adjacent exactly when \((c-a,d-b)\) modulo four belongs to \(\{(\pm1,0),(0,\pm1),(1,1),(-1,-1)\}\). Both are six-regular on sixteen vertices, with two common neighbors for every distinct pair. The neighborhood induced subgraph is two disjoint triangles in \(R\) and a six-cycle in \(S\), so they are nonisomorphic.

A subset fails the cutoff-two condition precisely if it contains some connected induced triple. This follows because every connected graph on at least three vertices contains a connected three-vertex induced subgraph: choose three consecutive vertices along a simple path or two neighbors of one vertex. A triple is connected if and only if at least two of its three possible edges occur. Each graph has exactly \(176\) forbidden triples. Thus the complex is an explicitly specified finite face poset of subsets of the sixteen vertices; enumeration checks all \(2^{16}=65536\) subsets per graph.

## Proof
**Exact face construction.** The provided standalone verifier constructs each graph from the defining coordinate rule and checks both the forbidden-triple and independent connected-component definitions of each face for every subset. The augmented face vectors, ordered by dimension \(-1,0,1,\ldots\), are
\[
R:(1,16,120,384,528,144),\qquad
S:(1,16,120,384,544,240,32).
\]
Accordingly there are \(1192\) and \(1336\) nonempty faces. The same count \(176\) of forbidden triples, and hence the identical two-skeleton face counts, follows independently from these data.

**Explicit acyclic matchings.** On each poset of nonempty faces run this deterministic matching algorithm. For \(v=0,1,\ldots,15\) in that order, visit the currently unmatched faces in ascending integer bitmask order; whenever \(v\notin F\) and both \(F\) and \(F\cup\{v\}\) are still unmatched, pair them, removing both from subsequent stages. This gives \(542\) matched cover pairs for \(R\) and \(638\) for \(S\). The unmatched faces are exactly one zero-cell, one two-cell, and respectively \(106\) and \(58\) three-cells; the lone two-cell bitmasks are \(44\) and \(82\). Orient every nonmatched covering incidence from the larger face to the smaller, and every matched one in reverse. Direct topological sorting of *all* \(4224\) and \(4960\) oriented nonempty-face incidences visits every face, proving the directed Hasse graphs acyclic. Thus these are legitimate acyclic matchings in Forman's discrete-Morse theorem and provide CW models with precisely these critical cells.

**Exact integral Morse differential.** Order every oriented simplex by increasing vertex index. Its signed simplicial boundary has the usual alternating deletion signs. The sole potentially nonzero Morse cellular differential is \(\partial_3\) from the critical three-cells to the one critical two-cell; there are no critical one-cells or cells above dimension three. In the checker `morse_boundary_3_to_2`, an unmatched two-face \(f\) paired upward with a three-face \(t\) is eliminated through the unit-coefficient relation \(\partial t=0\) in the corresponding chain contraction. Its projection to the critical two-cell is computed recursively from all other two-faces in \(\partial t\). A two-face paired downward with a one-face projects to zero, and the critical two-face projects to one. Since the matching is acyclic, these recursions terminate and compute the exact signed Morse differential, not merely mod-two ranks.

For \(R\), the \(106\) integer coefficients are \(-1\) eight times, \(0\) eighty-two times, and \(+1\) sixteen times. For \(S\), the \(58\) integer coefficients are \(-1\) ten times, \(0\) forty-three times, and \(+1\) five times. In particular, the respective critical three-faces with integer bitmasks \(360\) and \(340\) each have attaching degree \(+1\) to the unique two-cell. These calculations are independently reproducible from the complete enumerated face posets and matching rule.

**Homotopy conclusion.** Each Morse CW complex starts with one zero-cell and a two-cell attached to that point, so its two-skeleton is \(S^2\). Attach one three-cell with degree \(+1\); the resulting CW subcomplex is the mapping cone of a degree-one self-map of \(S^2\), hence is contractible. Every remaining three-cell attaches along a map from \(S^2\) to this contractible subcomplex and therefore attaches nullhomotopically. The CW complex is consequently a wedge of one three-sphere for each remaining three-cell: \(106-1=105\) for \(R\) and \(58-1=57\) for \(S\). This proves the claimed integral homotopy equivalences and excludes all integral torsion; the conclusion does not infer homotopy type from Betti numbers alone.

## Verification
Use Python 3 with only the standard library. Execute `python3 verify_two_independence.py` in a directory containing that self-contained file. It reconstructs both graphs, tests all \(65536\) vertex subsets for each, independently checks the graph-component and connected-triple face predicates, verifies the full directed Hasse orientations and topological sorts, and computes the exact integral Morse differentials described in the proof. A separate direct mod-two simplicial-boundary elimination gives ranks \((15,105,279,144)\) for \(R\) and \((15,105,279,208,32)\) for \(S\). The resulting mod-two Betti numbers are \(105\) and \(57\) in dimension three, and zero in other positive dimensions. The complete machine-readable output is `verification_output.json`; its final marker is `SHRIKHANDE_ROOK_TWO_INDEPENDENCE_OK`.

## Relationship to prior work
Deshpande and Singh [1] introduced a systematic homotopy study of higher-independence complexes and classified several graph families; neither of these two strongly regular graphs belongs to those computed families. Abdelmalek and collaborators [2] investigate chordal graphs, trees and related classes; both graphs here have induced four-cycles and are not chordal. Subsequent Alexander-dual and co-connected results [3] do not state this pair's integral homotopy types; the pair is not among their listed covered grid/chordal families.

An earlier exact computation [4] distinguishes the *ordinary* independence complexes of these same two graphs: \(\operatorname{Ind}(S)\simeq\bigvee^{23}S^2\) and \(\operatorname{Ind}(R)\simeq\bigvee^{15}S^2\). These are cutoff-one complexes, not the cutoff-two objects computed here. The two-matching complex \(M_2(K_{4,4})\) studied in [5] is also different: it allows selected graph edges of degree at most two at every vertex, whereas the cutoff-two complex of the line graph requires every connected component of selected edges to contain at most two edges. The former has \(7342\) nonempty faces versus \(1192\) for the latter. Similarly, an ordinary three-cut complex of the rook graph is not the Alexander dual of its cutoff-two independence complex: that dual instead corresponds to the three-cut complex on the *complement* of the rook graph. Comparison of those distinct objects does not cover this theorem.

## Limitations
This is a complete classification for two specifically presented finite graphs, not an all-strongly-regular-graph theorem. It does not assert their first known topological distinction or analyze the entire higher-independence filtration. The exhaustive certificate is finite but checks the full stated domain; the structural deduction uses Forman's theorem and ordinary CW attaching maps. The literature searches, full prior-computation readings and relevant primary-paper sections disclosed below do not prove absolute bibliographic uniqueness. There has been no independent mathematical audit of the new result.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v1, first public January 15, 2020; https://arxiv.org/abs/2001.05448.
2. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863v1, first public June 21, 2021; https://arxiv.org/abs/2106.10863.
3. P. Deshpande, A. Roy and R. Sawant, *The complex of \(r\)-co-connected subgraphs, chordality and Fröberg's theorem*, arXiv:2510.25710, https://arxiv.org/abs/2510.25710.
4. *Independence complexes of the Shrikhande and \(4\times4\) rook graphs have different sphere-wedge homotopy types*, public primary result and reproducibility files (October 11, 2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187.
5. *The two-matching complex of \(K_{4,4}\) is a wedge of fifteen five-spheres*, public primary result and reproducibility files (October 11, 2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-two-matching-complex-of-k-4-4-is-a-wedge-of-fifteen-five-sph--915eed6b65e5.
6. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
