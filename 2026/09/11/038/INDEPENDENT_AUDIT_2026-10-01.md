# Independent audit — 2026-10-01

**Record:** `SCOPE-20260911-038`

## Correctness — PASS

A fresh exact chip-firing reconstruction on the stated eight-vertex multigraph reproduced the headline vertex rank exactly. For each of the eight vertices q, the class of D* minus q has an effective q-reduced representative; independently enumerating degree-two vertex subtractions found exactly 18 pairs with empty linear system, including (v0,v4). This gives rank at least one and rank at most one, hence vertex Baker-Norine rank exactly one. The committed verifier and certificate agree with the fresh calculation. The RESULT text uses the word “bridges” for the four square edges although those individual edges are not graph-theoretic bridges; that terminology defect does not alter the displayed graph or the rank computation.

## Originality — PASS

Published rank theory supplies the general algorithm and the equality between graph rank and the corresponding metric-graph rank, while recent tropical-trigonal papers classify existence of degree-three rank-one divisors under connectivity hypotheses. None of the inspected sources states this named divisor on this named square-backbone genus-five multigraph or gives its exact reduced-divisor certificate. Searches of the published-record index returned this exact record and nearby but different rank examples, not a prior covering result.

### Structured originality checks

- **equivalent_formulations:** Searches: Baker-Norine rank degree-3 divisor genus-5 square-backbone loop-of-loops; tropical trigonal lower connectivity degree 3 rank 1. Evidence: Hladky-Kral-Norine gives structural/algorithmic divisor-rank theory and graph/metric rank equality. Melo-Zheng gives trigonal existence equivalences for 3-edge-connected curves and a later extension to lower connectivity outside necklace cases. Reasoning: These are broader existence/rank frameworks, not an exact statement about D*=v0+v1+v2 on the displayed multigraph.
- **broader_coverage:** Searches: tropical trigonal curves 3-edge connected; tropical trigonal curves general case necklace. Evidence: The general-case tropical-trigonal paper extends existence equivalences to many lower-connectivity curves. Reasoning: Even if the graph falls in the broader trigonal class, the cited theorems do not identify the particular divisor D* or its exact rank certificate.
- **exact_database_or_table:** Searches: published-result semantic search for exact graph/divisor wording; web search for Gamma5* D* Baker-Norine rank. Evidence: Only the audited record matched exactly; nearby records concerned different graphs/divisors. Reasoning: No exact prior table row or named certificate was found.
- **claim_vs_prior_implication:** Searches: rank algorithm literature; trigonal classification literature. Evidence: Prior work makes the computation decidable and contextualizes trigonal existence. Reasoning: The exact value for this particular divisor still requires the graph-specific chip-firing calculation; it is not a parameter substitution into a published closed formula.

## Scientific value — PASS

The claim is a motivated exact invariant at the genus-five Brill-Noether boundary, on a small closed loop assembly for which the stated divisor provides a concrete specialness witness. It is not offered as a generic family theorem or a lifting result. The exact reduced-divisor certificate is reusable for later skeleton-specific questions.

## Source inspections

- **Hladky, Kral, Norine, Rank of divisors on tropical curves** (arXiv:0709.4485). Abstract and theorem-level summary returned by the full-text index. Assessment: BROADER_NOT_COVERING_EXACT_CLAIM. Provides algorithmic rank theory and graph/metric rank equality, but not the named divisor on the named graph.
- **Melo, Zheng, Tropical trigonal curves** (arXiv:2501.03903). Abstract and theorem summary. Assessment: BROADER_NOT_COVERING_EXACT_CLAIM. Classifies existence for 3-edge-connected tropical curves, not this exact divisor certificate.
- **Melo, Zheng, Tropical trigonal curves: the general case** (arXiv:2509.09502). Abstract describing extension outside necklace cases. Assessment: BROADER_NOT_COVERING_EXACT_CLAIM. Extends existence equivalences; does not state D* or its exact rank.

## Residual risks

- The exact literature search cannot prove absolute global novelty; the conclusion is best-knowledge based.
- The RESULT text calls the four square edges “bridges”; that terminology is false for individual cycle edges but does not affect the defined graph or final rank claim.

## Disposition

**PASSED**. The final claim passes correctness, originality, and scientific value.
