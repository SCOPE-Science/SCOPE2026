# Integral three-cut topology and full symmetry character of the Shrikhande graph

## Finding
Let \(S\) denote the Shrikhande graph on \((\mathbb Z/4\mathbb Z)^2\) and \(\Delta_3(S)\) its ordinary three-cut complex. There is an integral homotopy equivalence
\[
\Delta_3(S)\simeq\bigvee^{11} S^{11}.
\]
Moreover, the full automorphism group \(A=\operatorname{Aut}(S)\), of order \(192\), acts on \(\widetilde H_{11}(\Delta_3(S);\mathbb Q)\) with the complete character tabulated below. In particular its invariant subspace is zero and the symmetry quotient is rationally acyclic:
\[
\widetilde H_i(|\Delta_3(S)|/A;\mathbb Q)=0\quad\text{for all }i.
\]
This does not claim the quotient is contractible or identify the integral equivariant lattice. The familiar cospectral rook graph \(R=K_4\square K_4\) instead has \(\Delta_3(R)\simeq\bigvee^{27}S^{11}\); the rook homology rank had already been covered by a general published result and is included only as comparison.

The following table groups all \(192\) automorphisms by their cycle lengths on the graph's sixteen vertices **and** their homology trace. Rows are not claimed to be conjugacy classes.

| Vertex cycle lengths | Trace | Number of automorphisms |
|---|---:|---:|
| `1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1` | 11 | 1 |
| `1, 1, 1, 1, 2, 2, 2, 2, 2, 2` | -5 | 12 |
| `1, 1, 1, 1, 2, 2, 2, 2, 2, 2` | -3 | 4 |
| `1, 1, 1, 1, 2, 2, 2, 2, 2, 2` | 1 | 12 |
| `1, 3, 3, 3, 3, 3` | 2 | 32 |
| `1, 3, 6, 6` | 0 | 32 |
| `2, 2, 2, 2, 2, 2, 2, 2` | 1 | 12 |
| `2, 2, 2, 2, 2, 2, 2, 2` | 3 | 3 |
| `4, 4, 4, 4` | -1 | 18 |
| `4, 4, 4, 4` | 1 | 12 |
| `4, 4, 4, 4` | 3 | 6 |
| `8, 8` | -1 | 48 |

## Assumptions and scope
The Shrikhande vertices are pairs \((a,b)\in(\mathbb Z/4\mathbb Z)^2\). Distinct vertices are adjacent precisely when their difference is one of
\[
(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)
\]
modulo four. The rook graph has the same vertex set and joins two pairs when exactly one coordinate agrees. Both are finite, simple, six-regular graphs with strongly regular parameters \((16,6,2,2)\).

For any graph \(G\) with sixteen vertices, \(\Delta_3(G)\) has facets \(V(G)\setminus T\) where \(T\) runs over triples inducing a disconnected graph (zero or one induced edge). Its combinatorial Alexander dual \(L(G)=\Delta_3(G)^\vee\) consists exactly of sets in which **every** triple induces at least two edges. These definitions fix the cutoff and use ordinary, not total, cut complexes.

## Proof
1. **Complete dual face enumeration.** There are \(384\) disconnected triples for each graph. For \(S\), exhaustive independent tests of all \(65{,}536\) vertex subsets give the augmented face counts for \(L(S)\), indexed by face size \(0\) through \(4\), as \((1,16,120,176,60)\), and zero faces with more than four vertices. For \(R\) the corresponding vector is \((1,16,120,176,44)\). These dual complexes contain the complete graph on sixteen vertices as their one-skeleta. Their ordinary cut complexes respectively have \(65{,}163\) and \(65{,}179\) augmented faces, and \(384\) facets of dimension twelve each.

2. **Exact integral chains.** Orient faces by increasing vertex label. The augmented integral chain groups of \(L(S)\) through dimension three have ranks \((16,120,176,60)\). Both compositions of consecutive signed boundaries vanish by direct integer calculation. Fix vertex zero as root and identify the integral cycle lattice of the full sixteen-vertex one-skeleton with its \(\binom{15}{2}=105\) nonstar edge coordinates. Exact integer row and column elimination of the boundary from two-faces produces \(105\) unit pivots and no nonzero residual entries: its image equals the entire one-cycle lattice integrally. Independent integer reduction of the boundary from three-faces has \(60\) unit pivots and zero residual. Consequently this last map is split injective and its image is a primitive sublattice. Thus
\[
\widetilde H_2(L(S);\mathbb Z)\cong\mathbb Z^{176-105-60}=\mathbb Z^{11},
\]
with all other reduced integral homology zero. The same steps on \(L(R)\) have \(105\) and \(44\) unit pivots, giving rank \(27\). The provided certificate records each explicit integer-unit pivot; the checker replays their elimination and verifies that every residual matrix vanishes.

