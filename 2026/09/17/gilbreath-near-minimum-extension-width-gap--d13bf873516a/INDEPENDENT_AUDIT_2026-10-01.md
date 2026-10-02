# Independent scientific audit — SCOPE-20260917-d13bf873516a

Date (UTC): 2026-10-01

## Final claim

Every defective valid-extension set of a finite strictly increasing Gilbreath sequence has width at least 10. Consequently, extension width at most 9 is equivalent to anti-diagonal sum at most 7, yielding the stated complete anti-diagonal classification of widths 5, 7, and 9; the bound 10 is sharp at (2,3,5,9,15).

## Correctness

**PASS** — The reverse-preimage recurrence was reconstructed directly. The zero-suffix lemma forces the preceding even anti-diagonal entry to be 0 or 2. Choosing the rightmost failure of interval completeness gives an odd suffix sum at least 3; the completed suffix reverse tree is a full even interval, and the offending fold creates at least five positive distances. Earlier folds cannot decrease cardinality, proving defective width at least 10. The sharp example independently gives distance set {2,4,6,8,10}. A fresh bounded enumeration through length 9 found no violation of the theorem or the stated low-width forms.

## Originality

**PASS** — The closest Muney source supplies the reverse-tree framework, interval-completeness criterion, minimum-width theory, and the first defective example, but the accessible indexed material does not state the width-gap theorem or the complete widths-5/7/9 classification. Resultary search found this record as the exact match and no earlier matching classification. Because the primary full text was not accessible in this run, the originality conclusion is explicitly best-of-knowledge rather than exhaustive.

### Equivalent formulations

No equivalent theorem was located in the material actually read.

### Broader coverage

The audited theorem is a nontrivial consequence of the framework, not a direct table lookup.

### Exact database or table

No exact database/table supplies the claimed structural classification.

### Claim versus prior implication

The prior criterion alone does not mechanically state or numerically force the sharp width-10 gap without further proof.

## Scientific value

**PASS** — A sharp structural gap between interval-complete and defective extension sets and a complete near-minimum classification answer a natural stability question adjacent to the source's minimum-width theory. The result is theorem-level and infinite in n, not merely a small finite enumeration.

## Source inspections

- **Holes in Valid-Extension Sets of Finite Gilbreath Sequences** — https://arxiv.org/abs/2606.23721. Indexed abstract/metadata and searchable descriptions; full text could not be retrieved in this run Assessment: PLAUSIBLE_BUT_NOT_FULLY_INSPECTED. Accessible material reports the valid-extension framework, interval-completeness condition, minimum-width result, and smallest defect, but not the audited width-gap classification.
- **A080839** — https://oeis.org/A080839. Sequence entry and references Assessment: NOT_COVERING. Provides enumeration counts, not the extension-width classification.
- **A width gap and exact near-minimum classification for finite Gilbreath sequences** — https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-gilbreath-near-minimum-extension-width-gap--d13bf873516a. Title and summary Assessment: SELF_MATCH. Exact same theorem.

## Limitations and residual risks

- The result classifies only the near-minimum regime through width 9. It does not classify widths 10 and above or address Gilbreath's conjecture for the primes.
- The highly relevant Muney primary paper could not be inspected in full during this run; a stronger nearby statement in inaccessible text remains a residual originality risk.
- The bounded computation is supplementary and is not used as proof of the all-length theorem.

## Disposition

**PASS**
