# An edge-restoration transition for closed-neighborhood complexes of crown graphs

## Finding
Let \(\mathcal C(G)\) denote the **closed-neighborhood complex** of a finite simple graph \(G\): its simplices are the subsets of \(N_G[v]=\{v\}\cup N_G(v)\) for some vertex \(v\). For every nonempty finite bipartite graph \(G=(A\sqcup B,E)\) possessing a vertex in each part adjacent to *every* vertex of the opposite part, there is a homotopy equivalence
\[
|\mathcal C(G)|\simeq \Sigma|G|\simeq\bigvee^{\,|E|-|A|-|B|+1}S^2.
\]
Here \(|G|\) denotes the ordinary one-dimensional geometric realization, and the suspension is unreduced. The homotopy equivalence need not be canonical, but the integral isomorphism \(\widetilde H_2(\mathcal C(G);\mathbb Z)\cong H_1(G;\mathbb Z)\) arising as the Mayer–Vietoris connecting map is natural under edge-inclusion between bipartite graphs with the same vertex bipartition and the stated universal-vertex condition.

**Sharp edge-restoration filtration.** Let \(n\ge4\) and let \(G_{n,j}\), \(0\le j\le n\), have two parts \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with all cross edges except the pairs \(a_ib_i\) for \(1\le i\le n-j\). Write \(L_{n,j}=\mathcal C(G_{n,j})\) and \(b_n=n^2-3n+1\). Then \(L_{n,j}\subseteq L_{n,j+1}\), and
\[
\begin{aligned}
|L_{n,0}|&\simeq S^{n-2}\vee S^{n-2}\vee\bigvee^{b_n}S^2,\\
|L_{n,j}|&\simeq\bigvee^{b_n+j}S^2,\quad 1\le j\le n.
\end{aligned}
\]
For every \(j\ge1\) the map of reduced integral homology \(\widetilde H_2(L_{n,j})\to\widetilde H_2(L_{n,j+1})\) is a split injection with rank-one free cokernel. At the first restoration, the map \(\widetilde H_2(L_{n,0})\to\widetilde H_2(L_{n,1})\) has image rank \(b_n\) and free cokernel rank one. It is injective for \(n\ge5\), but for \(n=4\) its kernel has rank two. If \(n\ge5\), the two degree-\(n-2\) homology generators of \(L_{n,0}\) die under the first restoration (with degree-three generators when \(n=5\)). The homotopy description of \(L_{n,0}\) alone is previously known in the equivalent open-neighborhood guise and is expressly treated here as background, not as a new result.

## Assumptions and scope
All graphs are finite, simple, undirected and contain no isolated vertices in the stated general theorem. Each bipartition side is nonempty. The condition means \(a_\ast\in A\) satisfies \(N_G(a_\ast)=B\) and \(b_\ast\in B\) satisfies \(N_G(b_\ast)=A\); it forces connectedness. Graph inclusions preserve the labeled vertex set and bipartition. The zero sphere multiplicity denotes a contractible space. Homology is integral and reduced except where indicated. The entire filtration statement is for integers \(n\ge4\), \(0\le j\le n\), with no claim for higher homotopy groups of inclusion maps.

## Proof
**1. Exact two-hemisphere decomposition.** Put
\[
X=\bigcup_{b\in B}\Delta(N_G[b]),\qquad Y=\bigcup_{a\in A}\Delta(N_G[a]),
\]
where \(\Delta(S)\) denotes the simplex spanned by \(S\). By construction, \(\mathcal C(G)=X\cup Y\). A simplex of \(X\) has at most one vertex in \(B\), and a simplex of \(Y\) at most one in \(A\). Consequently every simplex in \(X\cap Y\) has size at most two. A cross edge \(\{a,b\}\) is in both exactly when \(ab\in E\): in \(X\) the only possible center containing \(b\) is \(b\) itself, and likewise for \(a\) in \(Y\). All graph vertices occur in both hemispheres, since they have neighbors. Thus the simplicial intersection \(X\cap Y\) is **exactly** the original graph \(G\), with no additional same-side edges or triangles.

