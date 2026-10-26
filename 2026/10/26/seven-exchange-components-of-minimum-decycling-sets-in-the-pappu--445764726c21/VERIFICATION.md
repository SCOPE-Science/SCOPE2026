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

# Reproducible finite checks

This package uses exact integer and finite-set operations. No third-party modules, random trials, sampling, or timeouts are required for the stated certificate.

Run:

```sh
python3 verification/lcf_check.py --check-certificate verification/complete_certificate.json
python3 verification/incidence_check.py --check-certificate verification/complete_certificate.json
```

The first checker constructs the graph from the stated LCF sequence and tests acyclicity with disjoint-set union. The second checker independently constructs the Pappus nine-point/nine-line incidence graph and tests acyclicity by leaf peeling. The latter also verifies an explicit eighteen-vertex isomorphism onto the LCF graph. Both test all 8568 five-vertex subsets and all legal single-vertex replacements. Both check their reconstructed complete vertex and edge lists against the enumerated certificate, and independently compute all shortest-path distances.

Reproduced facts: the graph has 18 vertices and 27 edges; the minimum decycling cardinality is 5 by the proved degree-count bound; 252 five-sets are decycling; the exchange graph has 630 edges, every state has degree 5, and there are six complete six-vertex components plus one connected 216-vertex component with 540 edges. The 216-state component has radius 6 and diameter 7, with 108 states in each eccentricity class and 108 unordered diameter pairs. The exhibited automorphism subgroup has 216 elements and orbits of sizes 36,108,108.

The certificate includes all 252 state masks and all 630 exchange edges indexed by the sorted state list. This is a complete finite certificate for the precise labeled graph and replacement rule. The checkers are ordinary mathematical programs, not independently issued proof certificates. They do not establish any generalization to other graphs or the absence of prior published equivalent results.
