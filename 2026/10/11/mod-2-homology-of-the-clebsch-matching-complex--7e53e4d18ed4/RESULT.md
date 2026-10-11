# Mod-\(2\) homology of the Clebsch matching complex
## Finding
Let \(C\) be the standard 5-regular Clebsch graph on the even-weight vectors of \(\mathbb F_2^5\), with two vertices adjacent exactly when their Hamming distance is \(4\). Let \(\operatorname{Match}(C)\) be the ordinary matching complex whose vertices are the edges of \(C\) and whose simplices are sets of pairwise disjoint graph edges. Then
\[
\widetilde H_i(\operatorname{Match}(C);\mathbb F_2)\cong
\begin{cases}
\mathbb F_2^{976},& i=5,\\
0,& i\neq 5.
\end{cases}
\]
The complex has dimension \(7\), so this is an exact concentration statement rather than a maximal-dimension tautology.

## Assumptions and scope
The graph is the 16-vertex, 40-edge, 5-regular Clebsch graph with strongly regular parameters \((16,5,0,2)\). The matching complex is the ordinary degree-at-most-one matching complex, not a generalized \(r\)-matching complex and not a perfect-matching complex. The coefficient field is exactly \(\mathbb F_2\). No assertion is made here about integral torsion or the homotopy type.

## Proof
The bundled verifier constructs the graph from first principles using the even-weight vectors of \(\mathbb F_2^5\). It checks that every vertex has degree \(5\), adjacent vertices have no common neighbors, and nonadjacent vertices have exactly two common neighbors, confirming the strongly regular parameters \((16,5,0,2)\).

It then exhaustively enumerates every matching. Including the empty face, the matching numbers by cardinality are
\[
1,40,620,4760,19190,39640,37740,12840,705.
\]
Thus the simplicial chain-group dimensions in degrees \(0\) through \(7\) are
\[
40,620,4760,19190,39640,37740,12840,705.
\]
As an independent face-count check, the verifier recomputes the same matching polynomial by the vertex-deletion recurrence that either leaves a chosen graph vertex unmatched or matches it to one of its neighbors.

For every simplex, the simplicial boundary over \(\mathbb F_2\) is obtained by deleting one selected graph edge. Exact Gaussian elimination over \(\mathbb F_2\), implemented twice with opposite pivot conventions, gives the boundary ranks
\[
39,581,4179,15011,24629,12135,705
\]
for the maps from degrees \(1\) through \(7\), respectively. The verifier also checks \(\partial^2=0\) on every simplex of cardinality at least three. Therefore
\[
\dim_{\mathbb F_2}\widetilde H_i
=
\dim C_i-\operatorname{rank}\partial_i-\operatorname{rank}\partial_{i+1}
\]
(with the usual reduced adjustment in degree \(0\)) gives the reduced Betti vector
\[
(0,0,0,0,0,976,0,0).
\]
The reduced Euler characteristic computed directly from the face vector is \(-976\), agreeing with the homology calculation.

## Verification
Running `python verify.py` reconstructs the graph, exhaustively enumerates all \(115536\) faces including the empty face, checks the graph parameters, independently recomputes the matching counts by vertex deletion, builds every mod-\(2\) simplicial boundary matrix, computes each boundary rank with two elimination pivot conventions, checks \(\partial^2=0\), and verifies the reduced Euler characteristic. The program terminates with `VERIFY_OK`.

## Relationship to prior work
Donovan and Scoville develop star-cluster and discrete-Morse methods for matching complexes and compute exact homotopy types for paths, cycles, centipedes, and Dutch windmills. Their full text contains no Clebsch or folded-cube instance. Jelić Milutinović, Jenne, McDonough, and Vega emphasize that exact topology is known for relatively few matching-complex families and study trees and polygonal-line or honeycomb families; their full text likewise contains no Clebsch or folded-cube case.

The Clebsch graph is also the projective cube \(PC(4)\). In the projective-cube sequence, \(PC(2)\cong K_4\), \(PC(3)\cong K_{4,4}\), and \(PC(4)\) is the Clebsch graph. Thus this calculation supplies a natural next exact matching-homology benchmark after the complete-graph and chessboard-complex cases. Searches under the aliases Clebsch graph, Greenwood--Gleason graph, folded 5-cube, projective cube \(PC(4)\), and independence complex of the line graph found no published statement implying the rank \(976\) concentration above.

## Limitations
This is an exhaustive finite computation for one highly symmetric graph. It proves only mod-\(2\) homology; it does not determine integral homology, simple-homotopy type, or a general formula for projective cubes. Literature searches cannot exclude every unindexed or differently phrased finite computation, so a residual originality risk remains.

## References
1. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780v1, first posted 2022-07-27; primary MSC 57Q70.
2. M. Jelić Milutinović, H. Jenne, A. McDonough, and J. Vega, *Matching complexes of trees and applications of the matching tree algorithm*, arXiv:1905.10560.
3. M. Chen, R. Naserasr, and A. Sarti, *Signed projective cubes, a homomorphism point of view*, arXiv:2406.10814v1.
