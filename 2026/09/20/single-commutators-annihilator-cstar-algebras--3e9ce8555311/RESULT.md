# Single commutators in annihilator C*-algebras

## Result

Let
\[
A=\left(\bigoplus_{\alpha\in I}K(H_\alpha)\right)_{c_0}
\]
be a complex annihilator C*-algebra, and let
\[
F=\{\alpha\in I:\dim H_\alpha<\infty\}.
\]
For \(\alpha\in F\), write \(\operatorname{tr}_\alpha\) for the normalized matrix
trace on \(K(H_\alpha)=M_{\dim H_\alpha}(\mathbb C)\). Define
\[
\tau_F:A\longrightarrow c_0(F),\qquad
\tau_F(x)=\bigl(\operatorname{tr}_\alpha(x_\alpha)\bigr)_{\alpha\in F}.
\]

Then the set of **single additive commutators**
\[
\mathcal C_1(A):=\{[a,b]=ab-ba:a,b\in A\}
\]
satisfies
\[
\boxed{\mathcal C_1(A)=\ker\tau_F.}
\]

Consequently:

1. \(\mathcal C_1(A)\), although defined nonlinearly, is a norm-closed linear
   subspace of \(A\).
2. The quotient map induced by \(\tau_F\) is an isometric isomorphism
   \[
   \boxed{A/\mathcal C_1(A)\cong c_0(F).}
   \]
3. For every \(x\in A\),
   \[
   \boxed{
   \operatorname{dist}(x,\mathcal C_1(A))
   =
   \sup_{\alpha\in F}
   |\operatorname{tr}_\alpha(x_\alpha)|.
   }
   \]
4. There is a universal constant \(C>0\) such that every
   \(x\in\mathcal C_1(A)\) admits
   \[
   x=[a,b],\qquad
   \max\{\|a\|,\|b\|\}\le C\|x\|^{1/2}.
   \]
   More strongly, the factors can be chosen coordinatewise so that
   \[
   \|a_\alpha\|,\|b_\alpha\|
   \le C\|x_\alpha\|^{1/2}
   \quad(\alpha\in I).
   \]
5. Every element of \(A\) is a single commutator if and only if \(A\) has no
   nonzero finite-dimensional elementary summand.

The bounded tracial functionals on \(A\) are exactly
\[
x\longmapsto
\sum_{\alpha\in F}c_\alpha\operatorname{tr}_\alpha(x_\alpha),
\qquad
(c_\alpha)\in\ell_1(F),
\]
with equality of norms. Hence
\[
\boxed{
\mathcal C_1(A)
=
\bigcap_{\varphi\ \mathrm{bounded\ trace}}\ker\varphi
=
\overline{\operatorname{span}}\{[a,b]:a,b\in A\}.
}
\]
Thus, for annihilator C*-algebras, the usual closed commutator subspace has
**commutator width one**.

## Why the uniform estimates matter

