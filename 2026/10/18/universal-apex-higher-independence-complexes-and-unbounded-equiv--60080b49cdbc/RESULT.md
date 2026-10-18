# Universal-apex higher independence complexes and unbounded equivariant splitting obstructions

## Finding
Let \(G\) be a finite simple graph on \(n\ge2\) vertices, let \(2\le r\le n\), and write \(G^+=G*K_1\) for the graph with a new universal vertex. Then
\[
\operatorname{Ind}_r(G^+)\simeq \operatorname{Ind}_r(G)\vee\bigvee^{\binom{n-1}{r-1}}S^{r-1}.
\]
This is an ordinary homotopy equivalence compatible, up to homotopy, with the natural inclusion of \(\operatorname{Ind}_r(G)\).

For every subgroup \(\Gamma\le\operatorname{Aut}(G)\), acting on \(G^+\) with the new vertex fixed, there is a canonical **integral** exact sequence of \(\mathbb Z[\Gamma]\)-modules
\[
0\longrightarrow \widetilde H_{r-1}(\operatorname{Ind}_r(G);\mathbb Z)
\longrightarrow \widetilde H_{r-1}(\operatorname{Ind}_r(G^+);\mathbb Z)
\longrightarrow \bigwedge^{r-1}I_G\longrightarrow0,
\]
where \(I_G=\ker(\mathbb Z[V(G)]\xrightarrow{\mathrm{sum}}\mathbb Z)\).
In every degree other than \(r-1\), inclusion induces an integral homology isomorphism. The exact sequence splits as a sequence of abelian groups, but not necessarily as a sequence of integral symmetry modules.

In fact, for **every** integer \(n\ge3\), take \(G=K_n\), \(r=n-1\), and let \(C_n=\langle g\rangle\) rotate the old vertices. Put \(\epsilon=(-1)^{n-1}\), \(R=\mathbb Z[C_n]\), \(N_\epsilon=\sum_{j=0}^{n-1}\epsilon^jg^j\), and \(I_\epsilon=(g-\epsilon)R\). Then the preceding exact sequence identifies with
\[
0\longrightarrow\mathbb Z_\epsilon\xrightarrow{1\mapsto N_\epsilon}
R\xrightarrow{\,\cdot(g-\epsilon)\,} I_\epsilon\longrightarrow0,
\]
where the generator acts by \(\epsilon\) on \(\mathbb Z_\epsilon\). Its class is a generator of
\[
\operatorname{Ext}^{1}_{R}(I_\epsilon,\mathbb Z_\epsilon)\cong\mathbb Z/n\mathbb Z.
\]
Consequently, the inclusion \(\operatorname{Ind}_{n-1}(K_n)\subseteq\operatorname{Ind}_{n-1}(K_{n+1})\) **does not admit a \(C_n\)-equivariant homotopy retraction**. Its integral equivariant module extension has exact order \(n\), despite both complexes having torsion-free homology. These obstruction orders are unbounded. The latter statement concerns torsion in an extension group, **not** torsion in the spaces' ordinary homology.

## Assumptions and scope
The graph is finite, undirected, simple, and has \(n\ge2\) distinct vertices. A face of \(\operatorname{Ind}_r(G)\) is a vertex set whose induced graph has every connected component of size at most \(r\). The new apex is adjacent to every original vertex; all graph automorphisms considered fix that apex. All homology groups are reduced simplicial homology with integer coefficients, except the explicitly stated rational-character formula. Homotopy equivalences are of geometric realizations. No equivariant homotopy equivalence is claimed.

