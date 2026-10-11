# The Euclidean diameter of partial permutohedra saturates exactly at \(m=2n\)
## Finding
For positive integers
\[
m,n\ge1,
\]
let
\[
\mathcal P(m,n)
=
\operatorname{conv}
\left\{
x\in\{0,1,\ldots,n\}^m:
\text{the nonzero coordinates of }x\text{ are distinct}
\right\}
\subset\mathbb R^m
\tag{1}
\]
be the standard partial permutohedron.

Put
\[
s=\min\{m,2n\},
\qquad
a=\left\lfloor\frac s2\right\rfloor,
\qquad
b=\left\lceil\frac s2\right\rceil,
\tag{2}
\]
and define
\[
S_n(k)
=
\sum_{r=0}^{k-1}(n-r)^2
\qquad
(0\le k\le n).
\tag{3}
\]
Then
\[
\boxed{
\operatorname{diam}_2\mathcal P(m,n)
=
\sqrt{S_n(a)+S_n(b)}.
}
\tag{4}
\]

The sum in (3) can be written without summation as
\[
S_n(k)
=
\frac{
n(n+1)(2n+1)
-
(n-k)(n-k+1)(2n-2k+1)
}{6}.
\tag{5}
\]

The formula exhibits a sharp dimension threshold. If
\[
m=2q\le2n,
\]
then
\[
\boxed{
\operatorname{diam}_2^2\mathcal P(2q,n)
=
2\sum_{j=n-q+1}^{n}j^2.
}
\tag{6}
\]
If
\[
m=2q+1<2n,
\]
then
\[
\boxed{
\operatorname{diam}_2^2\mathcal P(2q+1,n)
=
2\sum_{j=n-q+1}^{n}j^2+(n-q)^2.
}
\tag{7}
\]
For every
\[
m\ge2n,
\]
the diameter stops growing:
\[
\boxed{
\operatorname{diam}_2^2\mathcal P(m,n)
=
2\sum_{j=1}^{n}j^2
=
\frac{n(n+1)(2n+1)}3.
}
\tag{8}
\]

There is also an exact equality classification.

If
\[
s=2q,
\]
then every diameter pair consists of two vertices with disjoint supports, each having nonzero-value set
\[
\{n-q+1,\ldots,n\}.
\tag{9}
\]
If
\[
s=2q+1,
\]
then every diameter pair has disjoint supports, with one endpoint having nonzero-value set
\[
\{n-q,\ldots,n\}
\tag{10}
\]
and the other having
\[
\{n-q+1,\ldots,n\},
\tag{11}
\]
with the two roles interchangeable. In (9)--(11), the listed values may be placed in any order on the chosen supports.

Thus, when
\[
m\ge2n,
\]
both endpoints of every diameter pair use every value
\[
1,\ldots,n
\]
on disjoint supports. Extra ambient coordinates beyond \(2n\) are metrically inert for the diameter.

## Assumptions and scope
The metric is the standard Euclidean metric of \(\mathbb R^m\).

The source defines \(\mathcal P(m,n)\) by (1), proves it is full-dimensional, and records the vertex structure: a vertex with \(k\) nonzero coordinates uses exactly
\[
n,n-1,\ldots,n-k+1.
\tag{12}
\]
The proof below uses only this vertex structure and elementary Euclidean inequalities.

The diameter is the ambient Euclidean diameter
\[
\sup\{\|x-y\|_2:x,y\in\mathcal P(m,n)\},
\]
not the graph diameter of the one-skeleton.

## Proof
We first note that a Euclidean diameter pair of a polytope can be chosen among its vertices. In fact, every endpoint of a diameter pair is extreme. Suppose
\[
x=tu+(1-t)v,
\qquad
0<t<1,
\]
with distinct \(u,v\) in the polytope, and suppose \(y\) is at diameter distance \(D\) from \(x\). Then
\[
D
=
\|x-y\|_2
\le
t\|u-y\|_2+(1-t)\|v-y\|_2
\le
D.
\]
Equality in the Euclidean triangle inequality would force \(u-y\) and \(v-y\) to lie on the same ray, while equality in the second inequality forces both to have norm \(D\). Hence \(u=v\), a contradiction.

So let \(u,v\) be vertices of \(\mathcal P(m,n)\). For each coordinate,
\[
(u_i-v_i)^2
=
u_i^2+v_i^2-2u_iv_i
\le
\max\{u_i^2,v_i^2\},
\tag{13}
\]
because \(u_i,v_i\ge0\). Summing gives
\[
\|u-v\|_2^2
\le
\sum_{i=1}^m\max\{u_i^2,v_i^2\}.
\tag{14}
\]

By (12), the positive coordinates of each endpoint form a prefix of
\[
n,n-1,\ldots,1.
\]
Consequently, the nonzero terms on the right side of (14) form a submultiset of two copies of
\[
n^2,(n-1)^2,\ldots,1.
\tag{15}
\]
There are at most \(m\) coordinate maxima. Therefore the largest possible value of the right side of (14) is the sum of the \(m\) largest entries of the doubled list (15), or all \(2n\) positive entries if \(m>2n\).

