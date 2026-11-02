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

# Verification

Run `python3 check.py` in the extracted package directory. The checker uses only standard Python libraries and enumerates all finite latent and observed paths for three surveys using exact rational probabilities; it is not an infinite parameter proof. It validates the closed-form inverse across 687 admissible rational parameter triples, including negative and positive one-step memory, and verifies three exact zero-memory Bernoulli product cases. The example in RESULT.md is reproduced by the program. The general result, sign of the square-root branch, exceptional family, two-visit obstruction and Jacobian are established analytically in RESULT.md.

Scientific scope: known-occupied sites, stationary irreducible two-state availability, equal visit spacing, common conditional detector sensitivity, no false positives. Exact-rational tests are corroborative. Independent audit and empirical field validation have not been performed.
