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

# Verification record

Run `python check_kernel.py` with dependencies from `requirements.txt`; `checker_output.txt` records a successful reproducible execution. Exact symbolic checks assert polynomial identity, antipodal factorization, quadratic angular coefficient and the limiting boundary identity. The numerical consistency checks independently sum 150 spherical-harmonic Gegenbauer terms at 12 real parameter points in dimensions 3, 4, 5 and 8; they test numerical values only. Additional high-precision numerical cubic-root tests span dimensions 3, 4, 5, 8, 12, 32, 128.

Infinite-dimensional and all-degree conclusions are justified in the written generating-function proof, not extrapolated from the finite checker. The sole critical historical-publication limitation is incomplete access to an older weighted harmonic Bergman kernel article; this does not alter the analytic proof of the new statement but warrants specialist priority comparison. Independent audit is not performed.
