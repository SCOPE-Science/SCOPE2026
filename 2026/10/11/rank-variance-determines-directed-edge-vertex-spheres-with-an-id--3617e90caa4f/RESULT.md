# Rank variance determines directed-edge vertex spheres, with an ideal criterion for optimality
## Finding
Let
\[
Q=(V,A)
\]
be a finite connected quiver without loops or multiple edges, with
\[
|V|=N\ge3.
\]
Assume that \(Q\) has a rank function
\[
\rho:V\to\mathbb R
\]
such that
\[
\rho(v)+1=\rho(w)
\]
for every arrow \(v\to w\).

Write
\[
\bar\rho=\frac1N\sum_{v\in V}\rho(v),
\qquad
r_v=\rho(v)-\bar\rho,
\qquad
S=\sum_{v\in V}r_v^2.
\tag{1}
\]
The directed edge polytope is
\[
\operatorname{DE}(Q)
=
\operatorname{conv}\{e_v-e_w:v\to w\}
\subset\mathbb R^V.
\tag{2}
\]

Then every vertex of \(\operatorname{DE}(Q)\) lies on one common Euclidean sphere inside its affine hull. The center and squared radius are
\[
\boxed{
c=-\frac{r}{S}
}
\tag{3}
\]
and
\[
\boxed{
R^2=2-\frac1S.
}
\tag{4}
\]
This sphere is unique in the affine hull.

The common vertex sphere is the **minimum enclosing sphere** of \(\operatorname{DE}(Q)\) if and only if
\[
\boxed{
\sum_{v\in I}r_v\le0
\quad
\text{for every lower ideal }I
}
\tag{5}
\]
of the graded poset whose Hasse diagram is \(Q\).

Equivalently, (5) holds if and only if there are coefficients
\[
\lambda_a\ge0
\qquad
(a\in A)
\]
such that
\[
\sum_{a\in A}\lambda_a=1
\]
and
\[
c=\sum_{v\to w}\lambda_{v\to w}(e_v-e_w).
\tag{6}
\]
Thus the optimality criterion is exactly a nonnegative flow-feasibility condition.

If (5) fails, the sphere (3)--(4) still passes through every vertex, but it is not the minimum enclosing sphere; the true minimum enclosing radius is strictly smaller than \(R\).

## Assumptions and scope
The quiver is connected, loopless, and has no multiple edges. The result uses the source convention
\[
\varepsilon(v,w)=e_v-e_w
\]
for an arrow \(v\to w\).

A rank function is only defined up to addition of a constant. The centered vector \(r\), the quantity \(S\), the sphere center \(c\), and the radius \(R\) are therefore intrinsic to the ranked quiver.

The metric is the standard Euclidean metric in \(\mathbb R^V\), restricted to the affine hull of the directed edge polytope.

The theorem distinguishes two notions: a sphere through all vertices and the smallest sphere containing the polytope. They coincide exactly under the lower-ideal condition (5).

## Proof
The source proves that every arrow vector
\[
e_v-e_w
\]
is a vertex of \(\operatorname{DE}(Q)\), and that for a connected quiver with a rank function,
\[
\dim \operatorname{DE}(Q)=N-2.
\tag{7}
\]

Every arrow vector has coordinate sum zero. Since
\[
\rho(v)-\rho(w)=-1,
\]
it also satisfies
\[
\langle r,e_v-e_w\rangle=-1.
\]
Hence
\[
\operatorname{aff}\operatorname{DE}(Q)
\subset
H
=
\left\{
x:
\langle\mathbf1,x\rangle=0,\ 
\langle r,x\rangle=-1
\right\}.
\tag{8}
\]
The two normals \(\mathbf1\) and \(r\) are orthogonal, and \(r\ne0\). Therefore \(H\) has dimension \(N-2\). By (7),
\[
\operatorname{aff}\operatorname{DE}(Q)=H.
\tag{9}
\]

The point of \(H\) closest to the origin is
\[
c=-\frac rS.
\]
For every arrow vertex
\[
a=e_v-e_w,
\]
we have
\[
\|a\|^2=2,
\qquad
\langle a,c\rangle=\frac1S,
\qquad
\|c\|^2=\frac1S.
\]
Therefore
\[
\|a-c\|^2
=
2-\frac2S+\frac1S
=
2-\frac1S.
\tag{10}
\]
This proves (3)--(4).

Because the affine differences of the vertices span the tangent space of \(H\), a point of \(H\) equidistant from all vertices is unique. Thus (3) is the unique center of a sphere in \(H\) through all vertices.

It remains to characterize when that sphere is the minimum enclosing sphere.

A finite set of points all lying on a sphere of center \(c\) and radius \(R\) has that sphere as its minimum enclosing sphere exactly when
\[
c
\]
lies in the convex hull of the points. Indeed, if
\[
c=\sum_i\lambda_i a_i,
\qquad
\lambda_i\ge0,
\qquad
\sum_i\lambda_i=1,
\]
then for any alternative center \(q\),
\[
\sum_i\lambda_i\|a_i-q\|^2
=
R^2+\|q-c\|^2,
\]
so some vertex has distance at least \(R\) from \(q\), with strict inequality unless \(q=c\). Conversely, if \(c\) is outside the convex hull, strict separation allows a small shift of \(c\) toward the vertex hull that decreases every vertex distance.

