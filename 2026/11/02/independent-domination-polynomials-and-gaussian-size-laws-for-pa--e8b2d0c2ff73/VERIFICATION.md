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
# Verification details

The standalone Python 3 source `verify_path_clique.py` is embedded alongside this report. Executing it from a directory containing the source requires only `python3 verify_path_clique.py` and the Python standard library. Its independent graph bitmask predicate uses the exact adjacency relation for the direct product, not the run decomposition. It verifies 403,264 total graph subsets, across all the chosen cases with at most 18 vertices; separate local word enumeration and two-state transfer counting agree for 13 parameter pairs. It also confirms every computed minimum count and numerically brackets the dominant radii, mean slopes and variance slopes for \(q=3,4,5\). All checks passed in this package preparation.

The analytic Gaussian limit, all-parameter enumeration and strict variance positivity depend on the written arguments, not on the finite experiments or numerical differentiation. The limiting constants are implicitly defined via a simple positive transfer-matrix root; they are not claimed to have elementary closed forms. No independent mathematical audit has been carried out.
