# Sharp Euclidean residual-safety frontier for spectrally equivalent preconditioned Richardson

## Finding
Consider
\[
A=A^{\mathsf T}\succ0,
\qquad
B=B^{\mathsf T}\succ0,
\]
and the unit-step preconditioned Richardson correction
\[
x^+=x+B(b-Ax).
\]
Let
\[
C=A^{1/2}BA^{1/2}
\]
satisfy
\[
(1-\delta)I\preceq C\preceq(1+\delta)I,
\qquad
0\le\delta<1.
\]
For the Euclidean residual
\[
r=b-Ax,
\]
the exact worst one-step amplification over all such SPD pairs with
\[
\kappa_2(A)=\kappa
\]
is
\[
\boxed{\delta\sqrt{\kappa}}.
\]

Hence spectral equivalence alone guarantees Euclidean residual nonexpansion precisely when
\[
\boxed{\delta\sqrt{\kappa}\le1.}
\]
If the symmetric preconditioned spectral interval is expressed through
\[
\kappa_p=\frac{1+\delta}{1-\delta},
\]
the same frontier becomes
\[
\boxed{
\kappa_p\le
\frac{\sqrt{\kappa}+1}{\sqrt{\kappa}-1}
}
\]
for \(\kappa>1\).

The result separates two notions of convergence that are often conflated. The iteration is always contractive by at most \(\delta\) in the natural residual norm induced by \(A^{-1}\), while its ordinary Euclidean residual can increase whenever
\[
\delta>\frac1{\sqrt{\kappa}}.
\]

A minimal exact witness is obtained with
\[
\kappa=9,
\qquad
\delta=\frac12,
\]
\[
A=
\begin{pmatrix}
9&0\\
0&1
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
1/9&-1/6\\
-1/6&1
\end{pmatrix}.
\]
The symmetrically preconditioned matrix
\[
C=A^{1/2}BA^{1/2}
=
\begin{pmatrix}
1&-1/2\\
-1/2&1
\end{pmatrix}
\]
has eigenvalues \(1/2\) and \(3/2\), so its condition number is only \(3\). Nevertheless,
\[
I-AB=
\begin{pmatrix}
0&3/2\\
1/6&0
\end{pmatrix},
\]
whose Euclidean operator norm is \(3/2\). Thus some residual grows by fifty percent in one step while the spectral radius of the residual iteration is only \(1/2\).

## Assumptions and scope
The theorem is in exact arithmetic. Both the system matrix and the preconditioner are real symmetric positive definite.

The update uses a unit Richardson parameter. A scalar relaxation can be absorbed into \(B\), so the theorem applies after such a rescaling whenever the symmetrically preconditioned spectrum is enclosed in
\[
[1-\delta,1+\delta].
\]

The Euclidean residual norm is deliberately distinguished from the natural energy metric. No floating-point residual-gap claim is made.

The result is not a statement about Krylov acceleration. It concerns one stationary preconditioned Richardson correction and therefore also the local algebra of any iterative-refinement step whose correction operator is represented by the fixed SPD map \(B\).

## Proof
Since
\[
r=b-Ax,
\]
the update gives
\[
r^+
=
b-A(x+Br)
=
(I-AB)r.
\]
Because
\[
AB=A^{1/2}CA^{-1/2},
\]
we have
\[
I-AB
=
A^{1/2}(I-C)A^{-1/2}.
\]
Therefore
\[
\|I-AB\|_2
\le
\|A^{1/2}\|_2
\|I-C\|_2
\|A^{-1/2}\|_2.
\]
The spectral enclosure of \(C\) gives
\[
\|I-C\|_2\le\delta,
\]
and
\[
\|A^{1/2}\|_2\|A^{-1/2}\|_2
=
\sqrt{\kappa_2(A)}.
\]
Hence
\[
\|r^+\|_2
\le
\delta\sqrt{\kappa}\,\|r\|_2.
\]

