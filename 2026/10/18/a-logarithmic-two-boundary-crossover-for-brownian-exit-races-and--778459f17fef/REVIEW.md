# Scientific review

## Correctness (C) — PASS

The domain and limit are explicit: for fixed \(d,D>0\), fixed \(\theta\), and \(N\to\infty\), each of \(N\) independent walkers begins at \(d\) and the reset boundary is at \(d(2+\theta/\log N)\). Absorbing-interval image expansions give exact one-particle first-exit probability fluxes. Their leading small-time terms establish both competing Poisson-scale intensities; the differentiated fluxes establish a normalized two-mark Gumbel density. The convergence in probability of each scaled episode duration to one, geometric tightness of the number of resets, and the renewal mean identity establish the restarted laws. A separate tail argument proves the necessary uniform integrability for the mean. The numerical code checks finite examples but does not infer infinite-population convergence from them.

## Originality (O) — PASS with residual risk

Biswas, Majumdar and Pal (2026, arXiv:2603.25338) formulate the same finite-population model and its exact renewal mean; their examined asymptotics do not cover a moving interval boundary approaching the midpoint on the inverse-logarithmic scale. Their 2025 precursor (arXiv:2504.13501) gives a general renewal framework and finite-population diffusion formula. Linn and Lawley (2021, arXiv:2110.11277) establish minority-target probabilities for fixed unequal target distances, with a hypothesis that fails to stay uniform as the two distances become equal. Krapivsky, Majumdar and Rosso (2010, arXiv:1004.5042) provide exact box-exit probabilities, not the joint near-balanced time/mark and restarted completion laws. The extensive direct claim comparison and relevant scientific literature searches identified no covering result; nevertheless a general marked extreme-value theorem or implicit derivation from exact finite-\(N\) formulae could subsume portions of the statement. No global uniqueness is claimed.

## Mathematical value (V) — PASS

The boundary separation \(d\theta/\log N\) is forced by the small-time Brownian action difference and determines a genuine nondegenerate target-selection transition. The result gives the corresponding logistic probabilities and joint timing law; most significantly, a continuous Gumbel single-episode fluctuation produces a discrete geometric limit for the completed restarted search. The limit for the mean also identifies the full leading coefficient missed by fixed-ratio limits. The outcome is a motivated structural classification for a current statistical-physics model, rather than a routine finite-\(N\) integral.

## Limits and nearest literature

No result is asserted for interacting walkers, finite-duration reset operations, or thresholds outside the prescribed scaling window. The earlier general renewal and fixed-ratio results are explicitly recognized, and their possible implicit overlap remains a residual scientific risk. Computational checks are finite and not an independent audit.

Self-review: passed. Independent audit: not yet performed.
