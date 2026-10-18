# Reflection characters and quotient homology of even Möbius-ladder perfect-matching complexes

## Finding
For every even integer \(n\ge4\), let \(M_{2n}\) be the graph on \(\mathbb Z/(2n)\) whose edges are the rim edges \(e_i=\{i,i+1\}\) and antipodal spokes \(s_j=\{j,j+n\}\). Let \(K_n=\mathcal M_p(M_{2n})\) be the simplicial complex consisting of matchings extendible to a perfect matching. Put \(d=n/2-1\), and let the dihedral transformations be \(r(i)=i+1\) and \(t(i)=-i\). Then the reflection character on the only nonzero reduced rational homology group is

\[
\operatorname{tr}\!\left((r^a t)_*\mid\widetilde H_d(K_n;\mathbb Q)\right)
=\begin{cases}
0,&a\text{ even},\\
0,&a\text{ odd and }4\mid n,\\
2(-1)^k,&a\text{ odd and }n=4k+2.
\end{cases}
\]

The homology group has rational dimension two by the previously established nonequivariant homotopy theorem of Agarwal and Basak. Consequently, for the geometric quotient by an edge-axis reflection (odd \(a\)), its reduced rational Betti number in degree \(d\) is respectively \(1,2,0\) when \(n\equiv0,2,6\pmod8\); for the quotient by a vertex-axis reflection (even \(a\)) the rank is always one. All other reduced rational homology groups of these quotients vanish. The genuinely new, not previously implied character values are the \(n\equiv2\pmod4\) edge-axis traces and their distinct quotient dimensions. These calculations, together with previously published rotation characters, complete the rational dihedral character for even widths.

## Assumptions and scope
The graph has \(2n\) vertices and \(3n\) graph edges, where the latter form the simplicial vertices of \(K_n\). A simplex must **extend to a perfect matching**; being only a matching is insufficient. Integers \(n\) are even and at least four. The action on homology is induced from the labeled graph automorphisms; \(r^a t\) acts on graph vertices by \(i\mapsto a-i\). Different parities of \(a\) give the two reflection conjugacy classes. All representation and quotient homology statements are over \(\mathbb Q\); no equivariant homotopy equivalence or integral representation splitting is asserted.

We use two explicitly identified results of Agarwal and Basak, arXiv:2608.30601 (first public version 31 August 2026). Their matching-extension classification for even \(n\) identifies \(K_n\) with the independence complex of the graph on rim and spoke edges in which pairs are incompatible precisely when (i) the graph edges share an endpoint, or (ii) both are rim edges \(e_i,e_j\) with \(j-i\equiv n-1\) or \(n+1\pmod{2n}\). Their homotopy theorem gives \(K_n\simeq S^d\vee S^d\). Both statements are prior inputs, not original results here. The source proves the extension criterion by excluding minimal bad pairs and extending the other partial matchings column-by-column; finite independent checks of the equality of the full complexes are included below.

## Proof
**1. From an involution to an orbit graph.** Let \(G_n\) be the incompatibility graph just defined, so \(K_n=\operatorname{Ind}(G_n)\). For an involution \(g=r^a t\), a \(g\)-invariant simplex is a union of \(g\)-orbits of graph edges. Discard any orbit containing two incompatible edges, and build \(H_{n,a}\) with one vertex for every remaining orbit, connecting two orbit-vertices when some constituent edges are incompatible. The \(g\)-invariant simplices of \(K_n\), including the empty simplex, are in bijection with independent sets of \(H_{n,a}\).

If a fixed simplex contains \(q\) orbits of simplicial vertices, its contribution to the reduced signed Lefschetz number is \((-1)^{q-1}\): an orbit of length \(\ell\) contributes a permutation sign \((-1)^{\ell-1}\), which combines with the chain-degree sign. Thus, writing \(I(H;z)=\sum_{S\text{ independent}}z^{|S|}\),
\[
\widetilde L(g;K_n)=-I(H_{n,a};-1),\qquad
\operatorname{tr}(g_*\mid\widetilde H_d(K_n;\mathbb Q))=(-1)^{d+1}I(H_{n,a};-1).
\]
This includes the augmented empty simplex, whose contribution is minus one. The second equality uses the previously proved concentration of reduced homology in degree \(d\).

