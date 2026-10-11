# The symmetry representation and homotopy type of the total three-cut complex of the four-by-four grid

## Finding

Let \(G=P_4\mathbin{\square}P_4\) be the four-by-four square grid graph, and let \(X=\Delta^t_3(G)\) be its **total three-cut complex**. If \(F\) is the set of its nine bounded unit-square faces and \(D_4\) the group of grid symmetries, then

\[
X\simeq\bigvee^{36}S^{10},\qquad
\widetilde H_{10}(X;\mathbb Q)\cong_{\mathbb Q[D_4]}\mathbb Q\left[\binom{F}{2}\right].
\]

The second isomorphism is an **abstract rational representation isomorphism** to the permutation module on the 36 unordered pairs of distinct unit-square faces; no preferred basis is asserted. In the customary dihedral irreducible notation, the module is

\[
8A_1\oplus2A_2\oplus5B_1\oplus5B_2\oplus8E.
\]

All other reduced integral homology groups vanish, and \(\widetilde H_{10}(X;\mathbb Z)\cong\mathbb Z^{36}\). The pure 12-dimensional complex is not shellable. The rank 36 of its degree-ten homology was already published; the claims here are the complete homotopy type and the rational symmetry representation.

## Assumptions and scope

The graph has 16 vertices \(V=\{(i,j):0\le i,j\le3\}\), with two distinct vertices adjacent exactly when their Manhattan distance is one. Number these vertices \(4i+j\). For a graph \(H\), the total three-cut complex \(\Delta^t_3(H)\) has a facet \(V(H)\setminus T\) for every three-element independent vertex set \(T\); every subset of such a facet is a face. This is not the ordinary three-cut complex, whose forbidden triples need only induce disconnected graphs. The symmetry group \(D_4\) acts by the eight rotations/reflections of the square and preserves the complex. All homotopy statements concern ordinary geometric realizations. Homology is reduced unless indicated otherwise.

## Proof

**1. The exact finite complex.** There are 24 graph edges, 276 independent vertex triples, and hence 276 distinct 12-dimensional facets. Exhaustively taking subsets of their complements gives precisely 64,900 faces **including** the empty face. The nonempty face counts in dimensions zero through twelve are

\[
(16,120,560,1820,4368,8008,11440,12870,11440,8008,4368,1605,276).
\]

**2. The discrete-Morse certificate.** Starting with the full augmented face poset, for each vertex \(v=0,1,\ldots,15\) in order, match every still-unmatched face \(\sigma\) not containing \(v\) to \(\sigma\cup\{v\}\) whenever the latter face is also still unmatched, and remove both from consideration. This is a matching of cover relations: each simplex is in at most one pair. The successive pair counts are

\[
(32232,53,46,21,17,13,10,12,11,7,4,6,0,0,0,0).
\]

They sum to 32,432 pairs and leave exactly 36 faces, each of cardinality eleven (dimension ten). In particular the empty face is paired. For an independent acyclicity check, orient every codimension-one inclusion upward, reversing the 32,432 matched incidences. This directed Hasse graph has 64,900 vertices and 516,080 directed edges. A complete topological sort visits every vertex and therefore verifies that the matching is acyclic; these counts and the full test are reproduced by the included standalone program. Equivalently, the matching can be viewed on the ordinary nonempty-face poset by unmatching the empty-face pair, leaving one critical vertex and 36 critical ten-faces. Forman's discrete Morse theorem yields a CW complex with a single zero-cell, 36 ten-cells, and no other cells. The attaching maps to the zero-skeleton are constant, proving \(X\simeq\bigvee^{36}S^{10}\) and the asserted integral homology. The complex is pure of dimension twelve, so its nonzero degree-ten reduced homology obstructs pure shellability.

**3. Symmetry traces.** For each of the eight grid symmetries \(g\), enumerate its vertex orbits and their union subsets. Such a union is a setwise fixed simplex exactly when the corresponding bit mask is a face. If \(c\) vertex orbits are selected, the contribution of that simplex to the signed **reduced** Lefschetz trace is \((-1)^{c+1}\): the simplicial orientation sign \((-1)^{|\sigma|-c}\) multiplies the chain-degree sign \((-1)^{|\sigma|-1}\); this convention includes the empty face. Since reduced homology is supported only in the even degree ten, these reduced Lefschetz traces equal \(\operatorname{tr}(g\mid\widetilde H_{10}(X;\mathbb Q))\). They are

