# The Heawood two-independence complex is a wedge of thirteen five-spheres

## Finding
For the Heawood graph \(H\), the incidence graph of the Fano plane, the first higher-independence complex has the integral homotopy classification
\[
\operatorname{Ind}_{2}(H)\simeq\bigvee^{13}S^{5}.
\]
In particular, \(\widetilde H_{5}(\operatorname{Ind}_{2}(H);\mathbb Z)\cong\mathbb Z^{13}\), while every other reduced integral homology group is zero. The equivalence follows from an explicit finite acyclic matching of the entire simplicial face poset; it is not inferred merely from finite-field homology.

## Assumptions and scope
Use vertex labels \(0,1,\ldots,13\). The point vertices are \(0,\ldots,6\), the line vertices are \(7,\ldots,13\), and point \(i\) is adjacent to line \(7+j\) if and only if \(i-j\equiv0,1,3\pmod 7\). The differences of the three-element set \(\{0,1,3\}\) exhaust the six nonzero residues exactly once, so these incidences form the Fano projective plane and the graph is Heawood's cubic bipartite graph.

For any finite simple graph \(G\), define \(\operatorname{Ind}_{2}(G)\) as the abstract complex consisting of subsets of \(V(G)\) for which every connected component of the induced subgraph has at most two vertices. Equivalently, every vertex of that induced subgraph has degree at most one. The latter equivalence follows because a finite connected graph on at least three vertices has a vertex of degree at least two. This definition is not the two-matching complex on graph *edges*, and is not the ordinary independence complex.

## Proof
Represent each subset by a 14-bit integer \(s\), with bit \(i\) recording vertex \(i\). Put \(N(i)\) for the neighbor mask of vertex \(i\). The complete face predicate is
\[
 s\in K\quad\Longleftrightarrow\quad
 \forall i\in\{0,\ldots,13\}:\ 
 (i\notin s)\ \text{or}\ \bigl|s\cap N(i)\bigr|\leq1.
\]
Enumerating exactly the 16,384 masks with this predicate gives the complete face vector, in dimensions zero through six,
\[
(14,91,322,651,728,392,58),
\]
and 2,257 faces including the empty face. The face enumeration is exhaustive by construction, not a sample.

Here is a deterministic matching on all *nonempty* faces. Initially mark every nonempty face unmatched. In stages \(i=0,1,\ldots,13\), inspect the currently unmatched faces \(s\) in ascending integer order. Whenever \(i\notin s\) and both \(s\) and \(s\cup\{i\}\) remain unmatched, pair these two faces and remove both from the unmatched set. The resulting set of 1,121 pairs has precisely fourteen unmatched faces, consisting of one vertex and thirteen faces of dimension five.

To verify acyclicity over the *entire* nonempty face poset, orient each codimension-one covering relation from a larger face to a smaller one, reversing exactly those relations belonging to a chosen matching pair. The standalone finite verifier constructs every directed edge, calculates every indegree, and performs a Kahn topological sort. Its assertion that all 2,256 nonempty face vertices are removed proves that this directed Hasse graph is acyclic. This is exactly the finite acyclic-matching condition in discrete Morse theory; it is not an extrapolation from experimental ranks. The program also checks every selected pair consists of valid incident faces and that no face is used twice.

By discrete Morse theory, the finite complex is homotopy equivalent to a CW complex with one cell in dimension zero, thirteen cells in dimension five, and no cells in any other dimension. Since every attaching map of a five-cell has target a point in this CW structure, the CW complex is the wedge of thirteen five-spheres. This proves the stated *integral homotopy equivalence*.

## Verification
Run `python3 VERIFY.py` with Python 3.8 or later; only the standard library is required. `VERIFY_OUTPUT.txt` records the output. The program reconstructs the Fano incidence relation and all simplices, verifies closure under taking faces, reconstructs every matching pair and every directed Hasse incidence, and checks a topological sort of all nonempty faces. The count of critical cells is independently consistent with reduced Euler characteristic \(-13\). A separate direct mod-two boundary-matrix reduction finds boundary ranks \((13,78,244,407,321,58)\) in degrees one through six, giving thirteen reduced fifth-homology generators and none in other degrees. These mod-two calculations are cross-checks; the *integral homotopy conclusion* rests on the acyclic matching.

## Relationship to prior work
The higher-independence construction originates in Salvetti's account of \(d\)-independent graph complexes, publicly catalogued with date 2016-01-25, and is developed by Paolini–Salvetti. Deshpande–Singh (arXiv:2001.05448) classify the higher independence complexes of complete multipartite graphs, fully whiskered graphs, cycles, and perfect rooted trees, with related chordal constructions. These are not the Heawood graph, which has induced six-cycles and is not chordal. The Heawood *ordinary* independence complex and its graph *matching* complexes concern different face predicates; none of their stated homotopy classifications implies the present result. The contribution here is the exact finite integral homotopy type for the first higher-independence complex of the canonical seven-point projective-plane incidence graph.

## Limitations
This establishes one particular graph and the parameter two, not a family theorem for projective planes of arbitrary order. The matching is computationally certified on a 2,256-vertex directed Hasse diagram. No canonical equivariant matching, automorphism representation, shellability assertion, or homotopy classification for higher parameters is claimed. An unindexed equivalent prior calculation could exist, and independent external mathematical verification has not been performed.

## References
1. M. Salvetti, *Some Combinatorial Constructions and Relations with Artin Groups*, Springer INdAM Series (publicly catalogued 2016-01-25), DOI: 10.1007/978-3-319-20155-9_22.
2. G. Paolini and M. Salvetti, *Weighted sheaves and homology of Artin groups*, arXiv:1703.02586, initially posted 2017-03-07; Section 3 treats \(r\)-independence complexes of path graphs.
3. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, initially posted 2020-01-15; see the introduction and Sections 3–5.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
