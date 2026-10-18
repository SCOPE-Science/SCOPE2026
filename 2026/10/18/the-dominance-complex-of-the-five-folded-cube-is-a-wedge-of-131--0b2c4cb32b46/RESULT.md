# The dominance complex of the five-folded cube is a wedge of 131 nine-spheres

## Finding
Let \(C\) be the degree-five Clebsch graph (the folded five-cube), in the explicit sixteen-vertex Cayley presentation below. Its **dominance complex** \(\mathcal D(C)\), consisting of vertex subsets whose complements dominate \(C\), has the integral homotopy type
\[
\boxed{\mathcal D(C)\simeq\bigvee^{131}S^9.}
\]
In particular, its reduced integral homology is \(\mathbb Z^{131}\) in degree nine and zero in every other degree, and its fundamental group is trivial. This is a statement about the degree-five graph, **not** the ten-regular graph sometimes also called the Clebsch graph.

## Assumptions and scope
Let the vertex set be \(V=\mathbb F_2^4\), represented by integers \(0,1,\ldots,15\) with four binary digits. Distinct \(u,v\in V\) are adjacent exactly when \(u\oplus v\in\{1,2,4,8,15\}\), where \(\oplus\) denotes bitwise XOR. This graph has degree five and strongly regular parameters \((16,5,0,2)\); the accompanying checker verifies these parameters directly. It is the antipodal quotient of the ordinary five-dimensional cube.

For \(S\subseteq V\), define \(S\in\mathcal D(C)\) exactly when \(V\setminus S\) is a dominating set: every \(v\in V\) lies in \(V\setminus S\) or is adjacent to a vertex of \(V\setminus S\). Equivalently, \(S\) must contain no closed neighborhood \(N_C[v]=\{v\}\cup N_C(v)\) in its entirety. This includes the empty simplex in the abstract complex. The statement concerns the finite complex for this single graph, with ordinary geometric realization and integral homotopy equivalence.

## Proof
Encode subsets \(S\subseteq V\) by integers from \(0\) to \(65535\), using bit \(v\) to record membership of the vertex \(v\). Since each closed neighborhood \(N_C[v]\) is a six-element subset, membership in \(\mathcal D(C)\) is the exact finite predicate
\[
\forall v\in V:\quad N_C[v]\not\subseteq S.
\]
An exhaustive sweep of all \(65536\) masks gives \(53731\) faces including the empty face, hence \(53730\) nonempty faces. Its face vector in dimensions zero through eleven is
\[
(16,120,560,1820,4368,7992,11280,12150,9520,4768,1056,80).
\]
There are no higher-dimensional faces. A second implementation of face membership tests whether \(V\setminus S\) directly dominates every graph vertex; it agrees on **every** mask, not just on selected examples.

Construct a matching on the nonempty-face poset in stages, with pivot vertices \(0,1,\ldots,15\). Initially every nonempty face is unmatched. At pivot \(v\), for every still-unmatched face \(S\) not containing \(v\), pair \(S\) with \(S\cup\{v\}\) if both are currently unmatched, and remove both from the unmatched set. Process faces by increasing integer mask at each stage. These are legitimate, pairwise disjoint Hasse covers. The exact stage-pair counts are
\[
(25068,1054,314,223,61,31,11,0,23,10,4,0,0,0,0,0),
\]
for a total of \(26799\) matched pairs. The complete list is in `evidence/matching_pairs.tsv`; all surviving critical faces are in `evidence/critical_faces.txt`. The critical faces consist of precisely the vertex \(\{0\}\) and \(131\) faces of cardinality ten (dimension nine).

To verify the essential acyclicity claim, orient **every** Hasse cover of the nonempty face poset from its larger face to its smaller face, except reverse each matched cover. The standalone code constructs all \(401088\) such directed incidences. It performs Kahn's topological-sorting algorithm and removes all \(53730\) vertices, certifying that the full directed Hasse graph is acyclic. This is an exhaustive finite certificate: neither sampling nor a heuristic assumption of acyclicity is involved. The actual input certificate lists and reconstructed pairs are also checked for exact agreement.

By Forman's discrete Morse theorem, the complex is homotopy equivalent to a CW complex having exactly one zero-cell and \(131\) nine-cells, with no cells in intervening dimensions. Every nine-cell therefore attaches by the constant map to that unique zero-cell; the resulting CW complex is \(\bigvee^{131}S^9\). This establishes the claimed **integral homotopy type**, rather than merely rational homology or an Euler-characteristic calculation.

## Verification
Extract the supplied files preserving the `evidence/` subdirectory and run `python3 evidence/verify_dominance.py`. This needs Python 3.10+ and no third-party packages. It checks the graph, two independent descriptions of every face, full face vector, exact pair certificate, disjointness and cover conditions, critical-cell vector, and all directed Hasse edges by a complete topological sort. Its expected output is recorded in `evidence/verification_output.txt`. The face vector independently gives reduced Euler characteristic \(-131\), consistent with \(131\) odd-dimensional spheres. The executable proof uses all \(65536\) vertex masks and includes no probabilistic or finite-sample extrapolation.

## Relationship to prior work
Matsushita and Wakatsuki's 2023 paper establishes the general identification between graph dominance complexes and Alexander duals of the **complement graph's** open-neighborhood complexes. Its worked homotopy calculations concern cycles and path products, not the degree-five Clebsch graph or the rank \(131\) classification here. Matsushita's earlier vertex-cover bound applies to arbitrary graphs but does not determine this homotopy type. Ehrenborg and Hetyei classify dominance complexes of forests; the Clebsch graph is not a forest or a chordal graph.

Existing calculations of the Clebsch graph's **ordinary independence** and **ordinary open-neighborhood** complexes concern other functors. In particular, a calculation of \(\mathcal N(C)\) does not settle \(\mathcal D(C)\) through Matsushita–Wakatsuki duality, which involves \(\mathcal N(\overline C)\), not \(\mathcal N(C)\). A review of indexed equivalent and broader claims did not identify this exact homotopy classification. This is not a proof that no unindexed equivalent calculation exists.

## Limitations
The result is an exact classification of one canonical graph complex; it does not assert a formula for all folded cubes, strongly regular graphs, or all dominance complexes. The proof depends on the fully reproducible finite matching and Hasse-DAG computation, together with the standard discrete-Morse theorem. Neither a symmetry representation nor an independent mathematical audit is supplied. Prior-art checks reduce but cannot eliminate the risk of unindexed equivalent literature.

## References
1. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639, first submitted 2023-12-05. https://arxiv.org/abs/2312.02639
2. T. Matsushita, *Dominance complexes and vertex cover numbers of graphs*, arXiv:2009.04145, first submitted 2020-09-09. https://arxiv.org/abs/2009.04145
3. R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, European Journal of Combinatorics 27 (2006), 906–923. https://doi.org/10.1016/j.ejc.2005.04.010
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
5. E. W. Weisstein, *Clebsch Graph*, MathWorld (for the graph's standard isomorphism descriptions). https://mathworld.wolfram.com/ClebschGraph.html
