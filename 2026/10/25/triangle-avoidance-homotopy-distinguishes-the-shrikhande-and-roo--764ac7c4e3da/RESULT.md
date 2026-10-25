# Triangle-avoidance homotopy distinguishes the Shrikhande and rook graphs

## Finding
Let \(\mathrm{Sh}\) denote the Shrikhande graph and \(R\) the four-by-four rook graph. For any finite simple graph \(G\), define the **triangle-avoidance complex**
\[
\mathcal D_{\triangle}(G)=\{A\subseteq V(G): G[A]\text{ contains no triangle}\}.
\]
There are integral homotopy equivalences
\[
\boxed{\mathcal D_{\triangle}(\mathrm{Sh})\simeq\bigvee^{9}S^{6}},
\qquad
\boxed{\mathcal D_{\triangle}(R)\simeq\bigvee^{15}S^{5}}.
\]
Both graphs are strongly regular with parameters \((16,6,2,2)\); each has exactly \(32\) triangles. Nevertheless, their triangle-avoidance complexes have nonzero reduced integral homology in **different degrees**. The rook-graph result is independently known as the two-matching complex of \(K_{4,4}\); the new classification here is the Shrikhande case and the resulting comparison.

## Assumptions and scope
All graphs are finite, undirected, and simple. Vertices of each graph are the sixteen ordered pairs \((i,j)\in(\mathbb Z/4\mathbb Z)^2\), labeled by the integer \(4i+j\) with \(0\leq i,j<4\). In \(R\), distinct pairs are adjacent when they share a coordinate. In \(\mathrm{Sh}\), distinct pairs are adjacent when their difference lies in
\[
\{(\pm1,0),(0,\pm1),(\pm1,\pm1)\},
\]
where the signs in the last pair are taken **together**, so the latter contributes \((1,1)\) and \((-1,-1)\), not the other two diagonals. All coordinates are reduced modulo four. The empty set is a face of each simplicial complex. Homotopy equivalence is meant for the geometric realization, with integral coefficients in homology.

## Proof
The attached `verify.py` is an executable finite proof certificate. It does not need external data or libraries. Its two separate face predicates check all \(2^{16}=65{,}536\) point subsets; the predicates agree for every subset. It also directly verifies all graph adjacencies and the parameter condition that each pair of distinct vertices has exactly two common neighbors. Every graph vertex has six neighbors; every graph has 48 edges and 32 triangles.

For each complex, let \(F\) initially be its complete face set, **including** the empty face. Process the coordinates in one of the following explicit vertex orders. At vertex \(v\), pair every currently unpaired \(\sigma\in F\) with \(\sigma\cup\{v\}\), whenever both faces exist and \(v\notin\sigma\). Remove both faces from the unmatched set before advancing. These are elementary codimension-one face-poset matches.

The order for \(R\), with vertices specified by their integer labels, is `12,14,10,11,8,6,1,3,5,15,0,13,4,2,7,9`. The order for \(\mathrm{Sh}\) is `4,2,7,11,9,12,1,6,13,10,5,0,15,14,3,8`. Each is a permutation of all sixteen vertices.

The complete enumeration gives \(7{,}343\) faces for \(R\), including the empty set. Exactly \(3{,}664\) pairs are matched, leaving fifteen critical faces, all of dimension five. For \(\mathrm{Sh}\), there are \(8{,}951\) faces, \(4{,}471\) matched pairs, and nine critical faces, all of dimension six. In each augmented matching, the empty face is paired with a singleton.

To verify acyclicity **globally** rather than infer it from the number of pairs, orient every codimension-one Hasse incidence downward, except for matched incidences, which are oriented upward. An exhaustive topological sort visits every face. It checks all \(37{,}744\) incidences for \(R\) and all \(48{,}288\) incidences for \(\mathrm{Sh}\) without finding a directed cycle.

