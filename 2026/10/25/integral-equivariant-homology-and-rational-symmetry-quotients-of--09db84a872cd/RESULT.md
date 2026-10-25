# Integral equivariant homology and rational symmetry quotients of higher independence complexes of complete multipartite graphs

## Finding
For a complete multipartite graph \(\Gamma=K_{m_1,\ldots,m_s}\), set \(X=\operatorname{Ind}_r(\Gamma)\). The top reduced integral homology is naturally an exterior-power **quotient lattice**, equivariant under all graph automorphisms:
\[
\widetilde H_{r-1}(X;\mathbb Z)\cong
\frac{\bigwedge^r L}{\bigoplus_{i=1}^s\bigwedge^r L_i},\qquad
L=\ker(\mathbb Z^{V(\Gamma)}\to\mathbb Z),\quad
L_i=\ker(\mathbb Z^{V_i}\to\mathbb Z).
\]
Every other reduced integral homology group vanishes. The quotient lattice is torsion-free of rank
\[
\binom{N-1}{r}-\sum_{i=1}^s\binom{m_i-1}{r},\qquad N=\sum_i m_i.
\]
For the natural partwise permutation group \(G_0=\prod_{i=1}^s S_{m_i}\), the quotient has reduced rational homology concentrated in degree \(r-1\), of dimension
\[
\dim\widetilde H_{r-1}(X/G_0;\mathbb Q)=\binom{s-1}{r}.
\]
If all parts have equal size \(m\), then the quotient by the **entire** automorphism group \(S_m\wr S_s\) has zero reduced rational homology in every degree. These statements refine the previously known nonequivariant homotopy classification.

## Assumptions and scope
Let \(s\ge2\), \(m_i\ge1\), and \(2\le r\le N-1\) be integers. A face of the higher independence complex \(X\) is a vertex subset whose induced graph has connected components of size at most \(r\). In a complete multipartite graph this means: every vertex subset of size at most \(r\) is a face, and every subset contained in a single part is a face; there are no others. Hence
\[
X=K\cup\bigcup_i\Delta(V_i),\qquad K=\operatorname{skel}_{r-1}\Delta(V).
\]
We adopt \(\binom ab=0\) when \(b>a\). The group \(G_0\) permutes vertices within each part; when all part sizes are equal, \(\operatorname{Aut}(\Gamma)=S_m\wr S_s\). All homology groups are reduced unless stated otherwise.

## Proof
**1. Augmented chain model.** Give \(W=\mathbb Z^V\) the basis of graph vertices and augmentation \(\varepsilon:W\to\mathbb Z\), \(\varepsilon(e_v)=1\). The reduced simplicial chain group of the full simplex in degree \(q-1\) is \(\bigwedge^q W\), with boundary contraction \(\iota_\varepsilon\). Choose one vertex basis vector to split \(W=L\oplus\mathbb Z e_v\). Contraction is injective on \(e_v\wedge\bigwedge^{q-1}L\) and vanishes on \(\bigwedge^q L\). Therefore the skeleton \(K\) has
\[
\widetilde H_{r-1}(K;\mathbb Z)=\ker(\iota_\varepsilon:\bigwedge^rW\to\bigwedge^{r-1}W)=\bigwedge^rL
\]
and no other reduced integral homology. The isomorphism is canonical, independent of the auxiliary splitting.

**2. Relative attachments.** The simplices \(\Delta(V_i)\) intersect pairwise only in their empty face; their positive-dimensional cells outside \(K\) are disjoint. Consequently the relative cellular complex \(C_*(X,K)\) is the direct sum of \(C_*(\Delta(V_i),\operatorname{skel}_{r-1}\Delta(V_i))\). The long exact sequence for each contractible full simplex identifies its only nonzero relative homology with \(\bigwedge^r L_i\) in degree \(r\). Under the boundary connecting map into \(\widetilde H_{r-1}(K)\), this identifies with the natural inclusion \(\bigwedge^r L_i\hookrightarrow\bigwedge^r L\). Therefore
\[
0\longrightarrow\bigoplus_i\bigwedge^rL_i
\longrightarrow\bigwedge^rL
\longrightarrow\widetilde H_{r-1}(X;\mathbb Z)
\longrightarrow0
\]
is exact, and all other reduced homology groups are zero. Every map is induced by canonical vertex inclusions, so the description is equivariant for every graph automorphism, including those exchanging parts.

