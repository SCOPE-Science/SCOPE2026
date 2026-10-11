# Eleven three-spheres and the symmetric-group character of a four-cut complex

## Finding
Let \(G=J(5,2)=L(K_5)\) denote the triangular graph. Its vertices are the ten two-element subsets of \(\{0,1,2,3,4\}\); two vertices are adjacent precisely when the subsets intersect. For a graph \(H\), the *ordinary* four-cut complex \(\Delta_4(H)\) has one facet \(V(H)\setminus W\) for every four-element vertex subset \(W\) for which the induced graph \(H[W]\) is disconnected.

**Theorem.** The complex \(X=\Delta_4(J(5,2))\) has
\[
X\simeq\bigvee^{11}S^3,\qquad
\widetilde H_i(X;\mathbb Z)=\begin{cases}\mathbb Z^{11},&i=3,\\0,&i\ne3.\end{cases}
\]
It is pure of dimension \(5\) with ten facets and is **not shellable**. The natural \(S_5\)-representation on reduced rational homology satisfies
\[
\widetilde H_3(X;\mathbb Q)
\cong S^{(3,2)}\oplus S^{(2,2,1)}\oplus S^{(1,1,1,1,1)},
\]
where the terms are rational Specht modules. In particular its full \(S_5\)-invariant subspace is zero, while the sign representation occurs once. The character at cycle types \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), respectively, is \((11,-1,3,-1,-1,-1,1)\).

## Assumptions and scope
The graph has exactly five underlying labels. The cut complex is ordinary, defined using *disconnected* four-vertex induced subgraphs, not the total cut complex (which uses independent sets). Its action on simplicial homology permutes the underlying five labels; the representation classification is over \(\mathbb Q\), while the sphere-wedge and additive homology statements are integral. No extrapolation to larger triangular graphs is asserted.

## Proof
**Facet structure.** The complement of \(G\) is the Petersen graph \(KG(5,2)\), in which two two-subsets are adjacent exactly when disjoint. It is triangle-free and has no four-cycles. A disconnected four-vertex induced subgraph in \(G\) produces a complete bipartite graph between its components in the Petersen graph. A \(2+2\) component split would give a four-cycle there, so the split is \(1+3\). The unique isolated vertex is adjacent in the Petersen graph to all three other vertices; as its degree is three, those other vertices are precisely its Petersen neighbors. There are therefore ten such four-sets, indexed by their isolated vertices. On the underlying labels each consists of three edges of a triangle together with the edge on the complementary pair. Its six-vertex complement is the complete set of six cross-edges of the corresponding \(2+3\) partition. Thus exactly ten distinct five-dimensional facets exist.

**Perfect-dimensional discrete Morse model.** Order the ten vertices lexicographically as \((01),(02),(03),(04),(12),(13),(14),(23),(24),(34)\), with indices \(0\) through \(9\). Encode each simplex by a ten-bit integer. Enumerate all subfaces of the ten facets: there are \(371\) faces including the empty face, with numbers by cardinality \((1,10,45,110,135,60,10)\). Begin with every face unmatched, including the empty face. For each element in the fixed order \(9,8,7,6,5,4,3,2,1,0\), pair every still-unmatched simplex not containing that element with its one-element extension if that extension is still unmatched. The resulting matching has \(180\) pairs and \(11\) unpaired four-vertex faces. Remove the pair consisting of the empty simplex and singleton of index \(9\), retaining that singleton as a critical zero-cell. On the ordinary nonempty face poset this leaves exactly \(179\) disjoint matched pairs, one critical zero-cell, and eleven critical three-cells.

To certify acyclicity, orient each cover arrow of the nonempty face poset from higher dimension to lower, except reverse all matched cover arrows. The resulting directed graph has \(370\) nodes, \(1320\) arrows, and admits a complete topological ordering: all \(370\) nodes are removed by indegree-zero elimination. The complete pairing and critical-face list are in `evidence/four_cut_certificate.json`; `evidence/verify_four_cut.py` independently reconstructs them, checks every pair and every arrow, and verifies the DAG. By Forman's discrete Morse theorem, \(X\) is homotopy equivalent to a CW complex with one zero-cell and eleven three-cells, each attached to a point. This proves the claimed wedge of eleven three-spheres and all the integral homology groups, without inferring integral homology merely from characteristic-two computations.

**Equivariant homology.** For each of the \(120\) permutations of the five labels, compute the signed trace on each oriented simplicial chain group: a fixed face contributes the sign of the induced vertex permutation, and a non-fixed face contributes zero. Because the homology is concentrated in degrees zero and three, the Lefschetz trace satisfies \(L(g)=1-\chi_{H_3}(g)\). The exact enumeration yields the seven character values displayed above. Taking character inner products with the rational Specht characters (computed independently by the Frobenius alternant formula) gives multiplicity one for partitions \((3,2)\), \((2,2,1)\), and \((1^5)\), and multiplicity zero for all other partitions of five. This determines the representation. Since reduced homology vanishes outside degree three, the same action is the full reduced homology character.

The complex is pure of dimension five but has nonzero third homology; a pure shellable complex has reduced homology only in top dimension. Hence \(X\) is not shellable.

## Verification
Run `python3 evidence/verify_four_cut.py` with the two embedded evidence files extracted into the indicated common directory. The standard-library verifier rebuilds all ten disconnected quadruples by independent graph connectivity search; checks their equivalence to the ten \(2+3\) cross-edge facets; reconstructs all \(371\) faces, all \(179\) matched pairs, and the complete acyclic directed Hasse graph; and recomputes mod-two boundary ranks \((0,1,9,36,74,50,10)\). As a separate check on the complete character, it evaluates all \(120\) permutations and obtains the Specht decomposition from an exact alternant calculation rather than trusting a pre-entered character table. Successful execution ends with `VERIFY_OK`.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue's *Topology of Cut Complexes of Graphs* (arXiv:2304.13675, originally public April 26, 2023) introduces ordinary cut complexes and studies homology, shellability and named graph families. Its chordal-graph shellability criterion does not apply: \(J(5,2)\) has induced four-cycles. Its published specific graph classifications do not include this four-cut complex. The distinct *Total Cut Complexes of Graphs* (arXiv:2209.13503) uses independent quadruples, not disconnected induced quadruples.

There is also a second natural presentation: \(X\) is the subcomplex of the complex of bipartite graphs on five labeled vertices generated by its ten complete-bipartite \(K_{2,3}\) facets. Linusson and Shareshian's *Complexes of t-Colorable Graphs* (DOI:10.1137/S0895480100366968) treats **all** bipartite graphs and includes five additional maximal four-edge stars; that larger complex is therefore not the complex in this theorem. Its abstract-level homotopy classification does not determine the homotopy type or character of this proper subcomplex. Previous topology of the Petersen two-independence complex likewise concerns a different cut parameter and does not imply the present degree-three homology representation. These are actual differences in statements and coverage, rather than merely differences in names.

## Limitations
The full abstract homotopy type and rational \(S_5\)-module are established; an explicit integral \(\mathbb Z S_5\)-lattice decomposition or equivariant homotopy equivalence is not asserted. A finite exhaustive certificate proves this fixed five-label instance but gives no formula for larger triangular graphs. The literature comparisons cannot exclude an unindexed equivalent theorem. The cited colorable-graph paper's full original text was not available during this comparison; its precise overlap is recorded as a residual literature risk rather than inferred from snippets.

## References
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public April 26, 2023).

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503.

Linusson and Shareshian, *Complexes of t-Colorable Graphs*, SIAM Journal on Discrete Mathematics 16 (2003), 371–389, DOI:10.1137/S0895480100366968.

Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
