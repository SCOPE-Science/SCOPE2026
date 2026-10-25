# Integral homotopy and dihedral symmetry of the Robertson cage independence complex

## Finding
Let \(R\) denote the unique nineteen-vertex, four-regular graph of girth five (the Robertson cage), and let \(K=\operatorname{Ind}(R)\) be its ordinary simplicial independence complex. Then
\[
K\simeq S^3\vee S^4\vee S^4\vee S^4.
\]
In particular, \(\widetilde H_3(K;\mathbb Z)\cong\mathbb Z\), \(\widetilde H_4(K;\mathbb Z)\cong\mathbb Z^3\), and every other reduced integral homology group vanishes.

More precisely, \(\operatorname{Aut}(R)\) is the dihedral group of order twenty-four with specified generators \(r,s\), satisfying \(r^{12}=s^2=1\) and \(srs=r^{-1}\). Let \(\epsilon\) denote the rank-one integral lattice on which \(r\) acts by \(-1\) and \(s\) acts trivially, and \(\eta\) the rank-one lattice on which both act by \(-1\). The full **integral**, not merely rational, homology representations are
\[
\widetilde H_3(K;\mathbb Z)\cong\eta,\qquad
\widetilde H_4(K;\mathbb Z)\cong\mathbb Z[C_2]\oplus\epsilon,
\]
where \(\mathbb Z[C_2]\) is inflated through \(r\mapsto\overline r\), \(s\mapsto1\). Thus the invariant and anti-invariant integral sublattices for \(r\) have sum of index two in degree-four homology, despite spanning it over \(\mathbb Q\).

## Assumptions and scope
All simplicial homology is reduced and uses integer coefficients unless indicated. The graph has vertex set \(\{0,1,\ldots,18\}\). Its edge set is determined without external data by the following first ten adjacency rows and the six remaining edges (all indices are zero-based):

```
0: 1 2 3 4
1: 0 7 8 9
2: 0 11 13 15
3: 0 10 17 18
4: 0 12 14 16
5: 6 13 16 18
6: 5 14 15 17
7: 1 12 13 17
8: 1 10 15 16
9: 1 11 14 18
remaining edges: (10,13) (10,14) (11,16) (11,17) (12,15) (12,18)
```

The attached checker verifies that this graph is four-regular with nineteen vertices and girth five, identifying it with the unique Robertson cage. A face of \(K\) is exactly a nonempty subset containing no graph edge; the empty simplex is included by convention when calculating reduced chains.

For the action statement, on these nineteen vertices the permutations \(r\) and \(s\) are specified by the following image arrays, whose position is the source vertex index:

```
r = (5,6,13,18,16,1,0,17,15,14,12,10,11,7,4,2,8,3,9)
s = (0,1,2,4,3,6,5,8,7,9,12,11,10,15,18,13,17,16,14)
```

## Proof
First enumerate every independent set via binary masks. The numbers of nonempty simplices in dimensions zero through six are
\[
(19,133,437,703,516,137,4).
\]
At successive vertices in increasing index order, pair any still-unmatched nonempty independent face not containing the vertex with the face obtained by adding that vertex, when both remain unmatched. This specifies \(970\) distinct face pairs, with critical face masks

```
Dimension 0: 1
Dimension 3: 2248, 4420, 82052
Dimension 4: 3280, 5700, 6472, 172560, 368642
```

The explicit directed Hasse-graph acyclicity check visits all \(1949\) nonempty faces across \(7819\) covering incidences. Hence the acyclic matching yields a CW complex with a point, three three-cells, and five four-cells and no other cells.

Orient every face by increasing vertex index. In the displayed ordered critical-cell bases, exact signed gradient-path reduction gives the integral cellular boundary from the five four-cells to the three three-cells (columns are written as rows):
\[
\begin{pmatrix}
-1&0&0\\
0&-1&0\\
1&-1&0\\
0&0&0\\
0&0&0
\end{pmatrix}.
\]
The first two rows give independent unit pivots, and the third column is zero. Since the three-skeleton is a wedge of three copies of \(S^3\), the four-cell attaching maps are determined by their integer degrees: \(\pi_3(S^3\vee S^3\vee S^3)\cong\mathbb Z^3\). Applying integral changes of cell bases and cancelling the two degree-one pairs gives the asserted wedge \(S^3\vee3S^4\). This proves the homotopy type, not merely the ranks of homology.

