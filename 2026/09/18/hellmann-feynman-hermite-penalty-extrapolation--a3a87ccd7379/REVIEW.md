# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The block Schur-complement reduction is valid because the constraint-normal block \(C=U^TA^TAU\) is positive definite. When the smallest eigenvalue of \(D=Z^THZ\) is simple, the Schur determinant has a simple zero at \((t,\lambda)=(0,\lambda_*)\), so the implicit-function argument gives an analytic finite eigenvalue branch. Separation from the other eigenvalues of \(D\), together with divergence of the constraint-normal eigenvalues, identifies this branch with \(f(1/t)\) for small positive \(t\).

The expansion
\[
D-tG+t^2J+O(t^3)
\]
and standard simple-eigenvalue perturbation theory give
\[
a_1=-v^TGv,\qquad a_2=v^T(J-GSG)v.
\]
Signs were checked against an exactly solvable two-dimensional example and a reproducible random matrix calculation. The two-level fourth-order formula was independently derived by enforcing exactness on cubic polynomials in \(t=1/\rho\); the general \(2p\) order follows from the Hermite interpolation remainder. Hellmann–Feynman supplies the needed derivative conversion \(g'(t)=-t^{-2}f'(1/t)\).

Potential failure modes were checked explicitly: multiplicity of \(\lambda_*\) invalidates the scalar simple-branch coefficient formula; approximate eigenvectors perturb the derivative data; large extrapolation weights may amplify numerical errors. These are stated as limitations rather than hidden assumptions.

## Originality

The primary source, Wang–Xia (arXiv:2609.18538), was inspected at the theorem level. It establishes exact penalty duality, finite exact recovery, a first-order expansion with explicit leading coefficient, a two-level value-only cancellation of the \(1/\rho\) term, and Hellmann–Feynman sensitivity. It does not state the explicit second coefficient displayed here or the two-level fourth-order derivative-enhanced formula.

Searches covered exact and synonymous formulations involving constrained eigenvalues, projected Hessians, quadratic penalties, inverse-penalty asymptotics, Richardson extrapolation, Hellmann–Feynman derivatives, and Hermite extrapolation. Zhou–Bai–Li (2021) addresses constrained Rayleigh quotients through quadratic-eigenvalue and Krylov formulations rather than this penalty-path extrapolation. Bach (2021) is important prior art for high-order Richardson extrapolation of regularization paths; classical Richardson/Hermite interpolation is therefore not claimed as new. No inspected source gave the present projected-Hessian second coefficient or the Hellmann–Feynman Hermite order-doubling formula.

Because the primary source is extremely recent, simultaneous follow-up work is a residual originality risk. The originality claim is only to the best of our knowledge.

## Value

The source already computes penalty-path eigenvectors and uses Hellmann–Feynman sensitivity. Retaining those derivatives therefore exposes more asymptotic information per penalty level: with two levels the formal penalty error improves from second to fourth order, and in the simple-eigenvalue regime p levels improve from order p to order 2p. This is directly relevant to large-penalty continuation, where reducing the penalty required for a target asymptotic error can reduce spectral stiffness.

The contribution is not a new eigensolver or a finite-precision stability theorem. Its value is a sharper asymptotic acceleration mechanism and an explicit next coefficient for the newly introduced constrained-eigenvalue penalty path.
