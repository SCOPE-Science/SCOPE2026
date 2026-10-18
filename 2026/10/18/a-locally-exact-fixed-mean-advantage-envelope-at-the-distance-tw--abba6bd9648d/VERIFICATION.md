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

`python3 verify.py` runs finite sanity checks of the new theorem's crossing, reduced competitors and derivative. It checks selected positive indices against a finite grid; these checks cannot prove a statement about arbitrary finite lengths. The analytical proof gives a strict limit gap for every possible shift and then uses uniform binomial-to-Poisson convergence, so the infinite domain is not silently replaced by the grid. The original threshold, optimizer and rigidity statements are credited to Kleiner (2026), not independently re-proved. No independent validation or external certification has occurred.