To establish the integral action, signed vertex permutations act simplicially on \(K\). The checker constructs an actual integral three-cycle of twenty-five oriented simplices mapping to the free critical three-cell coordinate, verifies its simplicial boundary is zero, and evaluates its images under all twenty-four automorphisms. Its degrees are \(\operatorname{tr}(r^ks^b\mid\widetilde H_3)=(-1)^{k+b}\) for every \(0\le k<12\) and \(b\in\{0,1\}\).

In degree four, solve the exact integral Morse boundary. One basis consists of the three critical-chain vectors
\[
(1,-1,1,0,0),\quad (0,0,0,1,0),\quad (0,0,0,0,1).
\]
Explicit gradient lifts produce genuine simplicial four-cycles with respectively \(56,98,56\) nonzero terms. After signed permutation and chain projection, the matrices of the specified generators on this integral basis are
\[
[r]_4=\begin{pmatrix}0&0&1\\0&-1&0\\1&0&0\end{pmatrix},\qquad
[s]_4=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}.
\]
They display a swapped rank-two permutation lattice and a rank-one sign lattice, proving the integral module isomorphism. The \(+1\) and \(-1\) eigensublattices for \(r\) are generated respectively by the sum of the first and third basis elements, and by their difference together with the second basis element. The determinant of these three generators has absolute value two, proving the index-two assertion.

## Verification
Run `python verify_robertson.py` after installing the dependency declared in `requirements.txt`. The program constructs the graph and all independent simplices, checks that every alleged Morse pairing is a covering relation and that the oriented Hasse digraph is acyclic, computes the signed Morse boundary, constructs integral simplicial cycle representatives, enumerates the full graph automorphism group, and checks every integral generator matrix and every homology trace. It also independently computes the mod-two ranks of the complete simplicial boundary operators as \((0,18,115,322,380,133,4)\). Its terminal marker is `VERIFY_OK_ROBERTSON_INDEPENDENCE_MIXED_WEDGE_INTEGRAL_DIHEDRAL`. The checker and dependence specification are embedded in the same package.

## Relationship to prior work
Robertson's 1964 construction and the standard graph reference identify the unique \((4,5)\)-cage. Engström's 2008 paper introduces discrete-Morse bounds for independence complexes by forest deletion, and his 2014 paper bounds total Betti numbers through disjoint-cycle structure; neither inspected theorem determines this cage's homotopy type or integral symmetry lattice. Perarnau–Perkins discuss the Robertson graph in an extremal independent-set counting conjecture, which concerns the independence polynomial or occupancy fraction, not homology. Previously recorded independence-complex calculations on other named graphs are object-specific and do not imply this graph's exact homotopy and dihedral action. The novelty assessment is evidence-limited and does not constitute a priority guarantee.

## Limitations
The conclusion is specific to the uniquely defined nineteen-vertex cage, not a theorem about all regular graphs of girth five. The discrete-Morse complex and group actions are verified by finite, fully enumerated integer computations; the topological conclusion uses standard discrete-Morse and CW attaching-map results. Unindexed or inaccessible equivalent literature cannot be excluded. No independent scientific audit has been carried out.

## References
- N. Robertson, *The Smallest Graph of Girth 5 and Valency 4*, Bulletin of the American Mathematical Society **70** (1964), 824–825.
- House of Graphs, Robertson graph, entry 1288, https://houseofgraphs.org/graphs/1288.
- E. W. Weisstein, *Robertson Graph*, MathWorld, https://mathworld.wolfram.com/RobertsonGraph.html.
- A. Engström, *Upper bounds on the Witten index for supersymmetric lattice models by discrete Morse theory*, arXiv:0805.2163 (first publicly posted 2008-05-14), https://arxiv.org/pdf/0805.2163.
- A. Engström, *Graph colouring and the total Betti number*, arXiv:1412.8460 (first publicly posted 2014-12-29), https://arxiv.org/pdf/1412.8460.
- G. Perarnau and W. Perkins, *Counting independent sets in cubic graphs of given girth*, arXiv:1611.01474, §6.1 (first publicly posted 2016-11-04), https://arxiv.org/pdf/1611.01474.
