# Integral homotopy and the \(S_5\)-character of the Petersen edge-matching complex

## Finding
Let \(P=\operatorname{KG}(5,2)\), the Petersen graph, and let \(\mathcal M(P)\) be its **ordinary edge-matching complex**: each vertex is an edge of \(P\), and simplices are sets of pairwise disjoint edges. The complete integral homotopy type is
\[
\mathcal M(P)\simeq\bigvee^{5}S^{2}\vee\bigvee^{5}S^{3}.
\]

The canonical action \(\operatorname{Aut}(P)\cong S_5\) gives, as rational representations,
\[
\widetilde H_2(\mathcal M(P);\mathbb Q)\cong\operatorname{sgn}\otimes\mathbb Q^5,\qquad
\widetilde H_3(\mathcal M(P);\mathbb Q)\cong S^{(3,2)}.
\]
Here \(\mathbb Q^5\) denotes the permutation representation on the original five points and \(S^{(3,2)}\) the irreducible Specht representation corresponding to partition \((3,2)\). Both representations have dimension five but are nonisomorphic; neither admits nonzero full-group invariants.

## Assumptions and scope
Take the ten Petersen vertices to be lexicographically ordered two-element subsets of \(\{0,1,2,3,4\}\). Join two when disjoint. Lexicographically order its fifteen edges and represent a simplex by the corresponding 15-bit mask. A face is valid exactly when no two selected Petersen edges share a graph vertex. The maximal matching has size five; the complex has dimension four. Every statement concerns **this graph-edge matching complex**, not the conventional \(\mathcal M(K_5)\), whose one-dimensional realization happens to be the Petersen graph.

## Proof
**Exact simplicial model.** An occupied-vertex test over all \(2^{15}\) masks and a separate recursive matching enumeration return the same 332 faces including the empty face. The nonempty face vector in dimensions zero through four is \((15,75,145,90,6)\); its facet counts by dimension two, three and four are respectively \((5,60,6)\), so it is nonpure. Mod-two boundary ranks for dimensions one through four are \((14,61,79,6)\), corroborating reduced Betti ranks five in each of degrees two and three and zero elsewhere. This check alone would **not** establish the integral statement.

**Acyclic integral Morse reduction.** Repeatedly visit the fifteen graph edges in order, matching each still-unmatched face not containing the current edge with the face obtained by adjoining that edge whenever both are still unmatched; leave the empty face out of the matching. The supplied checker constructs 158 matched pairs. Directing matched Hasse incidences upward and all others downward, a complete topological-sort check covers all 975 nonempty-face Hasse incidences and visits all 331 nonempty faces. Thus the matching is acyclic. The unmatched cells are one zero-cell, seven two-cells, and seven three-cells, with no one-cells or cells in larger dimensions.

**Integral attaching degrees.** Order every simplex by ascending matching-edge index. Its boundary coefficient on deleting its \(i\)-th vertex is \((-1)^i\). Algebraic elimination of all 158 matched incidences, whose coefficients are \(\pm1\), yields the following exact cellular boundary from the seven critical three-cells to the seven critical two-cells (rows listed in critical-face mask order):

```text
 1  0 -1  0  1  0  1
 0 -1  1  1 -1 -1 -1
 0  0  0  0  0  0  0
 0  0  0  0  0  0  0
 0  0  0  0  0  0  0
-1  1  0 -1  0  1  0
 0  0  0  0  0  0
```

Only three rows are nonzero, and every column sums to zero across those rows, so the integral rank is at most two. The leading two-by-two minor has determinant \(-1\), hence the rank is exactly two and the nonzero Smith invariant factors are \((1,1)\). Since the one-skeleton of the reduced CW model is a point, its two-skeleton is a wedge of seven two-spheres. The degree vector completely determines each three-cell attachment via \(\pi_2\cong H_2\). Integer elementary basis changes diagonalize the attachment matrix, and two primitive three-cell/two-cell pairs cancel by standard CW elementary homotopy cancellation. The remaining five two-cells and five three-cells attach trivially. This proves the **integral homotopy equivalence**, not merely a numerical Betti table.

