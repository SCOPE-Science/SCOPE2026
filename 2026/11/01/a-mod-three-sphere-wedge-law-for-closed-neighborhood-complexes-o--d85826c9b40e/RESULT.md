# A mod-three sphere-wedge law for closed-neighborhood complexes of bipartite two-factor complements

## Finding
Let \(n\ge7\) and let \(H\) be any spanning simple bipartite \(2\)-regular graph on two classes of size \(n\), all of whose connected cycles have length at least six. Write
\[
H=\bigsqcup_{j=1}^{t}C_{2m_j},\qquad m_j\ge3,\qquad \sum_{j=1}^{t}m_j=n.
\]
Delete the edges of \(H\) from the complete bipartite graph and put \(G=K_{n,n}\setminus E(H)\). For a finite simple graph \(G\), define its **closed-neighborhood simplicial complex** by
\[
\mathcal N[G]=\{\sigma\subseteq V(G): \sigma\subseteq \{v\}\cup N_G(v)\text{ for some }v\in V(G)\}.
\]
Set
\[
c=\#\{j:3\mid m_j\},\qquad h=n-2-\sum_{j=1}^{t}\left\lfloor\frac{m_j+1}{3}\right\rfloor.
\]
Then \(h\ge3\) and the **complete integral homotopy classification** is
\[
\boxed{\displaystyle
\mathcal N[G]\simeq\bigvee^{\,n^2-4n+1}S^2\;\vee\;\bigvee^{\,2^{c+1}}S^h.}
\]
Consequently all reduced integral homology is torsion-free and is zero except in degrees \(2\) and \(h\), with ranks \(n^2-4n+1\) and \(2^{c+1}\), respectively. The homotopy type depends on the cycle-length partition, although every such \(G\) has exactly \(2n\) vertices and \(n(n-2)\) edges.

For example, when \(n=9\), removing respectively \(C_{18}\), \(C_6\sqcup C_{12}\), and three disjoint \(C_6\)'s yields high-dimensional multiplicities \(4\), \(8\), and \(16\), all in dimension \(4\), with exactly \(46\) two-spheres in each case. The formula is valid for disconnected forbidden two-factors, provided the remaining graph \(G\) is defined as above.

## Assumptions and scope
The cycles in \(H\) are simple and alternate between the fixed two bipartition classes; thus \(m_j\ge3\). No automorphism assumption or cyclic coordinate embedding of the entire graph is required. The closed-neighborhood complex is *not* the Lovász open-neighborhood complex and is *not* the graph-metric Vietoris--Rips complex. All homotopy types are ordinary (nonequivariant), integral, and based on the abstract simplicial complex above. Empty simplices are included by convention.

## Proof
**1. The bipartite pushout.** Write \(A\sqcup B\) for the bipartition of \(G\). Define subcomplexes \(U\) and \(V\) generated respectively by the closed-neighborhood simplices of centers in \(A\) and in \(B\). By definition \(\mathcal N[G]=U\cup V\). Every facet of \(U\) has at most one \(A\)-vertex, and every facet of \(V\) has at most one \(B\)-vertex. Their intersection \(W=U\cap V\) therefore has no faces of dimension greater than one; its edges are precisely the retained cross-edges of \(G\), so \(W=G\) as a one-dimensional simplicial complex. Every vertex of \(G\) has degree \(n-2\). Any two vertices in the same bipartition have at least \(n-4>0\) common neighbors, so \(G\) is connected. It has \(n(n-2)\) edges and \(2n\) vertices, hence
\[
\beta_1(W)=n(n-2)-2n+1=n^2-4n+1.
\]

**2. Reduction of the two sides.** For each \(a\in A\), its apex vertex occurs in exactly one closed-neighborhood facet defining \(U\), namely \(\Delta(\{a\}\cup N_G(a))\). Removing these cone apices one by one gives a simplicial collapse of \(U\) onto
\[
K_B=\bigcup_{a\in A}\Delta(N_G(a))\quad\text{on vertex set }B.
\]
The analogous collapse reduces \(V\) to \(K_A\) on \(A\). On the forbidden cycle \(C_{2m_j}\), each vertex in \(A\) is forbidden from its two consecutive \(B\)-neighbors, which are the edges of an ordinary cycle \(C_{m_j}\) on that class. Thus the graph \(F_B\) whose edges are these forbidden neighbor pairs is \(\bigsqcup_j C_{m_j}\), and likewise \(F_A\cong\bigsqcup_j C_{m_j}\). A face \(\sigma\subseteq B\) belongs to \(K_B\) exactly when it is disjoint from at least one edge of \(F_B\). Equivalently, the complement \(B\setminus\sigma\) is not independent in \(F_B\). Consequently
\[
K_B=\operatorname{Ind}(F_B)^\vee,\qquad K_A\cong K_B,
\]
where the superscript \(\vee\) is combinatorial Alexander duality on the corresponding \(n\)-element vertex set.

