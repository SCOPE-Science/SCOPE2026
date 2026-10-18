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

## Reproducible checks

Use Python >=3.10 and NetworkX 3.6.1. Run `python verify_degree_profiles.py` and `python verify_witness.py`. The first independently generates all finite poset isomorphism types on 1 through 8 elements by adjoining a maximal point over an ideal. It then enumerates every order ideal of each type, computes the exact global strict-lower/strict-upper degree histogram, and groups all signatures (not only signatures of equal-sized posets). The run asserts the 19,449 representatives, 19,448 signatures, unique colliding pair, and 18-point witness size. The second independently enumerates the two witness lattices from combinations, checks the common 18-entry signature and height distinction, and verifies equality at colour-refinement round one but not round two. Both printed outputs are embedded alongside the programs.

## Limits

The statement is exhaustive only through eight join-irreducibles. The algorithms use integer-exact subset tests and an exact directed isomorphism predicate from NetworkX; they do not certify the provenance of earlier mathematical publications or provide an independent human audit. Random trials or numerical approximation are not part of the completeness proof.
