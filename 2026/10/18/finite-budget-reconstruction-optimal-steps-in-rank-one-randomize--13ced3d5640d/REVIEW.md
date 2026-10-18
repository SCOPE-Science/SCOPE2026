# Self-review

## Correctness — PASS
The starting update is the source's randomized block-coordinate gradient update restricted to the one-row all-ones operator. The measurement residual evolves deterministically; exact sample independence converts the iterate's covariance into a weighted multinomial covariance. The exact bias–variance identity and a sharp Cauchy–Schwarz minimization over all real total weights establish both the global lower bound and the unique attainable step schedule. Requiring zero terminal residual forces total effective weight one and produces the separate sharp constrained optimum. The constant-step expression and its sign boundary are direct verified substitutions. Exhaustive rational enumerations are corroborative, not substitutes for general proof.

## Originality — PASS, with residual risk
The original 2024 randomized block-coordinate inverse-problem paper establishes the method and convergence properties, including an explicit full-column-rank structural assumption in its minimum-norm strong convergence theorem. The 2015 randomized Gauss–Seidel paper already shows that ordinary coordinate descent may fail to recover the least-norm solution; this known qualitative fact is not claimed as new. Neither inspected source gives the unique finite-budget deterministic schedule, its exact nonzero terminal residual, the sharp uniform-sampling reconstruction risk, or the constant-step monotonicity boundary. Targeted mathematical-record queries and comparisons against accessible prior claims disclosed no result implying this whole theorem. Equivalent implicit-regularization or optimal-weight formulations in broader stochastic-approximation literature remain a residual risk.

## Value — PASS
For an underdetermined system with a continuum of exact solutions, minimizing observation residual is not equivalent to minimizing reconstruction error. The theorem supplies an exact and operationally feasible budget-aware design rule, showing that the optimal finite-budget schedule remains strictly within conservative step bounds and deliberately does not interpolate noiseless data. The comparison with constant-step floor quantifies why residual convergence alone is an inadequate measure of minimum-norm reconstruction quality. The full classification is limited to the natural identical-block benchmark, not advertised as a general inverse-problem algorithm.

## Scientific limitations
Only independent uniform coordinate choices, deterministic steps, identical observation coefficients, the Euclidean minimum-norm target and exact arithmetic are covered. Any equivalent earlier result in broader optimal stochastic sampling theory would require reassessment. Independent validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
