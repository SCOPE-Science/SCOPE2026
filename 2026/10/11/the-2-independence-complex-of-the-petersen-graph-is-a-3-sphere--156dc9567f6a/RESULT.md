# The 2-independence complex of the Petersen graph is a 3-sphere
## Finding
Let \(P\) be the Petersen graph. Its \(2\)-independence complex satisfies
\[
\operatorname{Ind}_2(P)\simeq S^3.
\]
Here a face is a vertex subset for which every connected component of the induced subgraph has at most two vertices.

## Assumptions and scope
Use the standard Petersen graph with outer cycle vertices \(0,1,2,3,4\), inner vertices \(5,6,7,8,9\), spokes \(i\sim 5+i\), and inner pentagram edges \(5+i\sim 5+(i+2)\), with indices modulo \(5\). The claim is only about \(r=2\).

## Proof
Exhaustive enumeration gives \(260\) nonempty faces, with face vector \((10,45,90,80,30,5)\) in dimensions \(0\) through \(5\). Apply a staged vertex-toggle matching in the order \(0,1,\ldots,9\): at stage \(v\), pair each still-unmatched face not containing \(v\) with its extension by \(v\) whenever that extension is also a face and is still unmatched. The directed Hasse graph obtained by reversing matched incidences is acyclic.

The matching has exactly four critical cells: the vertex \(\{0\}\), the \(2\)-simplex \(\{1,4,6\}\), and the two \(3\)-simplices \(\{2,4,5,6\}\) and \(\{1,4,7,8\}\). Exact signed gradient-path summation gives Morse boundary
\[
\partial_3=(-1,-1):\mathbb Z^2\longrightarrow\mathbb Z.
\]
Thus the Morse CW complex has one \(0\)-cell, one \(2\)-cell, and two \(3\)-cells, with both \(3\)-cell attaching maps having degree \(-1\) on the \(2\)-sphere. Attaching either one of these \(3\)-cells along a degree-one map gives a contractible subcomplex. The remaining \(3\)-cell is consequently attached to a contractible space and contributes a single \(3\)-sphere. Hence \(\operatorname{Ind}_2(P)\simeq S^3\).

## Verification
Run `python3 verify.py`. The verifier reconstructs the graph and all faces, checks the full matching, performs an explicit topological-sort acyclicity test on the reversed Hasse diagram, and recomputes the two signed Morse boundary coefficients. It terminates with `PETERSEN_IND2_VERIFY_OK`.

## Relationship to prior work
Deshpande and Singh introduced and studied higher independence complexes and determined homotopy types for complete multipartite graphs, fully whiskered graphs, cycle graphs, and perfect rooted trees; their 2020 preprint is arXiv:2001.05448. Abdelmalek, Deshpande, Goyal, Roy, and Singh subsequently studied shellability and vertex decomposability for chordal families in arXiv:2106.10863. The Petersen graph is neither among the explicit families treated in those papers nor chordal. Searches for the exact Petersen \(2\)-independence homotopy type found no statement implying this computation.

## Limitations
This is a single exact benchmark at \(r=2\); it does not classify \(\operatorname{Ind}_r(P)\) for other values of \(r\), nor does it assert a general theorem for cubic or nonchordal graphs.

## References
1. P. Deshpande and A. Singh, “Higher Independence Complexes of graphs and their homotopy types,” arXiv:2001.05448, first posted 2020-01-15.
2. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, “Chordal graphs, higher independence and vertex decomposable complexes,” arXiv:2106.10863, first posted 2021-06-21.
