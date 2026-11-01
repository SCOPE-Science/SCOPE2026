# Nine six-spheres in the triangle-free vertex complex of the Shrikhande graph

## Finding
Let \(S\) be the Shrikhande graph, and let \(\operatorname{CF}_3(S)\) be the simplicial complex of vertex subsets of \(S\) that contain no triangle. Then the ordinary geometric realization has integral homotopy type
\[
\boxed{|\operatorname{CF}_3(S)|\simeq \bigvee^{9}S^6.}
\]
In particular, \(\widetilde H_6(\operatorname{CF}_3(S);\mathbb Z)\cong\mathbb Z^9\), and all other reduced integral homology groups vanish. Although the complex has dimension eight and facets in three different dimensions, its homotopy type consists entirely of six-spheres.

## Assumptions and scope
The graph \(S\) has vertex set \(V=(\mathbb Z/4\mathbb Z)^2\), identified with the integers \(0,1,\ldots,15\) by the rule \((i,j)\mapsto 4i+j\). Distinct vertices \(u,v\) are adjacent precisely if
\[
v-u\in\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}\pmod 4.
\]
This is the usual sixteen-vertex Shrikhande graph, strongly regular with parameters \((16,6,2,2)\). It has exactly thirty-two distinct triangles. The simplicial complex \(\operatorname{CF}_3(S)\) has precisely the vertex subsets containing no one of those thirty-two triangles, together with the empty face. All homotopy and homology claims concern this finite abstract simplicial complex, with its usual geometric realization and integral coefficients.

## Proof
**Complete face enumeration.** Encode a vertex subset \(F\subseteq V\) by the sixteen-bit integer \(m(F)=\sum_{v\in F}2^v\). A nonempty subset is a face if and only if none of the thirty-two triangle masks is contained in its mask. Exhaustive enumeration of the exact range \(1\le m<2^{16}\) gives \(8{,}950\) nonempty faces. The face vector, indexed by dimensions zero through eight, is
\[
(16,120,528,1452,2496,2568,1424,330,16).
\]
An independent test examines all triples in each selected vertex set using the graph adjacency table and gives the same face membership decision for every one of the \(2^{16}-1\) possible nonempty masks. The maximal faces have sizes seven, eight and nine, with multiplicities \(32,186,16\), respectively.

**Acyclic discrete-Morse matching.** Start with the set of all nonempty faces unmatched. For \(v=0,1,\ldots,15\), in that order, pair each remaining face \(F\) not containing \(v\) to \(F\cup\{v\}\) if both are still unmatched, then remove both from consideration. This procedure produces precisely \(4{,}465\) disjoint face pairs. The unmatched cells are one zero-simplex, five five-simplices and fourteen six-simplices. Their bit masks are supplied in `certificate.json` and reproduced directly by `verify.py`.

A greedy face pairing is not automatically an acyclic Morse matching. Here acyclicity is established by constructing the entire directed Hasse graph: orient every unmatched codimension-one incidence downward and every matched incidence upward. The resulting directed graph has \(8{,}950\) nodes and exactly \(48{,}272\) arrows. An exhaustive topological sort visits all nodes, so there is no directed cycle. Forman's finite discrete-Morse theorem therefore gives a homotopy-equivalent CW complex with precisely the stated critical cells.

**Integral attaching degrees.** The resulting CW complex has one zero-cell, five five-cells and fourteen six-cells, and no other cells. Its five-skeleton is therefore a wedge of five five-spheres. The exact integral cellular Morse boundary from degree six to degree five is the \(5\)-by-\(14\) signed matrix \(B\) in `certificate.json`. The matrix is reconstructed by enumerating every gradient path with its incidence signs, not by taking a mod-two rank. More explicitly, if a five-simplex \(\sigma\) is paired upwards with a six-simplex \(U\), write \([U:\sigma]\in\{\pm1\}\) for its simplicial incidence. Its projection to critical five-chains satisfies the recursion
\[
P(\sigma)=-[U:\sigma]\!\sum_{\substack{\eta\subset U,\ |\eta|=6\\ \eta\ne\sigma}}[U:\eta]P(\eta).
\]
For a critical five-simplex its projection is the corresponding basis element, while a five-simplex paired downward with a four-simplex projects to zero. The boundary of a critical six-simplex is the signed sum of the projections of its five-dimensional facets. Acyclicity makes this recurrence finite.

