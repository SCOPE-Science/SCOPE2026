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

# Computational verification

Run with Python 3: `python verify.py`. The program generates run-two words directly, creates the required-edge multigraph, constructs the explicit first/last-equal-pair matching and shortest balancing paths, checks full multiplicity balance, extracts Eulerian cyclic hosts and verifies every required cyclic window and the exclusion of `000` and `111` for all \(3\le k\le18\).

It separately solves an unrestricted shortest-overlap assignment with a pure-Python Hungarian algorithm for \(3\le k\le11\), and enumerates **all** binary cyclic candidates shorter than the displayed optimum for \(3\le k\le5\). It prints:

`VERIFY_OK exact_Lucas_cycles_k=3..18 independent_assignment_k=3..11 exhaustive_hosts_k=3..5`

The independent matching routine verifies the finite min-cost comparison, while direct enumeration supplies exhaustive finite negative checks only for the stated lengths. The infinite result is proved in `RESULT.md`. No independent external scientific audit has been performed.
