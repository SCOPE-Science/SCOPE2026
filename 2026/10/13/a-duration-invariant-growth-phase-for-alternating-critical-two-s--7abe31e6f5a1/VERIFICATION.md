---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification details

The mathematical proof uses characteristic-polynomial factorization, the Cayley–Hamilton identity for positive integer powers, a two-by-two trace–determinant computation, and the Perron root comparison. All hypotheses and quantifiers are in RESULT.md. The analytical factorization, not a finite census, establishes the unrestricted result.

The exact rational standalone checker `check_periodic_population.py` was run from the package source path before embedding. It verified 10,816 pairs of positive block lengths for 169 ordered rational parameter pairs; the signed phase, strictly positive power multipliers, isolated neutral growth factors, convex temporal averages on a five-point rational grid, two exact witness signs and the spectral projector limit were checked. The final package embeds that complete same-source checker; execute `python check_periodic_population.py` after extraction.

The checks do not test all real admissible vital rates or all positive block lengths; they are supplementary to the stated general proof. No independent audit has been performed.
