# Complete homotopy classification of order-four Latin-square partial-transversal complexes

## Finding
For every Latin square \(L\) of order four, let \(\mathcal T(L)\) be the abstract simplicial complex whose vertices are the sixteen cells and whose faces are sets of cells with pairwise distinct rows, columns, and symbols. Then exactly the following two possibilities occur, distinguished by the isotopy class of \(L\):

\[
\mathcal T(L)\cong_{\mathrm{simp}}\mathcal T(\mathbb Z/4\mathbb Z)
\quad\Longrightarrow\quad
|\mathcal T(L)|\cong S^1\times S^1,
\]
\[
\mathcal T(L)\cong_{\mathrm{simp}}\mathcal T((\mathbb Z/2\mathbb Z)^2)
\quad\Longrightarrow\quad
|\mathcal T(L)|\simeq\bigvee^{9}S^1.
\]

Here the group notation designates the addition table. More precisely, \(\mathcal T(\mathbb Z/4\mathbb Z)\) is itself a combinatorial triangulation of the torus, while \(\mathcal T((\mathbb Z/2\mathbb Z)^2)\) simplicially collapses to a connected graph with sixteen vertices and twenty-four edges. Every order-four Latin square is isotopic to exactly one of these two group tables. The two homotopy types are not equivalent: the cyclic case has nonzero degree-two integral homology, and the elementary-abelian case has none.

## Assumptions and scope
Write the row, column and symbol sets as \(\{0,1,2,3\}\), and label cell \((r,c)\) by the integer \(4r+c\). A subset \(\sigma\) of cells is a face of \(\mathcal T(L)\) if and only if its rows, columns and \(L\)-symbols are each injective on \(\sigma\). The empty face is included; topological realizations use the nonempty faces. An *isotopy* independently permutes the four rows, four columns and four symbols. It induces a simplicial isomorphism of the corresponding partial-transversal complexes.

For the cyclic representative, \(L_C(r,c)=r+c\pmod 4\). For the elementary-abelian representative, \(L_V(r,c)=r\mathbin{\mathrm{xor}}c\), with the four elements encoded as two-bit vectors. No assertion is made about larger Latin squares, arbitrary partial Latin squares, Latin trades, or different simplicial complexes associated with the same square.

## Proof
**Exhaustion of isotopy classes.** By relabelling symbols so that the first row is \((0,1,2,3)\), and then relabelling rows so that the first column is \((0,1,2,3)^{\mathsf T}\), every order-four Latin square is isotopic to a reduced square. Each of the other three rows must begin with its row index, and each column must contain four different symbols. Exhausting these finitely many permutations yields precisely four reduced squares:

\[
\begin{pmatrix}0&1&2&3\\1&0&3&2\\2&3&0&1\\3&2&1&0\end{pmatrix},
\quad
\begin{pmatrix}0&1&2&3\\1&0&3&2\\2&3&1&0\\3&2&0&1\end{pmatrix},
\]
\[
\begin{pmatrix}0&1&2&3\\1&2&3&0\\2&3&0&1\\3&0&1&2\end{pmatrix},
\quad
\begin{pmatrix}0&1&2&3\\1&3&0&2\\2&0&3&1\\3&2&1&0\end{pmatrix}.
\]

Independent row, column and symbol permutations identify the first with the elementary-abelian group table and the other three with the cyclic group table. The exact mappings are in `certificate.json` and checked by `verify.py`. The two classes are distinct because their numbers of full transversals are respectively eight and zero.

**Cyclic case.** Exhaustive face enumeration for \(L_C\), including the empty face, gives cardinality counts \((1,16,48,32,0)\). Every edge lies in exactly two triangles. The link of each of the sixteen vertices is a connected six-cycle (six vertices, six edges, all link degrees equal to two). Thus the complex is a connected closed combinatorial surface. The signed orientation table in `certificate.json` assigns \(\pm1\) to each of the thirty-two oriented triangles; for every shared edge, the adjacent oriented incidence numbers are opposite, giving an integral coherent orientation. Its Euler characteristic is \(16-48+32=0\). By classification of closed connected orientable surfaces, its realization is homeomorphic to the torus \(S^1\times S^1\).

