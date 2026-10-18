# Three five-spheres and twisted cubical symmetry in a clique-free complex

## Finding

Let \(Q_3\) have vertex set \(\mathbb F_2^3\) and edges joining vertices at Hamming distance one. Let \(C=L(Q_3)\), the cuboctahedral graph on the twelve cube edges, and let \(K=\mathrm{CF}_3(C)\), with a face for each set of vertices of \(C\) containing no triangle. Then
\[
K\simeq \bigvee^3 S^5.
\]
Consequently, \(\widetilde H_5(K;\mathbb Z)\cong\mathbb Z^3\), with all other reduced integral homology groups zero.

Let \(B_3=(C_2)^3\rtimes S_3\) act by affine coordinate flips and coordinate permutations of \(\mathbb F_2^3\). Write \(U\) for its signed three-dimensional coordinate representation and \(\varepsilon(g)=\operatorname{sgn}(p)\) when \(g(v)=p(v)+b\). The induced rational homology representation is
\[
\widetilde H_5(K;\mathbb Q)\cong\varepsilon\otimes U,
\qquad
\chi(g)=\operatorname{sgn}(p)\sum_{i:p(i)=i}(-1)^{b_i}.
\]
It is irreducible over \(\mathbb Q\), has no nonzero invariant vector, and is determined on all forty-eight automorphisms by this formula.

## Assumptions and scope

The graph \(Q_3\) is the ordinary three-dimensional cube, not a hypercube of variable dimension. Give its eight vertices the integer labels \(0,\ldots,7\), viewed as three-bit strings. The twelve cube edges are ordered lexicographically as

`[(0,1),(0,2),(0,4),(1,3),(1,5),(2,3),(2,6),(3,7),(4,5),(4,6),(5,7),(6,7)]`.

A vertex of \(C\) is one of these edges; two are adjacent precisely when the cube edges share an endpoint. A triangle of \(C\) consists of three pairwise incident edges in \(Q_3\). Because the cube has no three-cycle, any such three edges share a single common cube endpoint. Thus the forbidden triples are exactly the eight incident edge-stars. In particular
\[
\mathrm{CF}_3(L(Q_3))=M_2(Q_3),
\]
where \(M_2\) denotes the bounded-degree, or two-matching, complex in which every selected subgraph vertex has degree at most two.

The result concerns the integral homotopy type and the rational action of the specified cube automorphism group. No equivariant homotopy equivalence is asserted.

## Proof

**1. Exhaustive face model.** For the above edge ordering, identify every subset of edges with the mask \(s\in\{0,\ldots,4095\}\). Let \(t_v\) be the mask of the three edges at cube vertex \(v\). The subset \(s\) is a simplex exactly when \(s\mathbin{\&}t_v\ne t_v\) for every cube vertex. Exhausting all masks produces exactly 1699 faces *including the empty face*, with face counts for dimensions \(-1,0,\ldots,7\) equal to

`[1,12,66,212,423,516,352,108,9]`.

There are 49 facets: four of dimension five, 36 of dimension six, and nine of dimension seven. This confirms nonpurity, so sphere homology alone does not follow from the top face dimension.

**2. Exact acyclic matching.** On the augmented face poset, for each bit index \(i=0,\ldots,11\) in order, pair every remaining lower mask \(s\) not containing bit \(i\) with \(s+2^i\), if both masks are still present, and delete both from the available set. Within a bit phase visit lower masks in increasing numeric order. The process forms 847 pairs and leaves exactly the masks

`[598,888,1446,2710,3158]`.

Mask 598 is a four-simplex; each of the others is a five-simplex. For an exhaustive acyclicity certificate, orient all unmatched Hasse incidences downward and all matched incidences upward. The verifier constructs this complete directed graph, topologically sorts it, and visits all 1699 faces; no directed cycle exists. This is an acyclic algebraic/discrete Morse matching (including one pair with the empty face). The associated reduced Morse CW chain complex therefore has exactly one four-cell and four five-cells, in addition to the base point.

**3. Integral attaching degrees and homotopy.** Orient every simplex by increasing edge index and use the standard alternating signed boundary. Eliminate the 847 matched pairs in the induced acyclic order. The exact integral Morse boundary of five-cells with respective masks \(888,1446,2710,3158\) onto the four-cell with mask 598 is the row vector

\[
\partial^{\mathrm{Morse}}_5=(-1,\ 1,\ -1,\ -1).
\]

