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

Reproduction: run `python3 verify.py` with Python 3's standard library. The script expands both characteristic polynomials over exact rational coefficients and verifies the rational upper/lower bounds used for the Schatten-1 comparison. The Euclidean ratio is exactly \(\exp((4\sqrt5-8)/5)>1\), and positive definiteness follows from \(4/5<1\). Decimal output is illustrative; the strict nuclear-norm inequality is certified by rational arithmetic.

Limits: this package gives one mathematical counterexample. It contains no empirical financial-data analysis, independent audit, or external validation. No independent-audit evidence is claimed.
