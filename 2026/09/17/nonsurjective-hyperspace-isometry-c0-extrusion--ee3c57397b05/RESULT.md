# A standard non-surjective Hausdorff self-isometry of the convex hyperspace of c0

## Result

Let \(X\) be a nonzero real Banach space and write
\[
Y=X\oplus_\infty \mathbb R,\qquad
\|(x,t)\|=\max\{\|x\|,|t|\}.
\]
For \(A\in\mathcal C(X)\), where \(\mathcal C(X)\) denotes the nonempty bounded closed convex subsets of \(X\), set
\[
R(A):=d_H(A,\{0\})=\sup_{a\in A}\|a\|
\]
and define the **radius extrusion**
\[
\mathcal E(A):=A\times[-R(A),R(A)]\subseteq Y.
\]

Then \(\mathcal E:\mathcal C(X)\to\mathcal C(Y)\) has all of the following properties.

1. \(\mathcal E\) is an isometric embedding for the Hausdorff metric:
   \[
   d_H(\mathcal E(A),\mathcal E(B))=d_H(A,B)
   \qquad(A,B\in\mathcal C(X)).
   \]
2. \(\mathcal E(\{0\})=\{(0,0)\}\), but for every \(x\neq0\),
   \[
   \mathcal E(\{x\})=\{x\}\times[-\|x\|,\|x\|]
   \]
   is a nondegenerate segment. Thus even an origin-fixing non-surjective hyperspace isometry need not preserve singleton sets.
3. \(\mathcal E\) is an order embedding:
   \[
   A\subseteq B\quad\Longleftrightarrow\quad
   \mathcal E(A)\subseteq\mathcal E(B).
   \]
4. It commutes exactly with outer parallel bodies. If
   \(P_t^X(A)=A\oplus tB_X\) denotes closed Minkowski addition, then
   \[
   \mathcal E(P_t^X(A))
   =
   \mathcal E(A)\oplus tB_Y
   \qquad(t\ge0).
   \]
5. The same construction restricts to an isometric embedding
   \(\mathcal K(X)\to\mathcal K(Y)\) for nonempty compact convex sets.

Consequently, whenever \(X\) is linearly isometric to
\(X\oplus_\infty\mathbb R\), the convex hyperspace of \(X\) admits a proper
origin-fixing isometric self-embedding that does not preserve nonzero
singletons. In particular this holds for \(X=c_0\).

For \(c_0\), let
\[
U:c_0\oplus_\infty\mathbb R\longrightarrow c_0,\qquad
U(x,t)=(t,x_1,x_2,\ldots).
\]
Then
\[
F(A):=U[\mathcal E(A)]
\]
is a proper isometric self-embedding of both \(\mathcal C(c_0)\) and
\(\mathcal K(c_0)\), fixes \(\{0\}\), preserves inclusion and outer
parallel bodies, but maps every nonzero singleton to a nondegenerate line
segment.

## Proof

For nonempty bounded closed sets \(A,B\subseteq X\) and nonempty bounded
closed sets \(I,J\subseteq\mathbb R\), the max-product metric gives
\[
d_H^{X\oplus_\infty\mathbb R}(A\times I,B\times J)
=
\max\{d_H^X(A,B),d_H^{\mathbb R}(I,J)\}.
\]
Indeed, the directed distance from \((a,s)\) to \(B\times J\) is
\[
\max\{\operatorname{dist}(a,B),\operatorname{dist}(s,J)\},
\]
and taking the two directed suprema yields the displayed product formula.

The map \(A\mapsto R(A)=d_H(A,\{0\})\) is 1-Lipschitz by the triangle
inequality for the Hausdorff metric. Since
\[
d_H([-R(A),R(A)],[-R(B),R(B)])
=
|R(A)-R(B)|,
\]
the product formula gives
\[
\begin{aligned}
d_H(\mathcal E(A),\mathcal E(B))
&=\max\{d_H(A,B),|R(A)-R(B)|\}\\
&=d_H(A,B).
\end{aligned}
\]
This proves the isometry assertion.

If \(A\subseteq B\), then \(R(A)\le R(B)\), so
\(\mathcal E(A)\subseteq\mathcal E(B)\). Conversely, inclusion of the
extrusions implies \(A\subseteq B\) after projection onto the first
coordinate. Hence \(\mathcal E\) is an order embedding.