**Elementary-abelian case.** Exhaustive face enumeration for \(L_V\) gives cardinality counts \((1,16,48,32,8)\). The thirty-two pairs \((\sigma,\tau)\) in `certificate.json` are ordered elementary simplicial collapses: at the time of each deletion, \(\tau\) is the unique codimension-one coface of \(\sigma\). This criterion makes \(\sigma\) a free face. Following the entire certificate deletes sixty-four faces and leaves precisely one empty face, sixteen vertices and twenty-four edges, with no higher-dimensional faces. The remaining graph is connected. Any connected finite graph with \(v\) vertices and \(e\) edges is homotopy equivalent to a bouquet of \(e-v+1\) circles (contract a spanning tree). Here \(24-16+1=9\), proving the claimed wedge decomposition.

The same finite checks are independently reconstructed from the addition laws using both combination-based and backtracking face enumeration. This concludes the complete order-four classification.

## Verification
Run `python3 verify.py` in the directory containing `certificate.json`. For regeneration of the data, run `python3 make_cert.py` and then rerun `python3 verify.py`. Python 3's standard library suffices. The verifier enumerates every face for both group tables by two algorithms; checks all edge--triangle incidences, vertex-link connectivity, coherent triangle orientations and Euler characteristic in the cyclic case; validates every free-face deletion and the residual graph in the elementary-abelian case; and independently enumerates all reduced order-four squares and their explicit isotopies. It also checks the counts of full transversals. The proof requires neither a numerical approximation nor an inference from a homology-only computation.

## Relationship to prior work
Wanless (2002) studies group-table transversals and general \(k\)-plexes; Evans, Mammoliti and Wanless (first posted 2019) show in particular that all order-four Latin squares are equivalent to group tables and distinguish which maximal partial-transversal lengths occur. These results motivate the two representatives but do not determine the topology of the complex of *all* partial transversals. Hämäläinen (2009) explicitly computes simplicial homology for complexes associated with the same cyclic and elementary-abelian tables, but those complexes have **Latin trades as vertices**, not individual cells, and hence do not give the homotopy types here. Standard chessboard complexes omit the additional distinct-symbol restriction and are likewise different spaces.

The topological conclusion is a comparison of actual complex definitions, not a deduction that a matching paper lacking the word “torus” cannot contain it. Other formulations as rainbow-matching complexes of a properly edge-coloured complete bipartite graph, or as independence complexes of Latin-square conflict graphs, are included in the originality search.

## Limitations
The theorem addresses order four and exactly the partial-transversal complex defined above. The finite certificate and standard classification theorems establish the stated integral homotopy types; they do not classify higher orders, arbitrary 3-partite 3-uniform hypergraph matching complexes, or symmetry actions on homology. As with any literature search, an equivalent unindexed treatment under a different terminology may exist; no claim of exhaustive global novelty certification is made.

## References
1. I. M. Wanless, “A Generalisation of Transversals for Latin Squares,” *Electronic Journal of Combinatorics* 9 (2002), R12, first published 2002-03-18. https://doi.org/10.37236/1629
2. A. B. Evans, A. Mammoliti, I. M. Wanless, “Latin squares with maximal partial transversals of many lengths,” arXiv:1911.05912, first posted 2019-11-14, https://arxiv.org/abs/1911.05912
3. C. Hämäläinen, “Latin trades and simplicial complexes,” arXiv:0907.1481, first posted 2009-07-09, https://arxiv.org/abs/0907.1481
4. A. Hatcher, *Algebraic Topology* (2002), classification of compact surfaces and elementary homotopy equivalences.
