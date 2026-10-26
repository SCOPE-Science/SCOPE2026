# Self-review

## Correctness
**PASS.** The exact three-dimensional covariance lift reduces by node-exchange symmetry to a positive two-dimensional block. The Perron eigenvalue dominates the antisymmetric mode. Computing the unit-eigenvalue determinant gives a unique variance crossover at fixed timestep; the continuous moment generator gives the different, strictly larger exact-SDE threshold. The explicit mass-lumped two-node example is computed from a genuine Dirichlet mesh and independently checked against direct covariance matrix eigenvalues in 576 configurations. All quantifiers, endpoints, normalization and asymptotic ranges appear in RESULT.md. Tests corroborate, not replace, the analytic proof.

## Originality
**PASS, with disclosed risks.** Hearder, Le Bris and Djurdjevac's 2026 primary numerical scheme and prior stochastic-heat Lie–Trotter methods establish nonnegativity and finite-time moment behavior. The exact two-node asymptotic stability frontier, universal-step criterion and fixed-mesh stability reversal are not implied by the particular inspected finite-horizon results. published-finding corpus searches examined aliases (covariance eigenvalue, mean-square spectral radius, split-step heat stability) and returned only distinct claims. A possibly equivalent older general theorem or unavailable publisher article remains a specific risk, so this is not an assertion of absolute novelty.

## Mathematical value
**PASS.** A sharp parameter selection boundary and concrete geometric finite-element witness illuminate a real failure mode of an otherwise unconditional nonnegativity-preserving integrator. The narrow model is motivated by the two first interior finite-element nodes, and the difference between continuous-time and discrete-time long-horizon behavior matters for repeat stepping.

## Limits
Only the two-node symmetric linear semidiscrete stochastic heat system with independent nodal multiplicative noise and prescribed exponential splitting is treated. Almost-sure stability, arbitrary meshes and nonlinear SPDEs remain outside scope. Comparisons to the inaccessible 2022 full text are limited to its abstract. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
