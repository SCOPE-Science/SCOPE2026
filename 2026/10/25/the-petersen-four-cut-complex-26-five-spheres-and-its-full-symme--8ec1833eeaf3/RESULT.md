# The Petersen four-cut complex: 26 five-spheres and its full symmetric-group character

## Finding
Let \(P=KG(5,2)\) be the Petersen graph: its ten vertices are the two-element subsets of \([5]\), and two vertices are adjacent precisely when those subsets are disjoint. Define the **ordinary four-cut complex** \(X=\Delta_4(P)\) to be the simplicial complex whose facets are the complements, in \(V(P)\), of four-vertex subsets inducing a disconnected graph. Then there is an integral homotopy equivalence
\[
X\simeq\bigvee^{26}S^5.
\]
The natural label-permutation action of \(S_5\) on the single nonzero reduced rational homology group has the decomposition
\[
\widetilde H_5(X;\mathbb Q)\cong
S^{(5)}\oplus2S^{(4,1)}\oplus S^{(3,2)}\oplus2S^{(3,1,1)},
\]
where \(S^\lambda\) denotes the rational Specht representation indexed by \(\lambda\vdash5\). All other reduced integral and rational homology groups vanish. The seven rational character values, arranged by cycle type, are:

| Cycle type | \((1^5)\) | \((2,1^3)\) | \((2^2,1)\) | \((3,1^2)\) | \((3,2)\) | \((4,1)\) | \((5)\) |
|:--|--:|--:|--:|--:|--:|--:|--:|
| \(\operatorname{tr}(g\mid\widetilde H_5(X;\mathbb Q))\) | 26 | 6 | -2 | 2 | 0 | 0 | 1 |

In particular, the rational reduced homology of each of \(X/S_5\) and \(X/A_5\) is one-dimensional in degree five and vanishes in every other degree.

## Assumptions and scope
The graph is the ordinary simple Petersen graph, not its complement \(J(5,2)\). The cut condition means *disconnected induced subgraph*, not the independent-set condition defining the **total** four-cut complex. Homology is ordinary reduced simplicial homology over the indicated coefficients. The group action permutes the five ground labels, hence the ten graph vertices and all faces of \(X\). The conclusion is for this single ten-vertex graph; no assertion about other cut parameters or an infinite graph family is made.

## Proof
**Face structure.** The 210 four-subsets of \(V(P)\) separate into 70 connected and 140 disconnected ones. Since the Petersen graph has girth five, a connected induced four-vertex subgraph must be a four-vertex path or a three-edge claw. There are ten induced claws, one at each center, and \(10\cdot3\cdot2\cdot2/2=60\) induced four-vertex paths (count oriented nonbacktracking three-edge walks and divide by reversal). Thus \(X\) has exactly 140 facets of size six. Exhaustively enumerating all subsets of these facets gives the entire face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(10,45,120,210,240,140).
\]
As a structural check, the twelve absent size-five faces are exactly the complements of the twelve induced pentagons: a five-vertex set all of whose four-vertex deletions are connected is two-vertex-connected, hence in a graph of girth five its induced graph must be a chordless pentagon. Conversely deleting a vertex from such a pentagon leaves a connected path. These twelve exceptions distinguish the complex from the complete four-skeleton.

**Exact acyclic Morse matching.** Order the ten graph vertices lexicographically by their two-element labels. Leave the first singleton as a distinguished critical vertex. On the set of all other nonempty faces, perform ten successive element matchings: for \(i=0,\ldots,9\), simultaneously pair every remaining face not containing vertex \(i\) with its enlargement by vertex \(i\), provided both are still present, then delete both. These rules are deterministic and define disjoint cover-relation pairs.

The accompanying `verify.py` enumerates all 765 nonempty faces, constructs all 3,330 nonempty Hasse cover relations, and checks the reversed-matching directed graph by complete topological sorting. It verifies that all 765 vertices of that directed graph are processed, so there is no directed cycle. It also verifies that the matching contains exactly 369 pairs and leaves **one zero-dimensional cell and exactly 26 five-dimensional cells**, with no other critical cells. The elementary algebraic-topological discrete-Morse theorem therefore gives a CW model with one zero-cell, 26 five-cells and no other cells, hence the displayed wedge of five-spheres. This proves the integral assertion, not merely a mod-two Betti-number computation. The independent exact mod-two boundary ranks \((1,9,36,84,126,114)\) for augmented degrees zero through five corroborate the cell count.

