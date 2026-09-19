# Invariant-subspace defect identity for sum-normal tuples

## Result

Let \({\bf T}=(T_1,\ldots,T_d)\) be a commuting \(d\)-tuple on a complex Hilbert space \(\mathcal H\), and put
\[
D_{\bf T}:=\sum_{j=1}^d [T_j^*,T_j].
\]
Let \(\mathcal M\subseteq\mathcal H\) be a closed joint invariant subspace.  Relative to
\(\mathcal H=\mathcal M\oplus\mathcal M^\perp\), write
\[
T_j=\begin{pmatrix}A_j&X_j\\0&B_j\end{pmatrix},
\qquad A_j=T_j|_{\mathcal M}.
\]
Then
\[
\boxed{\;
D_{\bf A}
=
P_{\mathcal M}D_{\bf T}|_{\mathcal M}
+\sum_{j=1}^d X_jX_j^* .
\;}
\tag{1}
\]

Consequently:

1. If \({\bf T}\) is sum-hyponormal, then \({\bf T}|_{\mathcal M}\) is sum-hyponormal.
2. If \({\bf T}\) is sum-normal, then
   \[
   \boxed{D_{\bf A}=\sum_{j=1}^dX_jX_j^*.}
   \tag{2}
   \]
   Hence
   \[
   \boxed{\;
   {\bf T}|_{\mathcal M}\text{ is sum-normal}
   \iff
   \mathcal M\text{ reduces every }T_j.
   \;}
   \tag{3}
   \]
3. In particular, every finite-dimensional invariant subspace of a sum-normal tuple is reducing.

This gives the exact invariant-subspace boundary missing from Remark 1.2(b) of Chavan--Reza--Sequeira, *Sum of self-commutators of commuting operators*, arXiv:2609.19287v1.  That remark states that sum-normality passes to every invariant restriction.  Formula (2) shows that the assertion is false unless the invariant subspace is already reducing.

## Proof

For each \(j\),
\[
T_j^*T_j
=
\begin{pmatrix}
A_j^*A_j&A_j^*X_j\\
X_j^*A_j&X_j^*X_j+B_j^*B_j
\end{pmatrix},
\]
whereas
\[
T_jT_j^*
=
\begin{pmatrix}
A_jA_j^*+X_jX_j^*&X_jB_j^*\\
B_jX_j^*&B_jB_j^*
\end{pmatrix}.
\]
Therefore the \(\mathcal M\)-compression of the self-commutator is
\[
P_{\mathcal M}[T_j^*,T_j]|_{\mathcal M}
=
[A_j^*,A_j]-X_jX_j^*.
\]
Summing over \(j\) gives (1).

If \(D_{\bf T}\ge0\), then its compression is positive, and (1) is a sum of two positive operators.  Thus \(D_{\bf A}\ge0\), proving inheritance of sum-hyponormality.

If \(D_{\bf T}=0\), equation (1) becomes (2).  Hence \(D_{\bf A}=0\) precisely when
\(\sum_jX_jX_j^*=0\).  Since every summand is positive, this holds precisely when
\(X_j=0\) for every \(j\).  In the displayed block form, \(X_j=0\) is exactly the condition that \(\mathcal M^\perp\) is \(T_j\)-invariant; together with the assumed invariance of \(\mathcal M\), this says that \(\mathcal M\) reduces the tuple.  This proves (3).

Finally suppose \(\dim\mathcal M<\infty\) and \({\bf T}\) is sum-normal.  By (2),
\(D_{\bf A}\ge0\).  On the finite-dimensional space \(\mathcal M\),
\[
\operatorname{tr}D_{\bf A}
=
\sum_j\operatorname{tr}(A_j^*A_j-A_jA_j^*)=0.
\]
A positive finite-dimensional operator of trace zero is zero, so \(D_{\bf A}=0\).  Equation (3) now implies that \(\mathcal M\) reduces \({\bf T}\).

## Explicit counterexample to blanket sum-normal inheritance

Let
\[
\mathcal H=L^2(\mathbb T),\qquad Uf(z)=zf(z),
\]
so \(U\) is unitary and therefore normal.  Let \(\mathcal M=H^2(\mathbb T)\), which is \(U\)-invariant but not reducing.  The restriction \(U|_{\mathcal M}\) is the unilateral shift \(S\), and
\[
[S^*,S]=I-SS^*=P_{\mathbf 1}\ne0.
\]
Thus \(U\) is sum-normal (the case \(d=1\)), while its invariant restriction is merely hyponormal, not normal.

For every \(d\ge1\), the commuting tuple
\[
{\bf T}=(U,0,\ldots,0)
\]
is sum-normal, whereas
\[
{\bf T}|_{\mathcal M}=(S,0,\ldots,0)
\]
has
\[
D_{{\bf T}|_{\mathcal M}}=P_{\mathbf 1}\ne0.
\]
Hence the failure occurs in every tuple length, not only in a multivariable edge case.

## Consequence for arXiv:2609.19287v1

Remark 1.2(b) of arXiv:2609.19287v1 correctly states inheritance for sum-hyponormal tuples, but its parenthetical claim for sum-normal tuples is false.  The paper's own later block computation, equation (3.3), is consistent with (2): for a sum-normal tuple it obtains
\[
[A^*,A]=\sum_jX_jX_j^*.
\]
Remark 3.1 is likewise consistent with (3), since it observes that a sum-hyponormal tuple whose invariant restriction is sum-normal must reduce that subspace.

Remark 3.4, however, invokes Remark 1.2(b) to treat each invariant restriction \({\bf T}|_{\mathcal M_{j+1}}\) as sum-normal before applying Theorem 2.1 along a triangularizing chain of compact operators.  That step is not justified in general.  The auxiliary argument in Remark 3.4 therefore does not establish its claimed special case as written.

This does **not** by itself invalidate Theorem 2.2 or the paper's main decomposition theorem: Theorem 2.2 has a separate proof using joint eigenspaces and compact Taylor-spectrum structure.  The correction is confined to invariant-subspace inheritance and the argument in Remark 3.4 that depends on it.

## Context and originality

For a single normal operator it is classical that an invariant subspace need not be reducing; the bilateral-shift/Hardy-space example above is standard.  Likewise, the block-matrix computation behind (1) is elementary and is not claimed as a new general operator-theoretic technique.

The contribution claimed here is narrower: the exact defect identity (1) is used to locate and repair the sum-normal inheritance assertion in the newly posted arXiv:2609.19287v1, to identify the precise iff boundary (3), to give a counterexample valid for every \(d\), and to isolate the downstream argument that is affected while leaving the independently proved main theorem untouched.

To the best of our knowledge, no public correction of this specific v1 assertion was located at publication time.

## Limitations

The result does not address the paper's open question whether every sum-normal commuting tuple is normal, nor the existence of nonzero compact quasinilpotent sum-normal tuples.  It does not challenge Theorems 2.1--2.4.  It only corrects the blanket invariant-subspace inheritance statement and the auxiliary argument that uses it.

## References

1. S. Chavan, M. R. Reza, S. S. Sequeira, *Sum of self-commutators of commuting operators*, arXiv:2609.19287v1 (2026). https://arxiv.org/abs/2609.19287
2. For background on the classical distinction between invariant and reducing subspaces of normal operators, see the standard bilateral-shift example; a modern discussion of normal operators with nonnormal invariant restrictions appears in: *Reducing subspaces for rank-one perturbations of normal operators*, Proc. Roy. Soc. Edinburgh Sect. A (2022). https://doi.org/10.1017/prm.2021.68
