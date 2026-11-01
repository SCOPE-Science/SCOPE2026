# The Clebsch two-independence complex is a four-sphere with a sign character

## Finding
Let \(C\) be the five-regular Clebsch graph, equivalently the folded five-cube or Greenwood–Gleason graph. Define \(\operatorname{Ind}_2(C)\) to be the simplicial complex of vertex subsets whose induced connected components each contain at most two vertices. Then
\[
\boxed{\operatorname{Ind}_2(C)\simeq S^4.}
\]
The full graph automorphism group is \(\operatorname{Aut}(C)\cong\mathbb F_2^4\rtimes S_5\). On the unique nonzero reduced integral homology group, the action is the sign character of the \(S_5\) factor:
\[
\boxed{\widetilde H_4(\operatorname{Ind}_2(C);\mathbb Z)\cong\mathbb Z_{\operatorname{sgn}\circ\pi},\qquad
\pi:\mathbb F_2^4\rtimes S_5\longrightarrow S_5.}
\]
Thus translations preserve the fundamental homology class, while a transposition of the five natural cube directions reverses it. All other reduced integral homology groups vanish. The complex itself is nonpure of dimension seven, with sixteen four-dimensional facets and ten seven-dimensional facets.

## Assumptions and scope
The graph has vertex set \(\mathbb F_2^4\), encoded by the integers \(0,1,\ldots,15\), and adjacency
\[
x\sim y\quad\Longleftrightarrow\quad x+y\in\{e_1,e_2,e_3,e_4,e_1+e_2+e_3+e_4\}.
\]
Addition is in \(\mathbb F_2^4\). In the integer bitmask encoding, the five generator masks are `1,2,4,8,15`, and adjacency is tested using bitwise XOR. This is the 16-vertex, 40-edge, strongly regular graph with parameters \((16,5,0,2)\), not its ten-regular complement.

A vertex subset is a face exactly when every selected vertex has at most one selected neighbor. Indeed, an induced graph all of whose vertices have degree at most one is a disjoint union of edges and isolated vertices. Equivalently, the complex is the dissociation-set complex, or the independence complex of the three-uniform hypergraph of three-vertex paths of \(C\). These equivalences are definitions, not separate discoveries.

## Proof
**Finite face set.** Enumerate every one of the \(2^{16}=65,536\) vertex masks and retain exactly those satisfying the induced-degree condition above. Including the empty face, the face vector is
\[
(f_{-1},f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7)
=(1,16,120,400,660,576,280,80,10).
\]
The exhaustive face test is reproduced by `verify.py`, which checks downward closure and all strongly regular graph parameters.

**An acyclic matching.** Initially mark all augmented faces unmatched. For \(i=0,1,\ldots,15\) in that order, pair every currently unmatched face \(\sigma\) not containing vertex \(i\) with \(\sigma\cup\{i\}\), whenever the latter is also a currently unmatched face. The resulting augmented matching has \(1,066\) pairs, including the pair consisting of the empty face and vertex \(0\). Omit this pair when passing to the ordinary nonempty face poset. The ordinary matching has \(1,065\) pairs and exactly one critical zero-cell, five critical three-cells, and six critical four-cells.

For every one of the \(9,280\) ordinary face-poset Hasse incidences, orient the cover downward except when it belongs to the matching, in which case orient it upward. A complete topological sort visits all \(2,142\) nonempty faces. Therefore the matching is acyclic, not merely apparently cycle-free in sampled gradient paths. Forman's discrete Morse theorem gives a CW model with precisely the stated critical cells.

**The exact integral attaching matrix.** Give each simplex the ascending vertex orientation. If a matched lower three-face \(a\) is paired with an upper four-face \(u\), eliminate \(a\) by the signed boundary relation for \(u\). Repeat recursively along the acyclic matching. Applied to the boundaries of the six critical four-faces and expressed in the five critical three-faces, this produces the exact integral Morse differential
\[
\partial^{\mathrm M}_4=\begin{pmatrix}
-1&0&0&0&0&-1\\
1&1&0&0&0&0\\
0&-1&1&0&0&0\\
0&0&0&1&0&1\\
0&0&0&0&1&-1
\end{pmatrix}.
\]
The leading five-by-five minor has determinant \(-1\). Thus all five nonzero integral Smith invariant factors are units. There are no critical cells in dimensions one or two; the three-skeleton of the Morse CW model is a wedge of five three-spheres. By the Hurewicz isomorphism in degree three, the attaching maps of its four-cells are completely determined by the displayed integer matrix. Integral elementary changes of the three-sphere basis and four-cell attaching maps cancel five three/four-cell pairs, leaving one four-cell attached to a point. Hence the space is homotopy equivalent to \(S^4\). In particular this argument proves the actual homotopy type, not merely its homology.

