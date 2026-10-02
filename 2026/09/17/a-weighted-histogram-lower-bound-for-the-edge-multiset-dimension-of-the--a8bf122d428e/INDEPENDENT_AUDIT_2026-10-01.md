# Independent audit — SCOPE-20260917-008

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

The edge multiset dimension of the six-dimensional hypercube satisfies edim_m(Q₆) at least 8; together with the known 15-landmark certificate, the current bracket is 8 through 15.

## Correctness

**PASS** — The shell count 6 times binomial(5,r) per landmark follows by projecting each of the six parallel edge directions to Q₅. Summing the weighted histogram therefore forces total weight 84m. A fresh exact enumeration of all six-component histograms with total m and the only active capacities h₀,h₅ at most 2 reproduced the weight counts for m=6 as 7,12,27,36,54,60 and for m=7 as 8,14,32,44,68,80, giving minimum total weights 670 and 612 for 192 distinct histograms, respectively. These exceed the forced totals 504 and 588, ruling out m=6,7. Combined with the prior lower bound excluding smaller sets, this proves edim_m(Q₆) at least 8.

Residual risks:
- The proof uses the previously published lower bound of 6 to dispose of m below 6; that prior result was checked at the primary-source level.

## Originality

**PASS** — Allikvere's primary preprint explicitly reports only edim_m(Q₆) at least 6 while giving a 15-landmark upper certificate. The audited weighted-histogram argument raises the lower bound to 8. Published-results search found the audited Q₆ result and a related Q₇–Q₁₀ extension, but no earlier stronger Q₆ bound.

### equivalent_formulations

Searches: Resultary semantic search: Q6 edge multiset dimension hypercube lower bound 8 weighted histogram 192 edges; Web search for edim_m(Q6) 8 and edge multiset dimension Q6

Evidence: The exact Q₆ lower-bound hit is the audited record; Allikvere's arXiv abstract states only lower bound 6.

Reasoning: Distance-histogram and edge-multiset representations are the same invariant under the stated definition; no separate equivalent stronger result was found.

### broader_coverage

Searches: arXiv:2608.09983 The edge multiset dimension of hypercubes; arXiv:2607.10311 edge multiset dimension survey

Evidence: The primary hypercube paper covers existence and the lower bound 6 at Q₆, not 8.; A later SCOPE Q₇–Q₁₀ weighted-histogram record is adjacent, not dominating Q₆.

Reasoning: No general theorem inspected forces the Q₆ lower bound 8.

### exact_database_or_table

Searches: Search exact counts 670,504,612,588 with Q6 edge multiset

Evidence: No external table of these weighted histogram counts was found.

Reasoning: The counts were independently regenerated rather than read from a table.

### claim_vs_prior_implication

Searches: Compare Allikvere lower bound 6 with the weighted-histogram obstruction

Evidence: Lower bound 6 does not imply exclusion of resolving sets of size 6 or 7.

Reasoning: The new global weight invariant supplies the missing two exclusions.

### Source inspections

- **The edge multiset dimension of hypercubes** — https://arxiv.org/abs/2608.09983
  - Trigger: Direct prior Q₆ result
  - Material read: Primary abstract and result summary; full HTML endpoint unavailable in this run
  - Method: primary-source abstract inspection plus independent proof reconstruction
  - Assessment: NOT_COVERING lower bound 8
  - Evidence: Abstract explicitly states lower bound edim_m(Q₆) at least 6 and explicit resolving sets for Q₆ through Q₁₀.
- **A weighted-histogram lower bound for the edge multiset dimension of the 6-cube** — https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE008
  - Trigger: Exact published-results hit
  - Material read: Title and summary
  - Method: semantic published-results search
  - Assessment: SELF_MATCH
  - Evidence: Exact same lower bound.
- **Weighted-histogram certificates for the edge multiset dimension of Q7–Q10** — https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE009
  - Trigger: Potential broader same-family result
  - Material read: Title and summary
  - Method: semantic published-results search
  - Assessment: NOT_COVERING Q₆
  - Evidence: Applies to dimensions 7 through 10.

Originality residual risks:
- A very recent or unindexed improvement to the Q₆ lower bound could exist; no such source was located.

## Value

**PASS** — Q₆ is the first finite-dimensional hypercube case after the infinite-dimension transition established in the primary work. Raising its lower bound from 6 to 8 narrows a natural exact invariant and introduces a reusable weighted-histogram obstruction that extends to higher cubes.

Residual risks:
- The exact value remains open between 8 and 15.

## Scientific limitations

- The exact value is not determined.
- The package contains no standalone verifier artifact, so the finite histogram calculation was independently regenerated.

## Disposition

**PASSED**

This audit is not peer review or external certification.
