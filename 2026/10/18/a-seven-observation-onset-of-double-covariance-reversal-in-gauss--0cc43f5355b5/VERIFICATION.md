---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of short-window covariance positivity

Run `python3 verify_gaussian.py` using the Python 3 standard library. The program constructs the centered covariance columns by exact integer coefficient counts, verifies the five polynomial factorizations by convolution, and checks the stated Bernstein minima by exact rational arithmetic. The analytic proof in `RESULT.md` explains why these identities imply positivity over the entire correlation interval for each of the five dimensions. The larger-window sign pattern used to infer sharpness is a cited result, not a conclusion of the verifier.
