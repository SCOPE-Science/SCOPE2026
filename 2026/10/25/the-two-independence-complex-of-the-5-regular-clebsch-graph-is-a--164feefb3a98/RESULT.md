# The two-independence complex of the 5-regular Clebsch graph is a four-sphere

## Finding
Let \(C\) denote the **5-regular**, sixteen-vertex Clebsch graph (the folded five-cube), and let \(K=\operatorname{Ind}_2(C)\) be its two-independence complex. There is a homotopy equivalence
\[
|K|\simeq S^4.
\]
The automorphism group is the affine group of even-bit translations and coordinate permutations, \(\operatorname{Aut}(C)=T\rtimes S_5\), where \(T\cong(\mathbb Z/2\mathbb Z)^4\). Its action on the integral homology line is
\[
\widetilde H_4(K;\mathbb Z)\cong\mathbb Z_{\mathrm{sgn}},\qquad
(t,\pi)\longmapsto\operatorname{sgn}(\pi).
\]
Consequently the only nonzero reduced integral homology is \(\widetilde H_4(K;\mathbb Z)\cong\mathbb Z\); the 960 elements with even coordinate permutation have degree \(+1\), and the other 960 have degree \(-1\).

## Assumptions and scope
Use the even-weight elements \(V=\{v\in\{0,1\}^5: \sum v_i\equiv0\pmod2\}\), ordered by their five-bit integer values. The graph has one edge \(\{v,w\}\) exactly when the Hamming weight of \(v\oplus w\) is four. This specifies a simple graph with 16 vertices and 40 edges and removes ambiguity with the ten-regular complement sometimes also called Clebsch.

By definition, a nonempty subset \(A\subseteq V\) is a face of \(K\) precisely when every connected component of the induced graph \(C[A]\) contains at most two vertices. Equivalently, each vertex of \(C[A]\) has induced degree at most one; this equivalence is exact for every finite simple graph. The empty face is included when defining the simplicial complex and excluded from the nonempty-face Morse matching.

## Proof
**1. Explicit face-poset matching.** Encode the 16 vertices in increasing five-bit order as positions \(0,\ldots,15\), and encode a face by its sixteen-bit incidence integer. The complete nonempty face set has 2,142 elements with face vector, indexed by dimensions zero through seven,
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7)
=(16,120,400,660,576,280,80,10).
\]
This is not an inference from sampling: the supplied checker exhausts all 65,535 nonempty subsets and tests the defining induced-degree condition.

Define an ordered element matching using positions \(0,1,\ldots,15\). Initially all nonempty faces are unmatched. At position \(i\), pair every still-unmatched face \(A\) not containing \(i\) with \(A\cup\{i\}\) whenever both are still unmatched. Remove both members of each pair before proceeding to position \(i+1\). These are codimension-one face/coface pairs. The attached certificate records every pair, and the checker independently reconstructs the 1,070 pairs; only two unpaired nonempty simplices remain: mask \(1\) (a vertex) and mask \(61696\) (a four-dimensional simplex supported at positions \(8,12,13,14,15\)).

The acyclicity is verified directly, not inferred from the small number of critical cells: for each nonempty codimension-one face incidence orient the Hasse edge from larger to smaller simplex, *except* matched incidences, which are reversed. The resulting graph has exactly 2,142 vertices and 9,280 directed edges. The supplied independent topological-sort calculation visits all 2,142 vertices; therefore the graph is acyclic. This is a full finite combinatorial certificate of a discrete-Morse matching.

By the acyclic-matching theorem for simplicial face posets, \(K\) has the homotopy type of a CW complex with exactly one zero-cell and exactly one four-cell, and no other cells. Such a CW complex is \(S^4\), because its four-cell attaches to the unique point by the only possible constant map.

