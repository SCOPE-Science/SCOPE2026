# Mixed-dimensional homotopy of the octahedral two-matching complex

## Finding

Let \(O=K_{2,2,2}\) be the octahedral graph. Its two-matching simplicial complex has the exact integral homotopy type

\[
M_2(O)\simeq\bigvee^{3}S^3\vee\bigvee^{7}S^4.
\]

In particular, \(\widetilde H_3(M_2(O);\mathbb Z)\cong\mathbb Z^3\), \(\widetilde H_4(M_2(O);\mathbb Z)\cong\mathbb Z^7\), and all other reduced integral homology groups vanish. There is no torsion. The complex is not pure: it has maximal simplices of dimensions \(3\), \(4\), and \(5\).

## Assumptions and scope

Number the graph vertices \(0,1,2,3,4,5\) and form the three opposite pairs \(\{0,1\}\), \(\{2,3\}\), and \(\{4,5\}\). The twelve graph edges are the unordered pairs of vertices in different opposite pairs, ordered lexicographically:

```text
(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),
(1,4),(1,5),(2,4),(2,5),(3,4),(3,5)
```

An edge subset \(F\) is a face of \(M_2(O)\) precisely when every one of the six graph vertices has degree at most two in the selected-edge subgraph \((V(O),F)\). The empty set is included. This is the usual two-matching or constant-bound-two bounded-degree complex, *not* the ordinary matching complex and not the complex of acyclic Morse matchings.

The statement concerns this one finite graph; it does not assert any larger-family homotopy classification.

## Proof

**Step 1 (complete face set).** Represent each edge subset by the integer whose twelve bits mark selected edges in the order above. A mask is admissible if and only if it contains none of the \(24\) triples of edges incident to a common graph vertex. The two independent membership predicates in `verify_octahedral_two_matching.py` agree on all \(2^{12}=4096\) masks. Exactly \(772\) are faces including the empty face. The nonempty face vector, from dimension zero to five, is \((12,66,196,297,180,20)\). Direct containment tests give respectively \(3,60,20\) facets in dimensions \(3,4,5\).

**Step 2 (finite acyclic matching).** On the entire augmented face poset, sequentially toggle each of the twelve edges in the displayed order, pairing an available face \(F\) with \(F\cup\{e\}\) whenever both are still unpaired. This deterministic algorithm produces \(378\) disjoint codimension-one pairs, leaving exactly six critical three-faces and ten critical four-faces. The complete Hasse graph has \(2940\) cover incidences; reverse precisely the matched arrows and topologically sort the directed graph. The sort visits every face, proving acyclicity without sampling. The empty face belongs to a pair, so the corresponding ordinary discrete Morse CW complex has one basepoint and the stated positive-dimensional critical cells.

**Step 3 (signed integral attaching matrix).** Orient every simplex by increasing edge indices. Use the reduced/augmented simplicial boundary, including the signed map from each vertex to the empty simplex. For each acyclic matched pair with unit incidence \(u\in\{1,-1\}\), remove the pair by the exact integral Schur-complement update

\[
\partial'_{ab}=\partial_{ab}-\partial_{a h}\,u^{-1}\partial_{\ell b},
\]

where \(\ell\) and \(h\) are the lower and upper matched faces, respectively. This is standard algebraic discrete-Morse cancellation, preserves the integral chain homotopy type, and computes the integral cellular Morse differential. All \(378\) cancellations have unit pivots. With remaining three-faces ordered by masks \((102,106,166,170,204,3840)\) and remaining four-faces by masks \((1196,1226,1580,1952,2156,2246,2348,2912,3472,3664)\), the only possibly nonzero positive-degree differential, from degree four to three, is

\[
\partial_4=\begin{pmatrix}
0&0&0&0&-1&-1&0&1&0&1\\
0&-1&1&1&1&0&1&0&1&0\\
-1&0&-1&0&0&1&-1&-1&0&-1\\
1&1&0&-1&0&0&0&0&-1&0\\
0&0&0&0&0&0&0&0&0&0\\
0&0&0&0&0&0&0&0&0&0
\end{pmatrix}.
\]

The fourth row is minus the sum of the first three rows; the final two rows vanish. Hence the rank is at most three. The minor in the first three rows and columns indexed \(0,1,4\) has determinant \(+1\), so the rank is at least three and the three nonzero Smith invariant factors are all \(1\). In particular the integral homology is torsion-free and has ranks three in degree three and seven in degree four.

**Step 4 (integral homotopy, not just homology).** The acyclic matching gives a CW complex with one zero-cell, six three-cells and ten four-cells, and no cells of other positive dimensions. Its three-skeleton is \(\bigvee^6 S^3\). Since \(\pi_3(\bigvee^6S^3)\cong\mathbb Z^6\), each four-cell attaching map is determined by its integral degree vector, precisely the columns of \(\partial_4\). A unimodular basis change of the three-spheres and elementary four-cell handle slides put this matrix into the Smith form with three unit entries and seven zero columns. Cancelling the three unit attachments leaves three free three-spheres and seven freely attached four-spheres. This proves the claimed homotopy equivalence, rather than inferring it from Betti numbers alone.

## Verification

The standard-library script `verify_octahedral_two_matching.py` enumerates every face, independently checks the forbidden-triplet characterization, verifies \(\partial^2=0\) over \(\mathbb Z\), performs the full acyclicity check, and independently computes mod-two simplicial ranks. Its exact output is `verify_octahedral_two_matching.out`.

Direct augmented mod-two boundary ranks in dimensions zero through five are \((1,11,55,141,153,20)\); these reproduce reduced Betti numbers \((0,0,0,3,7,0)\). The finite verifier's success marker is `HOMOTOPY_WEDGE_3_S3_AND_7_S4_VERIFIED`. These checks establish the complete finite claim; they are not extrapolated to a parameterized family.

## Relationship to prior work

Vega introduced and studied two-matching homotopy in her work on leaves, clawed graphs, wheels and caterpillars [1]. Singh proved homotopy results for complete graphs and complete bipartite graphs [2]. The octahedral graph is a four-regular complete *tripartite* graph; it is not a graph in those exact classification families. Its ordinary matching complex, the discrete-Morse-vector-field complex, and its unordered two-point graph configuration space are different functors and do not determine the two-matching complex. No comparison establishing that the present exact two-matching result follows from these sources was found.

## Limitations

This is an exhaustive finite classification of one canonical graph, not a structural theorem for arbitrary complete multipartite or four-regular graphs. The evidence does not exclude an equivalent result in a source not inspected or indexed. The signed matrix and the claimed homotopy splitting depend on the stated edge ordering and on exact, rather than floating-point, cancellation. Independent third-party verification has not been performed.

## References

[1] Julianne Vega, *2-Matching Complexes*, arXiv:1909.10406, first posted 2019-09-23, https://arxiv.org/abs/1909.10406 . Relevant scope: introduction, definitions, and graph-family homotopy results.

[2] Anurag Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, first posted 2020-06-24, https://arxiv.org/abs/2006.13632 . Relevant scope: Theorems 1.1 and 1.2 and associated proofs.

[3] Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145. Standard acyclic-matching Morse CW interpretation.
