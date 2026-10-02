# Fresh audit — SCOPE-20260910-049

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

Among all 371,293 normalized monic degree-seven polynomials over \(\mathbb{F}_{13}\) of the stated affine-normal form, the direction-count histogram is 13 with eight directions, 117 with eleven, 1,196 with twelve, and 369,967 with thirteen; none has exactly nine directions.

## Correctness

**PASS** — A fresh full enumeration, independent of the package replay implementation, evaluated all \(13^5=371293\) normalized coefficient tuples, formed all pairwise slopes over \(\mathbb{F}_{13}\), and reproduced exactly the claimed histogram with zero nine-direction cases. The affine normalization is valid: output scaling/translation and input affine changes preserve direction cardinality, and input translation removes the degree-six coefficient because seven is invertible modulo thirteen.

Residual risk: The theorem is a finite computational classification; its correctness rests on exact finite-field enumeration, mitigated here by an independent implementation and the inspected archived recensus source.

## Originality

**PASS** — Resultary search found an earlier SCOPE result excluding nine-direction functions among degree at most six and sparse polynomial classes, explicitly leaving size 22 open; that makes the complete normalized degree-seven slice a genuine next boundary rather than a duplicate. Kadoo supplies global size-22 Rédei-type existence, not this polynomial-family obstruction. No exact prior histogram for all 371,293 normalized degree-seven representatives was found.

Residual risk: Search cannot exclude an unindexed computational table, but the exact finite census was not located outside the assigned record.

### Originality checks

**equivalent_formulations**

Searches: Resultary F13 degree 7 nine directions Rédei blocking set; degree-seven direction-count polynomial census PG(2,13).

Evidence: https://github.com/Resultary/2026/tree/main/2026/9/10/SCOPE049; https://github.com/Resultary/2026/tree/main/2026/9/9/SCOPE040.

Reasoning: The earlier result covers degrees at most six and sparse classes, not the complete normalized degree-seven family.

**broader_coverage**

Searches: Ball direction theorem q=13; Csajbók Rédei blocking set direction structure.

Evidence: S. Ball, The number of directions determined by a function over a finite field, DOI 10.1016/j.jcta.2003.09.006; B. Csajbók, https://arxiv.org/abs/1504.06748.

Reasoning: The structural theorems constrain possible direction counts but do not imply the zero count for nine directions in this complete degree-seven normalized family.

**exact_database_or_table**

Searches: Kadoo size-22 PG(2,13); exact histogram degree-seven F13 directions.

Evidence: F. H. Kadoo, DOI 10.33899/csmj.2010.163898; No external exact 371,293-row family histogram was found..

Reasoning: Known size-22 examples establish global existence but do not tabulate this normalized degree-seven family.

**claim_vs_prior_implication**

Searches: prior SCOPE040 boundary and Ball/Csajbók structural results.

Evidence: SCOPE040 states the degree-at-most-six exclusion while size 22 remains open at that stage..

Reasoning: Neither the earlier finite boundary nor the general direction theorems imply the degree-seven histogram, so the present exhaustive step is not a corollary.

### Source inspections

- **Assigned RESULT.md** — https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/10/049/RESULT.md. Trigger: Exact finite census and scope. Material read: Full normalized family definition, histogram, and limitations. Method: direct file inspection. Assessment: SUPPORTS. Evidence: The claim is carefully limited to the degree-seven normalized family.
- **audit_independent_recensus_deg7.py** — https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/10/049/artifacts/audit_independent_recensus_deg7.py. Trigger: Full finite recensus. Material read: Entire batched Vandermonde/slopes implementation. Method: direct source inspection plus fresh independent enumeration. Assessment: SUPPORTS. Evidence: The independent census architecture agrees with the fresh recount and exact histogram.
- **Resultary SCOPE040** — https://github.com/Resultary/2026/tree/main/2026/9/9/SCOPE040. Trigger: Closest prior published SCOPE boundary. Material read: Semantic-search title/summary showing degree-at-most-six and sparse-family exclusions. Method: Resultary semantic search. Assessment: NOT_COVERING_EXACTLY. Evidence: It leaves the complete degree-seven family beyond its exhaustive boundary.
- **The Minimal Blocking Set Of Size 22 In PG(2,13)** — https://doi.org/10.33899/csmj.2010.163898. Trigger: Same field/size and plausible dominating source. Material read: Abstract/full-text material on existence of size-22 Rédei-type minimal blocking sets. Method: primary-source inspection. Assessment: NOT_COVERING_EXACTLY. Evidence: Global existence does not imply existence or nonexistence inside this normalized degree-seven polynomial family.

## Value

**PASS** — This is a natural complete first-open-degree census in the direction problem after the prior degree-at-most-six obstruction, and it sharply rules out the full normalized degree-seven polynomial family while known size-22 examples force any remaining graph realization to arise elsewhere. That is a motivated finite cutoff/classification, not an arbitrary slice.

Residual risk: It does not classify all functions on \(\mathbb{F}_{13}\) or all Rédei-type blocking sets.

## Overall disposition

**PASSED**
