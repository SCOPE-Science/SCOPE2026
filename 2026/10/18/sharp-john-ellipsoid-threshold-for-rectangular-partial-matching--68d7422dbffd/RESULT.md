# Sharp John-ellipsoid threshold for rectangular partial matching polytopes

## Finding

For integers \(2\le a\le b\), let
\[
Q_{a,b}=\left\{X\in\mathbb R^{a\times b}: X_{ij}\ge0,\quad
\sum_{j=1}^b X_{ij}\le1\ (1\le i\le a),\quad
\sum_{i=1}^a X_{ij}\le1\ (1\le j\le b)\right\}.
\]
Equivalently, this is the full-dimensional convex hull of all partial permutation matrices, or the complete-bipartite matching polytope; matchings of *every* cardinality are included. Use the Frobenius Euclidean metric in its full \(ab\)-dimensional ambient space. Write \(R_{a,b}\) for the polytope obtained by omitting every column inequality. Thus \(R_{a,b}\) is a product of \(a\) standard coordinate \(b\)-simplices, and \(Q_{a,b}\subsetneq R_{a,b}\).

Put \(t=1/(b+1)\), \(J_b=\mathbf1_b\mathbf1_b^{\mathsf T}\), and
\[
S_b=\frac{(b+1)I_b-J_b}{b(b+1)^2},\qquad
\mathscr S=\operatorname{diag}(S_b,\ldots,S_b),\qquad
C=t\mathbf1_{a\times b}.
\]
The symmetric positive-definite operator \(\mathscr S\) has \(a\) blocks. Define
\[
\mathcal E^{\rm row}_{a,b}=\left\{C+Y:\operatorname{vec}(Y)^{\mathsf T}\mathscr S^{-1}\operatorname{vec}(Y)\le1\right\}.
\]
Here \(\operatorname{vec}\) stacks row coordinates. **The sharp survival theorem** is
\[
\boxed{\quad \mathcal E_J(Q_{a,b})=\mathcal E^{\rm row}_{a,b}
\ \Longleftrightarrow\ b+1\ge a+\sqrt a
\ \Longleftrightarrow\ b\ge a+\lceil\sqrt a\rceil-1.\quad}
\]
Equality of ellipsoids refers to their centers and positive-definite shape operators; the John ellipsoid is unique.

In the survival regime every coordinate facet and every row-cap facet touches this ellipsoid. Column-cap facets touch it **if and only if** \(b+1=a+\sqrt a\), a possibility only for square \(a\). The full list of its squared semiaxes is
\[
\frac1{b(b+1)^2}\quad\text{with multiplicity }a,
\qquad
\frac1{b(b+1)}\quad\text{with multiplicity }a(b-1).
\]
Its Euclidean volume, with \(\kappa_d=\pi^{d/2}/\Gamma(d/2+1)\), is
\[
\boxed{\operatorname{Vol}_{ab}(\mathcal E_J(Q_{a,b}))
=\kappa_{ab}\,b^{-ab/2}(b+1)^{-a(b+1)/2}.}
\]
If \(b+1<a+\sqrt a\), the row-product ellipsoid protrudes beyond every column supporting hyperplane by symmetry, so it is not the John ellipsoid of \(Q_{a,b}\). Nevertheless, in this regime **every column-cap facet touches** the *actual* unique John ellipsoid of \(Q_{a,b}\). This is a contact theorem, not a formula for that ellipsoid.

## Assumptions and scope

Throughout, \(a,b\) are integers satisfying \(2\le a\le b\). A Euclidean ellipsoid with center \(c\) and positive-definite shape operator \(\Sigma\) is the image of the unit Euclidean ball under \(z\mapsto c+\Sigma^{1/2}z\). For a supporting inequality \(\langle n,x\rangle\le d\), its exact maximum over the ellipsoid is \(\langle n,c\rangle+\sqrt{\langle n,\Sigma n\rangle}\). A facet is a contact facet if that maximum equals \(d\). The John ellipsoid is the unique maximum-volume full-dimensional ellipsoid contained in a convex body.

Both \(Q_{a,b}\) and \(R_{a,b}\) are full-dimensional. Heuer--Striker's partial-permutation-polytope description (Proposition 3.4 and Corollary 3.5) gives the complete irredundant facet list above for \(Q_{a,b}\). Its inequalities also follow from the bipartite matching-polytope description in Torres, Theorem 2.4. For \(a\ge2\), \(Q_{a,b}\ne R_{a,b}\): placing two ones in separate rows of the same column satisfies the row constraints but violates a column constraint.

## Proof

