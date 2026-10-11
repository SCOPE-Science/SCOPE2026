# Semi-balanced root polytopes have a canonical vertex sphere with a flow criterion for minimality
## Finding
Let
\[
G=(V,E)
\]
be a connected semi-balanced directed graph with
\[
|V|\ge3.
\]
For an edge
\[
e=\overrightarrow{th},
\]
write
\[
v_e=e_h-e_t,
\]
and let
\[
Q_G=\operatorname{conv}\{v_e:e\in E\}\subset\mathbb R^V
\tag{1}
\]
be the root polytope.

A semi-balanced graph admits a layer function
\[
\ell:V\to\mathbb R
\]
such that
\[
\ell(h)-\ell(t)=1
\tag{2}
\]
on every directed edge. Put
\[
\ell_0
=
\ell
-
\frac1{|V|}
\left(\sum_{v\in V}\ell(v)\right)\mathbf1,
\qquad
s=\|\ell_0\|^2,
\tag{3}
\]
and
\[
c=\frac{\ell_0}{s}.
\tag{4}
\]

Then every vertex of \(Q_G\) lies on one intrinsic Euclidean sphere in the affine hull:
\[
\boxed{
\|v_e-c\|^2
=
2-\frac1s
\quad
\text{for every }e\in E.
}
\tag{5}
\]
Thus
\[
\boxed{
R_0=\sqrt{2-\frac1s}
}
\tag{6}
\]
is a canonical all-vertex sphere radius.

This sphere is the unique minimum enclosing sphere exactly when
\[
\boxed{
c\in Q_G.
}
\tag{7}
\]
Equivalently, (7) holds exactly when there are weights
\[
w_e\ge0
\]
such that
\[
\sum_{e\in E}w_e=1
\tag{8}
\]
and
\[
\sum_{e=\overrightarrow{th}}w_e(e_h-e_t)=c.
\tag{9}
\]
When (7) holds, every root vertex is a contact point of the unique minimum enclosing sphere. When (7) fails, the true minimum enclosing radius is strictly smaller than \(R_0\).

For the standard orientation of a connected bipartite graph
\[
G=(A\sqcup B,E),
\qquad
|A|=p,
\qquad
|B|=q,
\]
with every edge directed from \(A\) to \(B\), the center and radius simplify to
\[
\boxed{
c=
\left(
-\frac1p\mathbf1_A,
\frac1q\mathbf1_B
\right),
}
\tag{10}
\]
\[
\boxed{
R_0
=
\sqrt{
2-\frac1p-\frac1q
}.
}
\tag{11}
\]
In this case (7) is equivalent to the proportional Hall inequalities
\[
\boxed{
p\,|N(X)|
\ge
q\,|X|
\qquad
\text{for every }X\subseteq A.
}
\tag{12}
\]
In particular, every connected biregular bipartite graph satisfies (12), so its standard root polytope has the unique minimum enclosing sphere in (10)--(11).

## Assumptions and scope
The realization is exactly the directed-graph root-polytope realization of the primary source, with the Euclidean metric inherited from the standard orthonormal basis of \(\mathbb R^V\).

The graph is finite, connected, and semi-balanced. Connectedness ensures that the source affine-dimension theorem gives
\[
\dim Q_G=|V|-2.
\]
The restriction \(|V|\ge3\) avoids the zero-dimensional single-edge case.

The layer function is unique up to adding a constant on a connected graph. Consequently \(\ell_0\), \(s\), \(c\), and \(R_0\) are independent of that additive choice.

The theorem identifies exactly when the canonical all-vertex sphere is the minimum enclosing sphere. It does not give a closed formula for the smaller minimum radius when the flow condition fails.

## Proof
The source shows that for a connected semi-balanced directed graph there is a linear layer functional whose value increases by \(1\) along every directed edge, and that
\[
\dim Q_G=|V|-2.
\tag{13}
\]
Every root vector satisfies
\[
\langle\mathbf1,v_e\rangle=0
\tag{14}
\]
and, by (2),
\[
\langle\ell,v_e\rangle=1.
\tag{15}
\]
Hence the affine hull is
\[
H
=
\left\{
x\in\mathbb R^V:
\langle\mathbf1,x\rangle=0,
\ \langle\ell,x\rangle=1
\right\}.
\tag{16}
\]
Indeed, the right side has dimension \(|V|-2\), matching (13).

