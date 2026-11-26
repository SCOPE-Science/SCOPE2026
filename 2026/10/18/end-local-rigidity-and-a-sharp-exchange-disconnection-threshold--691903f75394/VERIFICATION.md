---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification instructions and boundaries

Run `python3 verify_local_boundary.py`, `python3 verify_structural.py` and `python3 verify_masks.py` from the directory containing the code files. They require Python 3.9 or later and only the standard library. The `.out` files record observed outputs from the latter two programs; each program asserts its expected results before printing `VERIFY_OK`.

The first program checks all 84 left-region candidate triples in the five-column grid, the exact 13 successes, their bounded histories that fill three complete columns in at most five rounds without filling any vertex in the fourth column, and the 13-vertex exchange graph's connectivity, edges, radius and diameter. It also enumerates every size-three set on grid lengths 3 through 12. The second program uses a separate row-major bit mask representation to enumerate all size-one, size-two and size-three sets on lengths 3 through 10 and independently reconstructs adjacency and breadth-first distances.

The local boundary checker establishes the stronger test needed for width transfer: all 71 rejected triples reach a closed configuration with every vertex in column 4 still white. The neighbor sets of their blue sources do not change when extending the grid. For a successful triple the first three columns are filled before column 3 is touched, and ordinary column propagation finishes the longer grid. These local facts and the first-force dichotomy, not a finite list of successful widths, establish the all-length statement.

The package makes no assertion of independent external audit or validation.
