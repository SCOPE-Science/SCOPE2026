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

# Verification of the directed toroidal visibility formula

The included `verify.py` is a complete Python-standard-library executable; invoke `python3 verify.py` with no arguments. It constructs the arcs of the consistently oriented directed product from the coordinate definition, and checks pairwise directed geodesic avoidance in **two different ways**: (i) Boolean reachability in the non-wrapping displacement rectangle, and (ii) directed breadth-first search in the original graph with other selected vertices forbidden. Both use the exact global directed distance from coordinate increments.

The upper-bound certificate uses the proved observation that every selected set contains at most two vertices in each coordinate fibre. For width four it checks all 2,946 fibre-restricted vertex subsets of sizes six, seven and eight. Their size histogram is 2,040 / 816 / 90. For width five, since a selected set has at most eight vertices, it checks all 2,490 eight-vertex fibre-restricted subsets. Every one fails both independent path tests. Thus the exclusion is exhaustive **within the mathematically proven necessary class**, not sampling.

Explicit witnesses for widths four, five and six pass both tests. Inserting empty columns is a separately proved path-lifting argument for every greater width; finite checks through width thirty are supplementary only, not a replacement for the infinite proof.

Expected successful output:

```
BASE_WITNESSES_OK 4=5 5=7 6=8
EXHAUSTIVE_UPPER_OK 4 2946 [(6, 2040), (7, 816), (8, 90)]
EXHAUSTIVE_UPPER_OK 5 2490 [(8, 2490)]
CYCLE_EXTENSION_TEST_OK 6..30
VERIFY_OK
```

The executable does not certify historical novelty, arbitrary orientation cases, or independent mathematical review.
