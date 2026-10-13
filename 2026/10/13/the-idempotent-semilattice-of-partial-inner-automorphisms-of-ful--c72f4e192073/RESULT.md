# The idempotent semilattice of partial inner automorphisms of full linear monoids

## Finding

Let \(K\) be an arbitrary field, \(n\ge 2\), \(V=K^n\), and \(S=\operatorname{End}_K(V)\) under composition. Let \(\operatorname{Inn}(S)\) denote the inverse monoid of partial inner automorphisms as in Araújo et al. [1]. For any subspaces \(U,W\le V\), put

\[
\mathcal B(U,W)=\{A\in\operatorname{End}_K(V):\operatorname{im}A\subseteq U,\; W\subseteq\ker A\}.
\]

These are multiplication-closed linear subspaces, canonically identified as vector spaces with \(\operatorname{Hom}_K(V/W,U)\). Write \(\mathbf 1_X\) for the partial identity whose domain is \(X\subseteq S\). **The complete idempotent semilattice is**

\[
E(\operatorname{Inn}(S))
=\{\mathbf1_S,\mathbf1_{\{0\}}\}
\;\sqcup\;
\{\mathbf1_{\mathcal B(U,W)}:0<U<V,\ 0<W<V\}.
\]

Every displayed middle element is different, with multiplication

\[
\mathbf1_{\mathcal B(U,W)}\,\mathbf1_{\mathcal B(U',W')}
=\mathbf1_{\mathcal B(U\cap U',W+W')}.
\]

If one of the two new subspaces is zero or all of \(V\), the right-hand side means \(\mathbf1_{\{0\}}\); the top element is the identity on \(S\). In particular, the middle partial order is the product of the proper nonzero subspace lattice with its dual:

\[
\mathbf1_{\mathcal B(U,W)}\le\mathbf1_{\mathcal B(U',W')}
\quad\Longleftrightarrow\quad U\subseteq U'\text{ and }W'\subseteq W.
\]

For \(K=\mathbb F_q\), every prime power \(q\), the **exact number** of idempotents is

\[
\boxed{\displaystyle
|E(\operatorname{Inn}(M_n(\mathbb F_q)))|
=2+\left(\sum_{r=1}^{n-1}{n\brack r}_q\right)^2.}
\]

Here \({n\brack r}_q\) denotes the Gaussian binomial coefficient. If \(u=\dim U\) and \(w=\dim W\), the domain \(\mathcal B(U,W)\) has \(q^{u(n-w)}\) matrices; there are precisely \({n\brack u}_q{n\brack w}_q\) distinct middle idempotents with those dimensions.

A further structural boundary is

\[
\mathcal B(U,W)^2=\{0\}\quad\Longleftrightarrow\quad U\subseteq W,
\]

so the exact count of idempotents whose domains are square-zero subsemigroups, including \(\mathbf1_{\{0\}}\), is

\[
\boxed{\displaystyle 1+\sum_{w=1}^{n-1}{n\brack w}_q\sum_{u=1}^{w}{w\brack u}_q.}
\]

This classifies the idempotent semilattice, **not** the other elements of the inverse monoid and not arbitrary partial automorphisms of \(S\).

## Assumptions and scope

All vector spaces and linear maps are over the same arbitrary field \(K\). The dimension \(n\) is a finite integer at least two. Matrix multiplication is functional composition \(AB=A\circ B\). The cited construction [1, Definition 3.8] generates \(\operatorname{Inn}(S)\) from maps

\[
\phi_{g,h}:D_{g,h}\longrightarrow D_{h,g},\quad
D_{g,h}=\{A\in S:(gh)A=A=A(gh)\},\quad A\mapsto hAg,
\]

with arbitrary \(g,h\in S\). The inverse of \(\phi_{g,h}\) is \(\phi_{h,g}\). All these domains contain the zero matrix. Consequently \(\mathbf1_{\{0\}}\), not the empty partial identity, is the least element in the present inverse monoid.

## Proof

**1. Rectangular domains.** For any \(e\in S\), write \(T=e-I\). Then

\[
D_{e,I}=\{A:eA=A=Ae\}
=\mathcal B(\ker T,\operatorname{im}T).
\]

More generally \(D_{g,h}=\mathcal B(\ker(gh-I),\operatorname{im}(gh-I))\). A nonzero proper such domain is indexed by two nonzero proper subspaces, because \(T\ne0\) then forces \(\ker T\ne V\), \(\operatorname{im}T\ne0\), while \(\ker T=0\) or \(\operatorname{im}T=V\) makes the domain \(\{0\}\).

**2. The crucial closure under partial conjugations.** For a generator set \(e=gh\), \(f=hg\), and

\[
U=\ker(e-I),\ W=\operatorname{im}(e-I),\quad
U'=\ker(f-I),\ W'=\operatorname{im}(f-I).
\]

