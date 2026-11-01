# Three integral homology degrees in the bidirected octahedral multipath complex

## Finding
Let \(O=K_{2,2,2}\) be the octahedral graph, with three vertex parts of size two, and let \(D=\overleftrightarrow{O}\) denote its bidirected version. For the ordinary multipath complex \(X(D)\), whose simplices are arc sets forming vertex-disjoint directed paths, the reduced integral homology groups are
\[
\widetilde H_i(X(D);\mathbb Z)\cong
\begin{cases}
\mathbb Z^3 &i=2,\\
\mathbb Z^{92}&i=3,\\
\mathbb Z^{32}&i=4,\\
0&\text{otherwise}.
\end{cases}
\]
There is no integral homology torsion. Moreover, \(X(D)\) is simply connected, so the Hurewicz homomorphism gives \(\pi_2(X(D))\cong\mathbb Z^3\). No assertion is made about the higher homotopy type or a sphere-wedge decomposition.

## Assumptions and scope
The graph has vertex set \(\{0,1,2,3,4,5\}\), with parts \(\{0,1\}\), \(\{2,3\}\), and \(\{4,5\}\). There are precisely the \(24\) directed arcs \((u,v)\) whose endpoints belong to different parts, in lexicographic order. A subset of arcs is a multipath if each vertex has at most one selected outgoing arc and at most one selected incoming arc, and the selected arcs contain no directed cycle. The empty set is included as the augmented simplex, but not as a cell in the geometric realization. In particular, a directed cycle of length two is forbidden. All homology groups above are ordinary reduced simplicial homology with integral coefficients.

## Proof
Every multipath on six vertices has at most five arcs: with six selected arcs, every vertex has indegree and outdegree one, hence the selected directed partial permutation contains a cycle. Thus it suffices to enumerate subsets of sizes zero through five. A second, independent enumeration chooses the set of sources, chooses pairwise distinct targets, rejects any arc joining two vertices of the same part, and excludes all directed cycles. These two exhaustive constructions agree. There are \(1817\) faces including the empty face, with face vector
\[(f_0,f_1,f_2,f_3,f_4)=(24,192,616,744,240).\]
The maximal faces consist of \(240\) four-simplices and \(24\) three-simplices.

Perform the following explicit matching on the nonempty face poset. Process the \(24\) arcs in lexicographic order. At step \(j\), for each as-yet-unmatched face \(\sigma\) not containing arc \(j\), pair it with \(\sigma\cup\{j\}\) if that face also remains unmatched. At each step the pairs are disjoint, and exactly \(835\) pairs result. The remaining critical cells occur with counts \((1,0,12,101,32)\) in dimensions zero through four. To verify acyclicity, reverse all matched cover relations in the Hasse diagram and direct every other cover relation from upper face to lower face. The resulting graph on \(1816\) nonempty faces has \(6408\) cover relations; the executable proof checks that a full topological sort removes all \(1816\) vertices. The matching is therefore an acyclic Forman matching.

For an oriented face with increasing arc indices, use the usual signed simplicial boundary. To compute the integral Morse differential, take a matched lower cell \(\sigma\) with partner \(\tau\), solve the unit-coefficient relation \(\partial\tau=\epsilon\sigma+\sum\epsilon_j\sigma_j\) for \(\sigma\) and recursively substitute; matched upper cells reduce to zero, and critical cells to their generators. Acyclicity makes the recursion finite. The complete signed differential from critical three-cells to critical two-cells has shape \(12\times101\), exactly \(257\) nonzero entries, rank \(9\), and Smith nonzero invariant factors
\[(1,1,1,1,1,1,1,1,1).\]
The entire signed Morse differential from critical four-cells to critical three-cells is the zero \(101\times32\) matrix. All lower Morse differentials vanish for degree reasons. These calculations are reproduced exactly by the accompanying standalone verifier, which constructs the matrices rather than importing precomputed arrays.

It follows from integral discrete Morse theory that the resulting integral chain complex has one degree-zero generator, twelve degree-two generators, 101 degree-three generators and 32 degree-four generators, with the differential just described. The Smith invariant factors show that its degree-two cokernel is free of rank \(3\), while its degree-three kernel is free of rank \(92\); all 32 degree-four generators survive. There is no torsion. The associated CW model has one zero-cell and no one-cells, hence it is simply connected. The degree-two Hurewicz isomorphism then yields \(\pi_2\cong\mathbb Z^3\).

## Verification
Run `python verify.py` with Python 3.10 or later and SymPy installed. The script constructs the entire complex in two different ways, checks the claimed face vector and maximal-facet dimensions, forms the matching, verifies all directed cover relations and global acyclicity, constructs both signed integral Morse differentials, computes Smith normal form over the integers, and independently checks the original simplicial boundary ranks over \(\mathbb F_2\).

The recorded successful checks include `faces_nonempty=1816`, `matched_pairs=835`, `directed_Hasse_incidences=6408`, `critical_counts=(1,0,12,101,32)`, `smith=1^9`, and `morse_D4_101x32_zero`. Independently, the original binary chain boundaries have ranks \((23,169,444,208)\). The reduced Euler characteristic is \(-57=3-92+32\).

## Relationship to prior work
Caputi, Collari, and Smith (2026, arXiv:2601.05670) study multipath complexes of bidirectional paths and cycles, proving connectivity and integral homology formulas for those graph families and discussing the incompleteness of their homotopy classifications. The octahedron is neither a path nor a cycle. The earlier Caputi–Collari–Di Trani–Smith paper (arXiv:2208.04656, 2022) treats certain orientations of complete bipartite graphs, transitive tournaments, paths, polygons, and small oriented grids, with a complete-directed-graph Euler-characteristic formula. Its unidirectionally oriented complete bipartite graphs and complete digraphs do not identify the integral homology of this bidirected proper complete-tripartite graph.

The octahedral graph is also the line graph of the tetrahedron, and its associated complex can be described as the cycle-free rook-placement complex on six labels with the three \(2\times2\) diagonal blocks forbidden. Neither rephrasing changes the calculated chain complex. The result provides the complete integral homology of the smallest balanced complete-tripartite bidirected graph, a natural first multipartite test beyond the bidirectional path/cycle cases.

## Limitations
This theorem computes the full integral homology and the first nontrivial homotopy group for one finite digraph; it does not classify bidirected complete multipartite graphs generally, assert shellability or nonshellability, determine integral symmetry modules, or decide whether the complex is a wedge of spheres. An equivalent calculation in literature not indexed or inspected here remains possible. The computational proof requires running the provided program with a correct Python/SymPy implementation; it does not provide an independent formal verification of the language or algebra library.

## References
1. L. Caputi, C. Collari, and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, first posted 2026-01-09, https://arxiv.org/abs/2601.05670.
2. L. Caputi, C. Collari, S. Di Trani, and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, first posted 2022-08-09; *Mathematika* 70 (2024), e12235, https://arxiv.org/abs/2208.04656.
3. R. Forman, *Morse theory for cell complexes*, *Advances in Mathematics* 134 (1998), 90–145.
