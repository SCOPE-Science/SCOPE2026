# Same-model review

## Correctness
PASS. The support-set/token-graph equivalence is exact, and for ordered triples the path-token distance is the coordinatewise \(\ell_1\) distance. The supplied 52 triples are checked pairwise. A complete binary optimization over all 286 vertices and all 2255 distance-at-most-two conflicts returns optimum 52 with zero MIP gap; published exact values through length 12 are independently reconstructed by the same definition.

## Originality
PASS. The 2017 source defines the general constant-weight adjacent-transposition invariant and solves weight two. The direct 2024 weight-three paper is exact only through length 12 and reports \(50\le\rho(F_3(P_{13}))\le54\), explicitly leaving exact values beyond 12 open. Current OEIS A085684 and targeted semantic searches did not expose the exact value 52. Residual risk remains for unindexed or unpublished computations.

## Value
PASS. Length 13 is the first missing case in the direct weight-three literature, and the published interval has four units of uncertainty. An exact optimum at this natural boundary is a meaningful finite classification rather than an arbitrary slice.

## Closest literature and limitations
The closest source is Ndjatchi et al. (2024), whose Table 4 brackets the same quantity between 50 and 54. The new claim closes that gap but does not classify all optimizers, give a closed-form upper-bound proof, or address length 14 and beyond.

Same-model review: passed. Independent audit: not yet performed.
