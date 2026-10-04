# The total \(3\)-cut complex of the Wagner graph is a wedge of three \(2\)-spheres
## Finding
Let \(M_8\) be the 8-vertex Möbius ladder with vertex set \(\mathbb Z/8\mathbb Z\), cycle edges \(\{i,i+1\}\), and antipodal edges \(\{i,i+4\}\). If \(\Delta^t_3(M_8)\) is the total \(3\)-cut complex, whose facets are the complements of independent \(3\)-subsets, then \[\Delta^t_3(M_8)\simeq \bigvee^{3}S^2.\]

The eight independent \(3\)-subsets are
\[
\begin{aligned}
&\{0,2,5\},\ \{0,3,5\},\ \{0,3,6\},\ \{1,3,6\},\\
&\{1,4,6\},\ \{1,4,7\},\ \{2,4,7\},\ \{2,5,7\}.
\end{aligned}
\]
Thus the total \(3\)-cut complex has eight facets, each on five vertices, and nonempty face vector \((8,28,48,32,8)\).

## Assumptions and scope
The graph is defined explicitly above; no graph-database convention is needed. The total \(3\)-cut convention is the one introduced by Bayer--Denker--Jelić Milutinović--Rowlands--Sundaram--Xue: facets are complements of independent sets of cardinality \(3\). The statement is only about this eight-vertex Möbius ladder and this value of \(k\); it makes no periodicity claim for the family \(M_{2n}\).

## Proof
Enumerating independent triples gives exactly the eight sets displayed above. Taking their complements and closing under inclusion gives a finite complex with \(124\) nonempty faces.

On the nonempty face poset, process the vertices in the order \(0,1,\ldots,7\). At stage \(v\), whenever two still-unmatched faces have the form \(\sigma\) and \(\sigma\cup\{v\}\), match them. This deterministic matching contains \(60\) pairs and leaves exactly
\[
\{0\},\qquad \{1,2,5\},\qquad \{1,2,6\},\qquad \{1,3,7\}
\]
unmatched. Hence there is one critical \(0\)-cell and three critical \(2\)-cells.

For completeness, acyclicity is checked exhaustively rather than inferred from a heuristic. Orient every unmatched Hasse edge downward and every matched Hasse edge upward. The complex has \(368\) Hasse edges, and a complete topological-sort check visits all \(124\) vertices of this directed graph, so the Morse orientation is acyclic. Forman's discrete Morse theorem therefore replaces the complex by a CW complex with one \(0\)-cell and three \(2\)-cells and no other cells. Each \(2\)-cell attaches to the unique \(0\)-cell, so this CW complex is \(\bigvee^3 S^2\).

## Verification
The embedded `artifacts/verify.py` reconstructs the graph from the defining edge rule, enumerates all independent triples and all faces, reproduces the face vector and the \(60\)-pair matching, and checks the complete Morse orientation for directed cycles. As an independent chain-level cross-check it computes mod-\(2\) boundary ranks \((7,21,24,8)\), giving Betti vector \((1,0,3,0,0)\), and verifies Euler characteristic \(4\). Running the script with the standard Python interpreter ends with `VERIFY_OK`.

## Relationship to prior work
Bayer et al. introduced total cut complexes and determined them for several graph families, including chordal graphs, cycles, bipartite graphs, \(K_n\mathbin{\times}K_2\), and grid graphs. None of those family results contains the Wagner graph in the present guise: \(M_8\) is non-bipartite and is not a cycle, chordal graph, rectangular grid, or a prism over a complete graph.

Agarwal et al. subsequently determined independence and perfect-matching complexes of Möbius and circular ladder graphs. Their future-directions section explicitly asks for the homotopy types and homology of the cut and total cut complexes of Möbius ladders. The present computation supplies the first non-bipartite Möbius-ladder instance for the total \(3\)-cut complex: \(M_6\) is the complete bipartite graph \(K_{3,3}\), whereas \(M_8\) is not bipartite.

Exact searches under the aliases “Wagner graph”, “\(M_8\)”, and “Möbius ladder” found no statement implying this homotopy type. The closest indexed Wagner-graph result encountered concerns symbolic powers of its edge ideal, a different invariant that does not determine this total-cut homotopy type.

## Limitations
This is a finite exact result for one graph and one cut parameter. It does not determine \(\Delta^t_k(M_{2n})\) for other values of \(n\) or \(k\), does not establish a periodic family law, and does not claim shellability or a stronger equivariant homotopy statement. A very recent or non-indexed source could still contain the same finite computation, although the explicit September 2026 open-problem statement substantially narrows that bibliographic risk.

## References
1. Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram, and Lei Xue, “Total Cut Complexes of Graphs,” arXiv:2209.13503v1, first posted 2022-09-27.
2. Ayush Agarwal et al., “The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs,” arXiv:2608.30601v2, 2026.
3. Robin Forman, “Morse Theory for Cell Complexes,” *Advances in Mathematics* 134 (1998), 90--145.
