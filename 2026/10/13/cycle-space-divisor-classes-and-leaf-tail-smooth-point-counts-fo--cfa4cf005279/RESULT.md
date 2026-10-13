# Cycle-space divisor classes and leaf-tail smooth-point counts for rooted-tree order varieties

## Finding
For a finite rooted tree \(T\), orient its Hasse edges away from the root, regarding ancestry as the partial order. Let \(X_T\) be the projective toric variety of its order polytope. Every torus-fixed point is indexed by a filter (upward-closed set) \(S\subseteq V(T)\); write \(p_S\) for that point, \(\mathcal F(S)\) for the minimal members of \(S\), and \(\ell(u)\) for the number of leaves in the subtree rooted at \(u\).

**Theorem.** For every such \(T\) and \(S\),
\[
\operatorname{Cl}(\mathcal O_{X_T,p_S})\cong
H^1(G_S;\mathbb Z)\cong
\mathbb Z^{\,\sum_{u\in\mathcal F(S)}(\ell(u)-1)},
\]
where \(G_S\) is the explicit active-facet graph defined in the proof. The first isomorphism is canonical relative to the oriented facet edges. In particular, these class groups have no torsion, and \(p_S\) is smooth if and only if it is locally \(\mathbb Q\)-factorial, if and only if every frontier vertex \(u\in\mathcal F(S)\) has exactly one descendant leaf.

Writing
\[
R_T(q)=\sum_{S\text{ a filter of }T}q^{\sum_{u\in\mathcal F(S)}(\ell(u)-1)},
\]
we have a complete recursive rank enumerator. If the root has child subtrees \(T_1,\ldots,T_d\), with \(L\) leaves altogether,
\[
R_T(q)=q^{L-1}+\prod_{i=1}^{d}R_{T_i}(q),
\qquad R_{\bullet}(q)=2.
\]
For \(L\ge2\), let \(b(\lambda)\) be the closest strict ancestor of a leaf \(\lambda\) having at least two children, and define the terminal unary-tail length \(t_\lambda\) as the number of edges from \(b(\lambda)\) to \(\lambda\). Then
\[
\#\{\text{smooth torus-fixed points on }X_T\}
=\prod_{\lambda\text{ leaf}}(t_\lambda+1).
\]
If \(L=1\), the tree is a chain with \(n\) vertices and all \(n+1\) fixed points are smooth. For the complete binary tree of height \(h\), the total and smooth fixed-point counts are respectively \(M_h\) and \(2^{2^h}\), where \(M_0=2\) and \(M_h=M_{h-1}^2+1\). In particular,
\[
\frac{2^{2^h}}{M_h}\le (4/5)^{2^{h-1}}\quad(h\ge1).
\]

## Assumptions and scope
All varieties are over \(\mathbb C\), and the toric lattice of \(\mathcal O(T)\) is \(\mathbb Z^{V(T)}\). The order polytope consists of \(0\le x_u\le1\) and \(x_u\le x_v\) for every ancestor-comparable pair \(u\le v\); it is normal and has full dimension \(n=|V(T)|\). The associated projective toric variety is equivalently the projective Hibi variety of the opposite poset \(T^{\mathrm{op}}\) (this removes a potential convention ambiguity). The roots-to-leaves orientation, the filter convention, and the characteristic function \(x_u=1\) for \(u\in S\) are used throughout. The empty filter is included: its frontier is empty and its class group is trivial.

A frontier vertex is a minimal selected vertex; since \(S\) is a filter, its selected vertices are the disjoint union of complete descendant subtrees rooted at \(\mathcal F(S)\). The leaf count \(\ell(u)\) includes all terminal leaves below \(u\), and is at least one. The complete binary tree has a single root, and every non-leaf vertex has two children, with leaves at depth \(h\).

