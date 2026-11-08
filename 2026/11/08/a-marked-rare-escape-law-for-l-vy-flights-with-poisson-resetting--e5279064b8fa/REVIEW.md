# Scientific review

## Correctness — PASS
The claim is the joint five-coordinate weak law for fixed Poisson rate and a symmetric stable flight on a widening interval. The proof makes an explicit one-jump approximation with a quantified small-jump maximal estimate, then uses an exact marked geometric renewal transform to derive the distinct macroscopic lifetime and microscopic successful-excursion clocks. The reset count follows from a stopped compensated Poisson martingale. All boundary assumptions and normalizations are explicit. Direct integrals, a Laplace identity, and a coarse-grid diagnostic were replayed in `CHECKER.py`; the simulation is not a proof.

## Originality — PASS, with priority qualification
Żbik and Palmowski (2026, arXiv:2610.20410) give large-interval MFPT asymptotics for this same model. Linn and Lawley (2023, arXiv:2302.05409) already imply the exponential lifetime marginal under general frequent resets, and their 2024 paper (arXiv:2404.01142) gives stable-flight exit-side probabilities. Högele and Pavlyukevich (2013, arXiv:1303.5031) give joint exit-time/location asymptotics for Lévy perturbations of deterministic attractors, with different dynamics. The inspected theorems do not present the whole five-coordinate marked limit under hard resets. The residual risk of a general unindexed marked-renewal or small-noise exit theorem is material; absent that overlap, the additional continuous overshoot and last-success mark dependence is not subsumed merely by separate marginals.

## Value — PASS
Exit location, overshoot distance, terminal age and number of unsuccessful attempts answer distinct physical questions that mean first-passage time and left/right probabilities cannot answer. The explicit Pareto law and full dependence structure distinguish a very fast final escape excursion from a long search composed of many failed excursions. The result has a natural complete domain and does not require arbitrary parameter restrictions beyond stable flights and a fixed relative interior start.

## Limits and comparison risks
The Gaussian endpoint, moving boundary starts, finite-interval error rates and non-Poisson resetting are not addressed. The 2013 heavy-tailed attractor paper was assessed from accessible summaries rather than its whole proof. The numerical diagnostic is discretized. An independent literature and proof audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
