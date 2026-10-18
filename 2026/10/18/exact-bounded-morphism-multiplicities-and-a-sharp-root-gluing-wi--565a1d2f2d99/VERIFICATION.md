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

Run `python3 check_starlike.py` from the directory containing this file. The script has no third-party dependencies and directly checks finite rooted upsets without relying on the theoretical arm-count formula. It separately enumerates the local maps and their complete uncovered-arm distributions, then asserts agreement with the closed expressions. Successful execution prints `VERIFY_OK 319 rooted-frame exact checks; 319 independent complete defect-profile checks` followed by sample counts. These bounded computations validate finite cases, not the general combinatorial proof or the Poisson limit. The latter are established analytically in RESULT.md.
