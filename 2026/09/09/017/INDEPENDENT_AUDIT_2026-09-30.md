---
audit_date: 2026-09-30
status: passed
---

# Independent mathematical audit

## Final claim

Among ordered triples of partitions of height at most 3 with base size n at most 6, there are 288 base zeros and exactly 42 that become positive under dilation by 2; the per-n hole counts are 0,1,4,6,0,31, there are no dilation-by-3-only holes in the checked size window, and the lexicographically least hole is the triple ((1,1),(1,1),(1,1)), whose double has coefficient 1 while its triple again has coefficient 0.

## Correctness — PASS

A fresh Frobenius-character computation was implemented independently using the three-variable alternant coefficient formula and exact rational class sums. It reproduced 568 ordered base triples, 288 zeros and 280 positives, with per-n zero/positive counts (0,1), (4,4), (16,11), (33,31), (51,74), (184,159). Exactly 42 base zeros lift at dilation 2 with per-n counts 0,1,4,6,0,31. The independent computation also found four dilation-3 positives in-range, all already positive at dilation 2, hence zero dilation-3-only holes. The two displayed witness triples match the committed certificates.

## Originality — PASS

The primary saturation-hole literature establishes that Kronecker saturation fails and constructs large/asymptotic families, while also emphasizing bounded-height positivity algorithms. The inspected full text of Ikenmeyer-Mulmuley-Walter does not contain this low-degree height-at-most-3 census, the per-n 42-hole table, or the n=5 hole-free slice. Resultary searches returned the present record as the direct match and a separate S12 Kronecker census that does not classify dilation holes.

### Equivalent formulations

Searches: Kronecker saturation holes dilation bounded height; minimal Kronecker saturation counterexample

Evidence: Ikenmeyer-Mulmuley-Walter, arXiv:1507.02955, discusses saturation failure and bounded-height complexity.

Reasoning: The audited property is positivity after uniform dilation, matching the standard saturation-hole notion.

### Broader coverage

Searches: Kronecker saturation holes height 3; bounded height Kronecker positivity

Evidence: arXiv:1507.02955 gives asymptotic existence and complexity context, not this finite census.

Reasoning: Broader theory motivates the phenomenon but does not imply the exact low-degree counts.

### Exact database or table

Searches: Resultary height<=3 Kronecker dilation census; S12 Kronecker census holes

Evidence: Resultary SCOPE006 is a coefficient census at n=12, not a paired dilation-hole table.

Reasoning: A coefficient database could mechanically reproduce the numbers, but no prior published table with these paired dilation classifications was located.

### Claim versus prior implication

Searches: Kronecker coefficient (1,1) (2,2) saturation example

Evidence: No primary source located stating the full claimed table; the smallest witness itself is elementary.

Reasoning: The lex-least witness alone is not the contribution carrying originality; the exact bounded-height census and absence statements are not implied by the inspected general results.

## Value — PASS

Saturation failure is explicitly motivated in the primary literature, and bounded height is a standard tractable regime. A complete first-window census with a hole-free slice and non-monotone dilation witness supplies concrete boundary data that can guide structural conjectures. Its value is as an exact finite classification, not as a general saturation theorem.

## Sources inspected

- artifacts/hole_table.json blob 065a2f85fe4a19cca85447dc4604e0652d859b7f
- certificate blobs in the assigned tree
- https://arxiv.org/abs/1507.02955
- Resultary semantic search

## Residual risk

The smallest witness is easy and likely folklore; the accepted contribution is the complete stated finite census. The cutoff is computational and must not be presented as a structural threshold.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
