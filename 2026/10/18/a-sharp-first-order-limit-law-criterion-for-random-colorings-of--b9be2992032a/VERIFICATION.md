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

The complete proof of the all-sentence limit-law criterion is in RESULT.md. The finite reproducer \(\texttt{verify.py}\) uses no external dependencies. Its final printed marker is \(\texttt{EQUIVALENCE_COLOR_LIMIT_LAW_VERIFY_OK}\).

Finite computations: enumerate every coloring for \((s,c)=(1,1),(2,2),(3,2),(3,3),(4,2)\); verify all exact-existence probabilities against \(1-(1-2^{-s}\binom{s}{j})^c\) and all multinomial block-profile multiplicities; check the adjacent-threshold identity for small integers; confirm selected critical probabilities are near \(1-e^{-1}\). The full theorem for arbitrary growing \(s_n,c_n\) is established deductively, not computationally.

Known boundaries: fair independent coloring, one equivalence relation, a single unary predicate, equal-size growing classes, number of classes growing, first-order logic only. No independent audit has been performed.