3. **Passage to cut homotopy.** Integral combinatorial Alexander duality on the fifteen-simplex identifies \(\widetilde H_j(\Delta_3(S);\mathbb Z)\) with \(\widetilde H^{13-j}(L(S);\mathbb Z)\) (since the ambient graph has sixteen vertices, the index is \(16-j-3\)). The dual cohomology is free and concentrated in dimension two, hence the cut homology is free of rank eleven in dimension eleven and zero otherwise. Because the dual has no faces of size five, the cut complex contains the full ten-skeleton of the fifteen-simplex; it is therefore at least nine-connected. The zero degree-ten homology makes it ten-connected by the first nonvanishing Hurewicz theorem. Hurewicz identifies its eleventh homotopy group with \(\mathbb Z^{11}\), allowing a wedge of eleven eleven-spheres to map by generators and induce an integral homology isomorphism. Both spaces are simply connected CW complexes, so Whitehead's homology theorem supplies the claimed homotopy equivalence. The same argument gives the rook comparison.

4. **Full group and rational character.** Translations by \((\mathbb Z/4\mathbb Z)^2\) and twelve invertible linear maps preserving the six difference vectors give \(192\) distinct automorphisms of \(S\). This is the entire group: the graph induced on the six neighbors of a vertex is a six-cycle, while the nine distance-two vertices are individually determined by their distinct two-element neighbor sets in this cycle. Thus the vertex stabilizer injects into its dihedral group of order twelve. Every one of the \(192\) constructed vertex permutations is even, checked by inversion parity. For each group element, the signed simplicial chain traces on \(L(S)\) determine its second reduced homology character through
\[
\chi(g)=\operatorname{tr}(g|C_0)-\operatorname{tr}(g|C_1)+\operatorname{tr}(g|C_2)-\operatorname{tr}(g|C_3)-1.
\]
Equivariant Alexander duality twists this character by the sign of the ambient vertex permutation, here always \(+1\). For **every** automorphism a separate direct Lefschetz sum over its setwise-fixed cut faces, including the orientation sign, reproduces the same trace. The table therefore lists the full character, with no dependence on floating-point calculations.

5. **Quotient.** Summing the \(192\) character values gives exactly zero. The averaging projector therefore shows \(\dim\widetilde H_{11}(\Delta_3(S);\mathbb Q)^A=0\). For a finite simplicial group action, rational transfer (or averaging on a subdivision) identifies rational homology of the orbit space with the invariant rational homology. Since all other positive-degree reduced homology groups vanish and the space is connected, its orbit space is rationally acyclic.

## Verification
Run `python3 verify.py certificate.json` with Python 3 and the standard library; the exact expected text is in `verification_output.txt`. The checker independently checks graph adjacency and strongly regular parameters; all induced triples and all sixteen-vertex subsets; both descriptions of the dual; integral signed boundary-square identities; all \(105+60+105+44=314\) certificate unit pivots and terminal zero blocks; full automorphism-group upper and lower bounds; all \(192\) character values; and the direct fixed-cut-face Lefschetz check for every group element. Its final marker is `SHRIKHANDE_ROOK_THREE_CUT_INTEGRAL_EQUIVARIANT_OK`. This is a finite exact proof certificate, not a claim about other graph orders.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduce ordinary cut complexes and study their topological behavior in *Topology of Cut Complexes of Graphs* (first publicly posted April 26, 2023). Their strong complete-skeleton statements do not supply the present answer: this ordinary three-cut complex does **not** have a complete eleven-skeleton, as its eleven-dimensional face count is only \(1760\) versus \(\binom{16}{12}=1820\). Their 2024 sequel studies unions, squared paths and grids, not the present Shrikhande graph.

A separate published calculation of the ordinary three-cut complex of rook graphs gives the rook rank \(27\), which is expressly **not** claimed as new. The Shrikhande graph is not isomorphic to the rook graph, despite their identical strongly regular parameters; the rook result gives no Shrikhande homotopy type or its \(192\)-element automorphism character. Previous results on Shrikhande independence, neighborhood and four-cut complexes address distinct face conditions. The new contribution is the Shrikhande three-cut integral homotopy equivalence and its full rational symmetry character.

## Limitations
This is a finite classification for one natural graph, not a general statement for all strongly regular graphs or all cut thresholds. The rational character does not determine the integral action, attaching-map equivariance, or contractibility of the symmetry quotient. The literature comparison includes inspected primary papers and relevant indexed records; an unindexed equivalent computation remains possible. The self-review is not independent mathematical verification.

## References
- M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first public version 2023-04-26.
- M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first public version 2024-07-11.
- *Integral and equivariant homology of three-cut complexes of rook graphs*, published mathematical record, identifier `2026/10/11/SCOPE-integral-and-equivariant-homology-of-three-cut-complexes-of-rook--bd50464fc17f`, treated as prior coverage of the rook comparison.
- Standard integral combinatorial Alexander duality, Hurewicz and Whitehead theorems, and rational transfer for finite-group actions.
