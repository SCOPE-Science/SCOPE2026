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

# Reproducible finite verification

Run `python3 verify_grid4_robust.py` using Python 3 standard library, with no optional dependencies or downloads. The program independently enumerates all 65,536 vertex subsets via both maximum-independent-set recurrence and direct independent-set marking with a subset-zeta sweep, then runs the full specified discrete-Morse matching for each parameter \(2\le k\le8\).

For every parameter it constructs the complete oriented Hasse graph, reverses matched incidences and checks complete acyclicity by topological sorting. It verifies one critical zero-cell and the stated critical cells in dimension \(2k-3\), and independently checks the reduced Euler characteristic. It logs all face totals, matching counts, incidence totals and face vectors. The actual recorded execution ends with `VERIFY_OK`. Total matched pairs by ascending parameter: 15, 299, 2363, 9591, 21603, 30251, 32511. Total directed incidences: 48, 1952, 21992, 114644, 305904, 469316, 518144.

All arithmetic is finite and exact; no Monte Carlo test, numeric tolerance, partial enumeration or unbounded-time extrapolation is used. The mathematical conclusion uses the standard acyclic-matching theorem to pass from the verified finite certificate to the claimed homotopy equivalence. The verifier does not provide independent human certification, does not prove anything about larger rectangular grids, and does not independently investigate the originality of the result.
