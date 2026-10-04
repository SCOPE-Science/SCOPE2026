# Exact negative regression between endpoint degree and distance in a uniform Cayley tree

## Finding

Let \(T_n\) be uniform over the \(n^{n-2}\) labeled trees on \([n]\), with \(n\ge2\). Fix distinct vertices \(u,v\), and write
\[
D=d_{T_n}(u,v),
\qquad
\Delta=\deg_{T_n}(u).
\]

For \(1\le k\le n-1\),
\[
\boxed{
\Pr(D=k)
=
\frac{(k+1)(n-2)_{k-1}}{n^k},
}
\tag{1}
\]
where
\[
(x)_r=x(x-1)\cdots(x-r+1).
\]

For \(1\le k\le n-2\),
\[
\boxed{
\Delta-1\mid(D=k)
\overset d=
\operatorname{Bin}\!\left(n-k-2,\frac1n\right)
+
\operatorname{Bernoulli}\!\left(\frac1{k+1}\right),
}
\tag{2}
\]
with the two summands independent. At \(k=n-1\),
\[
\boxed{\Delta=1\quad\text{almost surely}.}
\tag{3}
\]

Equivalently,
\[
\boxed{
\mathbb E[z^{\Delta-1}\mid D=k]
=
\left(1+\frac{z-1}{n}\right)^{n-k-2}
\left(1+\frac{z-1}{k+1}\right)
}
\tag{4}
\]
for \(1\le k\le n-2\).

The conditional distributions are strictly ordered:
\[
\boxed{
\Delta\mid(D=k+1)
<_{\mathrm{st}}
\Delta\mid(D=k),
\qquad
1\le k\le n-2.
}
\tag{5}
\]

Consequently, for every pair of nondecreasing real functions \(f,h\) on the respective supports,
\[
\boxed{
\operatorname{Cov}(f(D),h(\Delta))\le0.
}
\tag{6}
\]
If \(n\ge3\) and both functions are strictly increasing on their realized supports, the inequality is strict.

The conditional mean is
\[
\boxed{
\mathbb E[\Delta\mid D=k]
=
2-\frac{k+2}{n}+\frac1{k+1},
\qquad
1\le k\le n-1.
}
\tag{7}
\]
In particular,
\[
\boxed{
\operatorname{Cov}(D,\Delta)
=
1-\frac1n\mathbb E[D(D+1)]
<0
\qquad(n\ge3).
}
\tag{8}
\]

Finally,
\[
\frac{D}{\sqrt n}\Longrightarrow R,
\qquad
\Pr(R\in dx)=x e^{-x^2/2}\,dx,
\tag{9}
\]
and
\[
\boxed{
\operatorname{Cov}(D,\Delta)\longrightarrow-1,
}
\tag{10}
\]
while
\[
\boxed{
\operatorname{Corr}(D,\Delta)
\sim
-\sqrt{\frac{2}{4-\pi}}\,n^{-1/2}.
}
\tag{11}
\]

Thus a larger marked-vertex separation forces the endpoint degree downward in the strong stochastic-regression sense, even though the ordinary correlation vanishes because distance fluctuates on the \(\sqrt n\) scale while degree remains tight.

## Assumptions and scope

The tree is uniform over all labeled trees on a fixed vertex set. The two marked vertices are fixed and distinct.

The stochastic ordering in (5) is first-order stochastic order.

The covariance inequality (6) follows from one-sided stochastic regression of \(\Delta\) on \(D\). No reverse conditional stochastic-monotonicity statement is claimed.

The asymptotic statements concern fixed marked vertices; exchangeability gives the same law for two uniformly sampled distinct labels.

## Proof

Fix \(k\), and first fix an ordered list of \(k-1\) distinct intermediate vertices
\[
w_1,\ldots,w_{k-1}.
\]
Let \(P\) be the path
\[
u-w_1-\cdots-w_{k-1}-v.
\]

