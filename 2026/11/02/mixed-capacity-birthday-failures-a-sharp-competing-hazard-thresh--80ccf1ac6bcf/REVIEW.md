# Scientific review

## Correctness (PASS)

The finite formulas follow from multinomial weights and occupancy truncation. Independent Poisson streams produce exact classwise Gamma waiting-time distributions. The expansions yield the critical mixed hazard and the full negligible/critical/dominant single-capacity regimes, while a maximal inequality transfers time-and-mark convergence to discrete arrivals. The uniqueness of the class-balance parameter follows from a strict monotone coupling. The standalone checker passes 2,183 deterministic assertions against two independent finite constructions. The rate assertion is limited to Poissonized log survival; it is not extended without proof.

## Originality (PASS, historically qualified)

The primary comparison is Gouet–Hitczenko–Wesołowski, arXiv:1905.06663, which assumes the same capacity for all urns, including in its Poisson theorem. Arratia–Garibaldi–Kilian, arXiv:1310.7055, considers a fixed collision criterion; Henze, doi:10.1016/S0167-7152(98)00076-5, similarly treats one fixed occupancy threshold. The distinct contribution assessed here is the mixed-capacity first-failure trichotomy with a joint capacity mark, exact finite joint law, and sharp critical minority scaling. No matching or implication-equivalent published statement was identified in the searches performed. Broad classical occupancy Poisson approximation could yield an alternative proof of some limits, so unlocated priority and general-theorem subsumption remain real risks; a failed search does not certify novelty.

## Value (PASS)

Uniform destination choice with heterogeneous capacities is a natural overflow-reliability model. The theorem determines the sharp size at which a sparse population of weaker bins controls system failure, resolves the full crossover rather than a single mean, and quantifies which class is responsible for first failure. The invariant is natural for dimensioning systems with small underprovisioned minorities; the critical minority exponent and balance constant are not arbitrary parameter slices. This is a focused exact asymptotic classification, not a claimed general hashing-performance theorem.

## Limits

Only capacity-one and capacity-two bins, uniform independent routing and first failure are covered. The numerical root is approximate. The related 1998 paper was available only through bibliographic/abstract material. Historical priority needs independent checking.

Self-review: passed. Independent audit: not yet performed.
