# Cuboctahedral two-independence complex: \(32\) three-spheres and full octahedral symmetry

## Finding
Let \(Q_3\) denote the graph with vertex set \(\{0,1\}^3\), adjacent at Hamming distance one. The cuboctahedral graph is its line graph \(C=L(Q_3)\), with twelve vertices indexed by the twelve edges of \(Q_3\). For each subset \(S\subseteq V(C)\), require every connected component of the induced graph \(C[S]\) to have at most two vertices. The resulting two-independence or dissociation complex satisfies
\[
\operatorname{Ind}_2(C)\simeq\bigvee^{32}S^3.
\]
This is an **integral homotopy** result, not merely a field-homology calculation. In particular, its only nonzero reduced integral homology is \(\widetilde H_3\cong\mathbb Z^{32}\).

There is also a complete rational character for the natural full octahedral automorphism group
\[\operatorname{Aut}(C)\cong (C_2)^3\rtimes S_3.\]
Describe a signed-coordinate permutation by the lengths of its cycles of positive sign-product and its cycles of negative sign-product. The table lists each signed-cycle class, its size, and the trace on \(\widetilde H_3(-;\mathbb Q)\):

| Positive cycle lengths | Negative cycle lengths | Class size | Trace |
|---|---|---:|---:|
| none | 1,1,1 | 1 | 10 |
| none | 1,2 | 6 | -2 |
| none | 3 | 8 | 1 |
| 1 | 1,1 | 3 | 8 |
| 1 | 2 | 6 | 0 |
| 1,1 | 1 | 3 | 2 |
| 1,1,1 | none | 1 | 32 |
| 1,2 | none | 6 | 2 |
| 2 | 1 | 6 | 4 |
| 3 | none | 8 | -1 |

The character sums to \(96\) over all \(48\) automorphisms, hence
\[\dim_{\mathbb Q}\widetilde H_3(\operatorname{Ind}_2(C);\mathbb Q)^{\operatorname{Aut}(C)}=2.\]
The central antipodal map has trace \(10\); its positive and negative eigenspaces have dimensions \(21\) and \(11\), respectively. The orientation-preserving subgroup has a three-dimensional fixed space.

## Assumptions and scope
All graphs are finite, simple, and undirected. The notation \(\operatorname{Ind}_2(G)\) means the complex of vertex subsets inducing components of size at most two. Equivalently, every selected vertex has at most one selected neighbor, or the selected induced subgraph contains no three-vertex path (not necessarily induced). This construction is distinct from the ordinary matching complex and from the complex forbidding only three-cliques.

The proof applies to the specified twelve-vertex graph, with no assertion about higher-dimensional cubes, graph subdivisions, or other Archimedean graphs. The automorphism character is over \(\mathbb Q\); the homotopy and homology conclusions are over \(\mathbb Z\).

## Proof
**1. Exact finite complex.** Encode cube vertices by integers \(0,\ldots,7\), identifying each with its three-bit vector. List all unordered pairs of Hamming distance one in lexicographic order, giving twelve cube edges. Regard these as the twelve vertices of \(C\); two are adjacent in \(C\) precisely when they share an endpoint in \(Q_3\). For every nonempty bitmask \(s\) of length twelve, retain \(s\) if and only if every selected vertex has at most one selected neighbor. This is equivalent to the component condition above; it is hereditary, so precisely defines the simplices.

Exhaustive enumeration of all \(2^{12}-1=4095\) nonempty subsets gives a face vector, in dimensions zero through four, of
\[(12,66,164,177,36),\]
thus \(455\) nonempty faces and Euler characteristic \(-31\).

**2. Discrete-Morse certificate.** On the remaining unmatched nonempty faces, for a vertex index \(v\) pair every available \(\sigma\) not containing \(v\) to \(\sigma\cup\{v\}\), provided both are still unmatched. Choose a vertex maximizing the available number of such pairs, breaking ties by the lowest index. Repeat until no pairs remain. This deterministic operation gives four stages, with vertex-index and pair-count data
\[(0,126),\quad(11,55),\quad(5,15),\quad(8,15).\]
The resulting \(211\) pairs use \(422\) nonempty faces. Exactly \(33\) critical faces remain: one vertex and thirty-two three-simplices; there are none in any other dimension.

Construct the full cover graph of the face poset by linking every nonempty simplex to each nonempty codimension-one face. It has exactly \(1512\) covering relations. Orient each unmatched covering relation from the larger face to the smaller and reverse the \(211\) matched relations. An exhaustive topological sort processes **all \(455\) face-nodes**, proving this directed graph is acyclic. In particular, the matching is an acyclic discrete-Morse matching rather than only a numerical pairing. Forman's discrete Morse theorem therefore produces a CW model with a single zero-cell and precisely thirty-two three-cells, without any other cells. Every three-cell attaches to the zero-skeleton by the unique constant map, so this CW model is a wedge of \(32\) copies of \(S^3\). This establishes the integral homotopy claim.

