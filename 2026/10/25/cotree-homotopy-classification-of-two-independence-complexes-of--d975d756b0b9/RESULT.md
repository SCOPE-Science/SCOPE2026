# Cotree homotopy classification of two-independence complexes of cographs

## Finding

For every finite nonempty cograph \(G\), the complex \(\operatorname{Ind}_2(G)\) is homotopy equivalent to a wedge of positive-dimensional spheres, or is contractible. Its **entire** homotopy type is determined by an integer polynomial computed along any union/join cotree. Let
\[
P_G(t)=\sum_{d\geq1}\widetilde\beta_d(\operatorname{Ind}_2(G);\mathbb Z)t^d,\qquad m(G)=|V(G)|.
\]
For the graph with one vertex, \(P_G=0\). For any two nonempty cographs with disjoint vertices,
\[
\begin{aligned}
P_{G_1\sqcup G_2}(t)&=tP_{G_1}(t)P_{G_2}(t),\\
P_{G_1\vee G_2}(t)&=P_{G_1}(t)+P_{G_2}(t)
                   +(m(G_1)m(G_2)-1)t.
\end{aligned}
\]
The coefficient of \(t^d\) is the multiplicity of \(S^d\) in the resulting wedge. There is no reduced integral homology outside these dimensions, and there is no integral torsion. The zero polynomial denotes a contractible complex.

## Assumptions and scope

All graphs are finite, nonempty and simple. A **cograph** is a graph with no induced four-vertex path; equivalently, it is generated from single vertices by disjoint union and graph join. The graph join \(G_1\vee G_2\) adds every edge between the disjoint vertex sets of \(G_1\) and \(G_2\). The simplices of \(\operatorname{Ind}_2(G)\) are exactly those vertex subsets whose **induced connected components** have cardinality at most two. In particular, an induced two-vertex edge is allowed, while a connected induced three-vertex set is not. This index convention agrees with Deshpande–Singh [2]; in Deshpande–Roy–Sawant [3], whose index counts the size of the *forbidden* connected subset, the same complex is called \(\operatorname{Ind}_3(G)\). Throughout, \(\widetilde\beta_d\) denotes integral reduced homology rank, not a dimension over a fixed finite field.

## Proof

**1. The union operation.** If \(G=G_1\sqcup G_2\), then each connected component of every induced subgraph lies wholly in one summand. Thus a vertex set is admissible precisely when its two intersections are admissible. Hence there is an equality of abstract simplicial complexes
\[
\operatorname{Ind}_2(G_1\sqcup G_2)
 =\operatorname{Ind}_2(G_1)*\operatorname{Ind}_2(G_2),
\]
where the star denotes simplicial join. For nonempty connected finite CW complexes, the ordinary topological join is homotopy equivalent to the reduced suspension of their smash product. Consequently, the join of wedges of spheres has one sphere of dimension \(d+e+1\) for each ordered choice of an \(S^d\) summand and an \(S^e\) summand. If either factor is contractible, its join with any nonempty space is contractible. This proves the polynomial product formula whenever the induction hypothesis holds.

**2. The graph-join operation.** Put \(A=\operatorname{Ind}_2(G_1)\) and \(B=\operatorname{Ind}_2(G_2)\). A subset meeting both vertex parts in a total of at least three vertices induces a connected subgraph of order at least three: two vertices in one part and one in the other are connected through the cross edges, and any additional vertices attach to this connected triple. Therefore the only mixed simplices in \(\operatorname{Ind}_2(G_1\vee G_2)\) are the \(m(G_1)m(G_2)\) individual cross edges. Every pair of vertices, adjacent or not, is a face of \(\operatorname{Ind}_2(H)\) for any graph \(H\), because an induced two-vertex subgraph has component sizes at most two. Thus both \(A\) and \(B\) are path-connected (including the singleton case). As a topological realization, the graph-join complex is obtained from the disjoint union \(|A|\sqcup|B|\) by attaching exactly \(m(G_1)m(G_2)\) one-cells with endpoints in the two connected pieces. Choose one such one-cell as a connecting tree edge, and contract chosen paths within the pieces to basepoints for the remaining cross edges. The standard graph-of-spaces edge-attachment lemma yields
\[
\operatorname{Ind}_2(G_1\vee G_2)
\simeq |A|\vee |B|\vee
\bigvee^{m(G_1)m(G_2)-1}S^1.
\]
This establishes the additive polynomial recurrence, including the boundary case when the product of vertex counts is one.

