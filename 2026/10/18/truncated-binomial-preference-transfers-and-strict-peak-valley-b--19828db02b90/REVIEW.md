# Scientific review: strict peak–valley preference ordering

## Correctness

**PASS.** The conditional law is an exact binomial on a terminal support interval determined by all intermediate parking-prefix constraints. No prefix constraint outside the chosen two-bin gap is altered when the sum of the two loads is fixed. The joint swap inequality follows from the symmetric binomial weights; the strict-peak minus strict-valley formula follows from comparing triples with equal endpoints. The all-size strict inequality uses an explicitly feasible and unmatched load pair, while the sum of the two probabilities follows from Pollak's cyclic correspondence for equality partitions. Endpoint cases and the interpretation of car indices versus space-value indices have been checked. `verify.py` passed 24269 exact assertions, including independent preference-word enumeration through size six and all conditioned occupancy-profile cases through size seven; those finite tests supplement rather than replace the general proof.

## Originality

**PASS on the inspected scientific evidence, subject to residual historical-priority risk.** Diaconis and Hicks, *Probabilizing Parking Functions* (arXiv:1611.09821), identify the nonequidistribution of **strict** peaks while proving equidistribution of **weak** peaks and species; this observation is not a new claim here. The new claim is the all-size direction \(p_n^+>p_n^0>p_n^-\) and exact signed moment, together with a structural conditional-binomial theorem for loads at any two preferred-space values. Kenyon–Yin (arXiv:2103.17180), Bellin (arXiv:2108.08661), and Yin (arXiv:2112.02251) contain related exact coordinate or asymptotic tools but not these conclusions in their inspected statements. Searches for identical occupancy transfers, equivalent inequalities and dominating results found no explicit prior theorem; older multivariate generating-function identities could still encode part of it implicitly. Independent priority checking is not claimed.

## Value

**PASS.** The distinction between strict and weak peaks in random parking preferences was singled out in a primary mathematical study. The theorem determines the direction of the strict inequality for **every** size, connects it to an exact signed third-order occupancy statistic, and proves a general distributional principle (truncated symmetric-binomial transfers between any earlier and later preference labels). The latter also yields stochastic ordering of the entire sequence of preference-space loads. This addresses a natural dependence question beyond the known single-coordinate marginal monotonicity, while acknowledging classical ballot/Pollak inputs and the absence of a sharp asymptotic gap formula.

## Limits and closest related literature

The model is classical uniform parking functions; the sharp asymptotic constant for the peak–valley gap is not established. Diaconis–Hicks (2016, Section 4) is the closest prior treatment of peak patterns. Kenyon–Yin (2021), Bellin (2021) and Yin (2021) give additional partial or broader-looking coordinate results, but a direct implication to the proposed inequality was not found in their inspected material. A self-review cannot certify universal historical priority.

Self-review: passed. Independent audit: not yet performed.
