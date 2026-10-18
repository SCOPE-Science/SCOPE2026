# Review of a sharp mean-step reversal for adaptive Euler--Maruyama

## Correctness: PASS

The conditional Gaussian second-moment equation, its exact algebraic decomposition, the monotone-covariance inequality, and uniform moment-drift arguments collectively support the theorem for every stated parameter. Strictness follows from full support. The Gaussian perturbation calculation yields the opposite sign above the threshold. `verify.py` ran 2004 exact-algebra and deterministic-kernel checks; the infinite-dimensional parameter quantifiers rest on the proof, not the tests.

## Originality: PASS (with bibliographic risk)

Wen--Huang--Li (2026) already establish the adaptive Euler chain and numerical invariant measure. Leroy--Leimkuhler--Latz--Higham (2024) already expose the uncorrected time-rescaling bias and develop a different corrected method; their Eq. (2.10) gives the same uncorrected kernel family. Neither examined primary text was found to state or dominate the sharp *fixed-at-the-invariant-mean-step* OU variance comparison, its two-defect identity, and its sign reversal. Indexed Gaussian stationary-bias results address other samplers. Basic stationarity algebra and Gaussian integration are acknowledged background. Unindexed special-case overlap remains possible.

## Value: PASS

The mean step is an equal-evaluation-rate comparator in adaptive integration. The sharp threshold separates an exact no-benefit regime from an explicit benefit regime for radially decreasing step policies, while its two nonnegative mechanisms diagnose the contribution of mesh-point residence bias and variance in step lengths. A sign reversal is more informative than a generic statement that time rescaling changes the invariant measure.

## Scope and limits

Scalar quadratic dynamics, continuous even radially nonincreasing steps, bounded away from zero, with maximum strictly below the Euler stability bound. Physical-time sampling, integrated autocorrelation, total simulation runtime, and general potentials are excluded. The high-step perturbative witnesses need not obey all sufficient assumptions in the motivating paper, but use its Euler update. Full-text assessment of all possible earlier specialized calculations and independent external audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.
