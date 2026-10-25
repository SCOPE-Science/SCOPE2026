# Scientific review: two-generation Poisson outbreak-tail ordering

## Correctness

**PASS.** The claim precisely defines independent Poisson first and second generation reproduction and counts new cases, not the index case. Conditional probability generating functions give the exact distribution, moments and strict generating-function order. The two-sided logarithmic tail bound uses a finite exponential moment for an upper Chernoff estimate and an explicit positive-probability event with Stirling's formula for the matching lower bound; it does not extrapolate from a finite enumeration. A standard-library implementation compares independent coefficient computations at four parameter pairs and reports 646 passed numerical checks. The argument proves an eventual tail reversal for all positive parameter pairs with strictly ordered means; it does not produce a uniform finite reversal threshold.

## Originality

**PASS under the examined literature, with residual priority risk.** The motivating work of Boudreau et al. (2023) supplies the generation-dependent branching PGF framework and observes that metrics can rank interventions differently, but its full-text Sections 2–5 treat different vaccination schedules and do not give the all-parameter two-epoch rate-swap tail comparison or the coefficient \(\log(b/a)\). Classical Neyman type-A and compound-Poisson papers address cluster distributions or quantile asymptotics rather than this exact time-swapping theorem. Accessible research-record searches did not identify an equivalent statement or a broader theorem explicitly dominating the whole claim. Zheng's closely relevant 1995 tail-asymptotics paper was accessible only in abstract, leaving a meaningful risk that more general probability-tail theory contains part of the logarithmic lemma.

## Value

**PASS.** This is a motivated structural difference between mean control and catastrophic-tail control in a generational epidemic intervention framework: swapping the same two reproduction intensities changes the extreme-tail exponential factor by \((b/a)^n\) on the log scale, although the early-suppression schedule wins in expectation and generating-function order. It supplies an exact analytic benchmark for calibrating risk-sensitive early-outbreak policy comparisons. The result applies to infinite-reservoir two-generation Poisson branching, and does not itself establish real-world policy recommendations or finite-network tail claims.

Self-review: passed. Independent audit: not yet performed.
