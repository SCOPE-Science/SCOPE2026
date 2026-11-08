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

# Verification of the sharp lottery risk frontier

The proof's necessary inequality follows exactly from \(\mathbb E Z=cq\), the integer omitted-count bound under a cap, and the distinction between overbudget and non-overbudget outcomes. Its sufficiency uses a three-type distribution and uniform cyclic omission blocks, verifying all individual marginals rather than only their sum. The integer-cost case is treated separately.

The included `verification/verify_frontier.py` executed successfully on the delivered copy: `PASS: 2940 exact-fraction construction checks and 420 independent full-distribution LP comparisons.` The exact tests cover integer and noninteger exceptional costs, multiple project counts, boundary and interior caps, several inclusion marginals, and both attainable and unattainable cases. The LP checks enumerate every labeled subset and enforce the BB1 and cost-cap predicates independently. SciPy is optional for LP tests, while exact rational construction tests need only the Python standard library.

These are finite checks only; the proof covers all real parameters in the stated domain. No external independent audit or human proof verification is claimed. Possible equivalent published formulas remain a priority limitation.
