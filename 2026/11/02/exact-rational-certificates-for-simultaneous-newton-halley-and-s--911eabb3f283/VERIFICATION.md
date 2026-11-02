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

# Verification of the rational cycle certificates

Run `python3 verification/verify_q_cycles.py` from the package root; it depends on the Python 3 standard library only. The rational center/radius/derivative bounds are precisely those in `RESULT.md`; the program proves the displayed strict bounds by exact `Fraction` arithmetic and polynomial intervals. It additionally checks derivative identities by exact integer-polynomial arithmetic and the quartic discriminant using a fraction-free Sylvester determinant. It prints `VERIFIED` only after all assertions pass.

The analytic implication uses the mean-value theorem, cyclic strict image inclusion, Banach contraction, and complex holomorphic local attraction. Printed decimal approximations of interval derivative bounds are only diagnostic; all proof comparisons use exact rational numbers. The certificate does not prove that basins of the three methods overlap or establish global basin measures. No independent audit or external formal verification has been performed.
