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

The exact analytical proof in RESULT.md determines the coefficients of all six top-versus-middle response margins and proves the global lower bounds for fewer voters and candidates. The independently written standalone script `verify.py` directly enumerates all nine possible terminal pairs of opponent ballots for each voter at both orbit states, computes polynomial probabilities from `(1-p)` and `p/2`, and evaluates each plurality-winner uniform lottery with exact rational arithmetic. It passed all six affine margin coefficient identities, checked both directions of the explicit rational cycle, and tested 27 further rational utility triples inside the theorem's open parameter box. The program has no external dependencies and can be run with `python verify.py`.

This computation does not enumerate all utility profiles, all electorates, or all candidate counts and does not establish uniqueness or new publication priority; those are not asserted. Independent scientific audit has not been conducted.