Thus the common sphere is minimum exactly when (6) has a solution.

Interpret the coefficients \(\lambda_{v\to w}\) as a nonnegative flow on the arrows, with incidence convention
\[
e_v-e_w.
\]
Equation (6) prescribes the divergence
\[
c_v=-\frac{r_v}{S}.
\tag{11}
\]
The sum of the entries of \(c\) is zero. Also,
\[
\langle r,c\rangle=-1.
\]
Since every arrow vector has scalar product \(-1\) with \(r\), any nonnegative flow with divergence \(c\) automatically has total mass
\[
\sum_a\lambda_a=1.
\]

The source proves that a rank-function quiver is the Hasse diagram of a graded poset. Let \(I\) be a lower ideal. No arrow enters \(I\) from its complement. Summing the divergence equation over \(I\) gives
\[
\sum_{v\in I}c_v
=
\text{total flow leaving }I
\ge0.
\]
By (11), this is equivalent to
\[
\sum_{v\in I}r_v\le0.
\]
So (5) is necessary.

For sufficiency, build a transshipment network: vertices with \(c_v>0\) supply \(c_v\), vertices with \(c_v<0\) demand \(-c_v\), and the original arrows have unlimited capacity. The max-flow/min-cut theorem says that the prescribed divergence is feasible exactly when every upper ideal \(U\) has
\[
\sum_{v\in U}c_v\le0.
\]
Taking complements and using \(\sum_vc_v=0\), this is equivalent to
\[
\sum_{v\in I}c_v\ge0
\]
for every lower ideal \(I\), which is exactly (5). Hence (5), (6), and minimum-sphere optimality are equivalent.

## Verification
The proof is symbolic and applies to every connected rank-function quiver with at least three vertices.

The source-dependent facts were checked directly in the primary full text and page image: the definition of a directed edge polytope, the fact that all arrow vectors are vertices, the rank-function definition, the affine rank hyperplane, the dimension formula, and the equivalence with Hasse diagrams of graded posets.

The accompanying `verify.py` exhaustively checks a large collection of connected graded quivers on at most five labeled vertices. It verifies the exact common-sphere identity with rational arithmetic and independently compares the lower-ideal inequalities with a rational max-flow feasibility test for the barycentric flow (6). It also checks an explicit quiver for which the ideal condition fails, confirming that the criterion is nonvacuous. These finite checks are corroborative only.

## Relationship to prior work
Numata, Takahashi, and Tamaki give the complete dimension and face theory of directed edge polytopes in terms of rank functions and connectivity. Their paper provides exactly the affine rank hyperplane used in the proof, but it does not state a Euclidean circumsphere, circumcenter, minimum-enclosing-ball, or rank-variance theorem.

Kálmán and Tóthmérész study the same root-vector construction for semi-balanced directed graphs. Their potential function is the same rank-function phenomenon up to sign convention, and they develop dissections, triangulations, and Ehrhart theory. Their paper does not state the Euclidean vertex-sphere formula or the lower-ideal optimality criterion.

Earlier toric work on directed edge polytopes studies reflexivity, terminality, smoothness, and rigidity. Those lattice and toric properties do not determine the metric sphere in the standard coordinate realization.

A previously derived oriented-cycle Ehrhart theorem concerns exact \(h^*\)-polynomials and lattice volume. It does not imply the rank-variance sphere formula or the minimum-enclosing criterion for arbitrary graded quivers.

Targeted published-result and literature searches under “directed edge polytope”, “root polytope”, “rank function”, “circumsphere”, “circumcenter”, “minimum enclosing ball”, “Chebyshev center”, and “rank variance” did not locate a theorem implying (3)--(6).

## Limitations
The formula (4) gives the radius of the unique sphere through all vertices. It is the minimum enclosing radius only under the equivalent conditions (5)--(6).

The theorem does not give a closed formula for the true minimum enclosing radius when (5) fails.

The result is tied to the standard incidence-vector realization. General affine images do not preserve the Euclidean quantities.

A residual originality risk remains that the common-sphere calculation appears implicitly in oriented-matroid or flow-polytope literature under different terminology. The minimum-enclosing criterion is stated here explicitly in graded-poset language.

## References
1. Yasuhide Numata, Yusuke Takahashi, and Dai Tamaki, *Faces of Directed Edge Polytopes*, arXiv:2203.14521, first public version 2022-03-28; Australasian Journal of Combinatorics 88(1) (2024), 77--96.
2. Tamás Kálmán and Lilla Tóthmérész, *Root polytopes and Jaeger-type dissections for directed graphs*, arXiv:2105.00960, first public version 2021-05-03; Mathematika 68 (2022), 1176--1220.
3. Selvi Kara, Irem Portakal, and Akiyoshi Tsuchiya, *Rigid Gorenstein toric Fano varieties arising from directed graphs*, arXiv:2103.06404, first public version 2021-03-11; Collectanea Mathematica 74 (2023), 333--351.
