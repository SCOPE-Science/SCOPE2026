# A dimension-eleven reversal of vertex inertia in Loday's nested polytopes

## Finding

Let \(n\ge 2\). Consider three canonical Loday polytopes in the Euclidean hyperplane \(H_n=\{x\in\mathbb R^n:\sum_i x_i=n(n+1)/2\}\): the permutahedron \(\mathrm{Perm}_n\), the associahedron \(\mathrm{Asso}_n\), and the parallelepiped \(\mathrm{Para}_n\), with the standard compatible realizations \(\mathrm{Perm}_n\subseteq\mathrm{Asso}_n\subseteq\mathrm{Para}_n\). Write \(g_n=((n+1)/2)\mathbf1\), and define the **uniform-vertex inertia** of any one of these polytopes by

\[
J(K)=\frac1{|\operatorname{vert}(K)|}\sum_{v\in\operatorname{vert}(K)}\|v-g_n\|_2^2.
\]

Then, exactly,

\[
\boxed{J(\mathrm{Perm}_n)=\frac{n(n^2-1)}{12},\qquad
J(\mathrm{Asso}_n)=\frac{n(n-1)(n+1)(2n+1)}{60},\qquad
J(\mathrm{Para}_n)=\frac{(n-1)^3}{2}.}
\]

For \(n=2\) all three values are equal. For \(3\le n\le10\), they are strictly ordered

\[
J(\mathrm{Perm}_n)<J(\mathrm{Asso}_n)<J(\mathrm{Para}_n),
\]

but for every \(n\ge11\) the latter two **reverse their order**:

\[
J(\mathrm{Perm}_n)<J(\mathrm{Para}_n)<J(\mathrm{Asso}_n).
\]

In particular, the inclusion of these *convex sets* does not order the mean squared radius of their *uniformly sampled vertices*. The ratio \(J(\mathrm{Asso}_n)/J(\mathrm{Perm}_n)=(2n+1)/5\) for \(n\ge2\).

## Assumptions and scope

The ambient metric is the ordinary Euclidean metric restricted to \(H_n\), without rescaling or affine normalization. This is a statistic of **uniformly chosen vertices**, not uniformly chosen points of the convex bodies. The common point \(g_n\) is the uniform-vertex barycenter of each of the three realizations, as established in the cited literature. For clarity, their vertex sets are:

1. The \(n!\) permutations of \((1,2,\ldots,n)\) for \(\mathrm{Perm}_n\).
2. The \(C_n=\frac1{n+1}\binom{2n}{n}\) plane full binary trees with \(n\) internal nodes for \(\mathrm{Asso}_n\). Label internal nodes in symmetric (inorder) traversal; at node \(i\), let \(\ell_i\) and \(r_i\) be the numbers of leaves of its left and right subtrees. Its vertex is \((\ell_1r_1,\ldots,\ell_nr_n)\).
3. The \(2^{n-1}\) points \(g_n+\frac{n-1}{2}\sum_{i=1}^{n-1}\epsilon_i(e_i-e_{i+1})\), where each \(\epsilon_i\in\{-1,1\}\), for \(\mathrm{Para}_n\).

These are the standard unweighted realizations. In particular, the result does not assert the same formulas for other associahedron realizations or for volume-uniform distributions.

## Proof

**Permutahedron.** Every permutation vertex has the same squared displacement from \(g_n\):

\[
\sum_{i=1}^n\left(i-\frac{n+1}{2}\right)^2=\frac{n(n^2-1)}{12}.
\]

**Parallelepiped.** Uniformly choosing a vertex is equivalent to taking independent symmetric signs \(\epsilon_i\). Therefore all mixed terms vanish upon averaging, while \(\|e_i-e_{i+1}\|_2^2=2\). Consequently,

\[
J(\mathrm{Para}_n)=\frac{(n-1)^2}{4}\sum_{i=1}^{n-1}2=\frac{(n-1)^3}{2}.
\]

**Associahedron.** For a full binary tree \(T\) with \(n\) internal nodes, put \(Q(T)=\sum_i(\ell_i r_i)^2\), and set \(S_n=\sum_{T}Q(T)\), summed over all \(C_n\) trees. Let \(C(z)=\sum_{j\ge0}C_jz^j\) and \(S(z)=\sum_{n\ge1}S_nz^n\). At the root, if the left and right subtrees have \(a\) and \(b\) internal nodes, the root coordinate is \((a+1)(b+1)\), and every other coordinate is inherited unchanged from its subtree. Root decomposition gives the exact formal power-series identity

