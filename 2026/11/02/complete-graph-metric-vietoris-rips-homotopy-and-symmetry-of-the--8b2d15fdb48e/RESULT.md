# Complete graph-metric Vietoris–Rips homotopy and symmetry of the Desargues graph

## Finding
Let \(D\) be the 20-vertex Desargues graph, identified with the bipartite Kneser incidence graph \(H(5,2)\): its vertices are the two-element and three-element subsets of \([5]\), with adjacency precisely when a two-set is contained in a three-set. Distances are shortest-path distances in this graph. Write \(X_r=\operatorname{VR}_{\le r}(V(D))\), the flag complex on pairs at distance at most \(r\). For every real \(r\ge0\), its **complete integral homotopy filtration** is

\[
X_r\simeq
\begin{cases}
\bigvee^{19}S^0,&0\le r<1,\\
\bigvee^{11}S^1,&1\le r<2,\\
\bigvee^{19}S^2,&2\le r<3,\\
S^3,&3\le r<4,\\
S^9,&4\le r<5,\\
\mathrm{pt},&r\ge5.
\end{cases}
\]

The geometric automorphism group \(S_5\times C_2\), with \(S_5\) relabeling \([5]\) and central \(C_2\) complementing subsets, acts on every stage. Let \(W\) be the standard four-dimensional rational \(S_5\)-module, set \(A=\bigwedge^2 W\), \(B=\mathrm{sgn}\otimes S^{(3,2)}\) and \(C=\mathrm{sgn}\otimes W\), and let \(\epsilon\) be the nontrivial character of the complementing \(C_2\). The **complete nonzero reduced rational homology representations** are

\[
\begin{aligned}
\widetilde H_1(X_1;\mathbb Q)&\cong(A\boxtimes\mathbf1)\oplus(B\boxtimes\epsilon),\\
\widetilde H_2(X_2;\mathbb Q)&\cong((B\oplus C)\boxtimes\mathbf1)\oplus((A\oplus C)\boxtimes\epsilon),\\
\widetilde H_3(X_3;\mathbb Q)&\cong\mathrm{sgn}\boxtimes\mathbf1,\\
\widetilde H_9(X_4;\mathbb Q)&\cong\mathrm{sgn}\boxtimes\mathbf1.
\end{aligned}
\]

All other positive-degree reduced homology groups at these stages vanish, and the displayed integral sphere-wedge descriptions show that no torsion occurs. The positive-dimensional persistent homology consists of 11 degree-one bars from threshold 1 to 2, 19 degree-two bars from 2 to 3, one degree-three bar from 3 to 4, and one degree-nine bar from 4 to 5 (over every field). In degree zero there are 19 finite reduced bars from 0 to 1. All bars are of unit length.

For example, all positive rational homology of the full quotient \(X_r/(S_5\times C_2)\) vanishes. Under quotient by \(A_5\times C_2\), one rational class survives at each of thresholds 3 and 4, in the respective degrees 3 and 9.

## Assumptions and scope
Only the finite **vertex metric** of \(D=H(5,2)\) is considered, not all points of the geometric realization of its edges. The complex is inclusive: a nonempty vertex set is a simplex exactly if all pairwise graph distances are at most \(r\). Zero threshold gives twenty discrete vertices. The graph is connected, cubic, of diameter five, and has the complementing antipodal involution \(A\mapsto[5]\setminus A\). The natural \(S_5\times C_2\) action respects the metric and has order 240.

The representations in the finding refer to the corresponding nonzero degree at each integral threshold. In the representation formulas \(S^{(3,2)}\) is the five-dimensional Specht representation of \(S_5\) and \(\mathrm{sgn}\) is its sign character. No equivariant homotopy equivalences to the displayed sphere wedges are asserted.

## Proof
**Combinatorial stages.** Order the vertices lexicographically, with all ten two-sets followed by all ten three-sets. The exact graph is generated from the subset-containment rule. Breadth-first distances yield the distance profile \((1,3,6,6,3,1)\) from any vertex. At threshold 1 the complex is the original triangle-free graph, with 20 vertices and 30 edges, hence a wedge of eleven circles. At threshold 5 all edges are present and the complex is a simplex. At threshold 4 the only absent graph edges are the ten complementary pairs \(\{A,[5]\setminus A\}\); they form a perfect matching. Consequently \(X_4\) is the join of ten 0-spheres, the boundary of a ten-dimensional cross polytope, and is homeomorphic to \(S^9\).

**Exhaustive finite Morse certificates at the two intermediate thresholds.** The complete nonempty face vectors, indexed by simplex cardinality, are

\[
\begin{array}{c|rrrrrrr}
\text{threshold}&1&2&3&4&5&6&7\\\hline
2&20&90&120&30&0&0&0\\
3&20&150&540&1000&960&450&80.
\end{array}
\]

The accompanying `morse_certificate.json` encodes a matching for **every noncritical simplex** at thresholds 2 and 3. Each simplex is represented by the bit mask of its lexicographically numbered vertex set, and a matched pair gives masks for a codimension-one face and its coface. At threshold 2 there are 120 pairs, leaving precisely one critical vertex and nineteen critical triangles. At threshold 3 there are 1,599 pairs, leaving precisely one critical vertex and one critical tetrahedron. These counts exhaust all 260 and 3,200 nonempty simplices, respectively. The standalone `desargues_checker.py` regenerates *every* face from the defining graph, tests each matched covering relation and exclusive use of every face, orients each Hasse edge down except for reversed matched edges, and runs a complete directed-acyclicity test. Thus the matchings are bona fide acyclic discrete-Morse matchings, not heuristic or sampled collapses.