On the source and target domains the map is \(A\mapsto hAg\). The restriction \(h:U\to U'\) is an isomorphism with inverse \(g:U'\to U\): for \(u\in U\), \(ghu=u\), and for \(u'\in U'\), \(hgu'=u'\). Also \(g\) induces an isomorphism \(\overline g:V/W'\to V/W\) with inverse induced by \(h\), since \(gW'\subseteq W\), \(hW\subseteq W'\), and both \(gh\) and \(hg\) act as identities on the respective quotients.

Thus, in the canonical \(\operatorname{Hom}\)-identifications, \(\phi_{g,h}\) is the tensor-factor transformation \(A\mapsto(h|_U)A\overline g\). Any restriction of its source to

\[
\mathcal B(P,Q),\qquad P\subseteq U,\quad Q\supseteq W,
\]

has **rectangular image** \(\mathcal B(hP,g^{-1}Q)\), as follows either by the factor isomorphisms or by applying the inverse \(B\mapsto gBh\). Similarly the preimage of a target rectangle \(\mathcal B(P',Q')\) equals

\[
\mathcal B\bigl(U\cap h^{-1}(P'),\ W+g(Q')\bigr).
\]

In particular intersections, preimages, and images under the generated partial maps preserve rectangular domains. Starting with the defining generators and inducting over composition and inverse, **every element of \(\operatorname{Inn}(S)\) has a rectangular domain**, perhaps \(S\) or \(\{0\}\). Outside those two extremes, both defining subspaces are nonzero proper: intersections only shrink image subspaces and enlarge common kernels, and the factor isomorphisms preserve properness and nonzeroness whenever the resulting domain is nonzero. Every idempotent in any inverse monoid of partial bijections is a partial identity on its domain. This proves the inclusion \(\subseteq\) in the claimed classification.

**3. Realization of every pair.** Fix \(0<U<V\), \(0<W<V\). Let \(\lambda_1,\ldots,\lambda_a\) be a basis of the annihilator \(U^\perp\subseteq V^*\), and let \(w_1,\ldots,w_b\) be a basis of \(W\). Each rank-one operator \(T_{ij}(v)=\lambda_i(v)w_j\) yields \(e_{ij}=I-T_{ij}\) and a generating partial identity

\[
\phi_{e_{ij},I}=\mathbf1_{D_{e_{ij},I}}
=\mathbf1_{\mathcal B(\ker T_{ij},\operatorname{im}T_{ij})}.
\]

The product of these finitely many partial identities has domain

\[
\mathcal B\left(\bigcap_{i,j}\ker T_{ij},\sum_{i,j}\operatorname{im}T_{ij}\right)
=\mathcal B(U,W).
\]

The full identity is \(\phi_{I,I}\). The identity on \(\{0\}\) is \(\phi_{0,I}\). Hence every claimed semilattice element occurs.

**4. Uniqueness, counting, and square-zero criterion.** For proper nonzero \(U,W\), all matrices in \(\mathcal B(U,W)\) collectively have image spanning \(U\) and common kernel exactly \(W\), because rank-one maps \(V/W\to U\) realize every vector and separate each nonzero coset. Hence the ordered pair \((U,W)\) is recoverable uniquely. The intersection and order formulas follow immediately from the defining image/kernel constraints. For finite \(K\), the number of subspaces of each dimension is Gaussian-binomial, and the dimension of \(\operatorname{Hom}_K(V/W,U)\) is \(u(n-w)\), giving both enumerations.

If \(U\subseteq W\), the product of any two maps with images in \(U\) and kernels containing \(W\) vanishes. Conversely, if \(u\in U\setminus W\), choose a linear functional \(\ell:V/W\to K\) nonzero at the coset of \(u\); the rank-one map \(A(v)=\ell(v+W)u\) has \(A^2\ne0\). Thus the square-zero criterion is exact. Choose \(W\) first and count its nonzero \(U\)-subspaces to obtain the final displayed sum.

## Verification

The self-contained `verify.py` independently enumerates matrices and domains, using finite-field multiplication rather than the Gaussian formulas. It computes the meet-closure of all generator domains for \((n,q)=(2,2),(3,2),(2,3)\), separately enumerates all subspaces over \(\mathbb F_2\) to compare the claimed rectangular-domain set for \(n=2,3\), and directly closes the full generated partial-bijection monoid for \((n,q)=(2,2)\). The resulting domain counts are \(11,198,18\), respectively. The binary cases have exactly \(4\) and \(36\) square-zero domains, respectively, independently checking the containment criterion. The complete partial-bijection monoid for \((2,2)\) has \(52\) elements and exactly \(11\) idempotents. These tests corroborate the finite-field formulas and generator closure but do not establish the general theorem; the linear-algebra argument above does.

## Relationship to prior work

Araújo et al. [1, §3] introduce the defining partial inner automorphisms for arbitrary semigroups and [1, Problem 7.9] explicitly pose the characterization of the corresponding inverse monoid for finite-dimensional vector-space endomorphism monoids. Their explicit solved families are completely simple semigroups, full transformation monoids, and endomorphism monoids of finite abelian group-sets. Our result is solely the **idempotent semilattice** in that unanswered linear case. The earlier manuscript [2] contains related work on natural conjugacy and is a historical precursor to [1]; nothing in this theorem claims to reintroduce the general construction. The Gaussian subspace-counting ingredients are standard; the asserted contribution is their exact realization, with no missing or additional idempotent domains, inside this specified inverse monoid.

## Limitations

The structure of non-idempotent partial maps, multiplication between non-idempotents, maximal subgroups, Green relations, and generators/presentations of the whole inverse monoid are not classified. This is thus only a structural part of [1, Problem 7.9]. No independent audit or exhaustive infinite-field computation has been performed. Earlier unpublished or differently phrased equivalent idempotent-domain descriptions cannot be ruled out by the literature search.

## References

[1] J. Araújo, W. Bentz, M. Kinyon, J. Konieczny, A. Malheiro, and V. Mercier, *The Inverse Monoid of Partial Inner Automorphisms of a Semigroup*, arXiv:2605.00041v1, first posted 2026-04-28, particularly Definition 3.8, Theorem 3.2, Proposition 3.6 and Problem 7.9. https://arxiv.org/abs/2605.00041

[2] J. Araújo, W. Bentz, M. Kinyon, J. Konieczny, A. Malheiro, and V. Mercier, *Conjugacy in Abstract Semigroups, Transformation and Diagram Monoids, and Conjugacy Growth*, arXiv:2301.04252 (first posted in 2023; inspected v3), historical precursor. https://arxiv.org/abs/2301.04252
