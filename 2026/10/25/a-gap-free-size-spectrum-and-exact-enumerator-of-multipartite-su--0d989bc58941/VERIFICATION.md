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

# Reproducibility

Run `python3 checker.py` (Python 3.10+, standard library). The exact finite tests independently enumerate all source subsets and all constraints on small relations, compare to an independent function enumeration for additional cases, enumerate all allowed permutations on smaller support profiles, and check the interval and coefficient formula for 37 multipartite profiles of order two through seven.

Observed output:

```
ALL_CHECKS_OK
multipartite_profiles= 37
forbidden_permutation_subprofiles= 1131
independent_powerset_repair_checks= 7
independent_function_assignment_checks= 35
example_(3,2,2)= [(4, 4), (5, 48), (6, 384), (7, 288)]
```

This verification is finite and does not certify arbitrary orders. The general derivation is contained in RESULT.md: finite-function bijectivity, maximal unused-part criterion, explicit shift permutation, rook inclusion-exclusion, and matching upper and lower interval bounds. The only computational dependencies are Python standard library modules `itertools`, `math`, and `collections`. No independent review has been undertaken.
