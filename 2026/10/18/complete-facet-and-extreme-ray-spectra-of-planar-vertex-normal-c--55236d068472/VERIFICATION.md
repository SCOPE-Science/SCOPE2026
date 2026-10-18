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

# Reproducibility

Execute `python3 verify.py` from the directory containing the attached source. It uses only the Python 3 standard library. The program enumerates every proposed positive-circuit generator for the regular normal grid in each dimension from 3 through 12, checks the combinatorial formulas, reconstructs the closed polygonal chain, checks every defining nonlocal support inequality, verifies exact-coordinate facet transfer witnesses up to floating-point roundoff, and checks the active-constraint ranks needed for an extreme ray.

The completed execution returned ten passing dimensional cases, 1,480 ray rank checks and 150 facet witness checks; no assertion failed. A checker's finite successful run does not prove a formula for arbitrary dimension. The separate mathematical proof establishes the unlimited result, and numerical rank thresholds can misbehave in substantially larger test instances.

# Verification state

The proof and its limitations received self-review. An independent audit has not been performed. No separate machine-checked proof, external certificate, or expert validation is claimed.
