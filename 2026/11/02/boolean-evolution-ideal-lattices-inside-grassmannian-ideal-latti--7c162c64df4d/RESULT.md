# Boolean evolution-ideal lattices inside Grassmannian ideal lattices of graph blowups

## Finding
Let \(H\) be a finite connected simple graph on \(n\ge2\) vertices, whose adjacency matrix is invertible over \(\mathbb R\), and let \(b\ge2\). Form the independent-fibre blowup \(G=H[\overline{K_b}]\): each vertex of \(H\) is replaced by \(b\) pairwise nonadjacent twins, with complete bipartite connections between fibres corresponding to edges of \(H\). Let \(E=E(G)\) be the real graph evolution algebra.

Write \(V_v=\operatorname{span}_{\mathbb R}\{e_{v,a}:1\le a\le b\}\), \(y_v=\sum_{a=1}^b e_{v,a}\), \(U=\bigoplus_v\mathbb R y_v\), and \(W_v=\{\sum_a c_a e_{v,a}:\sum_a c_a=0\}\). Then:

1. \(E^2=U\), and \(U\) is a simple \(n\)-dimensional evolution algebra. The **complete lattice of ordinary two-sided algebra ideals** is
   \[\{0\}\ \cup\ \{J:E^2\subseteq J\subseteq E\}\cong\{0\}\cup\mathcal L_{\mathbb R}(\mathbb R^{(b-1)n}),\]
   where the second part of the union is ordered as the subspace lattice through \(J\mapsto J/U\). In particular, \(U\) is the unique minimal nonzero ideal.
2. The **complete collection of evolution ideals having a natural basis extendible to a natural basis of \(E\)** consists of \(0\) and exactly the subspaces
   \[J(S_v)=\bigoplus_{v\in V(H)}(\mathbb R y_v\oplus S_v),\qquad S_v\le W_v.\]
   Thus the nonzero extension-property evolution-ideal poset is \(\prod_v\mathcal L_{\mathbb R}(\mathbb R^{b-1})\). In the double blowup \(b=2\), it is Boolean, with exactly \(2^n\) nonzero evolution ideals and one zero ideal; by contrast, the ordinary ideal lattice contains continuously many ideals.
3. For **any** connected \(d\)-regular base graph \(H\), even if its adjacency matrix is singular, the blowup has the proper evolution ideal \(U\) with an extendible natural basis over \(\mathbb R\). If \(H\) has edge Cheeger constant \(h(H)\ge h>0\), then
   \[h(G)\ge \frac{b h^2}{4d}.\]
   Consequently, the independent \(b\)-fold blowups of any bounded-degree regular expander family are themselves a uniformly expanding family of connected symmetric evolution algebras with proper evolution ideals.

A concrete nonsingular-base example is \(H=K_3\), \(b=2\), so \(G=K_{2,2,2}\). It has six vertices, degree four, \(h(G)=2\), and \(\dim E^2=3\). Its ordinary ideals are \(0\) and all subspaces containing \(E^2\), but it has exactly nine evolution ideals with the extension property (including zero).

## Assumptions and scope
An evolution algebra here is a commutative, generally nonassociative \(\mathbb R\)-algebra with natural basis \((e_x)\) and products \(e_xe_y=0\) for distinct basis vectors, \(e_x^2=\sum_{z\sim x}e_z\). An ordinary ideal means a linear subspace \(J\) with \(JE\subseteq J\). The stronger term *extension-property evolution ideal* means such an ideal having a natural basis which is a subset of some natural basis of \(E\); this is the restrictive evolution-ideal convention used in the motivating 2026 source. The exact lattice statements in parts 1 and 2 assume the base adjacency is nonsingular and use positivity of the Euclidean dot product over \(\mathbb R\). The expansion statement in part 3 does not assume nonsingularity. No assertion is made for arbitrary nonsymmetric evolution algebras or general characteristic.