**2. Explicit collapses of the hemispheres.** Each \(b\in B\) occurs in exactly one \(X\)-facet containing a vertex of \(B\), namely \(\Delta(\{b\}\cup N_G(b))\). Because \(N_G(b)\ne\varnothing\), the simplex \(\Delta(\{b\}\cup N_G(b))\) collapses relative to its nonempty base \(\Delta(N_G(b))\), deleting every face containing \(b\). These collapses do not interfere for distinct \(b\)'s, since their deleted faces contain different \(B\)-vertices. Hence
\[
X\searrow\bigcup_{b\in B}\Delta(N_G(b)).
\]
The latter union is a subcomplex of \(\Delta(A)\), and the universal vertex \(b_\ast\) contributes the **entire** simplex \(\Delta(A)\). Thus \(X\searrow\Delta(A)\). Symmetrically \(Y\searrow\Delta(B)\). In particular both hemispheres are nonempty and contractible.

**3. Homotopy pushout and natural homology.** The inclusions of the common simplicial subcomplex \(G\) into \(X,Y\) are cofibrations. The union is their homotopy pushout. Both target spaces are contractible; replacing the inclusions by constant maps yields the (unreduced) suspension \(\Sigma|G|\). Since \(G\) is a connected graph with cycle rank \(|E|-|A|-|B|+1\), its suspension has the asserted wedge-of-two-spheres homotopy type. The natural Mayer–Vietoris exact sequence of the two-hemisphere cover has connecting isomorphism \(\widetilde H_2(X\cup Y;\mathbb Z)\to H_1(X\cap Y;\mathbb Z)\), because the hemispheres are acyclic. All constructions respect an edge inclusion on the same bipartition, proving naturality.

**4. The first endpoint of the crown restoration.** For \(j=0\), the bases of the \(B\)-centered hemispheres are the \(n\) codimension-one facets \(A\setminus\{a_i\}\). Thus \(X_0\searrow\partial\Delta(A)\simeq S^{n-2}\); similarly \(Y_0\searrow\partial\Delta(B)\simeq S^{n-2}\). The intersection is the connected crown graph \(K_{n,n}\setminus M\), with \(2n\) vertices and \(n(n-1)\) edges, so its cycle rank is \(b_n=n^2-3n+1\). Since \(n\ge4\), the two hemispheres are simply connected, and every map from their connected one-dimensional intersection is nullhomotopic. The homotopy pushout splits as the wedge of both hemispheres and the suspension of the intersection, giving the displayed \(j=0\) formula. This endpoint is the known open-neighborhood complex of \(K_2\square K_n\), under the facet-identifying relabeling, and is not claimed as new.

**5. The restoration phase and maps.** For \(j\ge1\), a restored matching pair has an endpoint universal on each side. Step 3 therefore gives the sphere multiplicity \(|E(G_{n,j})|-2n+1=n(n-1)+j-2n+1=b_n+j\). Each added cross edge creates exactly one independent cycle in a connected graph; graph inclusion induces a split injection on integral \(H_1\) with free rank-one cokernel. The natural Mayer–Vietoris isomorphisms transfer this to the second-homology maps for \(j\ge1\).

At \(j=0\), Mayer–Vietoris instead gives a short exact sequence
\[
0\longrightarrow \widetilde H_2(X_0)\oplus\widetilde H_2(Y_0)\longrightarrow\widetilde H_2(L_{n,0})\longrightarrow H_1(G_{n,0})\longrightarrow0,
\]
since the two hemispheres have vanishing first homology. Under the inclusion into \(L_{n,1}\), the initial hemispheres map into contractible hemispheres, hence their second-homology images vanish. By naturality the induced map from the quotient \(H_1(G_{n,0})\) is the injective cycle-space inclusion into \(H_1(G_{n,1})\), with rank-one free cokernel. Therefore the image has rank \(b_n\), the kernel is exactly the old hemispherical \(H_2\)-subgroup, and the cokernel is \(\mathbb Z\). When \(n=4\), each initial hemisphere has one \(H_2\) generator, giving kernel \(\mathbb Z^2\); when \(n\ge5\) both initial hemisphere \(H_2\) groups are zero, giving injectivity. For \(n\ge5\), the two top-degree classes from \(S^{n-2}\) map to zero, because every target has homology only in degree two. This proves every asserted inclusion-map and homotopy-type statement.

