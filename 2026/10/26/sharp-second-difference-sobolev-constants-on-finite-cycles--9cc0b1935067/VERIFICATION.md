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

The analytical proof establishes every integer cycle size and both scalar fields. `verification/check_cycles.py` uses exact rational arithmetic to test the Green pseudoinverse identity, kernel monotonicity, block formula and exhaustive sign enumeration on specified finite ranges. Invoking `python verification/check_cycles.py` produced: `PASS: 2853 exact rational checks; all subsets tested for 3 <= n <= 13.` The checks certify these finite computations only; the all-order optimality depends on the published cycle-power edge-isoperimetric theorem cited in RESULT.md. Uniqueness of real extremizers and higher-difference orders are not addressed.
