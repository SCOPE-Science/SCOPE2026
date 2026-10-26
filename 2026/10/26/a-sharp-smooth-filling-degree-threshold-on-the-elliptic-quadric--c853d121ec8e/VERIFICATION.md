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

With Python 3 and SymPy installed, execute `python verify.py`. It prints the five rational points, checks each lies on the displayed cubic, and prints the exact reduced Gröbner bases in the four affine charts. The result should be the unit polynomial in every chart, certifying geometric smoothness over the algebraic closure. `expected_output.txt` records the actual checked output. All computations are finite, exact, and self-contained; no enumeration is used to prove the quartic obstruction, which is established by the Picard argument in RESULT.md. No independent audit has been performed.