**Full symmetry and its degree.** Write the five Cayley generators as \(s_1,\ldots,s_5\). They have the unique linear relation \(s_1+\cdots+s_5=0\); any four are independent. The ten vertices outside \(\{0,s_1,\ldots,s_5\}\) are the ten distinct pair sums \(s_i+s_j\). Consequently a graph automorphism is determined by the image of \(0\) and the permutation induced on its five neighbors: at most \(16\cdot120=1,920\) choices. Translations and arbitrary linear permutations of the five generators realize all these choices, establishing the full semidirect-product group.

Because all reduced homology is concentrated in even degree four and is infinite cyclic, an automorphism's degree on homology equals its reduced Lefschetz number. The checker computes this number exactly as the alternating signed trace on the augmented simplicial chains, assigning each invariant nonempty simplex the orientation sign of its induced vertex permutation. The four basis translations have reduced Lefschetz numbers \(+1,+1,+1,+1\). A transposition interchanging \(s_1\) and \(s_2\) has reduced Lefschetz number \(-1\). These elements generate the translation subgroup and, by conjugacy, determine the character on the full symmetric-group factor. Hence the integral action is \(\operatorname{sgn}\circ\pi\), as claimed.

## Verification
Run `python3 verify.py` with Python 3.10 or later; no dependencies are needed. The program reconstructs all \(2^{16}\) masks, verifies the graph, builds the matching, topologically sorts the entire oriented Hasse graph, computes the exact signed five-by-six matrix by recursive pivot elimination, and checks its unimodular minor with exact integer arithmetic. As an independent check it computes simplicial boundary ranks over \(\mathbb F_2\) directly from the full complex, obtaining precisely one nonzero reduced Betti number in dimension four. It also checks all facet dimensions, reduced Euler characteristic, and the homology degrees of automorphism generators using signed Lefschetz sums. Expected success line: `CLEBSCH_TWO_INDEPENDENCE_S4_OK`. The included `verification_output.txt` records the complete output of the packaged checker.

## Relationship to prior work
Deshpande and Singh introduced and classified higher-independence complexes for complete multipartite graphs, fully whiskered graphs, cycles, paths and perfect rooted trees (arXiv:2001.05448). The Clebsch graph belongs to none of those classes. Abdelmalek, Deshpande, Goyal, Roy and Singh studied shellability and decomposability for chordal and related graph families (arXiv:2106.10863). The Clebsch graph contains induced four-cycles, so the chordal-family results do not imply the present homotopy classification.

Previously reported Clebsch **open-neighborhood** homology and Clebsch **matching** homology concern different simplicial complexes. An open-neighborhood simplex has a common neighbor, whereas a face here forbids induced three-vertex connected subgraphs; a matching-complex vertex represents a graph edge rather than a graph vertex. Neither previous statement yields this four-sphere or its integral symmetry character. The ordinary four-cube and folded-cube independence calculations likewise use a different complex or graph.

Literature and indexed mathematical-record searches were also made under the names *Clebsch*, *folded five-cube*, *Greenwood–Gleason*, *projective cube*, *dissociation complex*, *two-independence complex*, and *three-vertex-path hypergraph*. No covering exact homotopy or equivariant theorem was identified. This is a best-knowledge originality assessment; a differently indexed or implicit equivalent statement could exist.

## Limitations
The result concerns precisely the two-independence complex of the five-regular Clebsch graph; it does not classify higher cutoffs, all folded cubes, or all strongly regular graphs. The standalone computation is exhaustive because there are only \(2^{16}\) vertex subsets and each finite incidence is checked, not because a finite sample supports an infinite conjecture. The group character is an integral homology representation statement, not an assertion of equivariant homotopy equivalence. Independent scientific audit has not been performed.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first public 2020-01-15, Journal of the Ramanujan Mathematical Society 36 (2021), 53–71; https://arxiv.org/html/2001.05448v2.
2. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, first public 2021-06-21; https://arxiv.org/abs/2106.10863.
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145; DOI: 10.1006/aima.1997.1650.
4. *The five-regular Clebsch neighborhood complex is a wedge of thirty-one two-spheres*, published mathematical record, 2026-10-11; https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-5-regular-clebsch-neighborhood-complex-is-a-wedge-of-31-2-sp--1dc11cc6574a.
5. *Mod-two homology of the Clebsch matching complex*, published mathematical record, 2026-10-11; https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-mod-2-homology-of-the-clebsch-matching-complex--7e53e4d18ed4.
