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

# Reproducibility and scope

Run `python3 verify_cyclic_double.py` from the directory containing this file and the script. The verifier uses only the Python standard library. It independently constructs all tetrahedral facets using Gale evenness and disjoint polygon edges; these two enumerations agree for every \(5\leq n\leq24\). It then checks the graph structure, two parity-component descriptions where applicable, circle multiplicities and all 580 signed dihedral Lefschetz traces. The verifier passed in the included state.

These are exhaustive finite checks over the stated twenty parameter values, not a proof for unbounded \(n\). The universal proof is in RESULT.md. No independent audit has been performed, and no external certification is asserted.
