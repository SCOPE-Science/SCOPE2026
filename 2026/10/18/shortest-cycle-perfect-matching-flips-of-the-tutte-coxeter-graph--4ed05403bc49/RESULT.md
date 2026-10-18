# Shortest-cycle perfect-matching flips of the Tutte–Coxeter graph

## Finding
Let \(T\) be the thirty-vertex Tutte–Coxeter graph, and let \(F_8(T)\) be the graph whose vertices are all perfect matchings of \(T\), with two distinct perfect matchings adjacent precisely when their symmetric difference is the eight edges of a single cycle of length \(8\) in \(T\). Then \(F_8(T)\) is a **connected, simple, ten-regular bipartite graph** with exactly \(288\) vertices and \(1440\) edges, radius \(5\) and diameter \(6\).

The bipartition has an intrinsic description using the cycle type of the spanning two-factor complementary to a perfect matching. Exactly \(144\) perfect matchings have a complementary Hamiltonian \(30\)-cycle, while the other \(144\) have complementary cycles of lengths \(10\) and \(20\). Every eight-cycle flip switches between these types. For each of the \(144\) Hamiltonian-complement matchings, the numbers of vertices of \(F_8(T)\) at distances \(0,1,\ldots,6\) are
\[
 (1,10,42,97,101,37,0),
\]
whereas each of the \(144\) split-complement matchings has distance profile
\[
 (1,10,45,97,96,37,2).
\]
Thus the Hamiltonian-complement matchings are precisely the center of the flip graph, while split-complement matchings are exactly the eccentricity-\(6\) vertices. These statements about flips, connectivity and distances are the present finding; the scalar number of perfect matchings and their complementary two-factor types are prior known data, not claimed as original.

## Assumptions and scope
Write \(U=\{0,1,2,3,4,5\}\). The *duads* are the \(15\) two-element subsets of \(U\), and the *synthemes* are the \(15\) partitions of \(U\) into three unordered disjoint duads. Define \(T\) to have these \(30\) objects as vertices and an edge between a duad and a syntheme if and only if the former is one of the latter's three pairs. This is the standard Tutte–Coxeter incidence graph. Each vertex has degree \(3\), so the complement of any perfect matching is a spanning \(2\)-regular subgraph.

An *eight-cycle flip* removes the four matching edges on an alternating simple eight-cycle and adds the other four edges of that cycle. Every intermediate object in the flip graph is itself a perfect matching; no temporary deficient matching is permitted. Distances are ordinary undirected shortest-path lengths in the graph of perfect matchings, not distances in the thirty-vertex source graph.

## Proof
The claim has a finite exhaustive proof in two independent implementations, using the explicit duad–syntheme construction above. For precision, the key logical steps and complete search spaces are as follows.

**Exhaustive matching space.** Order the \(15\) duads. Each duad is incident with three synthemes. Recursively assign to every duad one of these synthemes, rejecting any reused syntheme. At recursion depth \(15\) exactly one edge incident with each vertex has been chosen, hence one perfect matching is obtained. Conversely every perfect matching yields exactly one of these assignments; no branch is pruned except an infeasible reused syntheme. This produces \(288\) distinct matchings. A second verifier instead chooses the least uncovered vertex in the full thirty-vertex graph and recursively matches it to an available neighbor; it also finds precisely \(288\) matchings.

**Cycles and complete transitions.** Enumerate every simple length-\(8\) closed walk whose starting vertex is the least vertex on the walk, with all eight vertices distinct; canonicalize by the unordered set of eight graph edges. The resulting set has exactly \(90\) distinct cycles. For each cycle and each enumerated perfect matching, count the matching edges of the cycle. Precisely \(32\) matchings have four alternating matching edges along any given cycle. Every such matching yields a second perfect matching by taking the symmetric difference with the cycle edges, and no other matching participates in a flip along that cycle. Therefore each cycle produces \(32/2=16\) unordered flip transitions. The transition sets for different cycles are disjoint, because the symmetric difference of the two endpoints uniquely identifies the cycle. Hence there are \(90\cdot16=1440\) edges. A separate pairwise enumeration of all \(\binom{288}{2}\) matching pairs produces exactly the same edges. For each pair with an eight-edge symmetric difference, the second implementation verifies directly that these eight edges form one connected simple eight-cycle. Thus no legal flip is missed or spuriously added.