By the elementary discrete-Morse CW theorem, the resulting homotopy models have exactly the displayed critical cells. Because there are no one-cells at threshold 2, each of the nineteen two-cell attaching maps is constant; similarly the unique three-cell at threshold 3 attaches to a point. This proves the integral homotopy equivalences \(X_2\simeq\bigvee^{19}S^2\) and \(X_3\simeq S^3\). These are finite exhaustive proofs certified by explicit matching data and an independent validity checker.

**Symmetry representations.** A permutation \(g\in S_5\) and the complement involution act by literal vertex permutations of every face. For a face \(\sigma\) fixed setwise, its contribution to the simplicial Lefschetz number is \((-1)^{\dim\sigma}\) times the sign of the induced ordering permutation. Summing over the *complete* face set gives \(L_r(g)\). Because the complex is connected and has rational homology only in degree \(d\) at each positive threshold, its sole reduced character is \((-1)^d(L_r(g)-1)\).

For an explicit irreducible-character comparison, write \(w(g)=\#\operatorname{Fix}_{[5]}(g)-1\) for the standard character. Then

\[
\chi_A(g)=\tfrac12(w(g)^2-w(g^2)),\quad
\chi_B(g)=\mathrm{sgn}(g)\left(\tfrac12(w(g)^2+w(g^2))-1-w(g)\right),\quad
\chi_C(g)=\mathrm{sgn}(g)w(g).
\]

The checker verifies the Lefschetz character identities for **every one of the 240 elements**, for scales 1, 2 and 3. At scale 4 the cross-polytope top-homology character is the orientation determinant: \(g\in S_5\) permutes the ten unordered two-subsets with sign \(\mathrm{sgn}(g)^{\binom{3}{1}}=\mathrm{sgn}(g)\), and complementation reverses all ten axes, hence has orientation sign \((-1)^{10}=+1\). This gives the fourth character formula. Group averaging in characteristic zero gives the stated rational quotient consequences.

**Persistence.** At every integer threshold, reduced homology is concentrated in the one degree listed above. These degrees are distinct across successive thresholds. Therefore all positive-dimensional maps between different thresholds vanish, establishing the unit-length bar intervals, while connectivity gives the degree-zero bars. No unstated assumption about attaching maps is needed.

## Verification
Run from a directory containing both included standalone files:

```sh
python3 desargues_checker.py morse_certificate.json
```

The Python-standard-library-only checker independently reconstructs the 20-vertex graph and all 260 and 3,200 faces at the two nontrivial certificate stages. It validates both perfect Morse matchings by exhaustive Hasse-diagram cycle detection. It then verifies all 240 group actions and compares the actual fixed-face signed Lefschetz traces against the formulas above, including the signed orientation at the cross-polytope stage. Successful execution ends with the literal marker `DESARGUES_ALL_SCALES_MORSE_AND_240_CHARACTERS_OK`.

## Relationship to prior work
Saleh, Titz Mite and Witzel determine all Vietoris–Rips homotopy types of the five Platonic-solid vertex sets (first public version February 28, 2023; arXiv:2302.14388). In particular their dodecahedral graph, which also has 20 cubic vertices and diameter five, has a different sequence, with one degree-two sphere at threshold 2 and nine degree-three spheres at threshold 3. Their theorem does **not** cover the Desargues graph, which is the nonplanar Levi graph of the Desargues configuration rather than a Platonic-solid graph. Their paper also does not give the displayed full 240-element Desargues symmetry characters.

Adamaszek et al.'s work on Vietoris–Rips complexes of metric gluings gives general results for special graph gluings, but does not supply the concrete Desargues incidence-graph calculation. The published research record on a scale-three **Čech nerve** of the Desargues graph concerns a different filtered construction (and a different reported two-sphere rank), not the shortest-path flag Rips complexes proved here. Other published Rips calculations for cubic graphs likewise involve different underlying graphs. Existing graph-description references identify the Desargues graph and its group, not the new homotopy and equivariant barcode asserted above.

## Limitations
The claim is restricted to the 20-vertex Desargues graph with the *vertex shortest-path* metric; no generalization to all bipartite Kneser graphs, to continuous metric graphs, or to arbitrary scale-dependent equivariant homotopy types is claimed. The checker and explicit certificate establish the finite statements exactly, but no independent external audit has been performed. Bibliographic novelty is evaluated against the identified primary texts and indexed claims; unindexed equivalent results remain a residual risk.

## References
1. N. Saleh, T. Titz Mite and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1, February 28, 2023. https://arxiv.org/html/2302.14388v1
2. M. Adamaszek et al., *On Homotopy Types of Vietoris–Rips Complexes of Metric Gluings*, arXiv:1712.06224, initial public version December 2017; https://arxiv.org/html/1712.06224v5
3. E. W. Weisstein, *Desargues Graph*, MathWorld. https://mathworld.wolfram.com/DesarguesGraph.html
4. Forman's acyclic discrete-Morse matching theorem, as used in reference 1, Section 1.
