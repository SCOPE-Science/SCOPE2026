# Scientific review: three-periodic BDF3 stability

## Correctness

**PASS.** The universal result follows from the exact differentiated-cubic recurrence, the explicitly evaluated period trace and determinant, and three strictly positive Schur polynomials. The cyclic polynomial coefficient lists in RESULT.md permit direct reconstruction independent of a program. The symbolic verifier checks all identities and the degeneration asymptotic; independent sampled comparisons are supplementary, not extrapolated to all grids. The domain is strictly positive fixed three-periodic steps.

## Originality

**PASS on the available scientific comparisons, with qualified priority risk.** Guglielmi–Zennaro's accessible original abstract concerns general spectral-radius sufficient bounds for variable-step BDF3, and the later Li–Liao full preprint provides an adjacent-step-ratio-limited theorem rather than arbitrary fixed three-periodic patterns. Söderlind–Fekete–Faragó treat smooth grids, a different family. The primary full Guglielmi–Zennaro article was not accessible; a specialist equivalent within it or elsewhere cannot be conclusively excluded. The proposed statement is not inferred merely from absence of a keyword match; the stated implications and hypothesis gaps are compared explicitly in AUDIT.json.

## Mathematical value

**PASS.** An entire natural two-parameter family of highly irregular recurring meshes is classified without a priori ratio caps. The exact sharp supremum and near-neutral degeneration reveal a genuine stability-versus-damping distinction. This is more than a coefficient substitution or routine finite sample: it identifies why restrictive arbitrary-mesh ratio bounds need not apply to this structured family while no uniform spectral margin survives. It does not purport to prove nonlinear error bounds or stability for arbitrary meshes.

## Closest literature and limits

Guglielmi–Zennaro (2001), https://doi.org/10.1007/s211-001-8010-0, remains the most important unresolved full-text comparison. Li–Liao (2022), https://arxiv.org/abs/2201.00527, has a different ratio-limited implication. Söderlind–Fekete–Faragó (2018), https://doi.org/10.1007/s10543-018-0716-y, assumes smooth-grid deformation. No independent mathematical audit or exhaustive historical uniqueness proof is asserted.

Self-review: passed. Independent audit: not yet performed.
