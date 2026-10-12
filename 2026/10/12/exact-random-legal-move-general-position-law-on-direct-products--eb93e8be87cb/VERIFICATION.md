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

# Reproducible scientific checks
Run `python verify_random_greedy.py` with Python 3.10 or later, with only standard-library modules. The program constructs the adjacency matrix and computes shortest paths by breadth-first search on each finite graph. It constructs every forbidden triple directly from the distance equality, then recursively explores all feasible continuation states. For each reachable set it gives all currently legal next vertices equal probability, accumulates **exact rational** terminal-type probabilities, and compares with the theorem. The saved stdout is in `verification_output.txt`.

All six boards are checked exhaustively over reachable legal states; respectively 103, 212, 384, 477, 960, and 2306 states are recorded. The same code computes rational values for selected larger sizes, but these are demonstrations, not exhaustive general checks. The proof of the infinite formula, forced completion, and asymptotic behavior is in `RESULT.md`. No independent external audit has taken place.
