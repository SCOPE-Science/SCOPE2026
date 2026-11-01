# Mixed-dimensional integral multipath homotopy of the bidirected \(K_{3,3}\)

## Finding
Let \(D=\overleftrightarrow{K_{3,3}}\) be the loopless digraph with vertex bipartition \(L=\{0,1,2\}\), \(R=\{3,4,5\}\), and both directed arcs between every vertex in \(L\) and every vertex in \(R\). Let \(X(D)\) be its multipath complex: simplices are subsets of the 18 arcs that form vertex-disjoint directed simple paths and isolated vertices, with **all directed cycles forbidden**. Then
\[
X(D)\simeq \bigvee^{19}S^3\vee\bigvee^{12}S^4.
\]
Thus \(\widetilde H_3(X(D);\mathbb Z)\cong\mathbb Z^{19}\), \(\widetilde H_4(X(D);\mathbb Z)\cong\mathbb Z^{12}\), and the other reduced integral homology groups vanish. The nonempty face vector, in dimensions zero through four, is \((18,108,264,252,72)\); there are 714 nonempty simplices. The maximal faces comprise 72 three-simplices and 72 four-simplices, so the complex is not pure.

## Assumptions and scope
The digraph is **bidirected**, rather than the all-left-to-right orientation of the complete bipartite graph. Each directed arc is a separate vertex of the simplicial complex. A collection of arcs is a simplex precisely when every graph vertex has indegree and outdegree at most one in the selected subgraph and that subgraph contains no directed cycle (including two-cycles). The graph is finite, simple and loopless; all chains and homotopy statements use integral coefficients unless otherwise noted. The claim covers this one graph, not a full family of balanced bipartite digraphs.

## Proof
Enumerate the arcs in the following order: first \((u,v)\) with \(u\in L\), \(v\in R\), in lexicographic order, then \((u,v)\) with \(u\in R\), \(v\in L\), again in lexicographic order. Identify an arc subset with an 18-bit integer. Enumerating all \(2^{18}\) subsets with the degree-and-cycle test gives 714 nonempty multipaths with the stated face vector. A second test based on weak connected components independently agrees on all subsets: the selected component on \(s\) vertices must have \(s-1\) arcs and obey the indegree/outdegree constraints.

Construct a discrete-Morse matching on the nonempty face poset by processing arc indices in the fixed order
\[
(0,9,1,10,2,11,3,12,4,13,5,14,6,15,7,16,8,17).
\]
At each index, pair every still-unmatched face not containing that arc with its union with the arc, provided this union is still unmatched. This produces 336 disjoint Hasse pairs, leaving one critical vertex, five critical two-cells, 24 critical three-cells and twelve critical four-cells. The directed Hasse graph has 2,376 incidences; orient matched incidences upward and every other incidence downward. Exhaustive topological sorting visits all 714 vertices, proving the matching acyclic. Forman's discrete Morse theorem therefore yields a CW complex with exactly those critical cells.

For exact attaching-degree calculations, take each simplicial boundary with its signed incidence coefficients in the lexicographically ordered arc basis. Cancel the 336 matched cell pairs by legal integral unit pivots, each time taking the Schur complement in the boundary matrix. These cancellations are recorded by the standalone checker and the complete `certificate.json`. The remaining cellular boundary in degree three is a \(5\times24\) integral matrix with 18 nonzero entries, all equal to \(1\) or \(-1\). Its five columns labeled by upper-face bitmasks
\[
(6304,33952,35088,65676,67716)
\]
form a \(5\times5\) minor of determinant \(+1\). The remaining degree-four cellular boundary is the zero \(24\times12\) matrix. There are no critical one-cells.

The two-skeleton is a wedge of five two-spheres, and the 24 three-cell attaching maps are classified by their degree vectors in \(\pi_2(\bigvee^5 S^2)\cong\mathbb Z^5\). The unit maximal minor permits elementary basis changes and homotopy cancellations of five two-cell/three-cell pairs; the three-skeleton becomes a wedge of 19 three-spheres. After these cancellations, the remaining twelve four-cell attaching maps land in this wedge. Since \(\pi_3(\bigvee^{19}S^3)\cong H_3(\bigvee^{19}S^3;\mathbb Z)\cong\mathbb Z^{19}\), their attaching degrees are determined by the cellular degree-four boundary, which is zero. Therefore all twelve attaching maps are null-homotopic, giving the claimed integral wedge decomposition.

## Verification
Run `python3 verify.py --check-certificate certificate.json` from the directory containing both files. The standard-library-only verifier reconstructs every face in two ways, all 336 matching pairs, the entire directed Hasse graph and its acyclicity, all integral chain cancellations, the exact unit minor and the zero degree-four boundary. Its output is included verbatim as `verification_output.txt`. Independent direct mod-two boundary ranks in dimensions one through four are \((17,91,173,60)\), giving unreduced Betti vector \((1,0,0,19,12)\). The reduced Euler characteristic is \(-7=-19+12\). No probabilistic test or finite sample is substituted for enumeration: all \(2^{18}\) potential arc subsets are checked.

## Relationship to prior work
The cycle-free chessboard complex \(\Omega_6\) of Vrećica and Živaljević is the multipath complex of the **complete** bidirected six-vertex digraph. The present complex is the proper induced subcomplex obtained by allowing only arcs crossing a fixed \(3+3\) bipartition; the general connectivity theorems for \(\Omega_6\) do not determine its homotopy. Caputi, Collari, Di Trani and Smith compute Euler characteristics for complete bipartite digraphs oriented entirely from one color class to the other (chessboard complexes), and homotopy types for other graph classes; that orientation is a different complex. Caputi, Collari and Smith's subsequent bidirectional polygonal work treats paths and cycles, not this complete bipartite graph. Previously available computations of neighboring bidirected complete bipartite cases, including \(\overleftrightarrow{K_{2,n}}\) and \(\overleftrightarrow{K_{3,4}}\), do not yield this six-vertex homotopy type by restriction. A general Hamiltonian-cycle description of top reduced homology already accounts for the twelve degree-four classes here; the new information includes the nineteen degree-three spheres and the full integral homotopy splitting.

## Limitations
This is an exact finite classification for the specified graph. It does not classify \(\overleftrightarrow{K_{m,n}}\) in general, prove a uniform recurrence, or determine group representations on the homology. Related published or unindexed computations might contain an equivalent statement; novelty is assessed against the specific inspected literature and mathematical research records, not asserted as an absolute uniqueness guarantee. Verification relies on standard discrete-Morse and CW attachment theorems together with the executable finite certificate; no independent external mathematical audit is claimed.

## References
1. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, first posted 2022-08-09; *Mathematika* 70 (2024), e12235, DOI:10.1112/mtk.12235. Sections 2, 3.2, 4 and 5.
2. L. Caputi, C. Collari and S. Di Trani, *Combinatorial and topological aspects of path posets, and multipath cohomology*, *Journal of Algebraic Combinatorics* 57 (2023), 617–658, DOI:10.1007/s10801-022-01180-9; first published online 2022-11-10. Sections 3 and 6.
3. S. T. Vrećica and R. Živaljević, *Cycle-free chessboard complexes and symmetric homology of algebras*, arXiv:0710.5252, first posted 2007-10-27; *European Journal of Combinatorics* 30 (2009), 542–554. Sections 2–3 and 7–9.
4. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670, first posted 2026-01-09. Introduction and Theorems 1.4, 2.8 and 2.10.
