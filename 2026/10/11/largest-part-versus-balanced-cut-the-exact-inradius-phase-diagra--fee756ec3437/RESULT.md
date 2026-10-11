# Largest part versus balanced cut: the exact inradius phase diagram for complete multipartite symmetric edge polytopes
## Finding
Let
\[
G=K_{n_1,\ldots,n_k},
\qquad k\ge3,
\]
be a complete multipartite graph with part sizes \(n_1,\ldots,n_k\). Put
\[
N=\sum_{i=1}^k n_i,
\qquad
m=\max_i n_i.
\]
Its symmetric edge polytope is
\[
P_G=
\operatorname{conv}
\{\pm(e_u-e_v):uv\in E(G)\}
\subset
H,
\qquad
H=\left\{x\in\mathbb R^N:\sum_v x_v=0\right\},
\]
with the intrinsic Euclidean metric of \(H\).

Define
\[
A_{N,m}
=
m-\frac{m\bmod2}{N}
\]
and
\[
B_N
=
\frac{\lfloor N^2/4\rfloor}{N}.
\]
Then
\[
\boxed{
r_{\mathrm{in}}(P_G)
=
\frac1{\sqrt{\max\{A_{N,m},B_N\}}}.
}
\tag{1}
\]

Equivalently, if \(\operatorname{spread}(G)\) denotes the maximum variance of a real \(1\)-Lipschitz function on the uniformly distributed vertex set of \(G\), then
\[
\boxed{
\operatorname{spread}(G)
=
\max\left\{
\frac{m}{N}-\frac{m\bmod2}{N^2},
\frac{\lfloor N^2/4\rfloor}{N^2}
\right\}.
}
\tag{2}
\]

The two branches have distinct extremal mechanisms.

The first branch is realized by choosing one largest part, assigning the values \(+1\) and \(-1\) there as evenly as parity permits, and assigning \(0\) outside that part.

The second branch is realized by a globally balanced binary labeling with values in \(\{0,1\}\).

The centered maximal ball of \(P_G\) is tangent exactly to the facets whose centered polar normals have maximal Euclidean norm. Using the published complete-multipartite facet classification, this means:
- type-(i) facets supported on a largest part, with \(+1\) and \(-1\) as evenly split as parity permits, whenever \(A_{N,m}\) attains the maximum in (1);
- type-(ii) facets whose \(1\)-level has cardinality \(\lfloor N/2\rfloor\) or \(\lceil N/2\rceil\), whenever \(B_N\) attains the maximum.

At equality
\[
A_{N,m}=B_N,
\]
both mechanisms occur.

## Assumptions and scope
The graph has at least three nonempty parts. This is the range in which the cited source's Proposition 3.5 gives the exact two-type facet classification used below.

The metric is the canonical Euclidean metric in the zero-sum affine span \(H\). The theorem is not invariant under arbitrary affine transformations.

The graph spread in (2) uses unit edge lengths:
\[
|f(u)-f(v)|\le1
\]
for every edge \(uv\).

## Proof
Because
\[
P_G=
\operatorname{conv}\{\pm(e_u-e_v):uv\in E(G)\},
\]
its polar inside \(H\) is
\[
Q_G=
\left\{
y\in H:
|y_u-y_v|\le1
\text{ for every }uv\in E(G)
\right\}.
\tag{3}
\]
The polytope \(P_G\) is centrally symmetric. If a Euclidean ball \(B(c,r)\) lies in \(P_G\), then so does \(B(-c,r)\); convexity implies
\[
B(0,r)
=
\frac12B(c,r)+\frac12B(-c,r)
\subseteq P_G.
\]
Hence the inradius is attained at the origin.

For a centered symmetric convex body,
\[
r_{\mathrm{in}}(P_G)
=
\frac1{R(Q_G)},
\tag{4}
\]
where
\[
R(Q_G)=\max_{y\in Q_G}\|y\|_2.
\]
Thus it remains to compute the circumradius of \(Q_G\).

The source's complete-multipartite facet theorem says that, up to adding a constant, every facet-defining function \(f\) has one of two forms.

Type (i): for one part \(A_i\), the values on \(A_i\) are in \(\{-1,1\}\) and both signs occur, while \(f=0\) on every other part.

Type (ii): \(f\) takes only the values \(0\) and \(1\), subject to the connectivity alternatives stated in that theorem.

Subtracting the mean of \(f\) does not change the corresponding linear functional on \(H\). Therefore the vertices of \(Q_G\) are the centered versions
\[
\widetilde f
=
f-\bar f\mathbf1
\]
of these facet-defining functions.

For a type-(i) facet supported on a part of size \(q\), suppose \(t\) entries are \(+1\) and \(q-t\) are \(-1\). Then
\[
\bar f=\frac{2t-q}{N}
\]
and
\[
\|\widetilde f\|_2^2
=
q-\frac{(2t-q)^2}{N}.
\tag{5}
\]
For fixed \(q\), this is maximal when the two signs are as balanced as possible. Hence
\[
\|\widetilde f\|_2^2
\le
q-\frac{q\bmod2}{N}.
\]
The function
\[
q\longmapsto q-\frac{q\bmod2}{N}
\]
is strictly increasing in the positive integer \(q\), so every type-(i) polar vertex satisfies
\[
\|\widetilde f\|_2^2\le A_{N,m}.
\tag{6}
\]