**2. Complete symmetry group.** Translation by any even bit vector and permutation of the five coordinates preserves Hamming distance four, so \(T\rtimes S_5\) acts faithfully on \(C\). This gives 16 times 120 automorphisms. Conversely, any automorphism fixing the zero vertex permutes its five neighbors (the weight-four vectors). Every one of its ten remaining nonzero nonneighbors (weight-two vectors) is uniquely specified as the common neighbor of exactly one *pair* of these five neighbors. Thus the vertex stabilizer injects into \(S_5\). Transitivity of \(T\) proves these are all 1,920 automorphisms.

**3. Integral orientation character.** For a simplicial automorphism \(g\), its reduced Lefschetz number is the exact signed face sum
\[
\widetilde L(g)=-1+
\sum_{\substack{\varnothing\ne A\in K\g(A)=A}}
(-1)^{|A|-1}\operatorname{sgn}(g|_A).
\]
Here \(\operatorname{sgn}(g|_A)\) means the sign of the permutation induced on the canonically ordered vertices of the invariant face. As \(S^4\) is the homotopy type, the reduced Lefschetz number is exactly the integer degree on \(\widetilde H_4\). The checker enumerates *all* 1,920 affine automorphisms and every fixed face and obtains \(\widetilde L(t,\pi)=\operatorname{sgn}(\pi)\) in each case. This exhaustively certifies the asserted integral one-dimensional character; it is not merely a mod-two statement.

## Verification
The standalone `verify.py` reads `certificate.json` and uses only the Python standard library. Run `python3 verify.py` from the extracted folder. It reconstructs the graph, independently enumerates all faces, rebuilds the matching and checks its complete pair set and two critical cells, topologically sorts the entire reversed-matching Hasse digraph, establishes the full affine automorphism group as in the proof, and checks the signed Lefschetz formula for all 1,920 automorphisms. Reported counts are 40 edges, 2,142 nonempty faces, 1,070 Morse pairs, 9,280 face incidences, and 960 positive and 960 negative symmetry degrees. The finite combinatorial exhaustion is complete because the vertex set has exactly sixteen elements.

## Relationship to prior work
Deshpande and Singh (2020/2021), *Higher Independence Complexes of Graphs and Their Homotopy Types*, define the same higher-independence functor and prove homotopy classifications for complete multipartite, fully whiskered, paths, cycles, and perfect rooted-tree families; their paper also supplies the sequential element-matching technique used here. The 5-regular Clebsch graph belongs to none of those classes. Sawant (2026), *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, provides recent motivation for higher-independence topology and three-path-free complexes, but treats trees, not this girth-four strongly regular graph. Xu, Lei, Liu and Li (2025) describe the same explicit even-subset Clebsch model but address Hadwiger minors of its complement. Published computations of the **ordinary** independence complex and of the open-neighborhood complex of the Clebsch graph are distinct invariants and do not imply this two-independence homotopy type or its integral affine-symmetry character. No equivalent result was identified in the searches described in the review; this is not proof of global novelty.

## Limitations
This is an exact classification of this one natural finite graph complex, not a theorem for all folded hypercubes or all strongly regular graphs. The automorphism representation is an assertion on integral homology, not an equivariant homotopy equivalence. No statement about shellability or vertex decomposability is made. Independently produced scientific validation and exhaustive literature coverage are not claimed.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, first public 2020-01-15, arXiv:2001.05448, https://arxiv.org/html/2001.05448v2 . Sections 2–5, including Proposition 2.10 on sequential element matchings.
2. R. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, first public 2026-05-24, arXiv:2605.25150, https://arxiv.org/abs/2605.25150 . Introduction and Theorem 3.6.
3. G. Xu, L. Lei, X. Liu, Y. Li, *Hadwiger's Conjecture for Dense Strongly Regular Graphs*, *Symmetry* 17 (2025), 1588, https://doi.org/10.3390/sym17101588 . Published 2025-09-23; Section 3 gives the even-subset model of the Clebsch graph.
4. F. M. Abdelmalek et al., *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, https://arxiv.org/html/2106.10863v3 . Non-Clebsch graph classes and structural context.
