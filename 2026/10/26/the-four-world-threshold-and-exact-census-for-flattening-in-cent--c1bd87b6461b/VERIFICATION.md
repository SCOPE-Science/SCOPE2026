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
Run `python3 check_selection.py` (Python 3 standard library). The program counts all 331776 policies, verifies each nested-set selection equation, independently counts ranked reductions, and determines relabelling classes. The finite enumeration is exhaustive for four worlds, and the mathematical reduction proves that no semantic policy is omitted. It also checks that all eight three-world policies satisfy the equation. This is not independent auditing; no external validation has been performed.
