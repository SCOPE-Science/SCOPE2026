# Algebraically independent metric skeletons and Euclidean nonembeddability

## Result

Let \(X\) be a metrizable space and let \(D\subseteq X\) be a fixed countable subset. Write \(\operatorname{Met}(X)\) for the compatible metrics on \(X\), with the uniform topology, and define
\[
\mathcal A_D(X)=\left\{d\in\operatorname{Met}(X):
\{d(x,y):\{x,y\}\in[D]^2\}\text{ is algebraically independent over }\mathbb Q
\right\}.
\]

### Theorem 1: arbitrary-topology countable skeletons

For every metrizable \(X\) and every countable \(D\subseteq X\),
\[
\boxed{\mathcal A_D(X)\text{ is a dense }G_\delta\text{ subset of }\operatorname{Met}(X).}
\]

Thus the zero-dimensionality hypothesis needed for algebraic independence of *all* distances can be dropped completely when algebraic independence is prescribed on one fixed countable skeleton. In particular, if \(X\) is separable and \(D\) is a fixed countable dense subset, then a generic compatible metric has algebraically independent distances on a dense skeleton.

If \(X\) is completely metrizable, Ishiki's Baire theorem also says that complete compatible metrics are comeager in \(\operatorname{Met}(X)\). Hence
\[
\mathcal A_D(X)\cap\{\text{complete compatible metrics}\}
\]
is comeager.

### Theorem 2: finite-dimensional Euclidean strata are nowhere dense

For \(m\ge 1\), let
\[
\mathcal E_m(X)=\left\{d\in\operatorname{Met}(X):
(X,d)\text{ admits an isometric embedding into }\mathbb R^m
\right\}.
\]
If \(|X|\ge m+2\), then
\[
\boxed{\mathcal E_m(X)\text{ is closed and nowhere dense in }\operatorname{Met}(X).}
\]
Consequently, for every infinite metrizable \(X\),
\[
\boxed{\bigcup_{m\ge1}\mathcal E_m(X)\text{ is meagre}.}
\]
So a generic compatible metric on any infinite metrizable space has no isometric embedding into any finite-dimensional Euclidean space.

### Theorem 3: rigidity-matroid obstruction on the skeleton

Let \(d\in\mathcal A_D(X)\), let \(G=(V,E)\) be a finite graph with \(V\subseteq D\), and suppose the edge lengths
\[
\ell_{ij}=d(i,j),\qquad ij\in E,
\]
are realized by a framework in \(\mathbb R^m\). Then \(E\) is independent in the \(m\)-dimensional Cayley--Menger algebraic rigidity matroid.

In dimension two this says:
\[
\boxed{\text{every planar-realizable distance graph cut from }D\text{ is }(2,3)\text{-sparse}.}
\]
If \(F\subseteq D\) has \(k\ge2\) points and its complete metric is Euclidean-realizable, then its affine Euclidean dimension is exactly
\[
\boxed{k-1.}
\]
Hence an infinite \(D\) cannot embed isometrically into any finite-dimensional Euclidean space.

For a separable \(X\) with a fixed countable dense \(D\), Theorem 1 therefore yields the local consequence:
\[
\boxed{\text{every infinite open }U\subseteq X\text{ is not isometrically embeddable into any finite-dimensional }\mathbb R^m.}
\]
In particular, if \(X\) has no isolated points, no nonempty open metric subspace is finitely Euclidean.

## Proof

### 1. Polynomial avoidance on a fixed finite set

Fix distinct unordered pairs
\[
e_1,\dots,e_r\in[D]^2
\]
and a nonzero polynomial \(P\in\mathbb Q[T_1,\dots,T_r]\). Define
\[
\mathcal U(P;e_1,\dots,e_r)
=
\{d\in\operatorname{Met}(X):P(d(e_1),\dots,d(e_r))\ne0\}.
\]
Finite distance evaluations are continuous in the uniform topology, so this set is open.