The five columns of \(B\) at zero-based indices \(0,1,4,9,11\) form a square integer matrix with determinant \(+1\). Hence the attaching-degree map has a unimodular rank-five minor: all five five-cells can be cancelled against five six-cells by integral changes of cellular basis. Since \(\pi_5(\bigvee^5S^5)\cong\mathbb Z^5\), these degree vectors classify the six-cell attaching maps at the relevant dimension, and the basis changes can be realized by homotopy equivalences and cellular slides. Nine six-cells remain attached trivially to a point. This establishes the claimed wedge of nine six-spheres, rather than merely a statement about homology over a field.

## Verification
Run `python3 verify.py` with standard Python 3. No external libraries or files are required. The checker reconstructs the graph and its strongly regular parameters, all triangles, all faces by two membership tests, the full matching, and every directed Hasse incidence. It computes the integral Morse matrix by signed recursion and evaluates the exhibited unit minor by an exact integer determinant.

Independently of the Morse reduction, direct mod-two elimination on the original simplicial boundary matrices gives the ranks
\[
(15,105,423,1029,1467,1101,314,16)
\]
for differentials in degrees one through eight. This yields one reduced Betti number, equal to nine in degree six, and zero in the other degrees. These field calculations corroborate the integral homotopy proof but cannot by themselves certify it. A successful complete replay ends with `ALL_VERIFY_OK`.

## Relationship to prior work
Ghosh and Selvaraja introduce and study clique-free complexes and establish shellability under chordality and related hypotheses. Their theorem for chordal graphs does not apply to the Shrikhande graph (whose induced vertex neighborhoods are six-cycles), and the inspected primary manuscript does not give the above homotopy classification.

The sixteen-vertex rook graph \(R=K_4\square K_4\) shares the Shrikhande graph's strongly regular parameters. In \(R\), every triangle consists of three squares in one row or column; consequently \(\operatorname{CF}_3(R)\) is *exactly* the already studied two-matching complex \(M_2(K_{4,4})\), which has the previously established type \(\bigvee^{15}S^5\). That rook calculation is not claimed as new. The difference between the two clique-free homotopy types does not follow from their shared spectrum or strongly regular parameters.

A separate earlier computation gives the independence complexes \(\operatorname{CF}_2(S)\) and \(\operatorname{CF}_2(R)\), but their inclusion into the three-clique-free complexes does not determine the new homotopy type. Similarly, results about clique homology of strongly regular graphs concern the flag complex of the graph itself, not the complex forbidding triangles in induced vertex subsets. The specific Shrikhande calculation here is the new component of the comparison.

## Limitations
This is an exact finite homotopy classification for one canonical graph. It does not provide an infinite-family classification for Doob or other strongly regular graphs, an equivariant splitting under the automorphism group, or a shellability classification. Full homotopy equivalence is obtained by the explicit finite Morse certificate; numerical experiments alone would not suffice. Equivalent but unindexed published computations cannot be ruled out by search.

## References
1. Rakesh Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1, first publicly posted 2026-02-10, https://arxiv.org/abs/2602.09623.
2. *The two-matching complex of \(K_{4,4}\) is a wedge of fifteen five-spheres*, published mathematical research record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-two-matching-complex-of-k-4-4-is-a-wedge-of-fifteen-five-sph--915eed6b65e5.
3. *Independence complexes of the Shrikhande and \(4\times4\) rook graphs have different sphere-wedge homotopy types*, published mathematical research record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187.
4. Sebastian M. Cioabă and Mutasim Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328v1, 2026-06-25, https://arxiv.org/abs/2606.27328.
5. Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
