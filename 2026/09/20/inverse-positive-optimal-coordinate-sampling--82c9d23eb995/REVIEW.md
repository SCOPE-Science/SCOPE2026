# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The coordinate update gives the exact energy decrement
\((e_i^TAe)^2/A_{ii}\). Averaging with fixed probabilities reduces the sharp
one-step factor to the smallest eigenvalue of \(P^{1/2}CP^{1/2}\). For
\(q=C^{-1}{\bf1}\) and \(S={\bf1}^Tq\), a Rayleigh-quotient test followed by
Cauchy--Schwarz proves the universal upper bound \(\rho(p)\le1/S\). At
\(p_i=q_i/S\), entrywise nonnegativity of \(C^{-1}\) makes the inverse scaled
matrix nonnegative; its strictly positive eigenvector with eigenvalue \(S\) fixes
its spectral radius by Perron--Frobenius/Collatz--Wielandt, proving attainment.
Equality in Cauchy--Schwarz proves uniqueness. Boundary samplings are singular and
cannot improve the optimum. The Poisson formulas follow from the explicit solution
of the one-dimensional discrete Poisson equation with unit forcing.

The proof was stress-tested on reducible as well as irreducible inverse-positive
examples, diagonal and two-dimensional limiting cases, and deterministic numerical
SPD Stieltjes instances. The published verification reproduces the rate formula,
the expected-energy identity and the Poisson asymptotics.

## Originality

**PASS, to the best of our knowledge.** Gower--Richtárik (2015) supplies the
general randomized linear-system framework and an SDP route to optimal fixed
sampling. Kovalev--Gorbunov--Gasanov--Richtárik (2018) explicitly discuss optimal
RCD probabilities through semidefinite programming and report limited structural
information about that optimum, while proving several general limitations of
importance sampling. Richtárik--Takáč (2016) and Frommer--Szyld (2023) optimize
different probability-dependent convergence bounds. The present claim instead
solves the exact smallest-eigenvalue objective in closed form for the inverse-positive
SPD class.

The mathematically equivalent saturated E-optimal-design formulation was also
checked. Pukelsheim--Torsney (1991) provides broad optimal-weight theory for
linearly independent support points and includes E-optimality in its framework, but
the checked theorem and corollary statements did not provide the inverse-positive
closed form proved here. Searches under E-optimality, inverse-positive and M-matrix
terminology, diagonal scaling, randomized Gauss--Seidel and randomized coordinate
descent did not locate an equivalent statement. The broad historical optimal-design
and matrix-scaling literatures remain the main residual originality risk.

The 2026 Lok--Rebrova subspace-constrained RCD paper was checked as a current-status
reference; its low-rank subspace mechanism does not subsume this fixed-sampling
formula.

## Value

**PASS.** The result replaces a generic semidefinite optimization by one linear
solve on a natural numerical-linear-algebra class that includes SPD Stieltjes
matrices, supplies a uniqueness theorem rather than only a candidate distribution,
and gives an explicit structured PDE example. The Poisson profile also quantifies
how the exact energy-optimal sampling differs from the standard uniform/diagonal
choice even when all coordinate Lipschitz constants are equal.

## Scientific limitations

The theorem concerns exact arithmetic, exact coordinate minimization, fixed iid
single-coordinate sampling and worst-case expected A-energy contraction. It does
not establish optimality among adaptive, without-replacement, block, accelerated,
greedy, spectral or conjugate-direction methods, nor does it compare wall-clock
costs. Computing the distribution for an unstructured matrix requires a linear
solve, so the theorem is principally structural unless that solve is reusable or
available from problem structure. The inverse-positive condition is sufficient,
not asserted necessary for closed-form solvability. An equivalent older theorem
under optimal-design or diagonal-scaling terminology cannot be ruled out completely.
