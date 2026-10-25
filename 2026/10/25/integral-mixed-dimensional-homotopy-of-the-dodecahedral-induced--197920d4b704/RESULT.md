# Integral mixed-dimensional homotopy of the dodecahedral induced-forest complex

## Finding
Let \(D=GP(10,2)\) be the twenty-vertex dodecahedral graph. The simplicial complex
\[
\mathcal F(D)=\{A\subseteq V(D): D[A]\text{ is a forest}\}
\]
has the **integral homotopy type**
\[
\boxed{\mathcal F(D)\simeq\bigvee^{10}S^{11}\vee\bigvee^{66}S^{12}.}
\]
Equivalently, its only nonzero reduced integral homology groups are \(\widetilde H_{11}\cong\mathbb Z^{10}\) and \(\widetilde H_{12}\cong\mathbb Z^{66}\). This is a complete homotopy classification for this specified graph, not a statement about all generalized Petersen graphs.

## Assumptions and scope
Use vertices \(o_i,u_i\) for \(i\in\{0,\ldots,9\}\), with subscripts modulo ten. The edges of \(D\) are \(o_io_{i+1}\), \(u_iu_{i+2}\), and \(o_iu_i\), one of each for every \(i\); thus \(D\) has 20 vertices and 30 edges. Encode \(o_i\) by bit \(i\) and \(u_i\) by bit \(10+i\), so each subset is a 20-bit mask. A simplex is a subset whose **induced** graph is cycle-free, rather than a subset of edges forming a spanning forest. Orient simplices by increasing vertex label. All homotopy and homology assertions use integral coefficients unless explicitly qualified.

## Proof
**Exhaustive finite reduction.** The accompanying standalone program enumerates all \(2^{20}=1,048,576\) masks and uses two independent exact cycle predicates: union–find detects an edge closing a cycle, and a separate graph search detects a visited nonparent neighbor. Both agree on all masks. Precisely \(755,608\) subsets are simplices, including the empty face. The face counts by cardinality \(k=0,1,\ldots,14\) are
\[
(1,20,190,1140,4845,15492,38580,76260,120540,151920,150480,113400,60620,19600,2520).
\]
No induced forest has more than fourteen vertices. As a check, the alternating reduced Euler characteristic is \(56=-10+66\).

**Discrete Morse matching.** Process vertices \(v=0,\ldots,19\). At stage \(v\), scan faces \(A\) in increasing mask order, requiring \(v\notin A\). If both \(A\) and \(A\cup\{v\}\) belong to the complex and neither has been matched, match this inclusion. This prescription, including the empty face, determines exactly \(377,742\) pairs. The only unmatched simplices are 34 twelve-vertex sets (dimension eleven) and 90 thirteen-vertex sets (dimension twelve). For every face–coface incidence, orient the arrow upward if it is matched and downward otherwise. The generated directed Hasse graph has \(755,608\) vertices and \(6,967,280\) edges. A complete topological sort visits every vertex, establishing acyclicity with no inference from sampling.

**Integral boundary.** The reduced Morse CW model therefore has one basepoint and critical cells only in dimensions eleven and twelve. Its only potentially nonzero cellular differential is \(\partial_{12}:\mathbb Z^{90}\to\mathbb Z^{34}\). For each lower twelve-vertex face \(L\), substitute zero if it is matched to an eleven-vertex face; substitute its standard basis vector if it is critical; and if it is matched upward to a thirteen-vertex face \(U\), substitute the signed sum of the other twelve-vertex faces of \(U\), divided by the \(\pm1\) incidence of \(L\) in \(\partial U\). Termination follows from the verified acyclic orientation. Applied to the boundaries of the 90 critical thirteen-vertex faces, this gives a \(34\times90\) integer matrix with 125 nonzero entries, all \(\pm1\).

**Unimodular reduction and homotopy.** Explicit elementary integer row and column operations isolate 24 unit pivots and leave an identically zero \(10\times66\) residual matrix. Hence the Smith invariants are exactly twenty-four ones and no nonunit invariants. In particular, \(\ker\partial_{12}\cong\mathbb Z^{66}\) and \(\operatorname{coker}\partial_{12}\cong\mathbb Z^{10}\), without torsion. The Morse model has no positive-dimensional cells below eleven; its eleven-skeleton is a wedge of eleven-spheres, and every twelve-cell attaching map is determined by its integer degree vector (the source sphere and target wedge summands are all eleven-dimensional). Unimodular changes of basis therefore split off 24 contractible cell pairs, leaving the asserted wedge of ten eleven-spheres and 66 twelve-spheres. No homology-to-homotopy inference in a non-simply-connected range is used.

## Verification
The complete, self-contained C++17 source is `verify.cpp`. From this directory, run `g++ -O3 -std=c++17 -o verify verify.cpp && ./verify`. The program constructs the graph from the explicit edge formula, independently compares the two acyclicity predicates on every vertex subset, constructs the matching, checks all directed face incidences, evaluates the signed Morse differential recursively, and performs integral elementary operations. It exits with an error if any required numerical identity or exact certificate fails. `VERIFY.log` contains the output recorded from an execution of this exact source. The final line is `VERIFY_OK`; the printed counts include 24 unit Smith pivots and the two reduced Betti ranks. The source, rather than a log alone, is the finite certificate and enables a fresh replay.

## Relationship to prior work
Taylan's publicly posted 2015 study of graph devoid complexes gives the forbidden-induced-subgraph framework and matching-tree techniques, but its inspected homotopy classifications concern different graph families and forbidden patterns. Zuffi's 2017 thesis, Section 1.5.1, gives the exact induced-acyclic-vertex-set definition, but no dodecahedral classification. Carnero Bravo's full-text forest-filtration paper formalizes the same induced-forest vertex complex as the final filtration stage and computes families including paths, cycles, cactus graphs, multipartite graphs and certain products; none of its inspected statements gives this dodecahedral classification. Published dodecahedral independence-complex results use vertex subsets with **no edges**, a strict and differently constrained subcomplex. Published matching-complex results instead take **edge subsets** with disjoint endpoints. Neither prior homotopy formula determines this induced-forest complex by implication. The exact statement and possible broader coverage were separately searched under the generalized Petersen name and equivalent induced-cycle-avoidance language; no covering theorem was found in the inspected material. Absence of indexed coverage is not a proof of universal priority.

## Limitations
The result is for the single exactly specified twenty-vertex graph. It does not classify \(\mathcal F(GP(n,2))\) for arbitrary \(n\), determine the action of its automorphism group, or assert shellability. The proof uses exhaustive finite enumeration and exact integer arithmetic, not experimental extrapolation. The originality assessment remains conditional on accessible literature and indexed records; equivalent unindexed or uninspected work cannot be excluded. Independent mathematical validation has not been performed.

## References
1. Demet Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, first posted 2015-01-27. https://arxiv.org/html/1501.06754v1
2. Andrés Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first posted 2023-07-25. https://arxiv.org/abs/2307.13271
3. Lorenzo Zuffi, *Simplicial Complexes From Graphs Toward Graph Persistence*, University of Bologna thesis, 2017, Definition 38, Section 1.5.1. https://amslaurea.unibo.it/id/eprint/13519/1/lorenzo_zuffi_graph_persistence.pdf
4. Discrete Morse matching and algebraic Morse reduction: standard finite CW and simplicial-chain constructions as instantiated and exhaustively certified in `verify.cpp`.
