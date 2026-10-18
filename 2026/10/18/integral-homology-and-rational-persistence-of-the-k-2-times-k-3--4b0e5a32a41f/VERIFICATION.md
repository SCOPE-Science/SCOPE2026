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

# Reproducibility and scope

Run the included executable `verify_forest.py` with Python 3.10 or later; it uses only the standard library. Compare its JSON output to the included `computed.json` (JSON-object equality, since key ordering may differ). The program fully enumerates all \(2^{18}=262144\) possible vertex subsets for each of five forest-degree stages, verifies an acyclic face-poset matching, constructs every relevant signed Morse differential, performs exact integer unit-pivot reductions, checks the entire simplicial boundary of lifted cycles, and proves rational inclusion ranks with maximal minors modulo two fixed primes.

The separate `verify_crosscheck.py` requires SymPy and uses another criterion for detecting induced forests, another vertex order and matching order, and SymPy's exact Smith normal forms. Compare its saved full stage-wise results with `crosscheck.txt`, noting that matching critical-cell counts differ because the matching orders differ but all integral Betti groups and f-vectors agree.

The main finite computation is exhaustive and includes source-domain and target-boundary checks, not merely finite experiments extrapolated to other graph orders. No full homotopy classification at forest degree two is claimed. The interval decomposition is rational only; integral persistence decomposition is not established. An independent outside audit has not been performed.
