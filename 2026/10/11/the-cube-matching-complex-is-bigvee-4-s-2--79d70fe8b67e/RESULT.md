# The cube matching complex is \(\bigvee^{4}S^2\)
## Finding
Let \(Q_3\) be the graph on \(\{0,1\}^3\) in which two binary triples are adjacent exactly when they differ in one coordinate. Its ordinary matching complex \(\mathcal M(Q_3)\), whose vertices are the twelve graph edges and whose simplices are pairwise disjoint edge sets, has homotopy type
\[
\mathcal M(Q_3)\simeq \bigvee^{4}S^2.
\]

## Assumptions and scope
The statement concerns the ordinary graph matching complex, equivalently the independence complex of the line graph \(L(Q_3)\). It is an exact assertion for the three-dimensional cube only. It does not assert a formula for higher-dimensional hypercubes, for higher matching complexes, or for Morse complexes.

The cube vertices are numbered \(0,\ldots,7\) by their three-bit binary expansions. Its edges, in the order used by the verifier, are
\[
(0,1),(0,2),(0,4),(1,3),(1,5),(2,3),(2,6),(3,7),(4,5),(4,6),(5,7),(6,7).
\]

## Proof
A simplex of \(\mathcal M(Q_3)\) is a matching in the displayed twelve-edge list. Exhaustive enumeration gives \(107\) nonempty simplices with face vector
\[
(f_0,f_1,f_2,f_3)=(12,42,44,9).
\]

Process the matching-complex vertices in edge-index order
\[
2,3,9,10,8,1,6,11,4,0,5,7.
\]
At each stage for an edge index \(e\), pair every still-unmatched simplex \(\sigma\) not containing \(e\) with \(\sigma\cup\{e\}\) whenever the latter is a simplex and is still unmatched. This produces \(51\) matched Hasse pairs. The unmatched simplices, written as edge-index sets, are
\[
\{2\},\quad \{0,5,8\},\quad \{0,7,8\},\quad \{6,7,8\},\quad \{1,4,11\}.
\]
Thus there is one critical \(0\)-simplex and four critical \(2\)-simplices.

The verifier constructs all \(252\) nontrivial Hasse cover relations. It reverses each matched cover relative to the other covers and topologically sorts the resulting directed graph. All \(107\) simplices are visited, so the matching is acyclic. Forman's discrete Morse theorem therefore gives a homotopy-equivalent CW complex with one \(0\)-cell, four \(2\)-cells, and no cells in any other positive dimension. With no \(1\)-cells, every \(2\)-cell is attached to the unique \(0\)-cell, giving exactly \(\bigvee^{4}S^2\).

## Verification
The standalone program `verify.py` reconstructs the cube from the twelve listed edges, exhausts every subset of the edge set, checks the matching condition, rebuilds the full face poset, applies the stated sequential element matching, and verifies acyclicity by topological sorting.

As an independent chain-level check, it computes augmented boundary ranks over \(\mathbb F_2\) equal to
\[
(1,11,31,9)
\]
in simplex dimensions \(0,1,2,3\). Hence the reduced mod-\(2\) Betti vector is
\[
(0,0,4,0),
\]
and the Euler characteristic is \(5\), both agreeing with the four-sphere wedge conclusion. Running `python3 verify.py` ends with `VERIFY_OK`.

## Relationship to prior work
The matching-complex literature treats many graph families, including paths, cycles, Dutch-windmill families, and planar rectangular grids. The 2023 paper on star clusters in matching and Morse complexes develops general matching-complex tools but does not list the cube graph among its exact examples. Matsushita's paper on small grids studies planar \(2\)-row grids and obtains recursive homotopy information for their matching complexes; the cube \(Q_3=P_2\mathbin{\square}P_2\mathbin{\square}P_2\) is a three-direction Cartesian product and is not in that family.

Searches under the equivalent formulation \(\operatorname{Ind}(L(Q_3))\), under cube and \(2\times2\times2\) grid aliases, and for the exact wedge statement did not locate a prior theorem implying this homotopy type. This negative search is not by itself a novelty proof; the originality assessment also uses full-text comparison with the most relevant matching-complex sources named below.

## Limitations
The proof is a finite exact computation plus standard discrete Morse theory; it gives no recurrence or structural classification for \(\mathcal M(Q_n)\) when \(n>3\). The originality conclusion is relative to the literature and databases inspected, so an unindexed computation under different terminology remains a residual risk.

## References
1. B. Braun and B. Hough, *Matching and independence complexes related to small grids*, arXiv:1606.01204.
2. T. Matsushita, *Matching complexes of small grids*, arXiv:1812.11000.
3. N. Scoville and J. Zaremsky, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780; New York J. Math. 29 (2023), 1393–1412.