## Proof
**Products and the square.** Every original basis vector in the fibre over \(v\) has the same square
\[e_{v,a}^2=s_v:=\sum_{w\sim_H v}y_w.\]
All mixed basis products vanish. Thus \(E^2=\operatorname{span}\{s_v:v\in V(H)\}\). When the adjacency matrix \(A_H\) is invertible, the vectors \((s_v)_v\) form a basis of \(U=\operatorname{span}\{y_v\}_v\), so \(E^2=U\). Its multiplication has the natural basis \((y_v)_v\), with
\[y_v^2=b\sum_{w\sim v}y_w=b s_v,\quad y_vy_w=0\quad(v\ne w).\]
In particular, \(U^2=U\), and it is simple: any nonzero ideal of \(U\), multiplied by a suitable \(y_v\), contains \(s_v\); multiplying this by \(y_w\) for a neighbor \(w\) gives \(b s_w\); connectedness propagates this to all \(s_w\), which span \(U\).

**All ordinary ideals.** If \(0\ne J\triangleleft E\), choose \(x=\sum c_{v,a}e_{v,a}\in J\) with \(c_{v,a}\ne0\). Then \(xe_{v,a}=c_{v,a}s_v\in J\). For every edge \(vw\) and every \(c\), we have \(s_v e_{w,c}=s_w\). By connectedness, \(J\) contains every \(s_w\), hence \(U\). Conversely, because \(E E=U\), every linear subspace containing \(U\) is automatically an ideal. This proves the complete ordinary ideal lattice and the uniqueness of the minimal nonzero ideal.

**Rigidity of natural bases.** For \(x,y\in E\), denote their components in \(V_v\) by \(x_v,y_v\). The multiplication formula is
\[xy=\sum_v\langle x_v,y_v\rangle s_v,\]
where \(\langle\ ,\ \rangle\) is the ordinary positive-definite Euclidean inner product in each fibre. Since the \(s_v\) are linearly independent, \(xy=0\) holds exactly when \(\langle x_v,y_v\rangle=0\) for every \(v\).

Take any natural basis \(B\) of \(E\). For each fixed \(v\), its nonzero fibre projections are pairwise orthogonal, so there are at most \(b\); since \(B\) spans \(E\), its projections span \(V_v\), so there are at least \(b\). Across the \(n\) fibres there are therefore exactly \(bn\) nonzero projections. As \(B\) has \(bn\) nonzero vectors and each has at least one nonzero projection, every member of \(B\) is supported in exactly one fibre. Moreover, its \(b\) vectors in any fibre form an orthogonal basis.

If a nonzero ideal \(J\) has a natural basis extendible to one of \(E\), this rigidity says \(J=\bigoplus_v T_v\) with \(T_v\le V_v\). The ordinary-ideal classification gives \(U\subseteq J\), hence \(\mathbb R y_v\subseteq T_v\) and uniquely \(T_v=\mathbb R y_v\oplus S_v\) for \(S_v\le W_v=y_v^\perp\). Conversely, for any such choices, take an orthogonal basis of every \(S_v\), extend it with \(y_v\) to an orthogonal basis of \(V_v\), and combine across fibres. This gives a natural basis of \(E\) containing a natural basis of \(J\). Since \(J\supseteq U=E^2\), it is indeed an ideal. This proves part 2.

**Expansion under blowup.** Suppose \(H\) is \(d\)-regular. The blowup is \(D=bd\)-regular, with adjacency matrix \(A_G=A_H\otimes J_b\). Its normalized adjacency eigenvalues are the normalized adjacency eigenvalues of \(H\), together with zero with multiplicity \((b-1)n\). If \(\delta_H\) and \(\delta_G\) are the second-smallest normalized Laplacian eigenvalues, then
\[\delta_G=\min\{1,\delta_H\}.\]
The usual Cheeger inequalities \(\delta_H\ge h(H)^2/(2d^2)\) and \(h(G)\ge D\delta_G/2\), together with \(h(H)\le d\), imply
\[h(G)\ge \frac{bd}{2}\min\left\{1,\frac{h(H)^2}{2d^2}\right\}\ge\frac{b h(H)^2}{4d}.\]
For any connected base, without requiring \(A_H\) invertible, the span \(U\) of the fibre sums is an ideal: \(y_v e_{w,a}\) is either zero or \(s_v\in U\). It is proper because \(b\ge2\). To see the restrictive extension property explicitly over \(\mathbb R\), use \(y_v\) and, within each fibre, \(w_{v,j}=\sum_{a=1}^{j}e_{v,a}-j e_{v,j+1}\) for \(1\le j<b\). These are nonzero pairwise orthogonal vectors, and their union is a natural basis of \(E\) extending \((y_v)_v\). Hence each such algebra has a proper extension-property evolution ideal. Taking any established bounded-degree regular expander family proves the asserted infinite-family construction.

