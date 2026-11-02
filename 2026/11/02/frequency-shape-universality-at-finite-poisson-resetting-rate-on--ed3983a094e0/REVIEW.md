# Self-review

## Correctness — PASS

The anchored graph-Poisson problem has a unique solution because the connected Laplacian has a positive-definite grounded minor. Translation by this solution changes the constant drift to a drive localized at the reset vertex, preserving the coordinate-reset map exactly. This establishes equality of entire transition laws, not merely first moments. The synchronous-coupling estimate with the positive-definite matrix \(2\kappa L+\lambda P\) proves unique invariant probability and exponential Wasserstein convergence. Generator identities and a positive-definite Frobenius operator prove the covariance formula, with the exact two-vertex evaluation checked symbolically. The included checker tests rooted weighted graphs and reproduces a finite-rate Poisson diagnostic; analytical arguments establish the infinite-time claims.

## Originality — PASS with historical risk

The direct motivating source is Paramero-Arias--Riascos (arXiv:2610.21842v1, 2026), whose analytical grounded-Laplacian equations use infinite resetting rate. Its finite-rate nonlinear simulations do not imply the exact pathwise stationary law of the unwrapped finite-network linear system. Majumder--Acharya--Gupta (arXiv:2604.04769, 2026) handles finite-rate continuum mean-field order parameters, not this rooted finite graph. Majumder--Chattopadhyay--Gupta (arXiv:2402.14921, 2024) and Sarkar--Gupta (arXiv:2203.00339, 2022) address other mean-field/global reset settings; Bressloff (arXiv:2411.15534, 2024) has an external medium with a different reset map. The inspected literature and scientific search results yielded no equivalent or stronger covering statement. The 2024 subsystem-resetting article was not read in full, and unindexed general linear-hybrid results are a genuine remaining risk. Novelty is not certified by unsuccessful search alone.

## Mathematical value — PASS

The graph-Poisson conjugacy classifies the entire finite-time and stationary frequency-profile dependence of the singly reset linear model, not only a special-case invariant. The covariance is uniquely determined on any finite connected weighted graph, with a sharp exactly solvable two-node relative-phase variance; zero total drive causes complete elimination of resetting-induced stationary fluctuations. It supplies a reproducible finite-rate benchmark for a physically motivated stochastic pinning regime overlooked by an infinite-reset limit.

## Limitations

The real-valued linear flow is defined as an exact model in its own right. Random long reset gaps can invalidate a global linear approximation to an angular nonlinear Kuramoto process. No assertion about multi-vertex resetting, nonlinear global synchronization, independent auditing, or historical priority is made.

Self-review: passed. Independent audit: not yet performed.
