# Scientific review: two-color score and compensator

## Correctness

**PASS.** The finite-deck identity for the compensator follows from reversal of a uniformly shuffled balanced deck. The exact martingale variance follows from orthogonal conditional Bernoulli increments and the hypergeometric variance. A bridge invariance principle, a uniform fourth-moment bound and endpoint truncation justify second-moment convergence, rather than inferring it from weak convergence alone. The two Gaussian integrals for the weighted bridge absolute area are evaluated by explicit substitutions. The score's first two moments are independently established in Kuba–Panholzer (2023, Theorem 9). Exact arithmetic checks all balanced decks through multiplicity eight, supplementing the infinite proof.

## Originality

**PASS, qualified.** Dey–Manthripragada (2026, Proposition 1.4) provide the weighted Brownian-bridge weak limit, but not the evaluated second moment and resulting cross-covariance. Kuba–Panholzer (2023) provide total-score moments, not the predictable-compensator decomposition. A targeted published-finding corpus search over the specific constants, aliases and score–martingale covariance and web searches for weighted absolute Brownian-bridge moments returned no equivalent complete claim. These searches are evidence about recorded overlap, not a proof of uniqueness. A hidden special-function formula or uninspected appendix is a residual priority risk.

## Value

**PASS.** The martingale and predictable parts are both of variance order \(m\), yet their large negative covariance changes the final-score variance at the same order. The exact coefficient and correlation give a natural, interpretable benchmark for asymptotic score fluctuation decompositions; this is more informative than merely extracting a moment from a specified weak limit.

## Closest literature and limitations

The main comparison is Dey–Manthripragada, *Limit Theorems for the Complete Feedback Card Guessing Game*, arXiv:2610.17479v1, especially its Proposition 1.4 and discussion of the fixed-number-of-types regime. The second comparison is Kuba–Panholzer, *On Card Guessing with Two Types of Cards*, arXiv:2303.04609v1, especially Theorem 9. The computation is specific to two colors with equal counts and independent fair tie-breaking. Independent mathematical and priority audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