## Proof
**1. Facets and active graph.** Standard facet theory for order polytopes yields precisely one lower facet \(x_r=0\) for the unique root, one upper facet \(x_\lambda=1\) for each terminal leaf, and one equality facet \(x_u=x_v\) for each parent-child cover edge \(u\to v\). At the filter vertex \(\mathbf1_S\), these are active exactly when (respectively) \(r\notin S\), \(\lambda\in S\), and \(\mathbf1_S(u)=\mathbf1_S(v)\).

Build \(G_S\) with vertices \(V(T)\cup\{*\}\). Keep an edge \(uv\) for every active cover facet, add \(r*\) when the lower-root facet is active, and add \(\lambda*\) for every active leaf-upper facet. Different leaves give different edges. Orient these edges arbitrarily, and assign potential zero to \(*\). The primitive active facet normals are, up to signs, the rows of the reduced integral incidence matrix of \(G_S\): the cover normal is \(e_v-e_u\), and a boundary normal is \(\pm e_u\).

The graph is connected. Every unselected vertex has all ancestors unselected and therefore has an active cover path to the unselected root and the edge \(r*\). Every selected vertex has a selected descendant leaf and an active cover path to that leaf and the edge \(\lambda*\). If there are no vertices of one type, only the other argument is needed. Thus all vertices reach \(*\).

**2. Integral class groups.** The toric divisor exact sequence on the affine chart of \(p_S\), or its local ring at the closed orbit, identifies its class group with the cokernel of the primitive-facet map
\[
\mathbb Z^{V(T)}\xrightarrow{\delta_S}\mathbb Z^{E(G_S)}
\longrightarrow\operatorname{Cl}(\mathcal O_{X_T,p_S})\longrightarrow0.
\]
Up to edge orientations \(\delta_S\) is the cellular coboundary map of the connected graph \(G_S\) with the \(*\)-potential set to zero. As any integer-valued vertex cochain has a unique representative vanishing at \(*\), the quotient is exactly \(H^1(G_S;\mathbb Z)\). In particular it is free, of rank \(|E(G_S)|-|V(G_S)|+1=|E(G_S)|-n\); a spanning-tree incidence minor has determinant \(\pm1\), so this is an integral, not merely a rational, statement.

For \(S\ne V(T)\), let \(c\) be the number of parent-zero-to-child-one boundary edges, and \(a\) the number of selected terminal leaves. Then the active cover count is \(n-1-c\), one root-lower facet is active, and \(a\) leaf-upper facets are active. Hence \(|E(G_S)|-n=a-c\). Here \(c=|\mathcal F(S)|\), while \(a=\sum_{u\in\mathcal F(S)}\ell(u)\), so the asserted rank follows. When \(S=V(T)\), the cover count is \(n-1\) and all \(L\) leaf-upper facets are active, giving rank \(L-1\), again the frontier sum since \(\mathcal F(S)=\{r\}\). For \(S=\varnothing\), both sides are zero.

**3. Smoothness and rank distribution.** At a torus-fixed point of an \(n\)-dimensional toric variety, the cone is simplicial exactly when its \(n\)-dimensional ray set has \(n\) rays; a toric cone is smooth precisely when those rays are a lattice basis. In our setting a zero cycle rank makes \(G_S\) a tree, so its \(n\) active normals have determinant \(\pm1\). A positive cycle rank gives more than \(n\) rays and non-\(\mathbb Q\)-factoriality. Hence smoothness, local \(\mathbb Q\)-factoriality, and vanishing of the above rank are equivalent. Because every summand \(\ell(u)-1\) is nonnegative, rank zero occurs exactly when every frontier subtree has one leaf.

A filter either contains the root, and is therefore the full vertex set (rank \(L-1\)), or excludes it, in which case it is independently specified by a filter of each child subtree. The rank of the latter is the sum of their ranks, including for a selected full child subtree. This proves the polynomial product recurrence and its base case.

If \(L\ge2\), a frontier subtree contains one leaf exactly when its root lies strictly below the closest branching ancestor of that leaf. For each leaf \(\lambda\), the frontier may be absent, or may consist of exactly one of the \(t_\lambda\) vertices on its terminal unary tail; these choices are independent across distinct leaves. The product counts all and only the smooth fixed points. For \(L=1\), every filter of the chain is a suffix and all \(n+1\) fixed points are smooth.

