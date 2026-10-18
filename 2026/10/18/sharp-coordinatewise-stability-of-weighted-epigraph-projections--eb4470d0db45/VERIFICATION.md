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

The embedded `verify.py` runs with Python 3.10+ without extra dependencies. It performs exact Fraction enumeration for active-subset and sorted-prefix norms (up to four coordinates with seven rational values per coordinate), randomized rational tests up to seven coordinates, and numerical tests of projected chart derivatives, active-set realization, and the polar Moreau identity. It also checks the two optimal-weight design families across dimensions 1–60. A successful run prints `VERIFY_OK` with the numerical assertion count. The analytical proof, not numerical tests, supplies the universal results. No independent mathematical validation has been performed.
