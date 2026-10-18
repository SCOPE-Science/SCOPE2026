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

# Mathematical verification

The proof gives an exact equivalence between reflected base containment and two sets of support inequalities. It then minimizes an explicit two-variable linear program, including the corner and mixed intersection cases, and recovers all feasible translations at the optimum. This establishes the universal statements independently of finite tests.

Execute `python verify_cayley.py` with Python 3 standard library. It checks 1,320 positive-integer orthotope pairs in dimensions one through six. For each, it enumerates feasible vertices of the planar linear program independently of the closed formula and uses exact `fractions.Fraction` arithmetic. It then tests 46,200 signed support evaluations at vertices of the proposed full center fiber. The finite tests passed.

The script does not enumerate all directions in arbitrary convex bodies and does not certify an infinite family by exhaustion. No independent mathematical audit has been performed. Literature uniqueness beyond the inspected sources is not asserted.
