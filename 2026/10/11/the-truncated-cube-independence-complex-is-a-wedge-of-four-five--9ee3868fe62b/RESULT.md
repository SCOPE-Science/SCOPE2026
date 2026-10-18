# The truncated-cube independence complex is a wedge of four five-spheres and eleven six-spheres

## Finding

For the graph \(G\) of the regular truncated cube, the ordinary independence complex \(K=\operatorname{Ind}(G)\) has the integral homotopy type
\[
K\simeq\bigvee^{4}S^{5}\vee\bigvee^{11}S^{6}.
\]
In particular \(\widetilde H_5(K;\mathbb Z)\cong\mathbb Z^{4}\), \(\widetilde H_6(K;\mathbb Z)\cong\mathbb Z^{11}\), and the other reduced integral homology groups are zero. This is a homotopy classification, not only a computation of Betti numbers.

## Assumptions and scope

The graph is completely specified as follows. Number the binary triples by \(b\in\{0,1,\ldots,7\}\), with their three coordinate bits indexed \(i\in\{0,1,2\}\). Vertex \(3b+i\) is the dart at cube corner \(b\) pointing along coordinate axis \(i\). There are two kinds of undirected graph edges:

- \(\{3b+i,3b+j\}\) for each fixed \(b\) and \(0\le i<j\le2\);
- \(\{3b+i,3(b\mathbin{\mathrm{xor}}2^i)+i\}\) for every \(b\) and \(i\), counted only once as undirected edges.

Here \(\mathrm{xor}\) denotes binary exclusive-or. Equivalently, place the dart \((b,i)\) at the Euclidean point whose \(i\)-th coordinate has signed magnitude \(1\) and whose other coordinates have signed magnitude \(1+\sqrt2\), with signs determined by \(b\). The graph's edges are exactly the pairs at Euclidean distance \(2\). Its \(24\) vertices and \(36\) edges form the truncated-cube (truncated-hexahedron) skeleton, with eight triangular and six octagonal faces. Only this precise finite graph is asserted, not a family of truncations.

A simplex of \(K\) is any nonempty subset of the 24 graph vertices containing no adjacent pair; the empty face is used only in the combinatorial enumeration. The maximal simplex dimension is \(7\).

## Proof

**Complete face enumeration.** For vertex bit masks \(s\in\{0,\ldots,2^{24}-1\}\), let \(A_v\) be the bit mask of neighbors of vertex \(v\). Starting from the empty mask, recursively adjoin each vertex \(v\) greater than the last chosen vertex exactly when \(s\mathbin{\&}A_v=0\). Every independent set occurs exactly once. The resulting face vector in dimensions \(0,\ldots,7\) is
\[
(24,240,1296,4092,7632,8056,4272,828),
\]
so exactly \(26440\) nonempty simplices occur.

**An acyclic matching.** At each index \(v=0,1,\ldots,23\), pair every currently unpaired independent set not containing \(v\) with its extension by \(v\), provided both are still present. Delete all those pairs, then proceed to the next index. First carry out this process on the augmented face set including the empty mask; subsequently unpair the empty mask and its singleton partner and omit the empty mask from the ordinary face poset. This leaves exactly \(13211\) matched pairs and the following critical cells: one vertex, five 5-simplices represented by decimal masks
\[
608392,\ 2237698,\ 5251618,\ 8945828,\ 8945940,
\]
and twelve 6-simplices represented by
\[
4752676,\ 4753700,\ 5391496,\ 5392520,\ 8946980,\ 9061512,\ 9061634,\ 9519650,\ 9520264,\ 9576980,\ 9577604,\ 9585800.
\]
All other nonempty cells are matched. These lists, and every pair, are reconstructed by `verify_morse.py`.

Orient each cover incidence in the ordinary face poset downward except matched incidences, which point upward. There are exactly \(143760\) directed incidences. The supplied program performs a complete topological sort visiting all \(26440\) nonempty faces; hence the directed graph is acyclic and the discrete-Morse matching is valid. The resulting CW complex has one 0-cell, five 5-cells and twelve 6-cells, with no cells in other positive dimensions.

