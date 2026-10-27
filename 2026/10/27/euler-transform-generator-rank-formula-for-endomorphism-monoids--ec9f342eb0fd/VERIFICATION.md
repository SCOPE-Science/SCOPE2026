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

# Verification scope

The package includes `checker.py` and its recorded standard output `checker_output.txt`. Run it with `python3 checker.py` in the directory containing those two files. It uses only the Python 3 standard library. It computes permutations, permissible pairs and their conjugacy orbits directly for small \(n\); it enumerates all eligible rank-three square-root lifts for essential rank-two orbits, and separately implements formal power-series and Euler-transform recurrences.

The explicit assertions cover \(2\le n\le5\) for direct conjugacy (the general theorem begins at \(n=5\)) and exact coefficient calculations through \(n=12\). This is corroborating finite arithmetic, not an exhaustive argument for every \(n\). The general result follows from the fiber decomposition, lift criterion, and published rank-reduction theorem given in `RESULT.md`. No independent audit has been undertaken.
