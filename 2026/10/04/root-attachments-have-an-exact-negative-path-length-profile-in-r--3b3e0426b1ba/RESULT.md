# Root attachments have an exact negative path-length profile in random recursive trees

## Finding

Let
\[
\mathcal T_n,
\qquad
n\ge2,
\]
be the standard random recursive tree on vertices
\[
\{1,\ldots,n\}.
\]
Equivalently, for every \(j\ge2\), vertex \(j\) independently chooses a parent
\[
P_j\sim\operatorname{Unif}\{1,\ldots,j-1\}.
\]

Let
\[
A_j=\mathbf 1\{P_j=1\},
\qquad
R_n=\sum_{j=2}^n A_j
\]
so that \(R_n\) is the outdegree of the root. Let
\[
T_n=\sum_{v=1}^n D(v)
\]
be the total path length, where \(D(v)\) is the graph distance from the root to \(v\).

Write
\[
H_m=\sum_{r=1}^m\frac1r,
\qquad
H_m^{(2)}=\sum_{r=1}^m\frac1{r^2}.
\]

Then every individual root attachment has an exact covariance with the final total path length:
\[
\boxed{
\operatorname{Cov}(A_j,T_n)
=
-\frac{n(H_{j-1}-1)}{j(j-1)},
\qquad
2\le j\le n.
}
\tag{1}
\]
The \(j=2\) value is zero because \(A_2=1\) deterministically, and every value for \(j\ge3\) is strictly negative.

The local statement is stronger than a covariance sign. For every \(3\le j\le n\),
\[
\boxed{
T_n\mid(A_j=1)
<
_{\mathrm{st}}
T_n\mid(A_j=0).
}
\tag{2}
\]
Indeed, the two conditional laws admit a coupling under which their difference is strictly positive almost surely.

Consequently, for every nondecreasing function \(h\) for which the covariance exists,
\[
\boxed{
\operatorname{Cov}(R_n,h(T_n))\le0.
}
\tag{3}
\]
If \(n\ge3\) and \(h\) is strictly increasing on the realized support of \(T_n\), then the inequality is strict.

Summing (1) yields the exact global covariance
\[
\boxed{
\operatorname{Cov}(R_n,T_n)
=
H_n-1-n\bigl(H_n^{(2)}-1\bigr)
<0,
\qquad
n\ge3.
}
\tag{4}
\]

The root-degree variance is
\[
\operatorname{Var}(R_n)
=
H_{n-1}-H_{n-1}^{(2)}.
\tag{5}
\]
The classical centered path-length limit has variance
\[
2-\frac{\pi^2}{6}.
\]
Therefore
\[
\boxed{
\frac{\operatorname{Cov}(R_n,T_n)}n
\longrightarrow
-\left(\frac{\pi^2}{6}-1\right),
}
\tag{6}
\]
while the correlation vanishes only logarithmically:
\[
\boxed{
\sqrt{\log n}\,
\operatorname{Corr}(R_n,T_n)
\longrightarrow
-\frac{\pi^2/6-1}{\sqrt{2-\pi^2/6}}.
}
\tag{7}
\]

Thus direct attachment to the root has a persistent path-shortening effect. Root degree and total search cost have covariance of linear order in \(n\), even though their correlation tends to zero because root-degree fluctuations grow on the \(\sqrt{\log n}\) scale while total-path-length fluctuations grow on the \(n\) scale.

## Assumptions and scope

The model is the uniform random recursive tree: the parent variables \(P_2,\ldots,P_n\) are mutually independent, and \(P_j\) is uniform on the earlier labels.

The total path length uses edge distance from the root. Some older increasing-tree literature uses a node-count convention for path length; that convention differs by the deterministic quantity \(n\), which does not change any covariance in the finding.

The stochastic order in (2) compares only the two conditional laws obtained by forcing one specified arrival \(j\) either to attach to the root or not. Equation (3) follows by summing the resulting local covariance inequalities. No claim is made that \(T_n\) is stochastically monotone conditional on the entire root degree \(R_n\).

## Proof

