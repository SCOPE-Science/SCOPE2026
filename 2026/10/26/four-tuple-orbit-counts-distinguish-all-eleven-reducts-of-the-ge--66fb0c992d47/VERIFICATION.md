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

# Verification notes

Run `python verify_orbit_profiles.py`. The script independently forms the elementary arc switch, arc converse, three-state rotation, graph-cut switch, and graph complement orbits from finite labelled edge arrays, without reusing the closed-form Burnside enumeration to generate the orbits. It checks all eleven actions at each \(n=1,2,3,4,5\), then tests pairwise distinctness of all eleven four-point values, failure of three-point separation, and the Stirling-transformed noninjective four-point counts.

The executed output, reproduced in `verification_output.txt`, ends with `ALL_DIRECT_ORBITS_PASS`. The verification independently enumerates finite configurations of up to five distinct vertices and does not establish the general formulas on arbitrarily many vertices. Infinite-arity correctness instead follows from the explicit finite group actions, Burnside averaging, quotient vector-space ranks, and equality-partition argument proved in `RESULT.md`. Nothing in these checks constitutes an independent external audit.
