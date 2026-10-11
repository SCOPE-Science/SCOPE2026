# The total \(3\)-cut complex of the \(4\)-cube: a \(129\)-sphere wedge and its hyperoctahedral character
## Finding
Let \(Q_4\) be the graph with vertex set \(\{0,1\}^4\), with adjacent vertices differing in exactly one binary coordinate. Let \(X=\Delta_3^t(Q_4)\) be the simplicial complex on its sixteen vertices whose facets are the complements of independent three-vertex sets. Then
\[
X\simeq\bigvee^{129}S^{10},\qquad
\widetilde H_j(X;\mathbb Z)=
\begin{cases}
\mathbb Z^{129},&j=10,\\
0,&j\ne10.
\end{cases}
\]
The complex is pure of dimension \(12\) and is not shellable.

Under the natural action of \(B_4=(C_2)^4\rtimes S_4\), the rational homology \(\widetilde H_{10}(X;\mathbb Q)\) has the character in the following table. Each group element is a coordinate permutation followed by coordinate bit-flips. The two cycle lists give the lengths of cycles in the coordinate permutation with respectively even and odd total flip parity. A dash denotes an empty list. These twenty rows exhaust the conjugacy classes of \(B_4\).

| Positive coordinate cycles | Negative coordinate cycles | Class size | Trace |
|:--|:--|--:|--:|
| - | 1,1,1,1 | 1 | 9 |
| - | 2,1,1 | 12 | 1 |
| - | 2,2 | 12 | 1 |
| - | 3,1 | 32 | 0 |
| - | 4 | 48 | 1 |
| 1 | 1,1,1 | 4 | 9 |
| 1 | 2,1 | 24 | 1 |
| 1 | 3 | 32 | 0 |
| 1,1 | 1,1 | 6 | 5 |
| 1,1 | 2 | 12 | -3 |
| 1,1,1 | 1 | 4 | 21 |
| 1,1,1,1 | - | 1 | 129 |
| 2 | 1,1 | 12 | 7 |
| 2 | 2 | 24 | -1 |
| 2,1 | 1 | 24 | 11 |
| 2,1,1 | - | 12 | 3 |
| 2,2 | - | 12 | 9 |
| 3 | 1 | 32 | 0 |
| 3,1 | - | 32 | 0 |
| 4 | - | 48 | -1 |

## Assumptions and scope
The graph and complex are finite and unweighted. Label the cube vertices by integers \(0,1,\ldots,15\) in binary; \(a\) and \(b\) are adjacent precisely if the binary expansion of \(a\oplus b\) contains exactly one nonzero bit. An independent triple contains no adjacent pair. By definition, a set \(\sigma\) belongs to \(X\) if and only if its complement contains an independent triple. This is the total cut convention, not the ordinary cut convention that uses arbitrary disconnected induced triples. The theorem concerns the four-dimensional hypercube alone, not all dimensions.

The full automorphism group has order \(16\cdot24=384\): an automorphism sends the zero vertex to an arbitrary vertex and permutes its four neighbors, and these data determine the automorphism. The representation table is a rational character, not a distinguished integral module basis.

## Proof
**Reconstruction.** There are \(32\) edges. Exhaustive evaluation of the \(\binom{16}{3}=560\) triples shows that exactly \(208\) are independent. Their complements are distinct facets of size \(13\). Closing these facets under taking subsets yields exactly \(64,670\) nonempty faces with dimension-wise face vector
\[
(f_0,f_1,\ldots,f_{12})=
(16,120,560,1820,4368,8008,11440,12870,11440,8008,4368,1444,208).
\]
This reconstruction, including all subfaces, is implemented without a precomputed facet table in the attached standard-library program.

**Acyclic matching.** Initially mark every nonempty face as available. Process vertex labels \(v=0,1,\ldots,15\) in order. At stage \(v\), for each available face \(\sigma\) not containing \(v\), match it with \(\sigma\cup\{v\}\) if that face is also available; remove both faces from availability. Processing available masks in ascending order specifies a deterministic matching, though pair order within each stage does not affect the result. Stagewise matching-pair counts are
\[
(32078,84,40,36,10,10,6,6,0,0,0,0,0,0,0,0).
\]
Thus there are \(32,270\) matched pairs and exactly \(130\) unmatched nonempty faces: one vertex and \(129\) ten-simplices. A matching is not accepted solely because the algorithm produces these counts. Orient every covering relation in the nonempty face poset from the larger to the smaller face, except that every matched cover is reversed. The verifier constructs all \(513,248\) covering relations and runs a complete topological-sort test on the resulting directed graph of \(64,670\) faces; all \(64,670\) are removed, proving that the matching has no directed cycle. Forman's discrete Morse theorem now gives a CW model with one zero-cell, \(129\) ten-cells and no other cells. Because every ten-cell attaches to the single zero-cell, the model is a wedge of \(129\) ten-spheres.

