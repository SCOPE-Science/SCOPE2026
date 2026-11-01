# Mixed-dimensional integral homotopy of the four-cube matching complex

## Finding
The graph \(Q_4\) has vertices \(\{0,1\}^4\), with an edge whenever two bit strings differ in exactly one coordinate. Let \(\mathcal M(Q_4)\) be its **ordinary matching complex**: the vertices of this simplicial complex are the 32 edges of \(Q_4\), and a face is a set of pairwise vertex-disjoint graph edges. There is an integral homotopy equivalence
\[
\boxed{\mathcal M(Q_4)\simeq S^4\vee\bigvee^{130}S^5.}
\]
Its reduced integral homology is \(\mathbb Z\) in degree four, \(\mathbb Z^{130}\) in degree five, and zero otherwise. All homology is torsion-free. These statements concern the full ordinary matching complex, **not** the subcomplex of perfect matchings.

## Assumptions and scope
This is a finite graph over the integers and an ordinary topological homotopy equivalence; no assumption on a field of coefficients is used. Identify cube vertices with integers from zero through fifteen, using four-bit binary expansion. List the 32 graph edges in lexicographic construction order: for each \(u=0,\ldots,15\), and each \(j=0,1,2,3\), include \((u,u\oplus2^j)\) if \(u<u\oplus2^j\). This gives a fixed edge index \(e=0,\ldots,31\). A simplex is represented by the 32-bit mask of the corresponding disjoint edge indices. The empty face is included only in augmented bookkeeping and is not a cell of the ordinary CW complex. All simplices are oriented by increasing graph-edge index.

Equivalently, \(Q_4\cong C_4\mathbin{\square}C_4\): the four-by-four **periodic** Cartesian grid. It is not the four-by-four planar Cartesian grid \(P_4\mathbin{\square}P_4\), which has only 24 edges; the periodic graph has 32.

## Proof
**1. Exhaustive face census.** Recursively consider each of the 32 graph edges in fixed order, excluding it or including it when its two endpoints are not used by previously included edges. Every matching has a unique inclusion/exclusion word, so this enumerates all faces exactly once. The counts by edge-set cardinality zero through eight are
\[
(1,32,400,2496,8256,14208,11648,3712,272).
\]
Thus the ordinary complex has 41,024 nonempty simplices, its largest simplices have dimension seven, and its reduced Euler characteristic is \(-129=1-130\).

**2. Two exhaustive discrete-Morse matchings.** Process edge-index pivots in increasing order, respectively decreasing order. At each pivot \(e\), pair each currently unmatched face \(\sigma\) lacking \(e\) with \(\sigma\cup\{e\}\), when both faces are currently unmatched. The paired faces differ by exactly one element, so each pair is a legitimate Hasse cover. A temporary augmented pair joining the empty face to a vertex is removed, leaving that vertex critical in the ordinary complex. The increasing-pivot matching leaves one critical zero-cell, 39 critical four-cells, and 168 critical five-cells, with precisely 20,408 matched pairs. The decreasing-pivot matching leaves one critical zero-cell, 12 critical four-cells, and 141 critical five-cells, with 20,435 matched pairs. In each case exactly 210,400 codimension-one cover relations are oriented downward, except that matched relations are reversed upward. Kahn's topological sort consumes all 41,024 faces, proving that both matchings are **acyclic**, not just pairwise disjoint. Forman's discrete Morse theorem supplies a homotopy-equivalent CW complex with only the stated critical cells.

**3. Exact integral Morse differentials.** For a critical four-simplex, project it to its own basis vector. A four-simplex matched downward to a three-simplex projects to zero. If a four-simplex \(\tau\) is matched upward to a five-simplex \(\beta\), solve the signed simplicial boundary relation of \(\beta\) for the coefficient of \(\tau\) and recursively project its other four-faces. Every incidence is \(+1\) or \(-1\), and acyclicity of the reversed Hasse digraph makes this signed gradient recursion terminate. Applying this projection to the oriented boundaries of the critical five-simplices gives the integral Morse matrices, with no field reduction or sampling.

For increasing pivot order the boundary \(\partial_5^{\mathrm{Morse}}\) is a \(39\times168\) integer matrix with 909 nonzero entries and Smith normal form having precisely 38 nonzero diagonal entries, **all equal to one**. For decreasing pivot order the boundary is a \(12\times141\) integer matrix with 512 nonzero entries and Smith normal form having precisely eleven nonzero entries, **all equal to one**. The exact computations agree and independently yield \(\widetilde H_4\cong\mathbb Z\), \(\widetilde H_5\cong\mathbb Z^{130}\), and no torsion. The dimensions zero through three and six through seven have no critical cells, so they have no reduced integral homology.

