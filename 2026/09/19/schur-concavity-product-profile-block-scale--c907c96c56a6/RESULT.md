# Schur concavity and the exact block-count envelope for the product-profile scale

## Result

Let \(q\ge d\ge2\), let \(b_1,\dots,b_q>0\), and put
\[
n=\sum_{i=1}^q b_i.
\]
For a block-size vector \(b=(b_1,\dots,b_q)\), define
\[
W_d(b)
=
\sum_{\substack{I\subseteq[q]\\ |I|=d-1}}
\left(\prod_{i\in I}b_i\right)^{1/2}
\left(n-\sum_{i\in I}b_i\right)^{1/2}.
\]
This is exactly the block scale \(w_d(\mathcal B)\) introduced by Abakumov--Friedland--Yomdin when \(b_i=|B_i|\).

### Theorem 1: strict Schur concavity and refinement monotonicity

On every simplex \(\{b_i>0:\sum b_i=n\}\), \(W_d\) is strictly Schur-concave: if \(b\) majorizes \(c\) (so \(b\) is at least as unequal as \(c\)) and \(b\) is not a permutation of \(c\), then
\[
W_d(b)<W_d(c).
\]
Moreover, splitting any block \(b_i=x+y\) into two positive blocks \(x,y\) strictly increases the scale.

Consequently, for integers
\[
n\ge q\ge d\ge2,
\]
the largest value of \(w_d(\mathcal B)\) among all partitions of \(n\) coordinates into between \(d\) and \(q\) nonempty blocks is attained uniquely, up to permutation of the blocks, by the most balanced \(q\)-block partition.

Write
\[
n=qm+s,\qquad 0\le s<q.
\]
Thus the maximizing block sizes are \(m+1\) repeated \(s\) times and \(m\) repeated \(q-s\) times. If
\[
a_-=\max\{0,d-1-(q-s)\},\qquad
a_+=\min\{d-1,s\},
\]
the exact integer envelope is
\[
\boxed{
\mathcal W_{d,q}(n)
=
\sum_{a=a_-}^{a_+}
\binom{s}{a}\binom{q-s}{d-1-a}
(m+1)^{a/2}m^{(d-1-a)/2}
\sqrt{(q-d+1)m+s-a}.
}
\]

When \(q\mid n\), this reduces to
\[
\boxed{
\mathcal W_{d,q}(n)
=
\binom q{d-1}\sqrt{q-d+1}
\left(\frac nq\right)^{d/2}.
}
\]

### Theorem 2: elementary-symmetric compression and global stability

Let \(e_d(b)\) be the \(d\)-th elementary symmetric polynomial in \(b_1,\dots,b_q\). Then
\[
\boxed{
W_d(b)^2
\le
d\binom q{d-1}e_d(b).
}
\]
Hence
\[
\boxed{
W_d(b)
\le
M_{d,q}(n):=
\binom q{d-1}\sqrt{q-d+1}
\left(\frac nq\right)^{d/2}.
}
\]
The constant in this continuous envelope is exact: equality is attained by equal block sizes. For integer block sizes it is attained whenever \(q\mid n\), so the coefficient cannot be reduced in a bound uniform in \(n\).

There is also a global quantitative rigidity estimate. Put
\[
V(b)=\sum_{i=1}^q\left(b_i-\frac nq\right)^2,
\qquad
\Delta(b)=\frac{q}{q-1}\frac{V(b)}{n^2}.
\]
Then
\[
\boxed{
W_d(b)
\le
M_{d,q}(n)\bigl(1-\Delta(b)\bigr)^{d/4}.
}
\]
In particular, if
\[
W_d(b)\ge(1-\varepsilon)M_{d,q}(n),
\]
then
\[
\boxed{
\frac{V(b)}{n^2}
\le
\frac{q-1}{q}
\left[1-(1-\varepsilon)^{4/d}\right].
}
\]
Thus near-maximal product-profile scale forces quantitative balance of the block sizes.

## Proof

### 1. Pairwise balancing

Fix all coordinates except two, denoted \(x,y>0\), and keep their sum
\[
x+y=S
\]
fixed. Group the terms in \(W_d\) according to whether the indexing set \(I\) contains neither, both, or exactly one of \(x,y\).

