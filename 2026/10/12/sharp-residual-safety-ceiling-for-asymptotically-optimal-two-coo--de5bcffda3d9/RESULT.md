# Sharp residual-safety ceiling for asymptotically optimal two-coordinate SOR

## Finding
Consider the symmetric positive-definite two-coordinate system
\[
A_\rho=
\begin{pmatrix}
1&\rho\\
\rho&1
\end{pmatrix},
\qquad
0\le\rho<1,
\]
and perform one classical forward SOR sweep with
\[
0<\omega<2.
\]
Let \(r^-\) and \(r^+\) be the Euclidean residuals before and after the completed sweep.

Put
\[
s=\sqrt{1-\rho^2}.
\]
Then the exact one-sweep residual-safety ceiling is
\[
\boxed{
\|r^+\|_2\le\|r^-\|_2
\text{ for every }r^-
\iff
\omega\le
\omega_{\mathrm E}(\rho)
=
\frac{2s}{1+s-s^2}.
}
\]

For the same two-cyclic family, the asymptotically optimal SOR parameter is
\[
\omega_{\mathrm{opt}}(\rho)
=
\frac{2}{1+s}.
\]
The two objectives agree only up to the sharp frontier
\[
\boxed{
\omega_{\mathrm{opt}}(\rho)
\le
\omega_{\mathrm E}(\rho)
\iff
\rho^2\le\frac12.
}
\]
Since
\[
\kappa_2(A_\rho)
=
\frac{1+\rho}{1-\rho},
\]
the equivalent condition-number statement is
\[
\boxed{
\omega_{\mathrm{opt}}
\text{ is one-sweep residual nonexpansive}
\iff
\kappa_2(A_\rho)
\le
3+2\sqrt2.
}
\]

The residual-safe ceiling expressed directly through \(\kappa\) is
\[
\omega_{\mathrm E}(\kappa)
=
\frac{
4\sqrt\kappa(\kappa+1)
}{
(\kappa-1)^2+2\sqrt\kappa(\kappa+1)
}.
\]

For a concrete exact witness, take
\[
\rho=\frac45,
\qquad
A=
\begin{pmatrix}
1&4/5\\
4/5&1
\end{pmatrix}.
\]
Then
\[
\kappa_2(A)=9,
\qquad
\omega_{\mathrm{opt}}=\frac54,
\]
whereas
\[
\omega_{\mathrm E}=\frac{30}{31}.
\]
Starting from
\[
r^-=(0,1)^{\mathsf T},
\]
one asymptotically optimal SOR sweep gives
\[
r^+=(-1,-1/4)^{\mathsf T},
\]
and therefore
\[
\frac{\|r^+\|_2^2}{\|r^-\|_2^2}
=
\frac{17}{16}.
\]

## Assumptions and scope
The theorem concerns exact arithmetic, the natural coordinate order \(1\to2\), the unit-diagonal SPD family \(A_\rho\), a completed forward SOR sweep, and Euclidean equation-residual norm.

The term “asymptotically optimal” refers to minimizing the spectral radius of the SOR error-iteration matrix for this two-cyclic family. The result does not claim that the same parameter is optimal for a finite stopping horizon.

The coefficient family is the canonical Jacobi-scaled two-coordinate SPD family. No global statement is made here over all \(2\times2\) SPD matrices with unequal diagonal entries, nor over higher dimensions, red-black orderings, SSOR, block SOR, asynchronous relaxation, or finite precision.

## Proof
Write the incoming residual as
\[
r^-=
\begin{pmatrix}
r_1\\r_2
\end{pmatrix}.
\]
The first relaxed coordinate update changes the first component by
\[
\delta_1=\omega r_1.
\]
The intermediate residual is
\[
\begin{pmatrix}
(1-\omega)r_1\\
r_2-\omega\rho r_1
\end{pmatrix}.
\]
The second relaxed coordinate update then uses
\[
\delta_2=
\omega
\left(
r_2-\omega\rho r_1
\right).
\]
After the complete sweep,
\[
r^+=R_{\omega,\rho}r^-,
\]
with
\[
R_{\omega,\rho}
=
\begin{pmatrix}
1-\omega+\omega^2\rho^2&-\omega\rho\\
-\omega\rho(1-\omega)&1-\omega
\end{pmatrix}.
\]

Hence residual nonexpansion for every incoming residual is equivalent to
\[
R_{\omega,\rho}^{\mathsf T}R_{\omega,\rho}
\preceq I.
\]
Let
\[
G=
I-
R_{\omega,\rho}^{\mathsf T}R_{\omega,\rho}
\]
and
\[
s=\sqrt{1-\rho^2}.
\]
A direct calculation gives
\[
G_{22}
=
\omega
\left[
2-\omega(2-s^2)
\right]
\]
and
\[
\det G
=
\omega^2
\left[
2s-\omega(1+s-s^2)
\right]
\left[
2s+\omega(1-s-s^2)
\right].
\]

For
\[
0<\omega<2,
\]
the second determinant factor is strictly positive. If
\[
1-s-s^2\ge0,
\]
this is immediate. If
\[
1-s-s^2<0,
\]
its zero is
\[
\frac{2s}{s+s^2-1}>2
\]
because
\[
s+s^2-1<s.
\]
Therefore, throughout the SOR convergence interval, the determinant changes sign only when
\[
2s-\omega(1+s-s^2)=0.
\]

