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

To replay with Python 3 and no third-party packages, run `python3 verification/check.py` from the extracted package root. The verifier computes polynomial greatest common divisors over each finite field to test \(\gcd(f,X^{q^2}-X)=1\) independently of the character-sum proof, then checks the irreducibility criterion and elliptic count for every nonzero pair of parameters in the tested fields.

Actual observed output:

```text
VERIFY_OK fields [(3, 4, 24), (5, 16, 160), (7, 36, 504), (11, 100, 2200), (13, 144, 3744), (17, 256, 8704), (19, 324, 12312), (23, 484, 22264), (29, 784, 45472), (9, 64, 1152), (25, 576, 28800)] total_pairs 2788 irreducibility_checks 125336
```

This tests all nonzero parameter pairs in eleven finite fields, including \(\mathbb F_9\) and \(\mathbb F_{25}\). A later attempt to run a more expensive \(\mathbb F_{49}\) case exceeded its bounded computation time and produced no conclusion; it is not included as mathematical evidence. All universal statements depend on the written proof, not finite tests.

Independent mathematical audit: not performed.
