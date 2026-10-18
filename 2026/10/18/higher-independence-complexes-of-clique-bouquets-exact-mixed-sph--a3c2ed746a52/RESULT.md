# Higher-independence complexes of clique bouquets: exact mixed sphere wedges and integral symmetries

## Finding
Let \(r\ge3\), \(n\ge2\), and \(m_1,\ldots,m_n\ge1\) be integers. Write \(N=\sum_{i=1}^{n}m_i\), and let \(G=K_1\vee(K_{m_1}\sqcup\cdots\sqcup K_{m_n})\), a connected clique bouquet with a unique central universal vertex. Then
\[
\operatorname{Ind}_r(G)\simeq
\bigvee^{\binom{N-1}{r-1}}S^{r-1}\;\vee\;
\bigvee^{\prod_{i=1}^{n}\binom{m_i-1}{r}}S^{nr-1}.
\]
The symbol \(\operatorname{Ind}_r(G)\) denotes the complex of vertex sets each of whose induced connected components has size at most \(r\). Interpret \(\binom{a}{b}=0\) for integers \(0\le a<b\) and an empty sphere wedge as a point. This gives a full integral homotopy type, including contractible cases. The two potentially nonzero reduced homology groups are free abelian, of exactly the displayed ranks.

Let \(A_T=\ker(\varepsilon:\mathbb Z^T\to\mathbb Z)\), where \(\varepsilon\) sums coefficients on a finite set \(T\). For the automorphism group preserving the clique blocks (including permutations of equal-sized blocks), the natural integral modules are
\[
\widetilde H_{r-1}(\operatorname{Ind}_r(G);\mathbb Z)
\cong\bigwedge^{r-1}A_{[N]},\qquad
\widetilde H_{nr-1}(\operatorname{Ind}_r(G);\mathbb Z)
\cong\bigotimes_{i=1}^{n}\bigwedge^{r}A_{[m_i]}.
\]
Internal block permutations act through the corresponding augmentation lattices. Exchanging two equal-size blocks acts by interchanging the tensor factors with Koszul sign \((-1)^r\). Since \(n\ge2\), the universal central vertex is structurally distinguished and this is the full graph automorphism action. If a displayed rank is zero, its module is zero.

In particular, for \(r=3\) with two four-vertex blades, \(\operatorname{Ind}_3(K_1\vee(K_4\sqcup K_4))\simeq\bigvee^{21}S^2\vee S^5\); for \(r=4\) with two five-vertex blades the homotopy type is \(\bigvee^{84}S^3\vee S^7\). These are examples, not assumptions or separate new claims.

## Assumptions and scope
The graph has one central vertex \(o\), disjoint vertex blocks \(V_i\) of respective sizes \(m_i\ge1\), all edges inside each \(V_i\), and all edges from \(o\) to every other vertex; no edges join distinct \(V_i\). No external maximality, homogeneity or genericity hypothesis is used. The parameter \(r\) is an integer at least three. All homotopy and homology assertions are integral and non-equivariant unless an integral module is explicitly stated. Reduced simplicial homology uses its standard augmented chain complex. The complete \(r=1,2\) classifications are not part of the scientific novelty asserted here.

## Proof
**Exact vertex decomposition.** For a finite set \(T\), denote by \(\operatorname{Sk}_{k}(T)\) the complex of subsets of \(T\) of size at most \(k+1\). Set \(J=\bigast_{i=1}^{n}\operatorname{Sk}_{r-1}(V_i)\) and \(L=\operatorname{Sk}_{r-2}(V_1\sqcup\cdots\sqcup V_n)\). When the center \(o\) is absent, induced connected components lie inside individual cliques and hence a face is exactly a face of \(J\). When \(o\) is present, all selected vertices form one connected component; this selection is allowed precisely when it has at most \(r\) vertices, or at most \(r-1\) outside \(o\). It follows **as an equality of face sets** that
\[
\operatorname{Ind}_r(G)=J\cup_{L}(o*L),\qquad L\subseteq J.
\]
The second term is the simplicial cone on \(L\); in particular the union is a homotopy cofiber of \(L\hookrightarrow J\).

**Skeleton lemma.** For any \(M\ge1\), the complex of subsets of an \(M\)-element set having at most \(k+1\) elements, with \(k\ge0\), is contractible when \(M\le k+1\). Otherwise it has the homotopy type of a wedge of \(\binom{M-1}{k+1}\) copies of \(S^k\). One explicit proof orders the vertices, and pairs each nonempty simplex missing the first vertex with its union with that vertex, provided the union is still a face. The residual critical faces are the \((k+1)\)-element subsets of the last \(M-1\) vertices, together with a single critical vertex; this elementary acyclic matching produces the indicated sphere wedge, with no intermediate-dimensional critical cells. In particular, \(L\simeq\bigvee^{\binom{N-1}{r-1}}S^{r-2}\) or is contractible.

