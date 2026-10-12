# Review of the sharp random-step mean-square stability law

## Correctness — PASS

For every \(h\in(0,2)\), the update matrix has determinant one and nonreal unit-circle eigenvalues and preserves the explicitly reconstructed unique positive quadratic covariance form \(S_h\). The second-moment recurrence follows by multiplying out \(T(h)ST(h)^\top\), requiring moments only through order four. Brouwer normalization of the primal and dual positive covariance maps gives strictly positive right and left eigenmatrices. Determinant-root concavity forces the dominant eigenvalue to be at least one, and its equality case forces all steps to share the same invariant form, which can occur exactly for a constant law. The positive adjoint eigenmatrix then provides two-sided exponential bounds for each nonzero initial state. Simple-eigenvalue perturbation supplies the explicit quadratic small-noise coefficient. Exact-rational tests (107) checked the underlying calculations. The infinite-horizon theorem rests on the displayed analytic arguments, not on finite experiments.

## Originality — PASS, subject to priority risk

The defining Abdulle–Garegnani random-time-step study (arXiv:1801.01340, Sections 2 and 7; Theorem 6 and its hypotheses) gives symplecticity and conditional finite/polynomial-horizon energy control. It does not state an infinite-horizon independent-step mean-square dichotomy, the first-four-moments covariance matrix, or the sharp symmetric-noise coefficient. Richardson–Finn (arXiv:1108.0322, Section 2) shows resonance with deterministic periodic step modulation, not the stochastic all-nonconstant-law criterion. Arnold–Papanicolaou–Wihstutz (1986) analyzes a continuous randomly forced oscillator's almost-sure Lyapunov exponent. Sturman–Thiffeault (2018/2019) studies bounded generalized Lyapunov exponents for specified random shear products. Searches for equivalent stochastic moment laws, stronger random-matrix implications, exact tables, and duplicate published findings did not locate the combined statement. Absence from searched literature is not proof of absolute novelty; an unindexed derivation remains a live risk.

## Value — PASS

The result identifies a sharp design boundary for independent random-step geometric integration, showing that individual symplectic ellipticity and energy boundedness do not imply long-horizon mean-square stability. The exact transition is not a textbook deduction from fixed-step stability; it needs a positive-operator eigenmatrix argument and strict determinant concavity. The small-variance coefficient quantifies when moment growth emerges as the step distribution spreads, and the finite moment matrix makes the phenomenon assessable for arbitrary compactly supported iid laws. The theorem has a natural object, an exact classification, and operational relevance for assessing probabilistic integrators, without claiming wider almost-sure or high-dimensional implications.

## Closest literature and limitations

The strongest source-specific comparison is Abdulle–Garegnani's conditional time-limited Hamiltonian bound. Other comparisons concern deterministic resonance and random continuous oscillators; they are compatible, not direct proofs of this result. Scope is a single harmonic oscillator, iid steps supported strictly inside \((0,2)\), exact arithmetic, and mean-square trajectories. Specialized unindexed mathematics may preempt priority, and no independent review has occurred.

Self-review: passed. Independent audit: not yet performed.
