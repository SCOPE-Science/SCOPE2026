# Integral equivariant persistence of the four-label permutahedron

## Finding
Let \(P\) be the graph on the \(24\) permutations of \(\{0,1,2,3\}\), where adjacent permutations differ by a swap in consecutive positions; let \(K_r=\operatorname{VR}_{\le r}(P)\) for its shortest-path metric. The group \(W=S_4\times C_2\) acts by relabeling symbols and reversing positions, and acts simplicially on \(K_2\subset K_3\). Let \(\mathcal H\) be the eight hexagonal facets of the three-dimensional permutahedron, four fixing the first symbol and four fixing the last. There is an exact sequence of **integral \(W\)-modules**
\[
0\longrightarrow\mathbb Z[\mathcal H]\xrightarrow{\;h\;} H_2(K_2;\mathbb Z)\xrightarrow{\;i_*\;}\mathbb Z_{\operatorname{sgn}\boxtimes\varepsilon}\longrightarrow0,
\]
where \(h\) sends each facet to the homology class of the oriented octahedral two-sphere supported on its six vertices, \(\operatorname{sgn}\) is the sign character of the relabeling \(S_4\), and \(\varepsilon\) is the nontrivial character of position reversal. In particular the inclusion is integrally surjective, its kernel is a **primitive rank-eight permutation lattice**, and \(H_2(K_2;\mathbb Z)\cong\mathbb Z^9\), \(H_2(K_3;\mathbb Z)\cong\mathbb Z\). The sequence splits as abelian groups; no integral \(W\)-equivariant splitting is asserted.

Over \(\mathbb Q\), Maschke's theorem gives
\[
H_2(K_2;\mathbb Q)\cong [(\mathbf1\oplus\mathrm{Std}_3)\boxtimes(\mathbf1\oplus\varepsilon)]\oplus(\operatorname{sgn}\boxtimes\varepsilon),\qquad H_2(K_3;\mathbb Q)\cong\operatorname{sgn}\boxtimes\varepsilon.
\]
The first summand is the eight-dimensional permutation module on \(\mathcal H\). This refines previously determined nonequivariant homotopy types and mod-two barcodes for the **same graph**, which alone do not determine the geometric integral persistence kernel or either symmetry representation.

## Assumptions and scope
Vertices are permutations \(p=(p_0,p_1,p_2,p_3)\) of \(\{0,1,2,3\}\). The edge metric is the minimum number of adjacent-position swaps. A nonempty set spans a simplex of \(K_r\) precisely when all its graph distances are at most \(r\). A group element \((\sigma,\delta)\in S_4\times C_2\) acts by \(p_j\mapsto\sigma(p_{3-j})\) when \(\delta=1\) and \(p_j\mapsto\sigma(p_j)\) otherwise. These operations commute and preserve the graph metric. The statement concerns the **inclusive integer radii two and three**, with ordinary oriented simplicial chains over \(\mathbb Z\); it does not concern Euclidean distances between embedded permutahedron vertices.

There are eight distinguished six-vertex subsets \(F_{\mathrm{first},a}=\{p:p_0=a\}\) and \(F_{\mathrm{last},a}=\{p:p_3=a\}\), for \(a=0,1,2,3\). Within each \(F\), exactly three disjoint pairs have graph distance three and all other pairs have distance at most two. Thus its induced \(K_2\) is the join of three copies of \(S^0\), an octahedral two-sphere. Orient the first four spheres by their canonical three-pair tensor-chain construction and negate the last four orientations, so every element of \(W\) permutes the eight oriented sphere chains without additional signs. The chain formula and the label ordering are implemented in `verify.py`.

## Proof
**Finite complexes and homotopy.** Exhaustive increasing-clique enumeration gives the face vectors \((24,96,112,30)\) for \(K_2\) and \((24,168,472,618,384,92)\) for \(K_3\). The two complete operation certificates `morse_scale2.json` and `morse_scale3.json` list elementary free codimension-one face/coface pairs and top-dimensional critical-simplex removals. Replay independently checks each free-face condition against **all remaining** cofaces and checks directed-Hasse acyclicity. The respective certificates have \(126\) and \(878\) matched pairs and exactly one critical vertex plus nine critical triangles at radius two, and one critical vertex plus one critical triangle at radius three. Discrete Morse theory therefore gives \(K_2\simeq\bigvee^9 S^2\) and \(K_3\simeq S^2\), proving both homology lattices are free of the stated ranks. These homotopy types agree with prior published calculations and are used only as premises, not proposed as the new contribution.

**Geometric kernel and its integral saturation.** For each \(F\in\mathcal H\), take the signed sum of the eight triangles formed by choosing one vertex from each of its three distance-three pairs. Every edge cancels twice with opposite signs, so \(h_F\) is an integral two-cycle. At radius three, all six vertices of \(F\) span a simplex, so \([h_F]\in\ker i_*\). In the degree-two oriented chain group of \(K_2\), form the integer matrix \(A\) whose first thirty columns are the oriented boundaries of its thirty tetrahedra, next eight columns are the \(h_F\), and final column is the explicitly listed signed twenty-triangle cycle \(z\) in `primitive_cycle.json`. Its size is \(112\times39\). Exact calculations reconstruct the edge/triangle boundary matrix \(\partial_2\), verify \(\partial_2 A=0\) and \(\operatorname{rank}(\partial_2)=73\), and compute the Smith normal form of \(A\): it has precisely \(39\) nonzero elementary divisors, **every one equal to one**. Therefore the column lattice of \(A\) is saturated in \(\mathbb Z^{112}\) and has the same rank \(112-73=39\) as \(\ker\partial_2\), so these lattices are equal. Modulo the thirty independent tetrahedral boundaries, the eight hexagon cycles and \(z\) form an **integral basis** of \(H_2(K_2;\mathbb Z)\). In particular the eight hexagon classes generate a primitive direct summand, with no hidden torsion or index.

