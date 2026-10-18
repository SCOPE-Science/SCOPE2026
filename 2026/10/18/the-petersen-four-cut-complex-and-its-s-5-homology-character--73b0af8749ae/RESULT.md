# The Petersen four-cut complex and its \(S_5\) homology character

## Finding

Let \(P=KG(5,2)\) be the Petersen graph. Its ordinary four-cut complex satisfies
\[
\Delta_4(P)\simeq\bigvee^{26}S^5.
\]
Under the canonical \(S_5\)-action on the graph labels, the complete rational homology representation is
\[
\widetilde H_5(\Delta_4(P);\mathbb Q)
 \cong\operatorname{Sp}^{(5)}\oplus 2\operatorname{Sp}^{(4,1)}
 \oplus\operatorname{Sp}^{(3,2)}\oplus 2\operatorname{Sp}^{(3,1,1)},
\]
with all other reduced homology groups zero. Here \(\operatorname{Sp}^{\lambda}\) denotes the rational Specht representation of the indicated partition of five. The character in the ordered conjugacy classes \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\) is \((26,6,-2,2,0,0,1)\). The homotopy equivalence is not claimed to be \(S_5\)-equivariant.

## Assumptions and scope

The ten vertices of \(P\) are unordered pairs of elements of \([5]=\{1,2,3,4,5\}\); distinct pairs are adjacent precisely when disjoint. For any finite graph \(G\), \(\Delta_4(G)\) means the **ordinary**, not total, cut complex: its facets are \(V(G)\setminus W\), with \(|W|=4\) and the induced subgraph \(G[W]\) disconnected. Every facet here has six vertices, so the complex is pure of dimension five. All faces, including the empty face, are included. The ten Petersen vertices and five ground labels carry the indicated natural permutation action.

## Proof

**Complete simplicial enumeration.** List the ten unordered ground-label pairs lexicographically and number them \(0\) through \(9\). Among the \(\binom{10}{4}=210\) four-vertex subsets, exactly \(140\) induce disconnected subgraphs, checked by graph traversal on the induced subgraphs. Complementation produces \(140\) six-vertex facets. Enumerating every subface of these facets gives the exact face vector, in dimensions \(-1,0,1,2,3,4,5\):
\[
(1,10,45,120,210,240,140).
\]
This enumeration is algorithmic and exhaustive because it ranges over all \(210\) subsets and all submasks of every resulting facet.

**Acyclic discrete-Morse matching.** Work on the poset of all \(765\) nonempty faces. Iterate through the ten vertices in their lexicographic order. At stage \(v\), among faces not matched at earlier stages, match each eligible pair \((F,F\cup\{v\})\) provided both faces are still unmatched and \(v\notin F\). Never match the empty face. A complete computation yields exactly \(369\) disjoint matched pairs, leaving one unmatched vertex and \(26\) unmatched five-simplices; there are no unmatched positive-dimensional faces below dimension five.

To certify acyclicity, form the full directed Hasse graph on all \(765\) nonempty faces: orient each matched cover relation from the smaller face to the larger face, and orient every other cover relation downward. The attached checker constructs **every** such directed covering edge and uses a topological sort. It visits all \(765\) faces, proving that no directed gradient cycle occurs. This is a finite complete verification of the required combinatorial certificate, not sampling. The discrete-Morse theorem therefore gives a CW model with one zero-cell, \(26\) five-cells, and no other cells. Every attaching map to its zero-skeleton is constant, so the complex is homotopy equivalent to a wedge of \(26\) five-spheres. In particular its integral homology is torsion-free.

**The \(S_5\) character.** For each \(g\in S_5\), let \(g\) act on the ten pairs. A face \(F\) fixed setwise by \(g\) contributes the sign of the vertex permutation \(g|_F\) to the trace on its oriented simplicial chain, and a nonfixed face contributes zero. The reduced Hopf trace formula, with the empty face and the homological concentration just proved, gives
\[
\chi(g)=\sum_{F\in\Delta_4(P),\;gF=F}
(-1)^{|F|}\operatorname{sgn}(g|_F).
\]
The attached checker enumerates all \(120\) permutations and all \(766\) faces, computing the character on the seven cycle types:

| Cycle type | \((1^5)\) | \((2,1^3)\) | \((2^2,1)\) | \((3,1^2)\) | \((3,2)\) | \((4,1)\) | \((5)\) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Class size | 1 | 10 | 15 | 20 | 20 | 30 | 24 |
| \(\chi(g)\) | 26 | 6 | -2 | 2 | 0 | 0 | 1 |

For an equivalent closed expression, let \(f(g)\) be the number of ground-label fixed points and \(p(g)\) the number of invariant unordered pairs of ground labels. Then the table is exactly
\[
\chi(g)=p(g)+f(g)^2-f(g)+1-f(g^2).
\]
To decompose it, the standard module \(U=\operatorname{Sp}^{(4,1)}\) has character \(f-1\); \(\operatorname{Sp}^{(3,2)}\) has character \(p-f\) by the two-subset permutation module; and \(\operatorname{Sp}^{(3,1,1)}\cong\bigwedge^2U\) has character \(\big((f-1)^2-(f(g^2)-1)\big)/2\). The character inner products with the seven irreducibles (ordered \((5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1),(1^5)\)) are exactly
\[
(1,2,1,2,0,0,0).
\]
These nonnegative integral multiplicities prove the asserted rational representation isomorphism.

## Verification

Run `python3 verify.py` using Python 3.9 or later; no third-party packages are required. The standalone file independently constructs the graph, all induced four-vertex subgraphs, all facets, all faces, the lexicographic matching, and the entire directed Hasse graph. It verifies the \(369\) matching pairs and all \(765\) vertices in an acyclic topological sort; it independently computes mod-two boundary ranks \((9,36,84,126,114)\) from dimensions one through five. It exhausts all \(120\) elements of \(S_5\), validates each trace against its conjugacy class, and computes all rational irreducible character inner products. Expected output begins `VERIFY_OK`. The full finite certificate, including the matching and acyclicity check, can be regenerated from this file; no external logs or downloaded datasets are needed.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced and studied ordinary cut complexes and computed the Petersen graph's **two-cut** complex as a wedge of six six-spheres (Corollary 6.6 of the cited original paper). Their section on \(k\ge3\) treats other graph families and does not give this ordinary four-cut classification or its \(S_5\)-character. Their sequel analyzes disjoint unions, squared paths, grids, and the equivariant homology of disjoint complete graphs, paths, and cycles, rather than this Petersen instance. These results establish the relevant framework but neither supply the distinct four-cut matching nor imply the computed representation. The present result concerns the fixed Petersen graph and one precise cut parameter, not all Kneser graphs or cut parameters.

## Limitations

The calculation is exact for the specified ten-vertex graph; it is not a general family theorem. No equivariant wedge decomposition or canonical rational representation isomorphism is claimed. The mod-two boundary check alone would not prove the integral or homotopy statements; those follow from the verified acyclic matching. The literature comparison cannot exclude unpublished or unindexed equivalent calculations. A separate independent mathematical audit has not been performed.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public April 26, 2023), especially Definition 2.1, Theorem 6.4, Corollary 6.6 and Sections 6–7. https://arxiv.org/html/2304.13675v2
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first public July 11, 2024), especially Sections 3–6. https://arxiv.org/html/2407.08158v1
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. Discrete-Morse theorem invoked for an acyclic face-poset matching.
