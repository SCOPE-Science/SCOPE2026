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

`verify.py` enumerates every nonempty subset of the sixteen edges of \(K_{4,4}\) and retains exactly those with row and column degrees at most \(2\). It then replays the fixed sixteen-edge toggle order, checks that every pair is a Hasse cover, constructs the full directed Hasse graph with matched covers reversed, and verifies acyclicity by topological sorting.

The verified counts are \(7342\) nonempty faces, \(3663\) matching pairs, one critical \(0\)-cell, fifteen critical \(5\)-cells, and \(37728\) Hasse covers. The topological sort visits all \(7342\) nodes. The independent mod-\(2\) boundary-rank calculation gives reduced Betti rank \(15\) only in degree \(5\), and the Euler characteristic is \(-14\).

The computation is finite and exhaustive for this explicitly labeled \(K_{4,4}\). No result for larger complete bipartite graphs is inferred from the experiment. The homotopy conclusion uses the verified acyclic matching and Forman's theorem; the homology calculation is only a cross-check.
