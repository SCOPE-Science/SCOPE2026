# Independent mathematical audit — 2026-10-01

## Final claim

Sharp Assouad-dimension ceiling from uniform disconnectedness on the line

## Correctness — PASS

PASS. The one-dimensional gap argument was reconstructed. For every constant below the optimal chain-disconnectedness constant, each compact non-singleton node has a separating gap consuming that fraction of its diameter. The two child diameters therefore have a strictly contracting total. At depth k, total active diameter decays geometrically while binary branching gives at most two-to-the-k active nodes. Summing the minimum of those bounds across their crossover gives exactly the stated Assouad exponent. For the central two-branch Cantor set, the first differing basic interval gives the matching lower bottleneck, the endpoints show optimality of the constant, and strong separation gives equality in dimension.

## Originality — PASS

PASS. The inspected literature supplies qualitative relations between Assouad dimension below one and uniform disconnectedness and separately the Stieltjes-clock bottleneck criterion. Targeted searches for the exact sharp function, the extremal problem over subsets of the line, and central-Cantor equality found no prior statement. The published-record semantic search likewise returned the audited record as the exact match rather than an earlier theorem.

### equivalent_formulations

Searches: sharp Assouad dimension bound uniform disconnectedness real line optimal constant Cantor; log 2 log(2/(1-c)) Assouad uniform disconnected

Evidence: Searches found qualitative equivalences and the current exact record but no earlier identical extremal formula.

Reasoning: Porosity and chain-bottleneck formulations were compared; none inspected gave the same optimal function.

### broader_coverage

Searches: Assouad dimension uniformly disconnected theorem dim_A < 1; Lu Xi uniform disconnected Assouad dimension

Evidence: Existing results give qualitative implications between dimension and uniform disconnectedness.

Reasoning: Qualitative equivalence does not mechanically determine the sharp quantitative ceiling at a prescribed optimal chain constant.

### exact_database_or_table

Searches: published mathematical record semantic search exact constant and central Cantor extremizer

Evidence: No numerical database/table is natural for this theorem; no earlier exact published record was found.

Reasoning: The exact-search analogue is theorem/record search rather than a tabulated invariant.

### claim_vs_prior_implication

Searches: arXiv:2609.20706 Stieltjes clock uniform disconnectedness; doi:10.1016/j.aim.2014.12.026 uniform disconnectedness

Evidence: The clock source identifies a disconnectedness criterion; general Assouad literature supplies qualitative dimension implications.

Reasoning: Neither inspected prior statement implies the sharp binary-tree exponent or equality family.

## Scientific value — PASS

PASS. This is a natural sharp extremal law between a standard quantitative disconnectedness invariant and Assouad dimension, with equality for a canonical one-parameter Cantor family. The exact constant is independently useful, and the Stieltjes-clock corollary converts a selection-theoretic jump parameter into a quantitative geometric ceiling.

## Source inspections

- **Stieltjes-clock Holder selection preprint** — https://arxiv.org/abs/2609.20706. Material read: Abstract and indexed theorem context. Assessment: GENERAL_CLOCK_CRITERION_NOT_SHARP_DIMENSION_COVERAGE. Evidence: The accessible statement concerns the disconnectedness/selection criterion, not the sharp Assouad ceiling.
- **Uniform-disconnectedness and Assouad-dimension literature** — https://doi.org/10.1016/j.aim.2014.12.026. Material read: Indexed theorem context and search excerpts. Assessment: QUALITATIVE_NOT_EXACT_COVERAGE. Evidence: The literature supplies qualitative implications but not the audited optimal constant formula.

## Limitations and residual risks

The sharp formula is proved only for subsets of the real line and uses its order structure. It does not give a same-constant higher-dimensional analogue, a converse quantitative lower bound on the optimal disconnectedness constant from dimension alone, or uniqueness of the central-Cantor extremizers.

- The very recent Stieltjes-clock source was not available in full text through the search interface.
- No claim is made beyond one-dimensional ordered sets.

## Disposition

**passed**
