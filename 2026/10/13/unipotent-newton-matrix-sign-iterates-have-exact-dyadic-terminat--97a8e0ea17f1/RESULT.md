# Unipotent Newton matrix-sign iterates have exact dyadic termination but unbounded first-step transients

## Finding
Newton's iteration for the matrix sign function is
\[
X_{k+1}
=
\frac12
\left(
X_k+X_k^{-1}
\right).
\]
Consider the unipotent initial matrices
\[
X_0=I+N,
\]
where \(N\) is nilpotent. All eigenvalues of \(X_0\) are \(1\), so
\[
\operatorname{sign}(X_0)=I.
\]

For the scaled Jordan shift
\[
N=MJ_n,
\qquad M>0,
\]
the Newton iteration has two simultaneous properties.

First, it terminates exactly after a dyadic number of nilpotent degrees:
\[
\boxed{
X_k=I
\iff
2^k\ge n.
}
\]
Hence the exact iteration count is
\[
\lceil\log_2 n\rceil.
\]

Second, for every \(n\ge3\) the first error can be arbitrarily larger than the initial error even though every eigenvalue is already equal to the limiting sign eigenvalue:
\[
\boxed{
\frac{\|X_1-I\|_2}{\|X_0-I\|_2}
\ge
\frac M2.
}
\]
The Frobenius ratio satisfies
\[
\frac{\|X_1-I\|_{\mathrm F}}
{\|X_0-I\|_{\mathrm F}}
\ge
\frac{M}{2\sqrt{n-1}}.
\]

In the minimal dimension \(n=3\),
\[
X_0=
\begin{pmatrix}
1&M&0\\
0&1&M\\
0&0&1
\end{pmatrix}
\]
gives
\[
X_1=
I+\frac{M^2}{2}E_{13},
\qquad
X_2=I.
\]
Thus the exact first-step amplification factors are
\[
\frac M2
\]
in spectral norm and
\[
\frac{M}{2\sqrt2}
\]
in Frobenius norm, followed immediately by exact convergence.

## Assumptions and scope
The theorem concerns exact arithmetic and the classical unscaled Newton iteration for the matrix sign function.

The initial matrix is restricted to the natural unipotent Jordan family \(I+MJ_n\). The claim does not assert a worst-case bound over all matrices with spectrum in the open right half-plane.

The error is measured against the exact matrix sign in spectral and Frobenius norm. Since the exact sign of every matrix in the family is \(I\), no conditioning or approximation of the target sign is hidden in the statement.

No floating-point statement is made. Large \(M\) produces increasingly ill-conditioned intermediate matrices, so finite-precision behavior can differ from the exact identities.

## Proof
Let
\[
Z_k=X_k-I.
\]
Because
\[
X_k=I+Z_k,
\]
Newton's iteration gives
\[
\begin{aligned}
Z_{k+1}
&=
\frac12
\left(
I+Z_k+(I+Z_k)^{-1}
\right)
-I\\
&=
\frac12
Z_k^2(I+Z_k)^{-1}.
\end{aligned}
\]
The last identity follows by multiplying by \(I+Z_k\), or equivalently from
\[
X+X^{-1}-2I
=
X^{-1}(X-I)^2.
\]

Since \(Z_0=N\) is nilpotent, every \(Z_k\) is a polynomial in \(N\) with zero constant term. Suppose
\[
Z_k
=
c_kN^{2^k}
+
\text{higher powers of }N,
\qquad c_k\ne0.
\]
Then
\[
(I+Z_k)^{-1}
=
I+\text{positive-degree powers of }N,
\]
and therefore
\[
Z_{k+1}
=
\frac{c_k^2}{2}
N^{2^{k+1}}
+
\text{higher powers of }N.
\]
Starting from
\[
c_0=1,
\]
the recurrence
\[
c_{k+1}=\frac{c_k^2}{2}
\]
gives
\[
c_k=2^{\,1-2^k}.
\]

For the size-\(n\) Jordan shift,
\[
J_n^j\ne0
\iff
j<n.
\]
Hence
\[
Z_k\ne0
\iff
2^k<n,
\]
which proves
\[
X_k=I
\iff
2^k\ge n.
\]

