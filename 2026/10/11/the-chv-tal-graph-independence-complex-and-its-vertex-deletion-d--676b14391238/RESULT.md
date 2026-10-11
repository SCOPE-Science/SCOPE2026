# The Chvátal graph independence complex and its vertex-deletion dichotomy

## Finding

Let \(G\) be the twelve-vertex Chvátal graph with the explicit edge list in `verify_chvatal.py`. Let \(K=\operatorname{Ind}(G)\) be the ordinary independence complex: a finite set of vertices is a simplex if and only if no pair in the set is an edge of \(G\). For each vertex \(v\), write \(D_v=\operatorname{Ind}(G-v)\) and \(L_v=\operatorname{Ind}(G-N_G[v])=\operatorname{lk}_K(v)\). The two full vertex-automorphism orbits in the displayed labeling are \(A=\{0,1,4,5\}\) and \(B=\{2,3,6,7,8,9,10,11\}\).

**Theorem.** The independence complex is \(K\simeq S^2\). For every \(v\in A\), the deletion \(D_v\) is simplicially collapsible to a vertex and \(L_v\simeq S^1\). For every \(v\in B\), \(D_v\simeq S^2\) and the link \(L_v\) is simplicially collapsible to a vertex. In the latter case the natural inclusion \(D_v\hookrightarrow K\) is a homotopy equivalence. Although \(G\) is four-chromatic and removal of **any** vertex reduces its chromatic number to three, removal affects the independence-complex homotopy type on only one of the two orbits.

## Assumptions and scope

All complexes are ordinary abstract finite simplicial complexes, with all independent subsets included. The complete graph is given by its 24 edges, encoded in `verify_chvatal.py`. In particular the graph is triangle-free and four-regular. The sets \(A\) and \(B\) are labels in this specified graph, not unspecified vertex types. Collapsibility refers to a finite sequence of elementary simplicial collapses; the assertion of homotopy equivalence for \(B\) is about the canonical inclusion, not just the abstract homotopy types. No statement is made for different graphs or higher-dimensional graph families.

## Proof

**1. Exact complex construction.** Enumerate all \(2^{12}-1\) nonempty subsets of the vertex set; keep a subset exactly when it contains no edge from the complete 24-edge list. This procedure gives \(126\) nonempty faces with face vector \((12,42,52,20)\), hence maximal dimension three. For a fixed vertex \(v\), construct \(D_v\) by forbidding \(v\), and \(L_v\) by forbidding the whole closed neighborhood \(N_G[v]\). All 12 deletion/link face counts agree with \(99,26\) for \(v\in A\) and \(98,27\) for \(v\in B\), respectively.

**2. Certified acyclic Morse matchings.** In each complex, toggle an admissible vertex in the prescribed order, matching an unmatched face \(\sigma\) not containing that vertex with \(\sigma\cup\{v\}\) when both remain unmatched. The code builds the **entire** directed Hasse graph, reversing matched incidences, then topologically sorts every directed incidence to establish acyclicity. All counts below refer to nonempty simplices, ordinary face-coface pairs and incidences between nonempty simplices.

| Complex | Nonempty simplices | Pairs | Directed incidences | Critical cells |
| --- | ---: | ---: | ---: | --- |
| \(K\) | 126 | 62 | 320 | one dimension-0, one dimension-2 |
| \(D_0\) | 99 | 49 | 243 | one dimension-0 |
| \(D_2\) | 98 | 48 | 239 | one dimension-0, one dimension-2 |
| \(L_0\) | 26 | 12 | 44 | one dimension-0, one dimension-1 |
| \(L_2\) | 27 | 13 | 47 | one dimension-0 |

The representative \(D_0\) uses pivot order \((5,0,1,2,3,4,6,7,8,9,10,11)\); the other four cases use increasing vertex order. In both one-critical-vertex cases, the verifier additionally **constructs and checks a complete legal free-face collapse sequence** of lengths 49 and 13, ending at the sole critical vertex. Thus \(D_0\) and \(L_2\) are simplicially collapsible, not merely homologically acyclic. Forman's acyclic-matching theorem identifies a CW model with the stated critical cells in the remaining cases. A CW complex with exactly one zero-cell and one \(d\)-cell for \(d\ge 1\), with \(d=1\) or \(2\), is \(S^d\); its attaching map to a point is forced. This proves \(K\simeq S^2\), \(D_2\simeq S^2\), and \(L_0\simeq S^1\).

**3. Exhaustive orbit transfer.** The permutations of labels
\[
(0,4,3,2,1,5,9,8,7,6,11,10),\qquad
(1,0,6,11,5,4,2,9,10,7,8,3)
\]
(listed by images of labels \(0,\ldots,11\)) both preserve every edge. Their generated orbits are exactly \(A\) and \(B\). No automorphism crosses between these sets: the numbers of nonempty simplices in \(D_v\) are 99 and 98 on the two sets, respectively, and deletion cardinality is invariant under graph automorphisms. Transporting the certificates proves the asserted conclusions for **all 12** vertices.

**4. Natural inclusions and chromatic contrast.** The identity \(K=D_v\cup(v*L_v)\), with intersection \(L_v\), describes adding the cone on the link. If \(L_v\) is collapsible, it is contractible, so its inclusion into its cone is a homotopy equivalence and the homotopy gluing lemma for these CW subcomplexes gives \(D_v\hookrightarrow K\) a homotopy equivalence. Finally exact backtracking checks that \(G\) is not three-colorable but is four-colorable, and each \(G-v\) is three-colorable but not two-colorable. This establishes the claimed contrast.

## Verification

Execute `python3 verify_chvatal.py` and `python3 crosscheck_homology.py` with Python 3 and its standard library. The first script enumerates all faces, checks both orbit-generating graph automorphisms, verifies each matching's complete gradient acyclicity, exhibits legal elementary-collapse orders for both collapsible representatives and checks chromatic numbers. The independent second implementation reconstructs the graph from adjacency rows, enumerates faces by combinations, and computes the complete boundary ranks over \(\mathbb F_2\) for \(K\) and **every** \(D_v,L_v\). Both programs terminate with explicit `*_OK` markers. The characteristic-two homology check independently corroborates Betti numbers but **does not** replace the discrete-Morse homotopy proof.

## Relationship to prior work

Barmak's star-cluster/suspension theorem gives a structural suspension result for independence complexes of triangle-free graphs, but does not identify the Chvátal complex as a sphere or classify the homotopy behavior of its twelve vertex deletions. The published characterization of the Chvátal graph by Kitaev and Pyatkin is concerned with semi-transitive orientability, not independence-complex homotopy. Homotopy computations by Goyal, Shukla and Singh treat other specified graph families, not this labeled canonical graph. The new statement adds a complete two-orbit deletion/link dichotomy and explicit collapse certificates.

## Limitations

This is an exact finite graph calculation with independently replayable enumerations and acyclic matching certificates, not an infinite graph-family theorem. The completeness of bibliographic discovery is not claimed: an equivalent result might exist in unindexed or unpublished work. The source date records the earliest verified public version of the cited methodological source, not an asserted publication date of the theorem above.

## References

- J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (first public 2010-07-02), https://arxiv.org/abs/1007.0418.
- S. Kitaev and A. Pyatkin, *On semi-transitive orientability of triangle-free graphs*, arXiv:2003.06204, https://arxiv.org/abs/2003.06204.
- S. Goyal, S. Shukla and A. Singh, *Homotopy type of independence complexes of certain families of graphs*, arXiv:1905.06926, https://arxiv.org/abs/1905.06926.
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, DOI:10.1006/aima.1997.1650.
