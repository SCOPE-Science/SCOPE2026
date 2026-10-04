# The Petersen total \(3\)-cut complex is a wedge of nine \(4\)-spheres
## Finding
Let \(P\) be the Petersen graph on vertices \(0,1,\ldots,9\) with edges
\[(01,12,23,34,40),(05,16,27,38,49),(57,79,96,68,85).\]
For a graph \(G\), the total \(3\)-cut complex \(\Delta^t_3(G)\) is the simplicial complex whose facets are complements of independent \(3\)-subsets of \(V(G)\). Then
\[\Delta^t_3(P)\simeq \bigvee^{9} S^4.\]
Consequently, \(\Delta^t_3(P)\) is not shellable: it is pure of dimension \(10-3-1=6\), while its reduced homology is nonzero in dimension \(4\).

## Assumptions and scope
Graphs are finite and simple. The definition of the total cut complex is the one of Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue. The Petersen graph presentation above is fixed only to make the finite verification reproducible; relabeling the graph does not change the simplicial isomorphism type. The claim concerns \(k=3\) only.

## Proof
The Petersen graph has exactly \(30\) independent \(3\)-subsets. Their complements are the \(30\) facets of \(\Delta^t_3(P)\), each of cardinality \(7\). Closing these facets under inclusion gives \(790\) nonempty simplices with face vector
\[(10,45,120,210,240,135,30).\]

Order the vertices as \(0,1,\ldots,9\). Starting with all nonempty faces unmatched, process these vertices in that order. At stage \(v\), whenever both an unmatched face \(\sigma\) not containing \(v\) and \(\sigma\cup\{v\}\) are present and unmatched, pair them. This gives \(390\) Hasse pairs. Direct orientation of every unmatched Hasse cover downward and every matched cover upward is acyclic on the full \(3510\)-cover Hasse diagram.

The only unmatched faces are one vertex and nine \(4\)-simplices. Thus Forman's discrete Morse theorem gives a CW complex homotopy equivalent to \(\Delta^t_3(P)\) with exactly one \(0\)-cell and nine \(4\)-cells and no other cells. Each \(4\)-cell is therefore attached to the single \(0\)-cell, so this CW complex is \(\bigvee^9 S^4\).

## Verification
Run `python3 verify_petersen_total_cut.py`. The verifier reconstructs the Petersen graph from the displayed edge set, enumerates all independent triples and every face of the total cut complex, rebuilds the sequential element matching, and performs a full directed-cycle test on all Hasse covers. It also separately computes simplicial boundary ranks over \(\mathbb F_2\), obtaining Betti vector
\[(1,0,0,0,9,0,0).\]
A successful replay ends with `PETERSEN_TOTAL_3_CUT_VERIFY_OK`.

## Relationship to prior work
The defining paper introduces total \(k\)-cut complexes, proves general structural results, and computes families including chordal graphs, cycles, bipartite graphs, prisms, and grids. Its full text contains no Petersen-graph computation. The Petersen graph is neither chordal nor bipartite, and the specific \(k=3\) claim is not a specialization of the displayed family formulas in that paper. Exact literature searches for the Petersen graph together with total cut complexes, independent triples, and the claimed wedge type did not locate a covering statement.

The non-shellability conclusion uses the standard fact recalled in the defining paper that a pure shellable \(d\)-complex is contractible or has the homotopy type of a wedge of \(d\)-spheres. Since \(\Delta^t_3(P)\) is pure \(6\)-dimensional but has nonzero \(\widetilde H_4\), it cannot be shellable.

## Limitations
This is an exact finite result for one canonical graph and one value of \(k\); it does not classify total cut complexes of cubic graphs or determine \(\Delta^t_k(P)\) for all \(k\). The originality assessment is relative to the inspected and searched literature and may miss an unindexed computation under substantially different terminology. Independent audit has not been performed.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, first posted 2022-09-27; later published in *Discrete & Computational Geometry*. The paper defines \(\Delta^t_k(G)\), states the pure-shellable homotopy consequence, and develops the main graph-family results.
2. R. Forman, *Morse Theory for Cell Complexes*, *Advances in Mathematics* **134** (1998), 90–145; the proof above uses the standard acyclic-matching consequence that one critical cell remains for each cell of the Morse CW model.