**The complete symmetry character.** Each permutation of the five original points induces a simplicial automorphism, with the usual orientation sign on ordered simplices. Over the prime field of order \(1000003\), the checker independently constructs bases for each simplicial boundary image, computes the induced traces on them, and obtains the rational homology traces from the exact chain identity
\[
\operatorname{tr}(g\mid H_k)=\operatorname{tr}(g\mid C_k)
-\operatorname{tr}(g\mid\operatorname{im}\partial_k)
-\operatorname{tr}(g\mid\operatorname{im}\partial_{k+1}).
\]
Every resulting rational trace has absolute value below half the modulus, so its modular lift is unambiguous. All 120 permutations are explicitly checked. If \(f_1(g)\) denotes the number of fixed points on five letters, \(f_2(g)\) the number of fixed two-element subsets, and \(\epsilon(g)\) the permutation sign, the characters are exactly
\[
\chi_2(g)=\epsilon(g)f_1(g),\qquad\chi_3(g)=f_2(g)-f_1(g).
\]
The first is the character of \(\operatorname{sgn}\otimes\mathbb Q^5\). The two-subset permutation module splits as \(\mathbf1\oplus S^{(4,1)}\oplus S^{(3,2)}\), whereas the five-point permutation module is \(\mathbf1\oplus S^{(4,1)}\), identifying the second character with \(S^{(3,2)}\). The first contains \(\operatorname{sgn}\oplus S^{(2,1,1,1)}\), so neither homology representation contains the trivial module.

## Verification
Run `python3 verify_petersen_matching.py` using Python 3.9 or later; no nonstandard packages or external data are required. The embedded `verification-output.txt` is a recorded execution. It reports 332 faces, exact facet counts and full independent enumeration agreement, boundary ranks, a full 158-pair acyclic matching, the exact seven-by-seven signed boundary, its rank-two unit minor, and the complete 120-element rational symmetry character. The checker recomputes all graph, simplex, Morse, and representation data rather than loading claimed matrices.

## Relationship to prior work
Mondal, Mukherjee, and Saha investigate \(\mathcal M(K_n)\), the matching complexes of **complete** graphs (the first preprint was public 2023-03-13). Their observation that \(\mathcal M(K_5)\) *is* the Petersen graph (a one-dimensional complex with six circle summands) does **not** compute \(\mathcal M(P)\), the complex whose vertices are Petersen **edges**. Larrión, Pizaña, and Villarroel-Flores likewise identify the Petersen graph as the matching graph of \(K_5\) and study a clique-operator problem, not the matching complex of the Petersen graph. Existing tree and homology-manifold matching-complex classifications do not cover this non-tree, nonmanifold case. The new contribution is both the exact integral homotopy type and the full rational \(S_5\)-representation; the basic definition of matching complexes is established literature.

## Limitations
The homotopy decomposition is nonequivariant; no equivariant wedge splitting is asserted. The representation calculation is over \(\mathbb Q\), not an integral \(\mathbb Z[S_5]\)-module classification. Although this is an exhaustive finite calculation supported by fully reproducible signed certificates, an equivalent unpublished or unindexed result remains a bibliographic risk. No analogous formula for arbitrary symmetric cubic graphs is claimed.

## References
1. A. Mondal, S. Mukherjee, and K. Saha, *Discrete Morse theory and the topology of matching complexes of complete graphs*, arXiv:2303.07054, first posted 2023-03-13; merged with *Topology of matching complexes of complete graphs via discrete Morse theory*, arXiv:2305.02973 (2023-05-04), published 2024.
2. F. Larrión, M. A. Pizaña, and R. Villarroel-Flores, *The Clique Operator on Matching and Chessboard Graphs*, https://xamanek.izt.uam.mx/map/papers/chessmatch7.pdf, especially Sections 1 and 3.
3. M. Jelić Milutinović, H. Jenne, A. McDonough, and J. Vega, *Matching complexes of trees and applications of the matching tree algorithm*, arXiv:1905.10560, 2019.
4. M. Bayer, B. Goeckner, and M. Jelić Milutinović, *Manifold Matching Complexes*, arXiv:1906.03328, 2019.
