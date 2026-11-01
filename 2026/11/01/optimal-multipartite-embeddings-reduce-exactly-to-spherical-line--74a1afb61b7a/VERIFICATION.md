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

# Reproducibility and limits

Run `python3 verify_paired_multipartite.py` with Python 3, without third-party dependencies. The checker establishes exact finite rational identities for the construction's Gram matrix, all pairwise graph metric inequalities in 154 configurations, 640 variance decompositions, and the seven-vector sharp rank certificate. Expected terminal line: `ALL_PAIRED_MULTIPARTITE_HILBERT_CHECKS_OK`.

The deterministic finite tests do not establish the all-parameter statement: that conclusion follows from the barycenter identity, equality-rigidity argument, elementary packing, Rademacher concentration, and Welch rank inequality proved in `RESULT.md`. Nothing here asserts independent verification or external certification.
