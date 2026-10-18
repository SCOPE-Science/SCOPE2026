# Crown-graph two-independence complexes: sphere wedges and integral symmetry

## Finding
For each integer \(n\geq3\), let \(\operatorname{Cr}_n\) be the crown graph on vertices \(a_1,\ldots,a_n,b_1,\ldots,b_n\), with the edge \(a_i b_j\) present precisely when \(i\ne j\). Its two-independence complex \(X_n=\operatorname{Ind}_2(\operatorname{Cr}_n)\) has faces the vertex subsets for which every induced-graph connected component contains at most two vertices. Then
\[
X_n\simeq\bigvee^{\binom{n-1}{2}}S^2.
\]
The vertex-permuting action of \(S_n\), together with layer exchange by \(C_2\), determines a canonical integral lattice isomorphism
\[
\widetilde H_2(X_n;\mathbb Z)\cong
\left(\bigwedge{}^2 I_n\right)\otimes\mathrm{sgn}_{C_2},\qquad
I_n=\ker\left(\mathbb Z^n\xrightarrow{\mathrm{sum}}\mathbb Z\right),
\]
where \(S_n\) permutes coordinates of \(I_n\), and layer exchange acts by minus the identity. Other reduced integral homology vanishes. Thus for \(\sigma\in S_n\) and \(\epsilon\in\{0,1\}\), the rational top-homology trace is
\[
\chi(\sigma,\epsilon)=(-1)^\epsilon\,
\frac{(f(\sigma)-1)^2-(f(\sigma^2)-1)}{2},
\]
where \(f(\tau)\) denotes the number of fixed column indices of \(\tau\). The boundary case \(n=2\) is contractible.

## Assumptions and scope
All graphs are finite and simple; a connected induced component containing two vertices must be a single edge, while isolated vertices form distinct singleton components. The simplicial complexes contain the empty face. For \(n\ge2\), let \(A=\{a_i\}\), \(B=\{b_i\}\), let \(\Delta_A,\Delta_B\) be their full simplices, and let \(E_A,E_B\) be their complete-graph one-skeleta. Write \(T_{ij}\) for the full tetrahedron on \(\{a_i,b_i,a_j,b_j\}\), and put \(L_n=\bigcup_{i<j}T_{ij}\). The \(S_n\times C_2\) action permutes column labels and exchanges the two rows. The homotopy equivalence is nonequivariant; the integral homology representation is equivariant.

## Proof
**1. Exact decomposition.** Every face supported entirely in a row belongs to \(\Delta_A\) or \(\Delta_B\). For a mixed subset \(S\), write its occupied column sets as \(I,J\subseteq[n]\), where \(I\) indexes its row-\(A\) vertices and \(J\) its row-\(B\) vertices. A selected \(a_i\) has \(|J|-\mathbf1_{i\in J}\) selected neighbors, and a selected \(b_j\) has \(|I|-\mathbf1_{j\in I}\) selected neighbors. If either \(|I|\) or \(|J|\) is at least three, the other nonempty row contains a vertex with at least two neighbors, creating a component with at least three vertices. Thus both cardinalities are at most two. If \(|I|=2\) and \(|J|=1\), the single element of \(J\) must belong to \(I\), and analogously with rows exchanged. If both are two, their sets must be equal. Any permissible mixed face is therefore contained in a \(T_{ij}\). Conversely all subsets of each \(T_{ij}\) satisfy the two-independence restriction, as their induced cross-edges are a matching. Hence exactly
\[
X_n=\Delta_A\cup\Delta_B\cup L_n,
\quad L_n\cap\Delta_A=E_A,
\quad L_n\cap\Delta_B=E_B,
\quad \Delta_A\cap\Delta_B=\{\varnothing\}.
\]

**2. Homotopy reduction.** Every maximal face of \(L_n\) containing \(b_i\) also contains \(a_i\); hence \(b_i\) is a dominated vertex with dominator \(a_i\). Removing the vertices \(b_1,\ldots,b_n\) sequentially by strong simplicial collapses reduces \(L_n\) to \(E_A\). By exchanging rows, \(L_n\) also collapses to \(E_B\). Thus each inclusion \(E_A\hookrightarrow L_n\) and \(E_B\hookrightarrow L_n\) is a homotopy equivalence. Let \(K=\Delta_A\cup_{E_A}L_n\). Its reduced homology and homotopy are trivial because \(E_A\to L_n\) is a homotopy equivalence and \(\Delta_A\) is contractible; more directly, the pushout along the cofibration is a homotopy pushout of a homotopy equivalence, so \(K\simeq\Delta_A\simeq *\). The second attachment is \(X_n=K\cup_{E_B}\Delta_B\). Both \(K\) and \(\Delta_B\) are contractible, and both inclusions from \(E_B\) are cofibrations. Consequently the homotopy pushout is \(\Sigma E_B\), with \(\Sigma\) the unreduced suspension. Since \(E_B\) is the connected complete graph on \(n\) vertices, \(E_B\simeq\bigvee^{\binom{n-1}{2}}S^1\). This proves the claimed wedge of two-spheres over \(\mathbb Z\) and all other integral homology groups.

**3. The integral symmetry lattice.** Define a simplicial column projection \(p:L_n\to E\), where \(E\) denotes the complete graph on \([n]\), by mapping \(a_i,b_i\mapsto i\). This is simplicial because every face of \(L_n\) involves at most two columns; the restrictions of \(p\) to either \(E_A\) or \(E_B\) are isomorphisms. Since \(L_n\simeq E_A\), the map \(p\) is a homotopy equivalence and is invariant under row exchange.

