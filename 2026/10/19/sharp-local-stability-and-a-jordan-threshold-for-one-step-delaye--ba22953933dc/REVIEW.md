# Scientific assessment

## Correctness — PASS

The theorem concerns a precisely defined normalized rank-one two-state eigensolver with a simple leading eigenvalue. Differentiation in the leading-eigenvector hemisphere gives one independent quadratic companion polynomial per eigengap. Applying the exact quadratic Schur inequalities yields an iff local exponential-attraction interval. The spectral maximum gap is attained by a real eigendirection, making the converse sharp. At the optimal mixing fraction the critical companion matrix has a rank-one nilpotent perturbation of minus identity, from which the exact Jordan amplification follows for every integer time. The supplied standard-library checker passed 288 root configurations, 144 actual-map finite-difference derivative checks, and 100 boundary power/norm checks. Computations are corroborative, not proofs of the quantified theorem.

## Originality — PASS (self-review; remaining risks noted)

The motivating 2026 asynchronous Grassmannian eigensolver establishes sufficient small-stepsize convergence regimes but no necessary-and-sufficient two-component local stepsize region or optimum stale proportion. The earlier 2023 distributed PCA algorithm similarly provides sufficient rate bounds. General multistep stability and Schur–Cohn analysis already encompass the scalar recurrence once it has been constructed, so the polynomial test is **not** new. The finding is the eigenvector-algorithm-specific sharp reduction, full mixture/stepsize phase boundary, and exact boundary transient norm. Targeted current literature and mathematical-result searches yielded no directly dominating claim. Related works may still contain an equivalent specialized result in uninspected sections or elsewhere; no absolute uniqueness is asserted.

## Value — PASS

Fixed one-step gradient latency is a natural idealization of asynchronous distributed eigenspace computation. The sharp threshold is a meaningful design fact: assigning one quarter of the aggregate to a stale gradient doubles the strict local stepsize ceiling over the all-fresh method, while the same critical optimum has a nondecaying Jordan collision and linearly growing first-order perturbation sensitivity. These facts distinguish step-size feasibility from actual convergence speed and show why the boundary must not be used directly.

## Scope and residual limitations

Only local deterministic behavior, rank-one real-symmetric eigenspaces, two proportional components and an exactly one-step lag are classified. No global basin, universal asynchronous execution, finite-precision robustness, improved asymptotic rate or boundary nonlinear stability is proved. General linear-multistep theory and possibly uninspected related appendices remain the principal novelty-comparison risks. Independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
