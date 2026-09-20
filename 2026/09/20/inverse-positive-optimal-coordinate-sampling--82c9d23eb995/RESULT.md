# Closed-form optimal coordinate sampling for inverse-positive SPD quadratics

## Setting

Let
\[
f(x)=\tfrac12 x^T A x-b^T x,
\]
where \(A\in\mathbb R^{n\times n}\) is symmetric positive definite (SPD), and let
\(x_*=A^{-1}b\). Write
\[
D=\operatorname{diag}(A),\qquad C=D^{-1/2}AD^{-1/2}.
\]
Thus \(C\succ0\) and \(C_{ii}=1\). At each iteration choose one coordinate \(i\)
independently with a fixed probability \(p_i>0\), \(\sum_i p_i=1\), and perform the
exact coordinate minimization
\[
x^+=x-\frac{(Ax-b)_i}{A_{ii}}e_i.
\]
Equivalently, this is randomized Gauss--Seidel relaxation for \(Ax=b\). The error
metric is the squared \(A\)-energy \(\|x-x_*\|_A^2\), equivalently twice the
quadratic objective gap.

For \(P=\operatorname{Diag}(p)\), define
\[
\rho(p)=\lambda_{\min}\!\left(P^{1/2}CP^{1/2}\right).
\]
The exact one-step worst-case expectation satisfies
\[
\mathbb E\!\left[\|x^+-x_*\|_A^2\mid x\right]
\le (1-\rho(p))\|x-x_*\|_A^2,
\]
and the factor \(1-\rho(p)\) is sharp for that fixed sampling distribution.

## Main theorem

Assume that \(A^{-1}\) is entrywise nonnegative. This includes every SPD Stieltjes
matrix (an SPD matrix with nonpositive off-diagonal entries). Define
\[
q=C^{-1}{\bf1},\qquad S={\bf1}^TC^{-1}{\bf1}={\bf1}^Tq.
\]
Then \(q_i>0\), and the unique fixed iid coordinate distribution maximizing the
sharp one-step contraction parameter is
\[
\boxed{\quad p_i^*=\frac{q_i}{S}\quad}
\]
with exact optimum
\[
\boxed{\quad \max_{p\in\Delta_n}\rho(p)=\rho^*=\frac1S.\quad}
\]
In the original scaling,
\[
q=D^{1/2}A^{-1}D^{1/2}{\bf1}
  =D^{1/2}A^{-1}\sqrt d,
\qquad d=(A_{11},\ldots,A_{nn})^T,
\]
so
\[
\boxed{
 p_i^*=\frac{\sqrt{A_{ii}}\,(A^{-1}\sqrt d)_i}
 {\sqrt d^{\,T}A^{-1}\sqrt d}},
\qquad
\boxed{
 \rho^*=\frac1{\sqrt d^{\,T}A^{-1}\sqrt d}}.
\]
The conclusion is structural: it solves the fixed-probability optimization exactly
on this matrix class. Computing \(p^*\) from a generic dense matrix requires a
linear solve and therefore is not automatically a cheaper way to solve the
original problem.

## Proof

For an error \(e=x-x_*\), an exact update of coordinate \(i\) gives
\[
\|e\|_A^2-\|e^+\|_A^2
=\frac{(e_i^TAe)^2}{A_{ii}}.
\]
Hence, with \(H=\operatorname{Diag}(p_i/A_{ii})\),
\[
\mathbb E[\|e^+\|_A^2\mid e]
=\|e\|_A^2-e^TAHAe.
\]
After the change of variables \(z=A^{1/2}e\), the sharp decrement constant is
\(\lambda_{\min}(A^{1/2}HA^{1/2})\). The nonzero spectra of the two Gram products
show that this equals
\[
\lambda_{\min}(P^{1/2}CP^{1/2})=\rho(p).
\]

Because \(A^{-1}\ge0\) entrywise, also
\[
C^{-1}=D^{1/2}A^{-1}D^{1/2}\ge0.
\]
Since its diagonal entries are positive, \(q=C^{-1}{\bf1}\) is strictly positive.
For arbitrary interior \(p\), put \(v=P^{-1/2}q\). The Rayleigh quotient gives
\[
\rho(p)
\le \frac{v^TP^{1/2}CP^{1/2}v}{v^Tv}
=\frac{S}{\sum_i q_i^2/p_i}.
\]
Cauchy--Schwarz yields
\[
\sum_i\frac{q_i^2}{p_i}\ge\left(\sum_iq_i\right)^2=S^2,
\]
so \(\rho(p)\le1/S\).

Now choose \(P_*=\operatorname{Diag}(q/S)\). Then for
\(v=P_*^{-1/2}q>0\),
\[
P_*^{1/2}CP_*^{1/2}v=P_*^{1/2}Cq
=P_*^{1/2}{\bf1}=\frac1S v.
\]
Moreover
\[
(P_*^{1/2}CP_*^{1/2})^{-1}
=P_*^{-1/2}C^{-1}P_*^{-1/2}\ge0
\]
entrywise, and the same positive vector is its eigenvector with eigenvalue \(S\).
By the Perron--Frobenius/Collatz--Wielandt characterization, \(S\) is the spectral
radius of this inverse matrix. Therefore the smallest eigenvalue of
\(P_*^{1/2}CP_*^{1/2}\) is exactly \(1/S\), proving attainability.

Equality in the Cauchy--Schwarz step requires \(p_i\propto q_i\), so the interior
optimizer is unique. If any \(p_i=0\), then \(P^{1/2}CP^{1/2}\) is singular and
\(\rho(p)=0\); hence the optimizer is unique on the full probability simplex.

## Explicit Dirichlet-Poisson corollary

