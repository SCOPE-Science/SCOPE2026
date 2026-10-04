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

Run `python3 verify.py` in the same directory. The script uses only the Python standard library. It constructs the displayed triangle from exact rational data, encloses every square root and positive tenth root by rational intervals certified through integer-power inequalities, and evaluates the exponent \(21/10\) without accepting floating-point signs.

Expected final line: `CERTIFIED_NEGATIVE`. The script additionally certifies the strictly negative normalized limit for the one-parameter slender family. Decimal displays are informative only; all assertions are made on exact `Fraction` endpoints.

Limits: this certificate proves the explicit endpoint counterexample and the sign of the displayed asymptotic limit. It does not search for an optimal exponent, and it is not an exhaustive computation over all triangles.
