# Scientific review

## Correctness
**PASS — analytical proof reconstructed.** For all sequences of positive integer distances and positive redraw durations whose logarithmic ratio converges to a finite real number, the Mittag-Leffler integral implies the standard logistic weak limit of logarithmic jump rates. The walk is time-changed by cumulative jump intensity; Doob's maximal inequality makes a fixed number of subcritical blocks spatially negligible relative to the initial distance, whereas reflection and heat-kernel bounds force absorption in a negligible fraction of the first supercritical block. A logistic-continuity argument closes the transition band and proves the geometric law. The provided checker passed 40 numeric checks on the source's exact spectral formula. Numerical evidence is not a substitute for the argument.

## Originality
**PASS under the inspected scope, with priority risk.** Levit and Reuveni's 2026 paper and supplements already provide the rate law, exact first-passage spectral representation, and a fixed-distance mean limit, including a fair-coin heuristic at the extreme rate-parameter endpoint. Those statements are credited. This result treats the joint exponential-distance and refresh-time limit and identifies the full parameter-dependent geometric distribution, requiring a nonuniform probabilistic argument. The older doubly stochastic random-walk work concerns a different rate distribution and interval escape. The Mittag-Leffler representation itself is classical. Literature and mathematical-record searches found no exact full crossover theorem; a generic singular-rate homogenization or geometric escape theorem might still imply the conclusion.

## Mathematical value
**PASS.** The full first-passage law, not merely the mean, changes at the natural spatial diffusion clock \(x^2\) when the rate law has fluctuations exponential in inverse shape. The explicit success parameter unifies fixed-distance behavior with exponentially distant targets and exponentially varying refresh periods. It gives a quantitative crossover profile for extreme random intensities, rather than a routine fixed-parameter moment consequence.

## Scope and outstanding risks
The theorem proves weak convergence only, not mean or higher-moment convergence, and applies to symmetric nearest-neighbor jumps and independent Mittag-Leffler rate redraws. The continuous-time heat-kernel estimate is uniform in initial distance; the singular rate band is handled before the tolerance vanishes. Independent historical-priority and mathematical review have not been performed.

Self-review: passed. Independent audit: not yet performed.
