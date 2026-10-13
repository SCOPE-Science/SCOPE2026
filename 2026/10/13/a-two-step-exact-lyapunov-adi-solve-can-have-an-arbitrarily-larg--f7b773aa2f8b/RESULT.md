# A two-step exact Lyapunov ADI solve can have an arbitrarily large first residual spike

## Finding
Consider
\[
AP+PA^{\mathsf T}+BB^{\mathsf T}=0
\]
with
\[
A_M=
\begin{pmatrix}
-1&M\\
0&-1
\end{pmatrix},
\qquad
B=e_2,
\qquad
M>0.
\]
Apply exact-arithmetic low-rank ADI from \(P_0=0\), using the real shift
\[
\sigma=1
\]
twice.

Every matrix \(A_M\) is Hurwitz and has exactly the same spectrum,
\[
\{-1,-1\}.
\]
Nevertheless the first Lyapunov residual can be made arbitrarily large.

For the low-rank ADI residual factor,
\[
R_k
=
A_MP_k+P_kA_M^{\mathsf T}+BB^{\mathsf T}
=
B_{\perp,k}B_{\perp,k}^{\mathsf T},
\]
the repeated shift acts through
\[
C_M
=
(A_M+I)(A_M-I)^{-1}
=
\begin{pmatrix}
0&-M/2\\
0&0
\end{pmatrix}.
\]
Therefore
\[
B_{\perp,0}=e_2,
\qquad
B_{\perp,1}=-\frac M2e_1,
\qquad
B_{\perp,2}=0.
\]
It follows that
\[
R_0=e_2e_2^{\mathsf T},
\qquad
R_1=\frac{M^2}{4}e_1e_1^{\mathsf T},
\qquad
R_2=0.
\]

Because these residuals have rank one,
\[
\|R_k\|_2=\|R_k\|_{\mathrm F}.
\]
Thus
\[
\boxed{
\frac{\|R_1\|_2}{\|R_0\|_2}
=
\frac{\|R_1\|_{\mathrm F}}{\|R_0\|_{\mathrm F}}
=
\frac{M^2}{4},
\qquad
R_2=0.
}
\]
For every \(G>0\), the choice
\[
M=2\sqrt G
\]
produces exactly a factor-\(G\) first residual change followed by exact termination at the next step.

The phenomenon does not reflect deterioration of the approximate Gramian in Loewner order. The exact solution is
\[
P=
\begin{pmatrix}
M^2/4&M/4\\
M/4&1/2
\end{pmatrix},
\]
whereas the first ADI approximation is
\[
P_1=
\begin{pmatrix}
M^2/8&M/4\\
M/4&1/2
\end{pmatrix}.
\]
Hence
\[
0\preceq P_1\preceq P_2=P,
\qquad
P-P_1
=
\frac{M^2}{8}e_1e_1^{\mathsf T}.
\]
The approximate solutions move monotonically toward \(P\) in the positive-semidefinite order even while the standard residual norm can spike without bound.

Finally, dimension two is minimal. In one dimension, for \(A=-a\) with \(a>0\) and any real ADI shift \(\sigma>0\), the residual factor is multiplied by
\[
\frac{a-\sigma}{a+\sigma},
\]
whose absolute value is strictly smaller than one.

## Assumptions and scope
The equation is the stable continuous-time Lyapunov equation with \(E=I\), one right-hand-side column, exact arithmetic, and \(P_0=0\). The ADI convention uses shifts in the open right half-plane; the example uses the repeated real shift \(\sigma=1\).

The claimed unboundedness is over the nonnormality parameter \(M\). The eigenvalues stay fixed at \(-1\), so this is deliberately not a condition-number statement for the eigenvector matrix or for the Lyapunov operator.

The theorem concerns the residual norm of the Lyapunov equation after individual ADI steps. It does not claim that practical finite-precision implementations will terminate exactly in two steps for arbitrarily large \(M\), because large nonnormality can magnify roundoff.

## Proof
For one real shift \(\sigma>0\), low-rank ADI forms
\[
Z_1=\sqrt{2\sigma}(A-\sigma I)^{-1}B
\]
and its residual factor satisfies
\[
B_{\perp,1}
=
B+\sqrt{2\sigma}\,Z_1
=
(A+\sigma I)(A-\sigma I)^{-1}B.
\]
When the same real shift is reused, the same Cayley factor acts again. Thus
\[
B_{\perp,k}=C_\sigma^kB,
\qquad
C_\sigma=(A+\sigma I)(A-\sigma I)^{-1}.
\]

For
\[
A=A_M,\qquad \sigma=1,
\]
one has
\[
A_M+I=
\begin{pmatrix}
0&M\\
0&0
\end{pmatrix},
\qquad
(A_M-I)^{-1}
=
\begin{pmatrix}
-1/2&-M/4\\
0&-1/2
\end{pmatrix}.
\]
Multiplication gives
\[
C_M
=
\begin{pmatrix}
0&-M/2\\
0&0
\end{pmatrix},
\qquad
C_M^2=0.
\]
Applying \(C_M\) to \(B=e_2\) gives the three residual factors stated above.

