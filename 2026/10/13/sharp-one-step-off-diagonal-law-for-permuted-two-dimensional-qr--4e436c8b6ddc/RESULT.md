# Sharp one-step off-diagonal law for permuted two-dimensional QR iteration

## Finding
Let
\[
A=
\begin{pmatrix}
a&b\\
b&d
\end{pmatrix}
=A^{\mathsf T}>0,
\qquad
b\ne0.
\]
Perform one unshifted QR step,
\[
A=QR,
\qquad
A^+=RQ=Q^{\mathsf T}AQ,
\]
with positive diagonal entries in \(R\).

Then
\[
\boxed{
b^+
=
b\,\frac{\det A}{a^2+b^2},
}
\]
so
\[
\frac{|b^+|}{|b|}
=
\frac{\det A}{\|Ae_1\|_2^2}.
\]
If the two coordinates are symmetrically permuted before the QR step, the corresponding factor is
\[
\frac{\det A}{\|Ae_2\|_2^2}.
\]

Therefore the exact best one-step permutation is to put the larger-norm column first. For a \(2\times2\) SPD matrix this is equivalently the larger diagonal entry first.

If
\[
\kappa=\kappa_2(A)>1,
\]
then the best permutation satisfies the sharp uniform bound
\[
\boxed{
\min\left\{
\frac{\det A}{\|Ae_1\|_2^2},
\frac{\det A}{\|Ae_2\|_2^2}
\right\}
\le
\frac{2\kappa}{\kappa^2+1}
<1.
}
\]
Equality occurs when the two column norms are equal. Hence this permutation rule makes every non-diagonal \(2\times2\) SPD unshifted QR step strictly off-diagonal contractive.

The unpermuted step can behave very differently. If the first coordinate is nearly the eigenvector of the smaller eigenvalue, the one-step off-diagonal amplification approaches
\[
\kappa.
\]
More precisely, for
\[
A=
R_\theta
\begin{pmatrix}
\mu&0\\
0&L
\end{pmatrix}
R_\theta^{\mathsf T},
\qquad
\kappa=L/\mu,
\]
where the first coordinate has squared weight \(\sin^2\theta\) on the \(L\)-eigendirection,
\[
\frac{|b^+|}{|b|}
=
\frac{\mu L}
{\mu^2\cos^2\theta+L^2\sin^2\theta},
\]
and the off-diagonal grows exactly when
\[
\sin^2\theta<\frac1{\kappa+1}.
\]

Thus a fixed-order QR step can transiently enlarge the off-diagonal by almost the full condition number, whereas the better of the two coordinate permutations contracts it by at least the sharp factor
\[
\frac{2\kappa}{\kappa^2+1}.
\]

## Assumptions and scope
The theorem concerns exact arithmetic, one unshifted QR step, real symmetric positive-definite \(2\times2\) matrices, and the magnitude of the single off-diagonal entry. Since the Frobenius norm of the off-diagonal part is
\[
\sqrt2\,|b|,
\]
the same amplification factors apply to that norm.

The QR factorization is normalized so that the diagonal of \(R\) is positive. This is the convention used in the permutation analysis of symmetric QR.

The permutation is a symmetric coordinate permutation. It may be viewed either as running the QR step on the permuted matrix or as permuting back afterward; the off-diagonal magnitude is unchanged by the final symmetric swap.

No claim is made for shifted QR, for matrices of dimension three or larger, for nonsymmetric matrices, or for global iteration counts.

## Proof
Because \(A\) is SPD,
\[
a>0,
\qquad
\det A=ad-b^2>0.
\]
Put
\[
r=\sqrt{a^2+b^2}.
\]
The positive-diagonal QR factorization has
\[
Q=
\frac1r
\begin{pmatrix}
a&-b\\
b&a
\end{pmatrix}.
\]
Indeed, its first column is the normalized first column of \(A\), and the second diagonal entry of \(R=Q^{\mathsf T}A\) is
\[
\frac{\det A}{r}>0.
\]

The new off-diagonal entry is
\[
b^+
=
e_1^{\mathsf T}Q^{\mathsf T}AQe_2.
\]
Now
\[
Qe_2
=
\frac1r
\begin{pmatrix}
-b\\
a
\end{pmatrix},
\]
and
\[
A
\begin{pmatrix}
-b\\
a
\end{pmatrix}
=
\begin{pmatrix}
0\\
ad-b^2
\end{pmatrix}.
\]
Therefore
\[
b^+
=
\frac1{r^2}
\begin{pmatrix}
a&b
\end{pmatrix}
\begin{pmatrix}
0\\
\det A
\end{pmatrix}
=
b\,\frac{\det A}{a^2+b^2}.
\]

After swapping the coordinates, the same argument replaces
\[
a^2+b^2
\]
by
\[
d^2+b^2.
\]
Hence the best ordering puts first the column with larger Euclidean norm. Since \(a,d>0\),
\[
a^2+b^2\ge d^2+b^2
\iff
a\ge d,
\]
so column ordering and descending diagonal ordering coincide in dimension two.