**3. Induction on a cotree.** For a one-vertex graph, \(\operatorname{Ind}_2(K_1)\) is a point. The preceding two steps preserve the class of spaces homotopy equivalent to wedges of positive-dimensional spheres or a point. Every finite cograph admits a finite binary cotree whose leaves are single vertices and whose internal nodes are disjoint unions or graph joins [1,3]. Induction on that cotree proves both formulas and the full integral homotopy classification. As they compute the actual reduced integral homology of the same complex, the resulting polynomial is independent of which valid cotree is used.

**4. Mixed-dimensional example.** Since \(\operatorname{Ind}_2(K_3)\) is the boundary triangle \(S^1\), the union of two triangles has complex \(S^1*S^1\simeq S^3\). Joining that six-vertex graph to a further \(K_3\) adds \(6\cdot3-1=17\) new circles, in addition to the circle already present from the second \(K_3\). Consequently
\[
\operatorname{Ind}_2((K_3\sqcup K_3)\vee K_3)
\simeq S^3\vee\bigvee^{18}S^1,
\]
showing that a natural cograph can have nonzero reduced homology in separated degrees.

## Verification

The proof above establishes the assertion for all finite cographs and does not rely on enumeration. A separate direct face-enumeration and mod-two boundary-reduction program (`verify_cograph_ind2.py`) generated 240 independently assembled cotrees with one through ten vertices, computed the homology of each corresponding complex, and compared the result with the cotree polynomial. It also checked the nine-vertex mixed-dimensional example. All 241 checks agreed. These finite checks are tests of the definitions and recurrence only, not substitutes for the topological proof. Reproduce with `python3 verify_cograph_ind2.py` under Python 3 using only the standard library.

## Relationship to prior work

Mamun, Nalikka and Ramos [1] prove a finite-generation theorem for the homology of arbitrary vertex-monotone graph complexes of cographs (Section 4.2), and explicitly describe simpler cotree behavior for the ordinary independence complex (Section 2.3). That finite-generation statement neither determines the homotopy type of this two-independence complex nor yields the displayed integral Betti polynomial. Deshpande and Singh [2, Theorem 3.5] calculate higher independence complexes of complete multipartite graphs, a proper subclass of cographs. Deshpande, Roy and Sawant [3, Theorem 4.7] give a conditional vertex-decomposability criterion for the **Alexander dual** of the higher independence complex on cographs, rather than the direct homotopy classification here; account for their shifted index convention above. The proof here uses only the special fact that mixed allowed faces in a graph join have size at most two. Published overlap searches did not identify this full cotree formula; they cannot establish exhaustive novelty.

## Limitations

The recurrence is specific to the component-size bound two. At higher bounds, mixed faces can have dimension at least two and the graph-join argument no longer applies. The result proves no shellability or vertex-decomposability of the complex itself; sphere-wedge homotopy alone does not imply either property. The stated polynomial records homotopy multiplicities, not canonical bases or group actions. Novelty is assessed against the inspected literature and available mathematical records; an unlocated equivalent theorem remains possible.

## References

1. A. Mamun, J. Nalikka and E. Ramos, *Universality in the algebra and topology of cographs*, arXiv:2609.04554v1, first public 2026-09-03; especially Sections 2.3 and 4.2. https://arxiv.org/html/2609.04554v1
2. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448v1, first public 2020-01-15, Theorem 3.5 (read via v2). https://arxiv.org/html/2001.05448v2
3. P. Deshpande, A. Roy and R. Sawant, *The complex of \(r\)-co-connected subgraphs, chordality and Fröberg's theorem*, arXiv:2510.25710v1, first public 2025-10-29, Theorem 4.7 (read via v2). https://arxiv.org/html/2510.25710v2
