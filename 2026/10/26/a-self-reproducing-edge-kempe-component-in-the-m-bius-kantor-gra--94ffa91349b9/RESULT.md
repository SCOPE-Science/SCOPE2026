# A self-reproducing edge-Kempe component in the Möbius–Kantor graph

## Finding
Let \(M=GP(8,3)\) be the Möbius–Kantor graph and let \(\mathcal K(M)\) be its reconfiguration graph of proper three-edge-colourings, identified under global permutations of the three colour names. Two distinct colour classes are adjacent when one whole connected alternating bichromatic cycle is switched. There are exactly twenty vertices of \(\mathcal K(M)\), and its complete isomorphism type is
\[
\mathcal K(M)\cong M\sqcup K_{1,3}.
\]
Thus the reconfiguration graph has two components, of orders sixteen and four, with precisely twenty-seven edges. Its large component has radius and diameter four; its small component is a three-leaf star with radius one and diameter two.

The three bichromatic two-factors of each colouring have the following complete cycle-type distribution (all cycle lengths counted in vertices): sixteen colourings have type \((6,10)\) in each of their three factors; three colourings have one factor of type \((8,8)\) and two Hamiltonian factors of type \((16)\); the remaining colouring has three factors of type \((8,8)\). The sixteen colourings of the first type form the copy of \(M\). The sole colouring of the last type is the centre of \(K_{1,3}\), whose three leaves are those of the middle type.

## Assumptions and scope
The fixed graph \(M\) has vertices \(u_i,v_i\) for \(i\in\{0,\ldots,7\}\), with indices modulo eight, and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\). The graph is simple, cubic, bipartite, and has twenty-four edges. A proper three-edge-colouring assigns one of three colours to each edge with all colours distinct around each vertex. A state is the unordered partition of the twenty-four edges into its three eight-edge perfect matchings, **not** an orbit under automorphisms of \(M\). Every switch interchanges two colours along an entire connected component of the subgraph using those two colours, and states are adjacent only when they are distinct after forgetting colour names.

## Proof
**Exhaustive state construction.** Fix the lexicographic ordering of the twenty-four unordered graph edges in `mk_kempe_verify.py`, and represent an edge subset by a twenty-four-bit integer. The first-uncovered-vertex perfect-matching recursion chooses the least uncovered vertex and branches over each edge joining it to another uncovered vertex. Every perfect matching has a unique first chosen edge and unique subsequent branches, so this recursion enumerates every perfect matching without omission. Direct execution of the fully specified finite recursion gives thirty-three perfect matchings. For any two disjoint perfect matchings with masks \(a,b\), the unique third class is the mask \(c=E\setminus(a\cup b)\); accepting this class exactly when it is a perfect matching and sorting the three masks gives precisely twenty distinct states. This is a finite exhaustive proof, not an inference from a partial search.

Independently, a direct edge-by-edge backtracking enumeration fixes colours \(0,1,2\) on the three edges incident to \(u_0\), then assigns colours to all remaining edges subject to properness. Every assignment has a unique representative with these fixed incident colours, since its three colour names occur exactly once there. This second exhaustive construction gives the same twenty unordered matching triples. The complete algorithms are included in the standalone verifier.

**Exhaustive adjacency construction.** In any proper cubic three-edge-colouring, each union of two colour classes is a spanning two-regular subgraph consisting of even cycles. Exchanging those two colours on one connected cycle changes precisely those two matching masks by symmetric difference with that cycle; the third class is unchanged. Performing this construction for all three colour pairs and all their connected components, discarding unchanged unordered triples, produces twenty-seven undirected adjacencies. As a separate exhaustive check, two distinct matching triples are recognized as adjacent precisely when they have one matching in common and a possible correspondence between their two other matchings has identical, nonempty symmetric differences forming one connected cycle. The two adjacency calculations agree exactly. The resulting connected components have sizes sixteen and four; the first is cubic with twenty-four edges, while the second has one degree-three vertex and three degree-one vertices.

**Exact named-graph certificate.** Number the twenty matching triples by sorting their three integer masks lexicographically, starting at index zero. The large component has indices
\[
\{2,3,5,6,7,8,9,10,12,13,14,15,16,17,18,19\}.
\]
An explicit bijection to the sixteen labeled vertices of \(M\), written as `(state index, image index)`, is

`(2,0), (3,8), (5,7), (6,15), (7,3), (8,11), (9,2), (10,1), (12,9), (13,12), (14,13), (15,5), (16,6), (17,14), (18,10), (19,4)`.

Here image indices \(0,\ldots,7\) designate \(u_i\), and \(8,\ldots,15\) designate \(v_i\). Comparing all twenty-four edges under this bijection with the three explicit edge families defining \(M\) gives equality, certifying the graph isomorphism (and all nonadjacencies, since the vertex map is bijective). The other four state indices are \(\{0,1,4,11\}\), with centre 1 and edges \(\{0,1\},\{1,4\},\{1,11\}\). Finally, decomposing the three two-factors at each state gives exactly the cycle-profile counts stated in the finding. Every finite comparison is executable from the supplied source.

## Verification
Run `python3 mk_kempe_verify.py` with Python 3.10 or later; the script uses only the standard library. It reconstructs the graph from the displayed formula, independently enumerates matchings and edge colourings, independently constructs adjacency by switches and by pairwise symmetric differences, verifies the explicit sixteen-vertex isomorphism, checks the star component and all cycle profiles, and calculates the distances. Successful execution ends with `VERIFY_OK` and the enumerated quantities. Because the exhaustive recursions are finite and their branching covers every permitted choice, no probabilistic or incomplete enumeration is used.

## Relationship to prior work
Belcastro and Haas introduced and studied edge-Kempe equivalence in cubic graphs, including equivalence-class counting and families of nonplanar bipartite examples. Their subsequent paper develops the full Kempe-equivalence graph and the normalization that fixes the three colours incident to a vertex. Goedgebeur and Östergård exhaustively tabulated the **numbers** of edge-Kempe classes of cubic graphs through thirty vertices (and bipartite cubic graphs further), so the mere existence of multiple classes, or a class count derived from that census, is not asserted to be new. The finding here is the **complete graph isomorphism** for the particular Möbius–Kantor graph and its exact split between a copy of the original graph and the three-leaf star, together with the exact bichromatic cycle profiles. General component-count tables and general degree identities do not determine this structure.

## Limitations
This is a finite-graph theorem for the specified unlabeled three-colour state model. It does not prove an infinite family statement or a comparable self-reproduction property for other symmetric cubic graphs. Global permutation of colours is factored out, but automorphisms of \(M\) are not; changing this convention changes state and edge counts. The conclusions are exactly reproducible, while priority beyond the inspected literature remains subject to possible unindexed earlier descriptions of this very same reconfiguration graph. No independent external audit has been performed.

## References
1. S.-M. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, first public preprint 2012-09-08, arXiv:1209.1730; subsequently *Discrete Mathematics* 325 (2014), 77–84. https://arxiv.org/abs/1209.1730
2. S.-M. Belcastro and R. Haas, *Edge-Kempe-equivalence graphs of class-1 regular graphs*, *Australasian Journal of Combinatorics* 69(2) (2017), 197–214. https://ajc.maths.uq.edu.au/pdf/69/ajc_v69_p197.pdf
3. J. Goedgebeur and P. R. J. Östergård, *Switching 3-edge-colorings of cubic graphs*, first public preprint 2021-05-04, arXiv:2105.01363; subsequently *Discrete Mathematics* 345 (2022), 112963. https://arxiv.org/abs/2105.01363
