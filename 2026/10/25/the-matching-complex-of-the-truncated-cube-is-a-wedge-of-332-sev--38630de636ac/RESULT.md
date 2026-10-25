# The matching complex of the truncated cube is a wedge of 332 seven-spheres

## Finding
Let \(T\) denote the ordinary 24-vertex, 36-edge truncated cubical graph, and let \(\mathcal M(T)\) be its simplicial matching complex. There is an integral homotopy equivalence
\[
\mathcal M(T)\simeq\bigvee^{332}S^7.
\]
Consequently \(\widetilde H_7(\mathcal M(T);\mathbb Z)\cong\mathbb Z^{332}\), and \(\widetilde H_i(\mathcal M(T);\mathbb Z)=0\) for every \(i\ne7\). This is a statement about the full homotopy type, not just rational Betti numbers.

## Assumptions and scope
Construct \(T\) without a drawing. Its vertices are \((v,i)\), where \(v\in\{0,1\}^3\) and \(i\in\{0,1,2\}\). For each fixed \(v\), connect the three vertices \((v,0),(v,1),(v,2)\) into a triangle. For each cube edge in coordinate \(i\), connect \((v,i)\) to \((v\oplus e_i,i)\), taking the copy with the \(i\)-th bit of \(v\) zero to avoid duplication. Here \(\oplus\) is bitwise addition modulo two. This is the graph of a cube with its eight vertices truncated, also called the three-dimensional cube-connected-cycles graph. It has 24 vertices, 36 edges, and eight triangular faces.

The vertices of \(\mathcal M(T)\) are the 36 graph edges; a subset is a simplex precisely when those graph edges are pairwise vertex-disjoint. A matching with \(k\) edges is a simplex of dimension \(k-1\); the empty matching is not a vertex of the nonempty-face poset. All conclusions concern this unique finite graph, not an asserted infinite family.

For exact reproduction, order the graph edges as follows: first, for \(v=0,\ldots,7\) in ascending binary order, list its three triangle edges with coordinate pairs \((0,1),(0,2),(1,2)\); next, for \(v=0,\ldots,7\) and \(i=0,1,2\), list the cube-edge connection when bit \(i\) of \(v\) is zero. Label these edges \(0,\ldots,35\) in that order.

## Proof
**1. Exhaustive face construction.** Let \(C_j\) be the set of graph-edge indices incident to either endpoint of edge \(j\). Generate all nonempty masks recursively: from an increasing list of chosen edge indices, append any larger \(j\) not in the union of the corresponding \(C_j\). Every matching appears exactly once because its indices have a unique increasing order. The numbers of matchings of sizes \(1\) through \(12\) are
\[
(36,558,4876,26421,92016,206676,292872,249420,117600,26928,2304,32).
\]
Their sum is \(1{,}019{,}739\); in particular, there are 32 perfect matchings and no matching larger than 12 edges. The face vector gives Euler characteristic \(-331\) and reduced Euler characteristic \(-332\).

**2. An explicit acyclic matching on the face poset.** Initially mark every nonempty face unpaired. For each graph-edge index \(j=0,\ldots,35\), pair any currently unpaired face \(F\) not containing \(j\) with \(F\cup\{j\}\), provided the latter is a valid and currently unpaired face. Each stage pairs faces of consecutive dimensions, and no face can be used twice. The checker constructs all pairs directly, yielding \(509{,}667\) pairs and precisely 405 unpaired faces: one vertex (dimension zero), 368 cells of dimension seven, and 36 cells of dimension eight. There are no other critical faces.

To certify acyclicity, orient every covering relation \(\sigma\supset\tau\) of the nonempty face poset downward, except relations in the matching, which are oriented upward. The full face poset has \(7{,}220{,}436\) covering incidences. A topological sort of this directed graph visits all \(1{,}019{,}739\) faces; hence the matching is acyclic. Forman's discrete Morse theorem yields a CW complex with one zero-cell, 368 seven-cells, 36 eight-cells, and no other cells, homotopy equivalent to \(\mathcal M(T)\).