**Group character.** For any \(g\in S_5\), it acts on the ten two-element labels and hence on the oriented augmented simplicial chain groups. A face contributes to the trace on its chain group precisely when it is setwise fixed; its contribution is the sign of the permutation of its ordered vertices. Thus the reduced Lefschetz trace is the finite signed sum
\[
L_{\mathrm{red}}(g)=\sum_{\sigma\in X}(-1)^{|\sigma|-1}
\operatorname{sgn}(g\mid\sigma),
\]
where the empty face contributes \(-1\), and nonfixed faces contribute zero. Since reduced homology is concentrated in odd degree five, the homology trace equals \(-L_{\mathrm{red}}(g)\). The attached verifier evaluates this formula for all 120 elements of \(S_5\); the seven class values are those in the table. Applying the Murnaghan–Nakayama character rule and exact character orthogonality yields precisely the four Specht summands and multiplicities stated above. The verifier implements the rim-hook recurrence and checks the seven exact scalar products. The trivial character occurs once and the sign character does not occur. Passing to a barycentric subdivision if needed makes the finite group action simplicially admissible; the rational transfer identity identifies the homology of each finite-group quotient with its rational invariant homology. For \(A_5\), invariants in an \(S_5\)-module come from the trivial and sign summands. Both quotients therefore have exactly one reduced rational degree-five class.

## Verification
Run `python3 verify.py` from the directory containing this result. The verifier depends only on the Python standard library; it constructs faces afresh from the displayed graph definition, establishes all 369 pairs and all 3,330 directed cover relations, verifies acyclicity and degree concentration, cross-checks augmented boundary ranks over \(\mathbb F_2\), checks all 120 signed Lefschetz traces, and reconstructs the rational Specht decomposition using exact integers. Its success marker is `PETERSEN_FOUR_CUT_HOMOTOPY_AND_CHARACTER_VERIFIED`. The proof of the integral homotopy claim relies on the exhaustive acyclic matching, not on extrapolating from the mod-two boundary computation.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced and studied ordinary cut complexes and proved the Petersen *two*-cut case, \(\Delta_2(P)\simeq\bigvee^6S^6\); their Petersen statement does not give the four-cut complex [1]. Bayer and collaborators' sequel treats disjoint unions, grids, squared paths and associated group characters, but not this Petersen four-cut instance [2]. A previously available three-cut Petersen computation concerns a different cut parameter, while an available four-cut computation for the triangular graph \(J(5,2)\) concerns the graph complementary to \(P\); the disconnected-induced-set condition is not invariant under graph complementation [3,4]. A high-girth theorem requiring girth at least \(k+2\) does not apply at \(k=4\) because the Petersen graph has girth five [5]. The present full homotopy type and seven-class \(S_5\)-character are not implied by those conclusions. The priority assessment is necessarily limited by the accessibility and indexing of other work.

## Limitations
Only the finite \(k=4\) Petersen instance and its natural \(S_5\)-action are proved. No canonical equivariant homotopy splitting, integral \(S_5\)-lattice decomposition, or assertion for other graphs is supplied. The explicit matching is not claimed to be equivariant; the equivariant conclusion is rational and follows instead from signed Lefschetz traces. Exact machine-verifiable finite enumeration is a component of the proof. Independent mathematical audit has not been performed.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public version 2023-04-26), particularly Definition and Corollary 6.6; https://arxiv.org/abs/2304.13675 .

[2] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first public version 2024-07-11), particularly Sections 5–6; https://arxiv.org/abs/2407.08158 .

[3] *An irreducible \(S_5\)-module in the Petersen three-cut complex*, published-finding corpus record `2026/10/11/SCOPE-an-irreducible-s-5-module-in-the-petersen-three-cut-complex--0eae16654cf3`.

[4] *Eleven three-spheres and the symmetric-group character of a four-cut complex*, published-finding corpus record `2026/10/11/SCOPE-eleven-three-spheres-and-the-symmetric-group-character-of-a-four--9dc76d8fa65e`.

[5] *High-girth cut complexes are wedges of top-dimensional spheres*, published-finding corpus record `2026/10/11/SCOPE-high-girth-cut-complexes-are-wedges-of-top-dimensional-spheres--ec8bbe3d352b`.
