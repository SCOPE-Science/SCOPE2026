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

The proof uses exact finite enumeration and algebra only. The parent probabilities are rational in the explicit witness, so every moment and correlation calculation can be checked without floating-point arithmetic.

Run `python verify.py`. The script enumerates all \(27\) ordered triples, reconstructs \(\mathbb E[L]\), \(\mathbb E[U]\), \(\mathbb E[L^2]\), \(\mathbb E[U^2]\), and \(\mathbb E[LU]\), verifies the displayed rational formula at several rational values of \(s\), and checks the exact counterexample and derivative. Successful execution prints `VERIFY_OK`.

The verification establishes only the stated three-draw counterexample and formula along the symmetric probability family. It does not certify a global optimizer over all probability vectors.
