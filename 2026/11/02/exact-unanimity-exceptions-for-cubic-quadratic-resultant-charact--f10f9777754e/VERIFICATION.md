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

Run `python verify_unanimity.py` with Python 3 and no dependencies. The script models both prime fields and quadratic field extensions, constructs every irreducible trace-zero quadratic, and checks each nonzero cubic constant for the complete exception table. It tests the exact resultant via modular arithmetic and compares all resultant characters. On the recorded run the last line was `VERIFY_OK fields=18 parameter_classes=572`; separate lines list all 18 fields and the number of uniform cases.

Proof-critical symbolic steps have also been reconstructed directly: resultant reduction; zero obstruction; signed-bias indicator identity; the cubic-character expansion; Jacobi-sum bound; and exhaustive list of field sizes surviving the bounds. The proof does not rely on extrapolating the finite tests. The Jacobi-sum magnitude identity is a standard theorem: a classical nonzero-character Gauss/Jacobi relation, independently documented in Berndt--Evans (1979, Theorem 2.2).

No independent review or external mathematical certification has been performed. The irreducible quadratics are restricted to trace zero, and the original cubic is restricted to \(X^3+c\) with \(c\ne0\).
