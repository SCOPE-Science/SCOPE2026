# Bidirected \(K_{3,3}\) multipaths form nineteen three-spheres and twelve four-spheres

## Finding

Let \(D\) be the bidirected complete bipartite digraph on two three-element parts, and let \(X(D)\) be the simplicial complex of directed linear forests (multipaths) on its directed arcs. There is an integral homotopy equivalence

\[
X(D)\simeq\bigvee^{19}S^3\vee\bigvee^{12}S^4.
\]

In particular, the only nonzero reduced integral homology groups are \(\widetilde H_3(X(D);\mathbb Z)\cong\mathbb Z^{19}\) and \(\widetilde H_4(X(D);\mathbb Z)\cong\mathbb Z^{12}\). This is a homotopy classification, not merely a numerical homology computation.

## Assumptions and scope

Take the left part \(L=\{0,1,2\}\) and right part \(R=\{3,4,5\}\). For every \(a\in L\) and \(b\in R\), both ordered arcs \((a,b)\) and \((b,a)\) occur; there are eighteen arcs, ordered lexicographically by source then target. A face of \(X(D)\) is an arc set with at most one selected incoming and outgoing arc at every vertex and with no directed cycles, including directed two-cycles. Isolated vertices of \(D\) are permitted. This definition is equivalently the directed linear forest complex, and is not the alternating-orientation matching complex. Orient simplices by increasing arc index.

## Proof

**1. Complete face reconstruction.** A set of selected arcs is a directed linear forest if and only if every vertex has selected indegree and outdegree at most one and its underlying undirected **multigraph**, in which opposite directed arcs become distinct parallel undirected edges, is a forest. Indeed, an undirected cycle (including a parallel-edge cycle of length two) under these degree restrictions forces each vertex on the cycle to have one incident incoming and one incident outgoing arc, hence is directed. Build all faces by recursively adding lexicographically later arcs, refusing a repeated target, repeated source, or merger of two vertices already in the same undirected component. This produces exactly 715 faces when the augmented empty face is included. The nonempty face vector by dimensions zero through four is

\[
(f_0,f_1,f_2,f_3,f_4)=(18,108,264,252,72).
\]

An independent exhaustive test of all candidate arc subsets with at most five arcs uses indegree/outdegree counts and a six-vertex topological sort, rather than the component-merger test; it reproduces precisely the same face set. Six arcs cannot form a directed linear forest on six vertices, so the test covers every possible face.

**2. An acyclic simplex matching.** Index arcs starting at zero. Process toggle indices in the exact order

`15, 0, 5, 1, 8, 4, 3, 13, 11, 12, 14, 16, 6, 7, 2, 17, 10, 9`.

At each index \(j\), pair each currently unpaired face \(\sigma\) not containing arc \(j\) with \(\sigma\cup\{j\}\) whenever both faces are currently unpaired and the latter is a face. The augmented matching has 342 pairs and 31 unpaired faces, precisely 19 of dimension three and 12 of dimension four. Remove the single pair containing the empty face. The resulting ordinary matching has 341 pairs, one critical vertex, 19 critical three-simplices, and 12 critical four-simplices. It is acyclic: direct every covering edge of the augmented face poset from the larger to the smaller face, except reverse the 341 matched covering edges. A complete Kahn topological sort processes all 715 faces and all 2,394 covering incidences, leaving no directed cycle. The ordinary nonempty-face matching is therefore acyclic as well.

**3. Signed integral Morse boundary.** Use the augmented simplicial boundary with the standard sign \((-1)^{r}\) when deleting an arc in zero-based position \(r\). For each of the 341 matched pairs, perform an integral chain cancellation at a current pivot equal to \(+1\) or \(-1\), choosing an available unit pivot of smallest sparse fill cost and updating all incident columns by the exact Schur complement. Every listed matching pair is cancelled and all remaining nonempty Morse differentials vanish. The only nonzero augmented differential left is the boundary of the surviving critical vertex onto the empty face, with coefficient one. In particular, the integral Morse boundary \(C_4^{\mathrm{Morse}}\to C_3^{\mathrm{Morse}}\) is identically zero, not merely zero modulo a prime.

