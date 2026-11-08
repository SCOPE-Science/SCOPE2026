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

Run `python3 verify.py` with Python 3 and no nonstandard packages. A clean execution of the embedded checker reports `VERIFY_OK 498`. It tests the exact rational spectrum/eigenvectors and budget identities for integer sizes 3 through 16 and several prices, including the critical boundary. It also tests the even/odd trace identities on additional nonsymmetric rational weight matrices.

All tests are finite. The all-size global upper bound, equality-case rigidity and optimizer classification require the analytic proof in `RESULT.md`; they are not inferred from enumeration. Independent mathematical audit is not performed.
