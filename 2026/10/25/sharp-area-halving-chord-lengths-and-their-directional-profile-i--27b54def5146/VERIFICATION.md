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

The accompanying `verify_halving.py` re-computes the half-area line by actual polygon clipping and binary search, rather than using the analytic chord profile to determine the line position. For each odd side count \(n\in\{3,5,7,9,11,13,19,31,51\}\), 37 sampled directions in the full fundamental sector were checked. Observed maximum absolute length error was below \(4\times10^{-13}\) for unit circumradius. The theorem is proved by the analytical sector and wedge-product argument in `RESULT.md`; finite numerical agreement does not certify a universal statement.

The asserted bibliographic distinction was assessed from public texts and scientific statement comparisons. The full 2022 Berele--Catoiu envelope paper could not be accessed during this check; no conclusion is claimed about uninspected portions. Independent audit is not performed.
