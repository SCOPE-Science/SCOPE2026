# Equivariant integral homotopy of the Franklin two-independence complex

## Finding

Let \(F\) be the twelve-vertex Franklin graph with the labeled LCF model specified below, and let \(X=\operatorname{Ind}_2(F)\) be the simplicial complex of induced vertex subsets whose connected components have at most two vertices. There is an integral homotopy equivalence

\[
|X|\simeq \bigvee^{5}S^{4}.
\]

The natural action of the complete automorphism group \(\operatorname{Aut}(F)\), of order \(48\), on \(H_4(X;\mathbb Q)\) has the following **complete** character distribution. Here the cycle type is the cycle partition on the twelve graph vertices; rows with the same cycle type but different character values are distinguished by their multiplicities.

| Vertex cycle type | Trace on \(H_4(X;\mathbb Q)\) | Number of automorphisms |
|:--|--:|--:|
| \(1^{12}\) | \(5\) | \(1\) |
| \(1^8 2^2\) | \(-3\) | \(3\) |
| \(1^4 2^4\) | \(1\) | \(3\) |
| \(2^6\) | \(-1\) | \(12\) |
| \(2^6\) | \(1\) | \(1\) |
| \(2^2 4^2\) | \(1\) | \(12\) |
| \(3^4\) | \(-1\) | \(8\) |
| \(6^2\) | \(1\) | \(8\) |

Among the automorphisms of cycle type \(2^6\), the unique trace-\(1\) element is the central half-turn \(i\mapsto i+6\); the other twelve have trace \(-1\). Thus the table, together with this explicit exception, assigns a trace to every graph automorphism.

The total character sum is zero. Consequently,

\[
\widetilde H_j\bigl(|X|/\operatorname{Aut}(F);\mathbb Q\bigr)=0
\quad\text{for every integer }j.
\]

This is a rational-homology assertion about the quotient; it does not assert that the quotient is contractible.

## Assumptions and scope

The vertices of \(F\) are \(\mathbb Z/12\mathbb Z\). Include every cyclic edge \(\{i,i+1\}\), and for each even \(i\) include the chord \(\{i,i+5\}\), with arithmetic modulo \(12\). Equivalently, the LCF word is \([5,-5]\) repeated six times. This is a cubic graph with \(12\) vertices and \(18\) edges. All faces of \(X\) are **vertex subsets**, not matchings of graph edges. A subset is a face if and only if every vertex of its induced graph has degree at most one.

All homology and attaching degrees in the homotopy statement are integral. For the automorphism character and quotient, coefficients are rational. No assertion is made for graphs other than the fixed labeled Franklin graph.

## Proof

**Face model.** Represent each subset by its twelve-bit mask \(m\). An exact exhaustive check using both induced-degree and induced-component predicates returns \(723\) faces including the empty face, with numbers in dimensions \(-1,0,1,2,3,4,5\) respectively

\[
(1,12,66,184,264,168,28).
\]

**Discrete-Morse reduction.** Starting with the face family, successively consider the vertices \(0,1,\ldots,11\). At a vertex \(v\), pair every two still-unmatched faces \(\sigma\) and \(\sigma\cup\{v\}\) for which \(v\notin\sigma\). This gives \(357\) pairs on the augmented face poset, including the pair between the empty face and \(\{0\}\). On the ordinary nonempty face poset, discard this augmented pair and take \(\{0\}\) as a critical zero-cell. The remaining \(356\) pairs are acyclic: the complete directed Hasse diagram has \(2748\) cover incidences, and the executable topological-sort check visits every nonempty face without a directed cycle.

The other critical faces are precisely the three-dimensional masks \(1066,2570\) and the four-dimensional masks \(1380,1698,2356,2388,2480,2706,2724\). Thus the ordinary Morse CW model has one zero-cell, two three-cells and seven four-cells, with no cells in dimensions one or two.

**Exact integral attachment calculation.** Orient every simplex by its increasing vertex sequence. Resolve matched lower faces through the signed boundary of their matched upper faces, recursively along the verified acyclic matching. In the displayed order of critical masks, the resulting integer Morse differential from the seven four-cells to the two three-cells is

