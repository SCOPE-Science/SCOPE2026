# First global counting-logic ambiguity among connected block graphs occurs at six vertices

## Finding

Consider finite simple uncoloured undirected graphs, and start one-dimensional colour refinement (1-WL) from the uniform vertex colour. Call a graph *globally identified* if 1-WL distinguishes it from every nonisomorphic graph; its comparison graph need not satisfy any restriction. Among connected block graphs, every graph on at most five vertices is globally identified. There are exactly 22 connected block-graph isomorphism types on six vertices, and **exactly one** is not globally identified: two disjoint triangles joined by a single bridge. Its 1-WL equivalence class among all six-vertex graphs has exactly two isomorphism types, with the other type the theta graph having three internally disjoint paths of lengths \(1,3,3\) between its two degree-three vertices.

Equivalently, among connected block graphs on at most six vertices, this is the unique graph not identified up to isomorphism by two-variable first-order logic with counting, \(C^2\). The equivalence with 1-WL identification is classical; the asserted finite threshold and complete first-failure class are the finite classification here.

## Assumptions and scope

A *block graph* is a connected finite simple graph in which every maximal biconnected edge block is a clique; a bridge is a two-vertex clique block. All graphs are unlabeled when counted up to isomorphism. Refinement is *global*: for two graphs on the same number of vertices, colours are assigned to equal signatures in the same colour vocabulary. Initially all vertices have one colour. At each step, the next signature of vertex \(v\) is its current colour together with the multiset of the current colours of its neighbours. Graphs are indistinguishable exactly when the colour multisets of their vertices agree at every step (equivalently, at stabilization). Different graph orders are distinguishable by their vertex counts.

The claim is **global identification**, not identification merely among other block graphs, nor a classification of all orders. The exact range is \(1\leq |V(G)|\leq6\) and the graph has to be connected.

## Proof

**Explicit obstruction.** Let \(G\) have vertex set \(\{0,1,2,3,4,5\}\) and edges

\[
E(G)=\{01,02,12,03,34,35,45\}.
\]

Then \(G\) is the bridge join of triangles \(012\) and \(345\), so it is a connected block graph. Let \(H\) have edges

\[
E(H)=\{03,01,12,23,04,45,53\}.
\]

It is a theta graph with paths of respective lengths \(1,3,3\), and has no triangles; \(G\) has exactly two triangles. They are not isomorphic. In both graphs, vertices \(0,3\) have degree three and the other four vertices degree two. The two degree-three vertices each have one degree-three and two degree-two neighbours. Each degree-two vertex has one neighbour of each degree. Thus the degree partition is equitable with identical class sizes and quotient neighbour counts in \(G\) and \(H\); all subsequent 1-WL colours coincide as multisets. Hence \(G\) is not globally identified.

**Minimality and uniqueness by finite exhaustion.** The bundled dependency-free verifier `verify.py` supplies a finite proof certificate in executable form. For each \(n=1,\ldots,6\), encode every labelled graph on \(\{0,\ldots,n-1\}\) by its \(\binom n2\) edge bits. The script enumerates all \(2^{\binom n2}\) bit masks without pruning. For each minimum unseen mask, it generates the complete isomorphism orbit using all adjacent vertex transpositions: those transpositions generate the symmetric group, so precisely one representative of every isomorphism type is retained. Connectivity is tested by reachability. The DFS low-link/edge-stack decomposition partitions the edges into biconnected blocks, and the block-graph test accepts exactly those connected graphs for which each block on \(t\) vertices has \(\binom t2\) edges. Every step is exact integer/finite-set arithmetic.

For each fixed \(n\), the verifier refines *all* isomorphism-class representatives simultaneously, using one dictionary of exact colour signatures. Thus any graph with the same sequence of colour-multisets falls into the same exact group. Refinement is repeated until the global colouring stabilizes; no sampling or statistical cutoff is used. The enumeration gives the following rows, respectively: number of all graph isomorphism types, number of connected block graphs, number of connected block-graph types having any nonisomorphic 1-WL mate, number of global 1-WL equivalence classes:

| \(n\) | All graphs | Connected block graphs | Globally ambiguous block graphs | Global 1-WL classes |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 0 | 2 |
| 3 | 4 | 2 | 0 | 4 |
| 4 | 11 | 4 | 0 | 11 |
| 5 | 34 | 9 | 0 | 34 |
| 6 | 156 | 22 | 1 | 152 |

The unique ambiguous connected block-graph representative at \(n=6\) is checked against the explicit \(G\) by isomorphism-orbit identifiers. Its exact 1-WL group consists of two nonisomorphic types, the explicit \(G\) and \(H\), and the script checks that precisely one of those two is a connected block graph. This exhausts all possible smaller cases and every case at the threshold.

## Verification

Run `python3 verify.py` with the standard Python library. The script prints the six rows above and terminates with `VERIFIED_FIRST_FAILURE_ORDER_6_AND_UNIQUE_PAIR`. It also checks each independent vertex-relabeling orbit, the connected-block-graph counts, the canonical identifiers of the explicit witnesses, and their triangle counts. The largest enumerated labelled family has \(2^{15}=32768\) members. Both witnesses have six vertices and seven edges. The packaged verifier was run successfully before release. The arguments certifying completeness are the exhaustive edge-bit range, the generating adjacent transpositions, and the exhaustive refinement of every resulting orbit, not a partial experimental search.

## Relationship to prior work

Arvind, Köbler, Rattan and Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness* (arXiv:1502.01255, initial public version 4 February 2015), define global amenability, relate it to fractional isomorphism, and prove a complete general characterization (Theorem 9 of the 4 May 2015 version). Kiefer, Schweitzer and Selman, *Graphs Identified by Logics with Counting* (arXiv:1503.08792, 30 March 2015), give a logically equivalent broad classification of graphs identified by \(C^2\) (their Section 4). Both works subsume the **graph-by-graph amenability question** and show why a finite refinement test answers it. The particular assertion here is the sharp *first-order cutoff and complete minimal obstruction census within connected block graphs*, with a pair specified also outside that class, rather than a new characterization algorithm. The reviewed portions of those papers did not state this precise block-graph threshold or census. A separate eight-vertex classification of indistinguishable pairs **both within connected chordal graphs** concerns a different comparator domain: the present six-vertex partner is not chordal, so there is no conflict with that restricted-pair threshold. A hidden earlier tabulation or a derived corollary remains a residual originality risk.

## Limitations

No claim is made that all connected block graphs are distinguishable **from other block graphs** at larger orders, that the present small class-relative census extends indefinitely, or that 1-WL distinguishes connected chordal graphs generally. The proof has only the stated six-vertex cutoff. The conclusion is a finite complete fact supported by a transparent exhaustive verification, not a new general C2-completeness theorem.

## References

1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first posted 2015-02-04); especially Section 2, Section 4 and Theorem 9. https://arxiv.org/abs/1502.01255
2. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792 (first posted 2015-03-30); especially Sections 2 and 4. https://arxiv.org/abs/1503.08792