**2. Vertex-axis reflections.** By rotation-conjugacy it suffices to consider \(a=0\). The spoke \(s_0=\{0,n\}\) is fixed by \(t\). Its only incident rim edges are \(e_0,e_{2n-1},e_{n-1},e_n\), grouped by \(t\) into the pairs \(\{e_0,e_{2n-1}\}\) and \(\{e_{n-1},e_n\}\). Each pair consists of incident (hence incompatible) rim edges and therefore is discarded from the orbit graph. No other spoke meets \(s_0\). Hence the orbit-vertex \(\{s_0\}\) is isolated in \(H_{n,0}\). Its independence polynomial has a factor \(1+z\), giving \(I(H_{n,0};-1)=0\) and trace zero.

**3. Edge-axis reflection: a folded chain of triangles.** By rotation-conjugacy take \(a=1\). The admissible rim orbits are \(E_0=\{e_0\}\), \(E_n=\{e_n\}\), and \(E_j=\{e_j,e_{2n-j}\}\) for \(1\le j\le n-1\). The spoke orbits are \(S_j=\{s_j,s_{1-j}\}\), indices modulo \(n\), with \(n/2\) distinct orbits. Put \(m=n/2\), and label the distinct spoke orbits \(S_0,\ldots,S_{m-1}\). Directly from the stated edge-incompatibility rules, each \(E_j\) and \(E_{n-j}\), for \(1\le j<m\), are **nonadjacent false twins** in \(H_{n,1}\): their open neighborhoods coincide. Delete the orbit-vertices \(E_{n-j}\). The resulting graph has vertices \(E_0,\ldots,E_m,S_0,\ldots,S_{m-1}\), and exactly the three edges
\[
E_jE_{j+1},\quad S_jE_j,\quad S_jE_{j+1}\qquad(0\le j<m).
\]
Thus it is a path of \(m\) triangles sharing successive vertices. This orbit-graph adjacency can be checked locally from the incident-edge rules; `verify_reflections.py` independently reconstructs every orbit and confirms the asserted graph for all even \(4\le n\le40\).

Removing a false twin preserves \(I(H;-1)\): when all neighbors are absent, the two nonadjacent twins contribute \((1+z)^2\) rather than \((1+z)\), both zero at \(z=-1\); when a neighbor is present, neither may be selected, so the contributions are both one. Repeating this argument gives equality of \(I(-1)\) for the orbit graph and the triangle chain.

**4. Exact chain evaluation.** Fix an independent subset \(T\subseteq\{E_0,\ldots,E_m\}\) in the triangle chain. The vertex \(S_j\) may be chosen or not exactly when neither \(E_j\) nor \(E_{j+1}\) is in \(T\). Summation at \(z=-1\) over those choices vanishes unless every path edge \(E_jE_{j+1}\) has an endpoint in \(T\). Because \(T\) is also independent, precisely one endpoint of every path edge is in \(T\). There are exactly two such subsets: alternating even-index and odd-index path vertices. Their sizes are \(\lceil(m+1)/2\rceil\) and \(\lfloor(m+1)/2\rfloor\). Therefore
\[
I(H_{n,1};-1)=(-1)^{\lceil(m+1)/2\rceil}+(-1)^{\lfloor(m+1)/2\rfloor}.
\]
If \(m\) is even this is zero. If \(m=2k+1\) it is \(2(-1)^{k+1}\); since \(d=m-1=2k\), the character formula of Step 1 gives \(2(-1)^k\). This proves both reflection classes for all allowed \(n\).

**5. Quotient homology.** A finite simplicial group action may be barycentrically subdivided, and over \(\mathbb Q\) the homology of the geometric quotient is the invariant subspace of the homology. Since an involution on a two-dimensional rational space has invariant dimension \((2+\operatorname{tr})/2\), the quotient assertions follow. No other reduced homology degree exists before or after taking invariants.

