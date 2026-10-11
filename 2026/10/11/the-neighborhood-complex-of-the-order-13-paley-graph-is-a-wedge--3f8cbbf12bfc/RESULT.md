# The neighborhood complex of the order-\(13\) Paley graph is a wedge of \(25\) two-spheres
## Finding
Let \(P_{13}\) be the Paley graph on \(\mathbb Z/13\mathbb Z\), with \(x\) adjacent to \(y\) exactly when \(y-x\in\{\pm1,\pm3,\pm4\}\). Its Lovász neighborhood complex \(\mathcal N(P_{13})\) satisfies
\[
\mathcal N(P_{13})\simeq\bigvee^{25}S^2.
\]

## Assumptions and scope
The neighborhood complex consists of all nonempty vertex sets contained in the open neighborhood of some graph vertex. The graph is finite, simple, and loopless. The claim is only about the order-\(13\) Paley graph and does not assert a pattern for larger Paley graphs.

## Proof
The quadratic residues modulo \(13\) are \(\{\pm1,\pm3,\pm4\}\), so every vertex has six neighbors. Enumerating all subsets of the thirteen open neighborhoods gives exactly \(598\) nonempty simplices with face vector
\[
(13,78,221,195,78,13).
\]

Order the vertices as \(0,1,\ldots,12\). Starting with the full face poset, process these vertices in order. At stage \(v\), whenever an as-yet unmatched face \(\sigma\) omits \(v\) and \(\sigma\cup\{v\}\) is also an as-yet unmatched face, pair \(\sigma\) with \(\sigma\cup\{v\}\). This produces \(286\) disjoint cover pairs. Direct orientation of every Hasse cover upward on matched pairs and downward on unmatched covers yields an acyclic directed graph on all \(598\) simplices. Thus this is an acyclic discrete-Morse matching.

Exactly \(26\) simplices are unmatched: the vertex \(\{0\}\) and \(25\) triangles. There are no critical cells in dimensions \(1\) or above \(2\). Forman's discrete Morse theorem therefore gives a CW complex with one \(0\)-cell and \(25\) \(2\)-cells. Every \(2\)-cell attaches to the unique point, hence the CW complex is \(\bigvee^{25}S^2\).

## Verification
Run `python verify.py` beside `CERTIFICATE.json`. The verifier reconstructs the Paley graph and the entire neighborhood complex, checks the strongly regular common-neighbor counts \(2\) and \(3\), regenerates all \(286\) matching pairs, checks all \(2,067\) Hasse covers, and topologically sorts the resulting directed Hasse graph. It also recomputes boundary ranks over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\); in each characteristic the ranks are \((12,66,130,65,13)\) and the Betti vector is \((1,0,25,0,0,0)\).

## Relationship to prior work
Shukla's arXiv preprint 1802.04526, first public on 2018-02-13, studies neighborhood complexes of graphs of maximum degree at most \(3\) and of \(4\)-regular circulant graphs. Its circulant notation \(C_n(s,t)\) uses two step sizes and therefore does not include the \(6\)-regular Paley graph \(C_{13}(1,3,4)\). Matsushita's 2017 paper identifies the fundamental group of a neighborhood complex with an even graph fundamental group, but it does not determine this Paley complex or its higher-dimensional homotopy type. Exact searches under the aliases “Paley \(P_{13}\),” “\(QR(13)\),” “\(C_{13}(1,3,4)\),” and “strongly regular \((13,6,2,3)\)” found no prior statement implying the wedge of \(25\) two-spheres.

## Limitations
The proof is finite and exact for \(P_{13}\). It does not classify neighborhood complexes of all Paley graphs, all conference graphs, or all \(6\)-regular circulants. Search-based originality can retain residual bibliographic risk even after alias and implication checks.

## References
1. S. Shukla, “Homotopy type of the neighborhood complexes of graphs of maximal degree at most \(3\) and \(4\)-regular circulant graphs,” arXiv:1802.04526, first version 2018-02-13; Electronic Journal of Combinatorics 26(2), P2.4 (2019), DOI 10.37236/7549.
2. T. Matsushita, “Fundamental Groups of Neighborhood Complexes,” Journal of Mathematical Sciences, the University of Tokyo 24 (2017), 321–353, MSC 55Q05.
3. R. Forman, “Morse theory for cell complexes,” Advances in Mathematics 134 (1998), 90–145.
