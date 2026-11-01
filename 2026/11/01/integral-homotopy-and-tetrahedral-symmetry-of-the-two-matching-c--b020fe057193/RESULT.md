# Integral homotopy and tetrahedral symmetry of the two-matching complex of the truncated tetrahedron

## Finding
Let \(T\) be the twelve-vertex, eighteen-edge truncated-tetrahedral graph, and let \(M_2(T)\) be the simplicial complex whose vertices are graph edges and whose faces are edge sets with selected degree at most two at each graph vertex. Then
\[
\boxed{M_2(T)\simeq\bigvee^{5}S^{8}.}
\]
In particular its complete reduced integral homology is \(\widetilde H_8(M_2(T);\mathbb Z)\cong\mathbb Z^5\), with zero groups in every other degree and no torsion.

The natural action of the full automorphism group \(\operatorname{Aut}(T)\cong\mathfrak S_4\) has degree-eight rational homology representation
\[
\boxed{\widetilde H_8(M_2(T);\mathbb Q)\cong
\mathbf1\oplus\operatorname{sgn}\oplus(\operatorname{sgn}\otimes\operatorname{Std}_4).}
\]
The character values for identity, transposition, double transposition, three-cycle, and four-cycle are respectively \((5,-1,1,2,1)\). Here \(\operatorname{Std}_4\) is the three-dimensional augmentation representation of \(\mathfrak S_4\).

## Assumptions and scope
The graph is specified without external graph-generation packages. Set
\[
V(T)=\{(i,j):i,j\in\{0,1,2,3\},\ i\ne j\}.
\]
Distinct ordered pairs \((i,j)\) and \((k,l)\) are adjacent precisely when \(i=k\) or \((k,l)=(j,i)\). Thus the four sets of vertices with fixed first coordinate span four disjoint triangles; the six reversal edges connect these triangles. Each vertex has degree three. This is the edge graph of the truncated tetrahedron, not the ordinary tetrahedron.

Write \(E(T)=\{e_0,\ldots,e_{17}\}\), with the edges ordered lexicographically by their two endpoint indices, where the twelve ordered-pair vertices are likewise lexicographically ordered. A face of \(M_2(T)\) is a subset \(F\subseteq E(T)\) with \(|\{e\in F:v\in e\}|\le2\) for every \(v\in V(T)\). The empty face is included in the combinatorial face poset; the geometric realization uses nonempty simplices. All homotopy equivalences are non-equivariant; only the stated rational homology representation is equivariant.

## Proof
**1. Exhaustive finite face reconstruction.** Encode each edge set as an 18-bit integer. For each graph vertex, construct the mask of its three incident edges. Among all \(2^{18}=262144\) masks, retain a mask exactly when every incident-edge intersection has cardinality at most two. An independent direct selected-edge-degree implementation tests every mask and agrees on all \(262144\) tests. There are \(69075\) faces including the empty face. The nonempty face vector in dimensions \(0\) through \(11\) is
\[
(18,153,804,2880,7326,13382,17352,15402,8698,2709,342,8).
\]

**2. An explicitly reproducible acyclic matching.** Starting from the full face set, process edge bits in increasing order \(0,1,\ldots,17\). At step \(i\), simultaneously pair every still unmatched face lacking bit \(i\) with its still unmatched one-bit augmentation, and delete these pairs from the unmatched pool. This gives exactly \(34533\) disjoint covering pairs; the only unmatched faces are seven of dimension eight and two of dimension nine. Their precise bitmasks, in ascending order within each dimension, are
\[
(81062,90872,157462,201464,202518,203430,208022)
\]
and
\[
(204582,208120).
\]
The empty face is paired with a singleton. On the ordinary nonaugmented face poset this singleton is instead retained as a single critical zero-cell, and the other critical cells remain unchanged.

Orient each covering relation from coface to face, except reverse the orientation for each matching pair. The standalone verifier constructs all \(485088\) incidences between the \(69075\) augmented faces, and a full topological sort visits all \(69075\) nodes. Hence the matching is acyclic, not just experimentally sampled. Discrete Morse theory gives a CW model with one zero-cell, seven eight-cells and two nine-cells, with no other cells. The basepoint and eight-cells form \(\bigvee^7 S^8\).

**3. Exact integer attaching degrees.** Give every simplex the orientation of increasing edge-bit indices; the simplicial boundary deletes the \(j\)-th bit with sign \((-1)^j\). For each lower matched face \(a\subset b\), write \(\partial b=\varepsilon a+\sum_{c\ne a}\varepsilon_c c\), where \(\varepsilon=\pm1\), and substitute \(a=-\varepsilon\sum_{c\ne a}\varepsilon_c c\). Recursively project all boundary terms to critical cells, setting projected matched higher cells to zero. Acyclicity makes this elimination well founded. It gives the exact integral Morse cellular differential, not an approximation.

