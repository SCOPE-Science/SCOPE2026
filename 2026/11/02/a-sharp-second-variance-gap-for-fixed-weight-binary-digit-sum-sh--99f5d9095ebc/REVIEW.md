# Scientific review

## Correctness — PASS

The carry process has a geometric tail and finite second moment. The conditional carry covariance is exactly \(2^{-(j-i)}q_i(1-q_i)\); summing it gives the closed second moment. Strict monotonicity of the pair energy in each inter-one gap, followed by exact crossing-pair summation for a single inserted zero, proves the minimum, the second-minimum gap, and equality cases for all \(k\ge2\). Exact recursion and binary-support checks corroborate this proof.

## Originality — PASS, with historical-priority risk

The closest direct precursor is Spiegelhofer and Wallner's 2023 second-cumulant recurrence; it gives values for individual shifts but no inspected sharp next-to-minimum fixed-weight variance law. Tarłowski 2026 Theorem 21 gives sharp bounds at **fixed tree-word length or block count**, and its first-minimum specialization covers the familiar consecutive-block minimum. That **known first minimum is not counted as new**. The substantive present result is the entire pair-energy expression together with the precise *second* variance level and its rigid equality patterns, not the existence of a variance or a routine recursion. Cheng 2026 optimizes a different statistic (the sign bias) at fixed Hamming weight. Sobolewski–Spiegelhofer 2025/2026 decomposes measures and discusses few-block shapes. Targeted searches of relevant mathematical literature and mathematical research records found no statement that implies the second-level rigidity without additional argument. An unlocated earlier general extremal theorem remains a residual risk.

## Mathematical value — PASS

The fixed-Hamming-weight variance is a natural scale parameter in Gaussian/Edgeworth approximations for digit-sum correlations. At exactly that constraint, separating a single pair of ones by even one zero enforces an explicit positive, order-one variance increment independent of the ambient bit length. This is a uniform arithmetic rigidity statement, distinguishes the two lowest possible variance levels, classifies all equality patterns, and makes the entire variance computable from the positions of the one-bits. It is not a new sign-bias theorem or a mere numerical sample.

## Limits

No new pointwise sign-bias estimate, higher-moment theorem, or independent novelty certification is claimed. The known cumulant recursion is stronger for computing individual values; the new contribution is its exact constrained second-level extremal consequence and proof of rigidity.

Self-review: passed. Independent audit: not yet performed.
