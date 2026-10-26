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

The accompanying `check.py` exactly verifies the finite conditional probabilities sum to one, the two rational expressions for the variance and derivative, and the root interval and derivative sign calculations. The all-positive-\(m\) proof uses the exact quadratic factorization and sign changes. Root decimals are illustrative. For arbitrary two-destination positive masses and ordered distinct distances, the written monotonicity argument gives the universal one-turn upper bound; no finite enumeration is relied upon for that bound.

Install SymPy using `requirements.txt`, then run `python check.py` in a directory containing both files. This reproduces only the mathematical identities and does not establish historical originality or empirical model validity.
