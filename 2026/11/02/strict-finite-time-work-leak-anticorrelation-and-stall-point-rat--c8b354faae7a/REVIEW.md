# Self-review

## Correctness — PASS

The claim explicitly fixes a strictly positive seven-rate three-state Markov generator, the parallel cold/hot channel decomposition, the exact aggregate stall condition, stationary initialization, signed event orientations and every real observation duration \(t>0\). The generator's invariant distribution and the two-derivative current-count kernel are reconstructed directly. The two nonzero relaxation eigenvalues are real negative by aggregate detailed balance. The kernel's one-zero property and positive total integral give a strict all-time proof for the integrated mixed covariance; finite experiments are not used as an infinite proof. An independent two-field tilted-generator calculation checks the asymptotic variance and mixed cumulant. The algebraic inversion is unique and respects positive channel-rate constraints. The packaged standalone checker passed symbolic identities and 125 physically admissible finite-time matrix-exponential comparisons.

## Originality — PASS (qualified best-knowledge)

The 2026 Prataviera–de Oliveira primary manuscript defines the identical three-state rate engine, solves its stationary means and hot-leak reversal threshold, and studies spectral filtering, but does not give the two-field counting covariance, its strict all-duration sign, or the bath-rate inverse. Sánchez, Sothmann, Jordan and Büttiker (2013) provide related noise analysis for a distinct four-state coupled quantum-dot device and a different tight-coupled current relation. Existing general full-counting-statistics and stalling fluctuation–dissipation methods are credited. Searches of published mathematical findings, relevant primary literature and accessible prior claim records did not reveal a directly covering special case. A broader unlocated theorem might nevertheless imply the sign and reconstruction; novelty has not been independently certified.

## Value — PASS

The source's mean work current vanishes precisely at a point where a hot-to-cold leak may persist. The theorem gives a strict finite-observation-time negative **cross-noise** law even though the instantaneous correlation kernel can change sign. Two low-order net-current statistics then identify both microscopic leakage directions from known aggregate kinetics, including a case in which the mean leak alone cannot determine their sum. This is a motivated structural noise signature and exact identifiability result, not a bare sign/numerical exercise.

## Closest literature and limits

The source's stationary current and engine reversal are prior results, not new claims. The earlier four-state heat/charge noise work and stalling response literature do not share this three-state parallel-channel count model. Residual risk is broader implicit coverage of the exact covariance by a general marked-network theorem. No claim is made for explicit quantum filters, nonstationary initialization, off-stall rates, microscopic battery energy or finite-sample statistical confidence.

Self-review: passed. Independent audit: not yet performed.
