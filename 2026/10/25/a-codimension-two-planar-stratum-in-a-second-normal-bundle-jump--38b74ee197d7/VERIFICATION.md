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

# Verification and scope

Run `python3 verify.py` with Python 3's standard library. The script reconstructs the two asserted immersion minors for the explicit Cox tuple, proves their dehomogenized factors have unit polynomial gcd, and computes the exact rational rank of the relative cohomology matrix as 14 out of 16. Expected output: `VERIFY_OK: Cox regularity, two coprime immersion minors, 16x16 rank 14`.

No finite computation proves the arbitrary-map statements. The proof uses the rank-one incidence variety for dimension, the normal exact sequence inside the blown-up plane for splitting, and the relative cohomology isomorphism for the general rank-drop statement. Characteristic-zero restrictions apply. No independently assessed audit or external certification is claimed.