The classical forest-extension formula says that if a forest on \([n]\) has component sizes
\[
s_1,\ldots,s_c,
\]
then the number of labeled trees containing that forest is
\[
n^{c-2}\prod_{\ell=1}^c s_\ell.
\tag{12}
\]

For the fixed path \(P\), there is one component of size \(k+1\) and \(n-k-1\) singleton components. Hence the number of trees containing \(P\) is
\[
(k+1)n^{n-k-2}.
\tag{13}
\]
A tree has a unique \(u\)-to-\(v\) path. Multiplying (13) by the number
\[
(n-2)_{k-1}
\]
of ordered intermediate lists and dividing by Cayley's count \(n^{n-2}\) proves (1).

Now condition on this fixed path. Let
\[
Y=\Delta-1
\]
be the number of neighbors of \(u\) outside the path, and put
\[
N=n-k-1.
\]
For any fixed \(r\)-subset \(S\) of these \(N\) outside vertices, require the additional edges
\[
\{u,x\},
\qquad x\in S.
\]
The prescribed forest now has one component of size \(k+1+r\) and \(N-r\) singleton components. Applying (12) again gives
\[
\Pr\!\left(S\subseteq N_T(u)\mid P\subseteq T\right)
=
\frac{k+1+r}{k+1}\,n^{-r}.
\tag{14}
\]

Using
\[
z^Y=(1+(z-1))^Y
\]
and summing (14) over subsets,
\[
\begin{aligned}
\mathbb E[z^Y\mid P\subseteq T]
&=
\sum_{r=0}^{N}
\binom Nr
(z-1)^r
\frac{k+1+r}{k+1}n^{-r}\\
&=
\left(1+\frac{z-1}{n}\right)^{N-1}
\left(1+\frac{z-1}{k+1}\right).
\end{aligned}
\tag{15}
\]
The result is independent of the intermediate labels, so conditioning only on \(D=k\) gives the same law. Since \(N-1=n-k-2\), this proves (2) and (4). When \(k=n-1\), there is no outside vertex, proving (3).

For \(k\le n-3\), couple
\[
B_k\sim\operatorname{Bin}\!\left(n-k-2,\frac1n\right)
\]
as
\[
B_k=B_{k+1}+E,
\qquad
E\sim\operatorname{Bernoulli}(1/n),
\]
with independence. Under a common uniform random variable,
\[
\operatorname{Bernoulli}\!\left(\frac1{k+2}\right)
\le
\operatorname{Bernoulli}\!\left(\frac1{k+1}\right)
\]
almost surely. At least one inequality is strict with positive probability, and the terminal step follows from (3). This proves (5).

