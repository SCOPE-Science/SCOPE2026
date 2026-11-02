# Scientific review: sharp payoff-blindness threshold

## Correctness — PASS

The payoff identity follows from summing shared-pool benefits over all closed-neighborhood groups, with one cost charged per cooperator per group. Every edgewise optimization is a linear functional of the free binary strategies; the proof attains both endpoints and verifies \(a_{xy}\ge0\), so the max-absolute formula does not rely on unproved relaxation. Square-torus stencil multiplicities are shown and independently recomputed by exact rational code. The strict cutoff rule explains why equality is not neutral. The voter fixation statement follows from an explicit bounded martingale and absorption on finite connected graphs. The tests corroborate but do not replace the uniform proof.

## Originality — PASS with priority caveat

Javarone and Singh (2023, arXiv:2310.15096v1) introduce payoff-difference thresholding and simulate the square lattice, but do not derive the graph-local exact cutoff or the sharp \(11\)-contrast torus value. The 2013 review provides the standard shared-pool accumulated-payoff rule, not the neutrality threshold. Takiguchi and Nemoto (2024 journal; 2026 preprint) use an **unthresholded** model and derive an asymptotic voter limit for large noise, so that result does not imply a sharp exact fixed-cutoff condition at finite noise. The classical voter fixation probability is credited and is not presented as independently original. Relevant indexed findings on evolutionary games and past work were checked at claim level; none of the recoverable claims covered this threshold. A hidden equivalent calculation remains possible.

## Value — PASS

The exact transition delineates where a payoff-tolerance mechanism completely ceases to implement selection for **any initial profile**, providing a state-independent calibration criterion rather than a simulation-specific estimate. It isolates the effect of overlapping group geometry (a square torus and a clique with the same degree have different thresholds) and remains valid at fixed, finite imitation noise. The extremal local stencil is small but the theorem applies to arbitrary network size and all binary configurations, with a general regular-graph formula; its precision is relevant to distinguishing an actual neutral regime from a merely weak-selection regime.

## Scope and risks

The full theorem presupposes standard shared-pot benefits rather than a literal reading of ambiguous defector-count notation in one printed 2023 formula. The threshold is fixed, not dynamically estimated. No claim is made about below-threshold long-run behavior. Priority searches can miss equivalent formulations, especially work not indexed under payoff tolerance. The proof has not undergone independent audit.

Self-review: passed. Independent audit: not yet performed.
