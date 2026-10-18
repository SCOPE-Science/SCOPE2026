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

# Reproduction and mathematical limits

Execute the included standalone standard-library program using `python3 verify.py`. It builds inversion subsets independently of the parity-check construction and searches the full difference-state space for \(n=3,4,5\). It then verifies explicit constructive linear solutions for all differences at those orders, all binary fillings of missing entries in the prescribed lower-bound witness, and 32 reproducible random differences at each order from 6 through 32. It separately checks general 2-factor-deleted bicliques by enumerating derangements: all such permutations up to \(n=7\), 200 at \(n=8\), with three target patterns per case.

Observed BFS results for cyclic deletions: \(n=3\), 3 remaining edges, diameter 1, distance counts \([1,7]\); \(n=4\), 8 remaining edges, diameter 2, counts \([1,89,166]\); \(n=5\), 15 remaining edges, diameter 3, counts \([1,591,21106,11070]\). Checks of the general two-factor family include 2 derangements at order 3, 9 at 4, 44 at 5, 265 at 6, 1854 at 7, and a 200-case sample at 8. The program exited successfully with `ALL_VERIFICATION_CHECKS_PASSED`.

The infinite-family correctness relies on the written proof, not extrapolation of these finite computations. The claim does not cover graphs whose missing-edge subgraph is not a spanning 2-factor, and does not assert exactness for every co-two-factor. Literature searches are not a universal proof of novelty; independent audit has not been performed.