The exact solution follows by writing
\[
P=
\begin{pmatrix}
x&y\\
y&z
\end{pmatrix}
\]
and equating entries in the Lyapunov equation:
\[
z=\frac12,\qquad
y=\frac M4,\qquad
x=\frac{M^2}{4}.
\]
The first ADI column is
\[
Z_1
=
\sqrt2
\begin{pmatrix}
-M/4\\
-1/2
\end{pmatrix},
\]
so
\[
P_1=Z_1Z_1^{\mathsf T}
=
\begin{pmatrix}
M^2/8&M/4\\
M/4&1/2
\end{pmatrix}.
\]
The second ADI column adds exactly
\[
\frac{M^2}{8}e_1e_1^{\mathsf T},
\]
which proves
\[
P_2=P
\]
and the Loewner-order statement.

For dimension one, the Cayley factor is the scalar
\[
\frac{-a+\sigma}{-a-\sigma}
=
\frac{a-\sigma}{a+\sigma}.
\]
Its absolute value is below one for every \(a,\sigma>0\), so no one-dimensional residual spike is possible.

## Verification
The embedded `verify.py` uses exact rational arithmetic. For several rational values of \(M\), it reconstructs the exact Lyapunov solution, the first ADI approximation, the residual matrices, the Cayley factor, the nilpotency identity
\[
C_M^2=0,
\]
and the exact second-step solution.

For the concrete choice
\[
M=6,
\]
it verifies
\[
\|R_1\|_2=9\|R_0\|_2
\]
and
\[
R_2=0.
\]

The arbitrary-\(M\) theorem is algebraic and is not inferred from finite experiments.

## Relationship to prior work
Druskin, Knizhnerman, and Simoncini develop convergence theory and relations between rational Krylov and ADI methods for Lyapunov equations. Their work establishes ADI as a rational approximation process and is prior background.

Wolf and Panzer give a directly computable low-rank residual formula for ADI:
\[
R=B_\perp B_\perp^{\mathsf T},
\]
together with a residual-factor recurrence, and explicitly note that the residual norm is commonly used as a convergence criterion. Their full text also allows repeated shifts. These facts are prior work and are used as the starting identity here.

Halikias studies strong stability under the Cayley transform and gives general conditions for excluding overshoot. That theory already explains why a stable nonnormal continuous-time matrix need not produce a norm-contractive Cayley map. The present claim does not assert that Cayley overshoot itself is new.

The additional result is the exact Lyapunov-ADI construction tying four properties together: fixed stable spectrum, an arbitrarily large first residual spike, exact zero residual after the immediately following repeated shift, and monotone positive-semidefinite improvement of the approximate Gramian. The dimension-two minimality statement is included in the same classification.

Baker, Embree, and Sabino analyze how nonnormality affects singular-value decay of Lyapunov solutions. Their result concerns compressibility of the exact solution, not stepwise ADI residual monotonicity.

Targeted searches under Lyapunov ADI residual growth, nonnormality, Jordan blocks, Cayley factors, overshoot, and exact termination did not locate an implication-equivalent statement of the combined theorem above.

## Limitations
The construction is deliberately two-dimensional and highly nonnormal. It proves that eigenvalues alone cannot control stepwise ADI residual monotonicity, but it does not give a sharp residual bound under additional numerical-range, dissipativity, or eigenvector-conditioning assumptions.

The exact two-step termination statement is an exact-arithmetic result. A finite-precision implementation with very large \(M\) may exhibit different behavior.

General Cayley-transform overshoot is prior theory. The originality claim is restricted to the stated Lyapunov-ADI residual construction, its exact two-step termination, the simultaneous Loewner-order improvement, and minimal dimension.

## References
1. V. Druskin, L. Knizhnerman, and V. Simoncini, “Analysis of the Rational Krylov Subspace and ADI Methods for Solving the Lyapunov Equation,” SIAM Journal on Numerical Analysis 49 (2011), 1875–1898. DOI 10.1137/100813257.
2. T. Wolf and H. K. F. Panzer, “The ADI iteration for Lyapunov equations implicitly performs H2 pseudo-optimal model order reduction,” arXiv:1309.3985, first submitted 2013-09-16.
3. G. Halikias, “Strong stability and the Cayley transform,” Mathematical Methods in the Applied Sciences 37 (2014), 212–216. DOI 10.1002/mma.2976.
4. J. Baker, M. Embree, and J. Sabino, “Fast Singular Value Decay for Lyapunov Solutions with Nonnormal Coefficients,” SIAM Journal on Matrix Analysis and Applications 36 (2015), 656–668. DOI 10.1137/140993867.