## Verification
The standalone standard-library Python 3 program `verify.py` constructs graph adjacency matrices and multiplication tables directly. It exhausts every subspace of \(\mathbb F_2^4\), \(\mathbb F_3^4\), and \(\mathbb F_2^6\) for the indicated small blowups, tests ideal closure against every original generator, and checks the predicted complete lattice counts. The tested counts of ordinary ideals are 6 for \(K_{2,2}\) over \(\mathbb F_2\), 7 for \(K_{2,2}\) over \(\mathbb F_3\), and 68 for \(K_{2,2,2}\) over \(\mathbb F_2\). It independently exhausts all projective natural-basis candidates for \(K_{2,2}\) over \(\mathbb F_3\), finding five extension-property evolution ideals versus seven ordinary ideals. It also tests the explicit real orthogonal natural bases and enumerates edge cuts, obtaining \(h(K_{2,2,2})=2\). All checks returned `VERIFY_OK`. Finite-field tests corroborate the algebraic identities but do not substitute for the real-field proof, and the spectral bound is proved symbolically rather than inferred from small graphs.

## Relationship to prior work
Giacomelli (2026, arXiv:2605.12672v1, first public version May 12, 2026) defines expander evolution algebras via edge expansion and states in Theorem 3.8 that symmetric examples are simple. The construction here directly contradicts that assertion **even using its restrictive extension-property definition of evolution ideal**. The 2016 characterization of Cabrera Casado, Siles Molina, and Velasco already separates simplicity from graph connectivity by requiring nonsingularity; its general arguments explain why the ordinary square ideal need not be the whole algebra. Those established criteria and the classical Cheeger inequalities are used as context, not claimed as new. Cadavid, Rodiño Montoya, and Rodríguez (2018) study the twin partition of graph evolution algebras to classify derivations, not the two ideal lattices considered here. The proposed contribution is the exact contrast between the full and extension-property ideal lattices in a structured blowup family, its Boolean special case, and its persistence in uniformly expanding graph families.

## Limitations
The direct infinitary claim depends on the existence of an established bounded-degree regular expander family; it does not supply new explicit expander generators. The exact extension-property ideal classification assumes the base adjacency is invertible over \(\mathbb R\), and may not persist without that hypothesis or over fields with isotropic coordinate forms. The general ordinary-ideal argument partly specializes earlier simplicity and descendant-ideal theory; no claim is made that those ingredients are historically new. An older explicit extension-property ideal classification for these blowups under other terminology cannot be excluded solely by the searches reported. No independent mathematical audit or formal machine certification is claimed.

## References
1. P. Giacomelli, *Expander Evolution Algebras*, arXiv:2605.12672v1, first submitted May 12, 2026. https://arxiv.org/abs/2605.12672. Definitions 2.9 and 3.5; Theorem 3.8.
2. Y. Cabrera Casado, M. Siles Molina, M. V. Velasco, *Evolution algebras of arbitrary dimension and their decompositions*, arXiv:1601.01832, 2016. https://arxiv.org/abs/1601.01832. Sections 2 and 4, especially Theorem 4.7 and Corollary 4.10.
3. P. Cadavid, M. L. Rodiño Montoya, P. M. Rodríguez, *Characterization theorems for the spaces of derivations of evolution algebras associated to graphs*, Linear and Multilinear Algebra, 2018, DOI 10.1080/03081087.2018.1541962. Twin-class formulation and derivation classification.
4. Standard Cheeger inequalities for regular graphs, as quoted in Giacomelli, Sections 2 and 7, and the spectral theorem for adjacency Kronecker products.