Let the eigenvalues be
\[
0<\mu<L.
\]
The two squared column norms satisfy
\[
\|Ae_1\|_2^2+\|Ae_2\|_2^2
=
\operatorname{tr}(A^2)
=
\mu^2+L^2.
\]
Thus
\[
\max_i\|Ae_i\|_2^2
\ge
\frac{\mu^2+L^2}{2}.
\]
Because
\[
\det A=\mu L,
\]
the best-permutation factor obeys
\[
\min(\gamma_1,\gamma_2)
=
\frac{\mu L}
{\max_i\|Ae_i\|_2^2}
\le
\frac{2\mu L}{\mu^2+L^2}
=
\frac{2\kappa}{\kappa^2+1}.
\]
For \(\kappa>1\), this is strictly below one.

Equality requires equal column norms. It is attained by rotating the eigenbasis by \(45^\circ\), for which
\[
A=
\frac12
\begin{pmatrix}
\mu+L&L-\mu\\
L-\mu&\mu+L
\end{pmatrix}.
\]

For the fixed-order law, write
\[
A=
R_\theta
\begin{pmatrix}
\mu&0\\
0&L
\end{pmatrix}
R_\theta^{\mathsf T}
\]
so that
\[
\|Ae_1\|_2^2
=
\mu^2\cos^2\theta
+
L^2\sin^2\theta.
\]
Hence
\[
\gamma_1
=
\frac{\mu L}
{\mu^2\cos^2\theta+L^2\sin^2\theta}.
\]
The inequality
\[
\gamma_1>1
\]
is equivalent to
\[
\mu^2+(L^2-\mu^2)\sin^2\theta<\mu L,
\]
and therefore to
\[
\sin^2\theta
<
\frac{\mu}{L+\mu}
=
\frac1{\kappa+1}.
\]
As
\[
\theta\to0
\]
through nonzero angles, \(b\ne0\) and
\[
\gamma_1\to\frac L\mu=\kappa.
\]
This proves the fixed-order supremum.

For the rational condition-four witness,
\[
A=
\frac1{169}
\begin{pmatrix}
244&180\\
180&601
\end{pmatrix}
\]
is the rotation of
\[
\operatorname{diag}(1,4)
\]
with cosine \(12/13\) and sine \(5/13\). Its displayed-order denominator is
\[
\|Ae_1\|_2^2=\frac{544}{169},
\]
so
\[
\gamma_1=\frac4{544/169}=\frac{169}{136}>1.
\]
After swapping,
\[
\|Ae_2\|_2^2=\frac{2329}{169},
\]
hence
\[
\gamma_2=\frac{676}{2329}<1.
\]

## Verification
The embedded `verify.py` checks the exact QR-step formula for several rational SPD matrices by constructing the orthogonal factor symbolically up to squared normalization. It verifies the condition-four transient witness, the swapped contraction, and the equality case
\[
A=
\frac12
\begin{pmatrix}
5&3\\
3&5
\end{pmatrix},
\]
where both permutations give
\[
\frac{|b^+|}{|b|}=\frac8{17}.
\]

The all-matrix statements are analytic. Finite checks are corroborative only.

## Relationship to prior work
The QR algorithm is a classical eigenvalue method. Watkins gives a modern account of the QR algorithm and places the subject under primary MSC \(65F15\).

Krishnamoorthy studies symmetric QR with permutations and proposes two low-cost permutation heuristics. One orders diagonal entries by decreasing magnitude; the other orders the diagonal of
\[
A^2,
\]
equivalently the column norms of \(A\), in decreasing order. The paper reports improved convergence in simulations and motivates permutations through instantaneous convergence.

The result here gives an exact two-dimensional theorem for that idea. For \(2\times2\) SPD matrices, diagonal ordering and column ordering coincide, they are exactly optimal among the two coordinate permutations for reducing the next off-diagonal magnitude, and their sharp condition-number contraction factor is
\[
\frac{2\kappa}{\kappa^2+1}.
\]
The same calculation also quantifies the transient that permutation prevents: a fixed ordering can amplify the off-diagonal by a factor arbitrarily close to
\[
\kappa.
\]

Targeted searches using symmetric QR, column ordering, permutation, off-diagonal growth, one-step contraction, and the exact condition-number factor did not locate this sharp \(2\times2\) law.

## Limitations
The theorem is one-step and two-dimensional. In higher dimensions, column ordering need not minimize any single global off-diagonal norm after a QR step.

The statement concerns unshifted QR. Practical symmetric eigensolvers use tridiagonal reduction, shifts, and deflation.

The off-diagonal norm is a natural diagonalization diagnostic, but the theorem does not directly optimize the diagonal eigenvalue-estimation error used in the permutation paper.

Older QR literature is extensive, and the displayed \(2\times2\) identity may have appeared as an exercise or local calculation under different terminology. This is the principal originality risk.

## References
1. D. S. Watkins, “The QR Algorithm Revisited,” SIAM Review 50 (2008), 133–145. DOI 10.1137/060659454.
2. A. Krishnamoorthy, “Symmetric QR Algorithm with Permutations,” arXiv:1402.5086v1, submitted 2014-02-20.
