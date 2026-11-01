# Mixed-dimensional sphere wedge for the bidirected \(K_{3,4}\) multipath complex

## Finding

Let \(D\) be the digraph obtained by replacing every edge of the complete bipartite graph \(K_{3,4}\) by two opposite arcs. Let \(X(D)\) be its multipath complex: the vertices of \(X(D)\) are the \(24\) directed arcs of \(D\), and a set of arcs is a face precisely when its connected components are directed paths and isolated graph vertices. Then

\[
X(D)\simeq\bigvee^{37}S^3\ \vee\ \bigvee^{48}S^4.
\]

The nonzero reduced integral homology groups are \(\widetilde H_3(X(D);\mathbb Z)\cong\mathbb Z^{37}\) and \(\widetilde H_4(X(D);\mathbb Z)\cong\mathbb Z^{48}\); there is no integral torsion. The complex is pure of dimension \(5\) and **is not shellable**.

## Assumptions and scope

The digraph has vertex classes \(A=\{0,1,2\}\) and \(B=\{3,4,5,6\}\). For each \(a\in A\), \(b\in B\), it has both arcs \(a\to b\) and \(b\to a\), and no other arcs. Each simplex is an arc set with at most one selected incoming and at most one selected outgoing arc at each graph vertex, and with no directed cycle; isolated vertices are allowed. The assertion applies to this single, completely specified digraph. It makes no assertion for all bidirected complete bipartite graphs.

## Proof

An exact exhaustive combinatorial certificate, provided by `verify_multipath_k34.py`, proves the following finite assertions. Its arc order is the nested order \((a,b),(b,a)\) over \(a\in A\), \(b\in B\), and its fixed toggle order is explicitly embedded in the program.

**Completeness of the face set.** An edge-set is a multipath if and only if it has incoming/outgoing degrees at most one and has no directed cycle. Any multipath on seven graph vertices has at most six arcs. The checker reconstructs all legal faces both by recursive extension and by an independent enumeration of every arc subset of cardinality at most six. These procedures agree on precisely \(3301\) augmented faces. The simplex counts in dimensions \(-1,0,1,2,3,4,5\) are respectively \(1,24,204,768,1296,864,144\). Every face with fewer than six arcs extends by at least one arc, so all \(144\) facets have dimension \(5\).

**Acyclic Morse matching.** Traverse all faces through the explicit sequence of arc toggles in the checker, pairing each still-unpaired face not containing the toggle arc with its still-unpaired admissible coface obtained by adding that arc. This yields \(1608\) pairs in the augmented face poset, exactly one involving the empty face. After omitting that one pair and the empty face, it yields an ordinary discrete-Morse matching with \(1607\) pairs and precisely one critical vertex, \(37\) critical three-simplices and \(48\) critical four-simplices. The checker constructs **all \(13104\) codimension-one Hasse incidences**. Orient matched covers upward and unmatched covers downward. A complete topological sort visits every one of the \(3301\) augmented faces, proving that the matching has no closed gradient path. Omitting the empty vertex from this acyclic digraph retains acyclicity.

**Exact integral attaching degrees.** Use each matched pair \((\alpha,\beta)\), with \(\beta\) one dimension above \(\alpha\), to eliminate the coefficient \(\pm1\) of \(\alpha\) in the signed simplicial boundary \(\partial\beta\). For a matched lower face \(\alpha\), express its critical-chain projection by the corresponding relation \(\alpha=-\varepsilon\sum_{\gamma\ne\alpha}[\beta:\gamma]\gamma\), where \(\varepsilon=[\beta:\alpha]\in\{\pm1\}\), recursively projecting every \(\gamma\). Every matched upper face projects to zero; critical faces project to their basis vectors. The acyclic matching ensures termination of this exact integer recursion. Applying it to all \(48\) critical four-cells gives a \(37\times48\) **zero integer Morse boundary matrix**. This is an exact, not a modular or floating-point, computation.

By the discrete Morse theorem the complex is homotopy equivalent to a CW complex with one zero-cell, \(37\) three-cells, \(48\) four-cells and no other cells. Its three-skeleton is \(\bigvee^{37}S^3\), which is two-connected. The Hurewicz isomorphism \(\pi_3\cong H_3\) identifies the homotopy classes of the four-cell attaching maps with their degree vectors. Since every vector is zero, every attaching map is nullhomotopic. The stated sphere-wedge homotopy equivalence follows, giving integral homology without torsion.

Finally, any pure shellable five-dimensional simplicial complex has reduced homology only in dimension five (or is contractible). Here reduced homology is nonzero in dimensions three and four, so \(X(D)\) is not shellable.

## Verification

Run `python3 verify_multipath_k34.py` with a standard Python 3 installation; no external packages or network access are needed. The checker verifies the complete face set twice, purity and facet count, every matching pair, global directed Hasse acyclicity, every entry of the exact integer Morse boundary, and independently computes all simplicial boundary ranks over \(\mathbb F_2\). Those ranks, in dimensions zero through five, are \((1,23,181,587,672,144)\). They independently recover mod-two Betti ranks \((0,0,0,37,48,0)\). The final success marker is `K34_BIDIRECTED_MULTIPATH_MIXED_WEDGE_EXACT_OK`.

The finite exhaustive certificate is part of the proof: it checks the entire specified finite complex and the full matching, not a sample or a conjectural extrapolation. The integral topological conclusion uses the exact signed Morse boundary and Hurewicz theorem, not the mod-two check.

## Relationship to prior work

Caputi, Collari, Di Trani and Smith (2022, arXiv:2208.04656v1) introduce the multipath-complex framework and calculate Euler characteristics for complete bipartite digraphs with all edges **oriented one way**. That construction has \(12\) arcs in the present sizes and is a chessboard/matching complex. The object here has \(24\) arcs, including directed two-cycles, so their Euler formula and acyclic orientation comparison do not determine its homotopy type.

Caputi, Collari and Smith (2026, arXiv:2601.05670v1) study bidirectional paths and polygons, giving connectivity and homology results. Their acyclic-blow-up comparison is explicitly restricted to digraphs without oriented cycles; the present object contains directed two-cycles. Neither the bidirectional polygon theorems nor that acyclic comparison imply the mixed-dimensional homotopy type proved here. Previously studied matching, two-matching, and ordinary discrete-Morse complexes of the **undirected** \(K_{3,4}\) also have different simplex sets and cannot be substituted for \(X(D)\).

The exact finite homotopy result is consistent with known adjacent bidirected complete-bipartite examples, but is not their formal consequence. Search-based originality has residual risk from equivalent unindexed or differently named calculations.

## Limitations

This theorem determines a single natural finite complex, not the family \(\overleftrightarrow{K_{3,n}}\) for arbitrary \(n\). It provides no natural equivariant homotopy splitting under \(S_3\times S_4\), and does not classify all bidirectional multipartite digraphs. Reproducibility of the finite proof does not constitute independent review of its significance or literature completeness.

## References

1. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1, publicly posted 2022-08-09. https://arxiv.org/abs/2208.04656
2. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, publicly posted 2026-01-09. https://arxiv.org/abs/2601.05670
3. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145. Standard acyclic-matching-to-CW theorem.
