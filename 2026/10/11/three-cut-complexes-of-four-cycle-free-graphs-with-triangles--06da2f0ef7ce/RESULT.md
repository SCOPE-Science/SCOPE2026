# Three-cut complexes of four-cycle-free graphs with triangles

## Finding
For every finite simple graph \(G\) with \(n\ge7\) vertices, at least one triangle, and no four-cycle (whether induced or not), write \(\Delta_3(G)\) for the ordinary three-cut complex. Its facets are the complements of disconnected induced triples. If \(d(v)\) is the degree of \(v\) and \(t(G)\) counts triangles, then
\[
\Delta_3(G)\simeq \bigvee^{\beta(G)} S^{n-4},\quad
\beta(G)=\binom{n-1}{2}-\sum_{v\in V(G)}\binom{d(v)}{2}+2t(G).
\]
The empty wedge means a contractible complex. In particular, all its integral reduced homology groups are free and vanish outside degree \(n-4\).

## Assumptions and scope
A four-cycle means any cycle of four distinct vertices, even one with chords. The graph need not be connected or regular. The hypothesis of at least one triangle makes the asserted family disjoint from earlier triangle-free classifications. The vertex lower bound guarantees \(n-4\ge3\), permitting the homotopy conclusion via standard simply connected CW methods. The complex is not the *total* three-cut complex: an induced triple with exactly one edge is disconnected and therefore contributes a facet.

Let \(B=\Delta_3(G)^\vee\) be the combinatorial Alexander dual on the same \(n\)-element ground set, with \(B=\{U\subseteq V(G):V(G)\setminus U\notin\Delta_3(G)\}\). Then \(U\in B\) if and only if \(U\) contains no disconnected induced triple. In particular, all vertices and edges belong to \(B\), and a triple is a two-face precisely if it induces a path on three vertices or a triangle.

## Proof
**No faces above dimension two.** Suppose four vertices induce a graph in which every triple is connected. Each vertex has at least two neighbors among the other three: a vertex with zero or one neighbor would be isolated in the triple consisting of it and the two vertices other than its possible single neighbor. A graph on four vertices of minimum degree at least two has a four-cycle (a four-vertex cycle itself, a triangle joined to the remaining vertex at two vertices, or a denser graph). This contradicts the hypothesis. Therefore \(B\) has no three-simplices, and no higher simplices by downward closure. It has the complete one-skeleton.

**Elementary collapses.** Enumerate all two-faces of \(B\) that induce paths on three vertices. In such a triple, the two endpoints are nonadjacent. Their unordered pair belongs to no other two-face: another common neighbor would create a four-cycle. Thus the endpoint pair is a free one-face, and the path triangle can be deleted together with that edge by an elementary simplicial collapse. All such deletions can be made in any order, because the designated private edges are distinct. Afterwards only the two-faces inducing graph triangles remain. Two different graph triangles cannot share an edge, since two common third vertices would form a four-cycle. Therefore each remaining two-face has a free edge, and it too collapses. The resulting one-dimensional complex \(R\) is connected, because elementary collapses preserve homotopy and the original \(B\) contains the complete one-skeleton.

**Rank.** Denote by \(p(G)\) the number of induced paths on three vertices. Counting length-two wedges at their centers and subtracting the three wedges in each triangle gives
\[p(G)=\sum_v\binom{d(v)}{2}-3t(G).\]
The collapse removes one edge for each of the \(p(G)+t(G)\) two-faces. Thus \(R\) is a connected graph on \(n\) vertices with \(\binom n2-p(G)-t(G)\) edges. It follows that
\[B\simeq R\simeq\bigvee^{\binom{n-1}{2}-p(G)-t(G)}S^1
=\bigvee^{\beta(G)}S^1.\]
This is an integral simplicial-collapse statement, not a rational approximation. It also proves that \(\beta(G)\ge0\).

**Alexander duality and homotopy type.** Combinatorial Alexander duality gives
\[\widetilde H_i(\Delta_3(G);\mathbb Z)\cong
\widetilde H^{n-i-3}(B;\mathbb Z).\]
Hence the unique potentially nonzero reduced homology is free of rank \(\beta(G)\) in degree \(n-4\). Because \(B\) has dimension two, every subset of at most \(n-4\) vertices is a face of \(\Delta_3(G)\); the latter has the entire \((n-5)\)-skeleton of the simplex. It has dimension exactly \(n-4\): a disconnected triple exists, since otherwise any four-vertex set would contradict the preceding four-cycle lemma. The full skeleton makes it \((n-6)\)-connected. As \(n-4\ge3\), the vanishing of next-to-top homology, together with Hurewicz, makes it \((n-5)\)-connected. Representatives of a basis for top homology define a map from a wedge of \(\beta(G)\) spheres of dimension \(n-4\); it is a homology isomorphism between simply connected CW complexes and hence a homotopy equivalence by Whitehead. If \(\beta(G)=0\), the complex is contractible by the same argument.

## Verification
The accompanying self-contained Python checker reconstructs \(B\) directly from graph edges, verifies that no four-set supports a higher face, executes all prescribed free-edge collapses, and confirms the Euler-rank formula. It covers triangle necklaces with three through six triangle blocks and the truncated tetrahedral graph. For the latter it also independently builds the original three-cut complex from disconnected triples and computes its complete mod-two Betti numbers; the sole nonzero reduced Betti number is \(27\) in dimension \(8\). Run `python3 verify_squarefree_threecut.py` and require the last line `VERIFY_OK`. These examples test the construction, but the unrestricted theorem follows from the symbolic collapses and duality, not the finite checks.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue introduced and developed the ordinary cut complexes. Their classification of chordal-graph shellability and their general face-lattice/Euler-characteristic results provide context, but do not state the displayed four-cycle-free, triangle-allowing homotopy formula. Their results for complete multipartite graphs, paths, cycles, and clique prisms do not imply this uniform extension. A previously established classification for graphs with neither triangles nor four-cycles has a different hypothesis and does not imply the case of a graph containing a triangle. The essential new step here is the consecutive collapse of path-triangle faces using unique nonedge endpoint pairs, followed by disjoint-edge triangle faces.

## Limitations
No homotopy conclusion is asserted for graphs having a four-cycle. In that setting, endpoint pairs can have multiple common neighbors, and four-vertex faces of the dual can occur, invalidating the collapse proof. This result does not assert shellability or a group representation. The literature comparison rules out identified covering results, not unknown or inaccessible equivalent formulations; independent assessment has not been performed.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public 2023-04-26), DOI 10.1137/23M1569034. The definition, Section 6 face lattice, and Sections 7 family comparisons are used.
2. A. Björner, *Topological Methods*, in *Handbook of Combinatorics*, for elementary simplicial collapses and wedge-space methods.
3. Standard combinatorial Alexander duality and Hurewicz–Whitehead theorems, as formulated in algebraic topology texts.
