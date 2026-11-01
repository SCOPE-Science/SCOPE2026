# Free fundamental groups of complex codimension-one \(\ell^p\) isometric-embedding spaces

## Finding
For every integer \(n\ge 2\) and every real \(1\le p<\infty\) with \(p\ne2\), let \(\mathcal I_{n,p}\) be the space of complex-linear isometric embeddings \(T:\ell_p^{n-1}(\mathbb C)\to\ell_p^n(\mathbb C)\), endowed with the operator-norm topology. It is path connected, and
\[
\boxed{\pi_1(\mathcal I_{n,p})\cong F_{\,1+(n-3)n!/2},}
\]
where \(F_k\) is the free group on \(k\) generators (\(F_0\) is trivial). Consequently,
\[
H_1(\mathcal I_{n,p};\mathbb Z)\cong\mathbb Z^{\,1+(n-3)n!/2}.
\]
The conclusion is independent of \(p\) throughout the stated non-Hilbert range. For \(n=2,3,4,5\), the free ranks are respectively \(0,1,13,121\).

## Assumptions and scope
The coordinate spaces have their standard complex \(\ell^p\) norms and no weights. An embedding is a **linear** map satisfying \(\|Tx\|_p=\|x\|_p\) for every input vector; it need not be onto. The parameter \(p\) is finite and not equal to \(2\), and \(n\) is finite and at least \(2\). The claimed fundamental group is based at any embedding, since the entire space is path connected. All topology on matrices is the finite-dimensional operator-norm topology. The claim concerns the **full** isometric-embedding space, not a single fixed-support stratum or the group of surjective isometries.

Write \(r=n-1\). The key structural fact is that every embedding's \(r\) columns have pairwise disjoint supports and individual \(\ell^p\) norm \(1\). Necessity follows from the strict scalar Clarkson equality criterion for \(p\ne2\): the equality \(\|u+v\|_p^p+\|u-v\|_p^p=2\|u\|_p^p+2\|v\|_p^p\) forces disjoint supports; sufficiency follows by summing coordinatewise. This is also the finite-atomic specialization of the Lamperti-type theorem in the first reference.

## Proof
### 1. Support geometry and independence of the exponent
With \(r=n-1\) nonempty disjoint column supports in \(n\) rows, precisely two types of supports can occur: all columns occupy a single row and one row is unused, or exactly one column occupies two rows while every other column occupies one. There can be no other type, since at most one row remains after allocating one to each column.

For a complex coordinate \(z\) set \(\Psi_p(z)=z|z|^{p/2-1}\), with \(\Psi_p(0)=0\). Coordinatewise application is a continuous, phase-equivariant homeomorphism between the \(\ell^p\) and Euclidean unit spheres, whose inverse uses exponent \(2/p-1\). Applied to each column, it identifies \(\mathcal I_{n,p}\) with the space of **Euclidean unit columns with pairwise disjoint supports**. This identification is not an assertion that all Euclidean isometries have disjoint supports. Work with the latter disjoint-column model below.

### 2. A graph of support transitions
A one-row-per-column configuration is indexed by an injection \(v:\{1,\dots,r\}\hookrightarrow\{1,\dots,n\}\). There are exactly \(V=n!\) such injections. Each gives a torus \(\mathbb T^r\) of independent column phases. Let \(G_n\) have these injections as vertices; join \(v\) to \(w\) if one column moves from its row to the unique previously empty row while all other columns remain fixed. These are exactly the pairs bounding a two-row-column stratum.

At every vertex there are \(r\) possible moves. Hence \(G_n\) is \(r\)-regular and has
\[
E=\frac{rn!}{2}=\frac{(n-1)n!}{2}
\]
undirected edges. Identify a vertex with a permutation of the \(n\) output rows, the final entry recording the unused row. An edge exchanges this unused row with the row occupied by one of the \(r\) columns. These star transpositions generate all permutations, so \(G_n\) is connected.

For each edge \(e\) labelled by the moving column \(j\), the closure of the corresponding configurations is \(S^3\times\mathbb T^{r-1}\): the moving column is \((z,w)\in\mathbb C^2\) with \(|z|^2+|w|^2=1\), and the unchanged \(r-1\) columns contribute phases. Its two endpoint tori are the loci \(w=0\) and \(z=0\). Distinct closed edge pieces meet only in such endpoint tori. Thus these pieces and the vertex tori describe **all** of the space, with their exact intersections.

