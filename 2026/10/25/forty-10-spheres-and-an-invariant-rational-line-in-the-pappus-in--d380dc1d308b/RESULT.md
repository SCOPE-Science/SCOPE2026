# Forty \(10\)-spheres and an invariant rational line in the Pappus induced-forest complex

## Finding
Let \(P\) be the eighteen-vertex Pappus graph, the incidence graph of the Pappus \((9_3)\) point-line configuration. Define its vertex-induced forest complex
\[
\mathcal F(P)=\{S\subseteq V(P):P[S]\text{ has no cycle}\}.
\]
There is an integral homotopy equivalence
\[
\boxed{\mathcal F(P)\simeq\bigvee^{40}S^{10}}.
\]
Write \(G=\operatorname{Aut}(P)\), which has order \(216\). Its action on the only nonzero reduced rational homology group has character \(\chi:G\to\mathbb Z\) taking value \(40\) once, \(4\) on \(32\) elements, \(1\) on \(48\) elements, and \(0\) on \(135\) elements. More precisely, the distribution by automorphism order is:

| Order | Character value and multiplicity |
| --- | --- |
| \(1\) | \(40\): \(1\) |
| \(2\) | \(4\): \(18\); \(0\): \(27\) |
| \(3\) | \(4\): \(14\); \(1\): \(12\) |
| \(4\) | \(0\): \(18\) |
| \(6\) | \(1\): \(36\); \(0\): \(54\) |
| \(12\) | \(0\): \(36\) |

Consequently \(\dim_{\mathbb Q}\widetilde H_{10}(\mathcal F(P);\mathbb Q)^G=1\), and the character inner product \(\langle\chi,\chi\rangle_G=10\). The attached verifier computes \(\chi(g)\) for each of the \(216\) permutations, not merely its distribution.

## Assumptions and scope
The graph is simple and has vertex set \(\{0,1,\ldots,17\}\). Its edges are the undirected pairs \(\{i,i+1\}\), for every \(i\), together with \(\{i,i+a_i\}\), where all indices are modulo \(18\) and \(a_i\) is periodic with period six and values \((5,7,-7,7,-7,-5)\). Duplicate undirected edges are listed once. This is the standard Pappus LCF description. The graph has \(27\) edges, degree three at each vertex, and girth six. The complex is on **vertices**, not the distinct edge-set forest/matroid complex or the matching complex.

All assertions concern this graph and its entire \(216\)-element automorphism group. The homotopy assertion is integral and nonequivariant. The character assertion is rational and equivariant; no integral decomposition into irreducible symmetry lattices is asserted.

## Proof
A subset of vertices is a simplex precisely when its induced graph is a forest. For each of the \(2^{18}=262144\) subsets, the verifier computes cycle-freeness using both disjoint-set union and the independent equality \(|E(P[S])|=|S|-c(P[S])\), with \(c\) computed by graph traversal. Both tests agree on exactly \(204492\) faces, including the empty face. The face counts by dimension from \(-1\) through \(12\) are
\[
(1,18,153,816,3060,8568,18546,31608,42516,44228,33660,16776,4290,252).
\]

Construct a partial matching of its face poset as follows. For \(j=0,1,\ldots,17\), visit all still-unmatched faces in increasing binary-mask order. If \(j\notin S\), both \(S\) and \(S\cup\{j\}\) are simplices, and both remain unmatched, pair these two faces. Finally delete the unique matched pair containing the empty face, retaining its vertex as a critical zero-cell. This completely defines the matching with no heuristic or hidden choices. In the directed face Hasse diagram reverse every matched incidence and orient every other incidence from a simplex to a facet. Direct topological sorting exhausts all \(204492\) vertices of this digraph across all \(1704456\) incidences. Thus the matching is acyclic.

There are exactly \(102203\) matched pairs among nonempty faces, and critical cells consist of one zero-cell, one nine-cell, \(62\) ten-cells, and \(21\) eleven-cells. Forman's discrete Morse theorem gives a CW complex of the same homotopy type with precisely these cells.