**3. No integral torsion.** Select one vertex in each part. The sum \(\bigoplus_i L_i\) is a direct summand of \(L\) with free complementary group of rank \(s-1\). This follows by splitting each \(\mathbb Z^{V_i}\) into its augmentation kernel and a chosen vertex line, and then taking the global augmentation kernel. The decomposition of \(\bigwedge^r L\) by wedge degrees in these summands exhibits the direct sum \(\bigoplus_i\bigwedge^r L_i\) as a direct summand of the underlying integral abelian group (not as an equivariant direct summand). Thus its quotient is free, with the displayed rank.

**4. Characters.** For any automorphism \(g\), write \(P_g\) for its permutation operator on \(\mathbb Q^V\), and \(P_{g,i}\) for the restriction to a part fixed setwise by \(g\). Since the quotient is a short exact sequence of rational representations, and the summands for moved parts have zero trace, its complete character is
\[
\chi_{r-1}(g)=[t^r]\left(\frac{\det(I+tP_g)}{1+t}
-\sum_{i:gV_i=V_i}\frac{\det(I+tP_{g,i})}{1+t}\right).
\]
For a permutation with cycles of lengths \(d\), the numerator is explicitly \(\prod_d(1-(-t)^d)\), so this is a finite exact formula for all automorphisms.

**5. Quotient topology over rational coefficients.** As a \(G_0\)-module over \(\mathbb Q\), the augmentation space is \(L\otimes\mathbb Q\cong\mathbb Q^{s-1}\oplus\bigoplus_i U_i\), where \(U_i=L_i\otimes\mathbb Q\) is the standard representation of \(S_{m_i}\). Positive exterior powers of each \(U_i\) are nontrivial hook representations, hence have no invariants; also \((\bigwedge^rL_i)^{G_0}=0\). It follows that the invariant part of the quotient lattice is \(\bigwedge^r\mathbb Q^{s-1}\), with dimension \(\binom{s-1}{r}\). If all parts have equal size, the remaining \(S_s\)-action on \(\mathbb Q^{s-1}\) is the standard representation; \(\bigwedge^r\operatorname{Std}_s\) contains no trivial constituent for \(r\ge1\). Finally, rational homology of a quotient by a finite group is the invariant rational homology of the original finite simplicial complex: barycentrically subdivide to avoid inversions and use averaging. This gives the two quotient assertions.

## Verification
The accompanying `verify.py` generates the higher-independence faces directly, calculates reduced boundary ranks modulo two, and independently matches signed simplicial Lefschetz traces with the exterior-power character for every automorphism in eight test configurations. It separately averages the character over within-part groups and full wreath-product groups. The checker prints `HIGHER_INDEPENDENCE_EQUIVARIANT_CHECKS_PASSED` upon successful completion. The all-parameter assertion is proved above and does not rely on extrapolation from finite tests.

For example, for \(\Gamma=K_{2,2,2,2}\) and \(r=2\), the complex has \(21\) reduced first-homology generators. Exactly \(3\) are invariant under \(S_2^4\), but none is invariant under \(S_2\wr S_4\).

## Relationship to prior work
Deshpande and Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, Theorem 3.5, established the nonequivariant sphere-wedge homotopy classification and rank formula for complete multipartite graphs. The present result adds a canonical **integral, automorphism-equivariant homology lattice**, a full all-automorphism character, and homology of two natural quotient families. Patra and Roy, *Graded Betti numbers of a hyperedge ideal associated to join of graphs*, arXiv:2311.07308, Theorem 4.4, calculate algebraic graded Betti numbers for ideals associated with these complexes, not the claimed permutation action on their integral topological homology. The difference is between numerical invariants of an ideal and group representations/quotient topology.

## Limitations
The equivariant statement determines integral homology as an abstract group-action lattice, not an integral equivariant homotopy type. The vanishing claims for full symmetry quotients are **rational acyclicity**, not contractibility or integral acyclicity; torsion in quotient homology is not ruled out. The priority search is bounded, so an equivalent unindexed result remains possible. Published nonequivariant homotopy and ideal Betti formulas are not claimed as discoveries.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, submitted January 15, 2020; Theorem 3.5 and its proof. https://arxiv.org/abs/2001.05448
2. S. K. Patra and A. Roy, *Graded Betti numbers of a hyperedge ideal associated to join of graphs*, arXiv:2311.07308, first submitted November 13, 2023; Theorem 4.4. https://arxiv.org/abs/2311.07308