For a type-(ii) facet, let \(t\) be the number of vertices on which \(f=1\). Then
\[
\bar f=\frac{t}{N}
\]
and
\[
\|\widetilde f\|_2^2
=
\frac{t(N-t)}{N}
\le
\frac{\lfloor N^2/4\rfloor}{N}
=
B_N.
\tag{7}
\]

Since the Euclidean norm is convex, its maximum on \(Q_G\) is attained at a vertex. Equations (6)--(7) therefore give
\[
R(Q_G)^2
\le
\max\{A_{N,m},B_N\}.
\tag{8}
\]

Both upper bounds are globally attainable in \(Q_G\), even before imposing vertexhood.

For the first branch, choose a largest part. Assign \(+1\) and \(-1\) there as evenly as possible and assign \(0\) off that part. Every edge joins different parts, so every edge difference has absolute value \(1\). After subtracting the mean, this gives a point of \(Q_G\) with squared norm
\[
A_{N,m}.
\tag{9}
\]

For the second branch, assign \(1\) to exactly \(\lfloor N/2\rfloor\) vertices and \(0\) to the rest. Every edge difference is at most \(1\), so after centering this gives a point of \(Q_G\) with squared norm
\[
B_N.
\tag{10}
\]

Thus
\[
R(Q_G)^2
=
\max\{A_{N,m},B_N\},
\]
and (1) follows from (4).

For the spread, any \(1\)-Lipschitz function \(f\) becomes an element of \(Q_G\) after subtracting its mean, and
\[
\left\|f-\bar f\mathbf1\right\|_2^2
=
N\,\operatorname{Var}(f).
\]
Therefore
\[
R(Q_G)^2
=
N\,\operatorname{spread}(G),
\]
which gives (2).

Finally, a facet of \(P_G\) is tangent to the centered inball precisely when the corresponding vertex of \(Q_G\) has norm \(R(Q_G)\). Equality in (5) forces a largest part and the most balanced possible sign split. Equality in (7) forces
\[
t\in\left\{\lfloor N/2\rfloor,\lceil N/2\rceil\right\}.
\]
Combining these equality conditions with the source's facet classification gives the stated contact description.

## Verification
The proof is symbolic and applies to every complete multipartite graph with at least three parts.

The critical source premise was checked directly in the full text: Proposition 3.5 classifies every facet-defining function into exactly the two types used above. The same source explicitly defines the symmetric edge polytope by the signed edge-root vectors.

The accompanying `verify.py` enumerates all source-classified facet functions for representative multipartite size vectors, computes the exact squared norm of every centered polar normal, and verifies that their maximum agrees with
\[
\max\left\{
m-\frac{m\bmod2}{N},
\frac{\lfloor N^2/4\rfloor}{N}
\right\}.
\]
It also verifies that the two explicit feasible Lipschitz labelings attain the two candidate values. These finite checks are corroborative only.

## Relationship to prior work
Higashitani, Jochemko, and Michałek give a complete combinatorial facet description of symmetric edge polytopes and specialize it to complete bipartite and complete multipartite graphs. Their Proposition 3.5 is exactly the structural input used here. Their paper studies facets, Gröbner bases, triangulations, Ehrhart \(h^*\)-polynomials, real-rootedness, and related arithmetic structure. The inspected full text contains no occurrence of “inradius,” “circumradius,” “Euclidean,” or “variance.”

The graph spread was introduced earlier as the maximum variance of a \(1\)-Lipschitz function. Addario-Berry, Janson, and McDiarmid survey this invariant and record the complete-graph value, then study random graph models. Their inspected full text contains no complete-multipartite spread formula.

Targeted searches for complete-multipartite graph spread, Lipschitz variance, complete-multipartite symmetric-edge-polytope inradius, polar circumradius, and the largest-part/balanced-cut phase description did not locate a theorem implying (1)--(2).

A previous wheel-family computation concerns the same polytope construction but a different graph family and a different extremal facet combinatorics. The present theorem uses the source's complete classification of multipartite facets and exhibits a two-mechanism phase competition that does not follow from the wheel formula.

## Limitations
The theorem is restricted to complete multipartite graphs with at least three parts.

The Euclidean inradius depends on the canonical root realization and is not affine invariant.

The originality assessment leaves a residual risk that the spread formula is known under another name in graph concentration or Lipschitz-function literature. The source facet classification makes the derivation short once the metric question is posed, so an unindexed folklore observation is plausible.

The theorem does not compute circumradii of \(P_G\), John ellipsoids, or non-Euclidean inradii.

## References
1. Akihiro Higashitani, Katharina Jochemko, and Mateusz Michałek, *Arithmetic Aspects of Symmetric Edge Polytopes*, arXiv:1807.07678, first public version 2018-07-20; Mathematika 65 (2019), 763--784, DOI 10.1112/S0025579319000147.
2. Louigi Addario-Berry, Svante Janson, and Colin McDiarmid, *On the Spread of Random Graphs*, arXiv:0902.1156; Combinatorics, Probability and Computing 23 (2014), 745--765, DOI 10.1017/S0963548314000248.
