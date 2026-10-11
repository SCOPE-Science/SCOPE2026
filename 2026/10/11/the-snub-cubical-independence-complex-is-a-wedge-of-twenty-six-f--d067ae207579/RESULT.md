# The snub cubical independence complex is a wedge of twenty-six four-spheres

## Finding
Let \(G\) be the edge graph of the snub cube, also called the snub cuboctahedron, with its 24 vertices and 60 edges. Its ordinary independence complex satisfies the integral homotopy equivalence
\[
\operatorname{Ind}(G)\simeq\bigvee^{26}S^4.
\]
The conclusion identifies the homotopy type, not just the ranks of homology groups. In particular, the complex is three-connected, with \(\pi_4\cong\mathbb Z^{26}\), and its reduced integral homology is nonzero only in degree four.

## Assumptions and scope
The graph is finite, undirected, and loopless. Its construction can be specified without a graph database. Let \(t>1\) denote the unique real root of \(t^3=t^2+t+1\), and set \(b=(1,t^{-1},t)\). For each permutation \(p\) of three positions and signs \(\epsilon_i\in\{-1,1\}\), include the point \((\epsilon_0b_{p(0)},\epsilon_1b_{p(1)},\epsilon_2b_{p(2)})\) precisely when the parity of the number of positive signs equals the parity of \(p\). This gives 24 distinct points. Join a pair precisely when its squared Euclidean distance is \(2+4t-2t^2\). These are the standard Cartesian coordinates and edge length of one chirality of the snub cube; choosing the opposite chirality produces an isomorphic edge graph.

Write \(K=\operatorname{Ind}(G)\) for the abstract simplicial complex of all independent vertex subsets of \(G\), including the empty face. The homotopy statement concerns the geometric realization of \(K\). The labelled vertices are ordered by the lexicographic iteration of permutations of positions followed by sign triples with \(-1\) before \(+1\), retaining the sign-parity condition.

## Proof
**Exact graph construction.** Computation in the cubic integer ring \(\mathbb Z[t]/(t^3-t^2-t-1)\) uses the identity \(t^{-1}=t^2-t-1\). Each squared intervertex distance is therefore represented exactly by three integer coefficients of \(1,t,t^2\). Comparing these coefficients with \((2,4,-2)\) produces exactly 60 edges; every vertex has degree five. The graph also has 32 triangles. The complete edge set is determined by the preceding formula and reproduced by `verify_homotopy.py`.

**Face enumeration.** Recursively append vertices in increasing order, rejecting an append exactly when the new vertex is adjacent to a previously selected vertex. This produces exactly 5,301 nonempty faces, with dimensions zero through seven having counts
\[
(24,216,912,1854,1680,564,48,3).
\]

**Acyclic matching.** On the poset of nonempty faces, process graph vertices in increasing order of \((13v+22)\bmod24\), where \(v=0,\ldots,23\). At the stage for vertex \(v\), pair every still-unpaired face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), whenever both faces remain unpaired. This is a precise deterministic partial matching, containing 2,628 distinct pairs. Orient each covering relation between faces upward if matched and downward otherwise. The full directed Hasse graph has 5,301 vertices and 22,728 incidences; an exhaustive topological sort visits all 5,301 vertices, establishing acyclicity. The unpaired faces are one zero-simplex, nine three-simplices, and 35 four-simplices. Forman's discrete Morse theorem thus gives a homotopy-equivalent CW complex with those critical cell counts and no others.

**Integral attaching degrees.** The signed Morse boundary from critical four-cells to critical three-cells is a \(9\times35\) integer matrix \(D\). Orient each simplicial face by increasing vertex labels. For a matched pair \((\tau,\eta)\), the coefficient of \(\tau\) in \(\partial\eta\) is \(\pm1\), so eliminating \(\tau\) from \(\partial\eta\) by integer elementary chain cancellation gives an exact recursive formula for all columns of \(D\). The file `verify_homotopy.py` implements this signed elimination directly from the acyclic matching. The nine columns with zero-based indices
\[
(7,19,20,26,28,1,18,29,10)
\]
form a square submatrix of determinant \(-1\). Hence the map \(D:\mathbb Z^{35}\to\mathbb Z^9\) is split-surjective, with 26-dimensional free kernel and no torsion cokernel.

The Morse CW complex has one zero-cell and nine three-cells, so its three-skeleton is \(\bigvee^9 S^3\). Its fourth-cell attaching maps lie in \(\pi_3(\bigvee^9S^3)\cong\mathbb Z^9\), where the homotopy class of each attaching map is completely determined by its signed cellular boundary column. The unimodular minor provides nine invertible attaching directions; cellular basis changes cancel these nine three/four-cell pairs, while the 26 remaining four-cells attach trivially. The resulting homotopy type is \(\bigvee^{26}S^4\), as claimed.

## Verification
Run `python3 verify_homotopy.py` using only the Python standard library. It reconstructs the exact graph from the cubic ring, enumerates all faces, reproduces the 2,628 Morse pairs, verifies acyclicity by a complete directed-Hasse topological sort, calculates the signed Morse boundary, and obtains the determinant \(-1\) for the specified integer minor.

Run `python3 verify_independent.py` separately. It rebuilds the geometry using high-precision decimal arithmetic and a different include/exclude enumeration, then computes all simplicial boundary ranks over \(\mathbb F_2\) by bit-column elimination. It obtains ranks \((23,193,719,1135,519,45,3)\) and unreduced Betti numbers \((1,0,0,0,26,0,0,0)\). This field calculation independently checks the combinatorics and ranks but does not by itself certify the integral homotopy conclusion; the acyclic matching and unimodular signed minor do that.

## Relationship to prior work
Barmak's *Star clusters in independence complexes of graphs* (arXiv:1007.0418v1, first public posting July 2, 2010) supplies general topological and connectivity methods but no exact snub-cube homotopy classification. Its claw-free matching-complex connectivity discussion does not imply the present result; this snub-cube graph has induced claws (for example, the labelled center 0 and leaves 9, 10, 16).

Goyal, Shukla and Singh's *Homotopy Type of Independence Complexes of Certain Families of Graphs* (arXiv:1905.06926v1) provides a rigorous staged vertex-toggle acyclic matching method, together with results for categorical products of complete graphs, generalized Mycielskian graphs, and specified local graph modifications. Its listed homotopy classifications do not include the snub cube or imply its exact degree matrix. Here the staged matching is a known technique; the specific complex, integral boundary calculation, and homotopy classification are the content of the finding.

The snub cubical graph is a canonical 24-vertex chiral Archimedean graph, unlike the other 24-vertex Archimedean graphs of smaller valence. Its independence complex has dimension seven but collapses in the homotopy sense to a wedge concentrated in dimension four. This describes a natural, finite, otherwise non-obvious topological invariant of the chiral polyhedral graph.

## Limitations
The theorem concerns only the snub cubical graph; it gives no uniform statement for all Archimedean solids or their higher-dimensional analogues. The computations are exhaustive over the 5,301 faces of this finite complex, not an extrapolation from sampled complexes. Mod-two homology alone would not determine the integral homotopy type. No independent external audit has been performed, and an equivalent result in unindexed literature cannot be excluded merely from unsuccessful searches.

## References
- J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (2010), https://arxiv.org/html/1007.0418v1.
- S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926v1 (2019), https://arxiv.org/html/1905.06926v1.
- E. W. Weisstein, *Snub Cubical Graph*, MathWorld, https://mathworld.wolfram.com/SnubCubicalGraph.html.
- *Snub cube*, Cartesian coordinates and chirality construction, https://en.wikipedia.org/wiki/Snub_cube.
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