**4. From Morse chains to homotopy.** An acyclic simplicial matching yields a CW model with one zero-cell, nineteen three-cells and twelve four-cells. The three-cells attach trivially to the vertex. The four-cell attaching maps lie in \(\pi_3(\bigvee^{19}S^3)\cong\mathbb Z^{19}\), where the Hurewicz map is an isomorphism. Their classes are exactly their integral cellular boundary degrees, already shown to vanish. Every four-cell therefore attaches nullhomotopically. This proves the asserted wedge homotopy type.

## Verification

Run `python3 multipath_k33_certificate.py` with standard Python 3; no third-party packages are required. The program enumerates all arcs and all faces, independently reproduces the face set by directed acyclicity, reconstructs the matching, verifies the entire directed Hasse graph is acyclic, carries out exact signed integral cancellation, and independently calculates the original augmented boundary ranks over \(\mathbb F_2\). These ranks in edge-count degrees one through five are \((1,17,91,173,60)\), giving reduced Betti numbers \((0,0,0,19,12)\) in dimensions zero through four. The final output marker is `BIDIRECTED_K33_MULTIPATH_INTEGRAL_19S3_12S4_VERIFIED`.

## Relationship to prior work

Caputi, Collari, Di Trani and Smith introduced and studied multipath homotopy in general. Their §3.2 complete-bipartite calculation (Theorem 3.7, arXiv:2208.04656) assumes **one-way** arcs from one part to the other, and computes the Euler characteristic of the corresponding chessboard/matching complex. It is not a computation for the bidirected digraph considered here. For comparison, that alternating \(K_{3,3}\) matching complex collapses to a connected graph with four independent cycles: each two-edge matching extends uniquely to a perfect matching, so six distinct free triangle-edge pairs collapse, leaving nine vertices and twelve graph edges. Its homotopy type is \(\bigvee^4S^1\), in contrast with the present mixed-dimensional wedge.

Caputi, Collari and Di Trani's earlier path-poset paper (arXiv:2110.11206) gives small multipath examples and general constructions but no corresponding bidirected complete-bipartite homotopy calculation. Deshpande and Sawant (arXiv:2602.14936) identify directed linear forest complexes with multipath complexes, and develop conflict-graph and hypergraph methods for general directed graphs; the inspected statements address shellability/vertex decomposability and do not specify this bidirected \(K_{3,3}\) homotopy type. Related indexed calculations for bidirected double stars concern trees, whereas \(K_{3,3}\) has many cycles; indexed \(K_{3,3}\) **Morse complexes** concern a different simplicial complex of graph vector fields. No equality or implication from those results to the displayed integral wedge was found in the inspected material.

## Limitations

The result concerns only the six-vertex fully bidirected complete bipartite graph with both parts of size three; no infinite-family or equivariant classification is asserted. The proof uses exact finite exhaustive enumeration, a fully reconstructible acyclic matching, and signed integral cancellations, not heuristic sampling. The mathematical claim is independently auditable using the supplied code, but no independent external audit has been performed. Literature searches cannot exclude an equivalent unindexed or inaccessible prior result.

## References

1. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, first public arXiv posting 2022-08-09, arXiv:2208.04656, Mathematika 70 (2024), article e12235, DOI:10.1112/mtk.12235.
2. L. Caputi, C. Collari and S. Di Trani, *Combinatorial and topological aspects of path posets, and multipath cohomology*, first public arXiv posting 2021-10-21, arXiv:2110.11206, J. Algebraic Combin. 57 (2023), 617–658, DOI:10.1007/s10801-022-01180-9.
3. P. Deshpande and R. Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936, first public 2026-02-16.
