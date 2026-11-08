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

The proof is an exact symbolic parameterization, with no dependence on experimental extrapolation. To replay, run `python3 verify.py` using standard-library Python. The enumerator covers all denominator/matrix pairs with row sum \(Q\in\{1,\dots,12\}\), computes every feasible nonnegative integer six-permutation coefficient vector, and compares the smallest support to the endpoint formula. The script reports 13,558 distinct denominator/matrix pairs, 67,790 assertions, and a sharp five-term example. The infinite/real-input assertion follows from the analytic proof in RESULT.md, not the finite enumeration. No independent audit, external validation, or machine formalization has been performed.