Now remove the pairing involving the empty face and restrict the matching to ordinary nonempty simplices. Acyclicity persists on this subposet. This leaves precisely one critical vertex, together with fifteen critical five-simplices for \(R\), or nine critical six-simplices for \(\mathrm{Sh}\). Forman's discrete Morse theorem produces a CW model with exactly those cells. Because there are no positive-dimensional cells below the single critical dimension, every attaching map is constant up to homotopy. The resulting CW complexes are, respectively, a wedge of fifteen five-spheres and a wedge of nine six-spheres. This proves both integral homotopy equivalences, not just homology ranks.

## Verification
Run `python3 verify.py` in the extracted directory. The only dependency is Python's standard library. All masks from zero to \(2^{16}-1\) are tested, every forbidden triangle is independently enumerated, and every face-poset cover relation is oriented and included in the acyclicity check. Separate full augmented simplicial boundary reductions over \(\mathbb F_2\) return reduced Betti vectors concentrated in degree five with rank fifteen for \(R\), and degree six with rank nine for \(\mathrm{Sh}\). The program prints `VERIFY_OK` on success. Actual recorded output is included as `verify_output.txt`.

The nonempty simplex counts by dimension are:

| Dimension | \(R\) | \(\mathrm{Sh}\) |
|---|---:|---:|
| 0 | 16 | 16 |
| 1 | 120 | 120 |
| 2 | 528 | 528 |
| 3 | 1,428 | 1,452 |
| 4 | 2,304 | 2,496 |
| 5 | 2,040 | 2,568 |
| 6 | 816 | 1,424 |
| 7 | 90 | 330 |
| 8 | 0 | 16 |

## Relationship to prior work
The construction is a special case of the **devoid complex** of a graph with forbidden pattern \(K_3\), as defined and studied by Taylan (arXiv:1501.06754, first submitted January 27, 2015). The inspected article proves homotopy calculations for paths, cycles, and certain forests, but gives no classification of the Shrikhande triangle-avoidance complex.

For the rook graph, forbidden triangles are precisely three selected squares in a row or a column. Thus \(\mathcal D_{\triangle}(R)\) is exactly the generalized chessboard complex \(\Delta_{4,4}^{2,2}\) of Jojić, Vrećica, and Živaljević (arXiv:1412.0386, first submitted December 1, 2014), or equivalently the two-matching complex \(M_2(K_{4,4})\). The previously published record *The two-matching complex of \(K_{4,4}\) is a wedge of fifteen five-spheres* (published-finding corpus record `915eed6b65e5`) states that same rook homotopy equivalence. It is **prior coverage**, not claimed as a new rook result.

Other published comparisons calculate ordinary independence complexes, Čech complexes, or neighborhood complexes of the Shrikhande and rook graphs. Their face conditions are not the triangle-avoidance rule, and their statements do not imply the present Shrikhande result. The substantive new topological fact is \(\mathcal D_{\triangle}(\mathrm{Sh})\simeq\bigvee^9S^6\), which makes the dimension-separated pair comparison possible.

## Limitations
This is a finite, exact calculation for two specified sixteen-vertex graphs; it is not a classification of all strongly regular graphs. The programs prove integral homotopy type through an explicit acyclic discrete-Morse matching; modular homology calculations are independent corroboration, not a substitute for the homotopy proof. Searches and direct examinations of relevant accessible sources found no result covering the Shrikhande claim, but unindexed equivalent prior work cannot be categorically excluded. Independent scientific validation has not been performed.

## References
- D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754 (first public version 2015-01-27), https://arxiv.org/abs/1501.06754.
- D. Jojić, S. T. Vrećica, and R. T. Živaljević, *Multiple chessboard complexes and the colored Tverberg problem*, arXiv:1412.0386 (first public version 2014-12-01), https://arxiv.org/abs/1412.0386.
- D. B. Karaguezian, V. Reiner, and M. L. Wachs, *Matching complexes, bounded degree graph complexes, and weight spaces of GL-complexes*, Journal of Algebra 239 (2001), 77–92, DOI:10.1006/jabr.2000.8654.
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, DOI:10.1006/aima.1997.1650.
- Published published-finding corpus record `915eed6b65e5`, *The two-matching complex of \(K_{4,4}\) is a wedge of fifteen five-spheres* (previously established rook-case classification; compared using its indexed title and summary).
