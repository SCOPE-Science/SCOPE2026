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

# Verification details
The mathematical argument is fully stated in `RESULT.md`. The finite diagnostics in `verify_profile.py` are independent of special Python modules, use 2,000 interior parameter samples and seven displayed reference parameters, and check: the defining quadratic equation; unit inputs; both transformed-output corner identities; the exact radical value; signs, mass budget, and stationarity of the dual certificate; and continuity at the transition. The checker passed when executed from the actual package directory. The infinite interval is proved by algebraic identities and a global completing-square inequality, not interpolation of the samples.

A specialist should independently reconstruct the signed dual lower bound and confirm that the previously published sharp threshold applies at the endpoint. The arithmetic verifier does not certify publication priority or replace an independent audit.
