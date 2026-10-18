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

# Verification and limits

The formula was proved from the \(2\times2\) multiplication matrix, the valuation of its entry ideal, and the determinant valuation. The independently implemented `verify_jordan.py` constructs the regular-action matrices directly from monomial multiplication and compares their power ranks and partition histograms against the theorem. It verifies every radical element for the following prime-field configurations: \((q,m)=(2,2),\ldots,(2,7)\); \((3,2),\ldots,(3,5)\); \((5,2),(5,3)\); \((7,2)\). Each configuration checks \(q^{2m-1}\) elements. Every comparison succeeded, and the final program marker is `VERIFY_OK_ALL_JORDAN_VALUATIONS`.

The proof is valid over arbitrary fields; the standalone computer checks cover only prime fields, are finite, and are not independent mathematical certification. The literature comparison does not prove universal uniqueness. Independent audit has not been performed.
