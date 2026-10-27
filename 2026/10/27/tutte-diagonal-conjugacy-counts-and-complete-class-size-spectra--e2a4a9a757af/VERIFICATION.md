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

# Verification and limits
The included `verify.py` constructs the literal finite-field unit multiplication and loops over all possible group-element pairs to determine centralizer orders. It independently evaluates the flat/contraction version of the formula and the Tutte subset expansion. Assertions check that the class-size profile sums to the total group order and that all three computations agree. Eleven loopless/empty-edge configurations and three loop-enhanced cases are tested, over fields of orders 2, 3, and 4.

Command: `python3 verify.py`

Expected final output: `VERIFY_OK_QUIVER_UNIT_GROUP_CONJUGACY`

The test is finite: it does not exhaust all graphs, fields, or dimensions, and it is not a substitute for the proof of the universal statements in `RESULT.md`.