Terms containing neither variable depend on \(x,y\) only through \(S\), so they are unchanged.

Terms containing both variables have a factor \(\sqrt{xy}\), hence increase when \(xy\) increases.

For the terms containing exactly one of \(x,y\), fix a \((d-2)\)-subset \(J\) of the remaining coordinates. Let
\[
P_J=\prod_{j\in J}b_j,\qquad
R_J=\sum_{\substack{\ell\notin J\\ \ell\ne x,y}}b_\ell.
\]
The paired contribution is
\[
\sqrt{P_J}
\left[
\sqrt{x(R_J+y)}
+
\sqrt{y(R_J+x)}
\right].
\]
Set \(T=xy\). The square of the bracket equals
\[
R_JS+2T+2\sqrt{T(R_J^2+R_JS+T)},
\]
which is strictly increasing in \(T>0\). At fixed \(S\), every transfer of mass from the larger of \(x,y\) to the smaller increases \(xy\) until equality is reached. Since \(q\ge d\), at least one such paired term exists. Therefore every nontrivial Robin-Hood transfer strictly increases \(W_d\), proving strict Schur concavity.

### 2. Splitting a block

Suppose one block of size \(b=x+y\) is replaced by two positive blocks \(x,y\). Terms whose indexing set avoids the split block are unchanged. For each old term containing \(b\), the corresponding new pair has, after removing the common factor \(\sqrt{P_J}\),
\[
\sqrt{x(R_J+y)}+\sqrt{y(R_J+x)}
>
\sqrt{(x+y)R_J}.
\]
When \(d\ge3\), there are additionally positive new terms whose indexing sets contain both \(x\) and \(y\). Thus every genuine split strictly increases \(W_d\).

For an integer partition with fewer than \(q\) blocks, a block can be split until there are exactly \(q\) blocks. Once there are \(q\) blocks, if two sizes differ by at least \(2\), the integer transfer
\[
(x,y)\mapsto(x-1,y+1)
\]
toward equality strictly increases \(W_d\). Iterating yields exactly the balanced multiset
\[
\{m+1,\dots,m+1,m,\dots,m\}.
\]
Grouping the \((d-1)\)-subsets according to the number \(a\) of size-\(m+1\) blocks they contain gives the displayed formula for \(\mathcal W_{d,q}(n)\).

### 3. Elementary-symmetric compression

For
\[
A_I=
\left(\prod_{i\in I}b_i\right)^{1/2}
\left(n-\sum_{i\in I}b_i\right)^{1/2},
\qquad |I|=d-1,
\]
Cauchy--Schwarz gives
\[
W_d(b)^2
\le
\binom q{d-1}\sum_{|I|=d-1}A_I^2.
\]
But
\[
\begin{aligned}
\sum_{|I|=d-1}A_I^2
&=
\sum_{|I|=d-1}
\left(\prod_{i\in I}b_i\right)
\sum_{j\notin I}b_j\\
&=
d\,e_d(b),
\end{aligned}
\]
because each \(d\)-fold product is counted once for each of its \(d\) omitted coordinates. This proves
\[
W_d(b)^2\le d\binom q{d-1}e_d(b).
\]

Maclaurin's inequality gives
\[
e_d(b)
\le
\binom qd\left(\frac nq\right)^d.
\]
Using
\[
d\binom qd=(q-d+1)\binom q{d-1}
\]
yields
\[
W_d(b)\le
\binom q{d-1}\sqrt{q-d+1}
\left(\frac nq\right)^{d/2}.
\]
Equal blocks make both inequalities equalities.

### 4. Quantitative stability

For \(d\ge2\), Maclaurin monotonicity between the second and \(d\)-th elementary symmetric means gives
\[
\frac{e_d(b)}{\binom qd}
\le
\left(
\frac{e_2(b)}{\binom q2}
\right)^{d/2}.
\]
Since
\[
e_2(b)
=
\frac12\left(n^2-\sum_i b_i^2\right)
\]
and
\[
\sum_i b_i^2=\frac{n^2}{q}+V(b),
\]
we have
\[
\frac{e_2(b)}
{\binom q2(n/q)^2}
=
1-\frac{q}{q-1}\frac{V(b)}{n^2}
=
1-\Delta(b).
\]
Combining this with the elementary-symmetric compression proves
\[
W_d(b)\le M_{d,q}(n)(1-\Delta(b))^{d/4}.
\]
The near-equality consequence follows by rearranging this inequality.

