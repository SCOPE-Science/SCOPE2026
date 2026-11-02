# Scientific review

## Correctness — PASS

The stochastic domination in the bipartite case follows from projecting each edge draw onto its endpoint in the larger part and proving pairwise-balancing optimality of ordinary coupon probabilities. An explicit no-isolate, matching-saturating construction attains the bound simultaneously for all deadlines, and the equality case at the first feasible deadline forces exactly a uniform perfect matching on balanced bipartite graphs. On odd cycles, the first-deadline count is an exhaustive matching-complement bijection; late domination follows from a strictly smaller vertex sampling hazard for any nonuniform law and an explicit union bound for the uniform law. Boundary conditions, quantifiers, and the strict inequality for every odd cycle of size at least seven were checked. The included exact-rational checker passes 864 assertions; it corroborates but is not used as a substitute for the proofs.

## Originality — PASS (qualified)

The closest comparison is to the generalized coupon-collector literature on group drawings and their optimization. Schilling–Henze (2021) concerns limit laws, Betken–Thäle (2022) uniform group-draw approximations, and the fully inspected Berend–Sher (2025) results identify expected-time advantages of nonuniform package distributions; these do not imply the exact bipartite all-deadline optimum together with absence of a universal fixed law on odd cycles. The classical uniform single-coupon stochastic order and the decomposition coupon distribution are credited, not asserted as original. A potentially relevant earlier optimization article by Schilling (2021) was not fully accessible; its detailed historical coverage is unresolved. Claim- and alias-based comparisons with indexed results and related mathematical claims did not find a dominating theorem, but they do not certify uniqueness or priority.

## Value — PASS

The object is a canonical graph-constrained group coupon collector: each sampled edge simultaneously covers its endpoints. The result answers a natural stronger design question, whether one fixed sampling rule can optimize every deadline rather than only mean time. The bipartite answer is exact on an infinite graph class and includes all optimizers for balanced instances, while the odd-cycle obstruction shows a genuine conflict between immediate and eventual completion. This is a structural parity phenomenon, not a routine improvement in a known scalar bound.

## Closest literature and boundaries

Schilling and Henze, *Two Poisson limit theorems...* (2021), DOI 10.1017/jpr.2021.15; Betken and Thäle, arXiv:2202.07485 (2022); Berend and Sher, arXiv:2509.17201 (2025); and Schilling, DOI 10.1016/j.ipl.2021.106112 (2021). The theorem is restricted to fixed independent edge draws and deliberately does not classify odd cycles of length three or five, all graph families, or adaptive policies. Full historical priority has not been independently established.

Self-review: passed. Independent audit: not yet performed.
