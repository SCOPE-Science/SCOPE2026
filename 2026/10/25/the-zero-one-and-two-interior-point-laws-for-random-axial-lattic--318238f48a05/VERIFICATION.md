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
Run `python3 verify.py` with a standard-library Python 3 interpreter. The verifier recomputes the rational Euler-factor ratios exactly, checks all low-interior normalized gcd types against direct triple-positive-solution enumeration for the entire box from 1 through 25, and checks two rational density coefficients. Expected output ends with `VERIFY_OK`. The finite certificate supports the algebra but is not a proof of the unbounded statistical limits. The mathematical argument for the limits is the explicit CRT plus uniform tail estimate in RESULT.md. This package reports self-review only; an independent audit has not been performed.
