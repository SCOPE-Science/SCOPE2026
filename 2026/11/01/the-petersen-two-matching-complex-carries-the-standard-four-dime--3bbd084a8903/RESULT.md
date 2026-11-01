# The Petersen two-matching complex carries the standard four-dimensional symmetry module

## Finding
Let \(P=\mathrm{KG}(5,2)\) be the Petersen graph, with vertices the two-element subsets of \(\{1,2,3,4,5\}\) and edges between disjoint pairs. Let \(X=M_2(P)\) be the simplicial complex whose vertices are the 15 edges of \(P\), and whose faces are sets of graph edges with degree at most two at every vertex. The natural \(S_5\)-action on \(P\) induces an action on \(X\).

**Theorem.** Its top reduced rational homology is, as an \(S_5\)-module,
\[
\widetilde H_7(X;\mathbb Q)\cong \ker\!\left(\mathbb Q^5\xrightarrow{\text{coordinate sum}}\mathbb Q\right)\cong S^{(4,1)}.
\]
All other reduced rational homology groups vanish. More explicitly, for every \(\sigma\in S_5\),
\[
\operatorname{tr}\left(\sigma\mid\widetilde H_7(X;\mathbb Q)\right)
=\#\{i\in\{1,\dots,5\}:\sigma i=i\}-1.
\]
The full character on cycle types \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\) is \((4,2,0,1,-1,0,-1)\), respectively. Consequently no nonzero rational class is fixed by the whole \(S_5\), whereas restriction to a point-stabilizer \(S_4\) has a one-dimensional invariant subspace.

## Assumptions and scope
The graph has no loops or multiple edges. The two-matching convention permits selected edges to share a graph vertex, but at most two selected edges can meet there. Since the Petersen graph is triangle-free, this complex is also the three-clique-free complex \(\mathrm{CF}_3(L(P))\) of its line graph: all triangles in \(L(P)\) are precisely the triples of edges incident to a common vertex of \(P\). Thus the theorem also computes the corresponding \(S_5\)-module for that clique-free model.

## Proof
**Homology concentration.** Order the ten Kneser vertices lexicographically and then order their fifteen edges lexicographically. There are exactly 10,870 faces, including the empty face. In cardinality orders zero through ten, their face vector is
\[
(1,15,105,445,1245,2358,2985,2400,1095,215,6).
\]
Sequentially toggle each of the fifteen simplex vertices whenever both a face and its extension are still unmatched. Remove the empty-face pair after forming the augmented matching, promoting its singleton partner to a critical zero-cell. The resulting ordinary face-poset matching contains exactly 5,432 pairs and five critical faces: one vertex and four seven-faces. Orient each covering relation from lower to upper when matched and from upper to lower otherwise. Exhaustive topological sorting of the 10,869 nonempty faces with all 63,780 covering relations proves that this directed graph is acyclic. Forman's discrete Morse theorem therefore gives
\[
X\simeq\bigvee^4 S^7.
\]
This nonequivariant homotopy fact was previously published and is reconstructed here only as a premise; the assertion of novelty concerns the symmetry representation.

**Equivariant chain trace.** Fix \(\sigma\in S_5\), acting on the fifteen graph edges. A fixed simplicial face \(F\) is a union of \(r(F)\) orbits of that action. Let \(k=|F|\). The permutation induced by \(\sigma\) on the oriented simplex of \(F\) has sign \((-1)^{k-r(F)}\). The augmented simplicial Lefschetz formula and the concentration of reduced homology in odd degree seven therefore give
\[
\operatorname{tr}(\sigma\mid\widetilde H_7(X;\mathbb Q))
=\sum_{F:\,\sigma F=F}(-1)^{|F|}\operatorname{sgn}(\sigma\mid F)
=\sum_{F:\,\sigma F=F}(-1)^{r(F)},
\]
where the empty face contributes \(+1\). In particular the character is determined exactly by the finite orbit structure of \(\sigma\) on the fifteen graph edges together with the vertex-degree constraints on a union of orbits.

Enumerating those orbit unions, for all 120 permutations, gives the character values in the Finding. A second enumeration of all fixed faces with their actual orientation signs yields the identical seven-class table. On each conjugacy class the resulting trace equals the number of fixed labels in the natural five-point action minus one. Rational representations of finite groups are semisimple, so equality of full characters identifies the module with the augmentation subrepresentation of \(\mathbb Q^5\), which is the irreducible rational Specht module \(S^{(4,1)}\).

## Verification
The self-contained standard-library Python program `verify.py` rebuilds the Petersen graph, enumerates all 32,768 possible edge subsets, checks every degree constraint, recomputes the face vector, constructs the ordinary discrete-Morse matching and checks every directed incidence for acyclicity. It evaluates the orbit-union alternating sum for all 120 group elements and independently computes the signed fixed-face trace for each, checking the character table and the equality with fixed-label count minus one. Run `python3 verify.py` from the directory containing that file. It terminates with `ALL_VERIFY_OK` on success; all exact computations use integers, not floating point.

## Relationship to prior work
The non-equivariant sphere-wedge classification for the Petersen two-matching complex was already given in the published calculation *The Petersen 2-matching complex is a wedge of four 7-spheres* (online 2026). The present theorem strictly refines that result by identifying the entire \(S_5\)-representation, information not implied by the number of spheres. Vega studies two-matching complexes and discrete-Morse constructions; Singh studies higher matching complexes of complete and complete-bipartite graphs. The new 2026 clique-free framework of Ghosh and Selvaraja motivates the equivalent line-graph formulation. Bate, Everitt, Ford and Ramos compute symmetric-group representations for matching complexes of complete hypergraphs; those are ordinary matchings and do not imply the present bounded-degree Petersen calculation. A separate published Petersen three-cut-complex character concerns a different simplicial complex with six-dimensional homology.

## Limitations
The representation is asserted over \(\mathbb Q\); no integral \(\mathbb Z[S_5]\)-lattice isomorphism or equivariant homotopy equivalence is claimed. This one-graph calculation does not classify higher matching complexes of general cubic graphs. The uniqueness comparison covers the named primary papers, indexed related calculations, and targeted searches, not every unindexed source. The enumeration is exhaustive for this finite graph, while the semisimple-character conclusion relies on characteristic zero.

## References
1. Ghosh and Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623, first posted 2026-02-10, https://arxiv.org/abs/2602.09623.
2. Julianne Vega, *2-Matching Complexes*, arXiv:1909.10406, first posted 2019-09-23, https://arxiv.org/abs/1909.10406.
3. Anurag Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, first posted 2020-06-24, https://arxiv.org/abs/2006.13632.
4. Michael Bate, Brent Everitt, Sam Ford and Eric Ramos, *Homology of matching complexes and representations of symmetric groups*, arXiv:2312.13750, first posted 2023-12-21, https://arxiv.org/abs/2312.13750.
5. *The Petersen 2-matching complex is a wedge of four 7-spheres*, publicly available result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-the-petersen-2-matching-complex-is-a-wedge-of-four-7-spheres--c0442780c8c1.
6. *An irreducible \(S_5\)-module in the Petersen three-cut complex*, publicly available result for a distinct complex, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-an-irreducible-s-5-module-in-the-petersen-three-cut-complex--0eae16654cf3.
