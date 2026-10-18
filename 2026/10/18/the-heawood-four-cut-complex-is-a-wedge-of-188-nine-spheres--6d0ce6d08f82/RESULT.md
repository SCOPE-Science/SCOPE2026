# The Heawood four-cut complex is a wedge of 188 nine-spheres

## Finding

Let \(H\) be the Heawood graph, the point–line incidence graph of the Fano plane. Its ordinary four-cut simplicial complex has the exact integral homotopy type

\[
\boxed{\Delta_4(H)\simeq\bigvee^{188}S^9.}
\]

The complex has exactly \(903\) facets of dimension \(9\) and contains the complete \(8\)-skeleton of the simplex on its fourteen graph vertices. A fully specified acyclic discrete-Morse matching leaves exactly \(188\) critical nine-dimensional faces and no other critical faces in the reduced augmented matching. Thus, in particular, \(\widetilde H_9(\Delta_4(H);\mathbb Z)\cong\mathbb Z^{188}\), and every other reduced integral homology group vanishes.

## Assumptions and scope

All graphs are finite, undirected and simple. Label the seven point vertices \(p_0,\ldots,p_6\), and label the seven line vertices \(\ell_0,\ldots,\ell_6\). Indices are taken modulo \(7\). Declare \(p_i\) adjacent to \(\ell_j\) exactly when \(i-j\in\{0,1,3\}\). This gives the cubic, bipartite, girth-six Heawood graph \(H\).

For an arbitrary graph \(G=(V,E)\), its *ordinary* \(k\)-cut complex \(\Delta_k(G)\) has as facets the complements \(V\setminus S\) of exactly those \(k\)-vertex subsets \(S\subseteq V\) whose induced graph \(G[S]\) is disconnected. Faces include the empty set. This construction is different from the total cut complex. The claim concerns exactly the graph \(H\) and parameter \(k=4\); it makes no assertion for arbitrary incidence graphs or other cut parameters.

For reproducibility, index the points by \(0,\ldots,6\) and lines by \(7,\ldots,13\), with \(\ell_j\) represented by vertex \(7+j\). A face is encoded by a fourteen-bit nonnegative integer whose set bits indicate its vertices.

## Proof

**1. Identify all facets.** Every connected induced subgraph on four vertices is a tree, since the girth of \(H\) is six. The only four-vertex trees are a claw and a three-edge path. Each of the fourteen vertices is the center of one induced claw because \(H\) is cubic and triangle-free. Every induced three-edge path is counted twice by its two orientations. There are

\[
\frac{14\cdot3\cdot2\cdot2}{2}=84
\]

such paths, since the girth-six condition forbids a repeated vertex or a chord. Thus exactly \(14+84=98\) four-subsets induce connected subgraphs. Among the \(\binom{14}{4}=1001\) four-subsets, exactly \(1001-98=903\) give disconnected induced graphs. Their ten-vertex complements are distinct facets of \(\Delta_4(H)\), so the complex is pure of dimension \(9\).

**2. Identify the lower skeleton.** Any induced subgraph on five vertices is a forest, because the girth is six. If a five-vertex forest is connected, delete any vertex of degree at least two; the remaining four vertices induce a disconnected graph. If it is already disconnected, delete a vertex without destroying all but one component. In either case, every five-vertex subset contains a disconnected four-vertex subset. Consequently every subset of at most nine vertices is a face of \(\Delta_4(H)\). Its face numbers, indexed by dimension from \(-1\) through \(9\), are

\[
(1,14,91,364,1001,2002,3003,3432,3003,2002,903).
\]

There are \(15816\) faces in total, including the empty face.

**3. Give and verify the acyclic matching.** Work on the full augmented face poset, including the empty face. Begin with every face unmatched. For each vertex \(v=0,1,\ldots,13\), pair *simultaneously* every currently unmatched face \(F\) not containing \(v\) with \(F\cup\{v\}\), provided both faces remain unmatched. Remove both members of every new pair before proceeding to the next vertex. Because each pair changes a single vertex, every pair is a covering relation in the face poset.

The exhaustive certificate `artifacts/verify.py` reconstructs every one of the \(15816\) faces, performs this matching, and verifies that the unmatched set consists of exactly \(188\) faces, all of cardinality ten. It checks acyclicity by orienting every unmatched Hasse cover downward and every matched cover upward, then applying a topological sort to the entire resulting directed graph. Exactly \(108416\) oriented cover relations are generated, and the topological sort visits all \(15816\) faces. Consequently there is no directed cycle, so the matching is acyclic. Its critical-face count is an exact finite certificate, not a sample or a probabilistic test.

**4. Deduce the homotopy type.** By discrete Morse theory, an acyclic matching of the augmented face poset yields a reduced CW model with one cell corresponding to each unmatched face; the matching of the empty simplex is interpreted as choosing a basepoint in the ordinary CW realization. There are no unmatched faces except the \(188\) nine-dimensional ones. Adjoin the basepoint to obtain a CW model with a single zero-cell and \(188\) nine-cells, and no cells in intermediate dimensions. Every nine-cell therefore has its attaching map into the zero-cell and is attached trivially. The model is the wedge of \(188\) copies of \(S^9\), proving the claimed homotopy equivalence and integral homology groups.

## Verification

Run `python3 artifacts/verify.py` from the directory containing the supplied files. It checks the point–line incidence graph, all \(1001\) four-subsets and their induced connectivity, all \(903\) facets, all face numbers and all covering relations, every matching pair and critical face, and the complete directed-acyclicity certificate. The output concludes `VERIFY_OK` and reports \(188\) critical nine-cells.

As an independent chain-level check, run `python3 artifacts/verify_mod2.py`. This program constructs the graph and cut complex afresh, builds all augmented simplicial boundary matrices, and performs Gaussian elimination over \(\mathbb F_2\) without referring to the discrete-Morse matching. Its only nonzero reduced Betti number is \(\widetilde\beta_9=188\), and the output concludes `MOD2_VERIFY_OK`. The mod-two calculation is corroborating evidence, not a substitute for the all-faces acyclic matching establishing integral homotopy type.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced and studied ordinary cut complexes, including homotopy classifications for trees, cycles, multipartite graphs, squared cycles and certain prisms; see [1], especially the definitions and the classification table. Those results give the governing construction and methods but do not contain the Heawood graph's ordinary four-cut homotopy type. Results about *total* cut complexes concern a different complex when the cut parameter is greater than two; they do not determine this result.

The new mathematical content is the exact Heawood four-cut classification together with an exhaustive, independently replayable discrete-Morse certificate. General results saying that a pure shellable complex is a wedge of top-dimensional spheres do not imply this classification without a shellability proof, which is neither needed nor asserted here.

## Limitations

The result is confined to the Heawood graph and cut parameter four. It does not determine the automorphism representation on top homology, shellability, other cut parameters, or any larger family of incidence graphs. The certificate is an exhaustive finite computation; its output must not be extrapolated to graphs of unbounded order. Mathematical correctness of the integer encoding and acyclicity criterion is explained in the proof, and the complete implementations are included rather than relying on a log alone.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public 26 April 2023), https://arxiv.org/abs/2304.13675 ; SIAM Journal on Discrete Mathematics **38** (2024), 1630–1675.
2. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145 (standard acyclic-matching/CW model theorem).
