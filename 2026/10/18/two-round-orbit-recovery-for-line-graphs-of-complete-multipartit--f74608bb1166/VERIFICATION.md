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

# Verification of the two-round multipartite line-graph theorem

The general proof appears in `RESULT.md`. The following commands reproduce finite consistency checks using Python 3 from the package directory:

```text
python direct_check.py
python moment_check.py
python orbit_check.py
```

`direct_check.py` constructs every line-graph edge and adjacency explicitly in 114 test configurations; it performs synchronous refinement and compares zero-, one- and two-round equality relations with the mathematical type partition and the predicted exact depth. `moment_check.py` independently evaluates incident-edge moment sums by exact integer arithmetic, checks their closed formula, and verifies their separation of realized types in 3,424 size vectors. `orbit_check.py` uses NetworkX to enumerate all automorphisms for seven small line graphs and reconstruct their actual orbits without assuming the root-graph action has no extra automorphisms. Terminal outputs are reproduced in `direct_check_output.txt`, `moment_check_output.txt`, and `orbit_check_output.txt`.

The direct checker sums 4,558 vertices over its test inputs, the moment checker compares 481,572 unordered type-pair instances, and the automorphism checker includes the 23-vertex minimal obstruction. These checks do not certify the universal mathematical claim; the proof of equations (1)–(4) and the orbit-transitivity argument establish it. No independent mathematical audit or external certification has been performed.
