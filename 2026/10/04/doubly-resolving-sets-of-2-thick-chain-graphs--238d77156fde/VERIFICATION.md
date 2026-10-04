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
# Verification

`verify.py` independently constructs canonical chain graphs from their class sizes. It enumerates every ordered 2-thick profile with at least two levels and total order at most \(12\). For every vertex subset it computes all-pairs shortest-path distances by breadth-first search and evaluates the literal doubly-resolving definition. It compares that result to the three structural conditions in RESULT.md.

The same replay independently expands the claimed inclusion-exclusion polynomial and compares every coefficient with the brute-force cardinality histogram. It also checks the stated formula for \(\psi(G)\) and the exact number of minimum doubly resolving sets.

Expected successful replay:

`VERIFY_OK profiles=71 subset_checks=200960 coefficient_checks=285 max_order=12`

This finite replay is a regression check for definitions, boundary cases, and counting. It does not certify the infinite theorem; the infinite claim is justified by the proof in RESULT.md. No external or independent audit has been performed.
