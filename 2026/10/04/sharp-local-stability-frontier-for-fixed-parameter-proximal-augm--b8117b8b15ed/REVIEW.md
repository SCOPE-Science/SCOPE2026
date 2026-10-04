# Same-model review

## Correctness

PASS. With \(r=1/\gamma\) and \(D=r+\rho-a>0\), the exact primal subproblem is globally \(D\)-strongly convex. Near the KKT point the box is inactive, so the full primal-dual map is exactly the displayed \(2\times2\) linear recurrence. Its trace and determinant give the three second-order Jury-Schur inequalities, which reduce without approximation to \(\rho>a\) and \(4/\gamma+\rho>2a\).

The excluded boundary cases are not hidden behind a sufficient condition: \(\rho=a\) gives determinant one, and \(4/\gamma+\rho=2a\) with \(\rho>a\) gives an exact \(-1\) eigenmode. Arbitrarily small eigenvector orbits remain inside the inactive-box neighborhood and fail to converge. Strictly outside the frontier there is an eigenvalue of modulus greater than one. The optimal local rate follows from the exact discriminant and monotonicity on the real-root and complex-root branches.

The bundled exact-rational verifier checks the characteristic identities, the optimal double root, a strongly-convex-but-unstable parameter choice, and both boundary-cycle mechanisms. The finite replay is supporting evidence; the quantified proof is algebraic.

## Originality

PASS. The recent primary paper was inspected at the P-ALM definition, assumptions, KKT-operator formulation, algorithm, and convergence discussion. It explicitly motivates the proximal term by its ability to make nonconvex subproblems strongly convex, but its nonconvex guarantee uses adaptive schedules and finite approximate-KKT termination rather than a fixed-parameter sequential phase portrait.

The closest nonconvex quadratic P-ALM paper was inspected in full. Its QPALM algorithm has a nested structure in which the proximity point can remain fixed through inner augmented-Lagrangian iterations, so its positive-penalty convergence mechanism does not imply the one-step frontier here. A 2020 nonlinear proximal-multiplier rate paper was available only at abstract level; it gives general linear convergence above a penalty threshold but not the exact two-parameter frontier in the inspected material.

Targeted published-finding corpus searches returned no equivalent fixed-P-ALM scalar law. Residual risk from older local multiplier literature is explicitly retained.

## Value

PASS. The finding distinguishes strong convexification of the primal subproblem from stability of the coupled primal-dual method on the simplest normal negative-curvature mode compatible with the standard composite assumptions. The exact frontier and unique rate-optimal proximal coefficient provide a concrete parameter-design benchmark for fixed and adaptive P-ALM schemes. The result is not presented as a multidimensional global theorem.

Same-model review: passed. Independent audit: not yet performed.
