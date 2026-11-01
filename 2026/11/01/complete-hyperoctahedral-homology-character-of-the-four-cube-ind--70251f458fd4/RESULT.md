# Complete hyperoctahedral homology character of the four-cube independence complex

## Finding

Let \(Q_4\) be the graph on \(\mathbb F_2^4\) with an edge between words differing in exactly one coordinate, and let \(K=\operatorname{Ind}(Q_4)\). Its graph automorphism group is the signed-coordinate group \(G=\mathbb F_2^4\rtimes S_4\), of order \(384\). Write its elements as \(g_{\sigma,b}\), acting by
\[
(g_{\sigma,b}x)_{\sigma(i)}=x_i+b_i\pmod 2\qquad(1\le i\le4).
\]
Here \(b\in\mathbb F_2^4\); put \(f(\sigma)=|\{i:\sigma(i)=i\}|\). Then the **complete rational homology character** is
\[
\operatorname{tr}\left(g_{\sigma,b}\mid\widetilde H_3(K;\mathbb Q)\right)
=\operatorname{sgn}(\sigma)\left[f(\sigma)-1+
\sum_{\sigma(i)=i}(-1)^{\sum_{j\ne i}b_j}\right].
\]
All other reduced rational homology vanishes. More structurally, let \(U=\ker(\mathbb Q^{[4]}\xrightarrow{\sum}\mathbb Q)\), with coordinate permutations acting naturally and translations acting trivially. Let \(P_3\) have basis \(e_1,\ldots,e_4\) with action
\[
g_{\sigma,b}\,e_i=(-1)^{\sum_{j\ne i}b_j}\,e_{\sigma(i)}.
\]
The representation is
\[
\widetilde H_3(K;\mathbb Q)\cong (\operatorname{sgn}\circ\pi)\otimes(U\oplus P_3),
\]
where \(\pi:G\to S_4\) is the coordinate-permutation projection. In particular, \(\dim\widetilde H_3(K;\mathbb Q)=7\), and
\[
\dim\widetilde H_3(K;\mathbb Q)^{\mathbb F_2^4}=3,
\qquad \dim\widetilde H_3(K;\mathbb Q)^G=0.
\]
For the quotient spaces this implies \(\dim\widetilde H_3(|K|/\mathbb F_2^4;\mathbb Q)=3\) and \(\widetilde H_*(|K|/G;\mathbb Q)=0\).

## Assumptions and scope

The conclusion concerns precisely the graph-theoretic four-cube and the natural automorphism action, not larger binary hypercubes. An independent set is a vertex set with no Hamming-distance-one pair. The action on simplicial chains uses the orientation induced by increasing numeric order of binary words. All homology is reduced except where explicitly specified. The module decomposition is over \(\mathbb Q\); no integral-equivariant decomposition or equivariant homotopy equivalence is asserted.

The automorphism group has the indicated form: an automorphism can carry \(0\) to any vertex by a translation; after fixing \(0\), it must permute its four neighboring unit words, which uniquely determine all remaining words through shortest-path distance and the cube's common-neighbor structure. Conversely each signed-coordinate permutation is a graph automorphism.

## Proof

**Homology concentration by a complete acyclic matching.** Index the sixteen vertices by \(0,\ldots,15\). A face is a sixteen-bit mask \(s\); it is retained exactly when none of its selected vertices differ by one cube-coordinate bit. Exhausting all \(2^{16}\) masks produces \(743\) faces, including the empty face. The numbers of nonempty simplices in dimensions \(0,\ldots,7\) are \((16,88,208,228,128,56,16,2)\).

Start with the \(742\) nonempty faces unmatched. Successively use pivots \(v=0,1,\ldots,15\). At pivot \(v\), pair each remaining face \(s\) omitting \(v\) with \(s\cup\{v\}\), provided the latter remains a face not yet paired. The sixteen stage-pair counts are
\[
(176,134,10,4,5,5,13,4,0,3,4,3,3,1,1,1),
\]
which sum to \(367\). The eight unmatched masks are exactly
\[
(1,1680,2400,10370,17028,24600,33064,33096).
\]
One is a vertex and the other seven are three-dimensional simplices. Orient all \(2816\) codimension-one incidences downward, reversing precisely the \(367\) matched edges. An exhaustive topological-sort check visits all \(742\) vertices of this directed graph: it is acyclic. Consequently discrete Morse theory gives one zero-cell and seven three-cells and no other cells. Every three-cell attaches to the zero-skeleton by a constant map. Thus, integrally,
\[
K\simeq\bigvee^7S^3,
\]
so the indicated rational homology is the only nonzero reduced rational group. This calculation verifies the necessary nonequivariant premise without relying on the earlier homotopy record.