With rows ordered by the seven increasing eight-cell masks above and columns by the two increasing nine-cell masks, the full attaching-degree matrix is
\[
\partial_9=
\begin{pmatrix}
0&0\\
0&1\\
0&0\\
0&1\\
1&0\\
-1&0\\
0&1
\end{pmatrix}.
\]
Its rows 2 and 5 (one-indexed) give a determinant \(-1\) minor. Thus its two independent degree columns are primitive and may be taken, after changes of sphere generators, to two standard basis vectors. Since \(\pi_8(\bigvee^7 S^8)\cong\mathbb Z^7\), the degree vectors completely determine the attaching maps up to homotopy; the two primitive nine-cell attachments cancel two eight-spheres. This proves \(M_2(T)\simeq\bigvee^5S^8\) over the integers, with no claim of an equivariant CW cancellation.

**4. The full tetrahedral symmetry character.** The four triangles of \(T\) are precisely its three-cycles. An automorphism must permute them. Each inter-triangle edge is a reversal edge, uniquely identifying its endpoint with the ordered pair of its two triangle labels; therefore the action on the four triangles determines the automorphism. Conversely every permutation of the four labels acts on ordered pairs. Hence \(\operatorname{Aut}(T)=\mathfrak S_4\).

For each of its 24 permutations \(g\), induce the permutation of the 18 graph edges. The exact reduced simplicial Lefschetz sum is
\[
L_{\mathrm{red}}(g)=
\sum_{\substack{\emptyset\ne\sigma\in M_2(T)\\g\sigma=\sigma}}
(-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma)-1.
\]
Because the only reduced rational homology is in even degree eight, this number equals its degree-eight trace. Exhaustive evaluation gives class sizes \((1,6,3,8,6)\) and traces \((5,-1,1,2,1)\), in the class order stated above. Inner products against the five irreducible \(\mathfrak S_4\) characters yield multiplicities \((1,1,0,1,0)\) for trivial, sign, standard, sign-twisted standard, and the two-dimensional irreducible. This establishes the representation formula.

## Verification
Run `python3 verify_truncated.py` with Python 3.10 or later; it uses no external library or downloaded data. It rebuilds the graph directly from the ordered-pair definition, independently tests all \(262144\) selected-edge subsets, checks the exact face vector, recomputes the lexicographic matching and its full acyclicity, and reconstructs the integer Morse matrix and a determinant \(-1\) maximal-rank minor.

Independently of the Morse calculation, the program forms the full simplicial chain complex over \(\mathbb F_2\) and reduces its boundary matrices by exact bitset Gaussian elimination. Only the reduced eighth Betti number is nonzero, with rank five; these finite-field checks corroborate, but do not replace, the integral proof. All 24 group permutations and every invariant simplex are enumerated in the signed Lefschetz check. The companion `verification_output.json` records exact numerical results, critical masks, ranks and characters. Successful replay prints `TRUNCATED_TETRAHEDRON_TWO_MATCHING_INTEGRAL_S4_VERIFIED`.

## Relationship to prior work
Vega's foundational *2-Matching Complexes* (first public September 23, 2019) introduces the same degree-two condition and proves homotopy results for leaf-attached clawed graphs, wheels, and caterpillars; these hypotheses do not include this cubic graph with four triangles and no leaves [1]. Singh's *Bounded degree complexes of forests* concerns forests, whereas \(T\) contains four triangles [2]. Singh's *Higher matching complexes of complete graphs and complete bipartite graphs* treats two families to which this noncomplete, nonbipartite graph does not belong [3]. Their relevant primary texts were inspected beyond their abstracts, including statements of the main theorems.

A published calculation for this very same truncated-tetrahedral graph determines its ordinary **one-matching** complex as \(\bigvee^{22}S^3\), together with deletion/link data [4]. That full result treats the incidence cutoff one, not the degree-two complex above; its theorem and proof do not imply the degree-two attaching matrix or full tetrahedral homology character. The degree-three complex is simply the full simplex because the graph is cubic. Thus the new result supplies the missing homotopy stage between the already-studied cutoff one and the trivial cutoff three. Its output does not prove anything about the inclusion maps between these stages.

Equivalent names include the uniform bounded-degree complex \(\mathrm{BD}^{(2,\ldots,2)}(T)\) and the independence complex of the 3-uniform hypergraph of triples forming vertex stars. Those are the *same* complex, and were considered during novelty comparisons. The ordinary matching complex of the line graph is a different cutoff and cannot be substituted. No claim of absolute bibliographic uniqueness is made.

## Limitations
This is a finite, completely reproducible homotopy computation for one naturally motivated twelve-vertex cubic graph. It does not prove a formula for all cubic or all Archimedean graphs, does not describe the homotopy class of either filtration inclusion, and does not give an equivariant sphere-wedge model. The rational character does not determine an integral \(\mathbb Z[\mathfrak S_4]\)-module structure. A genuine unindexed or inaccessible equivalent prior calculation remains possible. No external independent mathematical audit has been performed.

## References
1. J. Vega, *2-Matching Complexes*, arXiv:1909.10406, first submitted September 23, 2019, https://arxiv.org/html/1909.10406v2.
2. A. Singh, *Bounded degree complexes of forests*, arXiv:1910.12793, first submitted October 28, 2019, https://arxiv.org/abs/1910.12793.
3. A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, first submitted June 24, 2020, https://arxiv.org/abs/2006.13632.
4. *Edge-orbit matching-complex homotopy of the truncated tetrahedron*, publicly available research record, October 2026.