**Integral attaching degrees.** Give each simplex the orientation from increasing vertex indices. If deleting vertex \(v\) from face \(t\) gives face \(s\), the signed incidence is \((-1)^{\#\{w\in t:w<v\}}\). For each five-dimensional face paired upward to a six-dimensional face, eliminate the corresponding unit signed incidence by the usual gradient-path recursion. The resulting integral cellular boundary \(D=\partial^M_6\) is a \(5\)-by-\(12\) matrix: all entries vanish except, with 1-based row/column indices,
\[
D_{4,5}=D_{4,6}=D_{5,5}=D_{5,6}=-1,\qquad D_{4,9}=D_{5,9}=1.
\]
The two nonzero rows are identical; hence \(D\) has rank \(1\), and \(D_{4,5}=-1\) is a maximal unimodular minor. Its Smith normal form has one invariant factor \(1\) and no other nonzero entries.

The CW five-skeleton is \(\bigvee^5 S^5\). By the Hurewicz isomorphism, an attaching map of a six-cell into this skeleton is determined by its integral vector of degrees, since \(\pi_5(\bigvee^5 S^5)\cong\mathbb Z^5\). Integer changes of bases and cancellation of the unit attaching degree split off one 5/6 cell pair. The remaining four five-cells and eleven six-cells attach trivially, proving
\[
K\simeq\bigvee^4 S^5\vee\bigvee^{11}S^6.
\]

## Verification

`verify_morse.py` requires only Python 3 standard-library modules. It constructs the cube-dart graph, exhaustively enumerates all faces, builds the greedy matching, checks every oriented Hasse incidence for acyclicity, computes the exact signed Morse differential via recursive gradient paths and asserts the displayed full matrix.

`verify_independent.py` independently constructs the graph from exact coordinates in \(\mathbb Z[\sqrt2]\) by testing Euclidean squared distance equal to \(4\), uses a separate doubling algorithm to generate the entire complex, and computes simplicial boundary ranks over \(\mathbb F_2\). For dimensions \(1\) through \(7\), these ranks are \((23,217,1079,3013,4619,3433,828)\), giving reduced Betti numbers \((0,0,0,0,0,4,11,0)\) in degrees \(0\) through \(7\). The mod-two calculation is a cross-check and does not replace the integral Morse-boundary certificate.

Both programs were executed directly with Python 3 and completed all assertions. Regenerate their results by running `python3 verify_morse.py` and `python3 verify_independent.py` in a directory containing both files; neither program needs network access, external packages or supporting datasets.

## Relationship to prior work

Barmak's *Star clusters in independence complexes of graphs* [1], Sections 3 and 5, proves general suspension and connectivity statements; it does not evaluate this truncated-cube complex. Every vertex of \(G\) lies on a triangle, so the triangle-free suspension criterion does not apply. The claw-free connectivity bound is much weaker than a complete mixed-dimensional homotopy classification.

Goyal, Shukla and Singh [2] classify other families, including products of complete graphs, generalized Mycielskians and certain local graph modifications. Their results do not provide this graph's two exact sphere multiplicities.

A separately published computation of the truncated-cube graph's scale-three Vietoris–Rips complex concerns another simplicial complex: Vietoris–Rips at scale three includes a graph edge, while \(\operatorname{Ind}(G)\) excludes it. Conversely, the independent vertex pair labeled \(0,21\), whose graph distance is \(6\), does not form a scale-three Rips edge. Thus neither complex contains the other, and that homotopy classification does not imply the present result. Known polyhedral matching-complex and independence-complex computations on other graphs likewise do not determine this one.

## Limitations

The claim is for the ordinary, unweighted independence complex of this 24-vertex truncated-cube graph only. The certificate does not establish a formula for all Archimedean solids, all cubic planar graphs, or higher-dimensional truncated cubes. Literature searches are not guarantees of priority; an equivalent unindexed calculation remains possible. The result has undergone self-review; no independent scientific audit has been performed.

## References

1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (first submitted 2010-07-02), Sections 3 and 5; primary MSC 57M15. https://arxiv.org/abs/1007.0418
2. S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926v1 (2019), Sections 3–5. https://arxiv.org/abs/1905.06926
3. *A mixed-dimensional Rips wedge for the truncated cube*, public research-record identifier `2026/10/4/SCOPE-a-mixed-dimensional-rips-wedge-for-the-truncated-cube--4fae71a21a80` (scale-three graph-metric Vietoris–Rips complex, a different invariant).