## Verification
The accompanying standalone standard-library `verify.py` builds the closed-neighborhood simplices directly from graph adjacency, checks the exact hemisphere intersection, performs explicit elementary free-face collapses on both hemispheres, and computes mod-two reduced simplicial homology. It checks all \(26\) restoration stages with \(4\le n\le7\), independently generated \(64\) bipartite universal-pair graphs with each bipartition size between two and five, and (for \(n=4,5\)) all successive second-homology inclusion ranks using exact binary boundary elimination. The output `verification_output.txt` records the actual run. These finite checks are supplementary; the claims for all parameters follow from Steps 1–5, with integral maps established directly from graph cycle spaces.

## Relationship to prior work
T. Matsushita, *Closed neighborhood complexes of graphs* (arXiv:2511.12608; initially public 2025-11-16), introduces the exact closed-neighborhood construction and relates it to graph homotopy and path-group invariants; the inspected full text does not contain a universal-opposite-pair suspension criterion or the edge-restoration maps here.

The previously published *Neighborhood complexes of two-row rook graphs split into two spheres and a crown suspension* (published-finding corpus record `9b16e10ce620`, 2026-10-11), and *Open-neighborhood complexes of clique prisms: a mixed-dimensional sphere decomposition* (published-finding corpus record `d1fca5b06808`, 2026-10-11), determine \(\mathcal N(K_2\square K_n)\), which is simplicially isomorphic to **the un-restored endpoint** \(L_{n,0}\). This is full prior coverage of that endpoint, not merely analogous literature. Those theorems do not cover the closed-neighborhood complexes **after** a matching edge has been restored, arbitrary bipartite graphs with opposite universal vertices, or the maps through the endpoint transition. The result here is delimited to those new statements and an explicit transition in which the known endpoint is necessary context.

The published-finding corpus square-cell splitting result for triangle-free graphs with no \(K_{2,3}\) (`dff1a4056142`, 2026-10-11) has a different applicable domain: restored crown graphs contain \(K_{2,3}\) for the stated parameter range and are not covered by its normal form. Other published open-neighborhood square-free graph-spine theorems concern the **open** neighborhood functor rather than this closed-neighborhood construction. Search failures are not proof of priority.

## Limitations
The general suspension theorem requires a universal vertex on both opposite bipartition sides. The crown filtration begins at \(n=4\); the un-restored endpoint has pre-existing published coverage, explicitly credited above. The theorem does not give canonical wedge-summand identifications, global simplicial collapses of the entire closed-neighborhood complex, or higher-dimensional homotopy persistence. Bibliographic priority remains subject to older or unindexed equivalent results. Only self-review has been completed, not an independent audit.

## References
1. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608v1, 2025-11-16, https://arxiv.org/abs/2511.12608.
2. *Neighborhood complexes of two-row rook graphs split into two spheres and a crown suspension*, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-neighborhood-complexes-of-two-row-rook-graphs-split-into-two-sph--9b16e10ce620.
3. *Open-neighborhood complexes of clique prisms: a mixed-dimensional sphere decomposition*, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-open-neighborhood-complexes-of-clique-prisms-a-mixed-dimensional--d1fca5b06808.
4. *Square-cell splitting for closed neighborhood complexes of triangle-free graphs*, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-square-cell-splitting-for-closed-neighborhood-complexes-of-trian--dff1a4056142.