**Complement and geometry.** Delete the \(15\) selected matching edges from the \(45\)-edge cubic graph. Connected components of the remaining degree-two subgraph are cycles. Exhaustive component traversal yields exactly \(144\) matchings with cycle type \((30)\) and \(144\) with type \((10,20)\); these previously recorded counts are used here to classify the flip states. Inspecting every one of the \(1440\) fully enumerated transitions shows that its endpoints have opposite types. Every vertex has exactly \(10\) neighbors, hence the type classes give a ten-regular bipartition with \(144\) vertices per side.

**Exact distance audit.** Breadth-first search from each of the \(288\) flip-graph vertices visits every other vertex and gives the two distance histograms in the statement: \((1,10,42,97,101,37,0)\) for every Hamiltonian-complement source and \((1,10,45,97,96,37,2)\) for every split-complement source. These are complete rows, each summing to \(288\). Therefore the flip graph is connected, the former \(144\) vertices have eccentricity \(5\), the latter \(144\) have eccentricity \(6\), and the claimed sharp radius and diameter follow. The separate thirty-vertex matching implementation reconstructs all vertex-by-vertex breadth-first histograms and agrees exactly.

## Verification
The included `verify.py` uses only Python's standard library. Running `python3 verify.py certificate.json` enumerates every matching, all simple eight-cycles, each matching flip, all complementary cycle types, and all \(288\) shortest-path histograms. It writes `certificate.json` deterministically; the included instance records the \(45\) incidence edges, \(90\) eight-cycles, \(288\) perfect matchings, \(288\) two-factor types, all \(1440\) flip edges and all \(288\) complete distance histograms. `python_output.txt` is the actual resulting console output.

A structurally separate program, `independent.cpp`, can be compiled with `g++ -std=c++17 -O2 independent.cpp -o independent` and then run as `./independent`. It reconstructs the incidence graph, uses recursive matching on the full thirty-vertex set, compares all pairs of matchings and checks every proposed eight-cycle, independently enumerates eight-cycles, and runs breadth-first search from every matching. `cpp_output.txt` is its actual output. The two outputs agree on all reported numerical invariants. Both programs have been executed and their outputs checked against the files supplied here.

## Relationship to prior work
De Carvalho, Lucchesi and Murty study counts and bounds for perfect matchings in matching-covered bipartite graphs. Baez gives the duad–syntheme construction and the underlying graph's classical properties. Balasubramanian's matching-polynomial table independently records the value \(288\) for the number of perfect matchings. Existing enumeration also distinguishes the \(144\) Hamiltonian-complement and \(144\) split-complement matchings, and classifies one-factorizations; those counts are **not** claimed as new here. The new statement concerns the entire intrinsic graph obtained by toggling along *any* shortest cycle, including connectedness, ten-regularity, the natural two-factor bipartition and exact distance profiles.

Tratnik and Ye study resonance graphs for a **chosen collection of facial even cycles in a specified surface embedding**. Their general cubical-embedding statements do not specify the full collection of \(90\) graph-intrinsic eight-cycles in \(T\) and do not derive the numerical flip adjacency or metric classification. The definition in the present result does not choose any embedding or restrict moves to faces. Targeted published-record and mathematical-result searches did not identify an equivalent claim, but these searches do not prove uniqueness across all literature.

## Limitations
This is an exact finite-graph result: it does not assert any formula for arbitrary cubic bipartite graphs, other generalized quadrangles or longer-cycle moves. The proof is exhaustive and depends on correctness and reproducibility of finite enumeration and shortest-path code, with a complete state-and-transition certificate available for checking. The result does not imply an independent formal or external certification. Unindexed or inaccessible prior work could still contain an equivalent flip-graph calculation. No generalization beyond the explicitly defined \(T\) and eight-cycle operation is claimed.

## References
1. M. H. de Carvalho, C. L. Lucchesi, U. S. R. Murty, “On the Number of Perfect Matchings in a Bipartite Graph,” *SIAM Journal on Discrete Mathematics* 27 (2013), 940–958. DOI: `10.1137/120865938`.
2. J. Baez, “Tutte–Coxeter Graph,” *Visual Insight*, 15 August 2015. `https://math.ucr.edu/home/baez/visual_insight/20150815%20-%20Tutte-Coxeter%20Graph.html`.
3. K. Balasubramanian, “Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions,” *Symmetry* 17 (2025), 133. DOI: `10.3390/sym17010133`.
4. N. Tratnik and D. Ye, “Resonance Graphs and Perfect Matchings of Graphs on Surfaces,” arXiv:1710.00761v1 (2017), published *Graphs and Combinatorics* 39 (2023), article 68.
