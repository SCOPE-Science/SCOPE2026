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

The complete symbolic argument appears in RESULT.md. The accompanying standalone `verify.py` uses exact dynamic programming on the three denominations to check second-representation thresholds for every residue at 147 distinct parameter values (4 through 150). The program additionally compares the two threshold boundary cases and the independent maximum and gap-count formulas. Execute using Python 3 in any directory. No external modules or data are required. Finite computation is corroborating evidence, not a proof for all parameters. Independent mathematical auditing has not been performed.