Orient each simplex by increasing vertex label. The exact algebraic Morse differential is computed by expanding each boundary facet through its unique directed gradient paths: for a lower-dimensional matched face \(\tau\) paired to \(\sigma\), replace \(\tau\) with the signed sum of all other facets of \(\sigma\), divided by the incidence \(\pm1\). The strict Hasse acyclicity makes this recursion finite. The only possibly nonzero reduced Morse boundaries are
\[
\partial_{10}:\mathbb Z^{62}\longrightarrow\mathbb Z,
\qquad
\partial_{11}:\mathbb Z^{21}\longrightarrow\mathbb Z^{62}.
\]
The first is a \(1\)-by-\(62\) row with exactly five nonzero entries, each \(\pm1\), so it is surjective. The second is a \(62\)-by-\(21\) integer matrix with \(95\) nonzero entries, all \(\pm1\). It has \(21\) successive unit pivots under explicit integer elementary row/column operations, so it has rank \(21\) and a primitive image. The verifier also checks \(\partial_{10}\partial_{11}=0\). Hence
\[
\widetilde H_k(\mathcal F(P);\mathbb Z)=
\begin{cases}
\mathbb Z^{40},&k=10,\\
0,&k\ne10.
\end{cases}
\]
The CW model has no cells in dimensions \(1\) through \(8\), so it is \(8\)-connected. The vanishing of its ninth homology and the Hurewicz theorem imply that it is \(9\)-connected. Choosing \(40\) tenth-dimensional spherical maps representing a basis of its homology gives a homology equivalence from \(\bigvee^{40}S^{10}\). The simply connected homological Whitehead theorem turns this map into a homotopy equivalence. This proves the integral claim without assuming that Betti ranks alone determine the attaching maps.

For the symmetry computation, let \(g\in G\) have vertex-cycle orbits \(O_1,\ldots,O_t\). An invariant simplex is a union of these orbits. The oriented simplicial Lefschetz contribution of a nonempty union indexed by \(J\) is \(-(-1)^{|J|}\), because the orientation sign of a vertex permutation on its selected orbits is \((-1)^{|S|-|J|}\). Including the augmentation term for the empty face gives
\[
\chi(g)=-\!\sum_{\substack{J\subseteq\{1,\ldots,t\}\\P[\bigcup_{j\in J}O_j]\text{ acyclic}}}(-1)^{|J|}.
\]
The reduced Lefschetz number equals \(\chi(g)\), since reduced rational homology is supported only in even degree \(10\). Distance-preserving backtracking lists every automorphism (\(216\) in total), and the formula above evaluates every trace. Summing traces yields \(216\); summing squared traces yields \(2160\). Division by \(|G|=216\) gives the invariant dimension and character inner product stated above.

## Verification
Run `python3 pappus_forest_verify.py` in a directory containing that standalone source file. It uses only the Python standard library and needs no data downloads, computer-algebra package, or internet connection. The exact machine-readable output is also embedded as `verification_output.txt`. The program performs both forest tests, verifies the complete reversed-Hasse orientation is acyclic, constructs the signed Morse matrices, carries out integral unit-pivot elimination, enumerates the automorphism group and evaluates the Lefschetz character. The output ends in `VERIFY_OK` only after all assertions succeed.

## Relationship to prior work
Taylan (2015) developed general Morse/matching-tree methods for graph-defined devoid complexes and calculated families including paths and cycles; this is methodological precedent, not an explicit Pappus induced-forest classification. Zuffi (2017, §1.5.1) defined the same vertex-induced acyclic complex and distinguished it from an edge-acyclic complex, but did not calculate the Pappus example. Carnero Bravo (2023) studied the forest filtration and worked out several graph families (including paths, cycles, complete multipartite, cactus, joins and selected products); the Pappus incidence graph is not among those classified families. The known Pappus graph independence, matching, Čech, Rips and configuration-space results concern different simplicial constructions. In particular, the indexed Pappus matching complex also has \(40\) spheres, but in dimension \(5\) on graph **edges**, which does not imply this vertex-induced forest result.

## Limitations
This is a finite, exact classification for the Pappus incidence graph, not a theorem for all \((9_3)\) configurations or cubic symmetric graphs. It determines the rational homology character and its invariant dimension, not an integral automorphism-module decomposition or an equivariant wedge of spheres. Independent mathematical audit remains unperformed. Equivalent treatments in unindexed or uninspected literature cannot be categorically excluded by search; no absolute priority claim is made.

## References
1. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, first public 2015-01-27, https://arxiv.org/html/1501.06754v1.
2. L. Zuffi, *Simplicial Complexes From Graphs Toward Graph Persistence*, University of Bologna thesis, 2017, §1.5.1, https://amslaurea.unibo.it/id/eprint/13519/.
3. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, 2023, https://arxiv.org/abs/2307.13271.
4. *Pappus Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/PappusGraph.html (LCF description).
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete Morse theorem).