**3. Homotopy type of the side complexes.** The standard cycle independence-complex calculation, including its \(m=3\) case, is
\[
\operatorname{Ind}(C_m)\simeq
\begin{cases}
S^{\lfloor(m+1)/3\rfloor-1}\vee S^{\lfloor(m+1)/3\rfloor-1},&3\mid m,\\
S^{\lfloor(m+1)/3\rfloor-1},&3\nmid m.
\end{cases}
\]
Independence complexes take disjoint graph unions to simplicial joins. The join of the displayed wedges is a wedge of \(2^c\) spheres, all of dimension
\[
d=\sum_j\left\lfloor\frac{m_j+1}{3}\right\rfloor-1.
\]
Combinatorial Alexander duality over \(\mathbb Z\), followed by universal coefficients, therefore gives \(\widetilde H_i(K_B;\mathbb Z)=\mathbb Z^{2^c}\) for \(i=n-d-3=h\), and zero in all other degrees; the same holds for \(K_A\). There is no torsion, because the homology/cohomology of the cycle-independence wedges is free.

Every three-element subset of \(B\) belongs to \(K_B\): otherwise it would cover every edge of \(F_B\), yet every vertex cover of \(F_B\) has at least \(\sum_j\lceil m_j/2\rceil\ge\lceil n/2\rceil\ge4\) vertices. Hence \(K_B\) contains the full two-skeleton of the simplex on \(B\) and is simply connected; the same holds for \(K_A\). A simply connected CW complex with free reduced integral homology concentrated in a single degree \(h\ge2\) is a wedge of spheres of that degree, by the Hurewicz theorem and the homological Whitehead theorem. We obtain
\[
U\simeq K_B\simeq\bigvee^{2^c}S^h,
\qquad V\simeq K_A\simeq\bigvee^{2^c}S^h.
\]
The arithmetic hypotheses imply \(h\ge3\): for each \(m\ge3\), \(m-\lfloor(m+1)/3\rfloor\ge2\), and for total \(n\ge7\) the sum of these differences is at least five (a single cycle of length at least seven or at least two cycles of total length at least seven).

**4. The homotopy pushout.** Because \(U\) and \(V\) are simply connected and \(W=G\) is a connected graph, both inclusions \(W\hookrightarrow U\) and \(W\hookrightarrow V\) are nullhomotopic. Simplicial inclusions are cofibrations, so their union is a homotopy pushout. The homotopy pushout of two null maps from connected \(W\) splits as \(U\vee V\vee\Sigma W\). Since \(W\simeq\bigvee^{n^2-4n+1}S^1\), its suspension supplies exactly that many two-spheres. Combining with the two side contributions gives the boxed formula, including integral torsion-freeness and all quantified cases.

## Verification
The standalone standard-library checker `check.py` reconstructs the forbidden bipartite two-factor and every closed-neighborhood face. It independently verifies the intersection equality \(U\cap V=G\), the two side complexes and their triangular two-skeleta, and their homology together with the full complex's mod-two simplicial boundary ranks. Nine cycle-length partitions were checked: \((7)\), \((3,4)\), \((8)\), \((3,5)\), \((4,4)\), \((9)\), \((3,6)\), \((4,5)\), and \((3,3,3)\). The checker returned `VERIFY_OK 9 two-factors`. These checks are finite corroboration; the proof establishes the unrestricted claim over the integers.

## Relationship to prior work
Matsushita (2025), Sections 1--5, supplies the definition and general connections of closed-neighborhood complexes and discusses \(K_m\square K_n\), not the bipartite two-factor complements here. The three-periodic homotopy types of independence complexes of cycles are classical (Kozlov; Adamaszek) and are used as inputs, not claimed as discoveries. Prior published work on **Rips filtrations of the same bipartite factor complements** identifies the scale-two *Rips* complex with \(\operatorname{Ind}(H)\), using the original cycles of length \(2m_j\). In contrast, this result identifies the *closed-neighborhood / scale-one graph Čech* complex using the Alexander dual of the projected cycles of length \(m_j\), two nontrivial side complexes and a suspended graph. The corresponding homotopy classifications do not follow from one another without this separate pushout analysis. A full published published-finding corpus record was compared as a distinct but closely related result.

## Limitations
The restriction \(n\ge7\) ensures simple connectivity of the two side complexes by the complete two-skeleton; the smaller cases are not classified here. Forbidden factors with four-cycles, arbitrary degree patterns, equivariant homotopy types and persistent maps are not claimed. Literature comparison is bounded by accessible indexed sources: unindexed equivalent formulations could exist. Independent mathematical validation has not been performed.

## References
1. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608v1, first public 2025-11-16; version 2 (2025-12-07), https://arxiv.org/html/2511.12608v2. Definition 1.1, Theorem 1.2, Example 3.5, Section 4.
2. M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250, first public 2011-06-30, https://arxiv.org/abs/1106.6250. Classical cycle-independent-set topology.
3. D. N. Kozlov, *Complexes of directed trees*, Journal of Combinatorial Theory, Series A 88 (1999), 112--122, DOI: 10.1006/jcta.1999.2984. Cycle independence-complex formulas.
4. *Independence-complex transfer and three-periodic Rips barcodes of bipartite factor complements*, published research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-independence-complex-transfer-and-three-periodic-rips-barcodes-o--5408625c1e7e. A theorem on a different complex and filtration of the same underlying graphs.
