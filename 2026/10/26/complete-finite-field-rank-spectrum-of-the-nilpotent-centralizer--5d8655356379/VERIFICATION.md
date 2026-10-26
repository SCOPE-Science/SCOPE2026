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

# Verification evidence

`python3 verify.py` ran using Python 3 standard library only and printed `VERIFY_OK_CONSECUTIVE_JORDAN_RANK_SPECTRUM`. The verifier builds actual matrices in the regular representations \(R_m\oplus R_{m-1}\), not merely matrices in the reduced \(2\times2\) model. It independently computes finite-field Gaussian-elimination ranks, checks the regularity condition, directly checks commutation with the fixed nilpotent matrix and nilpotence for the stated sample/all-small cases, and compares coefficient-by-coefficient with the analytic recurrences.

Observed rank histograms \((r:\text{count})\):

- \((m,q)=(2,2)\): \((0:1),(1:5),(2:2)\).
- \((3,2)\): \((0:1),(1:9),(2:46),(3:40),(4:32)\).
- \((4,2)\): \((0:1),(1:9),(2:78),(3:392),(4:416),(5:640),(6:512)\).
- \((3,3)\): \((0:1),(1:32),(2:426),(3:756),(4:972)\).
- \((2,4)\): \((0:1),(1:27),(2:36)\).
- \((3,4)\): \((0:1),(1:75),(2:1908),(3:5184),(4:9216)\).

The comparison validates those finite settings only. The proof's infinite-parameter and arbitrary-prime-power claims rest on exact local-ring counting, not enumeration. No separate external audit was performed.
