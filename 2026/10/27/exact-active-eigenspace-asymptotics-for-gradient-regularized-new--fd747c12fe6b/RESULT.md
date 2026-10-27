# Exact active-eigenspace asymptotics for gradient-regularized Newton on SPD quadratics

## Finding

Let \(Q\in\mathbb R^{d\times d}\) be symmetric positive definite, let \(f(x)=\tfrac12 x^{\mathsf T}Qx\), fix \(H>0\), and start from any \(x_0\ne0\). Apply the fixed gradient-regularized Newton iteration

\[
x_{k+1}=x_k-\bigl(Q+\sqrt{H\|Qx_k\|_2}\,I\bigr)^{-1}Qx_k.
\]

For each eigenvalue \(\lambda\) of \(Q\), let \(P_\lambda\) be its orthogonal spectral projector, and define

\[
\lambda_* = \min\{\lambda\in\operatorname{spec}(Q):P_\lambda x_0\ne0\},\qquad P_*=P_{\lambda_*}.
\]

Then the iterates converge to the minimizer \(0\), their normalized direction converges to the normalized initial projection onto the lowest active eigenspace, and the exact asymptotic laws are

\[
\frac{x_k}{\|x_k\|_2}\longrightarrow\frac{P_*x_0}{\|P_*x_0\|_2},\qquad
\frac{\|x_{k+1}\|_2}{\|x_k\|_2^{3/2}}\longrightarrow\sqrt{\frac{H}{\lambda_*}},
\]

and

\[
\frac{\|\nabla f(x_{k+1})\|_2}{\|\nabla f(x_k)\|_2^{3/2}}\longrightarrow\frac{\sqrt H}{\lambda_*}.
\]

The exponent \(3/2\) is therefore exact on every nonzero SPD-quadratic trajectory, not merely an upper-bound exponent. The asymptotic constant depends on the smallest eigenvalue actually represented in \(x_0\), rather than necessarily on the global minimum eigenvalue of \(Q\).

## Assumptions and scope

The matrix \(Q\) is real symmetric positive definite, all linear solves are exact, the norm is Euclidean, and \(H\) is fixed and strictly positive. The claim concerns the stated fixed-regularization iteration on the unconstrained quadratic only. It does not cover line-search variants, inexact linear solves, nonsmooth terms, indefinite Hessians, or nonquadratic objectives.

## Proof

Write \(s_k=\|x_k\|_2\) and \(r_k=\sqrt{H\|Qx_k\|_2}\). The update is exactly

\[
x_{k+1}=r_k(Q+r_kI)^{-1}x_k.
\]

Every eigencomponent is multiplied by the positive scalar \(r_k/(\lambda+r_k)\), so a nonzero component never vanishes and each eigenspace remains invariant. Since \(s_k\le s_0\), we have \(r_k\le R:=\sqrt{H\lambda_{\max}(Q)s_0}\), and hence

\[
s_{k+1}\le\frac{R}{\lambda_{\min}(Q)+R}s_k.
\]

The factor on the right is strictly below one, proving geometric convergence to zero and therefore \(r_k\to0\).

For any active eigenvalue \(\mu>\lambda_*\), the ratio of its component norm to the component norm in \(E_*:=\operatorname{range}(P_*)\) evolves by the factor

\[
\frac{\lambda_*+r_k}{\mu+r_k}\longrightarrow\frac{\lambda_*}{\mu}<1.
\]

Thus every component above \(\lambda_*\) vanishes relative to the \(E_*\) component. Within \(E_*\), all coordinates receive the same scalar multiplier, so the direction of that projection remains the direction of \(P_*x_0\). This proves the asserted normalized-direction limit.

The spectral-direction limit also gives

\[
\frac{\|Qx_k\|_2}{s_k}\to\lambda_*,\qquad
\frac{\|(Q+r_kI)^{-1}x_k\|_2}{s_k}\to\frac1{\lambda_*}.
\]

Using \(s_{k+1}=r_k\|(Q+r_kI)^{-1}x_k\|_2\) and \(r_k/s_k^{1/2}=\sqrt{H\|Qx_k\|_2/s_k}\), we obtain

\[
\frac{s_{k+1}}{s_k^{3/2}}
=\frac{r_k}{s_k^{1/2}}\frac{\|(Q+r_kI)^{-1}x_k\|_2}{s_k}
\longrightarrow\sqrt{H\lambda_*}\,\frac1{\lambda_*}
=\sqrt{\frac H{\lambda_*}}.
\]

Finally, \(\|Qx_k\|_2/s_k\to\lambda_*\). Replacing each iterate norm by its gradient norm in the previous limit therefore yields

\[
\frac{\|Qx_{k+1}\|_2}{\|Qx_k\|_2^{3/2}}\longrightarrow\frac{\sqrt H}{\lambda_*}.
\]

All statements follow from the exact spectral recurrence; no finite experiment is used as an infinite proof.

## Verification

The algebraic proof covers every dimension and every nonzero initial vector, including repeated eigenvalues. A standard-library numerical sanity check in `verify_asymptotic.py` uses a diagonal matrix with an initially absent global minimum eigenspace and confirms convergence toward the lowest active eigenspace and the predicted constants. That finite check is illustrative only; it is not the proof. The claim makes no statement about finite-precision stability or inexact solves.

## Relationship to prior work

Mishchenko's regularized Newton method uses the same fixed update and proves a general local gradient bound of order \(3/2\) (Theorem 2 and its appendix proof). Doikov and Nesterov prove analogous local superlinear bounds for a Bregman-regularized family, while Doikov, Mishchenko, and Nesterov study an adaptive family of regularization powers. The cited theorems give upper bounds or general convergence classes, not the exact asymptotic equality constant or the active-eigenspace direction established here. This is a precise quadratic specialization, not a claim that the broader regularized-Newton convergence theory is new.

## Limitations

The result is restricted to symmetric positive-definite quadratics and exact arithmetic. It does not establish a uniform rate constant independent of the initial active spectrum, does not imply the same law for nonquadratic objectives, and does not certify behavior under rounding or approximate Hessian solves. The theorem makes no claim about priority beyond the cited statement comparisons.

## References

1. K. Mishchenko, “Regularized Newton Method with Global \(O(1/k^2)\) Convergence,” arXiv:2112.02089v1 (first public version submitted 2021-12-03); SIAM Journal on Optimization 33(3), 1440–1462 (2023), DOI 10.1137/22M1488752.
2. N. Doikov and Y. Nesterov, “Gradient Regularization of Newton Method with Bregman Distances,” arXiv:2112.02952v1 (2021); DOI 10.1007/s10107-023-01943-7.
3. N. Doikov, K. Mishchenko, and Y. Nesterov, “Super-Universal Regularized Newton Method,” arXiv:2208.05888v1 (first public version 2022-08-11); SIAM Journal on Optimization 34(1), 27–56 (2024), DOI 10.1137/22M1519444.
