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

# Exact verification

The standalone file `CHECK.py` uses Python standard-library `Fraction` arithmetic to derive coefficients from the rational Schwarz function, verify the fourth-order symmetric-point subordination identity, and verify the exact signed Hankel determinant. Running `python3 CHECK.py` checks the rational arithmetic without relying on floating-point approximations. The global Schwarz-map property is proved by the finite Blaschke factorization, and the existence and membership of the analytic function follow from the parity-separated integral construction in `RESULT.md`. The program does not provide a new theorem about the sharp supremum, nor does it replace independent mathematical review.