The translation space of \(H\) is
\[
T
=
\left\{
x:
\langle\mathbf1,x\rangle=0,
\ \langle\ell_0,x\rangle=0
\right\}.
\tag{17}
\]
The point \(c\) in (4) belongs to \(H\), because
\[
\langle\mathbf1,c\rangle=0
\]
and
\[
\langle\ell,c\rangle
=
\langle\ell_0,c\rangle
=
1.
\]
Moreover,
\[
c\perp T.
\]
Therefore \(c\) is the orthogonal projection of the ambient origin onto \(H\).

Every root vertex has ambient squared norm
\[
\|v_e\|^2=2.
\tag{18}
\]
Also
\[
\langle c,v_e\rangle
=
\frac{\langle\ell_0,v_e\rangle}{s}
=
\frac1s
\tag{19}
\]
and
\[
\|c\|^2=\frac1s.
\tag{20}
\]
Consequently
\[
\|v_e-c\|^2
=
2-\frac2s+\frac1s
=
2-\frac1s,
\]
which proves (5).

We now use a general finite-point lemma.

Let
\[
P=\operatorname{conv}\{z_1,\ldots,z_m\}
\]
lie in a Euclidean affine space, and suppose
\[
\|z_i-c\|=R
\]
for every \(i\).

If
\[
c=\sum_i\alpha_i z_i,
\qquad
\alpha_i\ge0,
\qquad
\sum_i\alpha_i=1,
\tag{21}
\]
then for every candidate center \(y\),
\[
\sum_i\alpha_i\|z_i-y\|^2
=
R^2+\|y-c\|^2.
\tag{22}
\]
Thus
\[
\max_i\|z_i-y\|^2
\ge
R^2+\|y-c\|^2.
\]
The ball centered at \(c\) is therefore minimum enclosing, and equality in the radius is possible only for
\[
y=c.
\]
So the minimum enclosing sphere is unique.

Conversely, suppose
\[
c\notin P.
\]
Strict separation gives a vector \(u\) in the translation space and a number
\[
\delta>0
\]
such that
\[
\langle u,z_i-c\rangle\ge\delta
\]
for every \(i\). For sufficiently small
\[
\varepsilon>0,
\]
the shifted center
\[
c+\varepsilon u
\]
satisfies
\[
\|z_i-(c+\varepsilon u)\|^2
=
R^2
-
2\varepsilon
\langle u,z_i-c\rangle
+
\varepsilon^2\|u\|^2
<
R^2
\]
for every \(i\). Hence the original all-vertex sphere is not minimum enclosing. This proves the equivalence (7), including strict radius improvement when (7) fails.

Applied to the root vertices, condition (21) is exactly (8)--(9).

Now specialize to the standard orientation of a connected bipartite graph. Choose
\[
\ell=0
\quad\text{on }A,
\qquad
\ell=1
\quad\text{on }B.
\]
Then
\[
s=\frac{pq}{p+q},
\]
and (4)--(6) become (10)--(11).

Writing an edge weight as
\[
w_{ab}
\qquad
(a\in A,\ b\in B),
\]
equation (9) is equivalent to
\[
\sum_{b:ab\in E}w_{ab}=\frac1p
\qquad
(a\in A)
\tag{23}
\]
and
\[
\sum_{a:ab\in E}w_{ab}=\frac1q
\qquad
(b\in B).
\tag{24}
\]
Thus (7) asks for a nonnegative transportation plan with uniform marginals supported on \(G\).

Scale by
\[
pq.
\]
The equivalent network-flow problem asks for a flow of total value
\[
pq
\]
from a source to each \(a\in A\) with capacity \(q\), across the allowed graph edges, and from each \(b\in B\) to the sink with capacity \(p\).

