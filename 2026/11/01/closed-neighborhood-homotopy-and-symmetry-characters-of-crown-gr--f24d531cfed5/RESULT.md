# Closed-neighborhood homotopy and symmetry characters of crown graphs

## Finding
For each integer \(n\ge3\), let \(Q_n\) be the crown graph obtained from \(K_{n,n}\) by deleting one perfect matching, and let \(X_n=\mathcal N[Q_n]\) be its **closed-neighborhood complex**. There is a complete integral homotopy classification:
\[
|X_n|\simeq
\begin{cases}
 S^1,&n=3,\\
 \displaystyle S^{n-2}\vee S^{n-2}\vee\bigvee^{n^2-3n+1}S^2,&n\ge4.
\end{cases}
\]
In particular, \(|X_4|\simeq\bigvee^7 S^2\), while \(|X_5|\simeq\bigvee^{11}S^2\vee S^3\vee S^3\). Thus removing the matched edges of a complete bipartite graph creates two additional high-dimensional sphere classes for every \(n\ge5\). All integral homology is torsion-free.

For \(n\ge5\), the full natural symmetry group \(S_n\times C_2\) acts on both nonzero reduced homology groups. Let \(\pi\in S_n\) permute the matched indices simultaneously, let \(s\) exchange the two color classes, let \(f(\pi)\) be the number of fixed indices of \(\pi\), and let \(t(\pi)\) be the number of its two-cycles. The **integral degree-two module** is the crown graph's cycle lattice twisted by the sign character of the side exchange:
\[
\widetilde H_2(X_n;\mathbb Z)\cong H_1(Q_n;\mathbb Z)\otimes\chi_s,
\]
where \(\chi_s(\pi)=1\) and \(\chi_s(s)=-1\). The high-degree module is the tensor product of the sign representation of \(S_n\) with the two-dimensional integral side-permutation module:
\[
\widetilde H_{n-2}(X_n;\mathbb Z)\cong \operatorname{sgn}_{S_n}\otimes\mathbb Z\{u_A,u_B\},
\]
where \(s\) interchanges \(u_A,u_B\). Consequently the integral traces are
\[
\begin{aligned}
\operatorname{tr}(\pi_*\mid\widetilde H_2)&=f(\pi)^2-3f(\pi)+1,
&\operatorname{tr}((s\pi)_*\mid\widetilde H_2)&=2t(\pi)-1,\\
\operatorname{tr}(\pi_*\mid\widetilde H_{n-2})&=2\operatorname{sgn}(\pi),
&\operatorname{tr}((s\pi)_*\mid\widetilde H_{n-2})&=0.
\end{aligned}
\]
The two homological degrees are distinct under the module assertions' hypothesis \(n\ge5\). No equivariant splitting of the single degree-two group at \(n=4\) is asserted.

## Assumptions and scope
Write the vertex sets as \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\). There is an edge \(a_i b_j\) precisely when \(i\ne j\); there are no edges within a color class. The complex \(\mathcal N[G]\) comprises exactly the subsets contained in some **closed** neighborhood \(N_G[v]=\{v\}\cup\{w:vw\in E(G)\}\). It must not be confused with the Lovász open-neighborhood complex \(\mathcal N(G)\). All spaces are finite simplicial realizations, all homology coefficients are \(\mathbb Z\) unless specified otherwise, and \(\simeq\) denotes ordinary homotopy equivalence, not homeomorphism or equivariant homotopy equivalence. The graph automorphisms under discussion simultaneously permute matched pairs and optionally exchange the two sides.

## Proof
**1. Exact two-complex cover.** Define \(U\subseteq X_n\) to be the union of simplices on the closed neighborhoods centered at \(a_i\), and \(V\subseteq X_n\) similarly for centers \(b_i\). Thus
\[
 U=\bigcup_{i=1}^n\Delta(\{a_i\}\cup(B\setminus\{b_i\})),\qquad
 V=\bigcup_{i=1}^n\Delta(\{b_i\}\cup(A\setminus\{a_i\})).
\]
Every simplex of \(U\) contains at most one vertex from \(A\), and every simplex of \(V\) at most one vertex from \(B\). Their intersection is exactly the one-dimensional crown graph \(Q_n\): the mixed edges \(a_i b_j\) with \(i\ne j\), together with their vertices. Indeed a simplex in the intersection cannot have two vertices on either side. Every allowed mixed edge belongs to the facet centered at both its endpoints. Hence \(X_n=U\cup V\) and \(U\cap V=Q_n\) as simplicial complexes.

