# Independent mathematical audit — 2026-10-01

## Final claim assessed

A missing-edge range for consecutive spanning-forest ratios

## Correctness — PASS

PASS. Double-counting the inclusion graph between s-component and (s-1)-component forests gives the lower bound (n-s+1)/(m-n+s). For the complete graph, minimizing the number of valid one-edge extensions over component-size profiles gives the matching upper bound with denominator D_{n,s}. The missing-edge hypothesis is exactly the comparison m-n+s <= D_{n,s}. The strictness argument correctly separates interior ranks from the top two ranks. This is an infinite proof; the atlas enumeration is only supporting evidence.

## Originality — PASS

PASS to the best of current knowledge. The directly motivating Bencs-Csikvari preprint states the consecutive-ratio assertion as a conjecture and supplies the universal s=2 case. A full published 18 September 2026 record on the same conjecture was inspected and proves a different high-component square-root boundary layer plus the first fixed top ranks; it does not imply the present edge-density criterion or the all-level sparse/planar corollary. Searches found no earlier theorem asserting the missing-edge condition or the m <= 3n-6 consequence. Older forest-enumeration sources and an unpublished monotonicity manuscript remain explicit residual risks because full text was not obtained.

### equivalent_formulations

Searches: Resultary semantic search: consecutive spanning forest ratios missing edges planar graphs Bencs Csikvari; forest component ratio normalized matching missing edges

Evidence: The exact current record is the only matching missing-edge theorem found. The inspected 18 September record uses k=n-s and n>=3k^2 instead of an edge-density hypothesis.

Reasoning: The two results overlap near the top of the forest poset but neither formulation reduces the present sparse-graph criterion to the earlier square-root boundary theorem.

### broader_coverage

Searches: arXiv:2609.18611 Bencs Csikvari forest-tree ratio Conjecture 5.8; Resultary 2026/9/18 spanning-forest-ratio-square-root-boundary

Evidence: The primary preprint presents the consecutive ratio as conjectural beyond its proved special case; the earlier published record proves only a boundary layer/top ranks.

Reasoning: No inspected stronger theorem covers all component levels for every graph with m<=3n-6.

### exact_database_or_table

Searches: OEIS A083483 complete-graph forest sequence; published mathematical record search for planar consecutive forest ratios

Evidence: Complete-graph forest counts may be tabulated, but the claim is a cross-graph inequality under a sparsity hypothesis, not a new numerical row.

Reasoning: A database cannot imply the theorem because the key statement quantifies over all connected graphs in a structural class.

### claim_vs_prior_implication

Searches: Myrvold 1992 Counting k-component forests; Teranishi 2005 number of spanning forests; Bencs Csikvari 2609.18611

Evidence: The inspected recent work does not state the missing-edge comparison. Older sources were only partially accessible and are retained as risks.

Reasoning: The present double-counting comparison supplies a new sufficient condition rather than a parameter substitution into an inspected prior formula.

## Scientific value — PASS

PASS. The result proves a current graph-theoretic conjecture on a broad natural class: every connected graph with at most 3n-6 edges, hence every connected planar graph, while also giving a sharper levelwise missing-edge criterion. That is a motivated structural regime, not an arbitrary finite slice.

## Source inspections

- **An inequality for the number of independent sets of matroids with an application to the forest-tree ratio of graphs** — https://arxiv.org/abs/2609.18611. Material read: Indexed primary-source statement context; full text was not retrievable through the available source interface during this run. Assessment: MOTIVATING_OPEN_PROBLEM. Evidence: Available material and the audited citation identify the consecutive-ratio statement as the stronger conjectural direction, with the s=2 case previously established.
- **A square-root boundary layer for the consecutive spanning-forest ratio conjecture** — https://github.com/Resultary/2026/blob/main/2026/9/18/SCOPE-spanning-forest-ratio-square-root-boundary--843428753b02/RESULT.md. Material read: Complete published RESULT.md. Assessment: OVERLAPPING_NOT_COVERING. Evidence: It proves n>=3k^2 and all ranks n-s<=3, but not the missing-edge criterion or the all-level planar conclusion.
- **Counting k-component forests of a graph** — https://doi.org/10.1002/net.3230220704. Material read: Bibliographic/abstract-level material only. Assessment: INACCESSIBLE_RESIDUAL_RISK. Evidence: No exact missing-edge theorem was located, but full text was not read.

## Limitations and residual risks

The result leaves low-component ratios of denser graphs unresolved except for the previously known universal s=2 case.

- Myrvold (1992), Teranishi (2005), and the unpublished Eaton-Kook-Thoma monotonicity manuscript were not inspected in full text.
- The edge threshold is sufficient and is not claimed necessary or optimal.

## Disposition

**passed**
