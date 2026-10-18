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

# Verification instructions and boundaries

Run `python3 verify_structural.py` and `python3 verify_masks.py` from the directory containing the two code files. Both require Python 3.9 or later and only the standard library. The supplied `.out` files record their observed outputs; each program asserts its expected results before printing `VERIFY_OK`.

The first program checks all 84 left-region candidate triples in the five-column grid, the exact 13 successes, their bounded histories that fill three complete columns in at most five rounds without filling any vertex in the fourth column, and the 13-vertex exchange graph's connectivity, edges, radius and diameter. It also enumerates every size-three set on grid lengths 3 through 12. The second program uses a separate row-major bit mask representation to enumerate all size-one, size-two and size-three sets on lengths 3 through 10 and independently reconstructs adjacency and breadth-first distances.

Both finite programs are exhaustive within their stated ranges, but neither constitutes an exhaustive examination of infinitely many grid lengths. For the all-length result the proof uses: (i) a local first-force dichotomy excluding non-end seeds, (ii) monotonicity under restriction to a five-column prefix, (iii) the complete finite boundary table, and (iv) propagation from a fully blue column. These are the mathematical links needed beyond computation.

The package makes no assertion of independent external audit or validation.
