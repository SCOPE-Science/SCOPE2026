# Petersen four-cut complex: a 26-sphere wedge and its full symmetry module

## Finding

Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph and let \(X=\Delta_4(P)\) be the ordinary four-cut complex. Then
\[
X\simeq\bigvee^{26}S^5.
\]
The integral homology is torsion-free, with \(\widetilde H_5(X;\mathbb Z)\cong\mathbb Z^{26}\) and no other reduced homology. The action of the full graph automorphism group \(\operatorname{Aut}(P)\cong S_5\) has rational decomposition
\[
\widetilde H_5(X;\mathbb Q)\cong S^{(5)}\oplus 2S^{(4,1)}\oplus S^{(3,2)}\oplus 2S^{(3,1,1)}.
\]
Here \(S^{\lambda}\) is the rational Specht module associated with the partition \(\lambda\) of five. In particular, \(\dim_{\mathbb Q}\widetilde H_5(X/S_5;\mathbb Q)=1\), and all other reduced rational homology of the quotient vanishes.

## Assumptions and scope

The graph vertices are the ten two-element subsets of \(\{1,2,3,4,5\}\) in lexicographic order, indexed from zero. Two vertices are adjacent precisely when the associated pairs are disjoint. A four-element set \(A\subseteq V(P)\) is *disconnected* when the induced graph \(P[A]\) is not connected. Define \(X\) to have a facet \(V(P)\setminus A\) for every such disconnected set, together with all subfaces. This is the ordinary cut complex, and must not be conflated with the total cut complex defined using independent sets. All homotopy and integral homology claims concern this finite abstract simplicial complex. All representation and quotient-homology claims use characteristic zero.

## Proof

**Exact complex and discrete Morse reduction.** There are precisely 140 disconnected four-subsets among the 210 four-subsets of ten vertices. The resulting 140 facets each have six vertices. The face vector in dimensions zero through five is
\[
(10,45,120,210,240,140),
\]
and there are 765 nonempty simplices. Enumerate nonempty faces as ten-bit masks. Process vertices in the zero-based order
\[
(8,7,5,9,2,3,6,1,4,0).
\]
At each stage, for each currently unmatched simplex not containing that vertex, pair it with its one-vertex extension when both remain unmatched. This specifies 369 disjoint face-coface pairs. Exactly one zero-simplex and 26 five-simplices remain unmatched. For completeness, direct the 3,330 covering edges of the nonempty face poset *upward* except for matched pairs, which point downward. An exhaustive topological sort of this directed Hasse graph visits every one of its 765 vertices, proving that the matching is acyclic. Thus Forman's discrete Morse theorem provides a CW model with a single zero-cell and 26 five-cells and no other cells. Each five-cell attaches to the zero-cell; the model is precisely a wedge of 26 five-spheres. This proves the integral homotopy and homology assertions without assuming a homological rank computation gives a homotopy equivalence.

**Full automorphism group.** The five collections of two-subsets containing a prescribed element of \(\{1,2,3,4,5\}\) are exactly the maximum independent four-sets of the Petersen graph. Each two-subset is recovered as the unique common vertex of its two corresponding collections. Every graph automorphism therefore permutes these five maximum independent sets faithfully. The evident \(S_5\) action realizes all permutations, hence \(\operatorname{Aut}(P)\cong S_5\).

**Character calculation.** For an element \(g\in S_5\), let \(c_d(g)\) be the signed number of \(g\)-fixed oriented \(d\)-simplices (the sign is the parity of the induced order permutation). Since only ordinary \(H_0\) and \(H_5\) are nonzero,
\[
\operatorname{tr}\left(g\mid\widetilde H_5(X;\mathbb Q)\right)
=1-\sum_{d=0}^5(-1)^d c_d(g).
\]
The seven cycle types of \(S_5\), with the corresponding trace and class cardinality, are shown below.

| Cycle type | Trace on \(\widetilde H_5\) | Class size |
|---|---:|---:|
| \((1,1,1,1,1)\) | 26 | 1 |
| \((2,1,1,1)\) | 6 | 10 |
| \((2,2,1)\) | -2 | 15 |
| \((3,1,1)\) | 2 | 20 |
| \((3,2)\) | 0 | 20 |
| \((4,1)\) | 0 | 30 |
| \((5)\) | 1 | 24 |

These numbers are obtained by enumerating every simplex fixed setwise by each of the 120 induced vertex permutations and calculating its orientation sign. Inner products with the seven irreducible rational characters, calculated by the Murnaghan–Nakayama rule, are \(1,2,1,2,0,0,0\) in partition order \((5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1)\). Orthogonality of the generated irreducible character table and dimension \(1+2\cdot4+5+2\cdot6=26\) independently check the decomposition.

**Quotient rational homology.** A finite simplicial group action, after barycentric subdivision, gives \(H_*(X/S_5;\mathbb Q)\cong H_*(X;\mathbb Q)^{S_5}\) by the characteristic-zero transfer/averaging argument. The multiplicity of the trivial representation \(S^{(5)}\) is one, so the quotient has one rational five-dimensional reduced homology class and no others.

## Verification

Execute `python3 check_petersen_4cut.py` using Python's standard library. The program constructs the graph and every face from the definition, independently checks the 369 matching pairs and topologically sorts all 3,330 directed Hasse edges, calculates mod-two boundary ranks \((9,36,84,126,114)\), enumerates 120 full automorphism actions, reconstructs every character value, and uses a standalone rim-hook recursion to reconstruct and orthogonality-check the entire \(S_5\) irreducible character table. The expected terminal marker is `PETERSEN_4CUT_26_S5_120_FULL_CHARACTER_MORSE_OK`. This is an exhaustive finite certificate for the stated ten-vertex complex; it is not a proof of any assertion for arbitrary graphs.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced and studied ordinary graph cut complexes, giving general constructions and calculations for several graph families. In the full openly accessible preprint arXiv:2304.13675, Corollary 6.6 includes the Petersen *two*-cut complex, whereas the article's table of families and specialized calculations do not establish the present four-cut homotopy type or character. Its Theorem 6.1 cannot supply a complete-face-lattice or homology classification here: that criterion requires a complete four-skeleton, but this complex has 240 rather than all 252 possible four-dimensional simplices. Other publicly indexed results concern the Petersen ordinary *three*-cut complex and the four-cut complex of the different triangular graph \(J(5,2)\), the complement of the Petersen graph. These concern different cut thresholds or different underlying graphs, so their conclusions do not imply the theorem above. An independently indexed equivalent computation has not been ruled out.

## Limitations

The result is restricted to the ordinary four-cut complex of the Petersen graph, and to rational coefficients for its symmetry representation and quotient. It does not determine the integral homology or homotopy type of the quotient, nor higher cut thresholds or graph families. Novelty is assessed against inspected published materials and indexed summaries, not established as a complete bibliographic uniqueness claim. No independent mathematical audit has been performed.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public posting April 26, 2023); SIAM Journal on Discrete Mathematics **38** (2024), 1630–1675. https://arxiv.org/abs/2304.13675
2. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
3. A. Björner and M. L. Wachs, *Shellable nonpure complexes and posets. I*, Transactions of the AMS **348** (1996), 1299–1327. https://doi.org/10.1090/S0002-9947-96-01534-6