\[
\partial^{\mathrm{Morse}}_4=
\begin{pmatrix}
1&1&1&0&0&0&-1\\
0&0&-1&-1&0&-1&1
\end{pmatrix}.
\]

Columns one and four have determinant \(-1\). The three-skeleton of the CW model is a wedge of two three-spheres; by the Hurewicz isomorphism, the homotopy class of each four-cell attaching map is completely determined by its two integral degrees. The unit minor permits two integral cellular cancellations, after which the five remaining four-cells attach trivially to a point. This proves \(|X|\simeq\bigvee^5 S^4\) and also the absence of integral torsion.

**Symmetry.** Exhaustive adjacency-preserving backtracking finds all \(48\) graph automorphisms. For any automorphism \(g\), the signed simplicial-chain trace is computed by summing over faces fixed setwise, with the sign of the induced permutation of their ordered vertices. Because all reduced rational homology is in degree four, the reduced Lefschetz identity gives

\[
\operatorname{tr}\bigl(g\mid\widetilde H_4(X;\mathbb Q)\bigr)
=\sum_{\substack{\sigma\in X\\g\sigma=\sigma}}
(-1)^{|\sigma|-1}\operatorname{sgn}(g\mid\sigma).
\]

The empty face contributes \(-1\). Evaluating this integer formula on each of the exhaustive \(48\) automorphisms yields the character table above. Its total trace is \(0\), so the invariant subspace in \(H_4(X;\mathbb Q)\) is zero. Averaging rational simplicial chains after barycentric subdivision identifies rational quotient homology with invariant rational homology, proving the final assertion.

## Verification

Run `python3 verify_franklin.py` using Python 3 and its standard library; a full expected output appears in `verification_output.json`. The checker independently implements the face condition in two ways, constructs the matching, verifies acyclicity, computes signed integral Morse differentials, checks ordinary homology over the fields of characteristics \(2,3,5\), exhaustively enumerates automorphisms, and computes each signed fixed-face character value. It asserts the displayed integral matrix and the entire eight-row character distribution. The final success marker is `FRANKLIN_INDEPENDENCE2_EQUIVARIANT_OK`.

## Relationship to prior work

Deshpande and Singh (first public arXiv version January 15, 2020) determine homotopy types of higher-independence complexes for complete multipartite, fully whiskered, path, cycle and perfect tree families. Deshpande, Shukla and Singh establish general connectivity bounds and a wedge-of-spheres result for chordal graphs. Abdelmalek and collaborators study shellability and vertex decomposability for chordal families. The Franklin graph is a nonchordal cubic graph with a four-cycle, no leaves, and none of those specific family hypotheses; none of these statements supplies its exact two-independence homotopy type or complete automorphism character. Calculations of the *ordinary matching complex* of the Franklin graph concern simplices of **edges**, so are different from this vertex-subset complex.

## Limitations

This is a finite exact classification, not an all-graph theorem. The Morse CW equivalence is not claimed to respect the graph automorphism group; the character is calculated separately on the original simplicial chains. The quotient's rational acyclicity does not determine its integral homology, fundamental group or homotopy type. An unindexed equivalent earlier calculation cannot be ruled out by literature searches, and no independent mathematical audit has yet been performed.

## References

1. Priyavrat Deshpande and Anurag Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, first posted January 15, 2020. https://arxiv.org/abs/2001.05448
2. Priyavrat Deshpande, Samir Shukla and Anurag Singh, *Distance \(r\)-Domination Number and \(r\)-Independence Complexes of Graphs*, arXiv:2001.06775, first posted January 19, 2020. https://arxiv.org/abs/2001.06775
3. Fred M. Abdelmalek, Priyavrat Deshpande, Shuchita Goyal, Amit Roy and Anurag Singh, *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863, first posted June 21, 2021. https://arxiv.org/abs/2106.10863
4. *Franklin graph* and *LCF notation*, standard graph references for the labeled cubic graph and its automorphisms. https://en.wikipedia.org/wiki/Franklin_graph ; https://en.wikipedia.org/wiki/LCF_notation
