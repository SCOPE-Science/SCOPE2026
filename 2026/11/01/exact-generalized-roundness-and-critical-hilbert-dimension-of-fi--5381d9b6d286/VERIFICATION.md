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

# Verification and reproduction

Run `python3 check_projective_negative_type.py` using Python 3.11 or later. It requires only the standard library. The checker constructs normalized homogeneous coordinates for \(\operatorname{PG}(2,q)\) with \(q\in\{2,3,4,5,7\}\), including the extension field \(\mathbb F_4\). It proves the incidence identity \(BB^\mathsf T=qI+J\) by integer enumeration for these examples, independently recomputes every shortest-path distance by breadth-first search, uses 65-digit `Decimal` arithmetic to bracket the scalar root, and tests the remaining eigenvalue signs and a critical equality-vector identity.

The expected terminal line is `ALL_PROJECTIVE_NEGATIVE_TYPE_CHECKS_OK`. Successful execution was observed on the complete packaged script, with all five fields and all \(19{,}476\) ordered-pair distances checked.

The all-order theorem is an analytic consequence of the projective-plane incidence identity; the computer checks neither enumerate non-Desarguesian planes nor establish claims about nonexistent orders. Values of the real root and asymptotic remainders are not independently interval-certified beyond the checked examples. No external independent scientific audit was performed.
