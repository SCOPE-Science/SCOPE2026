# The Tutte–Coxeter independence complex is a wedge of nine eight-spheres
## Finding
Let \(T\) be the Tutte–Coxeter graph in its canonical duad–syntheme model. Then
\[
\operatorname{Ind}(T)\simeq\bigvee^{9}S^{8}.
\]
Thus its reduced integral homology is free of rank \(9\) in degree \(8\) and vanishes in every other degree.

## Assumptions and scope
Take a six-element set \(X=\{0,1,2,3,4,5\}\). A duad is a two-element subset of \(X\), and a syntheme is a partition of \(X\) into three duads. The graph \(T\) has the \(15\) duads and \(15\) synthemes as vertices, with a duad adjacent to a syntheme exactly when the duad occurs in that partition. This gives the standard \(30\)-vertex, \(45\)-edge Tutte–Coxeter graph. The complex \(\operatorname{Ind}(T)\) consists of all independent vertex sets of \(T\).

The statement is specific to this graph. It does not assert a general formula for independence complexes of incidence graphs or cubic cages.

## Proof
Enumerating independent sets in the duad–syntheme model gives the nonempty face vector
\[
(30,390,2890,13515,41736,86610,120690,111225,66090,24948,6420,1370,240,30,2),
\]
so there are \(476{,}186\) nonempty faces. The ordinary Euler characteristic is \(10\), hence the reduced Euler characteristic is \(9\).

Order the \(30\) graph vertices by the lexicographic duad list followed by the lexicographic syntheme list. Apply successive element toggles to the nonempty face poset: at stage \(v\), pair a currently unmatched independent face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever the latter is still unmatched. The resulting matching contains exactly \(238{,}088\) pairs. Exactly ten faces remain unmatched: one vertex and nine faces of cardinality \(9\), hence one critical \(0\)-cell and nine critical \(8\)-cells.

Acyclicity is not inferred from the face counts. The verifier constructs every one of the \(3{,}461{,}400\) nonempty-face Hasse covers, reverses precisely the matched covers, and topologically sorts the entire directed Hasse graph. All \(476{,}186\) nodes are processed, proving that the matching is acyclic. Forman's discrete Morse theorem therefore gives a CW model with one \(0\)-cell and nine \(8\)-cells and no cells in dimensions \(1\) through \(7\). Every attaching map of an \(8\)-cell lands in the point-like \(7\)-skeleton, so this CW model is \(\bigvee^{9}S^{8}\).

## Verification
Run `python verify.py`. The checker independently constructs all duads and synthemes, verifies that the incidence graph has \(30\) vertices, \(45\) edges, degree \(3\) at every vertex, and girth \(8\), enumerates all independent faces, verifies the stated face vector and Euler characteristic, reconstructs every matching pair, checks every pair is a valid Hasse edge, builds the complete Morse-oriented Hasse graph, and verifies acyclicity by Kahn topological sorting. The expected terminal markers are `ACYCLIC_MATCHING_OK` and `VERIFY_OK`.

## Relationship to prior work
Matsushita and Wakatsuki study exact homotopy types of independence complexes of grid graphs and emphasize that such homotopy types are difficult to determine even for simply described graph families. Their work supplies a topology-primary literature anchor but does not treat the Tutte–Coxeter graph. Tsukuda proves a broad structural description for independence complexes of bipartite incidence graphs in terms of suspension and Alexander duality; that theorem applies at the level of graph class but does not evaluate the present complex as a nine-fold wedge of eight-spheres. Perarnau and Perkins study independent-set extremal questions for cubic graphs of prescribed girth and single out the Tutte–Coxeter graph in that enumerative setting; their results concern counts and occupancy rather than this homotopy type.

Searches were also made under the aliases Tutte \(8\)-cage, Cremona–Richmond incidence graph, Levi graph of \(GQ(2,2)\), and the generalized quadrangle \(W(2)\). No inspected source stated an equivalent exact homotopy type.

## Limitations
The proof is finite and exact for the canonical \(30\)-vertex graph, not a family theorem. The originality comparison is necessarily literature-bounded: a differently indexed computation under another alias could have been missed. The mathematical conclusion itself depends only on the explicit graph construction and the complete acyclic-matching verification, not on a database lookup or a numerical heuristic.

## References
1. T. Matsushita and S. Wakatsuki, *Independence complexes of \(n\times 6\)-grid graphs*, arXiv:2207.10363, first public 2022-07-21. Primary MSC 2020: 55P10.
2. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12(1), 2017, DOI 10.55016/ojs/cdm.v12i1.62277.
3. G. Perarnau and W. Perkins, *Counting independent sets in cubic graphs of given girth*, Journal of Combinatorial Theory, Series B 133 (2018), DOI 10.1016/j.jctb.2018.04.009.
