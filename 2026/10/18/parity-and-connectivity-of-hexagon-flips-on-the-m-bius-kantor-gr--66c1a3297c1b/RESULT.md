# Parity and connectivity of hexagon flips on the Möbius–Kantor graph
## Finding
Let \(G=GP(8,3)\), the cubic bipartite Möbius–Kantor graph on sixteen vertices. The *six-cycle flip graph* \(\mathcal F_6(G)\) has one vertex for each perfect matching of \(G\), with two distinct matchings adjacent exactly when their symmetric difference is the edge set of a simple six-cycle. Then \(\mathcal F_6(G)\) has **33 vertices, 96 edges, and precisely four connected components**, one of order \(30\) and three isolated vertices. The nontrivial component has diameter \(4\), with 24 vertices of degree \(6\) and six of degree \(8\). The three isolated matchings are pairwise edge-disjoint and together partition all 24 edges of \(G\).

There is an exact reachability criterion. Choose either fixed ordered bipartition \((L,R)\) of size eight each and assign to each perfect matching \(M\) the sign \(\sigma(M)\) of its matching permutation from \(L\) to \(R\). For the explicit orders given below, there are exactly three sign-positive and thirty sign-negative matchings. **Two perfect matchings are joined by a sequence of six-cycle flips if and only if they are identical or both have negative sign.** All distinct negative-sign matchings are connected by at most four flips. The names of the two parity classes may exchange under reordering the bipartition; the partition and reachability statement do not.

## Assumptions and scope
The graph has labeled vertices \(u_i,v_i\), \(i\in\mathbb Z/8\mathbb Z\), and undirected edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\), with indices taken modulo eight. A perfect matching contains eight mutually vertex-disjoint edges covering all sixteen vertices. Six-cycle means *every* simple cycle of length six in the abstract graph, not merely the faces of one selected surface embedding. No longer even cycles or unions of cycles are allowed in a single flip.

For a concrete sign normalization, set \(L=(0,2,4,6,9,11,13,15)\) and \(R=(1,3,5,7,8,10,12,14)\), where \(u_i=i\) and \(v_i=8+i\). Map the matched neighbor of the \(i\)-th left vertex to its zero-based position in \(R\); the sign is \((-1)\) to the number of inversions of that resulting permutation.

Equivalently, the graph is the bipartite circulant with left/right vertices indexed by \(\mathbb Z/8\mathbb Z\) and biadjacency matrix \(B_{ij}=1\) exactly for \(j-i\in\{0,1,3\}\) modulo eight. This is the Haar-graph representation established by Marušič and Pisanski [1]; their \(H(133)\) symbol uses three offsets equivalent to these under a cyclic translation. With the natural increasing index orders in this representation, positive and negative have the same respective multiplicities \(3\) and \(30\).

## Proof
First, toggling an alternating six-cycle in a bipartite perfect matching changes the matching permutation by a three-cycle on the three participating left vertices. A three-cycle is an even permutation, so \(\sigma\) is invariant under every permitted flip.

Second, consider the circulant biadjacency matrix \(B\). Its permanent counts perfect matchings and its determinant is the signed sum of the same permutations. Direct exact integer arithmetic gives \(\operatorname{per}(B)=33\) and \(\det(B)=-27\). Let \(n_+\) and \(n_-\) count positive and negative terms. Solving \(n_++n_-=33\), \(n_+-n_-=-27\) yields \(n_+=3\), \(n_-=30\). The permanent is obtained by the explicit eight-row subset recurrence in `verify_circulant.py`; the determinant is computed with integer Bareiss elimination. Both are independently checked by direct enumeration of all valid permutations in the same file.

The three positive permutations in the increasing circulant-coordinate orders are
\[
\begin{split}
&(0,1,2,3,4,5,6,7),\\
&(1,4,3,6,5,0,7,2),\\
&(3,2,5,4,7,6,1,0).
\end{split}
\]
Every pair of these permutations differs in all eight positions. Their edge sets are pairwise disjoint and exhaust the three allowed choices in every row, so they form a one-factorization. A six-cycle flip can change only three matching assignments; hence these three positive matchings cannot flip to each other. Parity preservation prevents flipping to a negative matching, proving that all three are isolated.

It remains to establish connectivity within the thirty negative matchings and the exact size and diameter of their flip graph. This is a finite exhaustive claim with a fully constructive certificate, not an extrapolation from experiments. For each nonempty set \(S\) of unmatched vertices, choose its least vertex \(v\); every perfect matching must match \(v\) to exactly one neighbor \(w\in S\). Recursing over all such choices produces each perfect matching exactly once. The supplied edge-mask verifier implements this complete branching argument. A separate depth-first enumeration lists *every* simple six-cycle by growing six distinct adjacent vertices and checking the closing edge; it deduplicates by the resulting six-edge mask. The result is precisely \(33\) perfect matchings and \(24\) different six-cycles. For each matching \(M\) and six-cycle \(C\), an allowed switch exists if and only if \(|M\cap E(C)|=3\), in which case the unique result is \(M\mathbin\triangle E(C)\). Exhausting these finitely many options produces the entire undirected flip adjacency relation, with \(96\) edges.

