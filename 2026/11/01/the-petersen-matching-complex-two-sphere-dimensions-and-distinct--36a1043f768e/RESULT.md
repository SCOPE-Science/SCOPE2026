# The Petersen matching complex: two sphere dimensions and distinct symmetric-group modules

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph: its vertices are the ten two-element subsets of a five-element set, with two vertices adjacent when disjoint. Let \(\mathcal M(P)\) be its **ordinary matching complex**, whose vertices are the fifteen edges of \(P\) and whose faces are collections of pairwise vertex-disjoint edges. In particular this is neither the complex of matchings in the complete graph on five vertices nor the higher two-matching complex of \(P\).

There is an integral homotopy equivalence
\[
\bigl|\mathcal M(P)\bigr|\simeq
 \left(\bigvee^5 S^2\right)\vee\left(\bigvee^5 S^3\right).
\]
Moreover, the natural action of \(\operatorname{Aut}(P)\cong\mathfrak S_5\) on the reduced rational homology is, by degree,
\[
\widetilde H_2(\mathcal M(P);\mathbb Q)
 \cong\operatorname{sgn}\otimes\mathbb Q^{[5]},\qquad
\widetilde H_3(\mathcal M(P);\mathbb Q)
 \cong S^{(3,2)}.
\]
Here \(\mathbb Q^{[5]}\) is the five-point permutation representation, \(\operatorname{sgn}\) the sign character, and \(S^{(3,2)}\) the five-dimensional irreducible rational Specht representation. All other reduced integral homology groups vanish. The integral groups in degrees two and three are each free of rank five; the *representation identifications* asserted above are rational, not integral lattice splittings.

## Assumptions and scope
All graphs are finite, simple and undirected. The word *matching* imposes maximum selected degree one, and includes nonperfect matchings. A face of size \(k+1\) has dimension \(k\). The boundary of an oriented face uses the increasing order on the fifteen graph edges in the canonical construction below. The graph automorphism acts on oriented simplices with the sign of the induced ordering permutation. There is no parameter extrapolation: the topological conclusion concerns the specified ten-vertex Petersen graph.

## Proof
**Complete finite complex.** Enumerate the graph vertices as the lexicographically ordered two-subsets of \(\{0,1,2,3,4\}\). Enumerate its fifteen edges lexicographically among pairs of disjoint graph vertices. Encode a matching by a fifteen-bit mask. The included executable checks all \(2^{15}\) masks, accepting exactly those with pairwise disjoint endpoint masks. It obtains the face numbers
\[
(f_{-1},f_0,f_1,f_2,f_3,f_4)=(1,15,75,145,90,6).
\]
Independently, the matching polynomial is obtained by the vertex-deletion recurrence: for a chosen graph vertex \(v\), a matching either omits \(v\) or matches it to one of its available neighbors. This gives the same coefficients, with no dependence on the face-mask test.

**Explicit integral discrete-Morse model.** Process the fifteen edge indices in this precise priority order:

`14,12,9,13,0,4,3,1,7,11,8,6,5,2,10`.

At each priority, visit the still-unmatched face masks in increasing numerical order, pairing a face without that edge to the face obtained by inserting it when both faces are currently unmatched. The preliminary augmented matching pairs the empty face with a vertex; remove this one pair and retain that vertex as critical. The final matching has 160 pairs on the nonempty face poset. Its eleven critical cells have dimensions
\[
(0,2,2,2,2,2,3,3,3,3,3).
\]
Their bitmasks are, respectively, `16384` in dimension zero, `73,521,530,1156,2336` in dimension two, and `1108,1186,2124,2146,2316` in dimension three.

Acyclicity is not inferred from the greedy construction alone: the verifier constructs every one of the 975 codimension-one incidences among the 331 nonempty faces, reverses the 160 matched incidences, and topologically sorts the resulting directed Hasse graph. All 331 vertices are removed, certifying a directed acyclic graph. Forman's finite discrete-Morse theorem therefore supplies a CW model with exactly the indicated critical cells.

**Signed attaching degrees and actual homotopy type.** For each critical three-cell, its signed simplicial boundary is propagated along *all* directed gradient paths through matched two/three-cell pairs. If a noncritical two-face is the lower member of a pair, solve its signed boundary relation by dividing by the incidence \(\pm1\); if it is the upper member of a one/two-cell pair, its projected coefficient is zero. The verifier computes all 25 entries of the integral Morse differential from the five three-cells to the five two-cells. Every entry is **exactly zero**, not merely zero modulo a prime.

The Morse CW model has one zero-cell and no one-cells, so its two-skeleton is a wedge of five two-spheres. By the degree-two Hurewicz isomorphism, the homotopy class of a three-cell attaching map \(S^2\to\bigvee^5S^2\) is determined by its integral degree vector. Each vector is zero by the exact Morse differential; all five attaching maps are null-homotopic. The resulting CW space is the stated wedge of five two-spheres and five three-spheres. No higher cells remain, and the integral homology conclusion follows as well.