Fix
\[
3\le j\le n.
\]
Condition first on
\[
A_j=1,
\]
so the parent of \(j\) is the root. Under the complementary conditioning
\[
A_j=0,
\]
the parent
\[
Q_j=P_j
\]
is uniform on
\[
\{2,\ldots,j-1\}.
\]

Couple the two conditional trees by using the same parent variables at every time other than \(j\), and use the same pre-\(j\) tree in both copies. In the \(A_j=1\) tree set
\[
P_j=1,
\]
while in the \(A_j=0\) tree set
\[
P_j=Q_j.
\]

Let
\[
S_{j,n}
\]
be the final number of vertices in the subtree rooted at \(j\), including \(j\) itself. Changing only the parent edge of \(j\) does not change which later vertices descend from \(j\), so \(S_{j,n}\) is the same in both coupled trees.

Every vertex in this subtree is deeper by exactly
\[
D(Q_j)
\]
when \(j\) attaches to \(Q_j\) rather than directly to the root. Hence
\[
\boxed{
T_n^{(0)}-T_n^{(1)}
=
S_{j,n}D(Q_j),
}
\tag{8}
\]
where the superscripts indicate \(A_j=0\) and \(A_j=1\), respectively.

Since
\[
S_{j,n}\ge1
\]
and every possible \(Q_j\) is a nonroot vertex,
\[
D(Q_j)\ge1.
\]
Thus the right-hand side of (8) is strictly positive almost surely. This proves (2).

The future parent choices are independent of the pre-\(j\) tree and of \(Q_j\). Standard recursive-tree growth gives
\[
\mathbb E S_{j,n}=\frac nj.
\tag{9}
\]
Indeed, if the subtree has size \(s\) when the whole tree has \(t\) vertices, the next vertex joins it with probability \(s/t\); iterating the expectation from size one at time \(j\) gives (9).

For a vertex \(q\), the standard recursive-tree depth mean is
\[
\mathbb E D(q)=H_{q-1}.
\]
Therefore
\[
\begin{aligned}
\mathbb E D(Q_j)
&=
\frac1{j-2}
\sum_{q=2}^{j-1}H_{q-1}\\
&=
\frac{j-1}{j-2}\bigl(H_{j-1}-1\bigr).
\end{aligned}
\tag{10}
\]

The two factors in (8) are independent, so
\[
\mathbb E[T_n\mid A_j=0]
-
\mathbb E[T_n\mid A_j=1]
=
\frac{n(j-1)}{j(j-2)}
\bigl(H_{j-1}-1\bigr).
\tag{11}
\]

Now
\[
\Pr(A_j=1)=\frac1{j-1}.
\]
For a Bernoulli variable \(A\) and an integrable \(X\),
\[
\operatorname{Cov}(A,X)
=
\Pr(A=1)\Pr(A=0)
\left(
\mathbb E[X\mid A=1]-\mathbb E[X\mid A=0]
\right).
\tag{12}
\]
Substituting (11) into (12) proves (1) for \(j\ge3\); the case \(j=2\) is immediate.

The same coupling proves more. If \(h\) is nondecreasing, then
\[
\mathbb E[h(T_n)\mid A_j=1]
\le
\mathbb E[h(T_n)\mid A_j=0],
\]
so
\[
\operatorname{Cov}(A_j,h(T_n))\le0.
\]
Summing over
\[
R_n=\sum_{j=2}^nA_j
\]
gives (3). Strictness follows from (8) when \(h\) is strictly increasing.

To sum the local covariances, put
\[
m=j-1.
\]
The identity
\[
\frac{H_m-1}{m(m+1)}
=
\frac{H_m-1}{m}
-
\frac{H_{m+1}-1}{m+1}
+
\frac1{(m+1)^2}
\tag{13}
\]
telescopes to
\[
\sum_{j=2}^n
\frac{H_{j-1}-1}{j(j-1)}
=
H_n^{(2)}-1-\frac{H_n-1}{n}.
\tag{14}
\]
Summing (1) and applying (14) proves (4).

