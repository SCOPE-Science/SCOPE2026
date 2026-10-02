---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

In the stated Rössler zero-Hopf unfolding, the two first-averaged zeros on the polar axis are the blown-up limits of the two exact equilibrium branches; because the angular chart is singular at zero radius, the cited first-order angular averaging argument does not certify periodic-orbit families from those two boundary zeros, while the positive-radius averaged zero is unaffected.

## Correctness — PASS

The equilibrium equations reduce exactly to a quadratic in z. Substitution of its two roots into the assigned source-coordinate transformation gives u=v=0 and hence R=0 identically, with the scaled W-limits equal to the two boundary averaged roots with opposite branch labels. Independently recomputing the source's numerical example gives R=0 for both exact equilibria and R=1 for both printed adjusted seeds. The polar angular formula contains division by the squared radius and the package derives a nonzero correction of order epsilon/R near the boundary roots, so the open-neighbourhood smoothness needed by the stated angular averaging setup is absent there.

**Checked sources.** Assigned RESULT.md at tree 452643dba69c2d625e7f0e5b83f62447df837607; artifacts/check_boundary_zeros.py blob 8fdc5e0422debf4a0088134617ce2449fd849b2e; Llibre–Szumiński, arXiv:2609.17336

**Residual risks.** Full primary-preprint text was not retrievable in this run; the exact source-coordinate transcription was therefore checked from the assigned package rather than re-extracted independently from the PDF.

## Originality — PASS

The finding is source-specific: it identifies the two boundary averaged roots with exact split equilibria and uses that identification to expose a failure of the particular angular certificate. Searches found the assigned result and a later 2026-09-20 follow-up, but no earlier primary result making this source-specific identification or proof-gap claim.

### Equivalent formulations

A generic warning that polar coordinates are singular at the origin is not equivalent to proving that these two specific averaged zeros are exactly the split equilibria and invalidate this proof step.

### Broader coverage

No pre-2026-09-18 broader theorem located was found to imply the record's source-specific comparison.

### Exact database or table

A table check is genuinely inapplicable because the claim is about a coordinate singularity and exact algebraic identification.

### Claim versus prior implication

The prior claim points in the opposite direction and does not imply the correction.

**Checked sources.** https://arxiv.org/abs/2609.17336; published result dated 2026-09-20; assigned package at the frozen Git tree

**Residual risks.** The motivating preprint is recent and may be revised. Full primary text was not available in this run.

## Value — PASS

The claim corrects the logical status of two out of three periodic-orbit certificates in a current zero-Hopf theorem and cleanly isolates the surviving positive-radius conclusion. A precise boundary counterexample to a proof mechanism is a motivated structural finding, even without proving nonexistence.

**Residual risks.** Its importance may diminish if the source supplies a different regular-coordinate existence argument in a later revision.

## Limitations

- This identifies a gap in the displayed first-order averaging certificate, not nonexistence of additional nearby periodic orbits.
- The primary preprint abstract was retrieved, but its full arXiv text could not be fetched in this run; the source-specific coordinate formulas were checked against the assigned package and its reproducibility script.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