### 3. The quotient by column phases
The torus \(\mathbb T^r\) acts by independently multiplying the \(r\) columns by complex phases. Because every column is nonzero, the action is free. Choosing locally one nonzero entry in each column and requiring it to have positive phase gives continuous local gauges; hence the quotient map is a principal \(\mathbb T^r\)-bundle
\[
\mathbb T^r\longrightarrow\mathcal I_{n,p}\longrightarrow Q_n.
\]
On a vertex torus the quotient is one point. On a closed edge piece \(S^3\times\mathbb T^{r-1}\), the quotient is the Hopf sphere \(S^3/\mathbb T\cong S^2\), with its north and south poles attached to the two vertices of the corresponding edge of \(G_n\). The base \(Q_n\) is therefore a graph of two-spheres: one sphere per edge, and spheres intersect only at the vertex points. As each sphere is simply connected, paths between its two attachment points are unique up to homotopy relative to their endpoints. The fundamental group of \(Q_n\) is the free group of the underlying connected graph:
\[
\pi_1(Q_n)\cong F_{E-V+1}.
\]

### 4. The fiber's phase loops all die
The homotopy exact sequence of the principal bundle contains
\[
\pi_2(Q_n)\xrightarrow{\partial}\pi_1(\mathbb T^r)\longrightarrow
\pi_1(\mathcal I_{n,p})\longrightarrow\pi_1(Q_n)\longrightarrow0.
\]
Fix an edge labelled by column \(j\). The restriction of this bundle to its embedded sphere \(S^2\subset Q_n\) is the standard Hopf fibration in the \(j\)-th circle factor, multiplied by a trivial \(\mathbb T^{r-1}\)-bundle. Therefore its connecting homomorphism takes that sphere class to \(\pm e_j\in\pi_1(\mathbb T^r)=\mathbb Z^r\). Every column label \(j\in\{1,\ldots,r\}\) occurs on an edge, so \(\partial\) is surjective. Exactness now makes \(\pi_1(\mathcal I_{n,p})\to\pi_1(Q_n)\) an isomorphism.

Finally,
\[
E-V+1=\frac{(n-1)n!}{2}-n!+1=1+\frac{(n-3)n!}{2}.
\]
Connectedness of the graph and connectedness of the torus fiber imply path connectedness of the total space. Abelianizing its free fundamental group gives the first-homology assertion. The formula also covers \(n=2\), where the embedding space is a complex \(\ell^p\) unit sphere homeomorphic to \(S^3\) and the rank is zero. This completes the proof.

## Verification
The proof is infinite in the dimension parameter and does not rely on enumeration. A supplementary standalone check, `verify_graph.py`, enumerates injections, support-transition edges, vertex degrees and connected components for \(2\le n\le7\). Running `python3 verify_graph.py` checks \(V=n!\), \(E=(n-1)n!/2\), graph connectedness and the claimed cycle ranks \(0,1,13,121,1081,10081\). The calculation tests only the combinatorial graph; it does **not** certify the Hopf-bundle exact-sequence step, which is proved above.

## Relationship to prior work
Dalfollo-Daley, Delfín, Fernández, Mars and Xia (arXiv:2610.32615v1, Theorem 3.18 and Proposition 4.5) classify finite-dimensional restricted \(\ell^p\) isometries and give the topology **within each fixed support pattern**. That theorem supplies the disjoint-support starting point, but its fixed-stratum product descriptions do not calculate the fundamental group obtained by gluing the strata at zero coefficients. The present result determines that global group and shows that all independent phase-circle generators disappear through the Hopf spheres. Lamperti's classical isometry theorem supplies the broader structural background.

For contrast, at the excluded Hilbert exponent \(p=2\), the full complex embedding space is the ordinary Stiefel manifold \(U(n)/U(1)\), which is simply connected. This standard observation is background, not an additional novelty claim. The non-Hilbert group is nontrivial for every \(n\ge3\) and nonabelian for every \(n\ge4\).

## Limitations
Only the fundamental group and its first-homology abelianization are calculated; no higher homotopy or complete homotopy type is claimed. The argument requires complex scalars, finite codimension-one target extension and \(p\ne2\); the topology of other dimension gaps and of real-valued embedding spaces is not covered. No assertion of definitive publication priority is made: an older treatment of these globally glued disjoint-support frame spaces under different terminology may exist.

## References
1. O. Dalfollo-Daley, A. Delfín, C. Fernández, C. Mars and X. Xia, *Restricted isometries in finite-dimensional \(\ell^p\)-spaces*, arXiv:2610.32615v1, first public October 23, 2026, https://arxiv.org/html/2610.32615v1. Theorem 3.18, Proposition 4.5 and Remark 3.19.
2. J. Lamperti, *On the isometries of certain function-spaces*, Pacific Journal of Mathematics **8** (1958), 459–466, https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-8/issue-3/On-the-isometries-of-certain-function-spaces/pjm/1103039892.full.
