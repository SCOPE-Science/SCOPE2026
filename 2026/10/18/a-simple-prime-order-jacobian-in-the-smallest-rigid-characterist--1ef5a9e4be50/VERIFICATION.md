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

The executable `verify.py` uses only the Python 3 standard library. It first verifies that the five degree-\(2\) through degree-\(6\) polynomial moduli are irreducible over \(\mathbb F_5\), by trial division against every monic polynomial of degree at most half the target degree.

For each extension degree \(1\le n\le6\), the code enumerates all \(5^n\) field elements, both as possible \(y\)-coordinates of \(y^5-y\) and as possible \(x\)-coordinates of \(x^4+x^2+x\). Separately, it computes the absolute trace on basis elements and the trace-zero histogram. Both methods reproduce the same six rational-point counts; the unique point at infinity is included.

Newton's identities and the genus-six functional equation reconstruct the complete zeta numerator. Independent binary polynomial arithmetic performs the degree-\(12\) irreducibility criterion modulo \(2\), and integer trial division establishes that the Jacobian point count \(11731\) is prime. The final output is `VERIFY_OK`; the actual output is preserved in `certificate.txt`.

This is an exact finite certificate for a specified genus-six curve, not an asymptotic test, nor a proof of a family-wide statement. It does not certify geometric simplicity or any independent external audit.
