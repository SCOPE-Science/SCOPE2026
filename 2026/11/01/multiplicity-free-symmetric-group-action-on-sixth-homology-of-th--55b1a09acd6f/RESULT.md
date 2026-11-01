# Multiplicity-free symmetric-group action on sixth homology of the seven-point intersecting-triple complex

## Finding
Let \(X\) be the simplicial complex whose vertices are the \(35\) three-element subsets of \([7]\), with a collection spanning a simplex exactly when every two of its triples intersect. Let \(\mathfrak S_7\) permute the ground set. Its action on sixth reduced rational homology has the exact multiplicity-free decomposition
\[
\widetilde H_6(X;\mathbb Q)\cong S^{(7)}\oplus S^{(4,3)}\oplus S^{(2,2,2,1)}.
\]
Here \(S^{\lambda}\) denotes the rational Specht module of partition \(\lambda\vdash 7\); the three summands have respective dimensions \(1,14,14\). In particular \(\dim \widetilde H_6(X;\mathbb Q)=29\), and the invariant subspace under all of \(\mathfrak S_7\) is one-dimensional. The assertion concerns the rational representation, not a proposed integral decomposition or a homotopy type.

## Assumptions and scope
The graph \(\mathrm{KG}(3,1)\) is taken in the convention of Feng (2026): its vertices are the triples of a seven-element ground set and its edges join disjoint triples. Thus \(X=\operatorname{Ind}(\mathrm{KG}(3,1))\). The proof uses as published inputs Feng's rational Betti-number calculation: the only nonzero reduced rational homology is in dimensions \(6\) and \(9\), of ranks \(29\) and \(7\), respectively; and Feng–Wang's earlier theorem that the six-ground-point cross-polytopal cycles in dimension \(9\) are linearly independent. Since there are seven such cycles and dimension-nine homology has dimension seven, they form a rational basis. These input results are not newly proved here.

## Proof
**The ninth-homology character.** For a six-element subset \(A\subseteq[7]\), its twenty triples divide into ten complementary pairs. The induced subcomplex on these twenty triples is the join of ten zero-spheres, a nine-dimensional cross-polytope boundary in \(X\); its maximal simplices select one triple from each complementary pair. The associated fundamental class transforms under the stabilizer \(\mathfrak S_A\cong\mathfrak S_6\) by the sign character. Indeed, permuting the ten antipodal pairs gives an orientation sign, and reversing individual pairs changes the orientation sign; their product equals the sign of the original six-point permutation. An independent finite checker verifies this identity for every one of the \(720\) permutations of six points. Consequently the published cross-polytope basis identifies
\[
\widetilde H_9(X;\mathbb Q)\cong \operatorname{Ind}_{\mathfrak S_6\times\mathfrak S_1}^{\mathfrak S_7}(\operatorname{sgn}_6\boxtimes\mathbf 1).
\]
For \(g\in\mathfrak S_7\) the character \(\chi_9(g)\) is therefore the sum of signs of \(g\) on all six-element subsets preserved setwise by \(g\). This formula is an application of the previously known degree-nine cycles, not the claimed new contribution.

**Reduced Lefschetz character.** Fix \(g\in\mathfrak S_7\), and partition the \(35\) triple-vertices into orbits under \(\langle g\rangle\). Discard an orbit if two triples inside it are disjoint. On the remaining orbits construct a graph \(D_g\) joining two orbits whenever some triple in the first is disjoint from some triple in the second. An invariant simplex of \(X\) is exactly a union of orbit-vertices forming an independent set in \(D_g\). An invariant simplex containing \(r\) triple-orbits has dimension equal to the sum of their orbit lengths minus one, and \(g\) acts on its oriented chain by the product of the signs of the cyclic shifts in those orbits. Its signed contribution in the reduced Lefschetz trace is exactly \((-1)^{r-1}\). Hence, writing \(I(D_g;t)\) for the ordinary independence polynomial including the empty independent set,
\[
\widetilde L(g)=-I(D_g;-1).
\]
This formula holds for every finite permutation and includes the empty face through the reduced-chain convention. As dimensions six and nine are the only nonzero reduced rational homology degrees, the Lefschetz fixed-point trace formula gives
\[
\chi_6(g)-\chi_9(g)=-I(D_g;-1),\qquad
\chi_6(g)=-I(D_g;-1)+\chi_9(g).
\]

**Exact finite evaluation.** Conjugacy classes of \(\mathfrak S_7\) correspond to its \(15\) partitions. For each representative, the attached standard-library-only checker explicitly constructs the triple-orbits and the conflict graph \(D_g\). It evaluates \(I(D_g;-1)\) by the exact deletion relation \(I(D_g;-1)=I(D_g-v;-1)-I(D_g-N[v];-1)\), with disjoint-component factorization and isolated-vertex cancellation. At the identity it obtains \(I(D_e;-1)=-22\), in agreement with the published \(29-7=22\) reduced Euler characteristic. The checker constructs all irreducible \(\mathfrak S_7\) characters using the Murnaghan–Nakayama rim-hook recursion, validates character orthogonality exactly with centralizer orders, and computes the character inner products. The only nonzero multiplicities of \(\chi_6\) are exactly one each for \((7)\), \((4,3)\), and \((2,2,2,1)\); all other multiplicities are zero. Hook-length dimensions are \(1,14,14\), summing to \(29\). This proves the decomposition.

## Verification
Run `python3 verify.py` with Python 3 and no third-party packages. Its assertions cover the \(35\) vertices, all \(15\) conjugacy classes, all \(720\) orientation-sign tests, independence-polynomial evaluations, exact irreducible characters and orthogonality, all multiplicities, and the dimension \(29\). It prints `VERIFY_OK` only when all checks succeed. The calculation is exhaustive over the finite \(\mathfrak S_7\) conjugacy classes, not an inference from a sample. It checks the new character calculation conditional on the published rational homology and cycle-independence inputs rather than recreating their full proofs.

## Relationship to prior work
Feng (arXiv:2610.17394, first public 2026-10-12) establishes the nonequivariant rational homology ranks, not the degree-six rational \(\mathfrak S_7\) decomposition. Feng and Wang (arXiv:2404.10566, first public 2024-04-16) establish independence of the degree-nine cross-polytopal cycles; those known cycles are used to subtract the ninth-homology character from the signed Lefschetz character. The previous result for the corresponding eight-point intersecting-triple complex has a different ground-set size and does not mathematically determine this degree-six \(\mathfrak S_7\) character. A character decomposition computed elsewhere under a different complex name could be equivalent, and has not been ruled out definitively.

## Limitations
The conclusion is rational and for exactly seven ground points. It does not compute an integral equivariant lattice, an integral homotopy type, general dependence on ground-set size, or explicit degree-six cycle generators. In particular, it does not resolve the published request for a concrete degree-six homology basis. Its originality assessment is limited by possible unindexed or differently formulated equivalent calculations, and it has not received independent mathematical validation.

## References
1. Z. Feng, *The rational homology of independence complexes of Kneser graphs on triples*, arXiv:2610.17394 (first public 2026-10-12). https://arxiv.org/abs/2610.17394
2. Z. Feng and G. Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566 (first public 2024-04-16). https://arxiv.org/abs/2404.10566
