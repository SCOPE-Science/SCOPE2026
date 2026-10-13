# Self-review

## Correctness
PASS. The first completed BiCGSTAB cycle reduces exactly to two positive spectral means. If
\[
m=\frac{\sum b_i^2\lambda_i}{\sum b_i^2},
\qquad
n=\frac{\sum b_i^2\lambda_i^2(\lambda_i-m)^2}{\sum b_i^2\lambda_i(\lambda_i-m)^2},
\]
then
\[
\frac{x_{1,i}}{x_i^\star}
=
\frac{\lambda_i(m+n-\lambda_i)}{mn}.
\]
Concavity in \(\lambda_i\) gives the lower endpoint reduction, while completing the square and optimizing the ratio of \(m\) and \(n\) gives the upper Kantorovich factor. The exact rational verifier reproduces the displayed negative witness and the two-mode identity.

## Originality
PASS. The full original BiCGSTAB paper was inspected. It derives the same recurrence, residual polynomial, residual-minimizing stabilization, and finite-termination property, but it does not state a componentwise first-cycle formula, a sharp coordinate envelope, the \(\kappa=2\) positivity frontier, or unconditional safety for two active eigenvalues.

Targeted searches covered BiCGSTAB/Bi-CGSTAB, positive orthants, nonnegative iterates, M-matrices, componentwise monotonicity, diagonal positive systems, first-cycle behavior, and two-eigenvalue reductions. No implication-equivalent statement was located. Residual risk remains that older Krylov or formal-orthogonal-polynomial literature uses another parametrization.

## Value
PASS. The result quantifies an intermediate-iterate feasibility property that residual-norm convergence does not control. It supplies both a sharp negative undershoot law and a sharp positive overshoot law, identifies the exact universal sign-safety boundary, and explains why two-mode problems are protected while three modes can fail.

## Closest literature and limitations
Van der Vorst's original paper is the closest source and provides the complete algorithmic substrate. Gutknecht's early variants and the later induced-dimension-reduction view develop related polynomial structure but not the componentwise envelope. The claim is limited to the first completed unpreconditioned cycle, positive diagonal systems, zero start, standard shadow residual, and exact arithmetic.

Self-review: passed. Independent audit: not yet performed.
