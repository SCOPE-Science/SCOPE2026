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

The theorem was checked by two independent routes: a symbolic argument proving strict normalized sumset growth followed by exact quotient-period counting, and a separately implemented finite enumerator.

Run `python monogenic_host_checker.py` without third-party libraries. It exhaustively calculates eventual subset-power index and period in all nonempty subsets of seventeen finite abelian groups (twelve cyclic groups of orders one through twelve and five specified products) and checks the general lower bound. For all equality cases with index greater than one, it verifies that the normalized generator subset has exactly two elements. It separately checks 121 cyclic constructions for every parameter pair between one and eleven. The required final line is `VERIFY_OK 17 groups`.

Small computations are not infinite proofs. The general claim is established by the five-step mathematical proof in RESULT.md. The historical-priority comparison is incomplete because the complete 2025 embedding article and 1975 commutative-representation article were unavailable; no independent scientific audit or formal machine proof was performed.