**Primitive persistent generator.** Reverse the complete radius-three collapse certificate to construct an integer simplicial two-cocycle \(c\) supported on thirty-four triangles, assigning value one to the unique critical triangle and propagating across free pairs with their incidence signs. The verifier checks \(\delta c=0\) against every tetrahedron of \(K_3\), and checks that \(\langle c,z\rangle=-1\). The cellular collapse sends \(c\) to the unit dual generator of \(H^2(K_3;\mathbb Z)\). Thus \(i_*[z]\) is a primitive generator, the eight hexagon cycles are the whole kernel, and the asserted sequence is exact. This is an integral statement, not an inference from a characteristic-two barcode.

**Symmetry character.** The certificate directly checks that every \(g\in W\) carries \(h_F\) to \(h_{gF}\) as an **equality of oriented simplicial chains**, fixing the lattice identification \(\ker i_*\cong\mathbb Z[\mathcal H]\). For every one of the \(48\) group elements, exact signed fixed-simplex Lefschetz sums compute \(\operatorname{tr}(g|H_2(K_r;\mathbb Q))=L(g,K_r)-1\), because each complex is connected and has only second rational homology. The radius-three trace is \(\operatorname{sgn}(\sigma)(-1)^\delta\); this is also verified independently from the transformed primitive cycle's cocycle pairing. The rank-eight facet-permutation representation is the sum of two four-point permutation representations exchanged by reversal; the four-point permutation module of \(S_4\) is \(\mathbf1\oplus\mathrm{Std}_3\). Characteristic zero semisimplicity gives the displayed rational direct sum.

The complete character table has rows indexed by the cycle partition of \(\sigma\); each ordered pair is \((\operatorname{tr}_{K_2},\operatorname{tr}_{K_3})\) for \(\delta=0\) and then \(\delta=1\):

| Cycle partition | No reversal | Reversal |
| --- | --- | --- |
| \((1,1,1,1)\) | \((9,1)\) | \((-1,-1)\) |
| \((2,1,1)\) | \((3,-1)\) | \((1,1)\) |
| \((2,2)\) | \((1,1)\) | \((-1,-1)\) |
| \((3,1)\) | \((3,1)\) | \((-1,-1)\) |
| \((4)\) | \((-1,-1)\) | \((1,1)\) |

## Verification
Run `python3 verify.py` alongside `morse_scale2.json`, `morse_scale3.json`, and `primitive_cycle.json` with Python 3 and SymPy 1.14.0. It reconstructs the labeled graph and shortest-path distance, enumerates all simplices, replays **every** collapse and verifies acyclicity on the full oriented Hasse graph, constructs the nine integer cycles, computes the exact \(39\)-column Smith certificate, checks the radius-three cocycle and primitive pairing, and checks each of the \(48\) symmetry actions and signed Lefschetz sums. No precomputed boundary matrices or character values are trusted as input. The execution recorded in `verification_output.txt` terminates with `VERIFY_OK_PERMUTOHEDRON_EQUIVARIANT_PERSISTENCE`.

## Relationship to prior work
The same graph is also the truncated-octahedral graph. The publicly available result **“Complete graph-metric Vietoris--Rips filtration of the truncated octahedral graph”** already establishes its nonequivariant sphere-wedge homotopy types at all integer scales, including \(K_2\simeq\bigvee^9S^2\) and \(K_3\simeq S^2\). **“Complete mod-two Rips persistence of the four-letter permutahedron”** already establishes the characteristic-two barcode, including eight degree-two intervals dying at radius three and one dying at radius four. These existing claims supply the dimensions but **neither entails** the integral primitive nature of the eight hexagonal facet cycles, the exact \(W\)-lattice sequence, the quotient orientation character, or the complete equivariant character table proved here. Adamaszek identifies graph-power clique complexes with graph-metric Rips complexes; Adamaszek--Adams classifies the circle case. The latter does not classify this 24-vertex permutation metric or its equivariant persistence.

## Limitations
No integral \(W\)-equivariant splitting of the sequence is claimed. No classification of the integral \(W\)-action in scales other than two and three, equivariant homotopy type, or filtration maps at other radii is asserted. The novelty comparison includes directly covering aliases and known same-graph results but cannot exclude an unindexed equivalent calculation. The finite exhaustive certificate establishes exactly the stated 24-vertex object and not a uniform assertion for higher permutahedra. Independent external scientific audit has not been performed.

## References
1. M. Adamaszek, “Clique complexes and graph powers,” arXiv:1104.0433v1 (first public version 2011-04-03).
2. M. Adamaszek and H. Adams, “The Vietoris--Rips complexes of a circle,” arXiv:1503.03669v1 (first public version 2015-03-12).
3. “Complete graph-metric Vietoris--Rips filtration of the truncated octahedral graph,” published mathematical research record, 2026-10-11.
4. “Complete mod-two Rips persistence of the four-letter permutahedron,” published mathematical research record, 2026-10-11.
