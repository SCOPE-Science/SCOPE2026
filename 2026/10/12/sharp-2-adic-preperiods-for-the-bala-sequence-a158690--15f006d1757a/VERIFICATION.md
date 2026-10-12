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

Run `python verification/verify.py` in the directory containing `verification`; no external dependencies are required. The verifier independently evaluates integer coefficients by formal EGF convolution and by a Stirling transform; it checks the first OEIS values. It exhausts residue classes for the finite forward-difference identities used in the infinite proof and tests the sharp obstruction and periodic tail for moduli from \(2^2\) through \(2^{12}\).

The certificate checks are exact integers without floating point. The proof, not a finite scan, establishes the theorem for every \(e\ge2\); the certificate does not establish originality or rule out inaccessible literature. `verification/output.txt` holds actual checker output from this package.
