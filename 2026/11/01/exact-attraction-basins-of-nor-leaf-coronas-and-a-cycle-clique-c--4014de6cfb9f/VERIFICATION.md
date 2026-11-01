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

The proofs of the all-graph phase correspondence, exact predecessor fibers, finite transfer identity, and sharp crossover are in `RESULT.md`. The independent `verify_nor.py` and `verify_nor.cpp` implementations were executed from the bundled source files. The accompanying outputs reproduce the 75-graph/16,932-state Python check and the 1,099-graph/1,065,508-state C++ check. Direct cycle independent-set enumerations through size twelve agree with the trace formula; integer recurrence calculations through size fifty-nine agree with the exact crossover.

Finite enumeration checks only its stated ranges. The all-graph claims rest on the explicit symbolic proofs, not on extrapolation. The primal model is synchronous **open-neighborhood** NOR without self-input or loops. The literature comparison does not constitute external certification of novelty. An independent external mathematical audit has not been performed.
