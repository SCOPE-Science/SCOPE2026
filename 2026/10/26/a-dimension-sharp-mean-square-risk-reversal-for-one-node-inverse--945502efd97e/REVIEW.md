# Scientific review

## Correctness — PASS

The theorem uses precisely specified real-Haar sphere sampling and known spectral endpoints. The beta moments are derived from spherical invariance; the two one-matvec formulas and unbiased interpolant are exact. An absolutely convergent geometric-series expansion gives exact mean-square difference coefficients. Their one-step difference has a strict sign for every dimension at least four. Dimension two is handled by an explicit integral, and in dimension three a one-sign-change coefficient argument proves a unique risk crossing. Bounded convergence establishes the singular limit without extending finite tests to an infinite theorem. The standalone verification script passed 18,835 deterministic checks; the proof, not these checks, certifies universal quantifiers.

## Originality — PASS, with residual risks

The 2022 primary source constructs general spectral measures, polynomial approximation rules and Gaussian/Lanczos quadrature and proves generic stochastic bounds; the 2017 foundational inverse-trace SLQ paper provides general approximation error bounds. Neither inspected mathematical treatment states the present exact mean-square comparison of a one-node inverse Gaussian rule with an endpoint-interpolatory one-matvec rule on rank-one two-level spectra. The new content is the global dimension-four risk threshold, unique dimension-three crossing, and dimension-two reversal. Direct searches for beta/Rayleigh inverse-trace risk and exact interpolation versus SLQ found no covering result; searches do not establish absolute novelty. The 2017 source was inspected through its accessible author full-text rendering rather than through a successfully downloaded PDF; this and possible unindexed special-case calculations are residual publication-priority risks.

## Value — PASS, with scope restriction

SLQ and polynomial spectral quadrature are frequently contrasted by approximation order and asymptotic sample bounds. In a one-matvec model the finite-budget statistical risk can reverse despite the interpolatory estimate being unbiased and spectrally exact. The sharp dimension dependence resolves a natural experimental benchmark for the bias–variance tradeoff and gives a non-asymptotic test case for implementations. The endpoint baseline requires exact endpoint information; this special spectrum has analytically known trace if its multiplicities are supplied, so the result is a method-comparison benchmark rather than an assertion of practical algorithmic superiority. It does not claim relevance to every spectrum, probe ensemble or function.

Self-review: passed. Independent audit: not yet performed.
