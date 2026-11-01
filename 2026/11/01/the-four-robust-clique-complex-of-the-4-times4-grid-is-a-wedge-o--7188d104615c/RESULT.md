# The four-robust clique complex of the \(4\times4\) grid is a wedge of 84 five-spheres

## Finding
For the ordinary 16-vertex square grid \(G=P_4\mathbin{\square}P_4\), let \(K=\operatorname{Cliq}_4(G)\) be the simplicial complex whose faces contain no independent four-set of the induced graph. Then
\[
\boxed{|K|\simeq\bigvee^{84} S^5.}
\]
Thus \(\widetilde H_5(K;\mathbb Z)\cong\mathbb Z^{84}\), and every other reduced integral homology group vanishes. The graph automorphism group \(D_4\) acts on fifth rational homology, with character
\[
\boxed{\chi(1,r,r^2,s_a,s_d)=(84,0,4,-10,-10),}
\]
where \(r\) is a quarter-turn, \(s_a\) a reflection across a horizontal or vertical axis, and \(s_d\) a diagonal reflection. The character is constant on conjugacy classes, and under standard dihedral notation the rational representation is
\[
\boxed{\widetilde H_5(K;\mathbb Q)\cong6A_1\oplus16A_2\oplus11B_1\oplus11B_2\oplus20E.}
\]
Here \(A_1\) is trivial; \(A_2\) is the reflection sign; \(B_1,B_2\) send the quarter-turn to \(-1\), with the two possible reflection signs; and \(E\) is the two-dimensional square representation. No canonical or integral module splitting is asserted.

## Assumptions and scope
The 16 grid vertices are labelled \(v_{r,c}=4r+c\) for \(0\le r,c\le3\), with adjacency exactly at Manhattan distance one. A face is a vertex subset whose induced graph has independence number at most three; the empty face is used only in the augmented face-enumeration convention. This is **not** the usual flag clique complex, the ordinary cut complex, the total cut complex, or a matching complex. The complex is finite and all homotopy statements refer to geometric realizations. The group \(D_4\) consists of eight geometric symmetries of the square grid.

## Proof
**Exact face construction.** Encode vertex subsets by 16-bit masks. Every independent four-set is a forbidden minimal nonface. Exhaustively test the \(\binom{16}{4}=1820\) four-subsets using the Manhattan graph adjacency rule; exactly 405 are independent. A subset mask is a simplex if and only if it contains none of those 405 masks. Testing all \(2^{16}=65536\) subsets then yields precisely 4,811 nonempty faces with dimension-wise counts
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(16,120,560,1415,1788,912).
\]
There are no higher faces. This enumeration is an exhaustive characterization by the definition, not a sample.

**Complete acyclic discrete-Morse matching.** Begin with the 4,812 masks including the empty mask. For each vertex index \(i=0,1,\dots,15\), in increasing order, pair every as-yet-unpaired face mask \(\sigma\) not containing vertex \(i\) with \(\sigma\cup\{i\}\), provided both are still present, and remove both from the candidate pool. To define a deterministic implementation, traverse available masks in increasing numerical order at each stage. The procedure yields 2,364 pairs including the unique pair \((\varnothing,\{v_{0,0}\})\); the remaining 84 masks all have six vertices. Delete that empty-face pair from the ordinary nonempty-face-poset matching, leaving 2,363 matched face incidences and one additional unmatched vertex \(v_{0,0}\).

The explicit standalone checker constructs the *entire* ordinary Hasse graph. Every codimension-one incidence is oriented from the larger to the smaller simplex except that a matched incidence is reversed. It checks 21,992 directed incidences, and a complete topological sort visits all 4,811 faces. Thus the matching contains no closed gradient path. This is a complete finite proof of acyclicity because every face and incidence is generated from the explicit graph definition. The critical cells are exactly one zero-cell and 84 five-cells; there are no other critical cells.

Forman's discrete Morse theorem gives a CW complex with precisely those cells. Every five-cell attaches to the zero-dimensional four-skeleton, hence attaches trivially. The CW complex is therefore a wedge of 84 five-spheres. This proves the complete **integral homotopy type**, not merely a Betti-number identity. As a count check, the reduced Euler characteristic computed from the face vector is \(-84\).