Define
\[
\omega_{\mathrm E}
=
\frac{2s}{1+s-s^2}.
\]
For
\[
0<\omega\le\omega_{\mathrm E},
\]
one also has
\[
\omega
\le
\frac{2}{2-s^2},
\]
because
\[
s(2-s^2)\le1+s-s^2
\]
is equivalent to
\[
(1-s)^2(1+s)\ge0.
\]
Thus
\[
G_{22}\ge0
\]
and
\[
\det G\ge0,
\]
so
\[
G\succeq0.
\]
If
\[
\omega>\omega_{\mathrm E},
\]
then
\[
\det G<0,
\]
so \(G\) is indefinite and there exists an incoming residual whose Euclidean norm grows. This proves the exact residual-safety ceiling.

Now derive the asymptotically optimal SOR parameter. The homogeneous SOR error matrix for the same family is
\[
T_{\omega,\rho}
=
\begin{pmatrix}
1-\omega&-\omega\rho\\
-\omega\rho(1-\omega)&1-\omega+\omega^2\rho^2
\end{pmatrix}.
\]
Its determinant is
\[
(1-\omega)^2,
\]
and the discriminant of its characteristic polynomial is
\[
\rho^2\omega^2
\left(
\rho^2\omega^2-4\omega+4
\right).
\]
The crossover from two real eigenvalues to a complex-conjugate pair occurs at the smaller positive root
\[
\omega_{\mathrm{opt}}
=
\frac{2}{1+s}.
\]
Below this crossover the dominant real eigenvalue decreases with \(\omega\); above it the two eigenvalues have modulus
\[
\omega-1,
\]
which increases with \(\omega\). Hence the crossover is the spectral-radius minimizer.

Finally,
\[
\omega_{\mathrm{opt}}
\le
\omega_{\mathrm E}
\]
is equivalent to
\[
\frac1{1+s}
\le
\frac{s}{1+s-s^2},
\]
which reduces to
\[
s^2\ge\frac12.
\]
Since
\[
s^2=1-\rho^2,
\]
this is
\[
\rho^2\le\frac12.
\]
Using
\[
\rho=\frac{\kappa-1}{\kappa+1}
\]
gives
\[
\kappa\le3+2\sqrt2.
\]

For the witness \(\rho=4/5\), one has
\[
s=\frac35,
\qquad
\omega_{\mathrm E}
=
\frac{30}{31},
\qquad
\omega_{\mathrm{opt}}
=
\frac54.
\]
The residual matrix at the optimal SOR parameter is
\[
R=
\begin{pmatrix}
3/4&-1\\
1/4&-1/4
\end{pmatrix}.
\]
Applying it to \(e_2\) gives the stated factor \(17/16\) in squared residual norm.

## Verification
The embedded `verify.py` uses exact rational arithmetic for the \(\rho=4/5\) witness. It reconstructs the completed-sweep residual map,
\[
R=
\begin{pmatrix}
3/4&-1\\
1/4&-1/4
\end{pmatrix},
\]
checks
\[
R(0,1)^{\mathsf T}=(-1,-1/4)^{\mathsf T},
\]
and verifies the exact squared amplification factor
\[
17/16.
\]

The checker also evaluates the closed formulas at several rational Pythagorean choices of \((\rho,s)\) and verifies that the determinant of
\[
I-R^{\mathsf T}R
\]
vanishes exactly at \(\omega_{\mathrm E}\). It separately checks the equality
\[
\omega_{\mathrm{opt}}=\omega_{\mathrm E}
\]
at
\[
\rho^2=\frac12
\]
with high-precision arithmetic.

The universal safe-interval statement is proved analytically; finite replay is corroborative only.

## Relationship to prior work
Successive overrelaxation is classical, and its relaxation parameter is traditionally optimized for asymptotic convergence rate. LeVeque and Trefethen’s full 1986 report analyzes the SOR iteration, explicitly identifies the spectral-radius-optimal relaxation parameter on the model Poisson family, and places the subject under MSC 65F10. That asymptotic optimization principle is prior work.

Later overrelaxation literature continues to compare parameter choices through spectral radii and asymptotic convergence. For example, Louka and Missirlis develop geometric parameter optimization for extrapolated SOR-type methods and explicitly relate their construction to the classical SOR optimum.

The claim here concerns a different criterion: Euclidean equation-residual monotonicity after one completed sweep. The proof gives an exact residual-operator ceiling for the canonical two-coordinate SPD family and shows where the classical asymptotically optimal parameter crosses that ceiling.

A closely related published result on two-coordinate Gauss–Seidel residual transients corresponds to the special case
\[
\omega=1
\]
and allows general unequal diagonals. It does not imply the SOR relaxation ceiling or the sharp crossover with \(\omega_{\mathrm{opt}}\).

Targeted searches under SOR, one-sweep residual amplification, Euclidean residual monotonicity, two-dimensional SPD systems, and optimal relaxation did not locate the formula
\[
\frac{2\sqrt{1-\rho^2}}
{1+\sqrt{1-\rho^2}-(1-\rho^2)}
\]
or the condition-number crossover
\[
3+2\sqrt2.
\]

## Limitations
The exact ceiling is proved only for the displayed unit-diagonal \(2\times2\) SPD family. It is not claimed to be the robust optimum over all \(2\times2\) SPD matrices with the same condition number.

The natural sweep order is fixed. In two coordinates, swapping the order transposes the role of the two residual components and can change the specific worst residual direction.

The theorem concerns Euclidean residual norm, not Euclidean solution error, \(A\)-energy error, or asymptotic spectral radius.

No finite-precision effects are analyzed. Near the safety boundary, rounding can perturb the observed norm change.

## References
1. R. J. LeVeque and L. N. Trefethen, “Fourier Analysis of the SOR Iteration,” ICASE Report 86-63, NASA CR-178191, September 1, 1986.
2. M. A. Louka and N. M. Missirlis, “A comparison of the Extrapolated Successive Overrelaxation and the Preconditioned Simultaneous Displacement methods for augmented linear systems,” arXiv:1502.02280v1, February 8, 2015.