The \(s=\min\{m,2n\}\) largest entries of the doubled list consist of two copies of
\[
n^2,(n-1)^2,\ldots,(n-a+1)^2
\]
when \(s=2a\), and, when \(s=2a+1\), those same doubled entries together with one copy of
\[
(n-a)^2.
\]
This is exactly
\[
S_n(a)+S_n(b).
\]
Hence
\[
\|u-v\|_2^2
\le
S_n(a)+S_n(b).
\tag{16}
\]

The bound is attained. Choose disjoint coordinate supports of sizes \(a\) and \(b\). On the first support place
\[
n,n-1,\ldots,n-a+1,
\]
and on the second support place
\[
n,n-1,\ldots,n-b+1.
\]
These are vertices by the source vertex description. Since the supports are disjoint, their squared distance is exactly the right side of (16). This proves (4), and (6)--(8) follow immediately.

It remains to prove the equality classification. Equality in (13) is strict whenever both \(u_i\) and \(v_i\) are positive. Thus every diameter pair has disjoint supports.

Next, equality in (16) requires the collection of positive coordinate squares occurring across the two endpoints to be exactly the \(s\) largest entries of the doubled list (15). If
\[
s=2q,
\]
those entries are two copies of
\[
n^2,(n-1)^2,\ldots,(n-q+1)^2.
\]
Since each endpoint can use a positive value at most once and its nonzero values form a prefix, both endpoints must use exactly the values in (9).

If
\[
s=2q+1,
\]
the top \(s\) entries are two copies through
\[
(n-q+1)^2
\]
and one copy of
\[
(n-q)^2.
\]
Hence one endpoint uses the prefix of length \(q+1\), the other the prefix of length \(q\), proving (10)--(11). The coordinate order is irrelevant to the squared distance, so arbitrary permutations on the two disjoint supports remain extremal.

This proves the theorem and the complete equality classification.

## Verification
The proof is exact for every pair of positive integers \(m,n\).

The source-dependent premise was checked directly in the full primary text: the definition of partial permutohedra and the vertex characterization in Proposition 2.7. The same paper also identifies partial permutohedra as anti-blocking versions of permutohedra and develops their face lattice, volume, and Ehrhart theory.

The earlier Heuer--Striker full text was inspected as the introduction of the family. Its program is inequality descriptions, facets, face lattices, projections, and volume. Neither inspected full text contains a Euclidean-diameter theorem; direct searches for “diameter” and “Euclidean” returned no matching metric statement.

The accompanying `verify.py` exhaustively enumerates the source vertices for
\[
1\le m,n\le5,
\]
checks every vertex pair, confirms (4), and verifies that every maximizing pair has exactly the disjoint-support and value-set structure in (9)--(11). This finite replay is corroborative only.

## Relationship to prior work
Behrend, Castillo, Chavez, Diaz-Lopez, Escobar, Harris, and Insko study the face lattice, volume, Ehrhart polynomial, generalized-permutohedron realization, and anti-blocking realization of partial permutohedra. Their explicit vertex structure is the only nontrivial source input needed here.

Heuer and Striker introduced the family earlier as a projection of partial alternating-sign-matrix polytopes and determined its inequality, facet, and face-lattice structure.

Existing Euclidean inradius results for partial permutohedra answer the opposite supporting-hyperplane problem. They do not imply the present vertex-pair optimization: the diameter is controlled by two disjoint prefix supports, and its sharp \(m=2n\) saturation has no inradius analogue.

Likewise, graph-diameter results for related generalized parking-function or permutohedral objects concern shortest paths in a one-skeleton rather than ambient Euclidean distance.

Targeted searches under “partial permutohedron”, “partial permutation polytope”, “parking function polytope”, “anti-blocking permutohedron”, “Euclidean diameter”, and “stellohedron” did not locate a statement implying (4)--(11).

## Limitations
The theorem concerns the standard coordinate realization of partial permutohedra.

It does not determine graph diameter, minimum enclosing radius, width, John or Löwner ellipsoids, or Euclidean diameters of arbitrary generalized permutohedra.

The proof uses positivity and the prefix structure of source vertices. An analogous diameter formula need not hold for a general anti-blocking polytope.

A broader theorem for down-closed permutation-orbit polytopes could subsume the same doubled-spectrum argument under different terminology. No such dominating statement was located in the targeted comparisons.

## References
1. Roger E. Behrend, Federico Castillo, Anastasia Chavez, Alexander Diaz-Lopez, Laura Escobar, Pamela E. Harris, and Erik Insko, *Partial permutohedra*, arXiv:2207.14253, first public version 2022-07-28; *Discrete & Computational Geometry* 76 (2026), 589--642, DOI 10.1007/s00454-025-00755-0.
2. Dylan Heuer and Jessica Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, first public version 2020-12-17; *SIAM Journal on Discrete Mathematics* 36 (2022), 2863--2888, DOI 10.1137/21M1417958.
