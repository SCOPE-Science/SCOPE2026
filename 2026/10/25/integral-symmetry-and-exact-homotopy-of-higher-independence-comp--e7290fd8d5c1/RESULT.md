# Integral symmetry and exact homotopy of higher independence complexes of double-star trees

## Finding

Let \(D_{a,b}\) be the tree formed from an edge joining centers \(u,v\) by attaching \(a\ge1\) leaves to \(u\) and \(b\ge1\) leaves to \(v\), and set \(t=a+b\). For every integer \(r\ge2\), its higher independence complex \(X=\operatorname{Ind}_r(D_{a,b})\) has

\[
X\simeq\begin{cases}
\bigvee^{\binom{t-1}{r-2}}S^{r-1},&2\le r\le t+1,\\
\mathrm{point},&r\ge t+2.
\end{cases}
\]

Let \(L\) be the set of all leaves and let \(E=\ker(\mathbb Z[L]\xrightarrow{\epsilon}\mathbb Z)\), where \(\epsilon\) sums coefficients. An automorphism \(g\) permutes the two centers, and \(\varepsilon(g)\in\{1,-1\}\) denotes the sign of that permutation. There is a **natural isomorphism of integral automorphism modules**

\[
\widetilde H_{r-1}(X;\mathbb Z)\cong \mathbb Z_{\varepsilon}\otimes\bigwedge^{r-2}E,
\qquad
\widetilde H_j(X;\mathbb Z)=0\quad(j\ne r-1).
\]

The exterior power is zero when \(r-2>t-1\). If \(g\) permutes the leaves in cycles \(C\), then its complete rational homology character is

\[
\chi_{r-1}(g)=\varepsilon(g)[z^{r-2}]
\frac{\prod_C\bigl(1-(-z)^{|C|}\bigr)}{1+z}.
\]

In particular, the quotient by the **full graph automorphism group** has exactly one reduced rational homology generator, in degree \(r-1\), for \(a\ne b\) and \(r\in\{2,3\}\), or for \(a=b\) and \(r=3\). In all other parameters the quotient is rationally acyclic. These are rational quotient claims, not assertions of quotient contractibility.

## Assumptions and scope

The graph is finite and simple. A face \(F\subseteq V(D_{a,b})\) belongs to \(\operatorname{Ind}_r(D_{a,b})\) exactly when every connected component of the induced graph \(D_{a,b}[F]\) has at most \(r\) vertices. Write \(A,B\) for the sets of leaves at the respective centers, so \(|A|=a\), \(|B|=b\), \(L=A\sqcup B\). Write \(\Delta_S\) for the full simplex on \(S\), \(\operatorname{sk}_d\Delta_S\) for its \(d\)-skeleton, and \(*\) for simplicial join. The complex \(\{\varnothing\}\) contains precisely the empty face and has reduced augmented homology \(\mathbb Z\) in degree \(-1\); this convention is essential when \(r=2\). The zero-fold wedge means a point. All group actions are induced by graph automorphisms.

## Proof

**1. Two contractible pieces.** Let \(Y\subseteq X\) be the subcomplex of faces missing at least one center. Every subset of \(L\) is a face, and an induced component containing only \(u\) has \(1+|F\cap A|\) vertices. Consequently, writing joins with a vertex as cones,

\[
Y=\Delta_L\ \cup\ \bigl(u*(\operatorname{sk}_{r-2}\Delta_A*\Delta_B)\bigr)
\ \cup\ \bigl(v*(\Delta_A*\operatorname{sk}_{r-2}\Delta_B)\bigr).
\]

Both cone bases contain the entire simplex on the opposite, nonempty leaf set: hence both bases are contractible. Attach the \(u\)-cone first to \(\Delta_L\), and then the \(v\)-cone. The first intersection is its base; the second intersection is also its base because the two cone pieces meet only in \(\Delta_L\). Attaching a cone along a contractible subcomplex to a contractible complex preserves contractibility, so \(|Y|\) is contractible.

Let \(K=\{F\subseteq L: |F|\le r-2\}=\operatorname{sk}_{r-3}\Delta_L\), including its empty face. Faces of \(X\) containing both centers have a connected component of size \(2+|F\cap L|\). Thus the second contractible piece is \(Z=\Delta_{\{u,v\}}*K\). Direct face inspection gives

\[
X=Y\cup Z,\qquad Y\cap Z=\partial\Delta_{\{u,v\}}*K.
\]

The geometric intersection is the suspension \(\Sigma|K|\) for nonempty realization. In the augmented \(r=2\) convention, it is two distinct center points. Both inclusions are cofibrations; the union of two contractible subcomplexes has homotopy type of the suspension of the intersection. It follows that \(X\simeq\Sigma^2K\) for \(r\ge3\), and \(X\simeq S^1\) for \(r=2\).

**2. Integral groups and homotopy type.** Put \(P=\mathbb Z[L]\) and \(k=r-2\). For \(0\le k\le t-1\), the only nonzero reduced augmented integral homology of the truncated simplex \(K\) is

\[
\widetilde H_{k-1}(K;\mathbb Z)
=\ker\!\left(\iota_\epsilon:\bigwedge^kP\longrightarrow\bigwedge^{k-1}P\right)
=\bigwedge^kE.
\]

For \(k=0\), the codomain is zero by convention. The first identification follows because the truncated simplex has every face below cardinality \(k\), so its augmented boundary complex agrees below degree \(k-1\) with that of the full simplex and has no chains above degree \(k-1\). To prove the second identification **over the integers**, choose any distinguished leaf \(w\), write \(P=\mathbb Zw\oplus E\) using \(e_x=x-w\), and decompose

