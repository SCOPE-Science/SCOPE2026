# The Nauru independence complex is \(\bigvee^4 S^5\vee S^6\)

## Finding
Let \(G=GP(12,5)\) be the Nauru graph. Its vertices are \(u_i,v_i\), with indices \(i\in\mathbb Z/12\mathbb Z\), and its edges are \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+5}\). For the ordinary simplicial independence complex of this graph, there is an integral homotopy equivalence
\[
\operatorname{Ind}(G)\simeq\bigvee^4 S^5\vee S^6.
\]
In particular, the only nonzero reduced integral homology groups are \(\widetilde H_5\cong\mathbb Z^4\) and \(\widetilde H_6\cong\mathbb Z\).

## Assumptions and scope
The graph is precisely the simple, undirected 24-vertex, 36-edge generalized Petersen graph \(GP(12,5)\), also called the Nauru graph or the order-four permutation star graph. Its independence complex has a simplex for each independent subset of graph vertices; the empty subset is included in the augmented combinatorial face poset. No assertion is made for the family of all generalized Petersen graphs, other permutation star graphs, or equivariant homotopy types. The result is an integral ordinary homotopy equivalence rather than merely a statement about homology groups.

## Proof
Number the graph vertices \(u_0,\ldots,u_{11},v_0,\ldots,v_{11}\) as \(0,\ldots,23\). Exhaustive independent-subset enumeration by the explicit edge formulas gives 35,219 faces, including the empty face, and the following nonempty face counts in dimensions \(0\) through \(11\):
\[
(24,240,1304,4212,8328,10036,7176,2964,752,156,24,2).
\]

Work on the augmented face poset. Initially every face is unmatched. For each vertex \(x\) in increasing numerical order, pair every still-unmatched face \(\sigma\) missing \(x\) with \(\sigma\cup\{x\}\), provided this coface is still unmatched. Delete both from further matching stages. The supplied verifier reconstructs exactly 17,605 disjoint cover pairs; all faces except six 5-simplices and three 6-simplices are paired, including the empty face.

Orient each codimension-one inclusion downwards, except that matched inclusions are oriented upwards. The verifier constructs every one of the 205,680 directed incidences and checks that the resulting directed graph admits a topological ordering of all 35,219 faces. The matching is therefore acyclic. The reduced discrete-Morse reduction yields an ordinary CW model with one 0-cell, six 5-cells and three 6-cells, and no other cells.

For the signed integral attaching-degree calculation, orient all simplices by increasing vertex labels. In the sorted critical-face bases, the verifier recursively eliminates every matched degree-five/six pair using its incidence coefficient \(+1\) or \(-1\). This produces the integer Morse boundary matrix, with six rows and three columns,
\[
\partial_6=\begin{pmatrix}
1&1&0\\
0&0&0\\
0&0&0\\
1&0&-1\\
1&0&-1\\
0&0&0
\end{pmatrix}.
\]
Its first column equals its second minus its third. The minor using rows one and four, and columns two and three (with one-based indexing), has determinant \(-1\). Therefore its image is a primitive free rank-two subgroup of \(\mathbb Z^6\), and its Smith normal form has precisely two unit invariant factors.

The 5-skeleton of this Morse CW model is \(\bigvee^6 S^5\). Homotopy classes of maps from \(S^5\) into this wedge are classified by their degree vectors, since \(\pi_5(\bigvee^6 S^5)\cong\mathbb Z^6\). A change of cellular bases by unimodular integer matrices is realized by homotopy equivalences of these wedges and by changing the attaching-cell basis. The two primitive attachments thus cancel two five-sphere summands, while the remaining 6-cell attaches trivially. This leaves \(\bigvee^4 S^5\vee S^6\), proving the asserted homotopy equivalence, not merely the integral homology statement.

## Verification
The standalone standard-library programs `verify_nauru.py` and `check_nauru_mod2.py` have no external runtime dependencies. Execute `python3 verify_nauru.py` to re-enumerate the 35,219 faces, reproduce the toggle matching and exact critical cells, topologically sort all 205,680 directed incidences, reconstruct the signed integer Morse matrix by matching-pair elimination and check its unimodular rank-two minor. Successful replay prints `NAURU_INTEGER_VERIFY_OK`.

Execute `python3 check_nauru_mod2.py` for a separate include/exclude enumeration and an all-degree mod-two simplicial boundary-rank calculation. The boundary ranks in degrees zero through eleven (degree zero includes the reduced augmentation) are
\[
(1,23,217,1087,3125,5203,4829,2346,618,134,22,2).
\]
The only nonzero reduced mod-two Betti numbers are four in degree five and one in degree six, agreeing with the integral Morse decomposition; this mod-two calculation alone would not prove torsion-freeness or a homotopy equivalence.

## Relationship to prior work
Barmak's 2010 star-cluster/suspension theorem shows, in particular, that an independence complex of a triangle-free graph is a suspension. It does not identify the Nauru graph's exact homotopy type, integral attaching maps or sphere multiplicities. Tsukuda's incidence-graph/Alexander-dual reduction applies to bipartite incidence graphs but leaves a separate finite homotopy calculation necessary for the Nauru graph. Nilakantan and Shukla classify a particular cyclic-neighborhood regular bipartite family whose relevant cubic examples contain four-cycles, whereas \(GP(12,5)\) has girth six. Agarwal and Basak treat Möbius and circular ladder graphs, not this generalized Petersen graph.

Published calculations of the independence complexes of the dodecahedral graph \(GP(10,2)\) and the Heawood graph yield different complexes: they do not contain the present classification as a corollary. Searches using the Nauru, generalized Petersen and permutation-star aliases, and comparisons to these exact neighboring results, revealed no covering statement. That limited evidence does not prove absence of a differently phrased or unindexed earlier solution.

## Limitations
This is an exhaustive finite, graph-specific computational proof. The signed attaching-degree matrix follows a deterministic elimination from the complete signed face incidences; the verification package, rather than an abbreviated closed-form manual enumeration, certifies those finite steps. It does not produce an equivariant or simple-homotopy classification of all graph families. An equivalent calculation in inaccessible or unindexed literature remains a residual originality risk. Independent review has not been performed.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, publicly submitted 2010-07-02; primary MSC 57M15. https://arxiv.org/abs/1007.0418
2. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), DOI:10.55016/ojs/cdm.v12i1.62277. https://cdm.ucalgary.ca/article/download/62277/46773/178118
3. N. Nilakantan and S. Shukla, *Homotopy type of the independence complexes of a family of regular bipartite graphs*, arXiv:1709.04789. https://arxiv.org/abs/1709.04789
4. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2, revised 2026-09-14. https://arxiv.org/abs/2608.30601
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
