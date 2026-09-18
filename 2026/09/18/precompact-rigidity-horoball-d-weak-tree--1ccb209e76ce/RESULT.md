# Precompact rigidity and horoball limit sets for metric-functional weak convergence

## Result

Let \((X,d)\) be a metric space with base point \(o\). For \(w\in X\), write
\[
h_w(x)=d(x,w)-d(o,w),
\]
let \(X^\diamondsuit\) be the pointwise closure of the internal functionals \(h_w\), and let
\(\sigma(X,X^\diamondsuit)\) be the topology introduced by Gutiérrez--Nevanlinna: a net
\(x_i\) converges to \(x\) precisely when
\[
\liminf_i h(x_i)\ge h(x)\qquad(h\in X^\diamondsuit).
\]

Two complementary facts hold.

### Theorem A: precompact rigidity

For every totally bounded subset \(A\subset X\), the subspace topology induced by
\(\sigma(X,X^\diamondsuit)\) on \(A\) is exactly the metric topology.

More quantitatively, fix \(x\in A\) and \(r>0\), and put
\[
A_r=\{y\in A:d(x,y)\ge r\}.
\]
If \(w_1,\ldots,w_N\) is an \(r/4\)-net of \(A_r\), then
\[
A\cap B_\sigma\!\left(x,\{h_{w_1},\ldots,h_{w_N}\},r/2\right)
\subset A\cap B_d(x,r),
\]
where
\[
B_\sigma(x,F,c)=\bigcap_{h\in F}\{y:h(y)>h(x)-c\}.
\]
Thus one may take at most the \(r/4\)-covering number of \(A\) many internal metric
functionals to certify a metric \(r\)-neighborhood inside \(A\).

Consequently:

1. on every compact metric space, \(\sigma(X,X^\diamondsuit)\) is the metric topology;
2. if a d-weakly convergent net has totally bounded range together with its limit, then
   it converges metrically;
3. in every proper metric space, every bounded d-weakly convergent net converges
   metrically.

Hence, in a proper space, any genuine weakening of metric convergence must escape to
infinity.

### Theorem B: exact horoball multi-limit sets in a proper CAT(0) tree

Let \(\mathcal T\) be the metric realization of the rooted full binary tree with unit
edge lengths, and let \(o\) be its root. This is a proper complete \(\mathbb R\)-tree,
hence a CAT(0) space. Let
\[
\xi=000\cdots
\]
be the distinguished end and \(b_\xi\) its Busemann functional normalized at \(o\).

For every real number \(C\), there is an unbounded sequence \((y_n)\) in \(\mathcal T\)
whose set of d-weak limits is exactly the closed horoball
\[
\Lambda_d(y_n)
=
H_C(\xi):=\{x\in\mathcal T:b_\xi(x)\le C\}.
\]

In particular, there is an unbounded sequence \((z_n)\) that converges d-weakly, and
therefore in \(\sigma(\mathcal T,\mathcal T^\diamondsuit)\), to **every point of
\(\mathcal T\)**. Thus the metric-functional weak topology can be maximally
non-Hausdorff even on a proper, complete, uniquely geodesic CAT(0) space.

The source paper already gives an every-point limit sequence on the snowflaked real
line and earlier work gives every-point examples on nonconvex subspaces. The new point
here is that the same extreme nonuniqueness occurs in a proper CAT(0) geodesic space,
together with an exact realization of every Busemann horoball as a d-weak limit set.
Theorem A identifies the sharp mechanism: boundedness rules the pathology out in every
proper metric space.

## Proof of Theorem A

The source paper proves that \(\sigma(X,X^\diamondsuit)\) is coarser than the metric
topology, so only the reverse inclusion on \(A\) needs proof.

Fix \(x\in A\) and \(r>0\). If \(A_r=\varnothing\), then
\(A\subset B_d(x,r)\) and there is nothing to prove. Otherwise total boundedness gives
a finite \(r/4\)-net \(w_1,\ldots,w_N\in A_r\).

For any \(z\in A_r\), choose \(w_i\) with \(d(z,w_i)<r/4\). Since
\(d(x,w_i)\ge r\),
\[
\begin{aligned}
h_{w_i}(z)-h_{w_i}(x)
&=d(z,w_i)-d(x,w_i)\\
&<\frac r4-r
=-\frac{3r}{4}
<-\frac r2.
\end{aligned}
\]
Hence \(z\notin B_\sigma(x,\{h_{w_1},\ldots,h_{w_N}\},r/2)\). Therefore
\[
A\cap B_\sigma(x,\{h_{w_1},\ldots,h_{w_N}\},r/2)
\subset A\setminus A_r
=A\cap B_d(x,r).
\]
Metric neighborhoods in \(A\) therefore contain relative
\(\sigma(X,X^\diamondsuit)\)-neighborhoods, proving equality of the two subspace
topologies.

If a d-weakly convergent net lies in a totally bounded set \(A\) together with its
limit, its convergence is convergence in the relative \(\sigma\)-topology and hence in
the relative metric topology. In a proper space, a bounded net and its limit lie in a
compact closed ball, which is totally bounded. This proves the corollaries.

## Metric functionals of the binary \(\mathbb R\)-tree

For \(x,w\in\mathcal T\), let \((x|w)_o\) be the length of the common initial segment
of the geodesics \([o,x]\) and \([o,w]\). Tree geometry gives
\[
h_w(x)=d(o,x)-2(x|w)_o.
\]
For an end \(\eta\in\partial\mathcal T\), define
\[
b_\eta(x)=d(o,x)-2(x|\eta)_o.
\]