\[
S(z)=2zC(z)S(z)+zA(z)^2,\qquad
A(z)=\sum_{j\ge0}(j+1)^2C_jz^j.
\]

The Catalan equation \(C(z)=1+zC(z)^2\) yields \(1-2zC(z)=\sqrt{1-4z}\). Using \((j+1)C_j=\binom{2j}{j}\) and differentiating its generating series,

\[
A(z)=\frac{1-2z}{(1-4z)^{3/2}},\qquad
S(z)=\frac{z(1-2z)^2}{(1-4z)^{7/2}}.
\]

Expanding the binomial series and simplifying its coefficient at \(z^n\) gives, for every \(n\ge1\),

\[
S_n=C_n\,\frac{n(n+1)(n^2+7n+7)}{30}.
\]

Since the average tree vertex equals \(g_n\), the mean squared centered radius equals its mean squared-coordinate sum minus \(n(n+1)^2/4\). Thus

\[
J(\mathrm{Asso}_n)=\frac{S_n}{C_n}-\frac{n(n+1)^2}{4}
=\frac{n(n-1)(n+1)(2n+1)}{60}.
\]

**Sharp order reversal.** Direct factorization of the established formulas yields

\[
J(\mathrm{Asso}_n)-J(\mathrm{Perm}_n)
=\frac{n(n-2)(n-1)(n+1)}{30},
\]

and

\[
J(\mathrm{Para}_n)-J(\mathrm{Asso}_n)
=-\frac{(n-2)(n-1)(2n^2-23n+15)}{60}.
\]

The quadratic \(2n^2-23n+15\) is negative at each integer \(3\le n\le10\) and positive at each integer \(n\ge11\). Also \(J(\mathrm{Para}_n)>J(\mathrm{Perm}_n)\) for every \(n\ge3\), because their difference factors as \(\frac{(n-1)(5n^2-13n+6)}{12}>0\) in this range. This proves every boundary case and ordering.

## Verification

The companion standard-library checker `artifacts/verify.py` can be run with `python3 artifacts/verify.py`. It directly enumerates every binary tree for \(1\le n\le10\), verifying the exact Catalan vertex count, each coordinate barycenter, and the exact rational inertia. It enumerates all signed parallelepiped vertices for \(2\le n\le9\); independently checks the formal-series coefficient identity through \(n=70\); and checks the factored comparisons through \(n=100\). Its successful output is `VERIFY_OK tree_vertices=23713 signed_vertices=510 gf_coefficients=70 comparison_dimensions=99`. The infinite claims above are proved by the exact generating-function argument; the finite checks are cross-checks only.

## Relationship to prior work

The source polytope realizations, their nesting and their common barycenter are established properties. The survey by Pilaud, Santos and Ziegler supplies the explicit three-polytope presentation. Loday gives the original tree-coordinate realization. Hohlweg, Lortie and Raymond prove the canonical associahedron vertex barycenter. These works are not claimed as new. What is established here is the **full three-way exact uniform-vertex inertia calculation and its sharp dimension-eleven reversal**. Prior claims about equal inradii or facet shells do not determine uniformly sampled vertex second moments, since the latter concern discrete vertex measures rather than convex-body inclusions or inscribed balls.

## Limitations

The statement concerns only the given Euclidean coordinate normalization and uniform-vertex distribution. It does not calculate covariance eigenvalues, higher moments, or volume-uniform inertia. The formulas are exact in all stated dimensions; no statistical extrapolation from the finite checker is used. The literature comparison did not establish an absolute absence of equivalent formulas in the wider Catalan additive-functional or polytope moment literature; this remains a bibliographic limitation.

## References

- V. Pilaud, F. Santos, G. M. Ziegler, *Celebrating Loday's Associahedron*, arXiv:2305.08471v1 (first public 2023-05-15), https://arxiv.org/abs/2305.08471.
- J.-L. Loday, *Realization of the Stasheff polytope*, arXiv:math/0212126v1 (2002), https://arxiv.org/abs/math/0212126.
- C. Hohlweg, J.-P. Lortie, A. Raymond, *The centers of gravity of the associahedron and of the permutahedron are the same*, arXiv:0910.0265v1 (2009), https://arxiv.org/abs/0910.0265.