It is dense. Let \(d\in\operatorname{Met}(X)\), let \(\varepsilon>0\), and let \(F\subseteq D\) be the finite set of endpoints of the \(e_i\). A finite metric can first be moved arbitrarily slightly into the strict metric cone: if \(c\) is the discrete metric on \(F\), then
\[
d_\delta=(1-\delta)d|_{F^2}+\delta c
\]
has strict triangle inequalities for every sufficiently small \(\delta>0\). The strict finite metric cone is open in the Euclidean space of edge coordinates. Since the zero set of a nonzero real polynomial has empty interior, there is a strict metric \(e\) on \(F\), arbitrarily close to \(d|_{F^2}\), such that
\[
P(e(e_1),\dots,e(e_r))\ne0.
\]

Ishiki's metric interpolation theorem, applied to the closed finite subset \(F\), extends \(e\) to a compatible metric \(m\) on all of \(X\) with
\[
m|_{F^2}=e,\qquad
\mathcal D_X(m,d)=\mathcal D_F(e,d|_{F^2}).
\]
Thus \(m\) can be chosen within \(\varepsilon\) of \(d\), and \(\mathcal U(P;e_1,\dots,e_r)\) is dense.

There are only countably many finite lists of edges from a countable \(D\), and only countably many rational polynomials. Therefore
\[
\mathcal A_D(X)
=
\bigcap_{r,e_1,\dots,e_r,P}
\mathcal U(P;e_1,\dots,e_r)
\]
is a countable intersection of open dense sets. Ishiki proved that \(\operatorname{Met}(X)\) is Baire for every metrizable \(X\), so this intersection is dense. This proves Theorem 1.

### 2. Closedness and nowhere density of Euclidean strata

Fix \(m\ge1\). For a compatible metric \(d\), choose a base point \(o\in X\) and form the Gram kernel
\[
G_d(x,y)=\frac12\bigl(d(o,x)^2+d(o,y)^2-d(x,y)^2\bigr).
\]
The metric \(d\) embeds isometrically in \(\mathbb R^m\) if and only if every finite Gram matrix
\[
(G_d(x_i,x_j))_{i,j}
\]
is positive semidefinite and has rank at most \(m\). These conditions are preserved under uniform limits: positivity is closed and rank at most \(m\) is expressed by the vanishing of all \((m+1)\times(m+1)\) minors. The resulting positive semidefinite kernel has a Hilbert-space realization whose span has dimension at most \(m\). Therefore \(\mathcal E_m(X)\) is closed in \(\operatorname{Met}(X)\).