This is not a floating-point rank or a mod-two calculation: each nonzero entry is obtained by recursively substituting the signed boundary of the matched coface, as implemented in the standalone verifier. One entry is a unit, so an integral change of basis leaves exactly one degree-one attachment and three zero attachments. The four-skeleton is \(S^4\), and \(\pi_4(S^4)\cong\mathbb Z\) classifies the attaching maps by their degrees. The degree-one attachment kills that four-sphere; the other three five-cells form \(\bigvee^3 S^5\). This establishes the claimed integral **homotopy type**, rather than merely the homology.

**4. Symmetry representation.** Each cube automorphism is uniquely \(g(v)=p(v)+b\), with \(p\in S_3\), \(b\in\mathbb F_2^3\); the induced action permutes the twelve ordered edge labels. If a face \(S\) is preserved setwise, denote the sign of the induced permutation of its ordered vertices by \(\operatorname{sgn}(g\vert_S)\). The signed augmented simplicial Lefschetz formula gives
\[
\operatorname{tr}(g\mid\widetilde H_5(K;\mathbb Q))
=\sum_{S\in K}(-1)^{|S|}\operatorname{sgn}(g\vert_S),
\]
where the empty face contributes one; the sign is positive because the only reduced homology lies in odd degree five and the reduced alternating chain-trace has the opposite sign. The standalone verifier evaluates this integer formula for every one of the forty-eight group elements, directly from the face masks and edge permutations. Each trace agrees with
\[
\operatorname{sgn}(p)\sum_{i:p(i)=i}(-1)^{b_i}.
\]

This is precisely the character of \(\varepsilon\otimes U\): a coordinate flip acts on \(U\) by its signs and a coordinate permutation acts by its permutation matrix, with an additional factor \(\operatorname{sgn}(p)\). Character equality determines a rational representation for a finite group in characteristic zero. The three sign characters of the normal flip subgroup occurring in \(U\) are distinct and transitively permuted by \(S_3\), so \(U\), and hence its twist, is irreducible. Averaging the forty-eight character values gives zero, proving absence of invariant vectors.

## Verification

Run `python3 verify_cuboctahedral.py` in a standard Python installation (no third-party modules). The program independently checks the equivalence between forbidden line-graph triangles and cube stars; enumerates every mask and maximal face; enumerates and acyclicity-checks the entire augmented matching; computes the signed integral critical boundary; calculates ordinary mod-two simplicial boundary ranks without using the Morse reduction; and evaluates signed Lefschetz traces for every cube automorphism.

Expected checks include 1699 augmented simplices, 847 matched pairs, critical masks `[598,888,1446,2710,3158]`, Morse row `[-1,1,-1,-1]`, and mod-two Betti number three only in degree five. The character-value distribution is `{-3:1,-1:15,0:16,1:15,3:1}`. The test program prints `all exact tests: PASS` only when every assertion succeeds. See `verification_output.txt` for the packaged run output.

## Relationship to prior work

Ghosh and Selvaraja (2026) study this clique-free construction, establishing sufficient shellability conditions for diamond-free chordal graphs and for certain clique-attached graphs; the cuboctahedral graph contains an induced four-cycle and is not covered by their chordal theorem. Singh (2020) determines higher-matching homotopy types for specified complete and complete-bipartite graphs, not the cube. Vega (2019/2021) computes two-matching complexes of certain whiskered, wheel, and caterpillar graph families. Goyal, Shukla, and Singh (2020) study the *clique complex* of line graphs, in contrast to the *three-clique-free complex* here.

Related calculations for the ordinary matching complex of the cuboctahedral graph and for the two-matching complex of the complete bipartite graph on eight vertices describe different complexes. The latter graph contains the cube as a spanning subgraph, but the homotopy type of a full simplicial complex does not determine the type of its induced subcomplex. We did not identify an equivalent cube-specific integral classification or the full twisted homology character in the checked literature; absence from searched sources is not a proof of worldwide novelty.

## Limitations

The theorem concerns one specific cubical graph and does not establish a formula for higher-dimensional cubes or for all cubic graphs. The representation statement is rational and does not classify integral equivariant extensions, stable equivariant homotopy, or representations under any larger artificially assigned symmetry. The finite verification is exhaustive for this twelve-vertex simplicial complex only. An unindexed or differently named prior calculation remains possible; independent external review has not occurred.

## References

- R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1, first public 2026-02-10, https://arxiv.org/abs/2602.09623 .
- A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, https://arxiv.org/abs/2006.13632 .
- J. Vega, *2-Matching Complexes*, arXiv:1909.10406, https://arxiv.org/abs/1909.10406 .
- S. Goyal, S. Shukla, and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130, https://arxiv.org/abs/2009.12130 .
- M. Wachs, *Topology of matching, chessboard, and general bounded degree graph complexes*, *Algebra Universalis* **49** (2003), 345–385, DOI:10.1007/s00012-003-1825-1 (survey; bibliographic record and abstract inspected).
