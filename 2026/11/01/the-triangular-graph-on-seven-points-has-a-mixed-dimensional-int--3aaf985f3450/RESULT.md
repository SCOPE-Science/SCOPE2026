# The triangular graph on seven points has a mixed-dimensional integral sphere-wedge neighborhood complex

## Finding
Write \(T_7=L(K_7)\), the triangular (Johnson) graph whose 21 vertices are the two-element subsets of \(\{0,1,2,3,4,5,6\}\). Two such vertices are adjacent when their intersection has size exactly one. For the ordinary **open** Lovász neighborhood complex, the exact integral homotopy type is
\[
\mathcal N(T_7)\simeq \bigvee^{246} S^3\ \vee\ \bigvee^{7} S^4.
\]
Thus \(\widetilde H_3(\mathcal N(T_7);\mathbb Z)\cong\mathbb Z^{246}\), \(\widetilde H_4(\mathcal N(T_7);\mathbb Z)\cong\mathbb Z^7\), and every other reduced integral homology group vanishes. This is a homotopy classification, not just a homology computation. The complex is pure of dimension nine and not shellable.

## Assumptions and scope
For a loopless finite graph \(G\), a nonempty set of its vertices is a simplex of \(\mathcal N(G)\) precisely when all of them have a common **open** neighbor. The empty face is included when enumerating the augmented face poset. Vertices of \(T_7\) are ordered lexicographically as two-element sets \((i,j)\) with \(0\le i<j\le6\). Each has exactly ten neighbors. There are 21 ten-vertex neighborhood facets (dimension nine). This result is about \(T_7\) only; no formula for larger triangular graphs is asserted.

## Proof
**1. Exact finite simplicial model.** For each pair \(a\subset\{0,\ldots,6\}\) of size two, let \(F_a\) consist of all other pairs meeting \(a\) in exactly one element. Form the union of the full simplices on \(F_a\), one for every pair \(a\). Each simplex is represented as a 21-bit integer. Exhaustively taking submasks of these 21 facets produces 18,495 distinct augmented faces (including the empty face), with ordinary face vector, by dimensions zero through nine,
\[
(21,210,1190,3780,5187,4410,2520,945,210,21).
\]
This generation is exhaustive because a set has a common neighbor if and only if it lies in some \(F_a\).

**2. A finite acyclic discrete-Morse matching.** Begin with all augmented faces unpaired. For each vertex bit \(i=0,1,\ldots,20\) in order, scan currently unpaired faces \(f\) in ascending integer order. If bit \(i\) is absent from \(f\) and both \(f\) and \(f\cup\{i\}\) are still unpaired, pair them and remove both from further consideration. There are exactly 9,121 pairs, including the pair \((\varnothing,\{(0,1)\})\). The remaining 253 augmented faces consist of exactly 246 faces of dimension three and seven of dimension four. On the ordinary nonempty face poset, omit the empty-face pair, leaving a single critical vertex and the same critical higher cells.

Orient every unmatched covering relation of the ordinary face poset downward, and reverse each matched covering relation. The accompanying independent directed-graph traversal constructs all 98,805 covering relations and performs a complete topological sort on all 18,494 nonempty faces. It visits every face, establishing that the discrete vector field contains **no closed gradient path**. This is a finite exhaustive certificate of acyclicity, rather than an inference from the critical-cell counts. Forman's discrete Morse theorem consequently supplies a CW complex with one zero-cell, 246 three-cells, seven four-cells, and no other cells.

**3. Exact integral attaching degrees.** Orient each simplex by ascending vertex-bit index. For a face \(g\) with ordered vertices \((i_0,\ldots,i_q)\), the incidence of its facet obtained by omitting \(i_j\) is \((-1)^j\). The signed Morse boundary from the critical four-cells to the critical three-cells is computed by *integer* gradient-path reduction as follows. A critical three-face projects to its own basis vector; a three-face paired as an upper cell with a two-face projects to zero. If a three-face \(f\) is paired as a lower face with an upper four-face \(g\), write \([g:f]\in\{+1,-1\}\) for its signed incidence and define
\[
P(f)=-[g:f]\sum_{h\text{ facet of }g,\ h\ne f}[g:h]P(h).
\]
Acyclicity makes these recurrences finite. For each critical four-face \(q\), its Morse boundary is \(\sum_{f\text{ facet of }q}[q:f]P(f)\). Evaluating all seven columns by exact integer arithmetic gives the **zero** \(246\)-by-\(7\) matrix. The complete reproducible enumeration, directed-cycle test, and signed reductions are in `verify.py`.

