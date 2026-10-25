# Integral homotopy of the Petersen Hamiltonian-path containment complex

## Finding
Let \(P\) denote the Petersen graph, realized as the Kneser graph \(\mathrm{KG}(5,2)\). Let \(K(P)\) be the abstract simplicial complex whose vertices are the fifteen edges of \(P\), and whose faces are precisely the edge sets that lie inside a spanning simple path of \(P\). Then
\[
K(P)\simeq\bigvee^{4}S^{5}\vee\bigvee^{24}S^{6}.
\]
In particular, \(\widetilde H_5(K(P);\mathbb Z)\cong\mathbb Z^4\), \(\widetilde H_6(K(P);\mathbb Z)\cong\mathbb Z^{24}\), and all other reduced integral homology groups vanish. The complex is pure of dimension eight; its top-dimensional simplices correspond to the 120 undirected spanning paths.

There is also a sharp, related path-extension boundary. Of the 10,372 linear-forest edge sets (including the empty set), precisely 160 fail to extend to a spanning path. Their inclusion-minimal members consist of ten six-edge forests and thirty eight-edge forests, each class constituting one orbit under \(\operatorname{Aut}(P)\cong S_5\). In particular every linear forest with at most five edges extends to a spanning path.

## Assumptions and scope
All graphs are finite, simple and undirected. The ten vertices of \(P\) are the two-element subsets of \(\{0,1,2,3,4\}\); two are adjacent exactly when disjoint. Number these vertices lexicographically, then lexicographically number the fifteen unordered graph edges from \(0\) to \(14\). A spanning simple path visits each of the ten graph vertices once and has nine edges. Its edge subsets are exactly the simplices of \(K(P)\). Reversal does not create a new facet. An edge subset is a linear forest if it has maximum vertex-degree at most two and has no cycle (isolated graph vertices are allowed).

The finding is a finite integral homotopy classification for this exact graph and containment construction; it does not assert a general theorem for all hypohamiltonian graphs or all path-containment complexes.

## Proof
**1. Finite construction.** The accompanying `verify.py` reconstructs \(\mathrm{KG}(5,2)\) directly from the disjointness rule. Depth-first enumeration of all ordered self-avoiding ten-vertex walks, followed by deduplication of the resulting nine-edge masks, yields exactly 120 facets. Iteration over every submask yields exactly 10,212 faces including the empty face. The numbers of nonempty simplices by size one through nine are
\[
(15,105,445,1245,2346,2905,2190,840,120).
\]
The finite enumeration is exhaustive because every spanning path has a starting vertex and a uniquely determined sequence of unused adjacent vertices; conversely every enumerated sequence satisfies the spanning-path condition.

**2. Explicit acyclic matching.** Use the fifteen edge-vertices in this fixed order:
`[12,1,7,9,10,14,11,5,3,4,8,0,13,2,6]`.
At each stage, pair every currently unmatched face missing the selected edge-vertex with its one-vertex extension, when both faces are present and unmatched. Within a stage each pair is determined without conflict because each face occurs in at most one toggle pair. The algorithm has 5,092 pairs on the augmented face poset. One of them pairs the empty face with a singleton vertex. On the ordinary nonempty face poset that singleton serves as the unique critical vertex; besides it, exactly four critical five-simplices and 24 critical six-simplices remain.

To check the nonexistence of closed gradient paths, orient every unmatched codimension-one cover relation downward and every matched relation upward. The verifier constructs all 58,830 codimension-one incidences and performs a full topological sort of the resulting directed graph on all 10,212 augmented faces. It deletes every face, so the matching is acyclic. This finite directed-acyclicity check is complete, not a sampled gradient-path search. By discrete Morse theory, \(K(P)\) has the homotopy type of a CW complex with one zero-cell, four five-cells and 24 six-cells.

