# Clique-free triangular-graph homotopy and the six-point symmetry character

## Finding

Let \(T_6=L(K_6)=J(6,2)\) be the triangular graph on the 15 two-element subsets of six labels, and let \(X=\operatorname{CF}_3(T_6)\) be the complex of vertex sets containing no triangle of \(T_6\). Then
\[
X\simeq\bigvee^{26}S^4,
\qquad
\widetilde H_4(X;\mathbb Q)\cong S^{(6)}\oplus S^{(4,2)}\oplus S^{(3,2,1)}
\]
as a rational representation of \(S_6\). In particular, \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z^{26}\), all other reduced integral homology vanishes, and the rational invariant subspace under \(S_6\) is one-dimensional. The Specht labels denote partitions of six.

## Assumptions and scope

Graph edges are unordered and graphs have no loops. Label the edges of \(K_6\) lexicographically by integers 0 through 14. A face of \(X\) is an edge set \(F\subseteq E(K_6)\) with no three pairwise incident edges. Equivalently, the spanning graph \(([6],F)\) has maximum degree at most two and no triangular cycle. The only forbidden minimal triples are the \(60\) three-edge stars and \(20\) triangles, totaling \(80\). This theorem concerns exactly six underlying labels and the canonical action of \(S_6\); no all-order assertion is made.

## Proof

**1. Complete face poset.** Enumerate the \(2^{15}\) candidate masks and exclude those containing a forbidden triple. The number of faces of cardinalities zero through six is respectively \(1,15,105,375,675,477,60\); no larger faces occur. The complex has \(1708\) augmented faces and its facets have sizes five and six (respectively \(117\) and \(60\) facets).

**2. Explicit acyclic matching.** In the order
`13,1,7,5,12,9,2,14,4,6,11,0,8,10,3`, for each pivot label \(j\), pair every still-unmatched face \(F\) omitting \(j\) with \(F\cup\{j\}\) when both remain unmatched. This specifies every pair unambiguously. The `verify.py` program reconstructs all \(840\) pairs and checks acyclicity by topologically sorting the *entire* directed face-incidence graph (reverse matched cover relations, leave other cover relations forward). Exactly \(28\) augmented faces remain unmatched: one three-dimensional face and twenty-seven four-dimensional faces. The empty face was matched to a vertex; omitting this augmented pair yields an ordinary acyclic matching with one critical vertex in addition to these twenty-eight higher-dimensional cells.

**3. Integral attaching degree.** For each three-dimensional face paired upward to a four-dimensional face, eliminate that unit incidence recursively in its signed simplicial boundary. On the unique critical three-cell the coefficient is \(1\); on any other three-dimensional face not paired upward it is \(0\). This gives the integral Morse differential from the \(27\) critical four-cells to the unique critical three-cell. Sorted by numerical face mask, its coefficients are
`[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,-1,0,0,1,0,0,0,0,0]`.
Every elimination uses a signed incidence \(\pm1\), and the displayed vector is primitive. The corresponding CW model consists of one vertex, one three-cell, and \(27\) four-cells. Attaching maps of the four-cells to the three-sphere have precisely these degrees. Elementary integer basis changes reduce the primitive degree vector to \((1,0,\ldots,0)\), so a three/four-cell pair cancels up to homotopy and the remaining space is \(\bigvee^{26}S^4\). This is an integral homotopy conclusion, not a finite-field inference.

**4. Equivariant character.** Each \(g\in S_6\) permutes the fifteen edge labels and hence the oriented simplices. Because homology is concentrated in even reduced degree four, the reduced Lefschetz formula reads
\[
\operatorname{tr}(g\mid\widetilde H_4(X;\mathbb Q))
=-\sum_{F\in X}(-1)^{|F|}\operatorname{sgn}(g\mid F),
\]
where the empty face has sign one, and only setwise fixed faces contribute. Direct exact enumeration of all \(720\) permutations yields the character values for cycle types
`(1^6):26; (2,1^4):4; (2^2,1^2):2; (2^3):4; (3,1^3):-1; (3,2,1):1; (3^2):-1; (4,1^2):0; (4,2):2; (5,1):1; (6):1`.
The Murnaghan–Nakayama rule calculates exactly the same values for \(\chi^{(6)}+\chi^{(4,2)}+\chi^{(3,2,1)}\). Character orthogonality yields the asserted rational decomposition; the first constituent is trivial and occurs once.

## Verification

Run `python3 verify.py` with standard-library Python 3. This reproduces the forbidden triples, all faces, all \(840\) pairings, acyclicity with and without the augmented empty-face pairing, the signed primitive integral Morse differential, independent mod-two raw boundary ranks \((14,91,284,391,60)\) in degrees one through five, the full \(720\)-element Lefschetz character, and its Specht decomposition. The finite computation is exhaustive for the stated six-point complex, not an extrapolation to other orders.

## Relationship to prior work

Ghosh and Selvaraja (2026) define and study clique-free complexes, especially shellability conditions for chordal and diamond-free graph classes. The triangular graph \(L(K_6)\) contains an induced four-cycle and is not chordal, so those published sufficient conditions do not imply its stated homotopy type or representation. Singh (2020) studies higher matching complexes, where only vertex-degree constraints are imposed; in contrast, the present complex additionally excludes triangles of the underlying \(K_6\). An accessible 2017 bounded-degree-complex study likewise does not impose this extra forbidden-cycle condition. A previously indexed four-cut complex of \(J(5,2)\) concerns a different cut-complex functor and five rather than six underlying points. Searches for exact complex aliases, stronger classification statements, and fixed homology tables identified no covering theorem. Not all relevant full texts were accessible, so this is a documented best-knowledge novelty comparison, not proof of global uniqueness.

## Limitations

This proves one natural finite homotopy and rational representation classification, not a general formula for \(L(K_n)\). The rational module decomposition does not assert an equivariant wedge splitting over the integers. Independent scientific audit has not been performed. The full text of the most recent motivating preprint was inaccessible through the attempted lawful channels; an unindexed or incidental prior calculation remains a residual originality risk.

## References

1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623, first posted 2026-02-10.
2. A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632 (2020); later *Discrete Mathematics* 345 (2022), 112761.
3. Standard discrete Morse theory: R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145.
4. Standard character theory: the Murnaghan–Nakayama rule for symmetric-group Specht characters.
