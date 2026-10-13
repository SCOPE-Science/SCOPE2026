# Self-review

## Correctness
PASS. The counterexample uses IID \(\operatorname{Exp}(1)\) observations, hence a valid \(\alpha\)-mixing sample, the Gaussian order-two kernel, \(\beta=1/2\), and \(b_n=n^{-1/2}\), which satisfies the source's bandwidth conditions. The target entropy tends to \(\log4\). For every realized sample, the estimator has a finite tail limit \(L_n\). At an all-equal deterministic sample location tending to infinity, that limit tends to \(\log\sqrt{8\pi/n}\), which cannot equal \(\log4\) for integer \(n\). Continuity gives a positive-probability sample neighborhood with a nonzero limiting error, forcing the time-integrated squared error, and hence its expectation, to be infinite.

## Originality
PASS. Searches for the exact theorem, exact article/DOI, generalized-past-entropy MISE, integrated quadratic-mean consistency, kernel-estimator tail behavior, and corrections/corrigenda found the target theorem but no published correction or equivalent Gaussian-tail counterexample. The most relevant earlier paper is the 2014 censored-dependent-data estimator paper; only abstract/metadata were accessible, so equivalence hidden in that full text remains a residual risk rather than evidence of coverage.

## Value
PASS. The finding distinguishes compact-time consistency from global Lebesgue-time integrated consistency and shows that the latter can fail maximally: its MISE is infinite for every sample size under a natural IID exponential model and the same Gaussian kernel family used by the source. It also explains why pointwise MSE convergence cannot be integrated over an infinite time domain without a domination or finite-measure condition.

## Closest literature and limitations
The 2025/2026 source itself is the closest literature because Theorem 3.3 is the statement being tested. The 2014 generalized-past-entropy estimator paper is structurally related but its accessible abstract does not expose this claim. The result does not settle corrected theorems on compact intervals or under integrable time weights.

Self-review: passed. Independent audit: not yet performed.