## Proof
**1. A cofiber decomposition for arbitrary graphs.** Set \(A=\operatorname{Ind}_r(G)\), and let \(B=\operatorname{sk}_{r-2}(\Delta^{n-1})\) be the complex of all subsets of the old vertices of size at most \(r-1\). Any apex-containing induced subgraph is connected, so that face is allowed precisely when the total size is at most \(r\). Thus, as actual simplicial complexes,
\[
K:=\operatorname{Ind}_r(G^+)=A\cup(a*B),\qquad A\cap(a*B)=B.
\]
For a fixed old vertex \(v\), every face of the cone \(v*B\) has at most \(r\) vertices, so \(v*B\subseteq A\). Therefore the inclusion \(B\hookrightarrow A\) is null-homotopic by an explicit cone null-homotopy. The union is its homotopy cofiber, giving \(K\simeq A\vee\Sigma B\). The usual elementary matching of the \((r-2)\)-skeleton of the \((n-1)\)-simplex relative to a fixed vertex leaves precisely \(\binom{n-1}{r-1}\) critical \((r-2)\)-cells and a basepoint. Equivalently \(B\simeq\bigvee^{\binom{n-1}{r-1}}S^{r-2}\). The splitting follows, including the claimed inclusion compatibility. The argument also covers \(r=2\): \(B\) is a disconnected set of \(n\) vertices and its suspension is a wedge of \(n-1\) circles.

**2. The canonical integral symmetry sequence.** The pair \((K,A)\), with cone attached along \(B\), has
\[
H_q(K,A;\mathbb Z)\cong\widetilde H_{q-1}(B;\mathbb Z)
\]
\(\Gamma\)-equivariantly. Since the inclusion \(B\hookrightarrow A\) is null-homotopic (though the displayed null-homotopy need not be \(\Gamma\)-equivariant), its map on integral homology is zero. The long exact sequence of the pair is therefore short exact in degree \(r-1\) and an isomorphism in all other degrees. Orient the simplex on its ordered vertex set, let \(P=\mathbb Z[V(G)]\), and use the augmented simplicial chain complex \(\bigwedge^\bullet P\), with differential contraction by the augmentation. Its degree-\((r-1)\) cycle lattice is \(\bigwedge^{r-1}I_G\): splitting the underlying abelian group \(P=\mathbb Zv\oplus I_G\) shows directly that the kernel of contraction in \(\bigwedge^{r-1}P\) is this exterior power, naturally under \(\Gamma\). Thus \(\widetilde H_{r-2}(B;\mathbb Z)\cong\bigwedge^{r-1}I_G\), yielding the asserted exact sequence. Its quotient is free abelian, hence it splits after forgetting \(\Gamma\).

For completeness, if a permutation \(h\in\Gamma\) has vertex cycle lengths \(\ell_1,\ldots,\ell_s\), its rational character increment in degree \(r-1\) is
\[
[t^{r-1}]\,\frac{\prod_{j=1}^s(1-(-t)^{\ell_j})}{1+t},
\]
as follows by the exterior-power determinant identity. This is an equality of virtual characters arising from the *exact* integral sequence; it does not assert an integral module splitting.

**3. An exact unbounded obstruction.** Set \(G=K_n\) and \(r=n-1\) for \(n\ge3\). Then \(A\) is the boundary of the \((n-1)\)-simplex on the old vertices, so its unique nonzero reduced integral homology is \(\widetilde H_{n-2}(A)\cong\mathbb Z_\epsilon\), with \(\epsilon=(-1)^{n-1}\) the orientation sign of the cyclic vertex permutation. The larger complex \(K\) is the \((n-2)\)-skeleton of the \(n\)-simplex on \(n+1\) vertices. For each old vertex \(i\), let \(\tau_i\) be the oriented boundary of the \((n-1)\)-simplex consisting of the apex and all old vertices except \(i\). Each \(\tau_i\) is a cycle in \(K\), has exactly one old-only \((n-2)\)-face, and its coefficient there is \(\pm1\). The complex has no higher-dimensional faces, and its top cycle rank is \(n\) by the simplex-skeleton computation. Furthermore any top cycle supported entirely in the apex cone must vanish, because a cone has no top cycles in that degree; comparing coefficients of the distinct old-only faces makes the \(\tau_i\) an integral basis. Thus cyclic permutation acts transitively on a basis up to consistent orientation choices, and \(\widetilde H_{n-2}(K)\cong R=\mathbb Z[C_n]\), the **regular integral** module.

Pick one cycle and take its full \(g\)-orbit as basis. The old boundary sphere is a primitive \(\epsilon\)-eigenvector, so its inclusion is, up to a global sign, exactly \(N_\epsilon=1+\epsilon g+\cdots+\epsilon^{n-1}g^{n-1}\). The image is the entire kernel of multiplication by \(g-\epsilon\) in \(R\), giving the exact sequence in the Finding. In particular, any \(R\)-map \(f:R\to\mathbb Z_\epsilon\) satisfies \(f(g^j)=\epsilon^j f(1)\), and hence \(f(N_\epsilon)=n f(1)\). It cannot restrict to the identity on \(\mathbb Z_\epsilon N_\epsilon\); no equivariant homology retraction, and therefore no equivariant homotopy retraction, can exist.

