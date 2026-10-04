# Critical-damping ratio for scalar least-squares primal-dual linesearch
## Finding
Consider the scalar least-squares problem
\[
\min_{x\in\mathbb R} \frac12(a x)^2,
\qquad a\neq0.
\]
Use the fixed-step primal-dual algorithm contained in the Malitsky--Pock linesearch method, with extrapolation \(\theta=1\), primal step \(\tau>0\), dual step \(\sigma>0\), and ratio \(\sigma=\beta\tau\). Put
\[
r:=\tau\sigma a^2\in(0,1).
\]
For fixed \(r\), varying \(\beta\) is equivalent to varying \(\sigma>0\). The exact asymptotic spectral radius is uniquely minimized at
\[
\sigma_* = 2\sqrt{r(1-r)},
\qquad
\beta_* = 4a^2(1-r),
\]
where the two eigenvalues coalesce. The minimum radius is
\[
\rho_*=
\frac{\sqrt{1-r}}{\sqrt r+\sqrt{1-r}}.
\]
Malitsky--Pock's fixed-step sufficient linesearch condition is \(r\leq\delta^2\). Therefore, when the product is set at its scalar ceiling \(r=\delta^2\),
\[
\beta_*=4a^2(1-\delta^2).
\]

## Assumptions and scope
The statement is exact for a one-dimensional nonzero linear operator \(Kx=ax\), \(g=0\), and \(f(u)=\tfrac12u^2\), so \(f^*(y)=\tfrac12y^2\). It concerns constant steps and the source algorithm's \(\theta=1\) specialization. It optimizes the asymptotic spectral radius over the primal/dual ratio while holding the product \(r=\tau\sigma a^2\) fixed. It does not claim that this scalar ratio is globally optimal for a multi-singular-value problem.

## Proof
The fixed-step iteration can be indexed as
\[
x^k=x^{k-1}-\tau a y^k,
\qquad
\bar x^k=2x^k-x^{k-1},
\qquad
y^{k+1}=\frac{y^k+\sigma a\bar x^k}{1+\sigma}.
\]
Because \(x^k-x^{k-1}=-\tau a y^k\),
\[
y^{k+1}
=
\frac{\sigma a x^k+(1-r)y^k}{1+\sigma}.
\]
Then \(x^{k+1}=x^k-\tau a y^{k+1}\), so
\[
\begin{bmatrix}x^{k+1}\\y^{k+1}\end{bmatrix}
=
M(r,\sigma)
\begin{bmatrix}x^k\\y^k\end{bmatrix},
\]
with
\[
M(r,\sigma)=\frac1{1+\sigma}
\begin{bmatrix}
1+\sigma-r & -\tau a(1-r)\\
\sigma a & 1-r
\end{bmatrix}.
\]
Its trace and determinant are
\[
T=\frac{2+\sigma-2r}{1+\sigma},
\qquad
D=\frac{1-r}{1+\sigma},
\]
and its discriminant is
\[
T^2-4D
=
\frac{\sigma^2-4r(1-r)}{(1+\sigma)^2}.
\]
Set \(q=1-r\) and \(\sigma_c=2\sqrt{rq}\). For \(0<\sigma<\sigma_c\), the roots are a complex-conjugate pair, hence
\[
\rho(M)=\sqrt D=\sqrt{\frac q{1+\sigma}},
\]
which is strictly decreasing in \(\sigma\).

For \(\sigma>\sigma_c\), the larger real eigenvalue is
\[
\lambda_+(\sigma)
=
\frac{\sigma+2q+\sqrt{\sigma^2-4rq}}{2(1+\sigma)}.
\]
Writing \(h=\sqrt{\sigma^2-4rq}\), direct differentiation gives
\[
\lambda_+'(\sigma)
=
\frac{(2r-1)+(\sigma+4rq)/h}{2(1+\sigma)^2}.
\]
This derivative is positive. If \(r\geq\tfrac12\), both displayed numerator terms are nonnegative and the second is positive. If \(r<\tfrac12\), then \((\sigma+4rq)/h>\sigma/h>1>1-2r\). Thus the spectral radius strictly increases after \(\sigma_c\). The unique minimum is therefore at the repeated-root boundary \(\sigma_* = \sigma_c\).

At that point,
\[
\rho_*=
\sqrt{\frac q{1+2\sqrt{rq}}}
=
\frac{\sqrt q}{\sqrt r+\sqrt q}.
\]
Finally, \(r=\tau\sigma a^2\) and \(\sigma=\beta\tau\) imply
\[
r=\frac{\sigma^2a^2}\beta,
\]
so at \(\sigma_*\),
\[
\beta_*=
\frac{a^2\sigma_*^2}r
=
4a^2(1-r).
\]

## Verification
The accompanying checker reconstructs the iteration matrix from \((a,r,\sigma)\), verifies its trace, determinant, and characteristic roots, and numerically checks the strict decrease/increase on both sides of the repeated-root threshold for a grid of \(r\)-values. The algebraic proof above, rather than the finite grid, establishes the statement for every \(r\in(0,1)\).

## Relationship to prior work
Malitsky and Pock introduce the linesearch parameter \(\beta\) as the primal/dual step ratio and explicitly note that fixed steps satisfying \(\tau\sigma\leq\delta^2/\lVert K\rVert^2\) recover the underlying fixed-step primal-dual algorithm. They do not give an exact rate-optimal choice of that ratio for the scalar least-squares mode.

Fercoq later formulates quadratic PDHG as a linear fixed-point iteration whose speed is governed by the spectral radius and develops adaptive spectral-radius estimation to improve primal and dual steps. That work supplies a broader spectral-tuning framework, but the inspected quadratic analysis does not state the closed scalar law above, the repeated-root boundary \(\sigma_*=2\sqrt{r(1-r)}\), or its translation \(\beta_*=4a^2(1-r)\) to the Malitsky--Pock ratio at a fixed product.

## Limitations
The result is a scalar calibration law. A matrix with several singular values couples one shared pair of steps to several modal products, so minimizing the worst modal radius is a different minimax problem. The result concerns asymptotic spectral radius, not finite-horizon norm transients at the repeated-root point. A later or unindexed analysis of scalar PDHG tuning could contain an equivalent formula; the literature search described in the review did not locate one.

## References
1. Y. Malitsky and T. Pock, *A first-order primal-dual algorithm with linesearch*, arXiv:1608.08883, first public version 31 August 2016.
2. O. Fercoq, *Monitoring the Convergence Speed of PDHG to Find Better Primal and Dual Step Sizes*, arXiv:2403.19202, 2024.
