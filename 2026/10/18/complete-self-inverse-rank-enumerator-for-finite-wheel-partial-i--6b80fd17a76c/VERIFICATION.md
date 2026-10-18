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

## Scope and direct checks
The Python standard-library checker `wheel_self_inverse_checker.py` independently enumerates all partial involutions on each wheel vertex subset, tests every pairwise wheel distance and compares the complete rank vector against the formula. Invoking `python wheel_self_inverse_checker.py` succeeded for all rim lengths three through nine. The claimed theorem concerns all integers \(n\ge5\). The small checks also exercise the boundary cases where the wheel is complete or unusually small.

## Reproducibility and proof limits
The checker does not rely on the cyclic component classification to generate the involutions and gives a genuinely independent finite check. Its computation cannot establish the formula for unbounded \(n\); that follows from the written cyclic-run enumeration, automorphism-group decomposition and disjoint hub-case analysis. No external or independent audit has been performed.