Finally, apply \(\operatorname{Hom}_R(-,\mathbb Z_\epsilon)\) to the projective middle term of \(0\to\mathbb Z_\epsilon N_\epsilon\to R\to I_\epsilon\to0\). Since \(\operatorname{Ext}^1_R(R,\mathbb Z_\epsilon)=0\), the resulting connecting map identifies
\[
\operatorname{Ext}^1_R(I_\epsilon,\mathbb Z_\epsilon)
\cong\operatorname{coker}\left(\operatorname{Hom}_R(R,\mathbb Z_\epsilon)\to\operatorname{Hom}_R(\mathbb Z_\epsilon N_\epsilon,\mathbb Z_\epsilon)\right)
\cong\mathbb Z/n\mathbb Z.
\]
The restriction map in the middle is multiplication by \(n\), and the displayed geometric extension maps to the identity on its kernel, hence represents \(1\pmod n\). Its order is exactly \(n\). This argument proves the *all-parameter* assertion without using finite computational extrapolation.

## Verification
The included `CHECK.py` is a reproducible Python 3 standard-library finite checker. It independently enumerates all vertex subsets and verifies the apex union for all labeled graphs on two, three and four vertices, covering 210 instances. It checks the homology-rank increment by exact sparse elimination modulo \(1000003\) on these instances and further named graphs on five and six vertices, covering 255 cases. It independently compares the character of simplex-skeleton homology via signed fixed faces against the exterior-power cycle-index formula for **every** permutation of up to seven vertices, covering 34,406 comparisons. A signed-facet check for complete graphs with three through nine old vertices verifies the primitive cyclic norm pattern. All checks passed on the packaged script; none is used as an infinite-case proof. The written cone, augmented-chain, and projective-resolution arguments prove the general claims.

## Relationship to prior work
Deshpande–Singh classify several families of higher-independence complexes, including complete multipartite graphs and cycles; their results do not state this arbitrary-graph universal-apex cofiber inclusion nor its integral equivariant extension class. Deshpande–Shukla–Singh establish homotopy sphere-wedge behavior for chordal graphs, encompassing the separate homotopy types of these complete-graph examples, but not the non-splitting of their *natural inclusion* under a cyclic symmetry. Patra–Roy give algebraic graded-Betti formulas for graph joins and wheel graphs. Those formulas bear on nonequivariant numerical invariants, but do not specify the cyclic integral module of the inclusion or compute the extension class of exact order \(n\). The standard cyclic norm exact sequence is used as an algebraic tool; its occurrence and exact obstruction order for these graph-filtration inclusions are the focus here. No claim is made that the sphere-skeleton ranks, cyclic norm resolution, or basic cofiber formalism themselves are new.

## Limitations
The nonequivariant splitting is not a \(\Gamma\)-equivariant wedge equivalence. The natural integral exact sequence may split for some groups and graphs; no general splitting criterion is claimed. The exact order calculation is for cyclic rotations of the complete-graph family, not all automorphism subgroups or all graphs. The absence of a \(C_n\)-equivariant retraction is an obstruction to retraction, not a classification of the full equivariant homotopy type. Known representation-theoretic descriptions of simplex skeleta are relevant prior algebraic background; inaccessible or unindexed equivalent statements remain a literature risk. No independent external mathematical audit is claimed.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, first public arXiv version 2020-01-15, arXiv:2001.05448, https://arxiv.org/abs/2001.05448.
2. P. Deshpande, S. Shukla and A. Singh, *Distance \(r\)-Domination Number and \(r\)-Independence Complexes of Graphs*, first public 2020-01-19, arXiv:2001.06775, https://arxiv.org/abs/2001.06775.
3. S. K. Patra and A. Roy, *Graded Betti Numbers of a Hyperedge Ideal Associated to Join of Graphs*, first public 2023-11-13, arXiv:2311.07308, https://arxiv.org/abs/2311.07308.
