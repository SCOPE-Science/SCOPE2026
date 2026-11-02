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

Exact algebra in `verify_symbolic.py` derives the genus-five Cartier coefficient matrix and proves the determinant identity in the polynomial ring over \(\mathbb F_7\). It also checks the decisive \(4\times4\) minor and relevant boundary identities. The geometric proof in `RESULT.md` separately handles irreducibility, the smooth parameter locus, local cusp normal form and transversality.

The independent standard-library `verify_primefield.py` enumerates all \(343\) coefficient triples over \(\mathbb F_7\), checks squarefreeness by polynomial gcd, recomputes the Cartier matrix from a different multiplication implementation, and compares its rank with the theorem's classification. Both programs ran successfully and produced the exact success markers documented in `RESULT.md`. Finite-field enumeration is not an exhaustive check of all algebraically closed parameters and supplies no independent mathematical audit. No statement about the Jacobian \(7\)-rank is verified or claimed.
