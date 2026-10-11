# The Desargues independence complex is \(S^4\vee\bigvee^5 S^5\)
## Finding
Let \(D=G(10,3)\) be the Desargues graph. Its independence complex has homotopy type
\[
\operatorname{Ind}(D)\simeq S^4\vee\bigvee^{5}S^5.
\]
Thus a canonical cubic symmetric graph has an independence complex with essential homotopy in two adjacent dimensions.

## Assumptions and scope
The graph is the generalized Petersen graph \(G(10,3)\): it has outer vertices \(u_i\), inner vertices \(v_i\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\), with indices modulo \(10\). The independence complex contains exactly the vertex subsets spanning no graph edge. The statement concerns this finite graph only; it does not assert a formula for all generalized Petersen graphs or all bipartite Kneser graphs.

## Proof
Exhaustive enumeration gives \(6,211\) nonempty faces and face vector
\[
(20,160,660,1510,1924,1320,480,115,20,2).
\]
A deterministic staged element matching on the nonempty face poset, using the vertex order recorded in `certificate.json`, contains \(3,102\) matched cover pairs. Direct orientation of every one of the \(30,360\) Hasse covers and a topological sort verify that the matching is acyclic. Its critical cells consist of one cell in dimension \(0\), one in dimension \(4\), and five in dimension \(5\).

Forman's theorem therefore gives a CW complex with one \(0\)-cell, one \(4\)-cell, and five \(5\)-cells. The integral Morse boundary from each critical \(5\)-cell to the unique critical \(4\)-cell is computed by signed gradient-path recursion and is exactly zero. Hence the \(4\)-skeleton is \(S^4\), and each \(5\)-cell is attached by a map \(S^4\to S^4\) of degree zero. Since \(\pi_4(S^4)\cong\mathbb Z\) via degree, every such attaching map is null-homotopic. The resulting CW complex is therefore \(S^4\vee\bigvee^5 S^5\).

## Verification
Running `verify.py` reconstructs the graph and every independent set from the defining edge rule, rebuilds the matching, verifies the entire directed Hasse graph is acyclic, recomputes all signed Morse boundary coefficients, and independently computes the full simplicial boundary ranks over \(\mathbb F_2\). The reduced mod-\(2\) Betti numbers are \(1\) in degree \(4\), \(5\) in degree \(5\), and zero otherwise, agreeing with the claimed wedge. No random sample or incomplete enumeration is used.

## Relationship to prior work
Matsushita and Wakatsuki determine exact wedge-of-spheres homotopy types for a substantial family of grid-graph independence complexes; their paper supplies the middle-window topological-combinatorics direction and has primary MSC 55P10. Tsukuda proves that the independence complex of any finite bipartite graph is homotopy equivalent to a suspension of an Alexander-dual hypergraph complex. Since the Desargues graph is bipartite, that theorem gives a structural reduction but does not evaluate the resulting complex for the Desargues configuration. Work on bipartite Kneser graphs by Kumar, Singh, and Verma studies graded Betti numbers and edge-ideal regularity rather than this exact independence-complex homotopy type. Searches under the aliases Desargues graph, \(G(10,3)\), bipartite Kneser graph \(H(5,2)\), and the bipartite double cover of the Petersen graph did not locate an exact homotopy computation matching the statement above.

## Limitations
The result is finite and graph-specific. The literature comparison cannot rule out an unindexed computation under another terminology; this remains the principal originality risk. The proof uses an exhaustive certificate rather than a conceptual family-level recurrence.

## References
1. T. Matsushita and S. Wakatsuki, *Independence complexes of \((n\times6)\)-grid graphs*, Homology, Homotopy and Applications 26 (2024), 15–27, arXiv:2207.10363, DOI:10.4310/HHA.2024.v26.n1.a2.
2. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), 28–46, DOI:10.55016/ojs/cdm.v12i1.62277.
3. A. Kumar, P. Singh, and R. Verma, *Certain homological invariants of bipartite Kneser graphs*, Journal of Algebra and Its Applications, DOI:10.1142/S0219498822502061.