Consider the long exact integral homology sequence of \((X_n,L_n)\). Excision and the preceding face decomposition split the relative chain complex into the complexes of \((\Delta_A,E_A)\) and \((\Delta_B,E_B)\). As both row simplices are contractible and their one-skeleta connected, boundary maps provide natural identifications
\[
H_2(X_n,L_n;\mathbb Z)\cong H_1(E_A;\mathbb Z)\oplus H_1(E_B;\mathbb Z)
\cong V\oplus V,\qquad V=H_1(E;\mathbb Z).
\]
Under the projection \(p_*:H_1(L_n;\mathbb Z)\to V\), the connecting homomorphism is \((u,v)\mapsto u+v\). Since \(H_2(L_n)=0\), exactness identifies \(H_2(X_n;\mathbb Z)\) with the kernel \(\{(u,-u):u\in V\}\). Column permutations act diagonally, while layer exchange interchanges the summands, sending \((u,-u)\) to \((-u,u)\). Hence row exchange acts by \(-1\) on this **integral** lattice.

Orient the edges of \(E\) by increasing column index. The simplicial boundary gives an \(S_n\)-equivariant contraction \(\partial:\bigwedge^2\mathbb Z^n\to I_n\) defined by \(\partial(e_i\wedge e_j)=e_j-e_i\). Its kernel is \(H_1(E;\mathbb Z)=V\). Since \(\mathbb Z^n\to\mathbb Z\) is a split exact sequence of free abelian groups and \(I_n\) is its kernel, one has \(\ker\partial=\bigwedge^2 I_n\) **as an integral lattice**, not merely after tensoring with \(\mathbb Q\). This proves the group-module statement. Finally \(\operatorname{tr}_{I_n}(\sigma)=f(\sigma)-1\); using \(\operatorname{tr}_{\wedge^2 I_n}(\sigma)=\big(\operatorname{tr}_{I_n}(\sigma)^2-\operatorname{tr}_{I_n}(\sigma^2)\big)/2\) yields the stated character, multiplied by the row-swap sign.

## Verification
The standalone verifier `certificates/check_crown.py` independently enumerates **every nonempty vertex subset** at \(n=2,3,4,5,6\), checks its connected-component definition against the stated union of simplices, computes complete mod-two chain-boundary ranks, and checks all \(S_n\times C_2\) rational Lefschetz characters for \(n=3,4,5,6\). These include, respectively, 12, 48, 240, and 1440 group elements. It reports nonempty-face counts 15, 38, 76, 137, 237, and second reduced Betti ranks 0, 1, 3, 6, 10, respectively, with no other reduced mod-two Betti ranks. Results are recorded in `certificates/verification_output.txt`. These finite computations are auxiliary: the infinite-family integral homotopy and representation assertions follow from the exact decomposition, strong collapses, and natural relative homology sequence proved above.

## Relationship to prior work
Sawant's 2026 work on \(r\)-independence complexes of trees develops a vertex-decomposability framework for an emerging line of research (arXiv:2605.25150, first public 24 May 2026). Its theorem covers trees, while crown graphs contain induced cycles and are not trees. Deshpande and Singh (arXiv:2001.05448, Section 3, including their complete multipartite theorem) classify higher independence complexes of several other graph families. Although \(\operatorname{Cr}_3\cong C_6\) falls under their cycle classification, \(\operatorname{Cr}_n\) for general \(n\) is not a complete multipartite graph: each opposite-row vertex has a different unique missing cross-edge. The full infinite family and its integral \(S_n\times C_2\)-lattice are not supplied by those results. Patra and Roy (arXiv:2311.07308, Theorem 4.4) calculate algebraic invariants for complete multipartite graphs and related constructions, not this crown-graph integral homotopy theorem. Colbrook and Drysdale (arXiv:2609.35842) use crown graphs for a different representation-number question; only their bibliographic statement and abstract were compared. Claim-level searches using crown/matching-deleted complete bipartite/dissociation/three-vertex-path-free aliases and comparisons with indexed studies of two-row rook neighborhood complexes and two-point crown configurations did not reveal an equivalent classification. Absence from those searches is not proof of global uniqueness.

## Limitations
The nonequivariant equivalence with a sphere wedge does not assert an equivariant wedge splitting. The group-module formula is integral in reduced degree two, but it does not classify equivariant homotopy type or quotient-space integral homology. The direct computational checks cover only \(2\le n\le6\); they cannot replace the general proof. An unindexed earlier solution, or an implication from a not-inspected theorem, remains possible. No independent scientific audit is claimed.

## References
- R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1 (2026-05-24), https://arxiv.org/abs/2605.25150 .
- P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448 (first submitted 2020-01-15), https://arxiv.org/abs/2001.05448 .
- S. K. Patra and A. Roy, *Graded Betti numbers of a hyperedge ideal associated to join of graphs*, arXiv:2311.07308 (first submitted 2023-11-13), https://arxiv.org/abs/2311.07308 .
- M. Colbrook and C. Drysdale, *Crown graphs maximise the representation number of bipartite graphs*, arXiv:2609.35842v1 (2026-09-24), https://arxiv.org/abs/2609.35842 .
