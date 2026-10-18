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
The result is proved analytically in `RESULT.md`; the exact-rational checker `verify.py` independently evaluates the polar-section integral for dimensions \(3\) through \(21\) and rational shape parameters. Run `python verify.py` using the Python standard library.

The general theorem is **not** inferred from a finite number of calculations. The checker only corroborates the formula and its derivatives in stated examples. Historical novelty is not independently certified.
