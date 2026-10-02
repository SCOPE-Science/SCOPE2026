# Independent audit — Hankel obstruction and multiplier repair for minimal backward-shift projections

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **repaired**.

## Correctness

**PASS** — The repaired final claim excludes the already-covered Hankel/BMOA correction from novelty. For \(f\in H^\infty\), coefficient comparison gives \(L_g f=M_{f^\sharp}^*g\) and the multiplier norm bound. For \(B=S^*\otimes I_K\), minimality makes every nonzero coefficient map injective on a minimal invariant subspace. If two nonzero coefficient-image closures differ, Beurling's description of a proper \(S^*\)-invariant subspace as \(K_\theta\), together with invariance under \(M_\theta^*\otimes I_K\), produces a nonzero vector killed by one coefficient map, contradicting injectivity. Hence all nonzero coefficient shadows have one common model space.

## Originality

**PASS** — Best-of-knowledge originality passes for the repaired arbitrary-multiplicity common-shadow theorem. The covered BMOA correction is treated solely as prior input.

### Equivalent formulations
The repaired claim is the general common-shadow theorem, not the covered Hankel boundary.

Evidence: The 2026-09-18 BMOA record covers only the obstruction/boundedness part. The source abstract states a common structure for nonzero coordinate projections in the bidisk setting, but the repaired theorem treats arbitrary Hilbert multiplicity and arbitrary coefficient functionals with a direct multiplier proof.

### Broader coverage
No inspected earlier source subsumes the repaired theorem.

Evidence: No earlier published archive hit stated the arbitrary-multiplicity/all-directions theorem. Classical Beurling theory supplies a proof ingredient rather than a dominating theorem.

### Exact database or table
The database check supports narrowing away from the covered theorem and retaining the distinct repair.

Evidence: Exact search found the prior BMOA correction but no earlier exact record for the arbitrary-multiplicity common-shadow theorem.

### Claim versus prior implication
The repaired theorem needs the minimality, multiplier-invariance and model-space argument given in the record.

Evidence: The BMOA obstruction alone does not imply the common-shadow result. The source's visible coordinate-projection statement does not mechanically imply equality for every coefficient functional in every Hilbert multiplicity.

### Source inspections

- **The sharp BMOA boundary for a backward-shift Hankel operator** — COVERS_REMOVED_PART.
  Identifier: https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-bmoa-boundary-backward-shift-hankel-operator--a39ad574fb44
  Material read: complete result and proof.
  Evidence: The earlier record already gives the BMOA threshold and explicit source correction.
- **Projections and minimal invariant subspaces in the Hardy space over the bidisk** — RELATED_NOT_DECISIVE.
  Identifier: https://arxiv.org/abs/2609.19311
  Material read: abstract and accessible metadata.
  Evidence: The abstract states common invariant structure for nonzero projections in the bidisk but does not expose the arbitrary-multiplicity/all-coefficient theorem in the accessible material.

### Residual risks

- The full 2026 source text was not accessible in the available text interface; an equivalent arbitrary-multiplicity lemma could be implicit in older vector-valued model-space literature not found by the searches.

## Scientific value

**PASS** — The repaired theorem salvages the motivating projection-rigidity phenomenon without the invalid synthesis step and strengthens it to arbitrary Hilbert multiplicity and arbitrary coefficient directions. This is a natural reusable structural lemma.

## Final assessment

The original framing required a substantive originality repair. The corrected research files state only the surviving correct, original, and valuable claim; all three axes were reassessed on that final claim.

This review does not constitute formal verification or a guarantee against undiscovered prior art.
