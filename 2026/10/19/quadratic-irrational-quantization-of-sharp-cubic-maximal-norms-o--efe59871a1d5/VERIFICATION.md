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

Run `python3 checks/verify_cubic.py` with Python, SymPy, and SciPy. The script checks exact radicals, the mean-one extremizer proportion, both nonnegative slack-polynomial factorizations, the stationary derivative identity, and the exact Schur-complement curvature. It also maximizes the finite two-level quotient numerically on graph sizes 4, 5, 6, 7, 10, 30, 50, and 200. These finite tests do not prove an infinite statement. The accompanying mathematical proof supplies the general Jensen reduction, unique scalar optimum, uniform local asymptotics, and Diophantine subsequences. No independent audit has been performed.
