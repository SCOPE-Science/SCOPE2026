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

The pointwise formula was compared with direct distinct-subsequence set enumeration for all binary weight-two words at lengths 2 through 12 and every permitted deletion count. There were 3,003 source/deletion-radius comparisons. The finite-length aggregate identity agreed with independent summation throughout that range. The canonical balanced maximum and plateau equality classification were checked for all lengths 2 through 54, using 1,101,870 source/radius evaluations.

Execute `python3 check.py` in this directory using Python 3's standard library. A zero exit code and three PASS lines indicate completion. Exhaustive checks over finite ranges do not independently prove the universal statements; the mathematical arguments appear in RESULT.md. No independent external audit has been performed.