For the one-dimensional Dirichlet Poisson matrix
\[
A_n=\operatorname{tridiag}(-1,2,-1),
\]
we have \(D=2I\), \(C=A_n/2\), and
\[
q_i=i(n+1-i).
\]
Consequently
\[
\boxed{
 p_i^*=\frac{6i(n+1-i)}{n(n+1)(n+2)}},
\qquad
\boxed{
 \rho^*=\frac{6}{n(n+1)(n+2)}}.
\]
Uniform sampling, which here is also the usual diagonal/Lipschitz sampling, has
\[
\rho_{\rm unif}=\frac{1-\cos(\pi/(n+1))}{n}.
\]
Thus
\[
\frac{\rho^*}{\rho_{\rm unif}}
\longrightarrow \frac{12}{\pi^2}=1.215854\ldots .
\]
This is an improvement in the sharp expected energy-contraction constant for this
fixed iid coordinate model; it is not a claim of the same percentage improvement
in wall-clock time.

## Relation to prior work and originality check

Gower and Richtárik (2015) formulate the optimal fixed sampling for randomized
linear-system methods, including randomized coordinate descent, through a
semidefinite optimization. Kovalev, Gorbunov, Gasanov and Richtárik (2018) state
that the optimal RCD probabilities can in principle be computed by SDP and note
that theoretical properties of the optimum were not then available; they also
show, among other negative results, that common importance samplings need not be
near-optimal in general. Richtárik and Takáč (2016) optimize probability choices
for broader stochastic-coordinate bounds rather than this exact quadratic
smallest-eigenvalue criterion. Frommer and Szyld (2023) optimize randomized
relaxation bounds in different residual norms and for broader matrix classes.

There is also an exact optimal-design translation. If \(F=C^{1/2}\) and \(f_i\)
is its \(i\)-th column, then
\[
P^{1/2}CP^{1/2}\quad\text{and}\quad
F P F^T=\sum_i p_i f_if_i^T
\]
have the same eigenvalues. Maximizing \(\rho(p)\) is therefore a saturated
E-optimal design problem on linearly independent support vectors. Pukelsheim and
Torsney (1991) give a general theory of optimal weights on linearly independent
support points, including the E-optimal criterion within the matrix-mean family.
The checked theorem and corollary statements did not yield the inverse-positive
closed form above. Searches using the coordinate-descent, E-optimal-design,
inverse-positive/M-matrix, diagonal-scaling and equivalent smallest-eigenvalue
formulations did not locate this formula. Accordingly, originality is claimed
only to the best of our knowledge; an equivalent theorem may exist in older
optimal-design or matrix-scaling literature under different terminology.

A current-status check also included the 2026 subspace-constrained RCD work of Lok
and Rebrova, whose contribution concerns low-rank-aware subspace restriction rather
than the fixed-probability optimization solved here.

## Computational model and limitations

- Exact arithmetic and exact one-coordinate minimization are assumed.
- Coordinate indices are iid draws from one fixed distribution; adaptive,
  without-replacement, block, greedy, accelerated, spectral and conjugate-direction
  rules are outside the theorem.
- Optimality is for the sharp worst-case one-step expected \(A\)-energy (equivalently
  quadratic objective-gap) factor. It is not an optimality claim for every other
  norm, tail criterion, finite-horizon policy or implementation cost.
- The entrywise condition \(A^{-1}\ge0\) is sufficient for the closed form and is
  automatic for SPD Stieltjes matrices. No claim is made that it is necessary for
  some other matrix to admit an explicit optimizer.
- Forming \(p^*\) for a generic matrix requires solving a linear system. The formula
  is directly useful when that solve is available, reusable, approximable, or
  structurally explicit, as in the Poisson example.
- Stronger algorithms can outperform coordinate descent under different primitive
  operations or preprocessing. The theorem does not provide a lower bound against
  conjugate-gradient, spectral/conjugate-direction, block, or other general solvers.
- Historical-equivalence risk remains because the E-optimal-design and diagonal
  matrix-scaling literatures are broad; the originality statement is therefore
  deliberately restricted to the sources and equivalent formulations checked.

## Reproducibility

`artifacts/verify_coordinate_sampling.py` deterministically checks the closed form
on generated SPD Stieltjes matrices, the expected energy-decrement identity, and
the Dirichlet-Poisson formula. `artifacts/verification.txt` records its verified
output. Numerical checks support the algebra but are not used as a substitute for
the proof above.

## References

1. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, SIAM J. Matrix Anal. Appl. 36(4), 1660--1690 (2015), DOI: 10.1137/15M1025487.
2. D. Kovalev, E. Gorbunov, E. Gasanov and P. Richtárik, *Stochastic Spectral and Conjugate Descent Methods* (2018), arXiv:1802.03703.
3. P. Richtárik and M. Takáč, *On optimal probabilities in stochastic coordinate descent methods*, Optimization Letters 10, 1233--1243 (2016), DOI: 10.1007/s11590-015-0916-1.
4. F. Pukelsheim and B. Torsney, *Optimal weights for experimental designs on linearly independent support points*, Ann. Statist. 19(3), 1614--1625 (1991), DOI: 10.1214/aos/1176348265.
5. A. Frommer and D. B. Szyld, *On the convergence of randomized and greedy relaxation schemes for solving nonsingular linear systems of equations*, Numer. Algorithms 92, 639--664 (2023), DOI: 10.1007/s11075-022-01431-7.
6. J. Lok and E. Rebrova, *Subspace-Constrained Randomized Coordinate Descent for Linear Systems with Good Low-Rank Matrix Approximations*, SIAM J. Matrix Anal. Appl. 47(3), 1495--1529 (2026), DOI: 10.1137/25M177446X.
