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

# Reproducible checks

The exact proof is in `RESULT.md`. Execute `python3 check_carbonate.py` from a directory containing that standalone file, using the Python 3 standard library. The checker reports success after independently computing the discriminant at ten rational parameters, checking the exact double-root factorization, testing three rational curvature signs and pooling-bias directions, comparing 3,000 random second differences to the analytic second derivative, and checking four square-root onset comparisons.

The finite tests address arithmetic implementation and examples, not the universal existence/uniqueness statements. Those rely on explicit positive factors, the cubic discriminant, real-root counting, and Jensen's inequality in the proof. The idealized carbonate-only restriction and the historical literature-access risk remain. An independent scientific audit has not been performed.
