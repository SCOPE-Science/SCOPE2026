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

Run `python3 verify.py` from the directory containing that file; only the Python standard library is needed. The script performs independent exact-rational Gaussian elimination of absorption and unit-current voltage systems on 840 reproducibly generated graph/parameter instances, compares the two solutions term by term, verifies the attained path bound for path sizes 2 through 14, verifies the finite broom voting weights, and evaluates eight growing-broom rational cases. Successful execution reports `PASS`.

The universal theorem and its asymptotic consequences are proved in `RESULT.md`, not inferred from the finite tests. The scientific review covers correctness, originality and mathematical value; independent external validation has not been performed. The 2021 predecessor already contains a generic finite-temperature assignment reversal and general absorption equations; neither is presented as a new finding.
