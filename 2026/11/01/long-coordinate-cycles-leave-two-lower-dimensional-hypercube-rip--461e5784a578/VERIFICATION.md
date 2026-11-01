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
# Verification notes

The proof consists of an all-parameter cyclic-word weight bound, an explicit orbit compatibility table, and the dominated-vertex/contiguity collapse. The published ordinary homotopy theorem for lower-dimensional binary-cube Rips complexes supplies only the final sphere-count interpretation. The structural conclusion does not depend on numerically verified cases.

Run `python checker.py` to enumerate admissible cyclic word orbits and verify every orbit adjacency and dominated-vertex inclusion for \(28\) parameter pairs. The expected output starts with `PASS 28 parameter instances, 648 admissible orbit vertices, 2448 orbit compatibility edges`.

Run `python lefcheck.py` (requires Python `networkx`) for an independent signed-simplicial-Lefschetz calculation in six small parameter pairs. Expected signed traces (equal to Euler characteristics of the geometric fixed spaces) are \(0\) for \((k,f)=(3,0)\) and \(2\) for the remaining five tested pairs. These checks are finite corroboration, not a substitute for Steps 1–5 of the proof. Both programs operate only on locally generated finite combinatorial objects, without remote data requests or external datasets.