**Square symmetry representation.** Each of the eight symmetries acts as an explicit vertex permutation and hence a simplicial automorphism. For each symmetry, the checker loops over *all* faces, retaining those setwise fixed. If the fixed simplex has ordered vertices \(i_0<\cdots<i_d\), its contribution to the reduced Lefschetz trace is \((-1)^d\) times the sign of the induced permutation on these ordered vertices. The augmented empty simplex contributes \(-1\). These signed fixed-simplex sums are exactly \((-84,0,-4,0,10,10,10,10)\) for identity, the three nontrivial rotations, and the four reflections, in that order. This uses the simplicial Hopf trace identity, including orientation signs. Because the homotopy classification places all reduced rational homology in odd degree five, multiplying the reduced Lefschetz traces by \(-1\) gives the class character \((84,0,4,-10,-10)\).

The conjugacy-class sizes in the order used above are \((1,2,1,2,2)\). The five rational irreducible character rows are \(A_1=(1,1,1,1,1)\), \(A_2=(1,1,1,-1,-1)\), \(B_1=(1,-1,1,1,-1)\), \(B_2=(1,-1,1,-1,1)\), and \(E=(2,0,-2,0,0)\). Character inner products yield the multiplicities \((6,16,11,11,20)\); their dimension-weighted sum is \(84\).

## Verification
Run `python3 verify.py` using Python 3 standard library. It reconstructs all independent four-sets; all 4,811 nonempty faces; all 2,363 ordinary matching pairs and critical cells; the 21,992 codimension-one incidences; and an exhaustive directed-acyclicity test. It separately applies eight explicitly defined grid symmetries to the complete face set and calculates signed reduced Lefschetz traces and rational character multiplicities. Each specified total is asserted, and the program reports `VERIFY_OK` only if every check succeeds. There are no external datasets, seeds, hidden solver outputs, or unresolved dependencies. The computations are finite but exhaustive for this fixed grid; they do not classify larger grids.

## Relationship to prior work
Filakovský's paper (first publicly posted February 11, 2026) defines robust clique complexes, proves the grid homotopy classification for parameters two and three, and proves higher-parameter classifications for square sequences assembled exclusively by edge gluings. Its Conjecture 1.5 proposes wedge-of-spheres results for all square sequences and greater parameters, explicitly identifying corner attachments at parameters above three as a technical obstacle. The \(4\times4\) grid necessarily uses corner gluings in the row-by-row square sequence; the higher-parameter edge-only result therefore does not cover the current claim. The paper gives a separate maximal-independence-number example, but the grid here has independence number eight, so that specialization also does not cover parameter four.

Prior results on the same grid's **total three-cut** complex, or on the **three-robust** complex of all bipartite graphs, concern a different robust parameter. The earlier four-robust result for the \(3\times4\) rectangular grid concerns a strictly smaller graph; no homotopy equivalence or induction from that instance to \(4\times4\) is supplied by those statements. The present result has its own full finite acyclic-matching certificate and a complete \(D_4\) homology character. The Alexander-dual total four-cut complex is an equivalent rephrasing of the object's combinatorics, not a known stronger theorem in the reviewed materials.

## Limitations
This is a complete fixed-graph theorem, not an all-grid solution to Conjecture 1.5. It does not prove that all four-robust square-sequence complexes are sphere wedges, does not identify canonical equivariant sphere representatives, and does not establish an integral decomposition of the \(D_4\)-module. Similar unpublished or unindexed calculations remain possible, and independent mathematical evaluation has not been performed.

## References
1. Marek Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365v1, publicly posted 2026-02-11, https://arxiv.org/abs/2602.11365.
2. A three-sphere wedge theorem for robust clique complexes of all connected bipartite graphs, published-finding corpus, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-three-sphere-wedge-theorem-for-robust-clique-complexes-of-all--8d06720b1a2b.
3. The symmetry representation and homotopy type of the total three-cut complex of the four-by-four grid, published-finding corpus, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-symmetry-representation-and-homotopy-type-of-the-total-three--d656b073fa51.
