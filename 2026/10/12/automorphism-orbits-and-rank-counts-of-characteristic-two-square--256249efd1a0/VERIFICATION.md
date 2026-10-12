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

Run `python3 verify.py` in the same directory. The script requires only Python's standard library. It computes the orbit-stabilizer coefficients directly using finite general linear group orders, then independently enumerates every algebra homomorphism and tests composition-idempotence and linear rank for \(\mathbb F_2\) with \(n=1,2,3\). It also enumerates the \(\mathbb F_4\), \(n=2\) case using explicit arithmetic in \(\mathbb F_2[z]/(z^2+z+1)\). The expected output includes `VERIFY_OK`.

The checks are finite cross-validations. The mathematical proof supplies the all-dimension and all-even-field statement; it is not inferred from enumeration. The proof requires only the Frobenius identity, the local Nakayama lemma, explicit conjugacy, and orbit-stabilizer. No external audit or independent certification has been performed.
