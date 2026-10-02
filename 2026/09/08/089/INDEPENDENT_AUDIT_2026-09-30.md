# Independent audit — SCOPE-20260908-089

Audit date (UTC): 2026-09-30 (UTC)

## Final claim

For the fixed Egan-Wanless order-10 pair A,B, A has 1080 transversals and 305 unlabelled orthogonal mates, with minimum B-overlay deficit 9 attained by a unique 1-partition; B has 932 transversals and 5 unlabelled orthogonal mates, with minimum A-overlay deficit 24 attained uniquely. The exhibited C* realizes deficit 9 and is a symbol relabelling of the published closest-to-MOLS mate.

## Correctness

**PASS** — The pinned A,B,C arrays were checked to be Latin, with A orthogonal to B and C and the published B-C overlay having 91 distinct pairs. A fresh exact transversal enumeration and exact-cover enumeration reproduced 1080/305 with unique minimum deficit 9 for mates of A, and 932/5 with unique minimum 24 for mates of B, including the complete deficit distributions. C* was checked Latin with the claimed overlays.

## Originality

**PASS** — The Egan-Wanless primary paper was inspected in its order-10 section: it supplies the baseline closest-to-MOLS triple and 91-pair overlap but does not enumerate all mates of either fixed square or give the 305/5 mate-stratum deficit distributions. published-results index searches found the current record as the exact match and no earlier source containing these census counts.

### Originality checks

#### Equivalent formulations

Searches: published-results semantic search: Egan-Wanless order 10 mate deficit 1080 305 932 5; Literature search: orthogonal mates/transversal census of the published order-10 squares.

Evidence: The published-results index returned this record as the exact match.; Egan-Wanless give the triple and 91-pair baseline, not these mate counts..

Reasoning: The 1-partition formulation is equivalent to orthogonal mates up to symbol relabelling; the primary source does not enumerate those partitions for the fixed order-10 squares.

#### Broader coverage

Searches: Egan-Wanless 2016 full order-10 section; order-10 transversal and MOLS literature.

Evidence: Egan-Wanless classify MOLS only through order 9 and explicitly present an order-10 near-triple rather than a comprehensive order-10 enumeration..

Reasoning: No broader order-10 classification was found that would imply the two fixed-square mate censuses.

#### Exact database or table

Searches: published-results semantic and web search for 1080 transversals/305 mates and 932/5 counts.

Evidence: No independent exact table with these four counts or the deficit distributions was found..

Reasoning: The baseline paper is not such a database.

#### Claim versus prior implication

Searches: Published closest-to-MOLS triple implications.

Evidence: The published fact |BC|=91 supplies only one mate with deficit 9.; It does not imply that 9 is optimal among all 305 mates of A or that B has only 5 mates with minimum 24..

Reasoning: The new exhaustive search closes natural strata not implied by the baseline witness.

## Value

**PASS** — This is a motivated exact boundary around the canonical published closest-to-MOLS order-10 triple, in the smallest still-open 3-MOLS order. Exhaustively closing the two natural orthogonal-mate strata gives a reusable constraint on attempts to improve that construction, while explicitly leaving the joint nonorthogonal region open.

## Source inspections

- **Enumeration of MOLS of small order** — https://arxiv.org/abs/1406.3681. Trigger: Pinned source objects and prior-coverage comparison. Material read: Full order-10 Section 8 including the printed A,B,C arrays and the 91-pair statement. Method: Primary full-text inspection. Assessment: Confirms the baseline objects and leaves the mate-stratum census uncovered. Evidence: The paper states the closest-to-MOLS order-10 triple and the 91 distinct B-C pairs; it does not give 305/5 mate counts.
- **Package mate census** — artifacts/squares.json; artifacts/mate_census.py; artifacts/verify.py; artifacts/candidate.json. Trigger: Correctness. Material read: All four artifacts. Method: Fresh exact replay and independent overlay checks. Assessment: Supports the stated finite census. Evidence: Fresh results exactly matched 1080/305/min9/unique and 932/5/min24/unique.

## Residual risks

- The joint trade-off region with neither third-square pair fully orthogonal remains open.
- The exhaustive proof is software-assisted exact cover, though independently replayed with the actual pinned arrays.

## Disposition

PASSED
