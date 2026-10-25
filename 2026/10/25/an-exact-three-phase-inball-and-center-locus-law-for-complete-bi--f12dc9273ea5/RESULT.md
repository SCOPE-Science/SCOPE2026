# An exact three-phase inball and center-locus law for complete-bipartite in-in zonotopes

## Finding
For integers \(2\le p\le q\), let \(G=K_{p,q}\) have bipartition \(A\sqcup B\), with \(|A|=p\), \(|B|=q\), and \(n=p+q\). The unit in-in zonotope, in its standard Euclidean realization, has **exact** inradius
\[
r(\mathcal I(G))=\min\{\sqrt n,p+1\}.
\]
There is a sharp three-phase classification of **all** maximum-radius inscribed-ball centers. Writing \(\mathcal C_{p,q}\) for their set,
\[
\dim\mathcal C_{p,q}=\begin{cases}
n-1,&n<(p+1)^2,\\
p-1,&n=(p+1)^2,\\
p,&n>(p+1)^2.
\end{cases}
\]
The affine hull equals, respectively,
\[
\left\{c:\sum_{v\in V}c_v=0\right\},\qquad
\left\{c:c_b=0\ (b\in B),\ \sum_{a\in A}c_a=0\right\},\qquad
\left\{c:c_b=0\ (b\in B)\right\}.
\]
The center set has nonempty relative interior in the indicated affine hull, with the origin in that relative interior. Precisely \(2\), \(2(q+1)\), or \(2q\) facets, respectively, touch the origin-centered largest ball. They correspond to the whole vertex set, both the whole set and the singletons in \(B\), or only those singletons. The equality phase occurs exactly when \(q=p^2+p+1\), starting with \((p,q)=(2,7)\).

## Assumptions and scope
In the graph vertex space \(\mathbb R^{V}\), with standard unit vectors \(e_v\), define the centrally symmetric full-dimensional polytope
\[
\mathcal I(G)=\sum_{v\in V}[-e_v,e_v]+\sum_{\{u,v\}\in E(G)}[-(e_u-e_v),e_u-e_v].
\]
All sums are Minkowski sums, all intervals include both endpoints, all conductances/generator weights are \(1\), and distances are ordinary ambient Euclidean distances. For \(S\subseteq V\), \(\delta_G(S)\) denotes graph edges with exactly one endpoint in \(S\). For every nonempty connected induced vertex set \(S\), its two facet inequalities are
\[
\left|\sum_{v\in S}x_v\right|\le |S|+|\delta_G(S)|.
\]
The complete facet description follows from the known in-in zonotope construction and its graph-join interpretation. No claim is made here for other weights or graph families.

## Proof
**1. Origin is an optimal ball center.** The polytope is centrally symmetric. If balls of radius \(r\) around \(c\) and \(-c\) lie in a convex centrally symmetric body, their midpoint ball of radius \(r\) around the origin lies in it as well. Therefore the inradius equals the smallest Euclidean distance from the origin to any facet hyperplane:
\[
r=\min_{\substack{\varnothing\ne S\subseteq V\\G[S]\text{ connected}}}\frac{|S|+|\delta_G(S)|}{\sqrt{|S|}}.
\]
Indeed the facet normal is the \(0/1\) indicator vector of \(S\), whose norm is \(\sqrt{|S|}\).

**2. Sharp cut bound.** Put \(a=|S\cap A|\), \(b=|S\cap B|\), \(t=a+b\). The cut cardinality is exactly
\[
|\delta_G(S)|=a(q-b)+b(p-a).
\]
If \(S\) lies entirely within one part, its cut size is at least \(p t\). Otherwise both parts meet \(S\); every vertex outside \(S\) is adjacent to a vertex inside \(S\), so the cut has at least \(n-t\) edges. Thus for every nonempty \(S\),
\[
|\delta_G(S)|\ge\min\{pt,n-t\}.
\]
Consequently, for \(1\le t\le n\),
\[
\frac{t+|\delta_G(S)|}{\sqrt t}
\ge\min\{(p+1)\sqrt t,n/\sqrt t\}
\ge\min\{p+1,\sqrt n\}.
\]
The last inequality uses \(\sqrt t\ge1\) and \(n/\sqrt t\ge\sqrt n\). Equality in the lower bound is realized by \(S=V\), which gives \(\sqrt n\), and by \(S=\{b\}\) for any \(b\in B\), which gives \(p+1\). This proves the radius.

