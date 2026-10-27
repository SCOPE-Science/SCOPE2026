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

# Reproduction and limits

Run `python3 windmill_majority_verify.py` with Python 3.10+ and no third-party dependencies. The script separately implements adjacency-list majority updating and triangle-sector updating, and checks that they agree for all states on \(K_1ee(rK_3)\) for \(r=1,2,3,4,5\). It checks exact fixed-point, two-cycle and minimal-preperiod counts; explicit sharpness witnesses to \(r=16\); and the count formula for selected larger values. `CHECKS.txt` contains the actual recorded output ending `ALL_CHECKS_PASSED`.

The analytic proof in RESULT.md, not this finite script, establishes the universal bounds, exact count and asymptotic. Primary-literature completeness and mathematical correctness have not been independently audited.
