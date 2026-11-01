# Odd cyclic fixed-point reduction for Möbius-ladder perfect-matching complexes

## Finding
Let \(m\ge1\) and \(L\ge3\) be odd integers, and put \(n=mL\). Write \(M_{2n}\) for the graph on \(\mathbb Z/(2n)\) with rim edges \(\{i,i+1\}\) and spoke edges \(\{i,i+n\}\); graph edges are simple, but the two-edge quotient below retains parallel edge labels. Let \(X_n=\mathcal M_p(M_{2n})\) denote the simplicial complex whose simplicial vertices are graph edges and whose faces are matchings extendible to a graph perfect matching. For the one-step rotation \(r(i)=i+1\), set \(H=\langle r^{2m}\rangle\), of order \(L\).

**Theorem.** The actual geometric fixed-point space \(|X_n|^H\) is canonically piecewise-linearly homeomorphic to \(|X_m|\) when \(m\ge3\), and to the three-point discrete space when \(m=1\). Consequently
\[
|X_n|^H\simeq\begin{cases}
\bigvee^2 S^{(m-1)/3},&m\equiv1\pmod6,\\
\bigvee^4 S^{m/3},&m\equiv3\pmod6,\\
\bigvee^2 S^{(m+1)/3},&m\equiv5\pmod6.
\end{cases}
\]
In the first line \(m=1\) gives \(\bigvee^2S^0\), i.e. three components. The sphere-wedge types of the *small* perfect-matching complexes are known from Agarwal–Basak; the claim here is the genuinely geometric PL fixed-space reduction for every odd covering degree \(L\ge3\).

## Assumptions and scope
A perfect-matching complex is different from the unrestricted matching complex. A matching is extendible if at least one perfect matching of the graph contains it. The action on the complex is induced by the graph's specified rotation. We retain three **distinct edge labels** on the two-vertex quotient at \(m=1\), even though they share endpoints. The fixed space consists of pointwise fixed geometric realizations, not merely invariant homology or quotient homology. All assertions concern finite simplicial complexes and integral topological homotopy types.

## Proof
**1. The graph covering.** Let \(B_m\) be the graph with vertices \(\mathbb Z/(2m)\), rim edges \(e_j=\{j,j+1\}\) indexed by \(j\in\mathbb Z/(2m)\), and spoke edges \(a_j=\{j,j+m\}\) indexed by \(j\in\mathbb Z/m\). For \(m\ge3\), this is exactly the ordinary Möbius ladder \(M_{2m}\). For \(m=1\), it is the two-vertex multigraph with labeled edges \(e_0,e_1,a_0\). Because \(L\) is odd, reduction of vertex labels modulo \(2m\) maps the large spoke displacement \(n=mL\) to the small spoke displacement \(m\) modulo \(2m\). It maps rim edges to rim edges. The inverse image of any labeled base edge has exactly \(L\) edges, one incident at each vertex of a given fiber, and these form one orbit of \(H\). Thus the reduction \(M_{2n}\to B_m\) is a regular degree-\(L\) graph covering (in the labeled multigraph sense when \(m=1\)), and \(H\)-orbits on its graph edges correspond bijectively to base graph edges.

**2. Matching condition descends exactly.** Select a collection \(F\subseteq E(B_m)\), and let \(\widetilde F\) be its *full inverse image* of large-graph edges. Because the covering is a local bijection on incident edges, \(\widetilde F\) is a matching if and only if \(F\) is a matching. If \(F\) extends to a perfect matching in \(B_m\), lifting that perfect matching gives a perfect matching in \(M_{2n}\) extending \(\widetilde F\).

Conversely suppose \(\widetilde F\) extends to a perfect matching \(P\) upstairs. Remove from the graphs all vertices used by \(F\) and \(\widetilde F\), respectively. The residual graphs still form a degree-\(L\) covering. Their bipartition comes from the parity of a residue-class vertex: both the rim edges and the spoke edges change parity because \(m\) is odd. The restriction of \(P\) to the residual large graph is a perfect matching. For every residual base edge \(e\), let \(w_e\ge0\) count the edges in this restricted matching lying above \(e\). Every residual base vertex has \(L\) lifts, each matched once, hence \(\sum_{e\ni v}w_e=L\). For any subset \(S\) of the left bipartition, summing this equation over \(S\) gives
\[
L|S|=\sum_{e\text{ leaving }S}w_e\le L|N(S)|.
\]
The inequality holds because the total incident weight over its neighboring right vertices is \(L|N(S)|\). Thus \(|S|\le|N(S)|\); Hall's marriage theorem gives a perfect matching of the residual *base* bipartite graph. Adding \(F\) extends it to a perfect matching in \(B_m\). This argument works for every \(m,L\) in scope and includes the labeled multigraph boundary \(m=1\).