If \(h\) is nondecreasing, then
\[
m_h(k)=\mathbb E[h(\Delta)\mid D=k]
\]
is nonincreasing. Thus
\[
\operatorname{Cov}(f(D),h(\Delta))
=
\operatorname{Cov}(f(D),m_h(D)).
\]
For an independent copy \(D'\),
\[
2\operatorname{Cov}(f(D),m_h(D))
=
\mathbb E[
(f(D)-f(D'))
(m_h(D)-m_h(D'))
]
\le0,
\]
which proves (6), including the stated strictness.

Taking expectations in (2) gives (7). A uniform Cayley-tree degree has the Prüfer-code law
\[
\Delta
\overset d=
1+\operatorname{Bin}\!\left(n-2,\frac1n\right),
\]
so
\[
\mathbb E\Delta=2-\frac2n.
\tag{16}
\]
Averaging (7) and comparing with (16) gives
\[
\mathbb E\frac1{D+1}
=
\frac{\mathbb ED}{n}.
\tag{17}
\]
Using (7),
\[
\operatorname{Cov}(D,\Delta)
=
\operatorname{Cov}
\left(
D,
-\frac Dn+\frac1{D+1}
\right).
\]
Since
\[
\mathbb E\frac{D}{D+1}
=
1-\mathbb E\frac1{D+1},
\]
equation (17) simplifies the expression to (8). Strict negativity also follows from (5).

Equation (1) can be rewritten as
\[
\Pr(D=k)
=
\frac{k+1}{n}
\prod_{j=2}^{k}
\left(1-\frac jn\right).
\tag{18}
\]
For \(k=x\sqrt n+o(\sqrt n)\), the logarithm of the product tends to
\[
-\frac{x^2}{2}.
\]
Moreover,
\[
\prod_{j=2}^{k}
\left(1-\frac jn\right)
\le
\exp\!\left(
-\frac{k(k+1)-2}{2n}
\right),
\]
which gives uniform integrability for the first two scaled moments. Hence
\[
\frac{\mathbb ED}{\sqrt n}\to\sqrt{\frac\pi2},
\qquad
\frac{\mathbb ED^2}{n}\to2.
\tag{19}
\]
Substitution in (8) proves (10).

The Prüfer law gives
\[
\operatorname{Var}(\Delta)
=
\frac{(n-2)(n-1)}{n^2}
\to1,
\tag{20}
\]
while (19) gives
\[
\frac{\operatorname{Var}(D)}n
\to
2-\frac\pi2
=
\frac{4-\pi}{2}.
\tag{21}
\]
Equations (10), (20), and (21) yield (11).

## Verification

The accompanying checker exhaustively enumerates every Prüfer code through \(n=8\). For fixed marked vertices it reconstructs the distance-degree joint law and verifies (1)--(4) exactly.

It independently checks the strict stochastic ordering of every successive conditional degree law through \(n=80\), the conditional mean formula, and the exact covariance identity (8).

Finite replay is supplementary. The all-\(n\) theorem follows from the forest-extension count and analytic coupling argument above.

## Relationship to prior work

Pitman's treatment of coalescent random forests gives a modern proof of the classical forest-extension formula: a forest with component sizes \(s_1,\ldots,s_c\) is contained in exactly
\[
n^{c-2}\prod_i s_i
\]
labeled trees. This is the counting engine used here, but the inspected source does not state the endpoint-degree law conditional on a marked-vertex distance.

Aldous studies uniform spanning trees and uniform labeled trees by random-walk methods and lists degree distribution and diameter among the properties analyzed. These are classical marginals, but the inspected source does not give the finite joint law in (2).

Berzunza Ojeda and Janson study distance profiles of rooted and unrooted simply generated trees. Their open text also treats conditioning on root degree, but the inspected statements do not specialize to an exact finite Cayley-tree law for endpoint degree conditional on the distance to another fixed vertex.

Targeted searches for conditional degree given distance, degree-distance covariance, negative regression, and stochastic monotonicity did not locate (2), (5), or (8).

## Limitations

The theorem is specific to the uniform labeled-tree model. Conditioning on a path in a nonuniform random-tree model generally changes the attachment law.

The stochastic regression is proved from distance to endpoint degree. No symmetric reverse-regression statement is claimed.

The forest-extension formula is classical and is not part of the originality claim. Older work on labeled trees may contain an equivalent bivariate degree-distance generating function under different notation; this is the principal originality risk.

## References

1. J. Pitman, “Coalescent Random Forests,” Berkeley Statistics Technical Report 457, first publicly dated 1996-09-01; later *Journal of Combinatorial Theory, Series A* 85 (1999), 165–193.
2. D. J. Aldous, “The Random Walk Construction of Uniform Spanning Trees and Uniform Labelled Trees,” *SIAM Journal on Discrete Mathematics* 3 (1990), 450–465, DOI 10.1137/0403039.
3. G. Berzunza Ojeda and S. Janson, “The distance profile of rooted and unrooted simply generated trees,” *Combinatorics, Probability and Computing* 31 (2022), 368–410, DOI 10.1017/S0963548321000304.
