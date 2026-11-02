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

# Verification of the circular-interval result

Run `python3 verify_cyclic_arcs.py` in this directory, alongside `SIX_VERTEX_WITNESS.json`.

The reproducible checks use only the Python standard library. The gap-partition minimax recursion and the unrelated bitset enumeration of explicit cyclic interval concepts agree for all 40 tested orders. An exact complete depth-four six-vertex tree is replayed against actual membership masks, and the forced balanced-branch obstruction rules out depth five. The script checks concept counts, all ten first-occurrence thresholds, and the stated six-vertex entropy mismatch.

The recurrence is proved for every positive integer order. Numerical threshold assertions are confined to orders at most forty. No external independent audit has been conducted, and code agreement alone does not substitute for the structural proof.
