# Scientific review

## Correctness — PASS

The unique nondegenerate parameter branch follows from three exact rational order equations. Substitution into the stage recurrence gives the claimed quadratic characteristic equation without approximation. Strict Schur inequalities establish the full open scalar stability interval. For nonpositive Chebyshev factor the recurrence is positive; for positive factor its two strictly positive, distinct characteristic roots yield the necessary-and-sufficient starting-ratio condition. The derivative of the smaller root and monotonicity of the exact exponential starter prove existence and uniqueness of the transcendental threshold. The root decomposition gives the exact first-negative index and its logarithmic asymptotic, while the first-stage expression proves sign loss before endpoint loss. A self-contained checker confirms rational identities and representative finite sequences; the proof, not numerical sampling, establishes all-index claims.

## Originality — PASS, subject to explicit residual risks

The motivating 2023 Chebyshev two-step method paper specifies stability polynomials, order equations, stage recursion, and absolute-stability intervals. Its relevant full-text discussion does not give an unshifted two-stage positivity cone or a threshold for exact-starter scalar decay. The 2011 strong-stability-preserving two-step Runge–Kutta paper studies general positivity/contractivity *guarantees* from monotone coefficients. The present scheme uses a negative historical-value coefficient and cannot invoke that guarantee; lack of an SSP guarantee does not determine an exact-starter frontier. Related results on positivity and delayed sign changes of **other** numerical recurrences do not cover these specific coefficients and starter. Mathematical-record searches did not locate a stronger formula containing the complete present result. General second-order recurrence methods are classical, so unindexed applications of those methods to this same scheme remain a residual risk. No exhaustive publication-uniqueness claim is made.

## Value — PASS

The work addresses a natural question for stabilized explicit integrators applied to positive parabolic or decay problems: how much of an enlarged *absolute-stability interval* can be used without violating positivity? The result does not just state that a negative coefficient makes monotonicity uncertain. It provides a complete initial-positive-state cone, the unique sharp exact-starter endpoint cutoff, a logarithmic first-failure law, and a distinct earlier internal-stage obstruction. The comparison is important for implementations with positivity-restricted nonlinear evaluations or physical state constraints. Its scope is small but the invariant and cutoff are complete and mathematically motivated.

## Closest literature and limits

Moisa and Faleichik, *Second order stabilized two-step Runge–Kutta methods*, arXiv:2303.16267 (2023); Ketcheson, Gottlieb, and Macdonald, *Strong stability preserving two-step Runge–Kutta methods*, arXiv:1106.3626 (2011). The result concerns one exact unshifted two-stage branch, exact scalar dynamics, fixed steps, and positive starts. It does not assert SSP, preservation on arbitrary matrices, or statements about the paper's separate small-damping numerical parameter selections. Other general recurrence-positivity treatments could imply part of this boundary after specialization; none identified covered the entire method-specific claim.

Self-review: passed. Independent audit: not yet performed.