Assume now \(|X|\ge m+2\). Given \(d\in\operatorname{Met}(X)\) and \(\varepsilon>0\), choose \(m+2\) distinct points \(F\subseteq X\). Every realization of \(F\) in \(\mathbb R^m\) forces its \((m+2)\)-point Cayley--Menger determinant to vanish. This determinant is a nonzero polynomial in the squared pairwise distances: it is nonzero, for example, on the regular \((m+1)\)-simplex. As above, after an arbitrarily small move into the strict finite metric cone, polynomial avoidance gives a metric \(e\) on \(F\), arbitrarily close to \(d|_{F^2}\), with nonzero Cayley--Menger determinant. Interpolation extends \(e\) to a compatible metric \(m'\) on \(X\) with \(\mathcal D_X(m',d)<\varepsilon\). Then \((X,m')\) cannot embed in \(\mathbb R^m\). Thus \(\mathcal E_m(X)\) has empty interior; being closed, it is nowhere dense. Theorem 2 follows.

### 3. Transfer to algebraic rigidity

For a finite Euclidean framework, write \(x_{ij}=\ell_{ij}^2\). The Cayley--Menger ideal consists of polynomial relations over \(\mathbb Q\) forced on squared Euclidean distances; a set of edges is dependent in its algebraic matroid exactly when it supports a nonzero such polynomial relation.

If \(E\) were dependent, there would be a nonzero
\[
Q\in\mathbb Q[(X_e)_{e\in E}]
\]
with
\[
Q((\ell_e^2)_{e\in E})=0
\]
for every \(m\)-dimensional realization. But
\[
R((T_e)_{e\in E})=Q((T_e^2)_{e\in E})
\]
is still a nonzero rational polynomial. Since the raw distances \((\ell_e)_{e\in E}\) belong to an algebraically independent subset, \(R(\ell_e:e\in E)\ne0\), a contradiction. Thus \(E\) is independent.

For \(m=2\), the Cayley--Menger algebraic matroid is the \((2,3)\)-sparsity matroid, giving the stated planar consequence. For a complete \(k\)-point submetric, realization in dimension at most \(k-2\) would force the \(k\)-point Cayley--Menger determinant to vanish; algebraic independence forbids this. Every Euclidean \(k\)-point metric has affine dimension at most \(k-1\), so any Euclidean realization must have dimension exactly \(k-1\).

Finally, if \(D\) is dense and \(U\subseteq X\) is infinite and open, then \(D\cap U\) is infinite. For every \(m\), choose \(m+2\) points of \(D\cap U\); the preceding complete-graph obstruction rules out an isometric embedding of \(U\) into \(\mathbb R^m\).

## Context and originality boundary

Ishiki's 2026 theorem proves density of metrics whose *entire* set of positive distances is algebraically independent when \(X\) is strongly zero-dimensional (and \(|X|\le\mathfrak c\)); it also proves a \(G_\delta\) statement for the full property on \(\sigma\)-compact spaces. The result above does not remove that hypothesis for full algebraic independence. Instead, it shows that algebraic independence on any fixed countable skeleton is generic for arbitrary metrizable topology, including connected spaces.

The proof deliberately uses Ishiki's earlier metric interpolation theorem and his Baire theorem for spaces of compatible metrics. The interpolation theorem itself, the Baire theorem, and the Cayley--Menger algebraic rigidity matroid are prior results, not contributions here. Ishiki's interpolation framework also proves broad generic failures of finite metric inequalities on non-discrete spaces; those results already give weaker non-Euclidean obstructions in many settings. Rouyer proved a generic non-Hilbert phenomenon for compact metric spaces in the different Gromov--Hausdorff parameter space.

The new claims are the fixed-countable-skeleton algebraic-independence theorem without a topological-dimension restriction, the closed-nowhere-dense description of each finite Euclidean stratum for arbitrary metrizable \(X\), and the transfer from an algebraically independent skeleton to Cayley--Menger rigidity-matroid independence and the resulting local exact-Euclidean obstruction. These claims are made to the best of our knowledge.

## Limitations

- The theorem does not prove algebraic independence of all distances when \(X\) is not strongly zero-dimensional; only distances on the prescribed countable skeleton are controlled.
- The Euclidean statements concern exact isometric embeddings. They do not obstruct bi-Lipschitz, quasi-isometric, coarse, or approximate Euclidean embeddings.
- Rigidity-matroid independence is a necessary condition for a skeleton edge assignment to be Euclidean-realizable, not a sufficient one.
- The argument is qualitative/Baire-category based and gives no quantitative perturbation radius or prevalence estimate.
- The motivating algebraic-independence preprint is very recent, and the broad interpolation/transmissible-property framework makes an unlocated equivalent reformulation the principal residual originality risk.

## References

1. Y. Ishiki, *Algebraically independent distances and rigid metrics*, arXiv:2609.19773 (2026).
2. Y. Ishiki, *An interpolation of metrics and spaces of metrics*, arXiv:2003.13227, v3 (2026).
3. Y. Ishiki, *Spaces of metrics are Baire*, arXiv:2402.04565 (2024; published 2025).
4. G. Malić and I. Streinu, *Computing Circuit Polynomials in the Algebraic Rigidity Matroid*, SIAM J. Appl. Algebra Geom. 7 (2023), 345--385, doi:10.1137/21M1437986.
5. J. Rouyer, *Generic Properties of Compact Metric Spaces*, Topology Appl. 158 (2011), 2140--2147; arXiv:1003.5087.