**3. Its exact integral cellular differential.** Orient each simplex by ascending graph-edge indices. For an upper face \(\sigma\) and a codimension-one face \(\tau=\sigma\setminus\{j\}\), write \([\sigma:\tau]=(-1)^{\#\{i\in\sigma:i<j\}}\). The Morse differential between critical dimensions eight and seven is calculated by exact signed gradient-path elimination. On seven-faces, define the reduction \(R\): a critical face is sent to its basis vector; a face paired downward with a six-face contributes zero; and when a seven-face \(\tau\) is paired upward with an eight-face \(\sigma\), use
\[
R(\tau)=-[\sigma:\tau]\sum_{\substack{\tau'\subset\sigma,\;|\tau'|=8\\\tau'\ne\tau}}[\sigma:\tau']R(\tau').
\]
Acyclicity guarantees termination. Applying this reduction to the ordinary oriented boundary of each of the 36 critical eight-faces gives an integral \(368\)-by-\(36\) Morse differential matrix with exactly 698 nonzero coefficients, each \(+1\) or \(-1\). An independent forward propagation through the complete directed Hasse topological order reproduces every one of the matrix's 13,248 entries.

Exact integer row and column operations find 36 successive unit pivots. Row elimination beneath each pivot is performed over \(\mathbb Z\) with no division other than by a unit; the absolute values of the intermediate entries never exceed two. Thus all 36 nonzero Smith invariant factors equal one. In particular, the differential is injective and has primitive image of rank 36.

**4. Promotion from homology to homotopy.** The Morse CW complex has only a base zero-cell, 368 seven-cells, and 36 eight-cells. Its seven-skeleton is \(\bigvee^{368}S^7\), which is six-connected, so its \(\pi_7\) is identified by Hurewicz with \(\mathbb Z^{368}\). Therefore the attaching maps of the eight-cells are classified by their integer degree vectors, namely by the preceding Morse matrix. Integral unit row and column operations correspond to changing the bases of seven-spheres and eight-cell attaching maps up to homotopy. Since its Smith form has 36 ones and no other nonzero entries, the 36 eight-cells cancel 36 of the seven-spheres and the remaining complex is \(\bigvee^{332}S^7\), as claimed.

## Verification
Compile the accompanying source `truncated_cube_verifier.cpp` with `g++ -O3 -std=c++17 truncated_cube_verifier.cpp -o check` and execute `./check`. It builds the graph and all faces from their definitions; verifies graph size, degrees, triangles, the entire face vector, all matching pairs, all Hasse incidences and acyclicity; calculates the Morse boundary in two independently organized ways; and checks 36 integral unit pivots. Success ends with `VERIFY_OK`. The computation is exact integer arithmetic, not a floating-point or bounded Monte Carlo experiment. The program requires a compiler supporting GCC-compatible builtins and signed 128-bit temporaries.

## Relationship to prior work
Knill's 2012 paper explicitly discusses the truncated cube's 24-vertex, 36-edge graph and computes the Euler characteristic of the **graph's clique complex**. That clique complex is not \(\mathcal M(T)=\operatorname{Ind}(L(T))\), the independence complex of the 36-vertex line graph. Taylan's 2015 study develops matching-tree methods for simplicial complexes but addresses families of devoid and dominance complexes, not this explicit matching-complex homotopy calculation. Bayer, Jelić Milutinović and Vega's theorem classifies the **general form** of matching complexes of outerplanar graphs; it does not apply here because the truncated cubical graph is cubic and hence not outerplanar (every nonempty outerplanar graph has a vertex of degree at most two). Published work on the ordinary vertex-independence complex of this graph, the matching complexes of the cube or truncated tetrahedron, and geometric graph complexes of related solids concerns distinct simplicial complexes and does not determine this rank-332 seven-dimensional wedge. The possibility of an unindexed equivalent calculation is retained as an originality risk.

## Limitations
The finding applies to the specified finite truncated cubical graph alone; it does not classify matching complexes for all Archimedean graphs or cube-connected-cycles networks. Its exhaustive proof depends on transparent finite enumeration and a complete algebraic Morse certificate rather than a closed-form formula for a graph family. The 2006 work on Archimedean Schlegel graphs was only accessible at abstract level for this comparison. Independent scientific audit has not been performed.

## References
1. O. Knill, *The theorems of Green–Stokes, Gauss–Bonnet and Poincaré–Hopf in graph theory*, arXiv:1201.6049v1, publicly posted 2012-01-29, https://arxiv.org/abs/1201.6049.
2. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, publicly posted 2015-01-27, https://arxiv.org/abs/1501.06754.
3. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, first posted 2024-11-07, https://arxiv.org/abs/2411.04601.
4. S. M. Rajtmajer et al., *On the complexity of Archimedean solids*, Journal of Mathematical Chemistry 39 (2006), 119–132, DOI:10.1007/s10910-005-9008-2 (month-level date only in accessed bibliographic metadata).
5. E. W. Weisstein, *Truncated Cubical Graph*, MathWorld, https://mathworld.wolfram.com/TruncatedCubicalGraph.html (graph-identification reference, not a matching-homology result).
