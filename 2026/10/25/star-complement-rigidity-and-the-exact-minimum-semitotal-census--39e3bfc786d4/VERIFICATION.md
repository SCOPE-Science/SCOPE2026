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
# Reproducibility and scope of checks

The included `verify.py` implements the subdivision graph by explicitly constructing each original-to-subdivider edge; it checks that every outside vertex has a selected neighbor and every selected vertex has a **different** selected vertex at graph distance one or two. It does not invoke the proof's omission-pattern characterization when deciding whether a candidate is valid. It then enumerates candidate subsets until it reaches the smallest feasible size, extracts the exact original-side/subdivider-side occupancy profile, and compares these coefficients with the explicit trivariate polynomial. For the eight-cycle it additionally checks the total 30 and independence count two.

Execute using Python 3 standard library: `python3 verify.py`. Successful execution prints the nine verified parameter pairs; assertions raise an error upon any difference. Tested pairs: (2,2), (2,3), (2,4), (2,5), (2,6), (3,3), (3,4), (3,5), (4,4). All assertions passed at generation. The proof for all dimensions consists of the forced-subdivider bound, witness classification, counting, and gap argument in RESULT.md; a finite computation cannot certify an infinite statement.

Independent audit has not been performed. The referenced sources were compared for implication overlap; residual priority risk remains.
