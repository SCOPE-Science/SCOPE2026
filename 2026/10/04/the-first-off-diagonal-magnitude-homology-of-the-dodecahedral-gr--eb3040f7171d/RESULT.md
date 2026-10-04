# The first off-diagonal magnitude homology of the dodecahedral graph has mod-2 rank 360
## Finding
For the dodecahedral graph \(D\cong GP(10,2)\) with its shortest-path metric, \(\dim_{\mathbb F_2}\operatorname{MH}_{3,4}(D;\mathbb F_2)=360\).

## Assumptions and scope
The graph \(D\) is the simple 20-vertex generalized Petersen graph \(GP(10,2)\): outer edges join \(u_i\) to \(u_{i+1}\), spokes join \(u_i\) to \(v_i\), and inner edges join \(v_i\) to \(v_{i+2}\), with indices modulo \(10\). Distances are graph shortest-path distances. Magnitude chains use the standard convention that a generator \((x_0,\ldots,x_k)\) has adjacent entries distinct and total length \(\sum_i d(x_i,x_{i+1})=\ell\). Coefficients in the claimed calculation are \(\mathbb F_2\).

## Proof
At length \(\ell=4\), exhaustive generation gives
\[
\dim C_{2,4}=1440,\qquad \dim C_{3,4}=3240,\qquad \dim C_{4,4}=1620.
\]
For an internal position, the magnitude differential deletes that vertex exactly when it is smooth, namely when \(d(x_{i-1},x_{i+1})=d(x_{i-1},x_i)+d(x_i,x_{i+1})\). Over \(\mathbb F_2\), exact sparse elimination gives
\[
\operatorname{rank}(\partial_3)=1320,\qquad \operatorname{rank}(\partial_4)=1560.
\]
The computation also verifies \(\partial_3\partial_4=0\). Therefore
\[
\dim \operatorname{MH}_{3,4}=(3240-1320)-1560=360.
\]

## Verification
`verify_magnitude_dodeca.py` reconstructs \(GP(10,2)\) without external libraries, computes all-pairs shortest-path distances, generates the three required chain groups, and constructs the magnitude differentials directly from the smooth-point criterion. Chain counts are independently checked by a dynamic-programming count. Each boundary rank is computed twice, once from column bitsets and once from transposed row bitsets. Every column of \(\partial_4\) is explicitly checked to map to zero under \(\partial_3\). Replay terminates with `VERIFY_OK`.

The verifier also records that the graph has 20 vertices, 30 edges, diameter 5, and that vertices 0 and 4 have two shortest paths of length 4. The latter is a direct witness that the graph is not geodetic, so the general geodetic-space computation of Asao–Wakatsuki does not imply this case.

## Relationship to prior work
Asao–Hiraoka–Kanazawa define the same magnitude chain complex and prove girth-controlled vanishing near the diagonal. Their paper gives a broad structural motivation for examining the first off-diagonal groups of a girth-5 graph but does not state the dodecahedral calculation. Gu's full-text computation treats trees, a pawful class, the icosahedral graph, and cycle graphs. Asao–Wakatsuki later give a complete computation for geodetic metric spaces and explicit Moore-graph examples (cycles, Petersen, Hoffman–Singleton, and the hypothetical missing Moore graph); the dodecahedral graph is not geodetic, as the packaged witness shows. Exact-name and alias searches for the dodecahedral graph, \(GP(10,2)\), and bidegree \((3,4)\), together with semantic published-finding corpus searches, found no checked source stating or implying the rank 360 claim.

## Limitations
The claim is only the single bidegree \((3,4)\) over \(\mathbb F_2\). It does not determine the integral group, possible torsion, other bidegrees, or a closed formula for a graph family. Absence from the checked literature is not a proof of global novelty; an obscure or poorly indexed computation may exist.

## References
1. Y. Asao, Y. Hiraoka, S. Kanazawa, “Girth, magnitude homology, and phase transition of diagonality”, arXiv:2101.09044, first public 2021-01-22; primary MSC 55N35 in the published record.
2. Y. Gu, “Graph magnitude homology via algebraic Morse theory”, arXiv:1809.07240.
3. Y. Asao, S. Wakatsuki, “Minimal projective resolution and magnitude homology of geodetic metric spaces”, arXiv:2408.12147.
4. Wolfram MathWorld, “Dodecahedral Graph”, identifying the graph with \(GP(10,2)\).