**Complete symmetry character.** Every permutation of the underlying five points preserves disjointness and therefore permutes the fifteen matching-complex vertices. The verifier computes the signed trace on each simplicial chain group and on the rank-79 boundary space \(B_2=\operatorname{im}(\partial_3)\). The rank is determined over the rationals from the proved Morse model and independently agrees with modular elimination. Its signed group action is reduced on a basis modulo the prime `1000003`; since the boundary representation has dimension 79 and finite order, its trace is an integer bounded in absolute value by 79, hence the modular result uniquely identifies its rational trace. The chain identities
\[
[H_2]=[C_2]-[C_1]+[C_0]-[\mathbf1]-[B_2],\qquad
[H_3]=[C_3]-[B_2]-[C_4]
\]
then give exact integer characters for **all 120 group elements**. The second identity uses injectivity of \(\partial_4\), already proved by the CW model.

For \(g\in\mathfrak S_5\), write \(f(g)\) for the number of fixed points, \(t(g)\) for the number of two-cycles, and \(\epsilon(g)\) for the permutation sign. The checked formulas are
\[
\operatorname{tr}(g\mid H_2)=\epsilon(g)f(g),\qquad
\operatorname{tr}(g\mid H_3)=\binom{f(g)}2+t(g)-f(g).
\]
The first is the sign-twisted natural five-point permutation character. The second is the difference between the permutation characters on two-subsets and one-subsets, which is the irreducible Specht character \(S^{(3,2)}\). The checker also verifies that its character norm is one using all seven conjugacy classes.

## Verification
Run `python3 verify.py` in the extracted package directory (Python standard library only). This recomputes the graph and all simplices, independently verifies their numbers by graph-vertex deletion, rebuilds and checks the full discrete-Morse matching and directed Hasse graph, computes the signed **integer** Morse boundary, and verifies the two homology characters against all 120 permutations. Expected terminal line: `ALL_VERIFY_OK`.

The seven conjugacy-class characters, ordered by cycle types `1^5`, `2 1^3`, `2^2 1`, `3 1^2`, `3 2`, `4 1`, `5`, are:

| Cycle type | \(H_2\) trace | \(H_3\) trace |
| --- | ---: | ---: |
| `1 1 1 1 1` | 5 | 5 |
| `2 1 1 1` | -3 | 1 |
| `2 2 1` | 1 | 1 |
| `3 1 1` | 2 | -1 |
| `3 2` | 0 | 1 |
| `4 1` | -1 | -1 |
| `5` | 0 | 0 |

## Relationship to prior work
Recent work of Bayer, Jelić Milutinović and Vega establishes a wedge-of-spheres conclusion for **outerplanar** graphs. The Petersen graph is nonplanar, and that theorem cannot supply this mixed-dimensional decomposition. The 2026 work of Chauhan, Sharma and Shukla concerns rectangular three-row **grid** graphs, not the Petersen graph, and studies connectivity/homology rather than these two complete symmetry modules.

A particularly important notational collision occurs in Mondal, Mukherjee and Saha: their \(M_5=\mathcal M(K_5)\) is **itself a one-dimensional Petersen graph**. Their calculation does **not** concern \(\mathcal M(P)\), which is a four-dimensional complex on fifteen vertices. Likewise, the higher two-matching complex of the Petersen graph permits degrees up to two, so its known homotopy type does not determine this subcomplex. Results for other Petersen-associated graph-Hom, cut or configuration complexes do not identify the present object or imply its homotopy or symmetry classes.

## Limitations
This is a finite graph classification; no theorem is asserted for all cubic graphs or all matching complexes. The homotopy equivalence need not be equivariant. The rational \(\mathfrak S_5\)-modules are identified by exact characters, but their integral lattice structures and equivariant attaching maps are not determined. The finite checker is a directly reproducible certificate, not an independent human validation. Exhaustive publication discovery is impossible; an unindexed equivalent calculation could still exist.

## References
1. M. Bayer, M. Jelić Milutinović, J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, first posted 2024-11-07; revised 2026-09-23. In particular Theorem 2 and its outerplanarity hypothesis.
2. P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366, first posted 2026-09-23. The abstract describes graph scope and connectivity results.
3. A. Mondal, S. Mukherjee, K. Saha, *Topology of matching complexes of complete graphs via discrete Morse theory*, Discrete Mathematics & Theoretical Computer Science 26:3 (2024), article 13. In particular its \(M_5=\mathcal M(K_5)\) convention.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. Discrete-Morse CW equivalence and gradient-path differentials.