**Independent numerical check.** The combinatorial Alexander dual \(L=X^\vee\) consists precisely of the subsets of cube vertices with independence number at most two. The cube is bipartite, so such a subset has at most two vertices from each bipartition class and hence at most four vertices. Direct low-dimensional enumeration gives \((f_0,f_1,f_2,f_3)=(16,120,352,376)\). Independently, the count of edge-containing triples is
\[
32(16-2)-16\binom42=352,
\]
and the count of four-vertex subsets admitting a perfect matching is
\[
\binom{32}{2}-16\binom42-24=376,
\]
where the last subtraction accounts for the twenty-four four-cycles, each providing two perfect matchings. Its reduced Euler characteristic is
\[
-1+16-120+352-376=-129,
\]
consistent with \(\widetilde H_3(L)\cong\mathbb Z^{129}\) by Alexander duality and the preceding Morse computation. This count alone would not establish the homotopy type; the acyclic matching does.

**Equivariant character.** For each group element \(g\), the Hopf trace formula and the homology concentration above give
\[
\operatorname{tr}(g\mid\widetilde H_{10}(X;\mathbb Q))=
\sum_{\substack{\emptyset\ne\sigma\in X\\g\sigma=\sigma}}
(-1)^{\dim\sigma}\operatorname{sgn}(g\mid\sigma)-1.
\]
An invariant face is a union of orbits of the vertex permutation. If it uses \(r\) orbits, its summand is \((-1)^{r+1}\), regardless of orbit lengths. Accordingly the expression is an exact finite alternating sum over orbit unions that are faces of \(X\). The verifier enumerates all \(384\) signed coordinate permutations, computes these sums and groups the results by the signed cycle partitions. Each of the twenty classes has one constant trace; their sizes sum to \(384\). As a separate check, every coordinate flip and coordinate transposition induces an even permutation of the sixteen cube vertices, so the equivariant combinatorial Alexander-duality formula has no sign twist. The program recomputes every trace as \(\sum_{\sigma\in L,\ g\sigma=\sigma}(-1)^{r(\sigma)}\) and obtains the identical result for all \(384\) elements. Thus the displayed table gives the complete rational character.

Because \(X\) has dimension \(12\), a pure shelling would force reduced homology to be concentrated in dimension \(12\). The nonzero degree-ten group therefore excludes shellability.

## Verification
Run `python3 artifacts/verify.py` from the extracted package. It needs Python's standard library only and outputs `VERIFY_OK` after exhaustive tests. The script regenerates every graph edge, independent triple, facet and nonempty face; builds a complete directed Hasse graph and checks its acyclicity by topological sorting; computes the independent Alexander-dual counts and four-cycle formula; and independently calculates the full \(384\)-element character in two ways. The outputs are deterministic for the fixed binary vertex labels. The checker validates this finite complex exhaustively, not an infinite family. It does not provide an independent human audit.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced total cut complexes and gave homotopy formulas for complete bipartite graphs, cycles, prisms over cliques, chordal graphs and certain rectangular grid complexes [1]. The four-dimensional hypercube is not complete bipartite or chordal, and it is not a rectangular planar grid graph; as a graph it may also be viewed as \(C_4\square C_4\). The results inspected in [1] do not imply the displayed rank or character. Chandrakar, Hazra, Rout and Singh [2] treat rectangular \(2\)-row and \(3\)-row grids, not the four-cube. The related cut-complex studies [3,4] concern the ordinary cut complex, which has different facets for this parameter. The homotopy and equivariant results here use neither a claimed general hypercube classification nor any extension from a smaller cube.

## Limitations
The argument is an exact finite combinatorial computation for \(Q_4\). It proves the integral homotopy type and a rational character but does not furnish a canonical equivariant geometric basis, an explicit decomposition into irreducible rational representations, or a result uniform in hypercube dimension. Comprehensive searches cannot rule out uncatalogued equivalent calculations. No independently performed audit is asserted.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503 (first public 2022-09-27); *Discrete & Computational Geometry*, DOI:10.1007/s00454-024-00630-4.
2. H. Chandrakar, N. R. Hazra, D. Rout, and A. Singh, *Topology of Total Cut Complexes and Cut Complexes of Grid Graphs*, arXiv:2408.07646 (2024-08-14).
3. M. Bayer et al., *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (2023-04-26), DOI:10.1137/23M1569034.
4. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (2024-07-11).
5. R. Forman, *Morse Theory for Cell Complexes*, *Advances in Mathematics* 134 (1998), 90–145.