The indicators \(A_j\) are independent with
\[
\Pr(A_j=1)=\frac1{j-1},
\]
so
\[
\operatorname{Var}(R_n)
=
\sum_{j=2}^n
\frac1{j-1}
\left(1-\frac1{j-1}\right)
=
H_{n-1}-H_{n-1}^{(2)},
\]
which proves (5).

Finally, the classical total-path-length theorem states that
\[
W_n
=
\frac{T_n-\mathbb ET_n}{n}
\]
converges in \(L^2\) to a nondegenerate limit \(W\) with
\[
\operatorname{Var}(W)=2-\frac{\pi^2}{6}.
\tag{15}
\]
Thus
\[
\frac{\operatorname{Var}(T_n)}{n^2}
\longrightarrow
2-\frac{\pi^2}{6}.
\]
Since
\[
H_n^{(2)}\longrightarrow\frac{\pi^2}{6}
\]
and
\[
H_n\sim\log n,
\]
equations (4), (5), and (15) give (6)--(7).

## Verification

The accompanying checker exhaustively enumerates every recursive tree through order \(9\) using all parent-choice sequences.

It verifies the exact local covariance (1) for every arrival index, the conditional mean gap (11), and strict first-order stochastic ordering of the two conditional total-path-length laws.

It also verifies the global covariance (4), the exact root-degree variance (5), the mean total path length, and the telescoping harmonic identity over a larger exact-rational grid.

Finite enumeration is supplementary. The universal theorem is proved by the parent-edge coupling, subtree-growth expectation, and harmonic summation above.

## Relationship to prior work

Dobrow and Fill study total path length for the uniform random recursive tree in detail. Their full treatment states the independent-parent growth construction, the exact mean total path length, and the \(L^2\) normalized limit used in (15). It does not introduce root degree as a joint statistic or state a covariance with root attachments.

Bergeron, Flajolet, and Salvy develop a unified generating-function theory for increasing trees. In their Section 5, path length and root degree are treated in separate subsections; for recursive trees they recover the classical harmonic mean root degree. The inspected sections do not give a mixed root-degree/path-length generating function or covariance.

A later study of power-weight recursive trees gives exact martingale-innovation identities for total path length and recovers the classical uniform variance coefficient. Its inspected full text does not state root degree, root-attachment covariance, or the stochastic comparison (2). That paper was first posted after the temporal anchor used for the present archive direction and is used only as supporting literature.

The closest previously checked result on the same tree model concerns root degree versus the number of leaves. Its covariance is positive and arises from leaf survival. The present path-length result is distinct: every nontrivial root attachment has a negative effect on total search cost, with an explicit arrival-time profile and a monotone-transform consequence.

## Limitations

The exact coupling uses uniform attachment. In preferential or label-weighted recursive trees, conditioning an arrival not to attach to the root changes the alternative-parent law and generally changes the formulas.

Equation (3) is a covariance consequence of coordinatewise root-attachment comparisons. It does not assert negative association of the full vector of tree statistics.

The dynamic argument is elementary once the correct coupling is identified. Older increasing-tree or recursive-tree literature may contain the same mixed first moment under a bivariate generating-function encoding; this remains the principal originality risk.

## References

1. R. P. Dobrow and J. A. Fill, “Total Path Length for Random Recursive Trees,” *Combinatorics, Probability and Computing* 8 (1999), 317–333, DOI 10.1017/S0963548399003855.
2. F. Bergeron, P. Flajolet, and B. Salvy, “Varieties of Increasing Trees,” in *CAAP '92*, Lecture Notes in Computer Science 581 (1992), 24–48, DOI 10.1007/3-540-55251-0_2.
3. G. O. Munsonius, “On Tail Bounds for Random Recursive Trees,” *Journal of Applied Probability* 49 (2012), 566–581, arXiv:1106.3865, DOI 10.1239/jap/1339878805.
4. M. Gałązka and H. Wdowicka, “Total Path Length in Power-Weight Recursive Trees: Martingale Limits and Global Fluctuations,” arXiv:2610.00614, first submitted 2026-09-30.
