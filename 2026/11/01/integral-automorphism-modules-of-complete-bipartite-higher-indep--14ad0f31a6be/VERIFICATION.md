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

# Reproduction instructions

Run `python check.py` with Python 3 and SymPy. The program directly enumerates faces in 96 bipartite higher-independence cases, computes the signed reduced Lefschetz character on 1,512 permutation instances including balanced exchanges, and calculates 30 integral Smith normal forms for the asserted coinvariant groups. The completed check returned:

`PASS {'parameter_cases': 96, 'signed_lefschetz': 1512, 'rank_checks': 96, 'integral_smith_tests': 30}`

The general proof is in `RESULT.md`. Specifically, recheck the relative pair exact sequence, primitivity of the two inclusion sublattices, and the application of the degree-one Shapiro isomorphism in the coinvariant calculation. Finite tests are not exhaustive over all parameters and are not evidence of novelty. No independent external audit or validation is claimed.
