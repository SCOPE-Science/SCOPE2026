# A sharp two-dimensional residual-safety radius and a three-dimensional nilpotent spike for Newton–Schulz inversion

## Finding
For the Newton–Schulz inverse iteration
\[
X_{k+1}=X_k(2I-AX_k),
\]
define the right residual
\[
E_k=I-AX_k.
\]
The residual obeys the exact squaring law
\[
E_{k+1}=E_k^2.
\]

This simple recurrence hides a sharp low-dimensional distinction.

For every
\[
0\le r<1,
\]
all complex \(2\times2\) residuals with
\[
\rho(E_0)\le r
\]
satisfy
\[
\|E_1\|_{\mathrm F}\le\|E_0\|_{\mathrm F}
\]
if and only if
\[
\boxed{r\le\frac12}.
\]
Thus one half is the exact spectral-radius safety ceiling for universal first-step Frobenius residual monotonicity in dimension two.

Dimension three is qualitatively different. For every prescribed amplification
\[
G>0,
\]
there is a nilpotent \(3\times3\) initial residual with
\[
\rho(E_0)=0
\]
whose first Newton–Schulz residual is larger by a factor exceeding \(G\), yet whose second residual is exactly zero.

Take
\[
E_0=
\begin{pmatrix}
0&M&0\\
0&0&M\\
0&0&0
\end{pmatrix}.
\]
Then
\[
E_1=E_0^2=
\begin{pmatrix}
0&0&M^2\\
0&0&0\\
0&0&0
\end{pmatrix},
\qquad
E_2=0,
\]
and
\[
\frac{\|E_1\|_{\mathrm F}}{\|E_0\|_{\mathrm F}}
=
\frac{M}{\sqrt2}.
\]
The spectral-norm ratio is even simpler:
\[
\frac{\|E_1\|_2}{\|E_0\|_2}=M.
\]

Choosing
\[
A=I_3,
\qquad
X_0=I_3-E_0,
\]
realizes this as an actual Newton–Schulz inverse iteration for a target matrix of condition number one. Hence the transient is caused entirely by nonnormality of the initial residual, not by conditioning of the matrix being inverted.

## Assumptions and scope
The theorem is in exact arithmetic and concerns the right residual
\[
E_k=I-AX_k
\]
of the classical Newton–Schulz inverse iteration.

The two-dimensional universal statement uses Frobenius norm. The three-dimensional nilpotent family gives unbounded amplification in both Frobenius and spectral norm.

The spectral-radius condition
\[
\rho(E_0)<1
\]
is an asymptotic convergence condition. The result does not contradict the standard stronger initialization condition
\[
\|E_0\|<1,
\]
because a submultiplicative norm below one immediately gives
\[
\|E_{k+1}\|
\le
\|E_k\|^2
<
\|E_k\|.
\]

No floating-point stability claim is made. The exact two-step termination of the nilpotent example can be perturbed by roundoff.

## Proof
First,
\[
AX_{k+1}
=
AX_k(2I-AX_k).
\]
Since
\[
AX_k=I-E_k,
\]
one obtains
\[
AX_{k+1}
=
(I-E_k)(I+E_k)
=
I-E_k^2.
\]
Therefore
\[
E_{k+1}=E_k^2
\]
and inductively
\[
E_k=E_0^{\,2^k}.
\]

Now let
\[
E\in\mathbb C^{2\times2},
\qquad
\rho(E)\le r.
\]
By unitary Schur decomposition,
\[
E=UTU^*,
\qquad
T=
\begin{pmatrix}
a&z\\
0&b
\end{pmatrix},
\]
where
\[
|a|\le r,
\qquad
|b|\le r.
\]
Frobenius norm is unitarily invariant, and
\[
T^2=
\begin{pmatrix}
a^2&z(a+b)\\
0&b^2
\end{pmatrix}.
\]
Hence
\[
\|E^2\|_{\mathrm F}^2
=
|a|^4+|b|^4+|z|^2|a+b|^2.
\]
If
\[
r\le\frac12,
\]
then
\[
|a+b|
\le
|a|+|b|
\le1,
\]
and also
\[
|a|^4\le|a|^2,
\qquad
|b|^4\le|b|^2.
\]
Therefore
\[
\|E^2\|_{\mathrm F}^2
\le
|a|^2+|b|^2+|z|^2
=
\|E\|_{\mathrm F}^2.
\]

To prove sharpness, fix
\[
\frac12<r<1
\]
and consider
\[
E_M=
\begin{pmatrix}
r&M\\
0&r
\end{pmatrix}.
\]
Then
\[
\rho(E_M)=r,
\]
while
\[
\|E_M\|_{\mathrm F}^2
=
2r^2+M^2
\]
and
\[
\|E_M^2\|_{\mathrm F}^2
=
2r^4+4r^2M^2.
\]
Thus
\[
\|E_M^2\|_{\mathrm F}^2-\|E_M\|_{\mathrm F}^2
=
-2r^2(1-r^2)
+
(4r^2-1)M^2.
\]
Because
\[
4r^2-1>0,
\]
this is positive for all sufficiently large \(M\). Hence the dimension-two threshold \(1/2\) is exact.

