# Independent mathematical audit

## correctness

PASS

Any strict alternating two-cycle must move by one \(-\eta\) step and one \(+\eta\) step, so its two parameter values are \(a\) and \(a-\eta\). Solving the two linear momentum periodicity equations gives exactly the displayed \(m_A,m_B\). Substitution into the two sign inputs yields the open interval \(\beta_1\eta/(1+\beta_2)<a<(1-\beta_1/(1+\beta_2))\eta\), which is nonempty exactly when \(2\beta_1<1+\beta_2\). These equations also prove completeness of all strict alternating two-cycles. Inside a fixed sign sector the Jacobian is triangular with eigenvalues 1 and \(\beta_2\), so the two-step multipliers are 1 and \(\beta_2^2\). Completing the square gives the exact objective floor. The actual package verifier at blob e81365df5c15e47f3a16ab644a5ace6a2a7d6930 was inspected and checks representative cycles, margins, transverse contraction, and the default coefficients.

## originality

PASS

The defining Lion paper introduces the asymmetric two-coefficient sign/momentum recurrence and emphasizes the fixed update magnitude, while the later Lyapunov work gives convergence analysis in its stated regimes. Targeted full-text/record searches found no scalar-quadratic period-two classification, chattering band, or transverse Floquet multiplier. Current Resultary search for constant-step Lion cycles returned no matching published finding. The audited cycle family follows from a dedicated discrete periodicity analysis rather than from a published convergence theorem.

## value

PASS

The theorem isolates an exact nonconvergent constant-step regime of a widely used sign optimizer on the simplest strongly convex objective. The complete band, continuum of cycles, transverse multiplier and nonzero objective floor explain a concrete algorithmic boundary rather than an arbitrary numerical curiosity. This is a motivated structural dynamical result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
