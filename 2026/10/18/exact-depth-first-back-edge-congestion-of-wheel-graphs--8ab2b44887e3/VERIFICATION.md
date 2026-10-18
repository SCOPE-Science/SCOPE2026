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

# Verification checks and limits

The mathematical argument in `RESULT.md` establishes the formula for every integer \(n\ge4\). It handles every rooted ordered DFS tree, including trees with branches, and constructs an attaining path.

Run `python3 verify_wheel_klx.py` with Python 3 and no external dependencies. The program builds each wheel directly, enumerates all ordered DFS traversals at rim orders three through nine (2,380 total, of which 1,428 have branching), calculates the traversal contour, represents non-tree edges as arcs from the descendant's last contour occurrence to the next ancestor occurrence, and counts arcs crossing each reverse tree edge. Exact minima agree with \(\lceil n/2\rceil+1\) for each tested rim order. The explicit attaining paths are independently checked through rim order 500; star cuts are also checked.

Finite enumeration is not an exhaustive proof beyond the enumerated orders. The matching general upper and lower bounds are deductive. No independent audit has been performed.