To prove sharpness, take
\[
A=
\begin{pmatrix}
\kappa&0\\
0&1
\end{pmatrix},
\qquad
D=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\]
and set
\[
C=I-\delta D.
\]
The eigenvalues of \(D\) are \(-1\) and \(1\), so \(C\) has eigenvalues
\[
1-\delta,
\qquad
1+\delta.
\]
Thus \(C\succ0\). Define
\[
B=A^{-1/2}CA^{-1/2}.
\]
Then \(B\succ0\) and
\[
I-AB
=
A^{1/2}(I-C)A^{-1/2}
=
\delta
\begin{pmatrix}
0&\sqrt{\kappa}\\
1/\sqrt{\kappa}&0
\end{pmatrix}.
\]
The two singular values of the displayed matrix are
\[
\delta\sqrt{\kappa}
\quad\text{and}\quad
\frac{\delta}{\sqrt{\kappa}},
\]
so the upper bound is attained exactly.

For the natural metric, put
\[
z=A^{-1/2}r.
\]
Then
\[
A^{-1/2}r^+
=
(I-C)z,
\]
hence
\[
\|r^+\|_{A^{-1}}
\le
\delta\|r\|_{A^{-1}}.
\]
Thus the Euclidean spike is entirely a similarity-geometry effect.

Finally,
\[
\delta=\frac{\kappa_p-1}{\kappa_p+1}.
\]
Substitution into
\[
\delta\sqrt{\kappa}\le1
\]
and elementary rearrangement yield
\[
\kappa_p\le
\frac{\sqrt{\kappa}+1}{\sqrt{\kappa}-1}.
\]
In dimension one,
\[
|r^+|\le\delta|r|,
\]
so dimension two is minimal for a Euclidean residual increase under \(\delta<1\).

## Verification
The embedded `verify.py` checks the rational equality witness
\[
A=\operatorname{diag}(9,1),
\qquad
\delta=\frac12,
\qquad
B=
\begin{pmatrix}
1/9&-1/6\\
-1/6&1
\end{pmatrix}.
\]
It verifies positive definiteness of \(A\) and \(B\), verifies that the symmetrically preconditioned matrix has characteristic polynomial corresponding to eigenvalues \(1/2\) and \(3/2\), and verifies
\[
I-AB=
\begin{pmatrix}
0&3/2\\
1/6&0
\end{pmatrix}.
\]
It also checks directly that applying this matrix to the second coordinate vector amplifies the Euclidean norm by exactly \(3/2\).

The all-dimensional upper bound is analytic and is not inferred from finite testing.

## Relationship to prior work
Preconditioned Richardson iteration and spectral-equivalence reasoning are classical. Kressner, Steinlechner, and Vandereycken explicitly place preconditioned Richardson in the SPD setting, emphasize preconditioning as a way to address poor conditioning, and formulate the SPD problem through the energy norm. Their public preprint lists primary MSC \(65F10\).

Bialecki analyzes preconditioned Richardson methods using spectral-equivalence constants for SPD discretizations. That work supplies classical convergence context but does not, in the accessible record, identify a sharp Euclidean residual-amplification frontier.

The additional statement here is metric-specific: even when the symmetrically preconditioned spectrum lies tightly in
\[
[1-\delta,1+\delta],
\]
the ordinary residual norm can grow by the exact sharp factor
\[
\delta\sqrt{\kappa_2(A)}.
\]
Targeted searches under spectral equivalence, preconditioned Richardson, Euclidean residual monotonicity, and residual amplification did not locate this exact two-condition-number frontier.

## Limitations
The theorem controls a single stationary correction. It does not analyze varying preconditioners, Krylov acceleration, or flexible methods.

The preconditioner is assumed SPD. Nonsymmetric or indefinite preconditioners can have substantially more complicated transient behavior.

The factor depends on the condition number of the original matrix because the Euclidean residual metric is not invariant under the symmetrizing similarity transform. A differently scaled residual metric can remove this amplification.

No claim is made about finite-precision residual gaps or backward stability.

## References
1. D. Kressner, M. Steinlechner, and B. Vandereycken, “Preconditioned low-rank Riemannian optimization for linear systems with tensor product structure,” arXiv:1508.02988v1, submitted 2015-08-12; SIAM Journal on Scientific Computing 38 (2016), A2018–A2044. DOI 10.1137/15M1032909.
2. B. Bialecki, “Preconditioned Richardson and Minimal Residual Iterative Methods for Piecewise Hermite Bicubic Orthogonal Spline Collocation Equations,” SIAM Journal on Scientific Computing 15 (1994), 668–680. DOI 10.1137/0915043.
