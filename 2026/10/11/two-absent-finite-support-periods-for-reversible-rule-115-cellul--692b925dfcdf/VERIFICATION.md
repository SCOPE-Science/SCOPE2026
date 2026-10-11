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

# Exact verification record

Run `python3 verify.py` with standard Python 3. The verifier has no third-party dependencies. It recomputes every eligible temporal column for periods \(3\), \(6\), \(9\), and \(18\); checks both directions of reachability from the homogeneous temporal-background root; tests an independent bit-sieve traversal against unpruned candidate traversal; and compares rooted components after exact threefold temporal repetition.

Observed summary (columns, forward vertices, forward edges, reverse vertices, reverse edges, root-component vertices, root-component distinct column words):

- \(p=3\): (4, 4, 7, 9, 21, 3, 2).
- \(p=6\): (10, 46, 121, 45, 159, 27, 10).
- \(p=9\): (31, 40, 52, 63, 102, 3, 2).
- \(p=18\): (973, 5500, 8590, 8235, 17484, 27, 10).

The final printed line is `VERIFIED: no primitive finite-support period 9 or 18`. The code independently checks both the Wolfram rule's truth table and its polynomial representation, and checks two explicit finite-support low-period witnesses. The output is a finite-graph exact computation plus a mathematical reduction, not a brute-force census of spatial initial conditions or a proof about all larger temporal periods. No independent audit or validation has yet occurred.