**1. Exact John ellipsoid of the row product.** The eigenvalues of \(S_b\) in the all-ones direction and on its orthogonal complement are, respectively, \(1/[b(b+1)^2]\) and \(1/[b(b+1)]\), hence \(S_b\) is positive definite. Direct multiplication gives
\[
S_b^{-1}=b(b+1)(I_b+J_b).
\]
For one simplex \(\Delta_b=\{x\ge0:\mathbf1_b^{\mathsf T}x\le1\}\), let \(c=t\mathbf1_b\). Its outward facet normals are \(n_j=-e_j\) for \(1\le j\le b\), together with \(n_{b+1}=\mathbf1_b\). Every facet has center-to-hyperplane margin exactly \(t\). Moreover,
\[
n_j^{\mathsf T}S_bn_j=t^2\quad(1\le j\le b+1),
\qquad \sum_{j=1}^{b+1}n_j=0,
\qquad \sum_{j=1}^{b+1}n_jn_j^{\mathsf T}=I_b+J_b.
\]
Thus the simplex ellipsoid \(c+S_b^{1/2}B_2^b\) contacts all its facets. Assign the positive equal weight \(w=b/(b+1)\) to each contact. In unit-ball coordinates, its contact normals are \(u_j=S_b^{1/2}n_j/t\). They satisfy the **exact John equations**
\[
\sum_j w u_j=0,\qquad \sum_j w u_ju_j^{\mathsf T}=I_b.
\]
Indeed the second equation follows from \(w(I_b+J_b)/t^2=S_b^{-1}\). John's contact criterion proves this is the **unique** John ellipsoid of \(\Delta_b\).

For the product of \(a\) simplices, concatenate the center and use the block diagonal shape \(\mathscr S\). Each row-block copy of the above facet contacts has zero first contact moment and identity second contact moment on that block. Their union has zero first moment and identity second moment on \(\mathbb R^{ab}\). The same John criterion establishes \(\mathcal E^{\rm row}_{a,b}=\mathcal E_J(R_{a,b})\) uniquely, with no assumption about symmetry.

**2. Exact column support.** Fix a column \(j\). Its cap inequality has outward normal \(N_j=\sum_{i=1}^a e_{ij}\) and right-hand side one. Because the rows are orthogonal shape blocks,
\[
\langle N_j,\mathscr S N_j\rangle
=\sum_{i=1}^a(S_b)_{jj}=a t^2,
\qquad
\langle N_j,C\rangle=a t.
\]
Consequently the exact column maximum over the row-product John ellipsoid is
\[
\max_{X\in\mathcal E^{\rm row}_{a,b}}\sum_iX_{ij}
=\frac{a+\sqrt a}{b+1}.
\]
All coordinate and row facets are already satisfied, with equality at their contact points. Hence \(\mathcal E^{\rm row}_{a,b}\subseteq Q_{a,b}\) exactly when \(b+1\ge a+\sqrt a\). Since \(Q_{a,b}\subseteq R_{a,b}\), every ellipsoid in \(Q_{a,b}\) is contained in \(R_{a,b}\). In the feasible regime, the unique John ellipsoid of \(R_{a,b}\) remains maximum-volume for \(Q_{a,b}\), and uniqueness gives the asserted equality. Conversely, if the inequality fails, this same ellipsoid is infeasible for \(Q_{a,b}\), so the two John ellipsoids cannot agree.

The integer cutoff follows by taking the least integer not smaller than \(a+\sqrt a-1\). Strict versus equality in the column support identity proves the asserted column-contact criterion. Equality requires \(\sqrt a\) integral and \(b=a+\sqrt a-1\).

**3. All column facets become active below the cutoff.** Suppose \(b+1<a+\sqrt a\). Let the actual unique John ellipsoid of \(Q_{a,b}\) have center \(C_Q\) and symmetric positive-definite square-root shape \(T_Q\). Permuting columns is an orthogonal symmetry of \(Q_{a,b}\), so John's uniqueness ensures that all column-cap support margins of this ellipsoid are equal. Suppose all were strictly positive.

Let \(C_R=C\) and \(T_R=\mathscr S^{1/2}\) describe the row-product John ellipsoid. For \(0<\varepsilon<1\), consider the ellipsoid described by
\[
C_\varepsilon=(1-\varepsilon)C_Q+\varepsilon C_R,
\qquad T_\varepsilon=(1-\varepsilon)T_Q+\varepsilon T_R.
\]
For every coordinate or row-cap inequality \(\langle n,x\rangle\le d\), the constraint \(\langle n,C_\varepsilon\rangle+\|T_\varepsilon n\|_2\le d\) follows from the triangle inequality and the fact that both endpoint ellipsoids lie in \(R_{a,b}\). Every column-cap inequality remains satisfied for sufficiently small positive \(\varepsilon\), because its support was strictly below one at \(\varepsilon=0\) and varies continuously. Hence the interpolated ellipsoid lies in \(Q_{a,b}\).

