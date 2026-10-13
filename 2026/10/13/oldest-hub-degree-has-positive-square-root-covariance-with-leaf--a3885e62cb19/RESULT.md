# Oldest-hub degree has positive square-root covariance with leaf abundance

## Finding

Start from the single edge on vertices \(1,2\). When the tree has \(n\ge2\) vertices, add vertex \(n+1\) and attach it to an existing vertex with probability proportional to its current degree. Let
\[
D_n
\]
be the degree of the initial vertex \(1\), and let
\[
L_n
\]
be the total number of leaves.

Define
\[
q_n=\mathbb P(D_n=1)
=\prod_{r=1}^{n-2}\frac{2r-1}{2r}
=\frac{\Gamma(n-\tfrac32)}{\sqrt{\pi}\,\Gamma(n-1)}.
\]
Then
\[
\mathbb E D_n=(2n-3)q_n
\tag{1}
\]
and
\[
\mathbb E L_n=\frac{2(n-1)}3+\frac{4q_n}3.
\tag{2}
\]

Put
\[
c_n=\operatorname{Cov}(D_n,L_n).
\]
The covariance satisfies the exact increment law
\[
\boxed{
c_{n+1}-c_n
=
\frac{q_n}{3(n-1)^2}
\left(
(n-1)(n-3)+(2n-3)q_n
\right).
}
\tag{3}
\]
Since \(c_2=0\), this gives
\[
\boxed{
c_n
=
\sum_{k=2}^{n-1}
\frac{q_k}{3(k-1)^2}
\left(
(k-1)(k-3)+(2k-3)q_k
\right).
}
\tag{4}
\]

The first increment vanishes and every subsequent increment is positive. Hence
\[
\boxed{
c_2=c_3=0,
\qquad
c_n>0\quad(n\ge4),
}
\tag{5}
\]
and \(c_n\) is strictly increasing from \(n=3\) onward.

Finally,
\[
q_n\sim\frac1{\sqrt{\pi n}},
\]
so (3) yields
\[
c_{n+1}-c_n
\sim
\frac1{3\sqrt{\pi n}},
\]
and summation gives
\[
\boxed{
\operatorname{Cov}(D_n,L_n)
\sim
\frac{2}{3\sqrt{\pi}}\sqrt n.
}
\tag{6}
\]

Thus the oldest hub and the global leaf population are positively coupled, despite competing for individual attachment events, and the coupling grows on the same square-root scale as the expected degree of the oldest vertex.

## Assumptions and scope

The model is the one-edge Barabási–Albert tree with initial graph consisting of one edge. At size \(n\), the sum of degrees is \(2(n-1)\).

The distinguished vertex is one of the two initial vertices. By symmetry either endpoint of the initial edge has the same law.

The result concerns the degree of one fixed oldest vertex against the total number of degree-one vertices. It is not a statement about the covariance between aggregate degree-class counts, nor about the number of leaf neighbors of a typical vertex.

## Proof

At size \(n\), write
\[
X_n=\mathbf 1\{\text{vertex }n+1\text{ attaches to vertex }1\}
\]
and
\[
Y_n=\mathbf 1\{\text{vertex }n+1\text{ attaches to a leaf}\}.
\]
Then
\[
D_{n+1}=D_n+X_n,
\qquad
L_{n+1}=L_n+1-Y_n.
\tag{7}
\]

Conditionally on the tree at size \(n\),
\[
\mathbb E[X_n\mid T_n]
=
\frac{D_n}{2(n-1)}
\tag{8}
\]
and, because every leaf has degree one,
\[
\mathbb E[Y_n\mid T_n]
=
\frac{L_n}{2(n-1)}.
\tag{9}
\]

Let
\[
R_n=\mathbf 1\{D_n=1\}.
\]
The events \(X_n=1\) and \(Y_n=1\) occur simultaneously exactly when the distinguished vertex is still a leaf and is selected. Hence
\[
\mathbb E[X_nY_n\mid T_n]
=
\frac{R_n}{2(n-1)}.
\tag{10}
\]

The vertex remains a leaf from size \(n\) to size \(n+1\) unless it is selected. Therefore
\[
q_{n+1}
=
\left(1-\frac1{2(n-1)}\right)q_n,
\qquad q_2=1,
\tag{11}
\]
which gives the product and gamma-function formula above.

Taking expectations in (7)--(9) gives
\[
d_{n+1}
=
\left(1+\frac1{2(n-1)}\right)d_n,
\qquad d_2=1,
\tag{12}
\]
where \(d_n=\mathbb E D_n\), and
\[
\ell_{n+1}
=
\left(1-\frac1{2(n-1)}\right)\ell_n+1,
\qquad \ell_2=2,
\tag{13}
\]
where \(\ell_n=\mathbb E L_n\).
Equations (11)--(13) give (1)--(2).

