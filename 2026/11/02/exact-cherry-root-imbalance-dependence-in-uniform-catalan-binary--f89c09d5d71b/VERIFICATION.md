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

# Verification scope

Run `python3 verification/verify.py` from the extracted artifact directory, using Python 3 standard library only. The exact script was run successfully and reported 71,631 checks, with complete Catalan shape enumeration for internal sizes 2–10 (16,796 shapes at size 10) and exact-rational split identities for sizes 2–100. Tests directly compare tree enumeration, conditional root-split regression, means, covariance, and variance with the analytic identities. Large-\(n\) asymptotics and uniqueness are not experimentally certified; their mathematical evidence consists of the coefficient-extraction and Stirling arguments presented in `RESULT.md`. No independent audit has been performed.