But \(\mathcal E^{\rm row}_{a,b}\) is not contained in \(Q_{a,b}\), whereas \(\mathcal E_J(Q_{a,b})\subset R_{a,b}\); uniqueness of the John ellipsoid of \(R_{a,b}\) implies \(\det T_R>\det T_Q\). Concavity of \(\log\det\) on the positive-definite cone then gives
\[
\log\det T_\varepsilon\ge(1-\varepsilon)\log\det T_Q+
\varepsilon\log\det T_R>\log\det T_Q.
\]
This contradicts optimality in \(Q_{a,b}\). Therefore no column-cap facet can be slack, and by column-permutation symmetry **all** of them touch its true John ellipsoid.

**4. Shape spectrum and volume.** The eigenvalues of \(S_b\) calculated in step 1 occur once and \(b-1\) times per row. Thus \(\det\mathscr S=b^{-ab}(b+1)^{-a(b+1)}\). The volume of the ellipsoid equals \(\kappa_{ab}\sqrt{\det\mathscr S}\), proving the formula.

## Verification

The companion self-contained program `verify.py` uses exact rational arithmetic to reconstruct the inverse shape, every coordinate and row-cap support equality, the weighted contact-frame equations, the two semiaxis values, and the integer cutoff for all \(2\le a\le12\) and \(a\le b<a+12\). It also tests the contact boundaries \((a,b)=(4,5),(9,11)\), and the contrasting regimes \((5,6)\) and \((5,7)\). It produces `VERIFY_OK cases=132 stable=110 changed=22 boundary=[(4, 5), (9, 11)]`. These finite verifications corroborate, but **do not prove**, the infinite-family theorem; that rests on the contact certificate, exact support calculation, and interpolation argument.

## Relationship to prior work

Heuer and Striker characterize the relevant partial-permutation / doubly substochastic polytopes, their vertices, facets, and selected enumeration and volume questions. Torres gives the general bipartite matching-polytope inequality description and results on the fixed-cardinality cases and normality. These papers identify the objects and inequalities used here, but their inspected statements and proofs do not yield the **sharp rectangular row-John survival cutoff**, the column-contact transition, or the resulting ellipsoid volume in the survival range.

Specializing to square matrices gives \(a=b\ge2\), which lies strictly outside the new ellipsoid-survival regime; a rectangular threshold cannot follow from a square-parameter treatment. Fixed-cardinality assignment-polytope theorems concern codimension-one slices and do not automatically determine a volume-optimal ellipsoid of the whole matching polytope. The row-product John ellipsoid is a standard product-simplex construction; the new result is precisely the sharp survival and contact behavior when *all genuine column constraints are added*.

## Limitations

The theorem **does not specify** the true John ellipsoid's complete spectrum or volume in the subcritical regime \(b+1<a+\sqrt a\); it proves only non-survival of the row-product ellipsoid and mandatory column-facet contact there. The classification is for complete bipartite matching polytopes with uniform unit capacities, not arbitrary bipartite graphs, weighted capacities, or fixed-cardinality slices. Exact inequalities and ellipsoid uniqueness are proved for the standard Frobenius metric; arbitrary affine coordinate changes can be transported geometrically, but the displayed shape is metric-dependent. Publication-priority checks of the most relevant literature are not exhaustive; a related study of square doubly substochastic polytope faces was accessible only through its abstract.

## References

1. Dylan Heuer and Jessica Striker, *Partial Permutation and Alternating Sign Matrix Polytopes*, arXiv:2012.09901 (first publicly posted 2020-12-17), especially Section 3, Proposition 3.4 and Corollary 3.5, https://arxiv.org/abs/2012.09901 .
2. Juan Camilo Torres, *Normality of k-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910 (first publicly posted 2023-06-20), especially Theorem 2.4, https://arxiv.org/abs/2306.11910 .
3. J. Cao and G. Chen, *Faces of the Polytope of Doubly Substochastic Matrices*, Linear Algebra and its Applications (2022), DOI:10.1016/j.laa.2021.11.012. Only the abstract was available for the present comparison.
4. F. John, *Extremum problems with inequalities as subsidiary conditions*, in *Studies and Essays Presented to R. Courant on his 60th Birthday*, 1948, pp. 187–204 (John's ellipsoid/contact characterization).
