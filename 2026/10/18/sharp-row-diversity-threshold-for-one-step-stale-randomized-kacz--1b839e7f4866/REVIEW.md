# Scientific review

## Correctness — PASS

The theorem explicitly fixes update semantics, independent probabilities, all initial pairs, and exact-arithmetic mean-square convergence. For each coordinate, the two-step augmented update has two explicit matrices; its covariance map preserves the positive semidefinite cone. A strictly positive definite comparison matrix \(W\) obeys two exact identities. Their sign gives a two-step strict contraction, a nonzero fixed covariance at equality, or an exponentially expanding covariance above the boundary. Decomposing \(W\) into two rank-one deterministic initial covariances proves that failure is witnessed by a deterministic initialization rather than an illicit randomized one. Exact rational code checks the identities; the universal result follows from the proof, not finite sampling.

## Originality — PASS with residual risk

Full text of the motivating randomized Kaczmarz experiment, of a classic asynchronous Kaczmarz sufficient-condition paper, of a related nonuniform asynchronous linear solver paper, and of a nearby published exact random-delay Gauss–Seidel result was compared with the new *self-stale, additive-correction* claim. The published random-delay Gauss–Seidel result instead overwrites a coordinate using the other coordinate's stale value, with a different recurrence. General jump-linear-system criteria include an implicit spectral-radius characterization, explicitly acknowledged; they do not state the derived sampling-diversity inequality or equal-global-collision/unequal-stability example. The relevant 2026 Carson–Ma article was checked only at the abstract level; a possible older exact special-case statement remains a scientific risk. The novelty claim is specifically about the explicit identity-Kaczmarz boundary, not the general covariance method.

## Value — PASS

The natural stability question is suggested by instability and row-sampling concentration in asynchronous Kaczmarz. The result provides an exact iff threshold and a practical benchmark for the number of orthogonal rows needed for stable overrelaxed stale updates. The exact equal-global-collision example shows why the total collision rate is an insufficient summary and why the largest row probability matters. It also sharply separates first-moment convergence from mean-square convergence. This is a structural, explicitly motivated classification, not an arbitrary numerical instance or a claimed general parallel-algorithm guarantee.

## Closest literature and limitations

Coleman's 2026 work motivates the stochastic row-update/staleness mechanism without proving this benchmark threshold. Liu–Wright–Sridhar (2014) supplies bounded-delay sufficient estimates, Jensen–Coleman–Sosonkina (2020/2021) supplies nonuniform asynchronous implementation evidence, and generic jump-system work supplies covariance/spectral tests. The exact public random-delay Gauss–Seidel work uses a different overwrite model. Only an identity system, i.i.d. choices, fixed one-commit staleness, and exact arithmetic are proved. General high-dimensional/nonlinear/adaptive or actual concurrency conclusions are not claimed; originality may be affected by inaccessible literature.

Self-review: passed. Independent audit: not yet performed.