## Verification
The reproducible program `verify_reflections.py` uses only Python 3's standard library and the exact specified graph labels. It enumerates all perfect matchings and all their subfaces for \(n=4,6,8,10,12\), independently computes signed invariant-face Lefschetz traces for both reflection classes at each width, and obtains the sequence \(0,-2,0,2,0\) for the odd-axis character. For \(n=4,6,8,10\), it independently enumerates all independent sets of the incompatibility graph and confirms the *full* equality of simplicial complexes. For \(n=4,6,8\), exact bit-vector boundary elimination yields the predicted rank-two reduced homology in degree \(d\), with no other reduced homology. Finally, it reconstructs the involution orbit graph and verifies all false-twin equalities and the exact triangle-chain adjacency for the nineteen even integers \(4\le n\le40\). The independent computations check examples, not an infinite proof; the all-parameter argument is Steps 1–5 with the cited matching-extension and homotopy inputs.

Execute `python3 verify_reflections.py`. The program prints `VERIFY_OK` only after every assertion passes.

## Relationship to prior work
Agarwal and Basak (arXiv:2608.30601, original public version August 31, 2026) establish the matching-extension description and nonequivariant sphere-wedge homotopy classification for the *same* complexes; their inspected perfect-matching section does not provide reflection characters or quotient ranks. The previously published calculation *Rotation has order two or four on Möbius-ladder perfect-matching homology* determines the one-step rotation and its square, but explicitly leaves reflections unclassified. In the \(n\equiv0\pmod4\) case, that quarter-turn representation already forces zero reflection trace; this covered consequence is included only to state a uniform complete reflection formula, not as the originality core. When \(n\equiv2\pmod4\), knowing the rotation and central half-turn leaves its commuting reflection signs undetermined, so the signed edge-axis value and mod-eight quotient ranks are not consequences of the earlier rotation result.

The published *Antipodal half-turn representation on Möbius-ladder perfect-matching homology* treats only the central involution, which is distinct from either mirror reflection. *Complete dihedral rational homology representations of odd Möbius-ladder perfect-matching complexes* applies only to odd \(n\), disjoint from the current hypotheses. Lekshmi and West count perfect matchings but do not study the simplicial homology or its group action. No covering theorem or exact table for the even-width reflection character was found in the inspected primary texts and targeted searchable records; nonappearance does not prove universal uniqueness.

## Limitations
The result relies on the 2026 published nonequivariant rank and flag-description lemmas and proves a rational, not integral-lattice, representation character. It does not establish an equivariant homotopy decomposition, fixed-point homeomorphism, or integral torsion information for the reflection quotients. The values for \(4\mid n\) are already implied by the published rotation representation; originality and nontrivial additional value rest on the new \(n\equiv2\pmod4\) reflection signs, including the distinction between mirror conjugacy classes. General equivariant methods could reproduce these values and an unindexed stronger result remains a literature risk. A later expanded version of the underlying arXiv preprint was identified; its additional circular-ladder material was not necessary for the particular original Möbius-ladder lemmas inspected here.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, first public version 2026-08-31, especially original Section 4, Lemmas 13–17 and Theorem 18. https://arxiv.org/abs/2608.30601
2. *Rotation has order two or four on Möbius-ladder perfect-matching homology*, published scientific record 3551187dd347, RESULT.md, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-rotation-has-order-two-or-four-on-m-bius-ladder-perfect-matching--3551187dd347
3. *The antipodal half-turn representation on Möbius-ladder perfect-matching homology*, published scientific record 317e26dcb314, RESULT.md, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-antipodal-half-turn-representation-on-m-bius-ladder-perfect--317e26dcb314
4. *Complete dihedral rational homology representations of odd Möbius-ladder perfect-matching complexes*, published scientific record d5bba5f21863, RESULT.md, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-dihedral-rational-homology-representations-of-odd-m-biu--d5bba5f21863
5. R. S. Lekshmi and D. B. West, *The Number of Perfect Matchings in Möbius Ladders and Prisms*, arXiv:2003.09602, 2020. https://arxiv.org/abs/2003.09602