\[
\bigwedge^kP=\bigwedge^kE\ \oplus\bigl(w\wedge\bigwedge^{k-1}E\bigr).
\]

Contraction by augmentation vanishes on the first summand and maps the second isomorphically onto \(\bigwedge^{k-1}E\). Thus the kernel is precisely \(\bigwedge^kE\), a free integral lattice of rank \(\binom{t-1}{k}\). The skeleton is a wedge of \(\binom{t-1}{k}\) spheres of dimension \(k-1\): one can see this by inducting on the number of vertices using deletion/link, with the base case \(k=0\) treated by the augmented \((-1)\)-sphere convention; alternatively, its \((k-2)\)-connectedness and its dimension \(k-1\) imply this standard skeleton classification when \(k\ge2\). Double suspension now gives the first claimed homotopy equivalence, including \(r=2\) and \(r=3\). For \(r\ge t+2\) the entire graph vertex set is a face and \(X\) is a simplex, so is contractible.

**3. Natural integral group action.** The reduced Mayer–Vietoris connecting isomorphism for \(Y\cup Z\) sends \(\widetilde H_{r-1}(X;\mathbb Z)\) to \(\widetilde H_{r-2}(Y\cap Z;\mathbb Z)\). The latter suspension isomorphism arises by joining a leaf cycle with the oriented center difference \([u]-[v]\). A leaf permutation acts on the leaf cycle by its exterior-power action on \(E\). Exchanging the two centers changes the sign of \([u]-[v]\). Naturality of the boundary map establishes the integral representation with the center-sign twist. No choice of distinguished leaf enters the resulting kernel identification.

For a permutation \(g\) on \(L\) with cycle lengths \(|C|\), the determinant generating series on \(P\) is \(\det(1+zg|P)=\prod_C(1-(-z)^{|C|})\). Since \(P_\mathbb Q\cong\mathbb Q\oplus E_\mathbb Q\), division by \(1+z\) gives the exterior-power character, then multiplication by \(\varepsilon(g)\) gives the displayed formula.

**4. Quotient invariants.** For \(a\ne b\), the full automorphism group is \(S_a\times S_b\); for \(a=b\), it is \((S_a\times S_a)\rtimes C_2\), the involution exchanging centers and the two leaf sets. Over \(\mathbb Q\), restricted to the product group, \(E\) decomposes as \(U_a\oplus U_b\oplus\mathbb Q q\), where \(U_j\) is the augmentation module on a block of \(j\) leaves and \(q\) is the block-relative-mean line. No positive exterior power of \(U_j\) has a trivial \(S_j\)-subrepresentation: for \(1\le h\le j-1\), \(\bigwedge^hU_j\) is the nontrivial hook Specht module, and its invariants vanish (the \(j=1\) case contributes zero). Hence \((\bigwedge^kE)^{S_a\times S_b}\) is one-dimensional only for \(k=0,1\), zero otherwise. In the balanced case, exchanging the blocks acts as \(-1\) on \(q\), and the center-sign factor is also \(-1\), so only the \(k=1\) line survives full invariants. Rational homology of a finite-group quotient equals invariant rational homology after barycentric subdivision and averaging, proving the quotient assertion.

## Verification

The accompanying `check_bistar.py` independently reconstructs the induced-component face predicate, exhaustive mod-two augmented boundaries, and signed Lefschetz traces. It checks all \(45\) cases with \(1\le a,b\le3\) and \(2\le r\le a+b+2\); within-block leaf automorphisms and balanced block interchanges are checked. Successful output is `DOUBLE_STAR_HIGHER_INDEPENDENCE_CHECKS_PASSED 45 cases; homology and all branch automorphisms`. The finite experiments corroborate, but are not a substitute for, the proof for arbitrary parameters. For a concrete sample, \(a=b=2\), \(r=3\) gives \(\bigvee^3S^2\), and only a one-dimensional rational top homology survives quotient by the full eight-element automorphism group.

## Relationship to prior work

Deshpande and Singh (arXiv:2001.05448, first public 2020-01-15) established higher independence-complex homotopy types of complete multipartite, fully whiskered, cycle, and perfect rooted-tree families. Their formulas cover some degenerate/special cases, but do not furnish this bistar-wide integral automorphism module. Deshpande, Shukla and Singh (arXiv:2001.06775) establish general wedge-of-spheres results for chordal graphs, which imply only qualitative information here. Abdelmalek, Deshpande, Goyal, Roy and Singh (arXiv:2106.10863) treat caterpillar vertex decomposability; Sawant (arXiv:2605.25150) treats all trees. Neither of the inspected general vertex-decomposability theorems yields the exact binomial homotopy rank, the integral automorphism module, or the rational homology of the full automorphism quotient. The claim is this quantitative and equivariant refinement, not the generic fact that a tree yields a sphere wedge.

## Limitations

The construction assumes two nonempty leaf groups and integer \(r\ge2\); it makes no assertion about the distinct ordinary-independence regime \(r=1\). The displayed group module is an integral homology representation, not an equivariant homotopy classification. The quotient calculation is rational; the integral torsion or fundamental group of orbit spaces is not determined. An earlier unindexed equivalent formula is possible despite the targeted literature comparisons. No independent audit has been performed.

## References

1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, initial version 2020-01-15, https://arxiv.org/abs/2001.05448.
2. P. Deshpande, S. Shukla and A. Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775, initial version 2020-01-19, https://arxiv.org/abs/2001.06775.
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, initial version 2021-06-21, https://arxiv.org/abs/2106.10863.
4. R. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150, initial version 2026-05-24, https://arxiv.org/abs/2605.25150.
