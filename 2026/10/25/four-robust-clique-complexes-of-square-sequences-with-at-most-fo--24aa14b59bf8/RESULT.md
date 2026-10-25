# Four-robust clique complexes of square sequences with at most four squares

## Finding

Let \(G\) be a square-sequence graph of length \(s\le4\): begin with a four-cycle and successively attach a four-cycle, with graph intersection exactly one edge or one two-edge path. The **four-robust clique complex** \(\operatorname{Cliq}_4(G)\) consists of all vertex subsets containing no independent four-element set.

**Theorem.** For every such \(G\), \(\operatorname{Cliq}_4(G)\) is either contractible or is homotopy equivalent to a wedge of \(5\)-spheres. Up to graph isomorphism, there are exactly \(1,2,7,29\) cases at lengths \(s=1,2,3,4\), respectively. The table gives the **complete** classification of the \(29\) length-four cases. Here \(r\) denotes the number of sphere summands; \(r=0\) means contractible.

| Number of graph vertices | \(r\) | Number of isomorphism classes |
| ---: | ---: | ---: |
| 7 | 0 | 3 |
| 8 | 0 | 4 |
| 8 | 1 | 4 |
| 9 | 2 | 7 |
| 9 | 3 | 2 |
| 9 | 4 | 1 |
| 10 | 4 | 8 |

For \(s=1,2\), every case is contractible. For \(s=3\), the two six-vertex and two seven-vertex classes are contractible; the three eight-vertex classes have homotopy type \(S^5\). In particular,
\[
\operatorname{Cliq}_4(P_3\square P_3)\simeq\bigvee^{4}S^5.
\]

## Assumptions and scope

All graphs are finite, simple, and undirected. Attachments are unions of subgraphs as in Definition 8 of the reference: an edge attachment introduces two new vertices and three edges; a corner attachment introduces one new vertex and two edges, closing a four-cycle on a pre-existing two-edge path. The graph need not have a unique square-sequence presentation. Classification is up to **graph isomorphism**, not labeled presentations. An empty wedge is the homotopy type of a point. The parameter \(4\) is fixed for the forbidden independent-set size, and the attachment length satisfies \(1\le s\le4\).

## Proof

**Exhaustion of the graph class.** Initially there is one graph, \(C_4\). Given a representative \(H\), any legal edge attachment is produced by choosing an edge \(ab\) and adjoining two new vertices \(x,y\) and edges \(bx,xy,ya\). Any legal corner attachment is produced by choosing an unordered pair \(a,c\) of neighbors of a vertex \(b\) and adjoining a new vertex \(x\) and edges \(ax,xc\). Every four-cycle glued along a one-edge or two-edge path has one of these two forms, up to renaming its new vertices. Thus extension of all representatives enumerates every next-level graph. Removing duplicates by exact graph isomorphism is legitimate because both the gluing property and the simplicial homotopy type are isomorphism invariants. The exhaustive enumeration yields \(1,2,7,29\) isomorphism classes at the four successive levels.

**Exact face set.** On a representative with vertices indexed \(0,\ldots,N-1\), enumerate every independent four-subset \(Q\). A nonempty subset \(F\) belongs to \(\operatorname{Cliq}_4(H)\) if and only if no such \(Q\subseteq F\). The checker evaluates this exact condition for every one of the \(2^N-1\) nonempty subsets, with \(N\le10\).

**An acyclic matching on every face poset.** Order the vertices. For each vertex in order, pair every still-unmatched face \(F\) not containing that vertex with \(F\cup\{v\}\), whenever both remain unmatched faces. The program constructs the entire nonempty-face Hasse diagram and directs each matched covering relation upwards, with every other covering relation directed downwards. An explicit topological-sort traversal visits **every** face, verifying the directed graph is acyclic; each face participates in at most one matched covering. The remaining critical faces consist, for **every** representative, of exactly one vertex together with \(r\) faces of dimension five and no other critical faces. The classification of \(r\) by graph order is the table above.

By the acyclic matching theorem in discrete Morse theory, the realization of each simplicial complex has the homotopy type of a CW complex with one zero-cell and \(r\) five-cells, and no cells of dimensions one through four. Each attaching map of a five-cell therefore lands in the point zero-skeleton and is null; the CW complex is a wedge of \(r\) copies of \(S^5\), or a point when \(r=0\). This proves the asserted **integral homotopy** classification, not merely field homology.

## Verification

Run `python square4_verify.py` with Python 3.10 or later and NetworkX installed. This constructs the graphs, filters by exact graph isomorphism, reconstructs all faces, checks all matching covering relations for acyclicity and asserts the complete table. Run `python square4_homology.py` independently: it reimplements graph extension and face enumeration and calculates every mod-two boundary-matrix rank for all \(39\) cases, reproducing the same reduced Betti-number table. The companion output files record the runs used for this finding. Neither implementation calls the other. The proof of sphere-wedge homotopy rests on the **exhaustive matching and acyclicity test**, rather than on mod-two homology alone.

## Relationship to prior work

Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs* (first publicly submitted February 11, 2026), defines these complexes and square-sequence graphs, proves the homotopy classification for parameters \(k=2,3\), and proves an arbitrary-\(k\) result for sequences constructed **exclusively by edge gluing** (Theorem 2 and Corollary 3). Conjecture 5 proposes a wedge-of-\((2k-3)\)-spheres conclusion when **corner gluing is allowed**. Thus the all-edge cases among our finite enumeration are already within published stronger coverage; the extension provided here is the complete \(k=4\), length-at-most-four classification **including the corner-glued cases**, which constitute \(21\) of the \(29\) length-four isomorphism classes. The corner-containing graphs have fewer than ten vertices, whereas a length-four all-edge attachment sequence produces ten vertices. Related work on bounded independence complexes provides background but does not supply this exhaustive finite homotopy classification in the inspected material.

## Limitations

No homotopy classification beyond four constituent squares or at forbidden independent-set size greater than four is claimed. The finite table is an exact classification of graph-isomorphism types and their homotopy types; it does not give an explicit general inductive formula in the unrestricted square-sequence problem. The complete matching tests are finite and cannot prove the infinite conjecture. Unindexed or inaccessible prior work could contain overlapping results; no independent mathematical audit has been performed.

## References

1. M. Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first submitted February 11, 2026; especially Definition 8, Definition 9, Corollary 3, and Conjecture 5. https://arxiv.org/abs/2602.11365
2. M. Kim and A. Lew, *Complexes of graphs with bounded independence number*, Israel Journal of Mathematics **249** (2022), 83–120, cited in the motivating paper for the original bounded-independence complex construction. This reference is background, not a claimed novelty exclusion based on complete full-text inspection.
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145 (acyclic combinatorial Morse matchings and CW reductions).