The standard structure theorem identifies annihilator (dual, or compact in
Kaplansky's sense) C*-algebras with \(c_0\)-direct sums of elementary
C*-algebras \(K(H_\alpha)\). Coordinatewise existence of commutator
factorizations is not by itself enough to give a commutator in the \(c_0\)-sum:
the norms of the factors could grow with the dimensions of the blocks.

Two recent dimension-free results remove exactly this obstruction.

- Shen--Wang--Zhi prove that every trace-zero matrix \(X\in M_n(\mathbb C)\)
  has \(X=[B,C]\) with
  \[
  \|B\|\,\|C\|\le K\|X\|
  \]
  for an absolute \(K\), independent of \(n\).
- Liu proves that every compact operator \(T\) on a separable
  infinite-dimensional complex Hilbert space is \(T=[B,C]\) with compact
  \(B,C\) and
  \[
  \max\{\|B\|,\|C\|\}\le c\|T\|^{1/2}
  \]
  for a universal \(c\).

The dimension independence is what allows the blockwise factorizations to
remain in the \(c_0\)-sum.

## Proof

### 1. The trace map

For every finite-dimensional block,
\[
|\operatorname{tr}_\alpha(x_\alpha)|\le\|x_\alpha\|.
\]
Since \(\|x_\alpha\|\to0\) in the \(c_0\)-sense,
\(\tau_F(x)\in c_0(F)\) and
\[
\|\tau_F(x)\|_\infty\le\|x\|.
\]
Thus \(\tau_F\) is contractive.

Every single commutator belongs to its kernel, because on a finite-dimensional
block
\[
\operatorname{tr}_\alpha([a_\alpha,b_\alpha])=0.
\]
Therefore
\[
\mathcal C_1(A)\subseteq\ker\tau_F.
\]

### 2. Infinite-dimensional blocks without separability assumptions

Liu's theorem is stated for separable infinite-dimensional Hilbert spaces.
It nevertheless gives the same universal estimate for a compact operator on
an arbitrary infinite-dimensional Hilbert space.

Indeed, let \(T\in K(H)\) with \(H\) arbitrary, and put
\[
M=\overline{\operatorname{ran}T+\operatorname{ran}T^*}.
\]
The space \(M\) is separable and reduces \(T\). If \(M\) is
infinite-dimensional, apply Liu's theorem to \(T|_M\) and extend the two
compact factors by zero on \(M^\perp\).

If \(M\) is finite-dimensional, choose an infinite-dimensional separable
closed subspace \(L\subseteq M^\perp\). Then
\[
N=M\oplus L
\]
is separable, infinite-dimensional, and reduces \(T\), with
\(T|_N=T|_M\oplus0_L\). Apply Liu's theorem on \(N\), and again extend the
factors by zero. Hence every compact \(T\) on every infinite-dimensional
complex Hilbert space has a compact commutator factorization with Liu's
same universal norm estimate.

### 3. Uniform factorizations on finite blocks

For a finite-dimensional block \(M_n(\mathbb C)\), trace zero is necessary
for being a commutator. It is also sufficient. The recent
Shen--Wang--Zhi estimate gives
\[
X=[B,C],\qquad \|B\|\,\|C\|\le K\|X\|.
\]
If \(X\ne0\), reciprocal rescaling
\[
(B,C)\mapsto(tB,t^{-1}C)
\]
with the appropriate \(t>0\) gives
\[
\max\{\|B\|,\|C\|\}\le \sqrt{K}\,\|X\|^{1/2}.
\]
For \(X=0\), take both factors zero.

Combining this with the infinite-dimensional result, there is an absolute
constant
\[
C=\max\{c,\sqrt K\}
\]
such that every allowed coordinate \(x_\alpha\) has
\[
x_\alpha=[a_\alpha,b_\alpha],
\qquad
\|a_\alpha\|,\|b_\alpha\|
\le C\|x_\alpha\|^{1/2}.
\]

### 4. Gluing the coordinates

Take \(x\in\ker\tau_F\). On every finite block \(x_\alpha\) has normalized
trace zero, while on every infinite-dimensional block there is no trace
condition. Choose the factorizations from the preceding step.

Since \(x\in A\),
\[
\|x_\alpha\|\to0
\]
in the \(c_0\)-sense. Therefore
\[
\|a_\alpha\|,\|b_\alpha\|
\le C\|x_\alpha\|^{1/2}\to0.
\]
Hence
\[
a=(a_\alpha),\qquad b=(b_\alpha)
\]
both lie in \(A\), and coordinatewise
\[
[a,b]=x.
\]
Thus
\[
\ker\tau_F\subseteq\mathcal C_1(A),
\]
which proves
\[
\mathcal C_1(A)=\ker\tau_F.
\]

The same estimate also gives
\[
\max\{\|a\|,\|b\|\}\le C\|x\|^{1/2}.
\]

### 5. Exact distance and quotient

For \(\lambda=(\lambda_\alpha)_{\alpha\in F}\in c_0(F)\), define
\(s(\lambda)\in A\) by
\[
s(\lambda)_\alpha=
\begin{cases}
\lambda_\alpha I_{H_\alpha},&\alpha\in F,\\
0,&\alpha\notin F.
\end{cases}
\]
Then
\[
\|s(\lambda)\|=\|\lambda\|_\infty,
\qquad
\tau_Fs(\lambda)=\lambda.
\]
So \(\tau_F\) has an isometric right inverse and is a quotient map of norm
one.

For arbitrary \(x\in A\), contractivity gives
\[
\operatorname{dist}(x,\ker\tau_F)\ge\|\tau_F(x)\|_\infty.
\]
On the other hand,
\[
x-s(\tau_F(x))\in\ker\tau_F
\]
and
\[
\|s(\tau_F(x))\|=\|\tau_F(x)\|_\infty.
\]
Hence
\[
\operatorname{dist}(x,\mathcal C_1(A))
=
\|\tau_F(x)\|_\infty.
\]
The isometric quotient identification follows.

### 6. All bounded traces

Let \(\varphi\) be a bounded tracial linear functional on \(A\).
Its restriction to a finite-dimensional simple block \(M_n(\mathbb C)\) is
a scalar multiple of the normalized trace.

Its restriction to an infinite-dimensional \(K(H)\) is zero. To see this,
take mutually orthogonal equivalent rank-one projections
\(p_1,\ldots,p_N\). Traciality gives the same value \(\lambda\) on each, while
\[
\left\|\sum_{j=1}^N p_j\right\|=1.
\]
Thus
\[
N|\lambda|
=
\left|\varphi\left(\sum_{j=1}^N p_j\right)\right|
\le\|\varphi\|,
\]
for every \(N\), so \(\lambda=0\). The functional vanishes on finite-rank
operators and hence, by density, on \(K(H)\).

Since the Banach dual of a \(c_0\)-sum is the corresponding \(\ell_1\)-sum,
the bounded traces are precisely the \(\ell_1(F)\)-linear combinations of
the normalized traces, with the stated norm equality. Their common kernel
is \(\ker\tau_F=\mathcal C_1(A)\).

Because every commutator lies in this common kernel and every element of
the common kernel is itself one commutator, the closed linear commutator
subspace coincides with the single-commutator set.

## Context and comparison

Liu's 2026 theorem resolves the Pearcy--Topping problem for
\(K(H)\) when \(H\) is separable infinite-dimensional, and supplies the
uniform square-root norm bound needed above. Earlier work on compact
operator commutators studied many important subclasses and commutator
ideals but did not have the general existence theorem now available.

The finite-dimensional obstruction is qualitatively different: in
\(M_n(\mathbb C)\), a commutator must have trace zero. The
dimension-independent estimate of Shen--Wang--Zhi is essential when matrix
sizes are unbounded across a \(c_0\)-sum.

The theorem above therefore identifies the exact global obstruction in every
annihilator C*-algebra: it is neither compactness, separability, nor growth
of matrix sizes, but only the normalized traces carried by the
finite-dimensional elementary summands.

## Limitations

- The result is restricted to annihilator C*-algebras, equivalently
  \(c_0\)-sums of elementary C*-algebras. It does not classify single
  commutators in arbitrary C*-algebras.
- No optimal value of the universal factor constant \(C\) is claimed.
- The theorem uses the recent uniform matrix and compact-operator
  commutator bounds as inputs; it does not reprove those results.
- The exact single-commutator classification was not located in the
  literature checked, but older operator-ideal or dual-C*-algebra literature
  may contain equivalent special cases. The originality claim is therefore
  to the best of our knowledge.

## References

1. Zhichao Liu, *Every compact operator is a commutator of compact
   operators*, arXiv:2609.20672v1 (2026).
   https://arxiv.org/abs/2609.20672
2. Hao Shen, Jiaqi Wang, Lihong Zhi, *A Dimension-Independent Commutator
   Bound*, arXiv:2609.09938 (2026).
   https://arxiv.org/abs/2609.09938
3. Alexei Yu. Pirkovskii, Yurii V. Selivanov, *Structure theory of
   homologically trivial and annihilator locally C*-algebras*,
   arXiv:1006.3934 (2010). The C*-case records the standard direct-sum
   structure of annihilator/dual C*-algebras.
   https://arxiv.org/abs/1006.3934
4. Daniel Beltiţă, Sasmita Patnaik, Gary Weiss, *B(H)-Commutators: A
   Historical Survey II and recent advances on commutators of compact
   operators*, arXiv:1303.4844 (2013).
   https://arxiv.org/abs/1303.4844
