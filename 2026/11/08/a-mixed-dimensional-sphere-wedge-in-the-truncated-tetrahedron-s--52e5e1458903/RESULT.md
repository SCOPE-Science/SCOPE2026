# A mixed-dimensional sphere wedge in the truncated tetrahedron's second independence complex

## Finding
Let \(T\) be the graph of the truncated tetrahedron, defined precisely below. Its second independence complex, equivalently its three-vertex-path-devoid complex, has the **integral homotopy type**
\[
\operatorname{Ind}_{2}(T)\simeq
\left(\bigvee^{3}S^{3}\right)\vee
\left(\bigvee^{3}S^{4}\right).
\]
In particular, the two nonzero reduced integral homology groups are \(\widetilde H_3\cong\mathbb Z^3\) and \(\widetilde H_4\cong\mathbb Z^3\); the conclusion determines the homotopy type, not just homology.

## Assumptions and scope
The vertex set of \(T\) is the twelve ordered pairs \((i,j)\), where \(i,j\in\{0,1,2,3\}\) and \(i\ne j\). Two distinct pairs \((i,j)\) and \((k,l)\) are adjacent precisely when \(i=k\), or when \((k,l)=(j,i)\). Thus the four groups having fixed first coordinate are triangles, joined by six edges linking reversed pairs; this is the standard truncated-tetrahedral graph with eighteen edges. There are no arbitrary choices of embedding.

A face of \(\operatorname{Ind}_2(T)\) is a subset of graph vertices such that every connected component of its **induced** subgraph has at most two vertices. Equivalently, the selected vertices contain no three-vertex path as a not-necessarily-induced subgraph. An induced triangle is therefore forbidden. The theorem concerns this single finite, explicitly labeled graph and ordinary nonequivariant homotopy.

## Proof
List graph vertices lexicographically as indices \(0,\ldots,11\) and encode a face \(F\) by its mask \(m(F)=\sum_{v\in F}2^v\). Every nonempty mask smaller than \(2^{12}\) is tested by an exact component traversal. The face vector, in dimensions zero through five, is
\[
(12,66,192,303,228,62),
\]
so there are precisely 863 nonempty faces. These checks are exhaustive, not samples. A separate forbidden-triple enumerator independently obtains the same vector and identifies 28 forbidden triples.

Next perform **successive element matchings** on currently unmatched faces, in the fixed vertex order
`0,3,6,9,1,4,7,10,2,5,8,11`.
At the step for vertex \(v\), match each remaining face \(A\) not containing \(v\) to \(A\cup\{v\}\) when the latter remains; remove both faces from subsequent steps. This completely specified algorithm produces 428 pairs and leaves exactly seven critical nonempty simplices. Their masks, grouped by dimension, are:

- dimension zero: `1`;
- dimension three: `660,1122,2314`;
- dimension four: `428,2348,3210`.

A direct finite acyclicity certificate orients each face-poset covering relation upwards except for the 428 matched covers, which are reversed. There are exactly 3432 covering relations; Kahn's topological-sort algorithm visits all 863 faces, leaving no directed cycle. Hence the matching is acyclic, and discrete Morse theory gives a CW model with one zero-cell, three three-cells, and three four-cells, and no other cells.

It remains essential to calculate attaching degrees: mixed-dimensional critical-cell counts alone do not imply the claimed wedge. Orient every simplicial face by increasing vertex index and use the integral incidence \(\partial[v_0,\ldots,v_d]=\sum_i(-1)^i[v_0,\ldots,\widehat v_i,\ldots,v_d]\). The exact gradient-path reduction of the boundary of the three critical four-simplices to the three critical three-simplices gives, in the mask orders just listed,
\[
\partial^{\mathrm{Morse}}_4=
\begin{pmatrix}0&0&0\\0&0&0\\0&0&0\end{pmatrix}.
\]
The supplied verifier computes this matrix over the **integers**, using the recurrence \(\rho(a)=-\sum_{c\ne a}[b:c][b:a]^{-1}\rho(c)\) when \(a\) is a matched lower face with paired upper face \(b\), with \(\rho\) the identity on critical faces and zero on matched upper faces. All incidences \([b:a]\) in a matched pair equal \(\pm1\), and acyclicity makes the recurrence finite. The attached critical three-cells have constant attaching maps since the two-skeleton is a point. Thus the three-skeleton is \(\bigvee^3S^3\). Because \(\pi_3(\bigvee^3S^3)\cong\mathbb Z^3\), the zero integral degree vector makes every four-cell attaching map nullhomotopic. Adding them produces precisely three further wedge summands \(S^4\), completing the proof.

## Verification
Run `python3 verify_morse.py` and `python3 verify_mod2.py` in the directory containing these files. Both require Python 3.10 or later and only the standard library. The first checks all 4095 nonempty vertex subsets, the 863 accepted faces, all 3432 face-poset covers, acyclicity of the prescribed matching, the critical cells, and the exact integral zero attaching matrix. Its final line is `INTEGRAL_HOMOTOPY_VERIFICATION_PASS`. The second uses a separate three-vertex-forbidden-subgraph model, independently computes faces, and performs mod-two Gaussian elimination on the original boundary matrices. It confirms boundary ranks \((11,55,137,163,62)\) and unreduced Betti numbers \((1,0,0,3,3,0)\), and ends with `INDEPENDENT_MOD2_VERIFICATION_PASS`.

The exact integral gradient calculation and topological-sort check, not the mod-two homology alone, support the homotopy statement. Both executable scripts and their actual output are supplied without external dependencies.

## Relationship to prior work
Taylan's original 2015 preprint develops matching trees for devoid complexes and computes the three-vertex-path-devoid complexes of forests as well as path- and cycle-based examples. The truncated tetrahedron contains triangles and induced hexagons, so those graph-family formulas do not imply this classification. Deshpande and Singh subsequently compute higher independence complexes for complete multipartite graphs, fully whiskered graphs, cycles, and perfect rooted trees; none is the present graph. Work on chordal graphs and trees likewise does not cover its induced six-cycles.

Known calculations for **ordinary** independence complexes, edge matching complexes, and graph-metric nerves of the truncated tetrahedron concern distinct simplicial complexes. No implication from any inspected result determines the integral \(\operatorname{Ind}_2(T)\) homotopy type. The present calculation demonstrates a mixed-dimensional sphere wedge in a canonical nonchordal, nonflag higher-independence example. This is a priority assessment relative to inspected evidence, not a claim of exhaustive global uniqueness.

## Limitations
The proof is a complete finite calculation for the twelve-vertex truncated tetrahedron; it does not provide a formula for truncations of arbitrary simplices, for higher independence parameters, or for equivariant homotopy. It proves a homotopy equivalence rather than a homeomorphism or simple-homotopy equivalence to the stated wedge. The displayed computations are exhaustive for this graph, but publication-priority searches cannot exclude all unindexed work. Independent mathematical validation has not been performed.

## References
1. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, first publicly submitted 27 January 2015, https://arxiv.org/abs/1501.06754 .
2. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, initial preprint 15 January 2020, https://arxiv.org/abs/2001.05448 .
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, 21 June 2021, https://arxiv.org/abs/2106.10863 .
4. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145, doi:10.1006/aima.1997.1650.
