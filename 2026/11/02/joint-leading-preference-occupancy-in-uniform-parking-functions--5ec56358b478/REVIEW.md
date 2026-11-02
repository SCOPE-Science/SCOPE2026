# Review: Joint leading-preference occupancy in uniform parking functions

## Correctness — PASS
The all-size proof fixes the positions requesting 1, reduces the remaining preferences by the capped shift, and counts the fiber with the established one-value enumerator. The resulting factorized conditional PGF proves the Bernoulli-plus-binomial law, strict stochastic regression and the exact covariance, including \(k=n\). Finite verification using both word enumeration and multinomial occupancy enumeration produced `VERIFY_OK 5026`. The finite checks are corroboration, not a substitute for the proof.

## Originality — PASS (qualified)
The one-value identity, one-variable Poisson limit and parking-function cardinality are prior work. Relevant material was inspected in Gessel–Seo (2005, Section 10), Diaconis–Hicks (2016, Sections 2–3), Kenyon–Yin (2021, introductory method description) and Stanley–Yin (2023, Theorem 4.2 and Corollary 4.3). The latter's variables include 1-preference count, unluckiness and the first-car preference multiplicity, not the count of preference value 2. The central new claim is the evaluated two-value occupancy law and its stochastic consequences. Searches against available mathematical records and web literature found related occupancy results for different random objects, not this implication. Priority may be affected by broader multivariate parking-function enumerators or uninspected tables; this is a real residual risk, not a claim of uniqueness.

## Mathematical value — PASS
The strict negative conditional ordering is a complete all-size qualitative dependence statement for two natural boundary categories in a classical hashing model, and the nonzero limiting covariance establishes persistent short-boundary dependence. The proof supplies the full bivariate coefficient distribution and an explicit joint Poisson/Bernoulli limit, not merely a recomputed marginal or small-size experiment.

## Limitations and references
Only classical uniform parking functions and the two specific values 1 and 2 are covered. No assertion about arbitrary preference values or other parking schemes is proved. The known input identity is cited to Yan (2015), with a reproduced proof-level statement in Diaconis–Hicks (arXiv:1611.09821) and Stanley–Yin (arXiv:2306.08681). The earliest selected primary source is Gessel–Seo (arXiv:math/0507497, first posted 2005-07-24). Independent historical-priority and proof audit have not been performed.

Self-review: passed. Independent audit: not yet performed.
