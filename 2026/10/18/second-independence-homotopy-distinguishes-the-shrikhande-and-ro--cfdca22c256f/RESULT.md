# Second-independence homotopy distinguishes the Shrikhande and rook graphs

## Finding

Let \(S\) be the Shrikhande graph and let \(R=K_4\mathbin{\square}K_4\) be the four-by-four rook graph. Both are strongly regular with parameters \((16,6,2,2)\), but they are not isomorphic. Their second higher-independence complexes have **distinct integral homotopy types**:

\[
\operatorname{Ind}_2(S)\simeq\bigvee^{57} S^3,
\qquad
\operatorname{Ind}_2(R)\simeq\bigvee^{105} S^3.
\]

Thus even among these two canonical cospectral sixteen-vertex graphs, the integral higher-independence homotopy type is not a function of the strongly regular parameters. The statement is about homotopy, not just rational Betti numbers.

## Assumptions and scope

All complexes are finite, abstract simplicial complexes, and all homotopy types refer to their geometric realizations. Use \(V=(\mathbb Z/4\mathbb Z)^2\), encode \((x,y)\) by the integer \(x+4y\) (both coordinates taken in \(\{0,1,2,3\}\)), and declare distinct vertices adjacent exactly when their difference is in the indicated generator set:

\[
D_S=\{(\pm1,0),(0,\pm1),(1,1),(-1,-1)\},
\]
\[
D_R=\{(\pm1,0),(2,0),(0,\pm1),(0,2)\}.
\]

The latter produces a complete graph on each row and on each column, namely \(R\). Each vertex of both graphs has six neighbors; every two distinct vertices have exactly two common neighbors. The graphs are not isomorphic: the six neighbors of each vertex in \(S\) induce a chordless six-cycle, whereas the six neighbors of each vertex in \(R\) induce two disjoint triangles. This follows directly from the displayed generator sets.

For any graph \(G\), the faces of \(\operatorname{Ind}_2(G)\) are vertex subsets \(A\) such that every connected component of the induced graph \(G[A]\) contains at most two vertices. Equivalently, \(G[A]\) has maximum degree at most one. We **do not** mean the usual matching complex on graph edges, or the two-matching complex allowing degree two at original vertices.

## Proof

For each graph, enumerate all \(2^{16}\) vertex masks in increasing integer order and retain exactly those masks whose induced graph has maximum degree at most one. A second implementation examines the connected components of each induced graph and checks their orders. The two predicates agree on every mask. Including the empty face, this gives exactly \(1337\) faces for \(S\) and \(1193\) for \(R\). The respective nonempty face vectors by dimensions \(0,1,\dots\) are

\[
(16,120,384,544,240,32)\quad\text{and}\quad(16,120,384,528,144).
\]

Now construct a partial matching on the **nonempty** face poset by a sequence of element matchings. Initially every nonempty face is unmatched. At each pivot vertex \(v\) in the prescribed sequence, pair every as-yet-unmatched face \(\sigma\) omitting \(v\) with \(\sigma\cup\{v\}\), provided the latter is also as-yet-unmatched. Once paired, faces are removed from further matching; the choice of increasing face order does not change the pairs within one pivot.

For \(S\), the pivot sequence (vertices encoded as above) is

`(3,10,5,7,13,0,1,8,4,9,11,14,6,12,15,2)`.

For \(R\), use

`(2,0,12,1,15,7,9,3,8,4,13,6,10,14,11,5)`.

These rules produce exactly \(639\) matched pairs and critical-cell counts \((1,0,0,57,0,0)\) for \(S\); they produce \(543\) pairs and counts \((1,0,0,105,0)\) for \(R\). The partial matchings are *acyclic*: orient each matched codimension-one incidence upward and every unmatched one downward. The supplied exact checker constructs the entire directed Hasse graph and performs a complete topological sorting. It visits all \(1336\) nonempty faces through \(4960\) incidences for \(S\), and all \(1192\) through \(4224\) incidences for \(R\), without a directed cycle.

Discrete Morse theory therefore supplies for each complex a CW model with exactly one zero-cell, no positive-dimensional cells except the indicated number of three-cells, and no cells of higher dimension. Since every attaching map of a three-cell to a point is constant, these CW models are wedges of exactly \(57\) and \(105\) three-spheres. This proves the asserted *integral homotopy* classifications. No unverified attaching-degree or torsion assumption is needed.

## Verification

The self-contained Python standard-library program `shr_rook_pair_certificate.py` exhaustively verifies graph adjacency, the two independent face predicates for every mask, the complete face vectors, all matching pairs and critical dimensions, and directed acyclicity of the entire matched Hasse diagrams. An independent mod-two simplicial boundary computation produces the ranks

\[
(15,105,279,208,32)\quad\text{for }S,
\qquad(15,105,279,144)\quad\text{for }R,
\]

in degrees beginning at one. The resulting mod-two reduced homology occurs only in degree three, with respective ranks \(57\) and \(105\), consistent with—but not replacing—the integral discrete-Morse proof. The recorded standard output is embedded as `certificate_output.txt`.

## Relationship to prior work

Deshpande and Singh (first public version January 15, 2020) defined and systematically studied higher-independence homotopy, establishing formulas for complete multipartite graphs, whiskered graphs, paths, cycles, and certain rooted trees. Abdelmalek and collaborators subsequently studied shellability and vertex decomposability of such complexes on chordal graphs and trees. Neither graph here is chordal (their indicated Cayley graphs contain induced four-cycles), and neither is one of those computed families.

Previously reported homotopy classifications of the *ordinary*, first independence complexes of \(S\) and \(R\) do not imply the claimed second-independence types. A two-matching complex of \(K_{4,4}\) is also a different object: its faces choose graph edges with original vertex degrees at most two, whereas \(\operatorname{Ind}_2(R)\) selects rook-graph vertices with induced maximum degree at most one. Likewise, the Lovász neighborhood and intrinsic Čech complexes of the same graphs have different face predicates. The result here is specifically the paired second-independence classification.

## Limitations

The theorem is restricted to this canonical pair, not to all strongly regular graphs or higher thresholds. Its verification is an exhaustive finite proof, not an infinite-family enumeration. No assertion is made about equivariant homotopy types or maps between successive higher-independence stages. Published or otherwise unindexed equivalent work remains an originality risk; no independent mathematical audit has been performed.

## References

1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448 (initial public version 2020-01-15), https://arxiv.org/abs/2001.05448. Definitions, discrete-Morse tools and exact graph-family theorems.
2. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863 (initial public version 2021-06-21), https://arxiv.org/abs/2106.10863.
3. A. E. Brouwer and H. Van Maldeghem, *Strongly Regular Graphs*, Section on the Shrikhande graph and lattice graph \(H(2,4)\), https://homepages.cwi.nl/~aeb/math/srg/rk3/srgw.pdf.
4. Published comparison record, *Independence complexes of the Shrikhande and \(4\times4\) rook graphs have different sphere-wedge homotopy types*, limited to the ordinary first independence stage (identified through published research records).
