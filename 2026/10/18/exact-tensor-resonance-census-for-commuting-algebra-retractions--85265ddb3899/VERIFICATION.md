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

# Verification

A complete algebraic proof is supplied in `RESULT.md`. The standalone checker `check_commuting_retractions.py` independently enumerates all dimension-two commuting idempotent tangent pairs over the prime fields of orders 2, 3 and 5. For each, it constructs the full linear constraints on quadratic corrections from idempotency and commutativity and performs finite-field Gaussian elimination, rather than using the semisimple-module proof. It finds 40, 76, and 184 tangent pairs and complete labelled-pair counts 868, 13612, and 562504. It also directly enumerates all 98 individual dimension-two binary algebra retractions and verifies the 868 commuting pairs from their actual composition law. The final checker signal is `ALL_SIMULTANEOUS_RETRACTION_CHECKS_PASSED`. Run `python3 check_commuting_retractions.py` from the directory containing the embedded file.

The finite experiments do not prove the formula over arbitrary extension fields, dimensions, or tuple lengths; that generality follows from the field-independent semisimple splitting and linear dimension calculation proved in `RESULT.md`. Originality is limited to the examined mathematical sources; historical priority is not independently certified.