\[
\begin{array}{c|rrrrrrrr}
g&e&r&r^2&r^3&v&h&d&a\\\hline
\operatorname{tr}(g)&36&0&4&0&6&6&6&6
\end{array}
\]

where \(r\) is quarter-turn, \(v,h\) the vertical/horizontal reflections, and \(d,a\) the two diagonal reflections. The five class values, ordered as identity, half-turn, quarter-turns, axis reflections, and diagonal reflections, are \((36,4,0,6,6)\) with class sizes \((1,1,2,2,2)\). Taking inner products with the five rational irreducible characters \((A_1,A_2,B_1,B_2,E)\) gives multiplicities \((8,2,5,5,8)\).

**4. The nine-plaquette permutation representation.** The group acts on the nine unit-square cells of the four-by-four vertex grid. On unordered pairs of distinct cells, the numbers of fixed pairs are \((36,4,0,6,6)\) for the same five classes: identity fixes all 36 pairs; the half-turn has four two-cycles of cells, fixing four pairs; a quarter-turn fixes no pair; each reflection has three fixed cells and three two-cycles, fixing \(\binom32+3=6\) pairs. The included program constructs the transformed cell corners and checks every pair directly. Thus the two rational representations have exactly the same character. All irreducible representations of \(D_4\) are realizable over \(\mathbb Q\), and rational representations of finite groups are semisimple. Equality of characters proves the asserted rational module isomorphism.

## Verification

Run `python3 verify_grid_d4.py` using Python 3 and its standard library. The program rebuilds the grid, every facet and simplex, every pair in the matching, the entire reversed-edge Hasse graph, all eight signed traces, the rational character decomposition, and the permutation-character equality for unordered pairs of square cells. Its required final output line is `VERIFY_OK`. It independently checks 64,900 faces, 32,432 matched pairs, 36 critical ten-simplices, and a topological sort of all 516,080 Hasse arcs. The proof uses these exhaustive finite checks; sampling or homology ranks alone would not establish its conclusion.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue introduced total cut complexes and in Table 3 of *Total Cut Complexes of Graphs* already recorded the unique nonzero Betti number \(\beta_{10}=36\) for the four-by-four grid's total three-cut complex. That rank is not new and by itself neither gives a homotopy classification nor determines the group action. Chandrakar, Hazra, Rout, and Singh subsequently proved homotopy formulas for two-row total cut complexes and three-row total three-cut grid complexes, not the four-row instance here. Results on **ordinary** three-cut complexes apply to larger, generally distinct simplicial complexes and therefore cannot be substituted for this calculation. Work on Cartesian-product lattices treats total two-cut homotopy and explicitly leaves higher total cut parameters as a question. The closest checked published mathematical records include an ordinary ten-cut calculation for the same grid and total three-cut calculations for other graphs; their statements do not imply this result.

## Limitations

This is one finite, naturally motivated graph, not a homotopy formula for arbitrary grids. The isomorphism of \(\mathbb Q[D_4]\)-modules is abstract, not canonical, and no isomorphism of integral \(\mathbb Z[D_4]\)-lattices or explicit homology basis indexed by pairs of cells is proved. The present proof is an exhaustive finite certificate checked by the supplied program, together with standard discrete-Morse and rational representation theory. The mathematical result has not received an independent audit; an equivalent unindexed calculation elsewhere remains a bibliographic risk.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503 (first posted 2022-09-27), Definitions 2.3 and 7.1, Theorem 7.5, Table 3 (page 22 of PDF).
2. H. Chandrakar, N. R. Hazra, D. Rout, A. Singh, *Topology of total cut complexes and cut complexes of grid graphs*, arXiv:2408.07646, Theorem 1.1 and Section 4.
3. M. Bayer et al., *Topology of Cut Complexes of Graphs II*, arXiv:2407.08158, theorems on ordinary cut complexes of rectangular grids.
4. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427, Theorem 50 and Question 51.
