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

## Reproduction

Run `python3 verify.py` from the directory containing this file and `verify.py`. This standalone Python-standard-library script reconstructs the rational confidence bands and orbit values for each integer period \(2\le p\le120\), verifies exact reciprocal trust decisions at all orbit phases, their updates and distinctness, then checks perturbed trajectories for four full periods. The script uses exact fractions, not floating-point comparisons.

The mathematical proof of the universal \(p\ge2\) statement is contained in RESULT.md. The finite verification is a cross-check and does not certify the infinite claim. It does not verify global attraction, which is not asserted. The source's prior period-three example is credited separately.

No independent audit or independent validation has been performed.