A finite source-side cut determined by
\[
X\subseteq A
\]
must also contain
\[
N(X)\subseteq B,
\]
and its capacity is
\[
q(p-|X|)+p|N(X)|.
\]
By max-flow/min-cut, a flow of value \(pq\) exists exactly when
\[
q(p-|X|)+p|N(X)|
\ge
pq
\]
for all \(X\), which is precisely (12).

Finally, if the graph is biregular, with degrees \(r\) on \(A\) and \(t\) on \(B\), then
\[
pr=qt=|E|.
\]
Assigning
\[
w_e=\frac1{|E|}
\]
to every edge gives row sums
\[
\frac r{|E|}=\frac1p
\]
and column sums
\[
\frac t{|E|}=\frac1q.
\]
Therefore every connected biregular bipartite graph satisfies the criterion.

## Verification
The proof is symbolic and applies to every connected semi-balanced directed graph with at least three vertices.

The source-dependent inputs were checked directly in the primary full text: Definition 2.1 of the directed root polytope, the layer-function characterization of semi-balanced graphs, the affine hyperplane containing \(Q_G\), and Corollary 3.2 giving dimension \(|V|-2\) in the connected semi-balanced case.

The accompanying `verify.py` performs two independent finite checks. First, it verifies the projection-center and common-radius identities on several genuinely multi-layer semi-balanced digraphs. Second, for every connected bipartite graph with
\[
1\le p,q\le4,
\]
it checks that the proportional Hall inequalities are equivalent to a maximum flow of value \(pq\), and it verifies the universal sphere formula
\[
R_0^2=2-\frac1p-\frac1q.
\]
These computations are corroborative only.

## Relationship to prior work
Kálmán and Tóthmérész introduced the directed root-polytope framework used here and developed its semi-balanced structure, spanning-tree dissections, shellings, and \(h^*\)-theory. Their paper identifies the layer functional and the affine dimension but does not discuss Euclidean circumradii, minimum enclosing spheres, or the convex-hull criterion above.

Earlier bipartite-root-polytope work relates Ehrhart theory to hypergraph interior polynomials and triangulations. It does not formulate the Euclidean minimum-sphere question.

The geometric distinction between “all vertices lie on a sphere” and “that sphere is the minimum enclosing sphere” is essential here. The source affine equations imply the former for every connected semi-balanced root polytope. The latter is equivalent to a positive-barycenter condition and, in the standard bipartite orientation, becomes the proportional Hall expansion condition (12).

Thus the theorem connects three structures that are not identified in the checked sources: the layer functional, the intrinsic Euclidean minimum sphere, and a balanced flow feasibility condition.

Targeted searches under “semi-balanced root polytope”, “bipartite root polytope”, “circumradius”, “minimum enclosing sphere”, “fractional matching”, “uniform marginals”, and “Hall condition” did not locate a theorem implying the statement above.

## Limitations
When the flow condition fails, the theorem proves that the true minimum enclosing radius is strictly below \(R_0\), but it does not give that smaller radius explicitly.

The result concerns the standard root-vector realization and its inherited Euclidean metric. It is not invariant under arbitrary affine or unimodular coordinate changes.

The proportional Hall formulation is written only for the standard two-layer bipartite orientation. For a general multi-layer semi-balanced orientation, (8)--(9) is the exact criterion, but no comparably simple cut formula is asserted here.

A residual originality risk remains for a general minimum-enclosing-sphere lemma combined with network-flow feasibility in literature outside root polytopes. Search nonappearance is not treated as a formal global novelty certificate.

## References
1. Tamás Kálmán and Lilla Tóthmérész, *Root polytopes and Jaeger-type dissections for directed graphs*, arXiv:2105.00960, first public version 2021-05-03; *Mathematika* 68 (2022), 1176--1220, DOI 10.1112/mtk.12163.
2. Tamás Kálmán and Lilla Tóthmérész, *\(h^*\)-vectors of graph polytopes using activities of dissecting spanning trees*, arXiv:2203.17127; *Algebraic Combinatorics* 6 (2023), 1637--1651, DOI 10.5802/alco.318.
