# Scientific review of the two-site hard-deadline survey theorem

## Correctness — PASS

The mathematical claim concerns exactly two independent potentially occupied sites, exponentially distributed active-time detections, and a fixed ordered one-switch policy with a hard realized deadline. Conditioning on first-site occupancy and detection time gives the expected missed-site count, including the mass of an absent site. Direct differentiation produces a strictly decreasing conditional hazard versus a strictly increasing discounted terminal detection intensity, giving the exact unique minimum for every finite horizon. The root identity supplies the large-deadline expansion. Separating the lower-order occupied-first contributions yields the leading missing-detection coefficients and exact ratio. Strict short-horizon order follows from early detection freeing time at the second site; the long-horizon order follows from the leading coefficient. The witness uses only exact integer comparisons. `verify.py` independently checks integration, derivatives, caps, and asymptotic constants, but finite tests are not the infinite proof.

## Originality — PASS within checked evidence, with residual historical risk

Guillera-Arroita, Hauser and McCarthy (2014), https://doi.org/10.1002/ece3.1056, use the same exponential removal-detection mechanism but constrain **expected** survey expenditure, optimize sitewise effort and do not derive order or actual-deadline time recycling. The earlier Hauser–McCarthy (2009) nonremoval formulation, https://doi.org/10.1111/j.1461-0248.2009.01323.x, cannot directly imply the stopped-survey cap loss. Brown (1980), https://doi.org/10.1287/opre.28.6.1275, concerns a single moving target rather than potentially occupied independent sites with additive rewards. Database and literature queries for two-site hard budgets, defective exponential search and log-absence priority yielded no exact match. The 2009 full text was not accessed; generic search/scheduling literature could contain an equivalent statement under other terminology. Search failure is not a uniqueness proof, and priority remains provisional.

## Value — PASS

The gap is motivated by a concrete limitation in the 2014 surveillance model: actual expenditure can deviate from an expectation-based budget. A single crew with a hard cutoff and time released on detection presents a different and natural allocation problem. The theorem provides a complete cap rule for every two-site parameter tuple and a non-obvious change of the optimal ordering index across budget scales. The exact counterexample proves that no fixed ranking by initial detection intensity is reliable for both short and long horizons. The conclusion is a transparent reference benchmark, not an empirical management recommendation or a claim about arbitrarily adaptive controls.

## Scope and outstanding risks

The policy class excludes return visits, travel time, false positives, correlated occupancy and more than two sites. The theorem does not assert a unique finite crossover, and the limiting order index only decides strict comparisons when the two values differ. Independent scientific audit and independent field-data validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
