# Self-review

## Correctness: PASS

For all positive interval lengths, diffusion coefficients and reset rates, the claim is proved by reduction of cover time to an inclusion-exclusion of three first-hitting times of the *same* reset trajectory. Laplace-transform renewal identities recover an asymmetric mean formula already present in Linn and Lawley. A new hyperbolic rational change of variable reduces the continuum of candidate sites to an explicit quartic-in-disguise derivative polynomial whose only positive zero corresponds to a maximum, never an interior minimum. Exact endpoint comparison then proves the global switch and all equality cases. The center curvature identity proves the distinct local-shape threshold. The included verification program passed 7,159 deterministic comparisons. These computations provide corroboration, not an infinite proof.

## Originality: PASS, with material residual risk

The formula for the asymmetric reflected Brownian mean cover time was already given by Linn and Lawley (arXiv:2406.12154v2, equation 38), and the midpoint special case and reset-rate optimization were investigated by Ghosh and Sabhapandit (arXiv:2605.31207v1). Neither is claimed anew. The assessed finding is the all-site optimization classification, exact position-switch rate and earlier local-stability threshold, established with a global derivative sign argument; the cited texts discuss rate optimization, not these site bifurcations. Targeted literature and published-finding corpus checks found no same or stronger explicit site-design theorem. This is not a novelty proof: a full formula in prior art makes independent priority assessment especially important, and an unexamined equivalent site-optimization result would defeat the originality claim.

## Value: PASS

A reset-site design problem is a natural physical extension of the rate-optimization problem: in practice both starting/resetting position and clock intensity are choices. The result classifies *every* admissible reset position, rules out all off-center optima, and gives a closed algebraic jump point. The different local/global thresholds explain why a centrally placed reset point can be locally favorable yet still globally inferior. This adds a qualitative and quantitative parameter diagram, not merely a recomputed special-case mean.

## Boundaries and closest literature

The theorem is restricted to one-dimensional homogeneous reflected Brownian motion, deterministic coincident start/reset sites, retained visitation memory, and Poisson reset times. It neither generalizes the known mean formula nor jointly optimizes rate and position. The nearest full-text prior is Linn–Lawley Section 4.1, equation (38); the 2026 midpoint paper supplies the motivating fixed-site reset-rate benchmark. The original full-text formulas materially inform the result, so implicit prior coverage remains a nontrivial risk.

Self-review: passed. Independent audit: not yet performed.