For the dimension-three obstruction, let
\[
N_M=
\begin{pmatrix}
0&M&0\\
0&0&M\\
0&0&0
\end{pmatrix}.
\]
It is nilpotent of index three, so
\[
\rho(N_M)=0,
\qquad
N_M^3=0.
\]
Direct multiplication gives
\[
N_M^2=
\begin{pmatrix}
0&0&M^2\\
0&0&0\\
0&0&0
\end{pmatrix}.
\]
Consequently
\[
\|N_M\|_{\mathrm F}=\sqrt2\,M,
\qquad
\|N_M^2\|_{\mathrm F}=M^2,
\]
and
\[
\|N_M\|_2=M,
\qquad
\|N_M^2\|_2=M^2.
\]
The stated amplification laws follow.

Finally, with
\[
A=I_3,
\qquad
X_0=I_3-N_M,
\]
the Newton–Schulz residual is exactly
\[
E_0=N_M.
\]
The squaring recurrence gives
\[
E_1=N_M^2,
\qquad
E_2=N_M^4=0,
\]
so
\[
X_2=I_3=A^{-1}.
\]

If a \(2\times2\) matrix has spectral radius zero, both eigenvalues are zero. Its characteristic polynomial is therefore
\[
\lambda^2,
\]
and Cayley–Hamilton gives
\[
E^2=0.
\]
The same is trivial in dimension one. Hence dimension three is minimal for a zero-spectral-radius residual spike.

## Verification
The embedded `verify.py` checks exact rational instances of the two-dimensional sharpness family and the three-dimensional nilpotent construction.

For
\[
r=\frac34,
\qquad
M=2,
\]
it verifies
\[
\rho(E_0)=\frac34<1
\]
and
\[
\|E_1\|_{\mathrm F}^2
>
\|E_0\|_{\mathrm F}^2.
\]

For
\[
M=10,
\]
it verifies the nilpotent identities
\[
E_0^3=0,
\qquad
E_1=E_0^2,
\qquad
E_2=0,
\]
together with the exact Frobenius amplification
\[
\frac{\|E_1\|_{\mathrm F}^2}
{\|E_0\|_{\mathrm F}^2}
=
50.
\]

The dimension-two universal bound is proved analytically by Schur triangularization and is not inferred from finite testing.

## Relationship to prior work
Newton–Schulz inversion is classical. Modern full-text treatments state the iteration
\[
X_{k+1}=X_k(2I-AX_k),
\]
the residual relation, and the fact that convergence is governed by
\[
\rho(I-AX_0)<1.
\]
Those facts are prior work.

Khaksar Haghani and Soleymani develop an improved Schulz-type matrix-inversion method and explicitly treat the classical Schulz iteration as the baseline. Gawlik and Leok analyze Newton–Schulz matrix iterations in a matrix-function setting; their public preprint places this subject primarily under MSC \(65F30\). Cordero, Segura, Torregrosa, and Vassileva give a modern full-text account of Newton–Schulz inversion and its residual convergence mechanism.

The additional result is a transient classification not supplied by those convergence statements: the exact two-dimensional Frobenius safety radius
\[
\rho(E_0)\le\frac12,
\]
followed by the dimension-three collapse of every spectral-radius-only safety guarantee, even at
\[
\rho(E_0)=0,
\]
with arbitrarily large first residual amplification and exact next-step termination.

A nearby published result on normal spectral filtering gives sharp Rayleigh-residual distortion through a filter-gain dynamic range. It does not cover this construction because Newton–Schulz residual squaring acts on a nonnormal matrix residual, and the three-dimensional witness is nilpotent.

Targeted searches under Newton–Schulz, residual squaring, nonnormality, Frobenius monotonicity, nilpotent residuals, spectral radius, and minimal dimension did not locate the two-dimensional threshold or the three-dimensional exact-termination spike.

## Limitations
The dimension-two sharp universal statement is for Frobenius norm. A separate operator-norm classification for all \(2\times2\) residuals is not claimed.

The three-dimensional obstruction allows an unrestricted initial approximate inverse. Standard practical initializations such as scaled adjoints often enforce a normal or norm-contractive residual and therefore exclude this pathology.

The target matrix in the sharp three-dimensional family is \(I_3\), so target conditioning is deliberately removed as an explanatory variable.

The result is exact-arithmetic. It does not quantify floating-point behavior for large \(M\).

Generic transient growth of nonnormal matrix powers is classical linear algebra. The originality claim is restricted to the sharp \(2\times2\) Newton–Schulz residual-safety radius, the minimal dimension-three zero-spectrum obstruction, and the exact two-step matrix-inversion realization.

## References
1. F. Khaksar Haghani and F. Soleymani, “An improved Schulz-type iterative method for matrix inversion with application,” Transactions of the Institute of Measurement and Control 36 (2014), 983–991. DOI 10.1177/0142331214528350. First published online 2014-04-15.
2. E. S. Gawlik and M. Leok, “Computing the Fréchet Derivative of the Polar Decomposition,” arXiv:1608.04491v1, submitted 2016-08-16; later published as “Iterative Computation of the Fréchet Derivative of the Polar Decomposition.”
3. A. Cordero, E. Segura, J. R. Torregrosa, and M. P. Vassileva, “New Iterative Procedures for Approximating Different Types of Inverse Matrix: Convergence and Stability,” Mathematical Methods in the Applied Sciences 48 (2025), 8806–8817. DOI 10.1002/mma.10754.
