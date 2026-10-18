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

The two executable source files use only Python's standard library. Reproduce their checks with `python3 verify_posets.py` and `python3 verify_generator.py`. The exhaustive primary script validates Catalan family sizes, directed counting signatures, complete within-signature isomorphisms, and resulting type counts for every size through ten. The independent generator script brute-forces all permutations through eight, explicitly tests 123-avoidance and recomputes palettes. Standard outputs from actual executions are provided. This proves a finite cutoff; no test extends to unbounded sizes.