**3. Integral attaching degrees.** For a simplex encoded by an edge mask, orient by increasing edge indices. If \(A=B\cup\{e\}\) with \(|A|=|B|+1\), set the signed incidence \([A:B]\) to \((-1)^q\), where \(q\) counts elements of \(B\) preceding \(e\). For a matched pair \(B\leftrightarrow A\) with \([A:B]=\varepsilon\), eliminating \(B\) in a boundary replaces it by the signed sum \(-\varepsilon\sum_{B'\subset A,\,B'\ne B}[A:B']B'\), recursively following gradient paths. This is exact integer chain reduction, with no modular approximation.

The supplied program constructs the resulting entire integer Morse differential from the 24 critical six-cells to the four critical five-cells. **Every entry of the resulting \(4\times24\) matrix is zero.** There are no other nontrivial differentials among critical cells.

**4. Homotopy, not only homology.** The reduced Morse CW complex has a single zero-cell and no cells of dimensions one through four. Thus its five-skeleton is \(\bigvee^4S^5\), a four-connected CW space. The Hurewicz homomorphism \(\pi_5(\bigvee^4S^5)\to H_5(\bigvee^4S^5;\mathbb Z)\) is an isomorphism. The degree vector of each six-cell attaching map is exactly its column in the integer Morse differential. Since all these columns are zero, every attaching map is nullhomotopic. Attaching all 24 six-cells therefore adds 24 independent six-spheres, proving the asserted homotopy equivalence.

**5. Sharp forest extension boundary.** Independently, `verify.py` exhausts all \(2^{15}\) graph-edge masks, checking degrees and acyclicity by disjoint-set union. This gives 10,372 linear forests including the empty set. Set subtraction from the 10,212 path-contained faces gives 160 nonextendible forests. Checking removal of each selected edge identifies the inclusion-minimal nonextendible members, exactly ten with six edges and thirty with eight. Applying all 120 permutations of the five underlying Kneser coordinates maps each size class transitively onto itself. The fixed graph definition makes this finite enumeration reproducible and exhaustive.

## Verification
The self-contained Python 3.10+ program `verify.py` uses only the standard library. Run `python3 verify.py` in a directory containing it. The supplied `verification_output.txt` is the exact output of the packaged program. Checks include the full face vector, completeness of the spanning-path enumeration, a topological sort of every matching-incidence arc, all integer signed Morse coefficients, independent simplicial boundary ranks over \(\mathbb F_2\), and all linear-forest masks and symmetry orbits. The final output line is `VERIFY_OK`.

The mod-two boundary ranks are corroboration rather than a substitute for the integral attaching-map computation. The finite algorithm proves only the explicitly enumerated ten-vertex case; its correctness relies on the proved coverage of the finite search and the standard discrete-Morse and Hurewicz theorems.

## Relationship to prior work
Holton and Sheehan (1993) give the classical graph-theoretic context for the Petersen graph and its hypohamiltonicity. Li and Wu (2015), Section 2.2 and Example 20(c), study extension of prescribed linear forests to Hamiltonian paths and analyze path endpoint behavior for the Petersen graph. Their notion of forest size includes isolated vertices, so their numerical size parameter should not be directly identified with the number of chosen edges in this result. Their graph-theoretic statements do not determine the homotopy of the simplicial complex consisting of **all subsets of all spanning paths**.

Grinberg, Katthän and Lewis (arXiv:2102.07894) study *directed* path-free and path-missing complexes defined using fixed source and sink vertices. Those face rules are different from undirected spanning-path containment with arbitrary endpoints, and their sphere/contractibility results do not imply this mixed sphere wedge. Forman's (1998) discrete Morse theory is the method used, not a previously published computation of this particular complex. Existing Petersen matching, cut and discrete-Morse complexes have distinct vertex sets or face predicates, and their homotopy classifications do not supply the present answer.

## Limitations
No generalization beyond \(P=\mathrm{KG}(5,2)\) is proved. The source comparisons do not establish absolute uniqueness: an equivalent unindexed or inaccessible result might exist. The full 1993 monograph was not available for material inspection, though bibliographic/contents information was checked. Reproducibility is based on an executable finite exhaustive certificate plus the mathematical argument showing why its output entails the homotopy equivalence; this is not a separately conducted independent audit.

## References
- D. A. Holton and J. Sheehan, *The Petersen Graph*, Cambridge University Press, 1993. DOI: `10.1017/CBO9780511662058` (publisher's first listed print publication: 1993-04-22).
- B. Li and B. Wu, *Spanning connectedness and Hamiltonian thickness of graphs and interval graphs*, Discrete Mathematics & Theoretical Computer Science **16** (2015). DOI: `10.46298/dmtcs.2082`; Section 2.2 and Example 20(c).
- R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145. DOI: `10.1006/aima.1997.1650`.
- D. Grinberg, L. Katthän and J. Lewis, *The path-missing and path-free complexes of a directed graph*, arXiv:`2102.07894` (first public 2021-02-15).