**3. Canonical PL fixed-space model.** A simplex fixed pointwise as a geometric set under the finite simplicial action has equal barycentric coordinates on each complete \(H\)-orbit of graph-edge vertices. Thus geometric fixed points are triangulated by barycenters of edge orbits that are individually faces of \(X_n\), with simplices indexed by mutually admissible collections of those orbits. Step 2 says exactly that their base labels form the faces of \(\mathcal M_p(B_m)\). The orbit-barycenter affine map therefore gives a canonical PL homeomorphism
\[
|X_n|^H\cong_{\mathrm{PL}}|\mathcal M_p(B_m)|.
\]

**4. Homotopy types.** For \(m\ge3\), apply the published nonequivariant classification of perfect-matching complexes of Möbius ladders in Agarwal–Basak, cited below: odd widths \(m\equiv1,5\pmod6\) give two spheres in the displayed degrees, while \(m\equiv3\pmod6\) gives four spheres. For \(m=1\), all three labeled edges are individually perfect matchings in \(B_1\), but no pair is a matching, so its complex is exactly three discrete vertices. This agrees with the first formula at \(m=1\). All claims follow.

## Verification
A finite face-level test enumerated edge orbits, admissible invariant matching collections and their extension to a perfect matching for \((n,m,L)=(9,3,3),(15,3,5),(15,5,3)\); the quotient face sets agree respectively with those from the small ladder. Tests covered all 34, 34 and 344 base matching candidates respectively (284 of the last 344 being extendible). These finite examples do not establish the theorem; the covering/Hall proof does. The check can be replicated directly by enumerating the orbit edge subsets and enumerating graph perfect matchings, retaining only edge sets contained in one of them. In general the PL homeomorphism is canonical and constructive: replace each base edge by the barycenter of its full \(H\)-orbit upstairs.

## Relationship to prior work
Agarwal and Basak (arXiv:2608.30601v1, August 31, 2026) determine the nonequivariant homotopy types of Möbius-ladder perfect-matching complexes; their classification supplies precisely the last step of this proof, and is **not claimed as new**. Closely related existing symmetry calculations determine antipodal or full dihedral *rational homology characters*, not the actual geometric fixed-point PL homeomorphism under arbitrary proper odd-order rotation subgroups. The related antipodal geometric fixed-space classification concerns the different **order-two** subgroup, not these odd-order subgroups. The present graph-cover descent principle proves a stronger fixed-space statement not implied by a rational character. No priority claim beyond inspected available literature is made.

## Limitations
The theorem covers odd \(m\) and odd covering degrees \(L\ge3\), hence all nontrivial **odd-order** subgroups of the canonical rotation group for odd-width Möbius ladders, but it does not classify reflections, even-order rotational subgroups, or arbitrary graph covers whose quotient is nonbipartite. The PL statement is between fixed space and smaller matching complex, whereas the subsequent sphere-wedge formulas assert homotopy equivalence only. The known sphere-wedge input is cited rather than reproved. Undiscovered or unindexed equivalent work remains a possible originality risk. Independent validation has not been performed.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v1, first public 2026-08-31, Main Theorem 1(b,c), and arXiv:2608.30601v2 (2026-09-14): https://arxiv.org/abs/2608.30601.
2. *The antipodal half-turn representation on Möbius-ladder perfect-matching homology*, published-finding corpus research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-antipodal-half-turn-representation-on-m-bius-ladder-perfect--317e26dcb314.
3. *Complete dihedral rational homology representations of odd Möbius-ladder perfect-matching complexes*, published-finding corpus research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-dihedral-rational-homology-representations-of-odd-m-biu--d5bba5f21863.
