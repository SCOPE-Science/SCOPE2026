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

The exact arithmetic verifier `verify.py` checks the defining update matrices, the four-variable covariance operator, the characteristic polynomial, the generating function, the critical pole coefficient, and the Schur polynomial identities. It also independently aggregates finitely many weighted update histories and compares the resulting squared errors against the moment recursion. Run `python3 -m pip install -r requirements.txt` then `python3 verify.py` in a directory containing both files.

The proof of the infinite-horizon dichotomy uses the Schur stability criterion for a cubic and an uncancelled generating-function pole; no finite enumeration establishes either conclusion. The result is not an independent audit or a claim of machine-formal verification.
