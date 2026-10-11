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

# Verification of the exact octahedral projection-inradius law

The mathematical proof is given in RESULT.md. For deterministic replay, run `python3 verify.py` with Python 3's standard library. The program verifies the two-cases cube-section vertex maximization on 1,329 normalized integer normal triples in *exact rational arithmetic*, independently computes the inradii of 500 genuinely projected planar polygons using supporting edges rather than polarity, validates the ray determinants and arctangent denominator formulas, and checks both distribution endpoints and monotonicity at a grid of 100 thresholds. It also performs a seeded 80,000-sample normal experiment with stated error tolerances.

The recorded execution returned `VERIFY_OK 1329 exact-rational cube sections; 500 independently projected planar hulls; 80000 Haar directions`. A replay made from the embedded file in the delivered package is the authoritative execution test; no third-party environment, external database, or network access is required by the code.

Finite rational checks and random simulation do **not** prove the identities for arbitrary orientations or the continuum distribution. Those follow from the analytic cube-section vertex classification, geometric polarity, and solid-angle argument. The standard solid-angle identity is a published mathematical lemma, not a computer certificate. No independent external review has occurred. The available abstract of a relevant 2026 random-section-diameter manuscript does not settle whether its uninspected full text contains an equivalent specialized identity.
