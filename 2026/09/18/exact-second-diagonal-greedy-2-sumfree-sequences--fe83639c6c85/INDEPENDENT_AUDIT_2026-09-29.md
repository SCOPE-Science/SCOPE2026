# Independent Audit — Exact second-diagonal greedy 2-sumfree sequences

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `893915c372d45f6c02aee3c31a8cbd002ccb1b91`  
**Audited current source tree:** `893915c372d45f6c02aee3c31a8cbd002ccb1b91`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assignment tree SHA. GitHub was used only as read-only evidence; this audit plan does not assert that any staged audit text is already published.

## Correctness — PASS

PASS. The residue set modulo M=9f-1 is strict 2-sumfree: every block-pair residue range in the proof misses R_f, and the two exceptional elements 4f-1 and 5f also avoid all periodic target classes and cannot themselves be formed from earlier allowed terms. The saturation table covers every omitted residue, with translations preserving distinctness and earlierness; the only uses of the initially absent f+1 occur after a positive period shift. Independent greedy enumeration for f=4 through 40 agrees with the claimed set formula over 400 terms per parameter. The difference word, modulus, and density follow directly, while the unique 2f entry in the period block prevents a proper-power period and the backward mismatch proves the stated minimal preperiod.

## Originality — PASS

PASS, NARROWLY. Van Berkel–Bosma's September 2026 paper formulates explicit period/preperiod conjectures for all strict greedy 2-sumfree sequences and supplies computational evidence plus proved regions nearer the diagonal. The audited family g=3f is an infinite ray beyond the source's proved general region, and the source does not provide the submitted closed residue formula or proof for this ray. Older 0-additive-sequence literature supplies the broad eventual-regularity context, not this parameterized family.

## Scientific value — PASS

PASS. The theorem proves an infinite family of a newly stated global conjectural pattern, including exact residues and minimal period/preperiod rather than merely finite verification. It provides a reusable modular-saturation certificate for a nontrivial second-diagonal family.

## Independent checks

- checked all residue-block sum exclusions and the exceptional-element cases
- checked every saturation-table interval and the shifted f+1 edge case
- independently generated strict greedy sequences for f=4..40 and compared 400 terms each to the closed formula
- rechecked the difference block, translation modulus, density, and minimality arguments
- compared the claim against van Berkel–Bosma's stated conjectural framework and proved-range description
- verified the current main directory tree exactly equals the assigned tree SHA

## Limitations

- The result treats only the ray g=3f, f≥4, not the full conjecture.
- The motivating conjectures are extremely recent, so simultaneous unindexed work remains a residual priority risk.
- Finite enumeration is only corroborative; the verdict rests on the all-f modular proof.

## Evidence and references

- https://arxiv.org/abs/2609.18522
- https://arxiv.org/abs/2609.16843
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/exact-second-diagonal-greedy-2-sumfree-sequences--fe83639c6c85

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