For the parallel-body identity, first note that
\[
R(P_t^X(A))=R(A)+t.
\]
The upper bound is immediate. For the reverse bound, choose \(a\in A\)
with \(\|a\|\) arbitrarily close to \(R(A)\) and, when \(a\ne0\), move from
\(a\) by \(t a/\|a\|\). Passing to the supremum gives equality. Since
\[
B_Y=B_X\times[-1,1],
\]
closed Minkowski addition gives
\[
\begin{aligned}
\mathcal E(A)\oplus tB_Y
&=
\bigl(A\times[-R(A),R(A)]\bigr)
 \oplus t\bigl(B_X\times[-1,1]\bigr)\\
&=
P_t^X(A)\times[-R(A)-t,R(A)+t]\\
&=
\mathcal E(P_t^X(A)).
\end{aligned}
\]

The singleton assertions follow directly from the definition. In
particular, only \(A=\{0\}\) can have \(\mathcal E(A)\) a singleton, so
the map is not surjective as soon as \(Y\ne\{0\}\). Compactness is
preserved because a product of compact sets is compact. Finally, \(U\) is
a surjective linear isometry, so composing with its induced action on
sets proves the \(c_0\) self-embedding statement.

## Context and boundary exposed

Cheng, He, Liu and Zheng (arXiv:2609.18252, 2026) prove that every
**surjective** Hausdorff isometry
\[
\mathcal C(X)\longrightarrow\mathcal C(Y)
\]
between arbitrary real Banach spaces preserves singleton sets and is
induced pointwise by a surjective affine isometry of the underlying
spaces. Their proof recovers outer parallel bodies and the inclusion order
before using surjectivity to identify minimal elements of the whole target
hyperspace.

The construction above shows that the surjectivity hypothesis cannot in
general be deleted in infinite dimension, even after adding three pieces
of structure that might appear to substitute for it: the map fixes the
origin singleton, is an order embedding, and preserves every outer
parallel-body ray exactly. The obstruction is that a minimal element of
the image need not be minimal in the ambient target hyperspace.

This also separates the infinite-dimensional situation from the
finite-dimensional Euclidean classification of Gruber and Lettl (1980).
They classify Hausdorff isometries of Euclidean convex bodies as
\(C\mapsto i(C)+D\), with a fixed convex summand \(D\). Under the standard
normalization that the origin singleton is fixed, this fixed summand must
be a singleton and the map reduces to the pointwise action of a linear
Euclidean isometry. The \(c_0\) construction above is origin-fixing but
still thickens every nonzero singleton by an amount depending on its
radius.

Zhou (2022) studied non-surjective \(\varepsilon\)-isometric embeddings of
compact-convex hyperspaces and obtained support-space linearization
results; the available abstract gives a pointwise representation only
under additional finite-dimensional/additivity hypotheses. The full text
of that paper was not inspected here, so it remains the most relevant
unresolved source for originality.

## Originality and limitations

To the best of our knowledge, the radius-extrusion construction and the
resulting proper standard self-isometry of \(\mathcal C(c_0)\) and
\(\mathcal K(c_0)\) have not been recorded in the literature in this form.
The current full text of arXiv:2609.18252 and the published
Gruber--Lettl classification were checked against the claim. Literature
checks also covered non-surjective Hausdorff isometries/embeddings,
compact and bounded convex hyperspaces, product/max-norm constructions,
singleton preservation, and \(c_0\).

The principal residual originality risk is Zhou's 2022 paper
*On non-surjective ε-isometric embeddings between Hausdorff metric spaces
of compact convex subsets* (J. Math. Anal. Appl. 514 (2022), 126282):
its abstract was inspected, but its full text was not available for
inspection. Older hyperspace-embedding literature may also contain an
equivalent product construction under different terminology.

The result is a sharp structural counterexample, not a classification of
all non-surjective Hausdorff isometries.

## References

1. L. Cheng, W. He, C. Liu, Z. Zheng, *Surjective Hausdorff Isometries of Hyperspaces of Bounded Closed Convex Sets*, arXiv:2609.18252 (2026). https://arxiv.org/abs/2609.18252
2. P. M. Gruber, G. Lettl, *Isometries of the Space of Convex Bodies in Euclidean Space*, Bull. London Math. Soc. 12 (1980), 455–462. https://doi.org/10.1112/blms/12.6.455
3. Y. Zhou, *On non-surjective ε-isometric embeddings between Hausdorff metric spaces of compact convex subsets*, J. Math. Anal. Appl. 514 (2022), 126282. https://doi.org/10.1016/j.jmaa.2022.126282
