# Scientific review

## Correctness — PASS

The argument starts from the exact Borda-score permutation vector, uses committee top-score inequalities, and reduces the extremum to a weighted rearrangement. The complementary-party substitution gives the lower bound. Explicit cyclic permutations realize both rational endpoints; rational mixtures realize the entire rational interval; pairwise score inequalities make strict mixtures uniquely winning. Edge cases of empty middle blocks, full committees, no first-party winner, and all first-party candidates elected are addressed. The standalone `verify.py` passed 304959 exact assertions, including all feasible endpoint constructions up to twelve candidates and the 51-voter example. The infinite quantifiers rest on the proof rather than enumeration.

## Originality — PASS with priority caveat

The primary 2026 article defines the party scoring statistic and analyzes OWA rules mostly empirically, without a seat-conditioned feasible interval. A same-authors article on spoiler effects uses Borda party totals with separate apportionment methods. Darmann–Klamler addresses fairness of item allocations, not selection of the highest-scoring candidates. The fully inspected 2017 threshold-of-exclusion article studies cohesive voting-bloc fractions rather than extrema of an affiliated party’s total normalized candidate points conditional on its candidate count and seat count. Published research comparisons found no equivalent implication, but this is not a definitive priority certification; the item-allocation paper was only partially inspected. Classical Borda scoring and rearrangement are fully acknowledged.

## Value — PASS

The full interval is a natural inverse question for a new allocation-proportionality statistic: knowing a party's candidate count and seats, exactly how far can its alleged vote share differ? The answer is a complete, sharp all-size classification, not a sample or a one-off counterexample. The zero-seat high-score corollary exposes a structural candidate-cardinality sensitivity of the measure, relevant to interpreting party score–seat mismatch. The scope is deliberately limited to separable Borda rather than all OWA rules.

## Closest literature and limitations

Boratyn–Stolicki, arXiv:2602.10083, Sections 4–7, is the closest source. Related discussions are Boratyn et al., DOI:10.3233/FAIA251258; Darmann–Klamler, DOI:10.1007/s00355-016-0982-z; and Grofman–Feld–Fraenkel, DOI:10.1016/j.mathsocsci.2016.11.004 (full author-hosted paper inspected). No claim is made about first-choice party votes, other OWA rules, or independence of the review.

Self-review: passed. Independent audit: not yet performed.