**Lefschetz character.** Fix \(g\in G\). The reduced simplicial Lefschetz number is the alternating sum of signed traces on the augmented simplicial chain groups. Since the only reduced homology is in dimension three,
\[
\operatorname{tr}(g\mid\widetilde H_3(K;\mathbb Q))=-\widetilde L(g).
\]
Every \(g\)-fixed face is a union of complete cycles of \(g\)'s permutation of cube vertices. Discard a vertex orbit when it contains adjacent cube vertices. Join two surviving orbits by an edge if any vertex in one is adjacent to any vertex in the other. Call this incompatibility graph \(H_g\). A fixed face corresponds precisely to an independent collection of these orbits. If it contains \(r\) selected orbits and \(q\) cube vertices, the orientation sign of \(g\) on the face is \((-1)^{q-r}\); its alternating chain weight is \((-1)^{q-1}\). Including the augmented empty face therefore gives
\[
\operatorname{tr}(g\mid\widetilde H_3(K;\mathbb Q))
=\sum_{J\in\operatorname{Ind}(H_g)}(-1)^{|J|}.
\]
This is a small, entirely finite independence-polynomial evaluation, with no appeal to a non-equivariant matching being equivariant.

**Exhaustive class comparison.** A signed permutation of four coordinates is specified by one of \(24\) permutations and one of \(16\) bit vectors. Its signed-cycle type is the multiset of pairs consisting of each coordinate-cycle length and parity of its flip bits; these give exactly twenty conjugacy types. Two independent algorithms attached to this result compute the trace for all \(384\) elements: one scans every fixed simplex with its actual orientation sign, and the other evaluates the incompatibility-orbit polynomial above. Both agree with
\[
\operatorname{sgn}(\sigma)\left[f(\sigma)-1+
\sum_{\sigma(i)=i}(-1)^{\sum_{j\ne i}b_j}\right]
\]
on **all \(384\) automorphisms**. The attached program constructs all \(384\) maps from the defining coordinate formula, checks every equality, and explicitly classifies the twenty types. This is an exhaustive finite proof of the displayed character, not extrapolation from selected examples.

**Representation identification.** The augmentation module \(U\) has permutation trace \(f(\sigma)-1\), and the signed three-coordinate module \(P_3\) has trace \(\sum_{\sigma(i)=i}(-1)^{\sum_{j\ne i}b_j}\). Tensoring both with the sign of \(\sigma\) therefore gives the verified full character. Equality of rational characters for finite groups implies isomorphism of rational representations (semisimplicity). Under the translation subgroup, \(U\) contributes three invariant dimensions. The four characters on \(P_3\) are the distinct nontrivial characters supported on the three-coordinate subsets; none is invariant. The full group acts on the translation-fixed summand as the sign-twisted standard \(S_4\)-module, which has no invariant vector. For any finite simplicial group action, barycentric subdivision and rational averaging identify rational homology of the quotient with the invariant part of the original rational homology. The quotient conclusions follow.

## Verification

Run `python3 verify_q4_equivariant.py` from a directory containing the attached standalone program. It requires only Python's standard library, reconstructs the complete face poset, all matching pairs, every Hasse incidence and the acyclicity ordering, and checks mod-two ranks of the original simplicial boundary matrices. It then computes all signed traces independently by fixed simplices and by vertex-orbit incompatibility graphs, checks the closed character expression for all group elements, and checks all translation-Fourier multiplicities. Expected final line: `VERIFY_OK`. The accompanying `verification_output.txt` records the actual execution and the twenty signed conjugacy classes with their sizes and traces. The class sizes sum to \(384\). The raw boundary ranks over \(\mathbb F_2\), in increasing positive chain degree, are \((15,73,135,86,42,14,2)\).

## Relationship to prior work

Bousquet-Mélou, Linusson and Nevo (2007) develop Morse methods for open and cylindrical square grids and discuss toroidal alternating-count questions; these results do not determine this full homology representation. Barmak (2010) provides general homotopy techniques for independence complexes, including triangle-free graphs and square-grid examples, without this cube-symmetry character. Jonsson (2010) constructs cross-cycles for periodic grids; the available abstract describes degrees and existence of classes rather than a complete action of all cube automorphisms. A separate published exact-object research record establishes the nonequivariant seven-sphere homotopy type of \(\operatorname{Ind}(Q_4)\), but explicitly does not claim an equivariant decomposition. The new contribution is the complete \(384\)-element character and natural representation splitting, not the previously available nonequivariant Betti number or homotopy type.

## Limitations

The theorem is restricted to the sixteen-vertex four-cube. It determines rational representations and rational homology of symmetry quotients, not their integral homology or homotopy types, and not an equivariant cell decomposition. It assumes the standard unweighted graph-automorphism action, not arbitrary permutations of cube vertices. An equivalent treatment outside the indexed literature remains possible; the full text of Jonsson's directly related periodic-grid paper could not be obtained in this inspection, so its overlap risk remains explicitly unresolved but no known implication supplies the displayed full character. Computational verification is complete for the finite stated domain, but no independent external audit has been performed.

## References

1. M. Bousquet-Mélou, S. Linusson and E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890, first publicly posted 2007-01-30. https://arxiv.org/abs/math/0701890
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418, first publicly posted 2010-07-02. https://arxiv.org/abs/1007.0418
3. J. Jonsson, *Certain homology cycles of the independence complex of grids*, Discrete & Computational Geometry 43 (2010), 927–950, DOI:10.1007/s00454-009-9224-9. https://doi.org/10.1007/s00454-009-9224-9
4. *The four-cube independence complex is a wedge of seven three-spheres*, publicly indexed exact-object result, 2026-10-11. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-four-cube-independence-complex-is-a-wedge-of-seven-three-sph--9947aaad144c
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