**4. Homotopy, not merely homology.** The increasing-pivot Morse CW complex has one zero-cell, no cells in dimensions one through three, 39 four-cells, and 168 five-cells. Its four-skeleton is \(\bigvee^{39}S^4\). Hurewicz identifies its fourth homotopy group with its fourth homology, so every five-cell attaching map is determined by its integral degree vector in \(\mathbb Z^{39}\). The 38 unit Smith pivots say these vectors generate a **primitive rank-38 direct summand** of that lattice. Integer changes of basis are realized by self-homotopy equivalences of a wedge of four-spheres. Following those changes, 38 five-cells attach by degree one to 38 distinct four-spheres and cancel those spheres. The remaining 130 five-cells attach trivially to the surviving single four-sphere. This gives precisely \(S^4\vee\bigvee^{130}S^5\). The decreasing-pivot matching independently yields the same conclusion after eleven such cancellations.

## Verification
Two standalone reproducible programs accompany the statement. Run `python3 verify.py` (Python 3 with SymPy) for the complete face enumeration, both explicit toggle matchings, exact reversed-Hasse acyclicity checks, signed integral Morse matrices, and Smith normal forms. Its concluding marker is `ALL_CHECKS_PASS`; its full output is embedded as `verify_output.txt`.

Run `python3 mod2_crosscheck.py` (Python 3 standard library) for an independent enumeration of all matchings and exact bitwise elimination of the **original** simplicial boundary matrices over \(\mathbb F_2\), rather than the Morse matrices. The boundary ranks in cardinalities one through eight are
\[
(1,31,369,2127,6129,8078,3440,272).
\]
They imply mod-two reduced Betti numbers one in degree four and 130 in degree five, zero elsewhere. The mod-two calculation confirms the census and rational-rank pattern; it does **not** certify absence of integral torsion or the homotopy splitting. Those conclusions rely on the separate signed integral Smith computations and the Hurewicz argument above. `mod2_crosscheck_output.txt` is included.

## Relationship to prior work
Matching complexes, their description as independence complexes of line graphs, and discrete-Morse approaches are classical. Engström's 2005 full-text theorem concerns connectivity of independence complexes of claw-free graphs; it gives no exact homotopy computation for the 4-cube. Jonsson's 2007 monograph systematically treats graph complexes and matching complexes and is a fundamental methodological source, but the matching chapter was accessible only via the publisher's contents and preview. Matsushita's 2018 preprint (published 2019) proves wedge decompositions for a two-row strip family and associated generalized line graphs; its explicitly defined graph family does not include \(Q_4\).

The previously published 3-cube matching complex result concerns \(Q_3\) rather than \(Q_4\). Another published exact matching complex is for the 16-vertex, 24-edge planar grid \(P_4\mathbin{\square}P_4\); it is not the periodic grid \(C_4\mathbin{\square}C_4\). Results for the matching complex of the **line graph** of the 3-cube concern the different double-line-graph complex. Published sphere-wedge results for outerplanar graphs do not imply this theorem, since \(Q_4\) has 32 edges on 16 vertices and thus exceeds the outerplanar bound of 29 edges. No inspected theorem, equivalent formulation, or exact table supplied the asserted 1-and-130 integral homotopy classification. This comparison does not exclude unindexed or inaccessible calculations.

## Limitations
This is an exact finite theorem for the full ordinary matching complex of one natural graph. It does not classify matching complexes of all hypercubes or all toroidal grids, prove stability in dimension, or determine equivariant homology representations. The associated certificate is computationally exhaustive for this one finite case; neither its mod-two output nor its agreement across two pivot orders is offered as a general theorem. The historical priority conclusion is limited by searchable sources, notably the unavailable full text of Jonsson's matching chapter. There has been no independent mathematical audit.

## References
1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1, first submitted 2005-12-17; especially Theorem 3.2 (connectivity bounds).
2. J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer, softcover first published 2007-11-15, DOI:10.1007/978-3-540-75859-4, chapter *Matchings* (full chapter not accessed).
3. T. Matsushita, *Matching complexes of small grids*, arXiv:1812.11000v1, first submitted 2018-12-28; *Electronic Journal of Combinatorics* 26(3), P3.1 (2019), Theorem 1.2.
4. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v1, first submitted 2024-11-07.
5. *The cube matching complex is a wedge of four 2-spheres*, publicly indexed calculation (2026), unique record suffix `79d70fe8b67e`.
6. *The matching complex of the 4-by-4 Cartesian square grid is a mixed-dimensional sphere wedge*, publicly indexed calculation (2026), unique record suffix `f1b5ea641880`.
7. *The cuboctahedral matching complex is a wedge of 57 three-spheres*, publicly indexed calculation (2026), unique record suffix `42f20681b118`.
