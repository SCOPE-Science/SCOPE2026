# The two-independence complex of the four-cube is a mixed-dimensional sphere wedge

## Finding
Let \(Q_4\) be the graph on the sixteen binary words in \(\mathbb F_2^4\), with edges between words at Hamming distance one. Let \(X=\operatorname{Ind}_2(Q_4)\) be its two-independence complex: a set of vertices is a face exactly when every connected component of its induced subgraph has at most two vertices. Then the **integral homotopy type** is
\[
X\simeq\left(\bigvee^{16}S^3\right)\vee S^4.
\]
In particular, its reduced integral homology is \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^{16}\), \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z\), and zero in other degrees. The same result applies to the two-independence complex of the toroidal square grid \(C_4\mathbin{\square}C_4\cong Q_4\).

## Assumptions and scope
Vertices of \(Q_4\) are indexed by integers \(0,\ldots,15\), interpreted as four-bit words. Two indices \(i,j\) are adjacent precisely when the binary expansion of \(i\oplus j\) has one nonzero bit. A vertex subset \(S\) is a simplex if and only if every \(i\in S\) has at most one neighbor in \(S\); equivalently, the induced graph is a disjoint union of isolated vertices and edges. The equivalence holds because any graph with maximum degree one is a union of such components. This is the usual two-independence, or three-vertex-path-free, convention; it is not the ordinary independence complex or the matching complex. All homotopy and homology statements have integral, not merely rational or mod-two, meaning. No conclusion about higher-dimensional hypercubes is asserted.

## Proof
**Exhaustive finite face model.** Write \(m(S)=\sum_{i\in S}2^i\) for a simplex mask. The included standalone exact verifier considers all \(2^{16}-1\) nonempty subsets and retains precisely those satisfying the preceding neighbor condition. It finds \(3054\) simplices with dimension-by-dimension face counts
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7)
=(16,120,464,964,960,440,80,10).
\]
Every mask and adjacency test is reconstructed solely from the four-bit definition, not an imported face table.

**Acyclic matching.** On the nonempty face poset, start with every face unmatched and process vertex toggles in the specified order
\[
(0,11,5,4,2,3,15,10,8,13,7,14,9,12,6,1).
\]
At a toggle vertex \(v\), match each still-unmatched face \(S\) not containing \(v\) to \(S\cup\{v\}\) when both faces are still unmatched. This gives exactly \(1518\) disjoint face/coface pairs. Orient the \(13568\) cover edges of the face-poset Hasse diagram downward, except orient all matched incidences upward. The executable verifier constructs this entire graph and topologically sorts every one of its \(3054\) vertices, proving the orientation has no directed cycle; hence the matching is an acyclic Forman matching. There is one critical vertex (mask \(1\)), sixteen critical three-simplices (masks \(600,960,1080,1424,4124,4488,8772,9236,12300,16962,17442,20490,32824,33168,40980,49186\)), and one critical four-simplex (mask \(33874\)). No other critical faces survive.

**Exact integer attaching degree.** The cellular Morse differential from the sole critical four-cell to the sixteen critical three-cells is computed with signed integer incidence, oriented by increasing original vertex labels. For a four-vertex face \(F\), the verifier computes the integer projection \(p(F)\) onto critical three-faces recursively: \(p(F)=F\) for critical faces; \(p(F)=0\) if the three-face is paired downward with a two-face; and if \(F\) is paired upward with a four-face \(U\), solve the oriented equation \(\partial U=0\) for the coefficient of \(F\), substituting projected other three-faces. All paired incidence coefficients are \(\pm1\), so elimination uses only integral operations. Acyclicity ensures recursion terminates, and the verifier independently checks no recursion cycle occurs. Applied to the signed simplicial boundary of the unique critical four-simplex, the result is **the zero vector in \(\mathbb Z^{16}\)**, checked exactly, not modulo a prime.

**Homotopy identification.** Forman's discrete Morse theorem supplies a CW complex with one zero-cell, sixteen three-cells, one four-cell and no other cells, with the above integer Morse boundary. Its three-skeleton is a wedge of sixteen three-spheres, which is two-connected. The Hurewicz isomorphism identifies \(\pi_3\) of this wedge with its third integral homology. Because the signed cellular boundary of the four-cell is zero, its attaching map represents zero in \(\pi_3\) and is nullhomotopic. Attaching it therefore adds a wedge summand \(S^4\). This proves the asserted integral homotopy equivalence.

## Verification
Run `python3 verify_ind2_q4.py` under Python 3.9 or later, from the directory containing that file. No nonstandard packages, network access, input datasets, or compiled extensions are required. Its exact reference output is embedded as `verify_ind2_q4.out`. The script tests the complete face list, every matching pair, every oriented Hasse cover, global acyclicity by full topological sort, and the exact signed integral Morse differential. As an independent arithmetic consistency check, it also directly constructs every original mod-two simplicial boundary and obtains full boundary ranks \((15,105,359,589,370,70,10)\), giving Betti vector \((1,0,0,16,1,0,0,0)\). The mod-two check is ancillary: the integer attaching-map calculation is essential for the claimed homotopy type.

## Relationship to prior work
Sawant's 2026 study of higher independence complexes proves vertex decomposability for **trees**, introducing a natural current boundary for such results; \(Q_4\) contains induced four-cycles and hence is not a tree. Deshpande and Singh's foundational 2020 homotopy classifications concern complete multipartite, path, cycle, whiskered, and selected tree graph families; the four-cube does not belong to those families. The chordal-graph study of Abdelmalek and collaborators also does not directly cover this nonchordal graph. Deshpande, Roy and Sawant's 2025 paper studies Alexander-dual co-connected complexes and selected graph classes, with no displayed four-cube two-independence homotopy classification. The published result for the **ordinary** independence complex of \(Q_4\) concerns a different simplicial complex and does not imply the present theorem. Searches found no exact stronger theorem for the same induced-component-size-two construction on \(Q_4\); absence of a search hit is not proof of worldwide priority.

## Limitations
This is a finite, natural sixteen-vertex classification supported by an exhaustive reproducible integer certificate, not an all-dimensions formula. It does not determine an equivariant homotopy type or assert shellability. The homotopy identification uses the standard discrete Morse and Hurewicz theorems in addition to verified finite computations. Literature discovery is not exhaustive: an unindexed equivalent computation might exist, and one recent complete-multipartite paper was only available in abstract form; its stated graph family is nevertheless inapplicable to \(Q_4\). Independent external scientific verification has not been performed.

## References
1. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150, first submitted 2026-05-24. https://arxiv.org/abs/2605.25150
2. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448. https://arxiv.org/abs/2001.05448
3. R. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863. https://arxiv.org/abs/2106.10863
4. P. Deshpande, A. Roy, and R. Sawant, *The complex of \(r\)-co-connected subgraphs, chordality and Fröberg's theorem*, arXiv:2510.25710, first submitted 2025-10-29. https://arxiv.org/abs/2510.25710
5. R. Forman, *Morse Theory for Cell Complexes*, Adv. Math. 134 (1998), 90–145.
