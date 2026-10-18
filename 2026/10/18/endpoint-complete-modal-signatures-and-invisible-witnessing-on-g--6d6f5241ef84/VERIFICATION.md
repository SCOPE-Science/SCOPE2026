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

# Reproducibility and limits

Run `python star_checker.py` with Python 3 and its standard library. The checker computes the complete 3-by-4 semantic-signature algebra from the indicated initial atomic values, verifies closure under \(\wedge,\vee,\to,\Box,\Diamond\), interprets twelve representatives through an independently written syntax-tree routine and compares representative formula values on two finite stars sharing endpoints.

The observed success marker is `GODEL_STAR_ENDPOINT_AND_12_SIGNATURES_OK`.

The infinite statements are verified mathematically in `RESULT.md`: every leaf formula takes one of three uniform roles, root modal extrema are therefore determined by endpoint infimum/supremum, and attaining endpoints is necessary and sufficient for witnessing. The actual non-witnessed model has rational leaves strictly between two rational interior endpoints and the witnessed comparison model adds the endpoint leaves. Their equality for **all** formula depths is an induction, not an extrapolation from finite tests. Since the root theories agree and every terminal leaf satisfies exactly the same set of formulas, even the two fixed models' local entailment relations coincide for arbitrarily large premise sets. Historical priority and arbitrary extensions of the language are not decided by the script.