**3. Full symmetry character.** Every cube automorphism is an affine signed coordinate permutation, specified by \(p\in S_3\) and \(b\in\{0,1\}^3\); the permutation on the twelve cube edges is induced from their endpoints. All \(48\) such maps preserve the complex. Conversely, the eight maximal three-cliques of the cuboctahedral graph correspond to the eight cube vertices and recover their incidence graph \(Q_3\); hence each automorphism of \(C\) comes from a cube automorphism. Thus these are the full automorphism group.

For an automorphism \(g\), a nonempty set \(\sigma\) of vertices contributes only when \(g(\sigma)=\sigma\). Its signed cellular Lefschetz contribution is \((-1)^{\lvert\sigma\rvert-1}\operatorname{sgn}(g\mid_\sigma)\), with the orientation sign computed by the parity of the induced permutation on the sorted vertices of \(\sigma\). Let the sum of these contributions over all nonempty simplices be \(L(g)\). Since the only ordinary rational homology groups are \(H_0\cong\mathbb Q\) and \(H_3\cong\mathbb Q^{32}\),
\[L(g)=1-\operatorname{tr}\big(g\mid H_3\big).\]
The two independent complete enumeration scripts give the class character tabulated above. Averaging its traces proves the two-dimensional fixed subspace, and the central involution's square equal to the identity gives the \(21/11\) eigenspace split. Every character value is obtained by an exact integer sum, not a numerical approximation.

## Verification
Run `python3 verify_cube_line_graph.py` and `python3 verify_coordinate_model.py` using an ordinary Python 3 interpreter. They require only the standard library. Each must exit successfully and exactly reproduce `verification_output_cube.txt` and `verification_output_coordinates.txt`, respectively. The first script validates face inclusion, all critical matching steps, all covering relations, directed acyclicity, independent mod-two boundary ranks, all signed-cycle character values, and invariant dimensions. The second reconstructs the same graph independently from its Euclidean cuboctahedral coordinates, tests components by breadth-first search, checks the face vector and Euler characteristic, then computes the character directly from geometric signed permutations. Their constructions are independent up to the common mathematical definition.

The mod-two boundary ranks in degrees one through four are \((11,55,109,36)\), giving ordinary mod-two Betti ranks \((1,0,0,32,0)\), a consistency check only. The integral wedge follows from the acyclic matching and critical-cell dimensions, not from those mod-two ranks.

## Relationship to prior work
Sawant's 2026 study of higher-independence complexes establishes vertex decomposability for **trees**, and explicitly equates the two-independence construction with the three-vertex-path-free construction. The cuboctahedral graph contains cycles, so the tree theorem does not give its homotopy or symmetry character. Deshpande and Singh's earlier foundational work classifies certain path, cycle, complete multipartite, and tree families rather than this line graph.

Ghosh and Selvaraja study \(\mathsf{CF}_3(G)\), the complex forbidding only three-cliques. Although an earlier recorded calculation addresses \(\mathsf{CF}_3(L(Q_3))\), this is a **different, strictly larger** complex: the cube-edge triple \(\{(0,2),(0,1),(1,3)\}\) induces a three-vertex path in \(L(Q_3)\) but no triangle, so it is permitted by \(\mathsf{CF}_3\) and forbidden by \(\operatorname{Ind}_2\). The previously classified \(\mathsf{CF}_3(L(Q_3))\) has three five-sphere summands, which does not imply this theorem. Published results concerning matching complexes and cut or Čech complexes of this graph also use different face conditions; even when the ground set is the same, their homotopy types do not determine the present one.

## Limitations
This is an exact finite-graph computation with a complete constructive homotopy certificate, not a classification for every cuboctahedral extension or line graph of a hypercube. The symmetry decomposition gives the rational character and dimensions of fixed subspaces; it does not classify the integral automorphism lattice. Searches of the literature and indexed mathematics have not established a universal priority or uniqueness guarantee; undiscovered prior overlap remains a bibliographic risk. The computation and self-review are not an independent external audit.

## References
- Rutuja Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150, publicly posted 2026-05-24; https://arxiv.org/abs/2605.25150 .
- Priyavrat Deshpande and Anurag Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448; https://arxiv.org/abs/2001.05448 .
- Priyavrat Deshpande, Samir Shukla and Anurag Singh, *Distance \(r\)-domination number and \(r\)-independence complexes of graphs*, arXiv:2001.06775; https://arxiv.org/abs/2001.06775 .
- Rakesh Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623, publicly posted 2026-02-10; https://arxiv.org/html/2602.09623v1 .
- Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete-Morse homotopy theorem).
