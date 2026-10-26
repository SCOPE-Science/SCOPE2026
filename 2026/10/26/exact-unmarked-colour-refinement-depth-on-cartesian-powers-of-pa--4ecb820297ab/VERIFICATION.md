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

# Verification record

The all-parameter mathematical proof is in `RESULT.md`. The standalone checker `verify_grid_power.py` uses only the Python 3 standard library, independently builds ordinary Cartesian adjacency lists, and computes round-by-round counting-refinement signatures. It compares all intermediate partitions with exact nearest-boundary-distance histograms, checks sharp stabilization and orbit-class sizes, then uses a separately constructed weighted quotient as a second finite check.

Run with `python3 verify_grid_power.py` in a directory containing that file. The exact output is embedded in `verification_output.txt`:

```
FULL_GRAPH_CONFIGURATIONS=51
FULL_GRAPH_TOTAL_VERTICES=6902
WEIGHTED_QUOTIENT_CONFIGURATIONS=176
WEIGHTED_QUOTIENT_TOTAL_STATES=21655
ALL_TESTS_PASS
```

Full graph tests cover path sizes from \(2\) through \(17\), dimensions up to \(9\), and graphs with at most \(900\) vertices. Weighted quotient tests additionally cover path sizes through \(101\), dimensions up to \(100\), and large profile counts. These exact finite tests are not exhaustive over the infinitely many parameter values, and they do not certify originality. The proof, not the tests, establishes the universal result. Independent audit is unperformed.
