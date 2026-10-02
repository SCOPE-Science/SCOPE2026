---
audit_date: 2026-09-30
status: passed
---

# Independent mathematical audit

## Final claim

For the committed demicap D0 in AG(4,3), exactly six maximal 20-caps contain D0, and every two distinct caps in this six-cap fiber intersect in exactly 12 points.

## Correctness — PASS

The sum-zero collinearity model was reconstructed independently. From D0 the no-line pool has 30 admissible points. An unbiased backtracking search over 10-point complements found exactly six completions. Reconstructing the six 20-caps gave all 15 pairwise intersection sizes equal to 12. This independently verifies the headline fiber count and spectrum without relying on the saved success log.

## Originality — PASS

Awan-Frechette-Li-McMahon explicitly state that the relevant demicap lies in six maximal caps and develop the surrounding 6-by-6 demicap structure. Their inspected full text does not state the 15-pair intersection spectrum for the six caps through a fixed demicap; its uses of 'intersection' concern other geometric decompositions. Resultary found the present record as the only direct match for I(D0)={12}. The six-cap count is therefore prior, while the uniform intersection spectrum is the audited final increment.

### Equivalent formulations

Searches: demicap maximal cap six AG(4,3) intersection; pairwise intersection caps through demicap

Evidence: Awan et al., arXiv:2106.14141, Section 5.1 states a chosen demicap is in six maximal caps.

Reasoning: The prior six-cap fiber is the same object; it does not by itself specify the pairwise intersections.

### Broader coverage

Searches: AG(4,3) demicap 6x6 maximal caps outer automorphism S6

Evidence: Awan et al. construct 36 caps as unions of two families of six demicaps and discuss the affine action.

Reasoning: That structure is broader contextual coverage, but no inspected theorem gives the fixed-fiber spectrum 12 for all 15 pairs.

### Exact database or table

Searches: Resultary AG(4,3) demicap pairwise intersection 12

Evidence: The direct hit was the present result; no separate published table was found.

Reasoning: No exact prior table located.

### Claim versus prior implication

Searches: Awan demicap intersection six maximal caps

Evidence: The prior paper gives six containing caps and incidence structure, but not a cited uniform pair-intersection theorem.

Reasoning: The count six alone is insufficient to force the 15 pairwise intersections; the audited exhaustive fiber computation supplies the missing exact statement.

## Value — PASS

The invariant is a natural structural refinement of the demicap fiber studied in the primary literature. It records a complete local intersection spectrum, not an arbitrary sample, and can be used to recognize the fiber incidence geometry.

## Sources inspected

- artifacts/verify.py blob 6fcfe40ff757bbc2b91f418f8c0ddad3891af6f4
- https://arxiv.org/abs/2106.14141
- Resultary semantic search

## Residual risk

The main originality risk is that the 12-intersection property may be derivable as a short corollary from the full affine-action results in Awan et al.; no such published implication was located in the inspected text. The claim remains limited to the committed D0 fiber.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
