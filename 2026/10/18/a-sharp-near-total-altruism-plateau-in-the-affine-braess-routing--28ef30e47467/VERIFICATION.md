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

Run `python3 verification.py` with Python 3's standard library in the same directory. It prints `VERIFY_OK` if exact rational tests succeed. It verifies the five-edge route differences and social-cost polynomial, Wardrop best-response inequalities for all three paths at 71 rational penetration values in one concrete case, and the positive-parameter family for integers \(2\le n\le40\). The implementation uses `fractions.Fraction` throughout, avoiding floating-point thresholds. This finite replay does not replace the analytical result, prove global uniqueness, or establish originality. Aggregate-flow uniqueness follows from the established Yi–Wei Theorem 2 and its checked applicability. Independent audit has not been performed.