**2. Homotopy types of both pieces.** The pure \(B\)-faces of \(U\) form \(\partial\Delta(B)\), the boundary of the \((n-1)\)-simplex: the facets \(B\setminus\{b_i\}\) occur for all \(i\). For each \(i\), the simplex \(\Delta(\{a_i\}\cup(B\setminus\{b_i\}))\) is a cone on one boundary facet, attached along that entire facet, and distinct such cones meet only inside the boundary. Deform each cone linearly onto its attaching facet while fixing that facet; the deformations agree on all intersections. This gives a strong deformation retraction \(U\to\partial\Delta(B)\), equivariant for simultaneous index permutations. Similarly \(V\to\partial\Delta(A)\). Therefore \(U\simeq V\simeq S^{n-2}\). The two retractions are exchanged by \(s\).

**3. The small boundary.** For \(n=3\), the graph \(Q_3\) is a six-cycle. Each of the six neighborhood facets is a triangle. Its edge joining the two neighbors of its center is free: the two neighbors have that center as their unique common neighbor in the six-cycle. Collapsing these six triangles across those six free edges leaves exactly \(Q_3\). Thus \(X_3\searrow Q_3\cong C_6\simeq S^1\).

**4. Homotopy pushout for \(n\ge4\).** Both \(U\) and \(V\) are simply connected spheres up to homotopy, because \(n-2\ge2\). Every map from a connected graph to a simply connected space is null-homotopic (choose a spanning tree and contract the remaining loops). In particular, each of the inclusions \(Q_n\hookrightarrow U\) and \(Q_n\hookrightarrow V\) is null-homotopic. Since these are inclusions of simplicial subcomplexes, they are cofibrations and their ordinary union is a homotopy pushout. Replacing the two maps by constant maps in that pushout yields
\[
 X_n\simeq U\vee V\vee\Sigma Q_n.
\]
The connected graph \(Q_n\) has \(2n\) vertices and \(n(n-1)\) edges, so its first Betti number is \(n(n-1)-2n+1=n^2-3n+1\). A connected graph is a wedge of that many circles; its suspension is a wedge of that many two-spheres. Substitution gives the asserted ordinary homotopy equivalence for all \(n\ge4\), including the coincident-dimension case \(n=4\). This argument proves the full homotopy type, rather than inferring a sphere wedge merely from Betti numbers.

**5. Integral representations for \(n\ge5\).** In the natural Mayer--Vietoris sequence for \(X_n=U\cup V\), the graph \(Q_n\) has no homology above degree one, and \(U,V\) have their only positive reduced homology in degree \(n-2\ge3\). Therefore the connecting morphism
\[
\delta:\widetilde H_2(X_n;\mathbb Z)\xrightarrow{\cong}H_1(Q_n;\mathbb Z)
\]
is an integral isomorphism, and inclusion induces
\[
\widetilde H_{n-2}(U;\mathbb Z)\oplus\widetilde H_{n-2}(V;\mathbb Z)
\xrightarrow{\cong}\widetilde H_{n-2}(X_n;\mathbb Z).
\]
The first isomorphism is natural under side-preserving permutations; exchanging \(U\) and \(V\) reverses the Mayer--Vietoris connecting sign, producing \(\chi_s\). For the second, the equivariant retractions of step 2 identify the two top generators with the orientations of \(\partial\Delta(B)\) and \(\partial\Delta(A)\). Index permutations act on each by their permutation sign, while side exchange interchanges them. This proves the two **integral** module identities without choosing a rational splitting.

