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

The accompanying `verify_capacity_cycle.py` uses only the Python standard library and independently enumerates all graph bipartitions and their permissible spanning subgraphs for paths and cycles of lengths three through nine. It checks exact coefficient formulas, recurrence implications, and finite-size asymptotic moment behavior: 77 assertions pass under `python verify_capacity_cycle.py`.

Critical infinite results instead follow from the tiling bijection, cycle-rooting double count, dominant-root analyticity, and characteristic-function argument in RESULT.md. Numerical checks do not verify arbitrary graph sizes or publication priority. The univariate sequence is known in OEIS A099925; no independent audit has been performed.
