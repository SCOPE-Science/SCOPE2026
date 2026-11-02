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

# Verification of the exact arithmetic proof

The core finite checkpoints are \(L_{13}=521\), \(L_{24}=103682\), \(L_{25}=167761\), and the legal summand-count profile \((4,3,4,2,3)\) for the five offsets \((23,25,27,29,31)\). Together with the Lucas recurrence and published uniqueness of legal decomposition, these establish the theorem for all indices congruent to \(13\) modulo \(24\).

`verify.py` is a standalone exact-integer reproduction of recurrence boundary checks, legal-decomposition constraints, and sample progressions. Its finite output is corroborative only; the recurrence proof establishes the infinite statement. Historical priority and independent verification are not certified.