**3. Exhaustive tangent-facet classification.** If \(1<t<n\), both \((p+1)\sqrt t>p+1\) and \(n/\sqrt t>\sqrt n\). Hence no such subset can produce the minimum. Among singletons, a vertex in \(B\) has degree \(p\) whereas a vertex in \(A\) has degree \(q\ge p\). A singleton of \(A\) can tie a singleton in \(B\) only for \(p=q\); in that balanced case \(\sqrt{2p}<p+1\), so neither type is tangent. Only the whole set and the \(B\)-singletons survive, with the claimed threshold. Each connected set indexes opposite facets, yielding the respective counts.

**4. All maximum-ball centers.** A Euclidean ball of radius \(r\) centered at \(c\) lies in the polytope exactly when
\[
\left|\sum_{v\in S}c_v\right|+r\sqrt{|S|}
\le |S|+|\delta_G(S)|
\]
for every connected induced \(S\). Each tangent facet at the origin forces its normal to annihilate \(c\). The normals are: the all-ones vector alone in the first regime; the all-ones vector and the \(q\) basis vectors on \(B\) at equality; or exactly those \(q\) basis vectors in the last regime. Their ranks are, respectively, \(1\), \(q+1\), and \(q\). Every other facet has strictly positive slack at the origin; because there are finitely many, sufficiently small vectors in the corresponding common nullspace satisfy all other inequalities. Thus the center set has nonempty relative interior in that nullspace, and its affine dimension is \(n-1\), \(p-1\), or \(p\), as stated.

## Verification
An independent exact-arithmetic script `verify.py` checks the cut inequalities and all equality cases for \(548905\) connected-subset-size orbits, independently enumerates \(55972\) connected vertex subsets, and uses rational row reduction to verify \(26\) contact-normal ranks. Execute `python verify.py` with Python 3.10 or later (no third-party packages). These bounded checks corroborate, but do not replace, the proofs for arbitrary \(p,q\).

## Relationship to prior work
Glew introduced in-in zonotopes, their hypercube-plus-graphical-zonotope Minkowski representation, and connected-induced-subgraph facet description [1]. Those structural inputs are used here, not claimed as new. He, Li, Su, and Zhu used their support functions in tropical and stringy integral representations [2]. This finding specializes the geometry to an infinite biclique family and **solves** the all-parameter Euclidean ball-center optimization, including the exact three-phase affine-center classification and complete contacting-facet list. Graphical zonotopes alone, graph associahedra, and symmetric edge polytopes are different convex bodies and their published radius formulas do not apply to this construction.

## Limitations
The result concerns only the specified unit-weight Euclidean in-in realization and \(2\le p\le q\). The affine hull and dimension of all maximum-ball centers are identified; an inequality description of the bounded center set is immediate from the displayed facet constraints, but its full face numbers and Euclidean volume are not classified. Historical priority remains provisional: the source abstracts and detailed public construction descriptions were inspected, but not all plausibly related complete primary texts could be retrieved. No claim of independent verification is made.

## References
[1] R. Glew, “Geometry of in-in correlators,” arXiv:2601.18903, first submitted 2026-01-26. https://arxiv.org/abs/2601.18903

[2] S. He, X. Li, Y.-X. Su, and F. Zhu, “Tropical and Stringy Integrals for In-In Correlators,” arXiv:2608.19720, first submitted 2026-08-20. https://arxiv.org/abs/2608.19720