## Consequences for product-profile anti-concentration

Abakumov--Friedland--Yomdin prove that if \(P:[0,1]^n\to\mathbb R\) is a nonconstant multi-affine polynomial of exact degree \(d\), all variables are active, and \(\mathcal B\) is an admissible partition, then
\[
\mathcal Q_P(\rho)
\le
\Phi_d\!\left(
C_d w_d(\mathcal B)\frac{\rho}{\operatorname{osc}(P)}
\right),
\]
with analogous density and quotient-Remez bounds using the same structural scale.

Therefore, if \(P\) has an admissible partition into at most \(q\) blocks, \(d\le q\le n\), their theorem immediately sharpens to the exact integer-envelope form
\[
\boxed{
\mathcal Q_P(\rho)
\le
\Phi_d\!\left(
C_d\mathcal W_{d,q}(n)
\frac{\rho}{\operatorname{osc}(P)}
\right).
}
\]
Likewise,
\[
\boxed{
\|f_P\|_{L^p(\mathbb R)}
\le
C_dp^{d-1}
\left(
\frac{\mathcal W_{d,q}(n)}
{\operatorname{osc}(P)}
\right)^{1-1/p},
\qquad 1<p<\infty,
}
\]
and the same substitution improves the block-count version of the quotient-Remez estimate.

If only a simple closed form is desired, one may replace \(\mathcal W_{d,q}(n)\) by
\[
M_{d,q}(n)
=
\binom q{d-1}\sqrt{q-d+1}(n/q)^{d/2}.
\]
For fixed \(d\) and large \(q\),
\[
M_{d,q}(n)
\sim
\frac{1}{(d-1)!}\,
q^{(d-1)/2}n^{d/2},
\]
so this identifies the exact leading coefficient of the source paper's \(q^{(d-1)/2}n^{d/2}\) reduction at the level of the structural invariant \(w_d\).

## Comparison with prior work

The source paper explicitly evaluates \(w_d\) on equal blocks and proves the coarse implication
\[
w_d(\mathcal B)\lesssim_d q^{(d-1)/2}n^{d/2}
\]
from
\[
w_d(\mathcal B)\le\sqrt n\left(\sum_{B\in\mathcal B}\sqrt{|B|}\right)^{d-1}.
\]
It also explicitly states that no optimality is asserted for \(w_d(\mathcal B)\) when the number of blocks exceeds \(d\), nor for the complete dependence on the number of blocks. The equal-block evaluation itself is therefore not claimed here.

The new points are the majorization theorem for the newly introduced scale, strict increase under refinement, the exact integer extremum for every \((n,q,d)\), the elementary-symmetric compression, and the global variance stability estimate. Targeted searches for the source identifier and for combinations of product-profile anti-concentration, block balancing, majorization, Schur concavity, and elementary-symmetric optimization did not locate an equivalent statement.

## Limitations

The theorem determines the extremal behavior of the structural scale \(w_d\), and consequently the best block-count compression obtainable by substituting a bound for \(w_d\) into the source paper's theorems. It does **not** prove that the actual concentration function for classes with more than \(d\) blocks requires the same \(q\)-dependence. In particular, it does not resolve the source paper's broader open question of the optimal dimensional exponent for arbitrary multi-affine polynomials.

The case \(d=1\) is trivial: \(W_1(b)=\sqrt n\) independently of the partition, so strict Schur concavity is false there.

Originality is asserted only to the best of our knowledge. The source preprint is very recent, so unindexed contemporaneous observations are a residual risk. No independent validation or formal proof-assistant verification is asserted.

## References

1. E. Abakumov, O. Friedland, Y. Yomdin, *Product-profile anti-concentration for block-structured multi-affine polynomials*, arXiv:2609.19473 (2026), https://arxiv.org/abs/2609.19473.
2. The proof uses the classical Cauchy--Schwarz and Maclaurin inequalities for elementary symmetric means.
