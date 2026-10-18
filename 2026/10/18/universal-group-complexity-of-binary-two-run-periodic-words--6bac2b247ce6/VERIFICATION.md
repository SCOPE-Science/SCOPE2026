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

The complete analytical proof is in `RESULT.md`. To replay finite checks, run `python3 verify.py` using a standard Python 3 interpreter. The script constructs factors directly from the periodic word and computes ambient word orbits under explicit permutation generators. It tests periods 2 through 12 with all lengths from 1 through three periods plus two, and all attainable targets; it also tests the six subgroups of the three-coordinate symmetric group against both run lengths 2 through 8.

The observed output is embedded as `verification_output.txt`. These finite tests support implementation details, subgroup counts, and boundary cases only; the theorem for all positive integer parameters rests on the symbolic proof. No independent audit has been undertaken.