**4. From the Morse model to homotopy type.** Because the Morse CW model has a point and only three- and four-dimensional cells, its three-skeleton is a wedge of 246 three-spheres. The Hurewicz isomorphism \(\pi_3(\bigvee^{246}S^3)\cong H_3(\bigvee^{246}S^3;\mathbb Z)\cong\mathbb Z^{246}\) identifies the attaching homotopy class of any four-cell with its vector of integral cellular incidence degrees. All seven vectors are zero by Step 3, so all four-cells attach nullhomotopically. This proves the displayed sphere-wedge equivalence. Finally a pure shellable nine-dimensional complex can only have reduced homology in dimension nine; nonzero homology in dimensions three and four excludes shellability.

## Verification
Running `python verify.py` in a standard Python 3 environment, without third-party dependencies, regenerates all faces and the deterministic sequential matching; checks every directed Hasse incidence with a topological sort; reconstructs the seven integral Morse boundary columns; and independently computes all simplicial boundary ranks over \(\mathbb F_2\). The boundary ranks from dimension one to nine are
\[
(20,190,1000,2534,2646,1764,756,189,21),
\]
so the independently reconstructed mod-two Betti ranks are \(246\) and \(7\) in dimensions three and four. This mod-two calculation is a cross-check only: the integral and homotopy claims depend on the exact signed Morse computation and the attaching-map argument. Output is recorded in `verification_output.txt`.

## Relationship to prior work
An earlier public exact computation, *Mixed-dimensional mod-two neighborhood homology first appears at \(T_7\)*, determines precisely the same two mod-two Betti ranks for \(T_7\). Its full public proof and verifier use binary elimination and **explicitly withhold** any conclusion on integral torsion, integral attaching maps, or homotopy type. Those mod-two ranks are prior work, not a new contribution here. This finding supplies the new integral acyclic Morse model, zero signed attaching matrix, and full sphere-wedge homotopy conclusion. Algebraic possibility alone shows why mod-two homology does not imply these conclusions: an even, nonzero integral attaching degree can be invisible modulo two.

Shukla's earlier neighborhood-complex homotopy classification concerns graphs of maximum degree at most three and four-regular circulant graphs; the triangular graph here is ten-regular and is not a four-regular circulant. Braun–Vega treat effects of Hajós-type graph operations on neighborhood complexes, not this exact graph. Goyal–Shukla–Singh classify **clique complexes** of line graphs, where a simplex is a clique, whereas this result concerns the very different common-neighbor complex. Fröberg's published full-text study addresses Stanley–Reisner rings of neighborhood complexes for paths, stars, complete and multipartite graphs, but does not give the \(T_7\) homotopy type. No broader covering result was identified in the inspected sources. Unindexed equivalent work and stronger theorems under graph-homomorphism-complex terminology remain possible.

## Limitations
This exact result is confined to the 21-vertex triangular graph \(T_7\), not the whole family \(T_n\). The checker verifies a finite object exhaustively; it is not a general proof schema for larger graphs. It does not determine the integral automorphism-group representation or canonical homotopy equivalence. The originality assessment is based on specified inspected literature and indexed records, not an exhaustive theorem-uniqueness certificate.

## References
1. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526v1, first posted 2018-02-13; Electronic Journal of Combinatorics 26 (2019), P2.4.
2. B. Braun and J. Vega, *Hajós-Type Constructions and Neighborhood Complexes*, arXiv:1812.07991v1, first posted 2018-12-19; SIAM Journal on Discrete Mathematics 34 (2020), 2424–2447.
3. S. Goyal, S. Shukla, and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130v1, first posted 2020-09-25.
4. R. Fröberg, *Stanley–Reisner rings of neighborhood complexes and linear resolutions*, Journal of Algebraic Combinatorics 63 (2026), article 56; DOI 10.1007/s10801-026-01530-x.
5. *Mixed-dimensional mod-two neighborhood homology first appears at \(T_7\)*, public indexed calculation dated 2026-10-11: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-mixed-dimensional-mod-two-neighborhood-homology-first-appears-at--5026f3f1e8ec .
6. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
