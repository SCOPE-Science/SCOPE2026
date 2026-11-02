# Scientific review: Temporal interaction budgets and a reversible cooperative fold in a higher-order Prisoner's Dilemma

## Correctness — PASS

The inherited payoff expression in [1] reduces algebraically to equation (1). The proof verifies the exact logit transform, integrates it over a period, and handles the exceptional constant mean-critical schedule correctly. Time reflection and the odd variational derivative establish exact reciprocal multipliers and half-period fold shooting. The nondegenerate scalar return-map fold is proved using \(D_\mu=3P/2\), \(D_{ss}=-P/4\) and the implicit-function theorem; a direct second-order variation gives \(3\eta^2/(32\omega^2)\). Symmetry makes the next term order four. Signs away from zero and local concavity establish the exhaustive nearby orbit count. The independent-from-proof numerical checker `verify.py` passed all nine shooting settings and periodic budget/Floquet tests; it does not replace the analytic proof.

## Originality — PASS, with residual priority risk

Civilini et al. [1] derive the fixed-share bifurcation, not a nonautonomous forcing theorem. Babajanyan et al. [2] analyze a two-population pairwise game with rapidly varying payoffs, and He et al. [3] model temporal activity in spatial public-goods games. The closest accessible prior claim (periodic synergy in a two-state collective-risk model) has a different source equation and cannot imply this forced scalar fold. Relevant published-finding corpus and literature searches did not produce matching scalar interaction-budget, phase-zero shooting or reciprocal multiplier claims. This best-knowledge check is not a guarantee of exhaustive world priority; possible unindexed specialist papers remain a risk.

## Value — PASS

The exact interaction-budget equality shows why the constant-share threshold is not enough to sustain a time-dependent cooperative cycle. The sharp frequency-sensitive positive shift quantifies the extra three-person interaction share needed under seasonal forcing. The symmetry identity pairs stable and unstable seasonal solutions and gives an exact inverse multiplier relationship. The parameter slice is motivated by the source's own displayed payoff values and does not inflate a finite calculation into a general theory for arbitrary game payoffs.

## Limitations and provenance

This is a mathematical theorem for a deterministic one-dimensional well-mixed replicator with externally supplied positive periodic triadic share. It is not an assertion about finite random hypergraph realization, mutation, environmental feedback, stochastic fixation, or forcing of arbitrary amplitude. The local expansion is not uniform as forcing frequency vanishes. Priority remains contingent on unexamined specialist literature, and numerical verification is supplementary rather than a rigorous global certificate.

Closest literature: [1] arXiv:2303.11475v1 (2023-03-20), https://arxiv.org/html/2303.11475v1 ; [2] https://doi.org/10.1002/advs.202001995 ; [3] https://arxiv.org/abs/2401.11782 .

Self-review: passed. Independent audit: not yet performed.
