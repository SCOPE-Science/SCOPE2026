# Self-review

## Correctness — PASS

The stationary Davies master equations give the displayed longitudinal and transverse Bloch components, their exact derivatives and the full-rank qubit SLD quantum Fisher information (QFI). Uniform Taylor expansion on the closed target Bloch ball proves that the coherence-square derivative is strictly positive for sufficiently small positive inverse temperature, so an optimizer must be pure. Along pure targets the limiting objective is a strictly concave quadratic with critical reset-to-bath ratio \(1/3\); its nondegenerate curvature and endpoint derivative justify exact finite-temperature optimality near that high-temperature boundary. The implicit-function theorem gives the positive transition slope \(8/27\). Rational arithmetic proves a finite-temperature coherent-state QFI witness larger than both diagonal extremizers. The self-contained `verify.py` passes 7,220 finite tests; numerical tests corroborate but never replace the analytic proof. The statement concerns estimation of inverse temperature, not unknown reset parameters.

## Originality — PASS (qualified best knowledge)

The principal full-text source, Li–Tong–Bao, arXiv:2610.31249v1, Supplemental Section III (equations S16–S24), solves the ground-reset steady-state Davies thermometry benchmark but does not optimize over coherent reset targets or identify a preparation phase transition. Its coherence-based metrology discussion is for frequency estimation, which is not the claimed QFI task. Frazão et al., arXiv:2405.14439v1, derive coherence-enhanced *transient* thermometry for freely relaxing initialized probes; that prior achievement does not give the stationary continuous-reset threshold, the finite-temperature calibration of the threshold, or the exact coherent reset witness. Altintas, arXiv:1602.06783v1, considers stationary phase-estimation QFI in a different two-qubit dephasing-reset model. Searches for aliases, Bloch-parametrized thermal-reset optimization, and related prior mathematical records did not identify dominating statements. A general QFI-target convexity/steady metrology theorem might subsume an element of the calculation. No priority certification is claimed.

## Value — PASS

Choosing a reset target is an operational resource that the initiating paper fixes at its ground-state benchmark. The result establishes when coherence must be supplied to obtain globally optimal high-temperature stationary thermometry, with a sharp and computable control threshold. An explicit finite-temperature witness demonstrates genuine improvement over *every* incoherent reset target at the same rate, not merely over one preparation. The critical-curve correction and iterated-limit qualification are useful to separate real protocol design from a singular large-temperature asymptotic.

## Scientific limits and residual risks

The bath thermalization rate diverges as inverse temperature tends to zero in the specified bosonic Davies model; physical realizability arbitrarily close to that boundary is not established. The target-state optimization is local in temperature near that limit at fixed reset rate, while the exact rational witness is one finite-temperature point. A mathematically broader and presently unidentified stationary qubit QFI optimization could contain the phase result. Independent evaluation and exhaustive priority screening have not been performed.

Self-review: passed. Independent audit: not yet performed.