Now expand the mixed product:
\[
D_{n+1}L_{n+1}
=
D_nL_n+D_n-D_nY_n+X_nL_n+X_n-X_nY_n.
\]
By (8)--(10), the two middle conditional terms cancel:
\[
\mathbb E[D_nY_n\mid T_n]
=
\mathbb E[X_nL_n\mid T_n]
=
\frac{D_nL_n}{2(n-1)}.
\]
Therefore, if
\[
M_n=\mathbb E[D_nL_n],
\]
then
\[
M_{n+1}
=
M_n+
\left(1+\frac1{2(n-1)}\right)d_n
-
\frac{q_n}{2(n-1)}.
\tag{14}
\]

Subtracting \(d_{n+1}\ell_{n+1}\) from (14), using (12)--(13), gives
\[
c_{n+1}-c_n
=
\frac{d_n\ell_n}{4(n-1)^2}
-
\frac{q_n}{2(n-1)}.
\tag{15}
\]
Substitution of (1)--(2) simplifies (15) to (3).

For \(n=2\), the bracket in (3) is zero. For \(n=3\), its first term is zero and its second term is positive. For every \(n\ge4\), both terms are positive. This proves (4)--(5).

Finally, the gamma-ratio asymptotic gives
\[
q_n=\frac1{\sqrt{\pi n}}\left(1+O(n^{-1})\right).
\]
Substitution into (3) gives
\[
c_{n+1}-c_n
=
\frac1{3\sqrt{\pi n}}+O(n^{-3/2}).
\]
Summing the asymptotic increments proves (6).

## Verification

The accompanying checker performs exact rational dynamic enumeration of all attachment states through size \(9\). It reconstructs the attachment probabilities from the degree-proportional rule rather than sampling.

For every \(2\le n\le9\), it verifies the exact formulas for \(q_n\), \(\mathbb E D_n\), \(\mathbb E L_n\), the mixed moment \(\mathbb E[D_nL_n]\), and the covariance sum (4). It separately verifies each finite increment (3).

It also evaluates the normalized covariance at large \(n\) from the exact recurrence as a numerical check on the constant in (6). This finite computation is supplementary; the all-\(n\) formulas and asymptotic are proved analytically above.

## Relationship to prior work

Peköz, Röllin, and Ross study joint degree counts and degree order statistics in proportional-attachment random graphs. Their model with one outgoing edge is explicitly the usual Barabási–Albert proportional-attachment tree. Their results provide the fixed-old-vertex degree context but do not introduce the total leaf count in the inspected full text.

Hartle and Krapivsky study leaves of preferential-attachment trees in detail. Their full text develops the joint degree--leafdegree distribution of typical vertices and finite-size fluctuations of aggregate counts such as the total number of leaves and the number of degree-two vertices. In particular, they derive aggregate covariances involving leaf counts. The inspected paper contains no occurrence of “oldest” and does not state a covariance between the degree of a distinguished initial vertex and the global number of leaves.

Feng and Hu study scale-free trees in the combinatorial-probability literature; the journal record classifies the paper primarily under \(60C05\). This supports the probabilistic classification of the present tree model.

The present result concerns a different local--global pair: one persistent old vertex versus the entire leaf population. Aggregate degree-count covariance formulas do not imply (3), because a distinguished old vertex has a nonstationary degree scale and its contribution is not exchangeable with a uniformly sampled vertex.

## Limitations

The initial seed is a single edge. A larger seed changes the exact survival probability of the distinguished seed vertex and therefore changes the finite constants.

Only the linear degree-proportional attachment rule is treated. Initial attractiveness or nonlinear attachment changes the denominators and the leaf-selection law.

The result proves a covariance and its asymptotic scale, not a joint limit theorem. It does not assert positive association for arbitrary functions of \(D_n\) and \(L_n\).

The originality comparison cannot exclude every older implicit recurrence in the extensive preferential-attachment literature. The closest inspected full leaf paper treats aggregate leaf/degree-count covariances rather than the distinguished-oldest-vertex statistic.

## References

1. E. A. Peköz, A. Röllin, and N. Ross, “Joint degree distributions of preferential attachment random graphs,” arXiv:1402.4686, first submitted 2014-02-19; later *Advances in Applied Probability* 49 (2017), 368–387.
2. H. Hartle and P. L. Krapivsky, “Leaves of preferential attachment trees,” arXiv:2602.01021, first submitted 2026-02-01.
3. Q. Feng and Z. Hu, “Phase Changes in the Topological Indices of Scale-Free Trees,” *Journal of Applied Probability* 50 (2013), 516–532, DOI 10.1239/jap/1371648958.