We claim
\[
\mathcal T^\diamondsuit
=
\{h_w:w\in\mathcal T\}\cup\{b_\eta:\eta\in\partial\mathcal T\}.
\]

Every \(b_\eta\) is the pointwise limit of \(h_{\eta(t)}\) along the ray to \(\eta\),
so the right side is contained in \(\mathcal T^\diamondsuit\).

Conversely, let \(h\) be a pointwise limit of internals \(h_{w_i}\). If a cofinal
subnet of \(w_i\) remains in a bounded ball, properness gives a further subnet
converging to some \(w\), hence \(h=h_w\). Otherwise pass to a subnet with
\(d(o,w_i)\to\infty\). Extend each segment \([o,w_i]\) to an end \(\eta_i\).
The end space of the locally finite binary tree is the compact Cantor space, so a
subnet of \(\eta_i\) converges to an end \(\eta\). For each fixed \(x\), convergence of
the initial finite edge pattern and \(d(o,w_i)\to\infty\) imply
\[
(x|w_i)_o\longrightarrow(x|\eta)_o.
\]
Therefore \(h_{w_i}(x)\to b_\eta(x)\), and \(h=b_\eta\). This proves the
classification.

## Proof of Theorem B

Fix \(C\in\mathbb R\). For each sufficiently large integer \(n\), let
\[
\eta_n=0^{n-1}1\,000\cdots
\]
and choose \(y_n\) on the ray \(\eta_n\) at radial distance
\[
L_n=2(n-1)+C
\]
from the root. For large \(n\), \(L_n>n\), so \(y_n\) lies beyond the branch point
where \(\eta_n\) leaves \(\xi\).

Because \((y_n|\xi)_o=n-1\),
\[
b_\xi(y_n)=L_n-2(n-1)=C
\]
for every sufficiently large \(n\).

Now fix any other end \(\eta\ne\xi\), and let \(j\) be the position of its first \(1\).
For \(n>j\),
\[
(y_n|\eta)_o=j-1,
\]
hence
\[
b_\eta(y_n)=L_n-2(j-1)\longrightarrow+\infty.
\]
For a fixed internal \(h_w\), with \(s=d(o,w)\),
\[
h_w(y_n)
=
L_n-2(y_n|w)_o
\ge L_n-2s
\longrightarrow+\infty.
\]

By the classification above, all metric functionals except \(b_\xi\) tend to
\(+\infty\), while \(b_\xi(y_n)=C\). Therefore a point \(a\in\mathcal T\) is a d-weak
limit of \((y_n)\) exactly when
\[
C=\liminf_n b_\xi(y_n)\ge b_\xi(a),
\]
which is precisely \(a\in H_C(\xi)\). This proves the exact horoball formula.

For the universal-limit sequence, keep the same rays \(\eta_n\) but choose \(z_n\) at
radial distance \(3n\). Then
\[
b_\xi(z_n)=3n-2(n-1)=n+2\to+\infty.
\]
The same estimates show that every other Busemann functional and every internal
functional also tends to \(+\infty\). Hence for every \(a\in\mathcal T\) and every
\(h\in\mathcal T^\diamondsuit\),
\[
\liminf_n h(z_n)=+\infty\ge h(a).
\]
Thus \(z_n\) converges d-weakly to every point of \(\mathcal T\).

## Relation to previous results

Gutiérrez--Nevanlinna introduced d-weak convergence in 2025/2026 and proved that in a
\(W\)-convex metric space the set of d-weak limits of a sequence is closed and
\(W\)-convex. Their September 2026 paper constructs the topology
\(\sigma(X,X^\diamondsuit)\), proves that its net convergence is exactly d-weak
convergence, and records a non-Hausdorff example on
\((\mathbb R,\sqrt{|x-y|})\) in which \(n\) converges to every point.

The present horoballs are compatible with the earlier convexity theorem, but give an
exact realization result in a proper CAT(0) space. Existing CAT(0) weak-topology
literature, including Lytchak--Petrunin, studies the projection/\(\Delta\)-weak notion
for bounded sequences and is a different convergence theory.

## Limitations

- The tree calculation uses the explicit horofunction boundary of the locally finite
  binary \(\mathbb R\)-tree; no claim is made that arbitrary proper CAT(0) spaces admit
  universal d-weak limit sequences.
- Theorem A says that total boundedness collapses this particular metric-functional
  weak topology to the metric topology. It does not identify the topology on arbitrary
  bounded subsets of non-proper spaces, which need not be totally bounded.
- The exact horoball realization concerns the Gutiérrez--Nevanlinna d-weak topology,
  not the established projection/\(\Delta\)-weak topology on CAT(0) spaces.
- The motivating topology paper is very recent, so unindexed parallel work remains a
  residual originality risk.

## References

1. A. W. Gutiérrez and O. Nevanlinna, *A Weak Topology on Metric Spaces*,
   arXiv:2609.19368 (submitted 16 September 2026).
2. A. W. Gutiérrez and O. Nevanlinna, *Metric functionals and weak convergence*,
   Z. Anal. Anwend. (2026), DOI: 10.4171/ZAA/1828; arXiv:2506.04154.
3. A. Lytchak and A. Petrunin, *Weak topology on CAT(0) spaces*,
   Israel J. Math. 255 (2023), 763--781, DOI: 10.1007/s11856-022-2420-5.
4. A. Karlsson, *Hahn--Banach for metric functionals and horofunctions*,
   J. Funct. Anal. 281 (2021), 109030, DOI: 10.1016/j.jfa.2021.109030.