Finally, a complete binary height-\(h\) tree has \(2^h\) leaves and terminal unary-tail length one for every leaf, yielding \(2^{2^h}\) smooth points. The recurrence at \(q=1\) gives \(M_0=2\), \(M_h=1+M_{h-1}^2\). Since \(M_1=5\), induction gives \(M_h\ge5^{2^{h-1}}\) for \(h\ge1\); dividing \(2^{2^h}=4^{2^{h-1}}\) proves the stated exponentially decreasing proportion.

## Verification
Run `python3 CHECKER.py` with Python 3.9 or later (standard library only). The companion `CHECKER_OUTPUT.txt` is the exact stdout of the packaged code. The checker enumerates every rooted labeled tree with fixed root \(0\) on \(1\le n\le6\) vertices, and every filter of each tree. It builds the active facet normals independently from inequalities, extracts a spanning-tree minor, checks that its integer determinant has absolute value one, recomputes the local rank, compares the full rank distribution to the product recurrence, and compares the smooth-point count to the terminal-tail product. It also checks complete binary trees through height three.

The exhaustive finite tests cover 1,442 rooted labeled trees and 17,471 filters, plus the binary-tree cases with 2, 5, 26, and 677 filters. These are tests, **not** a proof for all orders; the preceding graph-cohomology and combinatorial arguments prove the infinite statement.

## Relationship to prior work
Stanley's 1986 order-polytope theory supplies the facet/vertex description. Wagner's 1996 singularity criterion already relates the smooth locus of general projective Hibi varieties to tree fibers of poset contractions; the qualitative smoothness characterization is therefore not claimed as independent of this older result. Lakshmibai–Mukherjee (2007) independently treat affine Hibi singular loci by cotangent spaces. Friedl (arXiv v1 2015) gives the global divisor-class group and local Cartier test for projective Hibi varieties. Those results provide essential groundwork, but the inspected statements do not present the **rooted-tree pointwise integral rank formula**, its complete weighted distribution recurrence, or the explicit smooth fixed-point product and binary-tree proportion. In particular, global class-group rank is not itself a pointwise class-group classification.

This specialization is intended as an exact family computation, not a replacement for the general earlier singular-locus theorems. The elementary cohomological presentation is made explicit to fix the integral lattice and torsion issue; its relationship to Friedl's graph-based global sequence is acknowledged.

## Limitations
This theorem concerns torus-fixed local rings and does not describe the class group at every non-fixed point, the complete singular scheme, canonical divisors, or analytic normal forms. It assumes the usual saturated order-polytope toric variety over \(\mathbb C\). The original contribution claimed is the combined pointwise rooted-tree classification and generating enumerations, **not** the established facet criterion or general Hibi smoothness theory. Closely related unpublished or unindexed enumerative formulas cannot be excluded by database searching, and the review is not independent verification.

## References
1. R. P. Stanley, *Two Poset Polytopes*, Discrete & Computational Geometry **1** (1986), 9–23, doi:10.1007/BF02187680, especially Section 1, facets and filter vertices.
2. D. G. Wagner, *Singularities of Toric Varieties Associated with Finite Distributive Lattices*, Journal of Algebraic Combinatorics **5** (1996), 149–165, doi:10.1023/A:1022469218716, especially Theorem 2.3.
3. V. Lakshmibai and H. Mukherjee, *Singular Loci of Hibi Toric Varieties*, arXiv:0706.2686v1 (18 June 2007), especially Theorem 6.9.
4. T. Friedl, *Divisors on Projective Hibi Varieties*, arXiv:1506.02407v1 (8 June 2015), especially Theorem 8 and Lemma 12.
5. D. Cox, J. Little and H. Schenck, *Toric Varieties*, AMS (2011), Chapter 4, toric divisor-class exact sequence.