Now take
\[
N=MJ_n,
\qquad n\ge3.
\]
The first error is
\[
Z_1
=
\frac12
N^2(I+N)^{-1}.
\]
Using the finite nilpotent inverse,
\[
(I+N)^{-1}
=
I-N+N^2-\cdots+(-1)^{n-1}N^{n-1},
\]
we obtain
\[
Z_1
=
\frac12
\left(
N^2-N^3+\cdots
\right).
\]
For the third coordinate vector,
\[
N^2e_3=M^2e_1
\]
and
\[
N^je_3=0
\quad
(j\ge3).
\]
Therefore
\[
Z_1e_3=\frac{M^2}{2}e_1,
\]
so
\[
\|Z_1\|_2\ge\frac{M^2}{2}.
\]
Because
\[
\|Z_0\|_2
=
M\|J_n\|_2
=
M,
\]
the spectral-norm ratio is at least
\[
\frac M2.
\]

Also
\[
\|Z_0\|_{\mathrm F}
=
M\sqrt{n-1},
\]
while the single entry identified above implies
\[
\|Z_1\|_{\mathrm F}\ge\frac{M^2}{2}.
\]
This proves the Frobenius lower bound.

For \(n=3\), \(N^3=0\), so
\[
Z_1=\frac12N^2=\frac{M^2}{2}E_{13}.
\]
Hence both norm ratios are exact, and
\[
Z_2
=
\frac12Z_1^2(I+Z_1)^{-1}
=
0.
\]

Finally, in dimensions one and two every nilpotent matrix satisfies
\[
N^2=0.
\]
Thus
\[
Z_1=0
\]
for every unipotent initial matrix in those dimensions. Dimension three is therefore minimal for a nonzero, and hence for an unbounded, first-step unipotent transient.

## Verification
The embedded `verify.py` constructs exact rational Jordan-shift examples, evaluates Newton steps by finite nilpotent inversion, and checks the termination law for dimensions \(2\) through \(9\).

For \(n=3\) and \(M=10\), it verifies
\[
X_1-I=50E_{13},
\qquad
X_2=I,
\]
giving spectral amplification \(5\) and squared Frobenius amplification \(25/2\).

It also verifies that the first nonzero power in \(X_k-I\) has exponent \(2^k\) and coefficient
\[
2^{\,1-2^k}
\]
until termination.

The all-\(n\) statements are proved analytically; finite replay is corroborative only.

## Relationship to prior work
The matrix sign function and Newton iteration for computing it are classical. Higham, Mackey, Mackey, and Tisseur state the Newton matrix-sign iteration and emphasize an important distinction from the polar-decomposition case: for the sign iteration, the matrices are generally nonnormal and the errors are not determined solely by the eigenvalues of the iterates. They also place this work under primary MSC \(65F30\).

Kenney and Laub develop globally convergent rational iterations for the matrix sign function, including Newton's method as a member of the diagonal Padé family. Those convergence results are prior work.

The finding here gives a sharp and explicit realization of the nonnormal gap on the simplest possible spectrum. Every eigenvalue of the initial matrix is already exactly \(1\), so eigenvalue convergence is vacuous, yet the first matrix error can grow without bound. At the same time, the nilpotent degree is squared at each step, giving an exact finite-termination law
\[
\lceil\log_2 n\rceil.
\]
The combination of minimal dimension, unbounded transient, and exact dyadic termination was not located in the inspected sources.

Targeted searches using matrix-sign Newton iteration, unipotent and Jordan inputs, nilpotent index, exact finite termination, and transient norm growth did not locate an implication-equivalent statement.

## Limitations
The unbounded transient is proved for a structured unipotent family. It is not a global extremal theorem over all matrices of a specified condition number or departure from normality.

The result concerns the unscaled Newton iteration. Scaling strategies developed for the matrix-sign iteration can change the transient.

The family becomes increasingly nonnormal and ill-conditioned as \(M\) grows. The point is precisely that eigenvalue placement alone does not control the matrix error; no claim is made that large-\(M\) inputs are benign in finite precision.

Generic transient growth of nonnormal matrix powers and rational functions is classical. The originality claim is restricted to the Newton matrix-sign iteration, the exact dyadic termination law on scaled unipotent Jordan blocks, and the minimal-dimension unbounded-error construction.

## References
1. N. J. Higham, D. S. Mackey, N. Mackey, and F. Tisseur, “Computing the Polar Decomposition and the Matrix Sign Decomposition in Matrix Groups,” SIAM Journal on Matrix Analysis and Applications 25 (2004), 1178–1192. DOI 10.1137/S0895479803426644.
2. C. Kenney and A. J. Laub, “Rational Iterative Methods for the Matrix Sign Function,” SIAM Journal on Matrix Analysis and Applications 12 (1991), 273–291. DOI 10.1137/0612020.
