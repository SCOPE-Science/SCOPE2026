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

The file `verify.py` implements a finite exhaustive check of the endpoint bound and the run-avoidance consequences. Reproduce with `python3 verify.py`. The companion `verify_output.txt` records actual output ending `VERIFY_OK`.

For each order 2 through 6, every labeled tournament is generated from independent orientations of all unordered vertex pairs. A breadth-first traversal of the powerset automaton cross the trailing-run recognizer visits every reachable pair of an endpoint subset and the final-run state for arbitrarily long words whose run lengths are below the order. Every generated transition checks that the endpoint set contains at least the predicted number of vertices and that it is nonempty. This is a finite-state exhaustion only for each checked order, not an infinite proof over all orders.

An independent deterministic transition generator and iterative partition refinement verify that the run-language automaton has exactly twice the order in states for orders 2 through 8. Direct word enumeration through length 12 is compared with the claimed generating-function recurrence. The analytic proof in `RESULT.md` establishes the general order and unbounded word-length statements. No external or independent validation was performed.
