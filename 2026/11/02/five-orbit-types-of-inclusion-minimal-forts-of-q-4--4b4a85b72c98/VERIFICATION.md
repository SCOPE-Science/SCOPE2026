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
# Reproducibility and validation

Run `python3 verify.py` with Python 3.10 or newer. It requires no third-party packages. The expected successful output is:

`VERIFY_OK Q4_minimal_forts=348 sizes=4:28,6:32,8:288 aut_group=384 orbits=12,16,32,96,192 distinct_predicates_and_minimality_algorithms=agree`

Two mathematically equivalent yet independently implemented fort predicates compare graph-neighbor loops with bitset-neighbor intersections. Inclusion-minimality is evaluated both by a recurrence that searches all subforts and by directly iterating every proper nonempty submask. All subsets of the sixteen vertices are inspected, including the empty mask (excluded as a fort), and all \(384\) automorphisms are generated as distinct maps. All five representative sets are checked to be genuine inclusion-minimal forts; their pairwise disjoint orbits exhaust the full enumerated collection. The calculation tests the claimed finite graph exhaustively; it does not prove statements about other dimensions. The published aggregate total \(348\) is treated as prior knowledge, not an original result.