**The null attaching map.** Every factor \(\operatorname{Sk}_{r-1}(V_i)\) is either contractible or a wedge of \((r-1)\)-spheres. Consequently their join \(J\) is either contractible or a wedge of \(\prod_i\binom{m_i-1}{r}\) spheres of dimension \(nr-1\). In both cases \(J\) is \((r-2)\)-connected: in the noncontractible case \(nr-2\ge r-2\) for \(n\ge2\). As \(L\) is a CW complex of dimension at most \(r-2\), the map \(L\hookrightarrow J\) is nullhomotopic by cellular obstruction theory (and trivially when \(J\) is contractible). The homotopy cofiber of a null map is homotopy equivalent to \(J\vee\Sigma L\). Therefore
\[
\operatorname{Ind}_r(G)\simeq J\vee\Sigma L
\simeq\bigvee^{\prod_i\binom{m_i-1}{r}}S^{nr-1}
\vee\bigvee^{\binom{N-1}{r-1}}S^{r-1}.
\]
This proves the full non-equivariant integral homotopy classification, not merely ranks.

**Integral symmetry modules.** Identify an oriented \(k\)-simplex on \(T\) with its exterior basis wedge in \(\bigwedge^{k+1}\mathbb Z^T\). The augmented simplicial boundary is contraction by \(\varepsilon\), so the top reduced homology of the complete \(k\)-skeleton is naturally \(\bigwedge^{k+1}A_T\), including the vanishing case. This identification is equivariant under every permutation of \(T\). In the cone-attachment long exact sequence, \(\widetilde H_{r-1}(J)=0\) and \(\widetilde H_{r-2}(J)=0\), since \(n\ge2\). Therefore the connecting morphism identifies the degree \(r-1\) homology of \(\operatorname{Ind}_r(G)\) with \(\widetilde H_{r-2}(L)=\bigwedge^{r-1}A_{[N]}\), naturally and integrally. In degree \(nr-1\), the inclusion \(J\hookrightarrow\operatorname{Ind}_r(G)\) is an isomorphism on homology because the cone attachment only involves cells in dimensions at most \(r-1\). The standard integral join Künneth isomorphism identifies this module with \(\bigotimes_i\bigwedge^{r}A_{V_i}\), with no torsion. Swapping two factors whose cycles lie in dimension \(r-1\) changes orientation by \((-1)^{((r-1)+1)^2}=(-1)^r\), proving the block-permutation character.

**Face enumerator.** With empty face counted, the exact polynomial is
\[
F_{G,r}(t)=\prod_{i=1}^{n}\Bigl(\sum_{j=0}^{\min(r,m_i)}\binom{m_i}{j}t^j\Bigr)
+t\sum_{j=0}^{\min(r-1,N)}\binom Nj t^j.
\]
The first term counts all faces without the center; the second counts all faces with it. This identity is auxiliary and does not by itself prove the homotopy theorem.

## Verification
The accompanying self-contained program `verification/verify_clique_bouquets.py` constructs the graph adjacency and independently enumerates admissible faces by induced-component breadth-first search, compares them with the proved structural face decomposition, and calculates exact mod-two simplicial boundary ranks on ten parameter cases. The tested instances include \(r=3\), two four-vertex cliques (reduced Betti numbers \(21\) in degree \(2\) and \(1\) in degree \(5\)), and \(r=4\), two five-vertex cliques (\(84\) in degree \(3\) and \(1\) in degree \(7\)). The low-parameter controls are corroboration, not independently claimed research results.

The separate program `verification/verify_equivariance.py` computes signed Lefschetz traces from oriented simplices and compares them with exterior-algebra traces for identity, a transposition within a block, and exchange of two blocks in each of two test cases. All six comparisons agree. Recorded exact outputs accompany both scripts. These are finite tests; the infinite and integral conclusions follow from the argument above.

## Relationship to prior work
Deshpande, Shukla and Singh (arXiv:2001.06775, Theorem 16) establish a general wedge-of-spheres property for higher-independence complexes of chordal graphs, with possible sphere dimensions constrained to the form \(rk-1\); that result does not furnish this exact family's two ranks, null-attachment geometry or integral automorphism modules. Ghosh and Selvaraja (arXiv:2505.06614, Corollary 3.3 and Theorem 4.7) establish shellability for star-clique graphs and small-diameter block graphs, a stronger same-family qualitative fact, but give no exact sphere multiplicities or integral representations for the present bouquet. Deshpande and Singh (arXiv:2001.05448) classify higher-independence homotopy types for other graph families and use standard skeleton/join tools. Sawant (arXiv:2605.25150, publicly available May 24, 2026) motivates emerging questions through structural decompositions for trees, which do not cover clique bouquets containing triangles. The present exact formula and integral symmetry description refine qualitative topology without claiming novelty for the classical skeleton and cofiber lemmas.

## Limitations
This classification applies only to clique bouquets with one common universal vertex and to \(r\ge3\). It neither establishes a corresponding formula for arbitrary block graphs nor asserts shellability or an equivariant homotopy splitting. The homology-module isomorphisms are canonical, but the chosen nonequivariant nullhomotopy need not respect the graph automorphism group. Computational tests are finite checks, not proofs for all parameters. Prior-literature comparisons cannot exclude unindexed equivalent work.

## References
1. A. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150, first public May 24, 2026; https://arxiv.org/abs/2605.25150.
2. A. Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614, May 10, 2025; https://arxiv.org/html/2505.06614v3.
3. A. Deshpande, A. Shukla and A. Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775, January 19, 2020; https://arxiv.org/abs/2001.06775.
4. A. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448, January 15, 2020; https://arxiv.org/html/2001.05448v2.
5. S. Abdelmalek et al., *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, June 2021; https://arxiv.org/abs/2106.10863.