**6. Exact character formulas.** Orient each crown edge from \(A\) to \(B\). The cellular chain exact sequence of the connected graph gives, for every graph automorphism, \(\operatorname{tr}_{H_1}=\operatorname{tr}_{C_1}-\operatorname{tr}_{C_0}+1\). An index permutation with \(f\) fixed points fixes \(f(f-1)\) directed edges and \(2f\) vertices, yielding \(f^2-3f+1\). A side exchange composed with \(\pi\) fixes no vertices. An edge is setwise fixed exactly when its two indices form one of the \(t\) two-cycles of \(\pi\), giving \(2t\) such edges, each with reversed orientation; hence the graph-cycle trace is \(1-2t\). Twisting by \(\chi_s\) changes it to \(2t-1\). The two remaining traces follow immediately from the signed two-generator top module. All formulas hold integrally for every \(n\ge5\), with no assumption that the complex is a representation sphere.

## Verification
The standalone Python 3 checker `verify_crown_closed_neighborhood.py` builds every maximal simplex directly from crown-graph adjacency, expands all faces, forms augmented simplicial boundary matrices, and computes exact \(\mathbb F_2\) ranks. It checks the predicted nonzero reduced Betti degrees for all \(3\le n\le8\), including the exceptional dimensions at \(n=3,4\). It separately computes signed simplicial Lefschetz numbers for all index permutations at \(n=5\), and for a deterministic sample at \(n=6\), both with and without side exchange. All checks returned `FINITE_CHECK_OK` and `CHARACTER_CHECK_OK`. The unrestricted integral theorem follows from steps 1--6; finite characteristic-two checks are corroboration and do not detect hypothetical odd torsion on their own.

## Relationship to prior work
Matsushita's *Closed neighborhood complexes of graphs* [1] introduced a systematic treatment of \(\mathcal N[G]\), proved an equivalence relating its suspension to an independence complex of a canonical double cover, and identified its fundamental group. The full text inspected includes its Example 3.5, which determines a **different** family, namely closed-neighborhood complexes of \(K_m\square K_n\). Since \(Q_n\) is the **complement** of \(K_2\square K_n\), the example does not apply by a graph isomorphism. The general double-cover relation does not itself compute the unsuspended crown homotopy decomposition or its integral characters.

The complete-multipartite intrinsic graph Čech classification [2] computes, at scale two, the same closed-neighborhood construction on \(K_{n,n}\), giving a wedge of \((n-1)^2\) two-spheres. A crown \(Q_n\) is not complete multipartite for \(n\ge3\), so its deleted matched edges fundamentally change the facet intersection pattern; the mixed-dimensional homotopy and symmetry modules are not covered by [2]. A published classification of \(\mathcal N(K_m\square C_k)\) [3] uses **open** neighborhoods and a crown graph as an auxiliary relation graph, not closed neighborhoods of \(Q_n\) itself. The graph's algebraic cover ideals [4] address different invariants. These statement-level comparisons did not reveal a stronger theorem implying the entire present claim; indexing limitations remain.

## Limitations
The formula applies only to simple crown graphs with \(n\ge3\). The wedge decomposition is nonequivariant, and no equivariant homotopy classification is claimed. The integral character description is restricted to \(n\ge5\), where the two nonzero positive homology degrees are distinct; it does not assert an integral direct-sum decomposition of degree-two homology at \(n=4\). The result is a homotopy equivalence, not a simplicial collapse to a wedge of spheres. Finite computation and literature searches are not substitutes for the infinite proof or a comprehensive independent novelty audit.

## References
[1] T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608, first submitted 2025-11-16, https://arxiv.org/pdf/2511.12608; especially Definition 1.1, Theorem 1.2, Example 3.5 and Section 5.

[2] *Complete intrinsic graph Čech persistence of multipartite graphs, including their symmetry modules*, published mathematical result (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-intrinsic-graph-ech-persistence-of-multipartite-graphs--4c8b867ce9c1.

[3] *Mixed-dimensional neighborhood homotopy of complete-graph cycle products*, published mathematical result (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-mixed-dimensional-neighborhood-homotopy-of-complete-graph-cycle--3a53c8927b3c.

[4] A. Kumar, R. Kumar, R. Sarkar and S. Selvaraja, *Symbolic powers of certain cover ideals of graphs*, arXiv:1903.00178, https://arxiv.org/pdf/1903.00178, especially Section 3 on crown graphs.
