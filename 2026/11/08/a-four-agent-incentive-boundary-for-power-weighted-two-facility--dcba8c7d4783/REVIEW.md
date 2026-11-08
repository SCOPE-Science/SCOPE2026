# Scientific review: power-weighted two-facility lotteries

## Correctness — PASS

The analytic proof explicitly computes the indexed pair weights at the four-agent profile and reduces the gain from a deviation to one strict scalar inequality with positive denominators. The no-deviation statement holds for every report and every real exponent through two by convexity in the exponent and exact polynomial sign certificates; a fixed negative report yields strict improvement for every exponent at least three by monotonicity. At exponent three, the cubic sign pattern gives exactly the full interval of profitable reports. The extracted standard-library verifier checks 805 individual cost computations and 322 local best-response comparisons by rational arithmetic. The all-exponent statements are justified by proof, not by grids.

## Originality — PASS, with residual risks

Ma and Peng (arXiv:2608.09061) and Chan, Lin and Wang (arXiv:2608.22484) define equivalent linear-distance pair samplers and prove their strategyproofness, but their conclusions do not imply results for distance powers. The independently investigated inverse-square rule samples omitted agents for a different number of facilities. Indexed research search and inspected relevant sections did not identify this four-agent exponent-dependent exact cubic best-response classification. Unindexed power-weighted mechanism work is an originality risk. Related existing welfare analyses of the linear-distance lottery do not cover strategic misreporting under nonlinear sampling.

## Mathematical value — PASS

Power-weighting is a natural robustness test for a newly relevant strategyproof facility sampler: increased selection of distant pairs may improve spatial spread but can alter strategic incentives. This result quantifies a broad infinite region of incentive failure and a complementary verified local no-deviation range, identifying the entire cubic manipulation window rather than just an isolated counterexample. It is not a universal characterization of the exponent family, and it makes no claim for intermediate exponents.

## References and limits

The two main primary sources are https://arxiv.org/abs/2608.09061 (first public August 10, 2026) and https://arxiv.org/abs/2608.22484 (first public August 23, 2026). The original facility profiles and reduction concern indexed agents, so two collocated agents are distinct. No approximation guarantee for powered sampling or global classification for exponents between two and three is asserted. Independent validation has not taken place.

Self-review: passed. Independent audit: not yet performed.
