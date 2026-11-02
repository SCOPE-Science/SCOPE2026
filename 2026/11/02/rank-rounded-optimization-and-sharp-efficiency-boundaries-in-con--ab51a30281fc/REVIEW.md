# Scientific review: complete-bipartite average-distance swaps

## Correctness — PASS

The central pair-swap identity is obtained by explicit substitution of both agents' before/after averaged costs, with their mutual distance cancelling. It establishes strict increase of a fixed finite-state function without assuming regular degree. Each optimum is reconstructed from the gap decomposition of one-dimensional absolute distance: potential maximization and social-cost minimization reduce to distinct concave integer quadratics per prefix, and both rounded prefix paths are proved feasible. The exact \(K_{2,5}\) price-of-stability gap is verified against all seven type-pair classes, rather than a heuristic or a single run. Star bounds follow from median optimality and the triangle inequality. The standalone verifier corroborates all steps by finite enumeration; it is not substituted for the proof.

## Originality — PASS, with priority limits

The closest primary document is Bilò et al. (2023), *Schelling Games with Continuous Types*, https://arxiv.org/pdf/2305.06819. Its Proposition 3 proves finite improvement for regular networks, and Theorem 17 proves socially optimal equilibria on regular networks. Neither implies the nonregular complete-bipartite exact pair-swap identity, the two all-gap simultaneous rank-optimum constructions, or a \(K_{2,5}\) example with price of stability strictly above one. Binary-type Schelling articles (2021, 2024) employ different utility functions and hence do not dominate the stated continuous-distance result. Related indexed mathematical findings on complete bipartite graphs address different invariants. Equivalent specialized results in uninspected papers cannot be excluded; priority remains uncertain without independent assessment.

## Mathematical value — PASS

This is a structural theorem for a natural family of heterogeneous-degree networks. It both restores convergence beyond the paper's regular-degree positive class and gives comparison-optimal constructive algorithms for two distinct allocation objectives. The strict efficiency gap identifies a concrete boundary where convergence no longer implies an efficient equilibrium, while the star result quantifies the opposite possibility of optimal stable outcomes and extreme bad equilibria. These are motivated network/game properties, not isolated parameter arithmetic.

## Scope and residual risk

Only fully occupied unweighted bicliques, absolute real-type distances, and bilateral strictly improving swaps are covered; objective-specific rounded allocations must not be conflated. Publication priority is assessed against the inspected sources and bounded searches, not certified exhaustively. The scientific statements have not undergone independent audit.

Self-review: passed. Independent audit: not yet performed.
