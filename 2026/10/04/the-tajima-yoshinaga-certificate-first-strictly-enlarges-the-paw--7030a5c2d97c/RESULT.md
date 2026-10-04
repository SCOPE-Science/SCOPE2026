# The Tajima–Yoshinaga certificate first strictly enlarges the pawful class uniquely at six vertices
## Finding
Let \(\mathcal T\) be the class of finite simple connected graphs of diameter at most \(2\) that admit maps \(f_1,f_2\) satisfying Tajima--Yoshinaga Definition 5.1, and let \(\mathcal P\) be the pawful graphs. Up to isomorphism, \(\mathcal T\setminus\mathcal P\) has no graph on at most \(5\) vertices and exactly one graph on \(6\) vertices, namely Tajima--Yoshinaga's graph \(G_1\). Equivalently, their sufficient condition first strictly enlarges the pawful class at order \(6\), uniquely. The counts \((|\mathcal P_n|,|\mathcal T_n|)\) for \(n=1,\ldots,6\) are \((1,1),(1,1),(2,2),(5,5),(13,13),(47,48)\).

For the six-vertex exceptional class, use the labels of Tajima--Yoshinaga Figure 3. Its edge set is
\[
\{\{1,2\},\{1,5\},\{2,5\},\{2,3\},\{5,4\},\{3,4\},\{2,6\},\{6,4\},\{5,6\},\{6,3\}\}.
\]
The complete small-order census is:

| vertices | all simple graph types | connected types | connected diameter-\(\le 2\) | pawful | Definition-5.1 certificate | certified but non-pawful |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 2 | 2 | 1 | 1 | 1 | 1 | 0 |
| 3 | 4 | 2 | 2 | 2 | 2 | 0 |
| 4 | 11 | 6 | 5 | 5 | 5 | 0 |
| 5 | 34 | 21 | 15 | 13 | 13 | 0 |
| 6 | 156 | 112 | 60 | 47 | 48 | 1 |

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. The phrase “Definition-5.1 certificate” means precisely the existence of the maps \(f_1:X'\to X\) and \(f_2:Y'\to Y\) satisfying conditions (i)--(iii) of Tajima--Yoshinaga Definition 5.1; in particular the graph has diameter at most \(2\). “Pawful” is the distance-two triple condition recalled in their Definition 3.3.

The statement is only about the sufficient condition of Definition 5.1 through six vertices. It is not a classification of all diagonal graphs. In particular, Tajima--Yoshinaga Example 5.5 gives a five-vertex non-pawful diagonal graph \(G_2\) that does not admit their Definition-5.1 certificate.

## Proof
For each \(n\le 6\), encode a labeled simple graph by a bit mask on the \(\binom n2\) possible edges. Partition all \(2^{\binom n2}\) masks into orbits under all \(n!\) vertex permutations. Taking one canonical mask from each orbit yields, respectively, \(1,2,4,11,34,156\) isomorphism classes for \(n=1,\ldots,6\). Because the orbit union is checked to contain every mask, no external graph catalogue is needed for completeness.

For every connected diameter-at-most-two representative, test pawfulness directly from all ordered triples. To decide Definition 5.1 exactly, first note that \(f_1(a,c)\) is simply a choice of a common neighbor for every ordered pair \((a,c)\) at distance \(2\). Likewise \(f_2(\alpha,\beta,\delta)\) chooses a common neighbor \(\gamma\) of \(\beta\) and \(\delta\) for every ordered triple with \(d(\alpha,\beta)=1\) and \(d(\beta,\delta)=2\).

Condition (iii) filters the allowable \(f_2\)-choices: when \(d(\alpha,\gamma)=2\), the chosen \(\gamma\) must be the unique common neighbor of \(\beta\) and \(\delta\). For condition (ii), a selected quadruple \((\alpha,\beta,\gamma,\delta)\) forbids every selected quadruple of the form \((*,\alpha,\beta,\gamma)\) and forbids \(f_1(\alpha,\gamma)=\beta\) whenever \(d(\alpha,\gamma)=2\). Thus, after fixing \(f_2\), the remaining \(f_1\)-choices are independent. Exhaustive backtracking over all allowable \(f_2\)-choices, followed by the independent \(f_1\)-availability test, is therefore equivalent to the existence clause in Definition 5.1.

The resulting census is the table above. No certified non-pawful class occurs through five vertices. At six vertices exactly one occurs. Canonical isomorphism testing identifies that class with the edge-labeled graph in Tajima--Yoshinaga Figure 3. As a separate consistency check, their explicit ten values of \(f_1\) and thirty values of \(f_2\) are replayed on that graph and satisfy the exact domains and all three conditions of Definition 5.1.

## Verification
Run `python3 verify_small_pawful_boundary.py`. The verifier uses only the Python standard library. It reconstructs all graph-isomorphism orbits through six vertices, checks that the orbit union equals every labeled graph, recomputes the full census, verifies the source-labeled \(G_1\) and its published \(f_1,f_2\) maps, and independently searches for a certificate on each relevant isomorphism type. Successful replay ends with `VERIFY_OK`.

## Relationship to prior work
Gu introduced pawful graphs and proved their magnitude homology is diagonal. Tajima and Yoshinaga introduced the wider Definition-5.1 sufficient condition and proved that every graph carrying such a certificate has Asao--Izumihara complexes homotopy equivalent to wedges of spheres, hence is diagonal. Their Example 5.4 exhibits the six-vertex graph \(G_1\) as a non-pawful graph carrying the certificate, while Example 5.5 exhibits a five-vertex non-pawful diagonal graph outside that certificate class.

The inspected paper gives the witness \(G_1\) but does not state that six vertices are the first order at which Definition 5.1 strictly enlarges the pawful class, nor that \(G_1\) is the unique strict member at that order. Targeted searches under “non-pawful”, “Definition 5.1”, “smallest”, “minimal”, “six vertices”, “unique”, and “Asao--Izumihara” aliases did not locate a published census or an implication yielding this finite classification.

## Limitations
The exhaustive claim stops at six vertices. It says nothing about the number or structure of strict Definition-5.1 extensions from seven vertices onward. It also does not classify diagonal graphs themselves: diagonality is broader than this sufficient certificate, as the five-vertex \(G_2\) already shows. Literature searches reduce but do not eliminate the possibility of an equivalent small-graph census stated under terminology not inspected here.

## References
1. Y. Tajima and M. Yoshinaga, “Magnitude homology of graphs and discrete Morse theory on Asao--Izumihara complexes,” arXiv:2110.02458v1, first posted 2021-10-06; Homology, Homotopy and Applications 25 (2023), no. 1, 331--343, DOI 10.4310/HHA.2023.v25.n1.a17.
2. Y. Gu, “Graph magnitude homology via algebraic Morse theory,” arXiv:1809.07240, first posted 2018-09-19.
