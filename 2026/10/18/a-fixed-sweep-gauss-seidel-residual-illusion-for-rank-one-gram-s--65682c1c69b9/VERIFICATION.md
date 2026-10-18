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

Reproduce the finite checks with `python3 verify.py` using a standard Python 3 installation (no third-party packages). The program carries out 42 small exact rational one-sweep recurrences, analytic constant identities, and 15 numerical comparisons at dimension 8192 spanning three positive values of the coupling and five fixed sweep counts. The final observed line is `ALL_CHECKS_PASSED`.

The mathematical infinite-dimensional limit is established in `RESULT.md` by recurrence, an explicit generating function and exponentially decaying tails; none of the finite experiments substitutes for that argument. The physical embedding is finite-dimensional and algebraic. Claims are restricted to real exact arithmetic, fixed coupling and fixed positive sweep count. Independent audit has not been performed.