The complete 33-row adjacency certificate in `hexagon_flip_certificate.json` is checked entry-by-entry by `verify_cycle_masks.py`. Its complete graph search yields component orders \(30,1,1,1\), the stated degree distribution, and a largest finite shortest-path distance of exactly four in the thirty-vertex component. Since the three positive matchings are already proved isolated, this certifies connectivity of the entire negative-sign class, and the reachability criterion follows. The second verifier does not enumerate graph cycles: it generates all admissible bipartite matching permutations and joins two when they disagree in exactly three positions. Such a disagreement necessarily consists of one alternating six-cycle, and conversely every six-cycle flip changes exactly three positions. This independent criterion yields the identical complete adjacency relation. A third verifier derives the same component counts directly from the circulant representation and checks the permanent and determinant.

## Verification
Run from a directory containing the four filenames:

`python3 verify_cycle_masks.py hexagon_flip_certificate.json`

`python3 verify_bipartite_permutations.py hexagon_flip_certificate.json`

`python3 verify_circulant.py`

These programs use only the Python standard library. The first re-enumerates the graph and checks all 33 matching masks, 24 cycle masks, 33 adjacency rows, parity signs, component lists, isolated-matching edge partition, degree counts, and exact diameter against the JSON certificate. The second re-enumerates the bipartite permutations without cycle enumeration and compares the entire edge relation against the same certificate, while independently determining the component structure and diameter. The third constructs the equivalent circulant from scratch and rederives the counting equations and flip components. The algorithms have no assumptions about unvisited matching configurations: the branching and permutation loops are exhaustive over their finite specified domains.

## Relationship to prior work
Marušič and Pisanski [1] provide the standard \(GP(8,3)\) model, its Haar-graph representation, and its toroidal hexagonal embeddings; this establishes the object but not a perfect-matching flip classification. Lijnen and Ceulemans [2] study symmetry types of cellular embeddings of this same graph. Their accessible abstract does not settle the unrestricted six-cycle matching-reconfiguration problem, but the inaccessible body remains a priority risk. The complete matching count of \(33\) is previously recorded in a matching-polynomial study [3] and is not a novelty claim. Earlier resonance-graph results for nanotubes [4] and recent toroidal polyhexes [5] concern **facial** hexagons of fixed embeddings. Here the move set contains every one of the twenty-four abstract six-cycles, so those facial connectivity criteria do not directly yield the present complete adjacency graph. The parity argument itself is elementary and not claimed as a new general lemma; the graph-specific sufficiency on the negative class and isolation/diameter classification are the assessed contribution.

## Limitations
The result is only for the 16-vertex Möbius–Kantor graph and six-cycle moves. It neither asserts analogous connectivity in other cubic bipartite graphs nor determines transition rates or mixing times. The six-cycle flip graph is not the standard resonance graph of a single fixed embedding. The finite classification has reproducible complete enumerators but no independent mathematical audit. Published embedding classifications and unindexed matching tables could contain overlapping information; the full text of [2] was not available for a decisive whole-document comparison, and this risk should be assessed before any external novelty assertion.

## References
[1] D. Marušič and T. Pisanski, *The remarkable generalized Petersen graph \(G(8,3)\)*, Mathematica Slovaca 50 (2000), 117–121. https://dml.cz/bitstream/handle/10338.dmlcz/133137/MathSlov_50-2000-2_1.pdf

[2] E. Lijnen and A. Ceulemans, *Oriented 2-cell embeddings of a graph and their symmetry classification: generating algorithms and case study of the Möbius–Kantor graph*, Journal of Chemical Information and Computer Sciences 44 (2004), 1552–1564, https://doi.org/10.1021/ci049865c (public online date August 18, 2004).

[3] K. Balasubramanian, *Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions*, Symmetry 17 (2025), article 133. https://doi.org/10.3390/sym17010133

[4] N. Tratnik and P. Žigert Pleteršek, *Some properties of carbon nanotubes and their resonance graphs*, MATCH Communications in Mathematical and in Computer Chemistry 74 (2015), 175–186. https://www.researchgate.net/publication/282279418_Some_properties_of_carbon_nanotubes_and_their_resonance_graphs

[5] L. Liang and H. Zhang, *The resonance graphs of nanotubes and toroidal polyhexes*, arXiv:2609.19766 (2026). https://arxiv.org/abs/2609.19766
