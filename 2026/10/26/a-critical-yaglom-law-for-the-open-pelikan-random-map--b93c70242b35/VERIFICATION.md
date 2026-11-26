---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The standalone `check.py` may be run with Python 3 using `python check.py`. It recomputes finite-step transition coefficients using exact rational numbers, checks the first-return formula, and compares the predicted asymptotics at two interior opening parameters. Its recorded output is in `CHECK_OUTPUT.txt` and ends in `CHECKS_PASS`. These calculations check finite indices and do not prove the limiting theorem.

For the conditioned-time conclusion, the proof in `RESULT.md` takes the critical survival asymptotic from the cited survival theorem. It uses the resulting survival ratio and the exact cell recursion to obtain fixed-cell limits, then uses their normalization to justify convergence in total variation. No endpoint-uniformity or result for arbitrary interval initial laws is certified by the checks.
