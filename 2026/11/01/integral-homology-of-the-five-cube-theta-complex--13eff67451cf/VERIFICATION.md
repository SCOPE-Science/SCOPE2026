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
# Exact verification certificate

The standalone standard-library Python file `verify_q5.py` reconstructs the mathematical input from first principles. It enumerates every independent subset of the \(32\) vertices of the five-cube, pairing only covering faces with the specified parity-first vertex order, then directs every edge of the nonempty-face Hasse diagram and proves acyclicity by a complete topological-sort pass.

Checks completed: \(254{,}475\) independent subsets including the empty face; \(127{,}231\) matching pairs; twelve critical nonempty faces in dimensions \(0,5,7\) with counts \(1,1,10\); \(1{,}844{,}864\) covering edges; all \(254{,}474\) nonempty faces processed by the acyclicity check. A clean `python -I verify_q5.py` replay exactly reproduced the recorded output, including the terminal marker `VERIFY_OK`.

The mathematical inference from acyclic matching to a reduced-cell CW model uses Forman's theorem. Because its cells have no consecutive positive dimensions, the integral cellular chain differential vanishes. Combinatorial Alexander duality and the integral universal coefficient theorem yield the dual theta result.

This certificate proves only the asserted homology conditional on the executable implementation and the stated classical theorems. The higher homotopy attaching maps remain undetermined, and no external independent audit has been performed.
