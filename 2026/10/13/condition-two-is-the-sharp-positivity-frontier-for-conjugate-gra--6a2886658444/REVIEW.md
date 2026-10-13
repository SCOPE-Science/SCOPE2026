# Self-review

## Correctness
PASS. CG residual orthogonality makes the normalized residual polynomial an orthogonal polynomial for the positive discrete spectral measure. Its roots are Ritz values in the active spectral interval. If \(\kappa\le2\), each factor
\[
1-\lambda/\theta
\]
lies in \([-1,1]\), so every coordinate satisfies
\[
x_{k,i}=x_i^\star\bigl(1-p_k(\lambda_i)\bigr)\ge0.
\]
Two dimensions terminate in at most two active modes. For every \(\kappa>2\), a three-mode perturbation has a degree-two residual polynomial converging to an annihilator whose value at the high mode is \(\kappa-1>1\), giving a negative second-iterate coordinate. The packaged exact-rational witness verifies the strict failure at \(\kappa=4\).

## Originality
PASS. The closest full-text source gives the CG Krylov framework and the exact-line-search equivalence with the well-defined one-parameter Broyden family, but does not state a componentwise positivity theorem. Targeted searches for nonnegative CG iterates, positive-orthant invariance, Ritz-polynomial sign bounds, BFGS/Broyden positivity, and the condition-number-two threshold found no implication-equivalent statement.

The main residual risk is older CG or orthogonal-polynomial literature in which the factor bound may appear without positivity terminology. The Broyden transfer itself is an application of a published equivalence; the accepted originality lies in the sharp CG cone theorem and its minimal obstruction.

## Value
PASS. Energy-norm convergence does not certify coordinate feasibility. This theorem gives an exact safety boundary for a canonical Krylov method, identifies the exceptional two-dimensional regime, and shows the earliest possible failure above the boundary. The identical-iterate theorem extends the practical relevance to exact-line-search BFGS and the broader one-parameter Broyden family.

## Closest literature and limitations
Forsgren--Odland is the closest full-text source for the algorithmic structure and quasi-Newton equivalence. The finding is restricted to positive diagonal systems, the zero start, and exact arithmetic; the quasi-Newton corollary additionally assumes exact line search, identity initialization, and well-defined updates.

Self-review: passed. Independent audit: not yet performed.
