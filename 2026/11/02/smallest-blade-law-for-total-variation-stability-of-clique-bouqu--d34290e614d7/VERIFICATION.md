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

# Verification record

Run `python3 verify.py` with the Python 3 standard library. The checker's independent graph construction directly enumerates the hub-to-blade and within-blade edges; it separately evaluates the proposed polynomial formulas and the actual absolute-value directional derivative. Its fixed-seed finite test suite passed 230 graph-size profiles; 15,006 cut-profile formula and inequality checks; 230 smallest-blade sharpness witnesses; 9,600 integer-signal coarea and infinitesimal inequalities; and 3,595 first-order numerical Euler diagnostics.

The valid proof for all finite blade sizes is in `RESULT.md`, steps 1–4. Numerical verification alone would not justify a universal theorem, and explicit Euler diagnostics do not certify the exact heat semigroup at finite positive times. The analytic proof establishes the all-time bound. One full-text novelty risk remains: an equivalent classification could appear in unindexed semigroup or graph diffusion literature. Independent audit has not been performed.
